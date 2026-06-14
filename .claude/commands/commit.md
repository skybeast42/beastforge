---
description: Propose a commit at a brief/ticket boundary (CC-authored, User-approved)
argument-hint: [optional: step/ticket or scope hint]
---

Boundary commit helper. A **checkpoint, never a gate**; **propose, don't auto-run** — never commit without the User's explicit OK; never rewrite existing history (no amend / rebase). Focus: $ARGUMENTS

1. **Identify the boundary.** The task/ticket just completed (from context or `$ARGUMENTS`). If unclear, ask which task — don't guess.
2. **Boundary persistence check** — before staging, ask whether this turn surfaced anything captureable. **Propose each below in one short paragraph for User accept/skip/edit; never silently write.**
   - **Insight capture** — did a surprise land, a non-obvious workaround get discovered, a decision gain hidden depth, a task close with a gotcha worth retelling? → propose an entry to `tracks/00_insights/<type>.md` (per `02_derived`'s *Active insight captures*; **template/meta-feedback is always in scope**, not gated on publication). In any extended session — a repetitive run *or* a varied multi-hour build/audit flow — also checkpoint per the cadence trigger (the keystone *Capture-sweep* rule applies to both).
   - Did this turn reveal something new about how the User prefers to work (explicit feedback, non-obvious choice)? → propose an entry to `guidance/03_user.md`.
   - Did any `TODOLIST.md` items close in this commit's work? → propose marking them `[x]` with DEC/bump pointers. (Marking only — the `[x]`→`[X]`→pruned **prune machine ticks at `/wrap`, not here**; keystone *Persistence → TODOLIST pruning cadence*.)
   - **Long-task staleness:** if this commit touches a task's `03_Scripts`/`04_Output` but its `00_Briefs/**` hasn't changed across the last few commits to that task, the brief is drifting → nudge *"brief drifting — refresh its `STATUS:` markers, cut a ticket, or update `WORKLOG.md`?"* before staging. Catches the brief-freeze a multi-hour single session never trips at `/resume`/`/check`.

   If nothing surfaced, say so in one line and continue.
3. **Scope it path-scoped.** Stage only the relevant home unit — a task's `work/TASK_NNN_<name>/`, an `apps/<name>/`, or a `tracks/<topic>/` — plus the management docs it actually touched (`DECISIONS.md`, `MASTERPLAN.md`, `STATE.md`, `TODOLIST.md`) and, for a template change, the mirrored payload machinery (`apps/template/…`) + both `.template_version`. **Never `git add -A`** if it would sweep unrelated work; propose the exact path list.
4. **Author the message.** First line is one of:
   - **Task-boundary** (default): `TASK_NNN_name: <concise what/why>` (or the home unit's name for `apps/`/`tracks/` work)
   - **Release**: `M.N.P (theme): <concise what/why>` — for `.template_version` bumps. **Maintenance-project release gate** (signal: both the root `.template_version` AND a nested payload `apps/<x>/.template_version` exist): require (a) both files updated and equal, (b) `.template_changelog.md` (root + `apps/template/`, identical at rest) carries a new top-section matching the new version with theme + changes + migration notes, and (c) the **capture-sweep** is done — reusable lessons distilled to `tracks/00_insights/` and in-flight design parked to `TODOLIST.md`/`tracks/` (per keystone *Persistence*), or explicitly confirmed none. If any is missing, **refuse the commit** and surface what's owed. Field projects (single `.template_version`) skip this gate — they only touch the changelog via `/reforge`.
   - **Cross-cutting / management-doc-only**: `<scope>: <concise what/why>` — where `<scope>` names the touched doc(s) or theme (e.g. `TODOLIST + 10_deck_insights`)

   `git log --oneline` should read as a coherent ledger across all three. A short body for the why / decisions touched; end with the Co-Authored-By trailer.
5. **Propose, then commit on approval.** Show the User the exact scope + message; commit only on explicit OK.
6. **Tolerate prior manual commits.** If the boundary was already committed by the User (often a vague message), do **not** amend or rebase it — note it, then either skip or add a clarifying follow-up commit. History here is append-only.
7. **Branch / push.** Commit on the working branch as the project does; create a branch only if the User asks; never push unless asked.
8. If nothing is staged-worthy, say so and stop. Never block other work on a pending commit.
