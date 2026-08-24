# Skills

A collection of specialized, portable instruction sets for AI agents. Each canonical skill encodes best practices, workflows, and domain knowledge for a focused task—from debugging and code review to game design and competitive analysis.

## Repository layout

`skills/` is the complete authoritative source of every skill. Each immediate skill directory contains its `SKILL.md` entry point and any supporting files.

The root-level `hermes/` and `librechat/` directories are committed generated outputs. Do not edit them by hand: `scripts/sync_harness_skills.py` recreates them from `skills/` and `harnesses.yaml`, removing stale generated files and outputs. Each generated directory carries a `.generated-by-sync-harness-skills` ownership marker.

## Setup and synchronization

Python 3.11 or newer is required.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/sync_harness_skills.py
```

Run the generator after changing a canonical skill or harness configuration. It is idempotent: unchanged generated trees are left in place.

Use read-only drift detection in CI or before committing:

```bash
python scripts/sync_harness_skills.py --check
```

`--check` exits with status 0 when generated outputs are current, 1 when drift exists, and 2 for invalid configuration, unsafe paths, or filesystem/source errors. Use another config in a test or local experiment with `--config path/to/harnesses.yaml`; relative paths are resolved from the repository root.

## Harness configuration

`harnesses.yaml` names each generated output and defines its selection. The initial configuration is:

```yaml
harnesses:
  hermes:
    exclude:
      - vikunja-board-poller
      - vikunja-task-executor
      - vikunja-task-refiner
  librechat:
    exclude:
      - vikunja-board-poller
      - vikunja-task-executor
      - vikunja-task-refiner
```

For a harness, omitted `include` starts with every canonical skill. A present `include` starts with exactly those skill-directory names; `include: []` selects no skills. `exclude` is then removed, so it wins when a name appears in both lists. Omitting both keys selects all skills.

Examples:

```yaml
harnesses:
  all-skills: {}                 # default: every canonical skill
  no-skills:
    include: []                  # explicit empty output
  selected:
    include: [safe-image-analysis]
  filtered:
    exclude: [vikunja-board-poller]
  include-then-exclude:
    include: [safe-image-analysis, vikunja-board-poller]
    exclude: [vikunja-board-poller]
```

To add a harness, add a lowercase kebab-case output name to `harnesses.yaml`, use exact immediate directory names from `skills/` in optional `include` and `exclude` lists, then run the synchronization command and commit both the configuration and generated output. The current `hermes` and `librechat` harnesses intentionally exclude `vikunja-board-poller`, `vikunja-task-executor`, and `vikunja-task-refiner` while retaining every other canonical skill.

## How to use a skill

1. Browse the canonical `skills/` directory or the generated tree for your harness.
2. Copy the required skill folder into the target agent's skill directory.
3. Load the folder's `SKILL.md` when the task needs that workflow.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

© 2026 dawidkulpa

## Disclaimer

Parts of this repository, including documentation and skill definitions, were generated or co-authored with AI tools. All content is reviewed and curated by the author.
