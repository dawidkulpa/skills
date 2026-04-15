# Skill Authoring Guide for AI Agents

When authoring or maintaining skills in this repository, follow these conventions. This guide is written for AI agents working inside the skills repository.

## Directory Structure

Skills are stored in a flat structure under `skills/`:

```
skills/
├── skill-name-one/
│   ├── SKILL.md          (required entry point)
│   ├── example.md        (optional supporting files)
│   └── resources/        (optional subdirectories for assets)
└── skill-name-two/
    ├── SKILL.md
    └── helper-script.sh  (optional)
```

**Flat structure rule:** No nesting. Each skill is exactly one directory level under `skills/`. No skill subdirectories containing other skills.

## Naming Convention

Directory name must:
- Be in **kebab-case** (lowercase, hyphens between words)
- **Exactly match** the `name` field in the skill's SKILL.md frontmatter

Example: Directory `my-skill` must have `name: my-skill` in frontmatter.

## SKILL.md Entry Point

Every skill folder **must** have exactly one `SKILL.md` file at the root. This is the agent's entry point.

### Frontmatter Schema

All SKILL.md files must include this YAML frontmatter block:

```yaml
---
name: skill-name
description: "What this skill does and when an agent should use it"
---
```

**Required fields:**
- `name` (kebab-case, must match directory name)
- `description` (one sentence describing what the skill does + trigger condition for agent use)

**Optional fields** (if metadata is needed):

```yaml
---
name: skill-name
description: "What this skill does and when an agent should use it"
metadata:
  author: "Your Name"
  tags: "tag1, tag2"
  version: "1.0.0"
---
```

Optional metadata fields:
- `metadata.author` — author name or organization
- `metadata.tags` — comma-separated tags for categorization
- `metadata.version` — version number (e.g., `1.0.0`)

The frontmatter closes with `---` on its own line. The skill body starts immediately after.

## Supporting Files

Additional files inside a skill folder are optional and serve as supporting resources:

- `.md` files — documentation, examples, checklists
- Scripts — shell, Python, or other executable helpers
- Subdirectories — for assets, templates, or organized resources

**Important:** SKILL.md is the entry point. Everything else is auxiliary. Agents load SKILL.md first; supporting files are referenced *from* SKILL.md if needed.

## Self-Contained Skills

Each skill is self-contained:

- Use **relative paths only** to reference supporting files (e.g., `./examples/template.md`)
- **Never cross-reference** other skill folders
- Never assume other skills are available in the agent's context
- All required instructions, context, and examples live inside the skill folder

## Verification Checklist

Before finalizing a skill:

- [ ] Directory name is kebab-case
- [ ] Directory name matches `name` field in frontmatter exactly
- [ ] SKILL.md exists at skill root (not nested)
- [ ] Frontmatter includes `name` and `description`
- [ ] Description explains what the skill does + when an agent should use it
- [ ] No cross-references to other skill folders
- [ ] Supporting files use relative paths only
