from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import shutil
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync_harness_skills.py"
SPEC = importlib.util.spec_from_file_location("sync_harness_skills", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT_PATH}")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)
PROJECT_ROOT = SCRIPT_PATH.parent.parent


class SyncHarnessSkillsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "skills").mkdir()
        for name in ("alpha", "beta", "gamma"):
            skill = self.root / "skills" / name
            skill.mkdir()
            (skill / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_config(self, text: str) -> None:
        (self.root / "harnesses.yaml").write_text(text, encoding="utf-8")

    def synchronize(self, check: bool = False) -> tuple[int, list[str]]:
        return sync.synchronize(self.root, check=check)

    def generated_skills(self, harness: str) -> set[str]:
        return {
            path.name
            for path in (self.root / harness).iterdir()
            if path.is_dir() and not path.is_symlink()
        }

    def test_default_all_and_empty_include(self) -> None:
        self.write_config("harnesses:\n  all: {}\n  empty:\n    include: []\n")

        exit_code, changed = self.synchronize()

        self.assertEqual((exit_code, changed), (0, ["all", "empty"]))
        self.assertEqual(self.generated_skills("all"), {"alpha", "beta", "gamma"})
        self.assertEqual(self.generated_skills("empty"), set())
        self.assertEqual(
            (self.root / "all" / sync.MARKER_NAME).read_text(encoding="utf-8"),
            sync.MARKER_CONTENT,
        )

    def test_include_exclude_and_exclude_wins(self) -> None:
        self.write_config(
            "harnesses:\n"
            "  included:\n"
            "    include: [alpha, gamma]\n"
            "  excluded:\n"
            "    exclude: [beta]\n"
            "  both:\n"
            "    include: [alpha, beta]\n"
            "    exclude: [beta]\n"
        )

        self.synchronize()

        self.assertEqual(self.generated_skills("included"), {"alpha", "gamma"})
        self.assertEqual(self.generated_skills("excluded"), {"alpha", "gamma"})
        self.assertEqual(self.generated_skills("both"), {"alpha"})

    def test_recursive_copy_preserves_executable_mode(self) -> None:
        nested = self.root / "skills" / "alpha" / "resources"
        nested.mkdir()
        executable = nested / "helper.sh"
        executable.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        executable.chmod(0o755)
        self.write_config("harnesses:\n  output:\n    include: [alpha]\n")

        self.synchronize()

        generated = self.root / "output" / "alpha" / "resources" / "helper.sh"
        self.assertEqual(generated.read_text(encoding="utf-8"), "#!/bin/sh\nexit 0\n")
        self.assertTrue(generated.stat().st_mode & 0o111)

    def test_invalid_config_shapes(self) -> None:
        invalid_documents = [
            "harnesses: [\n",
            "[]\n",
            "other: {}\n",
            "harnesses: {}\n",
            "harnesses: {}\nextra: true\n",
            "harnesses:\n  valid: []\n",
            "harnesses:\n  valid:\n    extra: []\n",
            "harnesses:\n  valid:\n    include: null\n",
            "harnesses:\n  valid:\n    exclude: [1]\n",
        ]
        for document in invalid_documents:
            with self.subTest(document=document):
                self.write_config(document)
                with self.assertRaises(sync.SyncError):
                    self.synchronize()

    def test_duplicate_yaml_keys_and_list_entries_are_rejected(self) -> None:
        self.write_config("harnesses:\n  one: {}\n  one: {}\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()

        self.write_config("harnesses:\n  one:\n    include: [alpha, alpha]\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()

        self.write_config("harnesses:\n  one:\n    exclude: [alpha, alpha]\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()

    def test_unknown_skills_and_unsafe_harness_names_are_rejected(self) -> None:
        self.write_config("harnesses:\n  one:\n    include: [unknown]\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()

        for name in ("../escape", "UPPER", "skills", "with.dot"):
            with self.subTest(name=name):
                self.write_config(f"harnesses:\n  {name}: {{}}\n")
                with self.assertRaises(sync.SyncError):
                    self.synchronize()

    def test_source_symlink_and_unmarked_or_symlinked_outputs_are_rejected(self) -> None:
        source_link = self.root / "skills" / "alpha" / "linked.md"
        source_link.symlink_to(self.root / "skills" / "alpha" / "SKILL.md")
        self.write_config("harnesses:\n  output: {}\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()
        source_link.unlink()

        output = self.root / "output"
        output.mkdir()
        self.write_config("harnesses:\n  output: {}\n")
        with self.assertRaises(sync.SyncError):
            self.synchronize()
        shutil.rmtree(output)

        output.symlink_to(self.root / "skills" / "alpha", target_is_directory=True)
        with self.assertRaises(sync.SyncError):
            self.synchronize()

    def test_source_skill_requires_regular_skill_markdown(self) -> None:
        (self.root / "skills" / "missing-skill-md").mkdir()
        self.write_config("harnesses:\n  output: {}\n")

        with self.assertRaises(sync.SyncError):
            self.synchronize()

    def test_prevalidation_prevents_partial_mutation(self) -> None:
        self.write_config(
            "harnesses:\n"
            "  valid:\n"
            "    include: [alpha]\n"
            "  invalid:\n"
            "    include: [missing]\n"
        )

        with self.assertRaises(sync.SyncError):
            self.synchronize()

        self.assertFalse((self.root / "valid").exists())
        self.assertFalse((self.root / "invalid").exists())

    def test_idempotence_and_stale_cleanup_for_removed_marked_harness(self) -> None:
        self.write_config("harnesses:\n  kept: {}\n  removed: {}\n")
        self.assertEqual(self.synchronize()[0], 0)
        kept = self.root / "kept"
        first_inode = kept.stat().st_ino

        self.assertEqual(self.synchronize(), (0, []))
        self.assertEqual(kept.stat().st_ino, first_inode)

        self.write_config("harnesses:\n  kept: {}\n")
        self.assertEqual(self.synchronize(), (0, ["removed"]))
        self.assertFalse((self.root / "removed").exists())

    def test_check_reports_drift_without_mutation(self) -> None:
        self.write_config("harnesses:\n  output: {}\n")
        self.synchronize()
        generated_skill = self.root / "output" / "alpha" / "SKILL.md"
        generated_skill.unlink()
        stderr = io.StringIO()

        with contextlib.redirect_stderr(stderr):
            self.assertEqual(self.synchronize(check=True), (1, ["output"]))

        self.assertIn("drift: output", stderr.getvalue())
        self.assertFalse(generated_skill.exists())

        self.assertEqual(self.synchronize(), (0, ["output"]))
        self.assertTrue(generated_skill.exists())

    def test_actual_vikunja_exclusions_are_configured_for_each_current_harness(self) -> None:
        inventory = sync.inventory_skills(PROJECT_ROOT)
        selections = sync._load_config(PROJECT_ROOT / "harnesses.yaml", inventory)
        excluded = {
            "vikunja-board-poller",
            "vikunja-task-executor",
            "vikunja-task-refiner",
        }

        self.assertEqual(set(selections), {"hermes", "librechat"})
        for harness in selections:
            self.assertFalse(excluded & set(selections[harness]))
            self.assertEqual(set(inventory) - set(selections[harness]), excluded)


if __name__ == "__main__":
    unittest.main()
