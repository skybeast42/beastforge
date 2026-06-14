---
description: Run the task-integrity / reconciliation checks on demand
---

Validate the `work/` task-integrity check (full rules in CLAUDE.md → "The task-integrity check"). A task is **self-contained**, so there is no cross-folder symmetry to enforce.

Check and report:

- **Brief-less task** — a `work/TASK_NNN_*/` with no `00_Briefs/00_brief.md` (looks like the User's own unlogged work). → Offer to **retro-wrap** as a stub brief (`Origin: imported`, or `chat` if it grew from a CC chat): Objective inferred from the code + `git log`. **Proposed, never forced — proceed with whatever was asked regardless; help is never gated on backfilled logging.** (Exempt: `00_`-reserved folders.)
- **Name near-miss** — a task folder that is a typo, different name, or case-variant vs. an *existing* task name → likely a mistake → **stop, warn clearly, ask how to resolve. Never auto-correct.**
- **Fine, do not flag** — a task missing some stage folders (lazy stages are valid; planned-but-unstarted is fine).

Never auto-delete. Only a near-miss blocks; a brief-less task informs and offers — it does not gate.

Then run the **reconciliation checks** (CLAUDE.md → "Reconciliation checks") — these **warn, never block**:

- **Unlogged work** — a task's `03_Scripts`/`04_Output` changed (uncommitted, or since the last commit touching its `00_Briefs/`) with no corresponding change in `00_Briefs/**` or `DECISIONS.md` → warn *"work changed, nothing logged"*; the User decides whether a ticket/decision is owed. **Exempt `*/AIterritory/**`** — the AI's assessment zone is staging / prune-freely by design (CLAUDE.md → *AI territory*), so its churn is expected, not unlogged work.
- **Reproducible-execution gaps** — a task's `03_Scripts/` with **deliverable** scripts (`SCRIPT_NN_*` directly in `03_Scripts/`) but no `SCRIPT_00_RUNALL.*`; or `02_Data`/`04_Output` present with no `03_Scripts/` → warn. **Exempt `03_Scripts/AIterritory/**`** — `ASSESS_*` scripts live *outside* `SCRIPT_00_RUNALL` by design (CLAUDE.md → *AI territory*), so an assessment-only task (no deliverable pipeline yet) correctly has no RUNALL; mirrors the *Unlogged work* exemption above.
- **Task gap** — `STATE.md` references a task closed in `DECISIONS.md`, with no successor briefed → warn *"current task closed; next not briefed — `/brief` to scaffold."*
- **Command-table parity** — a `.claude/commands/*.md` with no row in a canonical command table (CLAUDE.md *Commands* + the README command table), or a table row naming a command with no file → warn *"command ↔ table drift"*. No-op when files and tables agree.
- **TODOLIST done-pileup** — backstop for the two-marker prune (which self-clears at each `/wrap`): if `TODOLIST.md` carries `[X]` items that have survived **more than one session** (the `/wrap` prune step was skipped), or done items have visibly piled up → warn *"done items overdue — the next `/wrap` clears them; DEC/changelog is the record."* No-op when only the current/previous session's done items remain.

These surface issues; they do not gate, and cannot prove completeness — they remove the *silent* failure. If everything is consistent, say so in one line.
