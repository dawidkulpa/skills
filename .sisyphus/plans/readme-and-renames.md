# README Updates & Skill Renames

## TL;DR

> **Quick Summary**: Add AI-generated content disclaimer to README, remove the skills catalog table (and its maintenance instructions from AGENTS.md), and rename all 3 skills with a `vikunja-` prefix since they're all Vikunja management skills.
> 
> **Deliverables**:
> - Updated README.md with AI disclaimer, catalog removed
> - Updated AGENTS.md with catalog maintenance instructions removed
> - 3 renamed skill directories with all cross-references updated
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: YES — 2 waves
> **Critical Path**: T1 (renames) → T2+T3 (README + AGENTS in parallel)

---

## Context

### Original Request
User asked for two things: (1) add a transparency disclaimer that the repo was at least partially AI-generated, and (2) rename the 3 existing skills to have a `vikunja-` prefix since they're all Vikunja kanban management skills. During discussion, user also decided to remove the skills catalog table from README entirely ("another thing to maintain") and any related instructions in AGENTS.md.

### Interview Summary
**Key Discussions**:
- Skills catalog: User wants it gone — simplification, one less thing to maintain
- Disclaimer: User wants transparency, asked me to draft concise wording
- Rename scope: All 3 skills (`board-poller`, `task-executor`, `task-refiner`) get `vikunja-` prefix

**Research Findings**:
- Each skill has only SKILL.md, no supporting files
- Cross-references exist between all 3 skills (dispatching, description mentions)
- 14 total reference points need updating across the 3 SKILL.md files

### Metis Review
**Identified Gaps** (addressed):
- H1 titles in SKILL.md files need updating too → included in rename task
- AGENTS.md verification checklist has a catalog item → included in removal task
- Description frontmatter contains cross-references on single lines → noted as edge case
- Bold-formatted references need careful handling → explicit in instructions
- External systems might reference skill names → flagged as decision needed

---

## Work Objectives

### Core Objective
Update the repo's public documentation for transparency and rename skills for clarity.

### Concrete Deliverables
- `README.md` — AI disclaimer added, "Available Skills" section removed
- `AGENTS.md` — "README Catalog Maintenance" section removed, verification checklist item about catalog removed
- `skills/vikunja-board-poller/` — renamed from `board-poller/`, all references updated
- `skills/vikunja-task-executor/` — renamed from `task-executor/`, all references updated  
- `skills/vikunja-task-refiner/` — renamed from `task-refiner/`, all references updated

### Definition of Done
- [ ] `ls skills/` shows only `vikunja-board-poller`, `vikunja-task-executor`, `vikunja-task-refiner` (no old names)
- [ ] `grep -rn "board-poller\|task-executor\|task-refiner" skills/ | grep -v vikunja-` returns 0 results
- [ ] README.md contains AI disclaimer text
- [ ] README.md has no table markup in former catalog area
- [ ] `grep -ci "catalog" AGENTS.md` returns 0

### Must Have
- AI disclaimer in README
- All 3 skills renamed with `vikunja-` prefix
- All cross-references updated (zero stale references)
- Catalog table removed from README
- Catalog maintenance instructions removed from AGENTS.md
- Git history preserved via `git mv`

### Must NOT Have (Guardrails)
- Do NOT modify skill content, procedures, or logic — only name-bearing strings
- Do NOT add new sections or features to README beyond the disclaimer
- Do NOT restructure AGENTS.md beyond removing catalog-related content
- Do NOT add a replacement catalog/index in any form
- Do NOT touch the License section in README
- Do NOT modify any AGENTS.md verification checklist items except the catalog one

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: N/A — no code, markdown-only changes
- **Automated tests**: None
- **Framework**: None

### QA Policy
Every task includes agent-executed QA scenarios using grep and ls commands.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **File renames**: Use Bash (ls, grep) — verify directories exist, old names gone, zero stale references
- **Content edits**: Use Bash (grep) — verify content present/absent

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — renames must happen first):
└── Task 1: Rename all 3 skills + update all cross-references [quick]

Wave 2 (After Wave 1 — independent edits, MAX PARALLEL):
├── Task 2: Update README.md (disclaimer + remove catalog) [quick]
└── Task 3: Update AGENTS.md (remove catalog instructions) [quick]

Wave FINAL (After ALL tasks — verification):
├── Task F1: Plan Compliance Audit (oracle)
├── Task F2: Code Quality Review (unspecified-high)
├── Task F3: Real Manual QA (unspecified-high)
└── Task F4: Scope Fidelity Check (deep)
-> Present results -> Get explicit user okay
```

### Dependency Matrix

| Task | Depends On | Blocks | Wave |
|------|-----------|--------|------|
| T1 | None | T2, T3 | 1 |
| T2 | T1 | F1-F4 | 2 |
| T3 | T1 | F1-F4 | 2 |
| F1-F4 | T1, T2, T3 | — | FINAL |

> T2 depends on T1 only because the README might reference skill names. Currently it doesn't, but running renames first keeps things safe.

### Agent Dispatch Summary

- **Wave 1**: 1 agent — T1 → `quick`
- **Wave 2**: 2 agents — T2 → `quick`, T3 → `quick`
- **FINAL**: 4 agents — F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [ ] 1. Rename all 3 skills with `vikunja-` prefix and update all cross-references

  **What to do**:

  **Step 1 — Rename directories** (use `git mv` to preserve history):
  ```bash
  git mv skills/board-poller skills/vikunja-board-poller
  git mv skills/task-executor skills/vikunja-task-executor
  git mv skills/task-refiner skills/vikunja-task-refiner
  ```

  **Step 2 — Update `vikunja-board-poller/SKILL.md`**:
  - Line 2: `name: board-poller` → `name: vikunja-board-poller`
  - Line 6: `# Board Poller` → `# Vikunja Board Poller`
  - Line 71: `task-refiner workflow` → `vikunja-task-refiner workflow`
  - Line 72: `task-executor workflow` → `vikunja-task-executor workflow`
  - Line 92: `**task-refiner** skill procedure` → `**vikunja-task-refiner** skill procedure`
  - Line 93: `**task-executor** skill procedure` → `**vikunja-task-executor** skill procedure`

  **Step 3 — Update `vikunja-task-executor/SKILL.md`**:
  - Line 2: `name: task-executor` → `name: vikunja-task-executor`
  - Line 3 (description): Update both `task-refiner` → `vikunja-task-refiner` AND `board-poller` → `vikunja-board-poller` within the single description line
  - Line 6: `# Task Executor` → `# Vikunja Task Executor`
  - Line 148 (and/or 154): `board-poller claimed it` → `vikunja-board-poller claimed it`

  **Step 4 — Update `vikunja-task-refiner/SKILL.md`**:
  - Line 2: `name: task-refiner` → `name: vikunja-task-refiner`
  - Line 3 (description): `board-poller skill` → `vikunja-board-poller skill`
  - Line 6: `# Task Refiner` → `# Vikunja Task Refiner`
  - Line 115 (and/or 117): `board-poller claimed it` → `vikunja-board-poller claimed it`

  **Step 5 — Verify zero stale references**:
  ```bash
  grep -rn "board-poller\|task-executor\|task-refiner" skills/ | grep -v vikunja-
  # MUST return 0 results
  ```

  **IMPORTANT edge cases**:
  - Description frontmatter (line 3) in task-executor contains BOTH `task-refiner` and `board-poller` on a single line — update both in one edit
  - Bold references like `**task-refiner**` must become `**vikunja-task-refiner**` (keep bold markers around the full name)
  - Do NOT use blind find-replace — the line numbers above are the validated targets

  **Must NOT do**:
  - Do NOT modify any skill content, procedures, hard gates, or logic
  - Do NOT change anything that isn't a skill name reference

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Mechanical find-and-replace across 3 files + git mv. No creative decisions.
  - **Skills**: [`git-master`]
    - `git-master`: Directory renames via `git mv` for history preservation

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 1 (solo)
  - **Blocks**: Tasks 2, 3
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `skills/board-poller/SKILL.md` — Full file, 102 lines. Lines 2, 6, 71, 72, 92, 93 contain rename targets.
  - `skills/task-executor/SKILL.md` — Full file, 185 lines. Lines 2, 3, 6, 148/154 contain rename targets.
  - `skills/task-refiner/SKILL.md` — Full file, 145 lines. Lines 2, 3, 6, 115/117 contain rename targets.

  **WHY Each Reference Matters**:
  - The Metis cross-reference table (in Context section above) maps every single reference point — use it as a checklist

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Directories renamed correctly
    Tool: Bash
    Preconditions: Git working tree clean before renames
    Steps:
      1. Run `ls skills/` 
      2. Assert output contains: vikunja-board-poller, vikunja-task-executor, vikunja-task-refiner
      3. Assert output does NOT contain: board-poller, task-executor, task-refiner (without prefix)
      4. Run `ls skills/vikunja-board-poller/SKILL.md skills/vikunja-task-executor/SKILL.md skills/vikunja-task-refiner/SKILL.md`
      5. Assert all 3 files exist
    Expected Result: 3 prefixed directories, 0 old directories, all SKILL.md files present
    Failure Indicators: Any old directory name still exists, or SKILL.md missing
    Evidence: .sisyphus/evidence/task-1-directories.txt

  Scenario: Zero stale references across all skills
    Tool: Bash
    Preconditions: All edits complete
    Steps:
      1. Run `grep -rn "board-poller\|task-executor\|task-refiner" skills/ | grep -v vikunja-`
      2. Assert output is empty (0 lines)
    Expected Result: No matches — every reference now has vikunja- prefix
    Failure Indicators: Any line returned means a stale reference was missed
    Evidence: .sisyphus/evidence/task-1-stale-refs.txt

  Scenario: Frontmatter names match directory names
    Tool: Bash
    Preconditions: All edits complete
    Steps:
      1. Run `grep "^name:" skills/vikunja-board-poller/SKILL.md`
      2. Assert output is `name: vikunja-board-poller`
      3. Run `grep "^name:" skills/vikunja-task-executor/SKILL.md`
      4. Assert output is `name: vikunja-task-executor`
      5. Run `grep "^name:" skills/vikunja-task-refiner/SKILL.md`
      6. Assert output is `name: vikunja-task-refiner`
    Expected Result: All 3 frontmatter names match their directory names exactly
    Failure Indicators: Any mismatch between directory name and frontmatter name
    Evidence: .sisyphus/evidence/task-1-frontmatter.txt
  ```

  **Commit**: YES
  - Message: `rename: add vikunja- prefix to all skill directories`
  - Files: `skills/vikunja-board-poller/SKILL.md`, `skills/vikunja-task-executor/SKILL.md`, `skills/vikunja-task-refiner/SKILL.md` (plus git mv tracking)
  - Pre-commit: `grep -rn "board-poller\|task-executor\|task-refiner" skills/ | grep -v vikunja-` → 0 results

- [ ] 2. Update README.md — add AI disclaimer, remove skills catalog

  **What to do**:

  **Step 1 — Add AI disclaimer**. Insert a `## Disclaimer` section after the License section (at the very end of the file). Suggested wording:

  ```markdown
  ## Disclaimer

  Parts of this repository, including documentation and skill definitions, were generated or co-authored with AI tools. All content is reviewed and curated by the author.
  ```

  **Step 2 — Remove the "Available Skills" section entirely** (heading + placeholder table, lines 15–19). Replace with a one-liner pointing to the directory:

  ```markdown
  ## Skills

  Browse the `skills/` directory — each folder contains a `SKILL.md` with full instructions.
  ```

  > Rationale: Keeping a heading for discoverability but removing the maintenance burden of a table. Users still know where to look.

  **Must NOT do**:
  - Do NOT touch the License section
  - Do NOT restructure or rewrite the intro text
  - Do NOT add a new catalog format

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Two small edits to a 25-line markdown file
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 3)
  - **Parallel Group**: Wave 2 (with Task 3)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 1

  **References**:

  **Pattern References**:
  - `README.md` — Full file, 25 lines. Lines 15-19 are the catalog to remove. Lines 21-25 are the License section (do not touch).

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: AI disclaimer is present
    Tool: Bash
    Preconditions: README.md has been edited
    Steps:
      1. Run `grep -i "AI" README.md`
      2. Assert output contains disclaimer text mentioning AI tools
      3. Run `grep -i "disclaimer" README.md`
      4. Assert "Disclaimer" heading exists
    Expected Result: Disclaimer section present with AI transparency text
    Failure Indicators: No AI-related text found, or no Disclaimer heading
    Evidence: .sisyphus/evidence/task-2-disclaimer.txt

  Scenario: Catalog table is gone
    Tool: Bash
    Preconditions: README.md has been edited
    Steps:
      1. Run `grep -c "No skills published yet" README.md`
      2. Assert result is 0
      3. Run `grep "Available Skills" README.md`
      4. Assert result is 0 (old heading gone)
    Expected Result: No catalog table markup, no placeholder text
    Failure Indicators: Table markup or placeholder text still present
    Evidence: .sisyphus/evidence/task-2-catalog-removed.txt

  Scenario: License section is untouched
    Tool: Bash
    Preconditions: README.md has been edited
    Steps:
      1. Run `grep "MIT License" README.md`
      2. Assert text is present
      3. Run `grep "© 2026 dawidkulpa" README.md`
      4. Assert text is present
    Expected Result: License section intact
    Failure Indicators: License text missing or modified
    Evidence: .sisyphus/evidence/task-2-license.txt
  ```

  **Commit**: YES (groups with Task 3)
  - Message: `docs: add AI disclaimer and simplify README`
  - Files: `README.md`
  - Pre-commit: `grep -i "disclaimer" README.md` → match found

- [ ] 3. Update AGENTS.md — remove catalog maintenance instructions

  **What to do**:

  **Step 1 — Remove "README Catalog Maintenance" section** (lines 88–95 of AGENTS.md). This is a standalone section with heading and body.

  **Step 2 — Remove verification checklist item** about catalog. Find and remove the line:
  ```
  - [ ] README.md catalog has been updated
  ```

  **Step 3 — Verify no other catalog references remain**:
  ```bash
  grep -ci "catalog" AGENTS.md
  # MUST return 0
  ```

  **Must NOT do**:
  - Do NOT remove or modify any other verification checklist items
  - Do NOT restructure other AGENTS.md sections

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Two small deletions from a markdown file
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 2)
  - **Parallel Group**: Wave 2 (with Task 2)
  - **Blocks**: F1-F4
  - **Blocked By**: Task 1

  **References**:

  **Pattern References**:
  - `AGENTS.md` — Lines 88-95 contain the "README Catalog Maintenance" section. Line 108 contains the checklist item `- [ ] README.md catalog has been updated`.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Catalog maintenance section removed
    Tool: Bash
    Preconditions: AGENTS.md has been edited
    Steps:
      1. Run `grep -c "Catalog Maintenance" AGENTS.md`
      2. Assert result is 0
      3. Run `grep -ci "catalog" AGENTS.md`
      4. Assert result is 0
    Expected Result: Zero catalog references in AGENTS.md
    Failure Indicators: Any match for "catalog" found
    Evidence: .sisyphus/evidence/task-3-catalog-removed.txt

  Scenario: Other checklist items preserved
    Tool: Bash
    Preconditions: AGENTS.md has been edited
    Steps:
      1. Run `grep "\- \[ \]" AGENTS.md`
      2. Assert at least 5 checklist items remain (there were 6 originally, removing 1)
      3. Verify items include: "Directory name is kebab-case", "SKILL.md exists", "Frontmatter includes"
    Expected Result: All non-catalog checklist items intact
    Failure Indicators: Fewer than 5 checklist items, or key items missing
    Evidence: .sisyphus/evidence/task-3-checklist.txt
  ```

  **Commit**: YES (groups with Task 2)
  - Message: `docs: add AI disclaimer and simplify README`
  - Files: `AGENTS.md`
  - Pre-commit: `grep -ci "catalog" AGENTS.md` → 0

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, run grep). For each "Must NOT Have": search codebase for forbidden patterns. Check evidence files exist in .sisyphus/evidence/. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Code Quality Review** — `unspecified-high`
  Review all changed files. Check for: broken markdown formatting, orphan headings, inconsistent naming, stale references. Verify frontmatter YAML is valid. Verify all `git mv` operations preserved history.
  Output: `Files [N clean/N issues] | VERDICT`

- [ ] F3. **Real Manual QA** — `unspecified-high`
  Execute EVERY QA scenario from EVERY task — follow exact steps, capture evidence. Test cross-task integration (renamed skills reference each other correctly). Save to `.sisyphus/evidence/final-qa/`.
  Output: `Scenarios [N/N pass] | Integration [N/N] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git diff). Verify 1:1 — everything in spec was built, nothing beyond spec was built. Check "Must NOT do" compliance. Flag unaccounted changes.
  Output: `Tasks [N/N compliant] | Unaccounted [CLEAN/N files] | VERDICT`

---

## Commit Strategy

| # | Message | Files | Pre-commit |
|---|---------|-------|-----------|
| 1 | `rename: add vikunja- prefix to all skill directories` | 3 SKILL.md files + git mv tracking | `grep stale-refs → 0` |
| 2 | `docs: add AI disclaimer and simplify README` | `README.md`, `AGENTS.md` | `grep disclaimer → found`, `grep catalog AGENTS.md → 0` |

> Tasks 2 and 3 share a commit since they're both documentation simplification changes.

---

## Success Criteria

### Verification Commands
```bash
# Renames correct
ls skills/                                                              # Expected: vikunja-board-poller vikunja-task-executor vikunja-task-refiner
grep -rn "board-poller\|task-executor\|task-refiner" skills/ | grep -v vikunja-  # Expected: 0 results

# Frontmatter matches directories
grep "^name:" skills/*/SKILL.md                                        # Expected: 3 lines with vikunja- prefix

# README updated
grep -i "disclaimer" README.md                                         # Expected: match
grep "No skills published yet" README.md                               # Expected: 0

# AGENTS.md updated  
grep -ci "catalog" AGENTS.md                                           # Expected: 0
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] Zero stale skill name references
- [ ] Git history preserved for renames
