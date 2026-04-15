---
name: vikunja-task-executor
description: Executes approved tasks from the Queued column by following the implementation plan written by vikunja-task-refiner. Handles non-coding tasks (research, homelab operations, API calls, purchases). Escalates coding tasks and errors to the Human column. Designed to work alongside the vikunja-board-poller skill.
---

# Vikunja Task Executor

## Overview

Execute only approved, refined, non-coding tasks from the Queued column.

**Core principle:** follow the written implementation plan exactly, execute only within the allowed domain, and escalate immediately when a hard gate is triggered.

## Configuration Constants

| Constant | Value | Description |
|---|---:|---|
| PROJECT_ID | 2 | Vikunja project ID |
| VIEW_ID | 8 | Kanban view ID |
| BUCKET_QUEUED | 11 | Source: task came from here |
| BUCKET_IN_PROGRESS | 5 | Current location while executing |
| BUCKET_HUMAN | 9 | Destination on error or coding task |
| BUCKET_DONE | 6 | Destination on success |

## MCP Tools Quick Reference

| Tool | Operation | Parameters | Purpose |
|------|-----------|------------|---------|
| `vikunja_tasks` | `get` | `id=N` | Get full task details |
| `vikunja_tasks` | `update` | `id=N, done=true` | Mark task complete |
| `vikunja_task_comments` | `list` | `id=N` | Read all task comments |
| `vikunja_task_comments` | `add` | `id=N, comment="..."` | Post agent comments |
| `vikunja_task_move` | `move` | `projectId=2, viewId=8, taskId=N, bucketId=N` | Move task between columns |
| `vikunja_task_attachments` | `list` | `taskId=N` | Review existing attachments on pickup |
| `vikunja_task_attachments` | `download` | `taskId=N, attachmentId=N, outputPath="..."` | Download attachment for context |
| `vikunja_task_attachments` | `upload` | `taskId=N, filePath="..."` | Upload produced artifact on completion |

## Execution Domain

| Domain | Can Execute | Tools Available | Notes |
|---|---|---|---|
| Research / Information gathering | ✅ Yes | Web search, API reads | Summarize findings in completion comment |
| Homelab / Infrastructure ops | ✅ Yes | Portainer, SSH, Docker MCP tools | Follow plan steps exactly |
| API integrations / HTTP calls | ✅ Yes | HTTP requests, MCP tools | Follow plan's exact API calls |
| Purchases / Shopping research | ✅ Yes | Web browsing | May need Human for payment step |
| Configuration / Settings changes | ✅ Yes | File edits, API updates | Verify before and after |
| File attachments (upload/download) | ✅ Yes | `vikunja_task_attachments` | Upload produced artifacts; download for context only |
| Coding / Software development | ❌ Escalate | None (future: OpenCode) | Move to Human with escalation comment |
| Physical world actions | ❌ Escalate | None | Move to Human with escalation comment |
| Financial transactions | ❌ Escalate | None (unless plan explicitly approved) | Move to Human |

<HARD-GATE>
PLAN REQUIRED: BEFORE executing any step, search the task description for the section header `## 🤖 Agent Analysis`. If this section does NOT exist, the task was moved to Queued without being refined first. Do NOT guess or improvise. Post a comment: "🤖 **Agent — Error**: No implementation plan found. This task appears to have been moved to Queued without refinement. Move it back to TODO for analysis." Then move to Human (bucketId=9) and EXIT.
</HARD-GATE>

<HARD-GATE>
CODING ESCALATION: Analyze the implementation plan steps. If ANY step requires writing code, modifying source files, running compilers/transpilers, or software development tooling — do NOT attempt execution. Post the coding escalation comment above. Move task to Human (bucketId=9). EXIT immediately. Do NOT execute any other steps from the plan first.
</HARD-GATE>

<HARD-GATE>
ERROR ESCALATION: On ANY unrecoverable error during execution: (1) Stop all further execution immediately. (2) Post the structured error comment using the template above — fill in ALL fields. (3) Move task to Human (bucketId=9) via `vikunja_task_move.move`. (4) EXIT. Do NOT retry failed steps more than once. Do NOT continue with remaining plan steps after a failure. Do NOT leave the task in In Progress without explanation.
</HARD-GATE>

<HARD-GATE>
NEVER OVERWRITE DESCRIPTION: Post execution results and progress updates as COMMENTS, not description edits. If the plan requires writing output to the description, append with `---` delimiter — NEVER replace the full description. The human's original content and the agent's implementation plan are both sacred.
</HARD-GATE>

<HARD-GATE>
QUESTION PROTOCOL: When execution is blocked by ambiguity, missing information, or a decision that requires human judgment — and the situation is NOT a failure or error — you MUST: (1) Post a comment using the Question Comment Template with all fields filled. (2) Cap questions at 3 per pause — if more are needed, ask the most critical 3 and note that follow-up questions may come after answers. (3) Move the task to Human (bucketId=9) via `vikunja_task_move.move(projectId=2, viewId=8, taskId=N, bucketId=9)`. (4) EXIT immediately. Do NOT wait for answers in the same session. Do NOT continue executing other steps. The next cron tick will handle re-entry after the human moves the task back to Queued. DISTINGUISH FROM ERROR: Use this gate when the work CAN proceed but needs a human decision. Use Error Escalation when something is BROKEN or IMPOSSIBLE. Where possible, include 2–3 concrete suggested options for each question so the human can pick or override rather than answer from scratch. When re-posting questions after an unanswered return (the human moved the task back without answering), use the header `🤖 **Agent — Question: Re-asking` instead of `🤖 **Agent — Question: Clarification Needed` — this marker makes a second consecutive unanswered return mechanically detectable.
</HARD-GATE>

<HARD-GATE>
RE-ENTRY DETECTION: BEFORE starting execution, check ALL comments on the task for the pattern `🤖 **Agent — Question`. If found, this is a RETURNING task — the human has answered your questions. Read ALL previous agent comments (progress, questions, errors) and all human replies. Define a "human reply" as any comment whose text does NOT begin with the pattern `🤖 **Agent` — this is a reply from a non-agent author regardless of the commenter's role or field. If multiple human comments appear consecutively after a question comment, treat all of them together as the answer and read them all for context. Determine the resume point: (a) Find the last `🤖 **Agent — Question` comment. (b) Check if a human reply (as defined above) follows it — if YES, extract the answers and identify the blocking step number from the question comment's "Blocking Step" field. (c) Find all `🤖 **Agent — Progress` comments to identify which steps were completed. (d) Resume execution from the blocking step, incorporating the human's answers. Do NOT re-execute steps that were already completed (they may have had side effects: API calls, infrastructure changes, file uploads). Do NOT restart analysis from scratch. If the MOST RECENT agent comment is a question comment and NO human reply follows it, the human moved the task back to Queued without answering — re-post the same questions and move back to Human (bucketId=9). To detect a second consecutive unanswered return: if the MOST RECENT `🤖 **Agent — Question` comment begins with `🤖 **Agent — Question: Re-asking` (the marker used when re-posting after an unanswered return) AND no human reply follows it, this is the second unanswered return — escalate as error: "Questions remain unanswered after two return cycles." If no `🤖 **Agent — Progress` comments exist in the history to identify completed work, use the "Steps Completed" field from the question comment itself to identify what was already done; if that field reads "None", treat the task as fresh and resume from step 1.
</HARD-GATE>

## Comment Templates

### Error Comment Template

```
🤖 **Agent — Error: Human Intervention Needed**

**Task**: [task title]
**Failed Step**: [which step in the implementation plan failed]
**Error**: [specific error message or description]
**What Was Tried**: [recovery attempts made before escalating]
**Current State**: [what has been completed, what remains]
**Suggested Action**: [what the human should do to resolve this]

*Fix the issue and move this task back to Queued when ready.*
```

### Success Comment Template

```
🤖 **Agent — Task Complete**

**Summary**: [what was accomplished]
**Steps Completed**: [brief list of actions taken]
**Output / Results**: [deliverables, links, data, or summary of findings]
**Attachments Uploaded**: [list of uploaded filenames with brief descriptions, or "None" if no artifacts were produced]
**Duration**: [rough estimate]
```

### Coding Escalation Comment Template

```
🤖 **Agent — Coding Task Detected**

This task requires software development or code modification. Escalating to Human until OpenCode integration is available.

**Plan**: Implementation plan is in the task description and ready for a developer to execute manually.

*Assign to a developer or integrate OpenCode, then move back to Queued.*
```

### Question Comment Template

```
🤖 **Agent — Question: Clarification Needed**

**Task**: [task title]
**Steps Completed**: [list steps completed so far, or "None — question arose before first step"]
**Blocking Step**: [step number and description that triggered the question]
**Questions**:
1. [specific question]
   - Suggested options: [option A] / [option B] / [option C] *(omit if no good options apply)*
2. [specific question]
   - Suggested options: [option A] / [option B] *(omit if no good options apply)*
**Current State**: [what has been done, what resources are held, any time-sensitive context]

*Please answer in the comments below, then move this task back to Queued when ready.*
```

> **Re-ask variant**: When re-posting after an unanswered return, replace the header with `🤖 **Agent — Question: Re-asking` to make the second consecutive unanswered cycle mechanically detectable by the RE-ENTRY DETECTION gate.

## Artifact File Convention

When execution produces files to upload as task attachments:
1. Write files to `/tmp/hermes/task-{taskId}/` (create the directory if needed)
2. Use descriptive filenames: `research-summary.md`, `api-response.json`, `screenshot-dashboard.png`
3. Upload each file after execution completes, before posting the success comment
4. If the artifact is text or data generated in memory, write it to the convention directory first using an available file-write tool, then upload

## Procedure

1. **Receive Task Context**  
    The task is already in In Progress (`bucketId=5`) because vikunja-board-poller claimed it. If the full task context is not already loaded, call `vikunja_tasks.get({ id: N })` and `vikunja_task_comments.list({ id: N })`. Build complete context before acting: task title, full description, the implementation plan inside the description, and all existing comments.
    Also call `vikunja_task_attachments({ operation: 'list', taskId: N })` to retrieve existing attachment metadata. Review attachment filenames, sizes, and upload dates for relevant context. If any attachment appears directly relevant to execution (e.g., referenced in the implementation plan, or contains input data needed for a step), download it with `vikunja_task_attachments({ operation: 'download', taskId: N, attachmentId: N, outputPath: '/tmp/hermes/task-{taskId}/{filename}' })`. If no attachments exist, proceed without them — do not comment on their absence.

   After loading the full context, apply the RE-ENTRY DETECTION hard gate. Scan all comments for the pattern `🤖 **Agent — Question`. If a question comment is found with a subsequent human reply, this is a returning task: parse the resume point (blocking step number from the "Blocking Step" field, completed steps from prior progress comments, human's answers from their reply). If no question comment exists, this is a fresh task — proceed normally to Step 2.

2. **Validate Implementation Plan**
   Apply the Plan Required hard gate before doing anything else. Search the task description for the exact header `## 🤖 Agent Analysis`. If the header is missing, post the no-plan error comment, move the task to Human (`bucketId=9`), and exit immediately. If the header is present, parse the plan carefully and extract the ordered steps, prerequisites, expected outcome, constraints, and any stated complexity or approval boundaries.
   After validating the plan, post a pickup acknowledgment comment: `🤖 **Agent — Starting Execution**: [task title]. Expected output: [list expected artifacts from the plan's Expected Artifacts section, or "task completion only — no uploadable artifacts" if none listed]. Will review [N] existing attachment(s) for context.` This comment serves as both a progress signal and an artifact declaration.

3. **Check Execution Domain**  
   Apply the Coding Escalation hard gate to the parsed plan. Read every step and classify the work against the execution domain table. Ask whether any step requires writing or modifying code, running development tooling, compiling or transpiling software, or doing software development of any kind. If yes, post the coding escalation comment, move the task to Human (`bucketId=9`), and exit immediately. If no, continue to execution.

4. **Execute Plan Steps**  
    Execute the implementation plan in order without improvising new scope. For significant milestones, add a progress comment in this format: `🤖 **Agent — Progress**: Completed step N of M: [brief description]`. Use only the tools and actions allowed by the plan and this skill's execution domain. 
   
    **Question vs. Error branching:** If a step is AMBIGUOUS (multiple valid options, unclear requirements, missing context not available to the agent, or requires a human decision), trigger the QUESTION PROTOCOL hard gate instead of attempting the step. If a step FAILS (tool error, API error, missing resource, impossible action), follow the Error Escalation path below. These are mutually exclusive — do NOT use Question Protocol for broken things.
    
    If a step fails, attempt one recovery only: either a single retry or the plan's stated fallback. If recovery fails or no safe recovery exists, trigger the Error Escalation hard gate, post the full structured error comment, move the task to Human (`bucketId=9`), and exit. On re-entry after questions: Resume from the blocking step identified in the RE-ENTRY DETECTION gate. Skip all steps already marked completed in prior progress comments — do not re-execute them.

5. **Post Results**  
   If the implementation plan's `### Expected Artifacts` section lists any artifacts, upload each produced file: `vikunja_task_attachments({ operation: 'upload', taskId: N, filePath: '/tmp/hermes/task-{taskId}/{filename}' })`. Upload artifacts one at a time. If an upload fails, note the failure and file path in the success comment but do NOT trigger error escalation — the task work itself was completed. Continue uploading remaining artifacts even if one fails.
   When execution completes successfully, post the success comment and fill in every field. Include a concise summary, the steps completed, and any outputs, links, findings, or configuration changes produced. If the implementation plan explicitly requires output in the task description, append it using a `---` delimiter instead of replacing any existing text. Use `vikunja_task_comments.add({ id: N, comment: "🤖 **Agent — Task Complete**: ..." })` for the main completion record.

6. **Move to Done**  
   After the success comment is posted, move the task to Done with `vikunja_task_move.move({ projectId: 2, viewId: 8, taskId: N, bucketId: 6 })`. Then mark the task complete with `vikunja_tasks.update({ id: N, done: true })`. Do not leave a successfully executed task in In Progress.

## Must NOT Do

- Do NOT write code or modify source files; escalate coding tasks to Human.
- Do NOT retry failed steps more than once.
- Do NOT leave tasks in In Progress without explanation; always move to Done or Human.
- Do NOT execute tasks without a written implementation plan.
- Do NOT make financial transactions without the plan explicitly stating approval.
- Do NOT delete or destroy data unless the plan explicitly calls for it.
- Do NOT delete existing attachments uploaded by humans or previous agent runs.
- Do NOT upload files not named in the implementation plan's `### Expected Artifacts` section.
- Do NOT download every attachment speculatively — only download when the filename or plan reference suggests relevance.
- Do NOT use the Question Protocol for actual failures or errors — questions are for ambiguity and human decisions only. If something is broken, use Error Escalation.
