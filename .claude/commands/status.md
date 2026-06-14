---
description: Read-only progress snapshot — tasks, tickets, recent decisions, asks, current state
---

Produce a read-only snapshot. **Take no actions and propose nothing.**

Report, concisely:

1. **Tasks** — for each `work/TASK_NNN_*/`, its state:
   - *planned* — only `00_Briefs/` (no `03_Scripts/`)
   - *in progress* — `03_Scripts/` exists
   - *has output* — `04_Output/` contains artifacts
2. **Open tickets** — `00_Briefs/NN_ticket_*.md` per task.
3. **Recent decisions** — `DECISIONS.md` entries from the last ~30 days.
4. **Open asks** — open items in the asks relay: **your `operator` inbox** (messages awaiting you — you have no command of your own, so run **`/inbox`** to read & reply *through this beast*) + my own open `sent/`. Flag any urgent.
5. **Open audits** — `tracks/audits/<scope>/` lacking `02_resolution.md`, or with deferred findings still open.
6. **Possible drift / unlogged work** — tasks whose `03_Scripts`/`04_Output` changed after the brief's last edit, or with such changes but no matching ticket/decision. Surface only; do not act.
7. **STATE hygiene** — if `STATE.md` narrates any closed work at more than one line, or `Current focus` reads as an achievement log, **offer to prune** (per CLAUDE.md → *STATE.md — the rule*). Surface; do not auto-edit.
8. **Current state** — a one-paragraph summary of `STATE.md`.

Open with the template version (from `.template_version`). `00_`-reserved folders are not tasks — exclude them. End with a one-line headline like "N tasks: X planned, Y in progress, Z with output."
