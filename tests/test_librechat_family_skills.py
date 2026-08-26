from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PROJECT_ROOT / "skills"

LIBRECHAT_FAMILY_SKILLS = {
    "citation-management",
    "convert-recipe",
    "create-recipe",
    "export-recipe",
    "grounded-citations",
    "imagegen",
    "literature-review",
    "manage-pantry",
    "meal-plan",
    "plant-care-pl",
    "product-research-pl",
    "scale-recipe",
    "shopping-list",
    "skill-creator",
    "task-prioritizer",
    "travel-agent",
}

FORBIDDEN_EXTERNAL_WORKFLOWS = {
    "parallel-cli",
    "OPENROUTER_API_KEY",
    "OPENAI_API_KEY",
    "NCBI_API_KEY",
    "$CODEX_HOME",
    "scripts/",
    "CookCLI",
    "nova-document",
    "pdf-report-creator",
    "claude-with-access-to-the-skill",
    "eval-viewer",
}

WEB_SEARCH_REFERENCE = re.compile(r"\bweb(?:[ _-])search\b", re.IGNORECASE)
WEB_SEARCH_PREREQUISITE = (
    "Before the first Web Search or `web_search` call, load the "
    "`web-search-querying` skill"
)


def load_skill(name: str) -> tuple[dict[str, object], str]:
    path = SKILLS_ROOT / name / "SKILL.md"
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise AssertionError(f"{name} does not start with YAML frontmatter")
    _, frontmatter_text, body = content.split("---", 2)
    frontmatter = yaml.safe_load(frontmatter_text)
    if not isinstance(frontmatter, dict):
        raise AssertionError(f"{name} frontmatter is not a mapping")
    return frontmatter, body


class LibreChatFamilySkillsTests(unittest.TestCase):
    def test_skills_are_flat_valid_and_bilingual(self) -> None:
        for name in sorted(LIBRECHAT_FAMILY_SKILLS):
            with self.subTest(skill=name):
                frontmatter, body = load_skill(name)
                self.assertEqual(frontmatter["name"], name)
                description = frontmatter["description"]
                if not isinstance(description, str):
                    self.fail(f"{name} description is not a string")
                self.assertTrue(description.strip())
                self.assertIn("use", description.lower())
                self.assertTrue(
                    "użyj" in description.lower() or "stosuj" in description.lower()
                )
                self.assertTrue(body.strip())

    def test_skills_do_not_require_upstream_cli_or_api_workflows(self) -> None:
        for name in sorted(LIBRECHAT_FAMILY_SKILLS):
            _, body = load_skill(name)
            for forbidden in FORBIDDEN_EXTERNAL_WORKFLOWS:
                with self.subTest(skill=name, forbidden=forbidden):
                    self.assertNotIn(forbidden, body)

    def test_web_searching_skills_load_query_guidance_before_searching(self) -> None:
        for path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            name = path.parent.name
            if name == "web-search-querying":
                continue
            content = path.read_text(encoding="utf-8")
            if not WEB_SEARCH_REFERENCE.search(content):
                continue
            _, body = load_skill(name)
            with self.subTest(skill=name):
                self.assertIn(WEB_SEARCH_PREREQUISITE, body)

    def test_librechat_specific_contracts_are_explicit(self) -> None:
        image_frontmatter, image_body = load_skill("imagegen")
        self.assertIn("Image Tools MCP", image_body)
        self.assertIn(
            "Image Tools MCP", str(image_frontmatter.get("compatibility", ""))
        )

        creator_frontmatter, creator_body = load_skill("skill-creator")
        self.assertIs(creator_frontmatter["disable-model-invocation"], True)
        self.assertIs(creator_frontmatter["user-invocable"], True)
        self.assertIn("fenced", creator_body.lower())
        self.assertIn("does not install", creator_body.lower())

        _, product_body = load_skill("product-research-pl")
        for required in ("Allegro", "Ceneo", "PLN", "Poland"):
            self.assertIn(required, product_body)

        _, plant_body = load_skill("plant-care-pl")
        for required in ("indoor", "garden", "poland"):
            self.assertIn(required, plant_body.lower())

        _, travel_body = load_skill("travel-agent")
        for required in ("children", "total budget", "backup"):
            self.assertIn(required, travel_body.lower())


if __name__ == "__main__":
    unittest.main()
