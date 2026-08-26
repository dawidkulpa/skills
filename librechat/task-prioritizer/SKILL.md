---
name: task-prioritizer
description: "Use to turn an overwhelming task list into a realistic ranked plan; użyj do ustalenia priorytetów i planu dnia lub tygodnia."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "productivity, prioritization, planning, focus, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/Cogaid/agent-skills/tree/main/skills/personal-assistance/task-prioritizer"
  source-license: "MIT"
---

# Task Prioritizer

Turn a brain dump into a plan the user can actually execute. Work in the user's language. Do not require code, scoring utilities, or external task systems, and do not claim tasks were saved or scheduled unless a connected tool confirms it.

## Workflow

1. **Capture the list.** Use tasks already in the conversation. If the list is incomplete, invite one short brain dump rather than a long interview.
2. **Clarify outcomes.** Rewrite vague items into a visible definition of done. Preserve real deadlines, commitments, owners, dependencies, waiting states, and estimated effort.
3. **Separate constraints from preferences.** Identify fixed appointments, hard deadlines, blockers, work that unlocks other tasks, and consequences of delay.
4. **Triage.** Use an Eisenhower-style urgent/important view when it adds clarity:
   - do soon: important and time-sensitive;
   - schedule: important but not immediate;
   - delegate or coordinate: someone else is better placed;
   - drop or defer: low-value work with no meaningful consequence.
5. **Score only when choices remain close.** Compare impact, confidence, effort, risk reduction, and dependency unlock. Use simple High/Medium/Low labels or explain a numerical scale; do not hide subjective guesses behind precision.
6. **Choose at most three meaningful priorities.** Mark one clear first action. A day may contain many small obligations, but only three outcomes should be presented as must-do priorities.
7. **Place work into time blocks.** Fit tasks to available time, energy, location, and tools. Add transition and interruption buffer. Protect focused work from fragmented small tasks.
8. **Create a fallback.** State the minimum viable day or week: the single outcome to preserve if time or energy collapses.

## Important rules

- A two-minute action can be batched or captured for later if doing it now would interrupt deep work. “Do it immediately” is not an absolute rule.
- Urgency created by another person's poor planning does not automatically outrank the user's important commitments; surface the tradeoff.
- Do not label rest, health, caregiving, or recovery as unproductive busywork.
- Break tasks down when the next action is unclear, but do not decompose obvious one-step work.
- If a deadline is impossible, flag it early and propose renegotiation, scope reduction, delegation, or sequencing—not a fantasy schedule.

## Output

```markdown
## Top priorities
1. **Outcome** — why now; definition of done; first action; time block
2. ...
3. ...

## Fixed and urgent commitments
- ...

## Schedule next
- ...

## Delegate, ask, or wait
- ...

## Defer or drop
- ...

## Minimum viable plan
- If the day goes badly, complete: ...

## Risks and assumptions
- ...
```

For a weekly request, group outcomes by day only after dependencies and deadlines are resolved. Avoid filling every hour.

## Final check

- Deadlines, dependencies, and consequences are visible.
- Priority order has a reason, not merely a score.
- The plan fits the user's stated capacity and energy.
- Top priorities are outcomes, each with a concrete next action.
- Nothing is claimed to be persisted, delegated, or scheduled without tool confirmation.
