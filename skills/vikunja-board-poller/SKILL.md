---
name: vikunja-board-poller
description: Polls a Vikunja kanban board for actionable tasks. Scans TODO and Queued columns, picks the oldest task, and dispatches to the appropriate workflow (refinement or execution). Designed for cron-triggered operation with no persistent state.
---

# Vikunja Board Poller

## Overview

Cron-triggered polling must stay stateless, lock work before acting, and dispatch exactly one task per run.

**Core principle:** read live board state, claim one task with a column move, load full context, then hand off.

## Configuration Constants

| Constant | Value | Description |
|----------|-------|-------------|
| PROJECT_ID | 2 | Vikunja project ID |
| VIEW_ID | 8 | Kanban view ID |
| BUCKET_OPEN | 7 | Human inbox — IGNORE (no agent action) |
| BUCKET_TODO | 4 | Agent trigger: task needs refinement |
| BUCKET_REFINING | 8 | Agent doing first analysis (lock column) |
| BUCKET_HUMAN | 9 | Waiting for human input |
| BUCKET_REFINED | 10 | Analysis done, awaiting human approval |
| BUCKET_QUEUED | 11 | Approved, ready for execution |
| BUCKET_IN_PROGRESS | 5 | Agent executing (lock column) |
| BUCKET_DONE | 6 | Complete |

## MCP Tools Quick Reference

| Tool | Operation | Parameters | Purpose |
|------|-----------|------------|---------|
| `vikunja_buckets` | `list-bucket-tasks` | `projectId=2, viewId=8` | Get all buckets with embedded tasks |
| `vikunja_buckets` | `list-bucket-tasks` | `projectId=2, viewId=8, bucketId=N` | Get tasks from one specific bucket |
| `vikunja_task_move` | `move` | `projectId=2, viewId=8, bucketId=N, taskId=N` | Move task between columns |
| `vikunja_tasks` | `get` | `id=N` | Get full task details (description, dates) |
| `vikunja_task_comments` | `list` | `id=N` | Read all task comments |
| `vikunja_task_attachments` | `list` | `taskId=N` | List existing file attachments on the task for downstream context |
| `vikunja_task_comments` | `add` | `id=N, comment="🤖 **Agent**: ..."` | Post agent comment |

<HARD-GATE>
CONCURRENCY GUARD: BEFORE picking any new task, call `vikunja_buckets.list-bucket-tasks(projectId=2, viewId=8)` and check Refining (bucketId=8) and In Progress (bucketId=5) buckets. If EITHER bucket has tasks (count > 0), the agent is already working. Post a status comment on the in-progress task and EXIT immediately. Do NOT pick new work while another task is being processed.
</HARD-GATE>

<HARD-GATE>
CLAIM BEFORE WORK: BEFORE doing any analysis, planning, or execution, move the task to its processing column. For TODO tasks: move to Refining (bucketId=8). For Queued tasks: move to In Progress (bucketId=5). This move is your distributed lock. If the move fails (task already moved by another session), EXIT gracefully — do NOT proceed with analysis.
</HARD-GATE>

<HARD-GATE>
ONE TASK PER TICK: Process exactly ONE task per cron run. After claiming a task and dispatching to the workflow, EXIT. Do NOT scan for additional tasks. The next cron tick will continue or find new work. Processing more than one task per tick risks race conditions and duplicated work.
</HARD-GATE>

<HARD-GATE>
NEVER OVERWRITE DESCRIPTION: When any workflow needs to write analysis or plan data into the task description, ALWAYS append below existing content using `---` delimiters. NEVER use `vikunja_tasks.update` to replace the full description string. The human's original content is sacred and must never be deleted.
</HARD-GATE>

## Mandatory Polling Procedure

1. **Scan Board State**
   - Call `vikunja_buckets.list-bucket-tasks(projectId=2, viewId=8)` to fetch the current kanban view with embedded tasks.
   - Note the counts in Open, TODO, Refining, Human, Refined, Queued, In Progress, and Done so you have a live mental map of the board before making any choice.
   - Treat this first scan as the source of truth for the current cron tick. Do not assume anything from earlier runs because this skill keeps zero persistent state.

2. **Concurrency Guard**
   - Apply the concurrency `<HARD-GATE>` before selecting work.
   - If Refining (`bucketId=8`) has one or more tasks, post `🤖 **Agent**: Skipping — already refining task [ID].` on the first active refining task and EXIT.
   - If In Progress (`bucketId=5`) has one or more tasks, post `🤖 **Agent**: Skipping — already executing task [ID].` on the first active in-progress task and EXIT.
   - Do not continue to task selection after either condition is true. Another session already holds the lock.

3. **Find Actionable Task**
    - Inspect TODO (`bucketId=4`) first. Tasks there need refinement and must be routed into the vikunja-task-refiner workflow.
    - Inspect Queued (`bucketId=11`) second. Tasks there are approved and must be routed into the vikunja-task-executor workflow.
   - If both buckets contain tasks, TODO wins. Always refine older incoming work before starting approved execution work.
   - If neither bucket contains tasks, log `🤖 **Agent**: Board clear — no actionable tasks.` and EXIT.
   - Within the chosen bucket, select the task with the lowest `position` value. This matches visual board order, where the lowest value is the oldest task.

4. **Claim Task**
   - Apply the claim `<HARD-GATE>` before loading details or comments.
   - For a TODO task, call `vikunja_task_move.move(projectId=2, viewId=8, taskId=N, bucketId=8)` to move it into Refining.
   - For a Queued task, call `vikunja_task_move.move(projectId=2, viewId=8, taskId=N, bucketId=5)` to move it into In Progress.
   - Treat the successful move as the distributed lock for this cron tick.
   - If the move fails for any reason, log the failure and EXIT immediately. Do not continue with analysis, planning, or execution.

5. **Load Task Context**
    - After the lock is held, call `vikunja_tasks.get(id=N)` to retrieve the full task body, including title, description, and timestamps.
    - Call `vikunja_task_comments.list(id=N)` to retrieve all comments in chronological order.
    - Also call `vikunja_task_attachments({ operation: 'list', taskId: N })` to retrieve attachment metadata (filenames, sizes, upload dates). If the attachment list is empty, proceed without attachment context — do not comment on the absence of attachments.
    - Compile a working context packet in this order: title, description, then comments from oldest to newest, and attachment metadata if present.
    - Use the full context packet for dispatch so the downstream workflow sees the original request, follow-up notes, prior agent history, and any file attachments together.

6. **Dispatch to Workflow**
    - If the claimed task came from TODO, continue in the same cron session by following the **vikunja-task-refiner** skill procedure.
    - If the claimed task came from Queued, continue in the same cron session by following the **vikunja-task-executor** skill procedure.
   - Dispatch only after the task is claimed and context is loaded.
   - After dispatching one task, EXIT. The next cron tick is responsible for any remaining board work.

## Must NOT Do

- Do NOT pick up tasks from Open (7), Refined (10), Human (9), or Done (6) columns.
- Do NOT implement priority scoring, urgency calculations, or smart ranking.
- Do NOT retry failed operations — if something fails, move the task to Human (9) and explain why with an `🤖 **Agent**:` comment.
- Do NOT include live credentials or other sensitive values anywhere in this file.
