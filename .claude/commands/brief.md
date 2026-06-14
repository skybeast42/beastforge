---
description: Scaffold a new task and its 00_Briefs/00_brief.md
argument-hint: [task name or short description]
---

Scaffold a new work task. Request: $ARGUMENTS

1. **First, try to map this to an existing task.** If it belongs to one, propose adding a `/ticket` there instead and stop. The test for *"is this a task?"* is **bounded**, not *reproducible* — a brief can contract a bounded effort whose deliverable lands in `work/` stages **or** in `apps/<name>/`/`tracks/<topic>/` (then the task is brief-only, stages lazy). Only **open-ended design/exploration or a passing note** (no bounded deliverable) is *not* a task — propose a `tracks/<topic>/` notebook instead and stop.
2. If genuinely a new bounded task, propose **one** confirmation: the next `TASK_NNN` (scan `work/` for the highest existing number; plain sequential) + a `lowercase_underscore` name — e.g. *"I'll create `work/TASK_003_crisis_scenarios/00_Briefs/00_brief.md`. OK / rename?"*. Propose; do not interrogate.
3. On confirmation, create `work/TASK_NNN_name/00_Briefs/00_brief.md` using the brief schema in CLAUDE.md. Set `Origin`: `plan` (deliberate, in plan mode) or `chat` (ad-hoc stub). Fill the Objective from the request; fill other sections as known, leave the rest as prompts.
4. Do **not** create the other stage folders (`01_DataSource` … `05_Reports`) yet — those are created lazily when execution actually begins, and a **brief-only** task whose deliverable lives in `apps/`/`tracks/` may never create them at all.

If you are entering plan mode for this work, save the plan itself as the `00_brief.md` content.
