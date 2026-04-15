# Repo Backbone: Public Skills Repository

## TL;DR

> **Quick Summary**: Set up the structural backbone for `dawidkulpa/skills` — a public, author-curated GitHub repository for sharing AI agent skills. Create README.md, AGENTS.md, and an empty `skills/` directory.
> 
> **Deliverables**:
> - `skills/.gitkeep` — empty directory structure for future skills
> - `AGENTS.md` — AI agent conventions for working in this repo (skill format, naming rules, directory structure)
> - `README.md` — public-facing repo introduction (what this is, how to use, empty catalog)
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: YES - 2 waves (structure first, then docs in parallel)
> **Critical Path**: skills/.gitkeep → AGENTS.md + README.md (parallel)

---

## Context

### Original Request
User wants to kickstart the `dawidkulpa/skills` repository as a public home for personally authored AI agent skills. The repo currently contains only a LICENSE (MIT) and an initial commit. The goal is to create the structural backbone — README, AGENTS.md, and the `skills/` directory — so the repo is ready to receive skills over time.

### Interview Summary
**Key Discussions**:
- **Identity**: Author showcase — curated, opinionated, high quality bar. Not community-contributed.
- **Skills**: None shipping initially. User adds skills manually over time.
- **Platform**: Platform-agnostic. Skills are portable SKILL.md + supporting files. No install helpers.
- **Structure**: Flat — each skill is a top-level folder under `skills/`.
- **Metadata**: Minimal YAML frontmatter — just `name` + `description` in each SKILL.md.
- **Deliverables**: README.md, AGENTS.md, `skills/` directory. Nothing else.

**Research Findings**:
- Standard skill format: SKILL.md with YAML frontmatter as entry point, supporting files optional
- Existing repos (anthropics/skills, obra/superpowers) use flat folder structure
- Folder name must match frontmatter `name` field (kebab-case)
- Discovery by directory presence — no manifest/registry needed

### Metis Review
**Identified Gaps** (addressed):
- AGENTS.md must explicitly prohibit nesting (flat structure only)
- AGENTS.md must state directory name === `name` field parity rule
- AGENTS.md should document that supporting files are allowed inside skill folders
- AGENTS.md should instruct agents to update README catalog when adding/removing skills
- README must use personal author voice ("I" not "we"), no community language
- No sample/example skills — `skills/` stays empty
- Optional frontmatter fields documented as optional (not required) in AGENTS.md

---

## Work Objectives

### Core Objective
Create the 3 foundational files that make `dawidkulpa/skills` a well-structured, documented, ready-to-populate public skill repository.

### Concrete Deliverables
- `skills/.gitkeep` — preserves empty directory in git
- `AGENTS.md` — skill authoring conventions for AI agents
- `README.md` — public repo introduction and skill catalog

### Definition of Done
- [ ] Exactly 4 files in repo (LICENSE + 3 new): verified by `find . -maxdepth 2 -not -path './.git/*' -not -path './.sisyphus/*' -type f | sort`
- [ ] LICENSE unchanged: `git diff HEAD -- LICENSE` produces empty output
- [ ] No sample skills: `find skills/ -name "SKILL.md" | wc -l` returns 0
- [ ] README has no platform-specific install commands
- [ ] README has no contribution/community language
- [ ] AGENTS.md documents frontmatter schema and naming rules

### Must Have
- Personal author voice in README
- Kebab-case naming rule documented
- Directory name ↔ frontmatter `name` parity rule
- Flat structure rule (no nesting)
- SKILL.md as required entry point documented
- Empty catalog placeholder in README

### Must NOT Have (Guardrails)
- No CI/CD, no linting, no GitHub Actions
- No CONTRIBUTING.md or community language ("we welcome contributions", "PRs", "fork")
- No install scripts or platform-specific helpers
- No `docs/` directory
- No `.agents/` directory inside the repo
- No sample/example skills under `skills/`
- No badges in README
- No prescribed SKILL.md body structure — only frontmatter schema + directory rules
- No catalog auto-generation scripts

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO (pure markdown repo)
- **Automated tests**: None (no code)
- **Framework**: N/A

### QA Policy
Every task includes agent-executed QA scenarios. Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **File structure**: Use Bash — verify file existence, content, absence of forbidden patterns
- **Content quality**: Use Bash (grep) — check for required sections, forbidden phrases

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — directory structure):
└── Task 1: Create skills/ directory with .gitkeep [quick]

Wave 2 (After Wave 1 — docs in parallel):
├── Task 2: Create AGENTS.md (depends: 1) [quick]
└── Task 3: Create README.md (depends: 1) [quick]

Wave FINAL (After ALL tasks — verification):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review (unspecified-high)
├── Task F3: Real manual QA (unspecified-high)
└── Task F4: Scope fidelity check (deep)
-> Present results -> Get explicit user okay
```

### Dependency Matrix

| Task | Depends On | Blocks | Wave |
|------|-----------|--------|------|
| 1    | —         | 2, 3   | 1    |
| 2    | 1         | F1-F4  | 2    |
| 3    | 1         | F1-F4  | 2    |

### Agent Dispatch Summary

- **Wave 1**: 1 task — T1 → `quick`
- **Wave 2**: 2 tasks — T2 → `quick`, T3 → `quick`
- **FINAL**: 4 tasks — F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [x] 1. Create `skills/` directory with `.gitkeep`

  **What to do**:
  - Create `skills/` directory at repo root
  - Add empty `.gitkeep` file inside it to preserve directory in git
  - Verify `.gitkeep` is 0 bytes

  **Must NOT do**:
  - Do not add any sample skills, templates, or example folders
  - Do not add a README inside `skills/`
  - Do not create any subdirectories inside `skills/`

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-file creation, trivial task
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `git-master`: Not needed — just file creation, commit handled later

  **Parallelization**:
  - **Can Run In Parallel**: NO (Wave 1 — foundation)
  - **Parallel Group**: Wave 1 (solo)
  - **Blocks**: Tasks 2, 3
  - **Blocked By**: None

  **References**:
  - `LICENSE` — verify this file exists and remains untouched after creating `skills/`

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: skills directory exists with empty .gitkeep
    Tool: Bash
    Preconditions: Repo has only LICENSE file
    Steps:
      1. Run: `test -d skills/ && echo "DIR_EXISTS" || echo "DIR_MISSING"`
      2. Assert output: "DIR_EXISTS"
      3. Run: `test -f skills/.gitkeep && echo "FILE_EXISTS" || echo "FILE_MISSING"`
      4. Assert output: "FILE_EXISTS"
      5. Run: `test ! -s skills/.gitkeep && echo "EMPTY" || echo "NOT_EMPTY"`
      6. Assert output: "EMPTY"
      7. Run: `find skills/ -mindepth 1 -not -name '.gitkeep' | wc -l`
      8. Assert output: "0" (nothing else in skills/)
    Expected Result: Directory exists, .gitkeep exists and is empty, no other files
    Failure Indicators: Missing directory, non-empty .gitkeep, extra files in skills/
    Evidence: .sisyphus/evidence/task-1-gitkeep-structure.txt
  ```

  **Commit**: YES
  - Message: `chore: add skills directory structure`
  - Files: `skills/.gitkeep`
  - Pre-commit: `test -f skills/.gitkeep && test ! -s skills/.gitkeep && echo PASS`

- [x] 2. Create `AGENTS.md` with skill authoring conventions

  **What to do**:
  - Create `AGENTS.md` at repo root
  - Target audience: AI agents working inside this repository (authoring/maintaining skills)
  - Document these conventions:
    - **Directory structure**: Each skill lives in `skills/<skill-name>/` with `SKILL.md` as the required entry point
    - **Flat structure rule**: No nesting — one level only under `skills/`
    - **Naming rule**: Directory name must be kebab-case and must exactly match the `name` field in SKILL.md frontmatter
    - **Required frontmatter**: YAML frontmatter with `name` (kebab-case, must match directory) and `description` (what it does + when to use it)
    - **Optional frontmatter**: Mention that `metadata.author`, `metadata.tags`, `metadata.version` are available but not required
    - **Supporting files**: Additional `.md` files, scripts, examples are allowed inside the skill folder. SKILL.md is the entry point; everything else is optional.
    - **Self-contained**: Each skill folder must be self-contained — use relative paths only, no cross-references to other skill folders
    - **README catalog maintenance**: When adding or removing a skill, update the skill catalog table in README.md
  - Include the SKILL.md frontmatter schema inline (not as a separate template file):
    ```yaml
    ---
    name: my-skill-name
    description: "What this skill does and when an agent should use it"
    ---
    ```
  - Tone: direct, instructional (addressing AI agents), concise

  **Must NOT do**:
  - Do not prescribe SKILL.md body sections or structure — only frontmatter + directory rules
  - Do not include platform-specific instructions (no Claude Code, OpenCode, Gemini references)
  - Do not create a separate template file — document format inline in AGENTS.md
  - Do not add example skill content or sample implementations
  - Do not use community language ("contributors", "PRs welcome")

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single markdown file, clear spec, ~50-80 lines
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `writing-skills`: About writing agent *skills*, not repo documentation

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 3)
  - **Parallel Group**: Wave 2 (with Task 3)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 1

  **References**:

  **Pattern References**:
  - Existing SKILL.md examples from the user's local skills (for understanding the format the user already uses):
    - `/home/zapal/.agents/skills/competitive-brief/SKILL.md` — simple skill with just SKILL.md
    - `/home/zapal/.agents/skills/victorialogs/SKILL.md` — skill with supporting reference files
    - `/home/zapal/.config/opencode/skills/superpowers/dispatching-parallel-agents/SKILL.md` — minimal superpowers skill

  **External References**:
  - YAML frontmatter standard for SKILL.md: `name` (kebab-case, 1-64 chars) + `description` (1-1024 chars)

  **WHY Each Reference Matters**:
  - The local SKILL.md files show the exact frontmatter format the user already uses — match this convention, don't invent a new one
  - The YAML frontmatter spec defines the field constraints (length limits, character rules)

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: AGENTS.md contains all required convention documentation
    Tool: Bash (grep)
    Preconditions: AGENTS.md created at repo root
    Steps:
      1. Run: `test -f AGENTS.md && echo "EXISTS" || echo "MISSING"`
      2. Assert: "EXISTS"
      3. Run: `grep -c 'SKILL.md' AGENTS.md`
      4. Assert: >= 1 (documents SKILL.md as entry point)
      5. Run: `grep -c 'kebab-case' AGENTS.md`
      6. Assert: >= 1 (documents naming convention)
      7. Run: `grep -c 'name' AGENTS.md`
      8. Assert: >= 1 (documents required frontmatter)
      9. Run: `grep -c 'description' AGENTS.md`
      10. Assert: >= 1 (documents required frontmatter)
      11. Run: `head -5 AGENTS.md | grep -ciE '(agent|AI)'`
      12. Assert: >= 1 (addresses agents, not humans)
    Expected Result: All conventions documented, agent-facing tone
    Failure Indicators: Missing sections, human-facing tone, missing frontmatter docs
    Evidence: .sisyphus/evidence/task-2-agents-md-content.txt

  Scenario: AGENTS.md does NOT contain forbidden content
    Tool: Bash (grep)
    Preconditions: AGENTS.md exists
    Steps:
      1. Run: `grep -ciE '(claude.code|opencode|gemini|cursor|windsurf)' AGENTS.md`
      2. Assert: 0 (no platform-specific references)
      3. Run: `grep -ciE '(contribut|pull.request|PR.welcome|fork)' AGENTS.md`
      4. Assert: 0 (no community language)
      5. Run: `grep -ciE '## (Overview|Introduction|Usage|Examples|API)' AGENTS.md`
      6. Assert: 0 (no prescribed body sections for SKILL.md)
    Expected Result: Clean of all forbidden content
    Failure Indicators: Platform names, community language, body section prescriptions
    Evidence: .sisyphus/evidence/task-2-agents-md-forbidden.txt
  ```

  **Commit**: YES
  - Message: `docs: add AGENTS.md with skill conventions`
  - Files: `AGENTS.md`
  - Pre-commit: `grep -q 'name' AGENTS.md && grep -q 'description' AGENTS.md && grep -q 'kebab-case' AGENTS.md && echo PASS`

- [x] 3. Create `README.md` with repo introduction

  **What to do**:
  - Create `README.md` at repo root
  - Target audience: humans browsing the GitHub repo
  - Content sections:
    - **Title/H1**: Repository name
    - **Intro paragraph**: What this repo is — a personal collection of AI agent skills, authored and curated by Dawid Kulpa. Brief explanation of what agent skills are (portable instruction sets that enhance AI coding assistants). 1-2 paragraphs, personal voice.
    - **How to use**: Generic instructions for using skills from this repo — browse `skills/` directory, copy the skill folder you want into your agent's skill directory. No platform-specific commands. Mention that each skill has a `SKILL.md` as its entry point.
    - **Skills catalog**: A section with a markdown table (columns: Name, Description) that is currently empty with a placeholder like "No skills published yet" or similar. This table will be manually updated as skills are added.
    - **License**: Brief reference to MIT license
  - Tone: personal, direct, minimal. "I" not "we". Author showcase, not community project.
  - Keep it short — aim for ~40-60 lines total. No fluff.

  **Must NOT do**:
  - No platform-specific installation commands (no `claude mcp install`, `opencode skill add`, etc.)
  - No contribution guidelines or community language ("we welcome", "PRs", "contributors", "fork")
  - No badges
  - No CI/CD references
  - No links to external documentation or tutorials
  - No "Getting Started" section that implies onboarding contributors
  - No over-explanation of what AI is or lengthy preambles

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single markdown file, clear spec, ~40-60 lines
  - **Skills**: `[]`
  - **Skills Evaluated but Omitted**:
    - `frontend-design`: Not a visual task, pure markdown

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 2)
  - **Parallel Group**: Wave 2 (with Task 2)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 1

  **References**:

  **Pattern References**:
  - `LICENSE` — MIT, copyright 2026 dawidkulpa. README should reference this.
  - GitHub remote: `https://github.com/dawidkulpa/skills` — the repo URL for context

  **External References**:
  - `https://github.com/anthropics/skills` — Anthropic's official skills repo README for structural inspiration (flat layout, minimal docs)
  - `https://github.com/obra/superpowers` — obra's superpowers README for tone reference (author-curated, opinionated)

  **WHY Each Reference Matters**:
  - LICENSE confirms the exact copyright holder name and year to reference
  - Anthropic's repo shows the "official" way a skills README looks — minimal, focused
  - obra's repo shows author-curated tone done well

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: README.md contains all required sections
    Tool: Bash (grep)
    Preconditions: README.md created at repo root
    Steps:
      1. Run: `test -f README.md && echo "EXISTS" || echo "MISSING"`
      2. Assert: "EXISTS"
      3. Run: `head -3 README.md | grep -c '#'`
      4. Assert: >= 1 (has H1 title)
      5. Run: `grep -ciE 'skill' README.md`
      6. Assert: >= 1 (mentions skills)
      7. Run: `grep -ciE '(license|MIT)' README.md`
      8. Assert: >= 1 (references license)
      9. Run: `grep -c 'SKILL.md' README.md`
      10. Assert: >= 1 (mentions entry point)
      11. Run: `wc -l < README.md`
      12. Assert: between 20 and 80 lines (concise, not bloated)
    Expected Result: All sections present, concise length
    Failure Indicators: Missing title, no license reference, over 80 lines
    Evidence: .sisyphus/evidence/task-3-readme-content.txt

  Scenario: README.md has no forbidden content
    Tool: Bash (grep)
    Preconditions: README.md exists
    Steps:
      1. Run: `grep -ciE '(claude|gemini|codex|opencode|cursor)\s+(mcp|skill|install|add)' README.md`
      2. Assert: 0 (no platform-specific install commands)
      3. Run: `grep -ciE '(contribut|pull.request|fork|PR.welcome)' README.md`
      4. Assert: 0 (no community language)
      5. Run: `grep -c 'badge' README.md`
      6. Assert: 0 (no badges)
      7. Run: `grep -c '\!\[' README.md`
      8. Assert: 0 (no badge images)
      9. Run: `grep -ciE '(we welcome|we accept|join us|community)' README.md`
      10. Assert: 0 (no community tone)
    Expected Result: Clean of all forbidden content
    Failure Indicators: Platform commands, community language, badges
    Evidence: .sisyphus/evidence/task-3-readme-forbidden.txt

  Scenario: README.md uses personal author voice
    Tool: Bash (grep)
    Preconditions: README.md exists
    Steps:
      1. Run: `grep -cE '\bI\b' README.md`
      2. Assert: >= 1 (uses first person "I")
      3. Run: `grep -ciE '\bwe\b' README.md`
      4. Assert: 0 (does not use "we")
    Expected Result: Personal author voice throughout
    Failure Indicators: Corporate "we" language, passive voice
    Evidence: .sisyphus/evidence/task-3-readme-voice.txt
  ```

  **Commit**: YES
  - Message: `docs: add README with repo introduction`
  - Files: `README.md`
  - Pre-commit: `grep -cE '(contribut|pull.request|fork|PR)' README.md | grep -q '^0$' && echo PASS`

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, grep for content). For each "Must NOT Have": search repo for forbidden patterns — reject with file:line if found. Verify exactly 4 files exist (LICENSE, README.md, AGENTS.md, skills/.gitkeep). Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Check all markdown files for: broken links, formatting issues, inconsistent heading levels, spelling errors, tone consistency (personal voice, not corporate). Verify markdown renders correctly. Check for AI slop: excessive caveats, filler phrases, over-explanation.
  Output: `README [PASS/FAIL] | AGENTS.md [PASS/FAIL] | Issues [N] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Read README.md as a new visitor — does it make sense? Can you understand what this repo is and how to use skills from it? Read AGENTS.md as an AI agent — are the conventions clear and unambiguous? Verify `skills/` is empty. Check LICENSE is intact.
  Output: `README clarity [PASS/FAIL] | AGENTS.md clarity [PASS/FAIL] | Structure [PASS/FAIL] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual files. Verify 1:1 — everything in spec was created, nothing beyond spec was created. Check "Must NOT do" compliance. Verify no extra files/directories. Flag any unaccounted changes.
  Output: `Tasks [N/N compliant] | Extra files [CLEAN/N] | Guardrails [N/N respected] | VERDICT`

---

## Commit Strategy

| Order | Message | Files | Pre-commit Check |
|-------|---------|-------|-----------------|
| 1 | `chore: add skills directory structure` | `skills/.gitkeep` | `test -f skills/.gitkeep` |
| 2 | `docs: add AGENTS.md with skill conventions` | `AGENTS.md` | `grep -q 'name' AGENTS.md && grep -q 'description' AGENTS.md` |
| 3 | `docs: add README with repo introduction` | `README.md` | `grep -cE '(contribut\|pull request\|fork\|PR)' README.md` returns 0 |

Each commit is independently valid and revertible.

---

## Success Criteria

### Verification Commands
```bash
# Exactly 4 files (excluding .git and .sisyphus)
find . -maxdepth 2 -not -path './.git/*' -not -path './.sisyphus/*' -type f | sort
# Expected: ./AGENTS.md ./LICENSE ./README.md ./skills/.gitkeep

# LICENSE unchanged
git diff HEAD -- LICENSE  # Expected: empty output

# No sample skills
find skills/ -name "SKILL.md" | wc -l  # Expected: 0

# No platform-specific install commands in README
grep -ciE '(claude|gemini|codex|opencode|cursor)\s+(mcp|skill|install|add)' README.md  # Expected: 0

# No community language in README
grep -ciE '(contribut|pull request|fork|PR)' README.md  # Expected: 0

# AGENTS.md documents required fields
grep -q 'name' AGENTS.md && grep -q 'description' AGENTS.md && echo "PASS"  # Expected: PASS

# No extra directories
find . -maxdepth 1 -type d -not -name '.git' -not -name '.sisyphus' -not -name '.' | sort
# Expected: ./skills
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] 3 atomic commits, each independently valid
- [ ] Personal author voice throughout
