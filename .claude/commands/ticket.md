---
description: Add a numbered amendment (ticket) to an existing task's brief
argument-hint: [what to add or change]
---

Add a ticket (an amendment to a task's brief). Request: $ARGUMENTS

1. **Determine the target task.** Infer it from the active context (the task most recently worked on/discussed) and *propose* it for confirmation — e.g. *"Adding `work/TASK_010_crisis/00_Briefs/02_ticket_add_stress_scenario.md`. OK / different task?"*.
2. If there is no clear active task, list the existing tasks and ask the User to pick — do not guess blindly.
3. Create the next `NN_ticket_<slug>.md` in that task's `00_Briefs/` (count from `01_`; `<slug>` is a short lowercase_underscore description from the request).
4. The ticket **amends** the brief — it does not modify `00_brief.md`. Write what is changing/being added and why.
5. **Header.** Start the ticket file with:
   ```markdown
   # Ticket NN — <title>
   **Task:** <task_name> · **Opened:** YYYY-MM-DD · **Origin:** plan | chat
   ```
   Body is open — write what is changing and why; close with a brief reference back to `00_brief.md` if the amendment is substantial.
