---
name: vikunja-task-refiner
description: Analyzes tasks in refinement, asks clarifying questions via comments, and produces detailed implementation plans. Handles both first-pass analysis and re-entry after human answers. Designed to work alongside the vikunja-board-poller skill.
---

# Vikunja Task Refiner

## Overview

Convert claimed TODO tasks into execution-ready implementation plans without losing any human-authored context.

**Core principle:** analyze first, ask targeted questions only when needed, append the plan without overwriting existing content, and require human approval before execution.

## Configuration Constants

| Constant | Value | Description |
|----------|-------|-------------|
| PROJECT_ID | 2 | Vikunja project ID |
| VIEW_ID | 8 | Kanban view ID |
| BUCKET_TODO | 4 | Source: task came from here |
| BUCKET_REFINING | 8 | Current location while analyzing |
| BUCKET_HUMAN | 9 | Destination when questions needed |
| BUCKET_REFINED | 10 | Destination when plan is complete |

## MCP Tools Quick Reference

| Tool | Operation | Parameters | Purpose |
|------|-----------|------------|---------|
| `vikunja_tasks` | `get` | `id=N` | Read the full task, especially the current description |
| `vikunja_tasks` | `update` | `id=N, description="..."` | Append the analysis section to the full description |
| `vikunja_task_comments` | `list` | `id=N` | Read all prior comments in chronological order |
| `vikunja_task_comments` | `add` | `id=N, comment="..."` | Post questions or completion comments |
| `vikunja_task_move` | `move` | `projectId=2, viewId=8, taskId=N, bucketId=N` | Move the task to Human or Refined |
| `vikunja_task_attachments` | `list` | `taskId=N` | Review existing attachments during analysis |
| `vikunja_task_attachments` | `download` | `taskId=N, attachmentId=N, outputPath="..."` | Download attachment when content is needed for analysis |

## Agent Comment Format Spec

- All agent comments MUST start with: `🤖 **Agent**:`
- Use the dedicated templates below for question and completion comments.
- Keep agent comments operational, specific, and human-actionable.

### Question Comment Template

```
🤖 **Agent — Questions for Review**:

Before writing an implementation plan, I need clarification:

1. [specific question]
2. [specific question]

*Please answer in the comments below, then move this task back to TODO when ready.*
```

### Analysis Complete Comment Template

```
🤖 **Agent — Analysis Complete**:

Implementation plan has been written into the task description. Please review and move to Queued when ready to execute.
```

## Task Description Append Format

Use the exact section header `## 🤖 Agent Analysis` on its own line so vikunja-task-executor can parse it reliably. Put the timestamp on the next line.

```
[Original human content — NEVER touched]

---
## 🤖 Agent Analysis
Timestamp: YYYY-MM-DDTHH:MM:SSZ

### Summary
[Brief statement of what needs to be done and why]

### Implementation Plan
[Step-by-step plan with exact commands, file paths, API calls, tool invocations]
[Depth: like a Sisyphus plan — an agent should be able to follow it mechanically]

### Prerequisites
[What must be in place before execution starts]

### Expected Outcome
[What success looks like — measurable results]

### Expected Artifacts
[List files/documents this task will produce, if any. Write "None — task produces no uploadable artifacts" if the task is purely operational. The executor will use this as an upload checklist.]

### Estimated Complexity
[Simple / Medium / Complex + brief justification]
---
```

<HARD-GATE>
RE-ENTRY DETECTION: BEFORE starting any analysis, check ALL comments on the task for the 🤖 prefix. If found, this is a RETURNING task — the human has answered your questions. Read ALL previous agent comments and all human replies. Understand what was asked, what was answered, and what information is now available. Do NOT repeat questions already asked. Do NOT restart analysis from scratch. Continue from where you left off.
</HARD-GATE>

<HARD-GATE>
NEVER OVERWRITE DESCRIPTION: When appending the implementation plan, use `vikunja_tasks.update(id=N, description="[FULL original content] + [appended section]")`. You MUST read the current description first, then construct the new value as: current description + `\n\n---\n` + new section. NEVER pass just the new section as the description — that destroys the human's original content.
</HARD-GATE>

<HARD-GATE>
QUESTION PROTOCOL: When information is insufficient, you MUST: (1) Post a comment with 🤖 prefix listing specific questions using the question template. (2) Move the task to Human (bucketId=9) via `vikunja_task_move.move(projectId=2, viewId=8, taskId=N, bucketId=9)`. (3) EXIT the current session. Do NOT wait for answers in the same session. Do NOT ask more than 5 questions at once. The next cron tick will handle re-entry after the human moves the task back to TODO.
</HARD-GATE>

<HARD-GATE>
CODING TASK DETECTION: If the task requires coding, scripting, or software development — include this in the implementation plan normally (the plan itself is always written). But add this warning block in the plan: `⚠️ This task requires coding execution. The executor will escalate to Human when it picks up this task, until OpenCode integration is available.` Do NOT refuse to write the plan — write it fully. The executor enforces the coding restriction at execution time.
</HARD-GATE>

## Procedure

1. **Receive Task Context**  
    The task is already in Refining (`bucketId=8`) because vikunja-board-poller claimed it. If the full context is not already loaded, call `vikunja_tasks.get(id=N)` and `vikunja_task_comments.list(id=N)`. Build a complete working picture before deciding anything: task title, full task description, and all comments in chronological order. Treat the current live task body as the source of truth because humans may have edited the description or added comments since the previous cron tick.

2. **Detect Task State**  
   Apply the re-entry hard gate before doing substantive analysis. Scan ALL comments for the 🤖 prefix. If no such comments exist, this is a FRESH first-pass refinement and analysis begins from scratch. If one or more agent comments exist, this is a RETURNING task: read the prior agent questions, read every human reply, and build an updated understanding from the previous checkpoint instead of starting over. Your job on re-entry is to use the newly supplied answers, not to repeat the same discovery loop.

3. **Analyze the Task**  
    Decompose the request into concrete actions and identify what is actually being asked. Classify the domain: infrastructure, homelab, research, API work, configuration, coding, or another operational category. Determine which tools, external systems, credentials, approvals, files, and dependencies will be required to execute later. For returning tasks, focus on the delta: which gaps were previously blocking planning, which answers resolved them, and whether any ambiguity still remains after incorporating the human's responses.

     Review the attachment metadata provided by vikunja-board-poller's context packet. If attachments are present, consider their filenames, sizes, and upload dates as additional context for understanding the task scope. If an attachment appears directly relevant to analysis (e.g., a requirements document, screenshot, or config file), download it with `vikunja_task_attachments({ operation: 'download', taskId: N, attachmentId: N, outputPath: '/tmp/hermes/task-{taskId}/{filename}' })` and incorporate its content. If no attachments exist, proceed without them.

4. **Decision Gate — Information Sufficient?**  
   Decide whether the task is now specific enough to produce a mechanical step-by-step implementation plan with exact commands, file paths, API calls, tool invocations, approval boundaries, and measurable outcomes. If yes, proceed to plan writing. If no, formulate targeted questions that unblock execution without being vague or sprawling. Ask only the minimum necessary questions, cap the batch at five, then follow the question hard gate exactly: post the question comment, move the task to Human (`bucketId=9`), and EXIT the session so re-entry can happen on a later cron tick.

5. **Write Implementation Plan**  
    Create a detailed implementation plan using the append format above. Depth standard: an agent with no prior context should be able to execute it mechanically. Include every command, every API call, every file path, every tool invocation, every dependency, and every expected response that materially affects execution. If the work includes coding, include the required warning block inside the plan but still write the full plan. Read the current description with `vikunja_tasks.get(id=N)`, extract the `description` field, construct the new description as `[current description]\n\n---\n## 🤖 Agent Analysis\nTimestamp: [ISO timestamp]\n...\n---`, then write it back with `vikunja_tasks.update(id=N, description="[full new value]")`.

    When populating the plan, assess whether the task will produce any files or artifacts (research summaries, config files, screenshots, API responses, etc.) and list them in the `### Expected Artifacts` section accordingly. If the task is purely operational with no downloadable output, write "None — task produces no uploadable artifacts".

6. **Post Completion Comment**  
   Add a completion comment using the analysis-complete template so the human knows refinement is done and where to review the result. Use `vikunja_task_comments.add(id=N, comment="🤖 **Agent — Analysis Complete**: ...")`. Keep the comment short and explicit: the implementation plan is now in the task description, human review is required, and the task should move to Queued only after approval.

7. **Move to Refined**  
    After the full plan has been appended and the completion comment has been posted, move the task to Refined with `vikunja_task_move.move(projectId=2, viewId=8, taskId=N, bucketId=10)`. This column means analysis is complete but execution is not yet authorized. Human approval remains mandatory: the human must manually move the task from Refined to Queued before vikunja-task-executor is allowed to act.

## Must NOT Do

- Do NOT delete or modify existing comments.
- Do NOT remove or overwrite any part of the human's original task description.
- Do NOT attempt to execute the plan — only write it.
- Do NOT auto-approve; human approval is always required to move from Refined to Queued.
- Do NOT ask more than 5 questions at a time.
