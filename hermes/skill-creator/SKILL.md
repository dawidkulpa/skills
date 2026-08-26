---
name: skill-creator
description: "Use only when the user explicitly asks to draft or revise a skill for manual installation; użyj tylko na jawną prośbę o treść skilla."
user-invocable: true
disable-model-invocation: true
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "skills, authoring, librechat, manual-installation, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/anthropics/skills/tree/main/skills/skill-creator"
  source-license: "Apache-2.0"
---

# Skill Creator for Manual Installation

Activate only when the current user explicitly asks to create, draft, rewrite, or improve a skill. Do not infer permission from a recurring workflow, a successful conversation, or a suggestion that something might be reusable.

This skill produces content in chat. It does not install, save, upload, sync, publish, enable, or test a skill in LibreChat or any other harness. The user reviews the output and adds it to the skill database manually.

Respond in the user's language. Write the skill itself in the language the user requests; if unspecified, use the current conversation language and make invocation robust for both Polish and English when appropriate.

## Capture the design

Use context already available before asking questions. Clarify only material gaps:

1. What repeatable task should the skill improve?
2. What explicit phrases or contexts should trigger it, in Polish and English?
3. When should it not trigger?
4. What inputs, tools, attachments, or external services are actually available in the target LibreChat agent?
5. What output format and success criteria are required?
6. Which safety, privacy, approval, market, or language rules must be enforced?

If the user supplied enough detail, state assumptions and draft immediately instead of conducting a long interview.

## Authoring rules

- Use a stable lowercase kebab-case `name` that matches the intended folder name.
- Make `description` the strongest trigger signal: describe both capability and when to use it, with relevant Polish and English phrases.
- Use only frontmatter fields supported or safely preserved by LibreChat: `name`, `description`, `always-apply`, `user-invocable`, `disable-model-invocation`, `allowed-tools`, `compatibility`, and bounded metadata.
- Do not list a tool in `allowed-tools` unless the user confirms its exact LibreChat tool identifier. Put non-enforced requirements in `compatibility`.
- Keep the main instructions chat-first. Do not assume filesystem access, terminal use, autonomous background work, subagents, persistence, or external credentials.
- Ask only decision-changing questions and avoid mandatory multi-step ceremony for simple requests.
- State transactional or irreversible-action confirmation boundaries explicitly.
- Make the skill self-contained; do not rely on another skill being loaded.
- Use relative paths only if the user explicitly requests supporting files.
- Do not include secrets, environment values, private URLs, or machine-specific paths.

## Output contract

Return these sections in the chat:

1. **Design summary** — trigger, non-trigger, assumptions, and required capabilities.
2. **Complete `SKILL.md`** — one copy-ready fenced block containing frontmatter and body.
3. **Optional supporting files** — only when necessary, each under a relative path heading and in its own fenced block.
4. **Manual installation steps** — create the matching folder, paste `SKILL.md`, add supporting files, upload or sync through the user's normal LibreChat administration flow, then activate it for the intended agent.
5. **Test prompts** — at least two positive prompts in Polish and English, one non-trigger prompt, and expected behavior for each.
6. **Review checklist** — name/description match, tool identifiers, language, safety boundary, no hidden dependency, and output format.

When the `SKILL.md` itself needs fenced examples, wrap the whole deliverable in a longer outer fence so the content remains copyable.

## Revision workflow

For an existing skill, preserve its name unless the user asks for a rename. Show the complete revised file rather than a fragment, then summarize material changes. Do not claim benchmark or execution results; offer manual test prompts the user can run in LibreChat.

## Final check

- The current request was an explicit skill-authoring request.
- The description contains useful Polish and English trigger language.
- No unavailable tool, write capability, persistence, or credential is assumed.
- The answer contains the full content needed for manual installation.
- No installation or publication is claimed.
