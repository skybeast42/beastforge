---
description: Session close-out — the /resume bookend: reconcile, persist, assert cold-resume-readiness, propose the boundary commit
---

Close out the session deliberately. `/wrap` is the bookend to `/resume`: the
template has a deliberate session *entry*, this is the deliberate *exit*.

It runs the close-out the Persistence rule already mandates (*"close at
boundaries, proactively"*) — but **on demand and as a guarantee**. Same
on-demand-vs-automatic relationship `/check` has to the session-start task-integrity
check: the floor runs unprompted with or without this command; `/wrap` is
the explicit, full-checklist invocation. Its distinct value over "save
everything" is a **cold-resume-readiness guarantee** — when `/wrap` returns
clean, a *fresh chat's* `/resume` picks up cleanly.

## 0. Scope

`/wrap` **persists and verifies; it does not start new work.** If the working
tree is clean and nothing is owed, say so and stop — a no-op wrap is a valid,
good outcome.

## 1. Reconcile — what's owed?

Run the same reconciliation as `/check`/`/resume` and surface anything unlogged:

- **Owed DECISIONS rows** — settled calls from this session not yet in
  `DECISIONS.md`.
- **Unticketed contract changes** — a decision/change that altered a step's
  inputs/outputs/behaviour with no matching ticket → **propose the ticket now**
  (the CLAUDE.md contract-change→ticket hook).
- **Unlogged work** — a task's `03_Scripts`/`04_Output` changed with no
  `00_Briefs`/`DECISIONS.md` change → flag; decide if a ticket or STATUS refresh
  is owed.
- **Stale brief STATUS** — `STATUS:` markers that froze behind what actually
  landed.
- **Open asks** — run `/inbox` to reconcile the asks relay: route any **resolved**
  ask's outcome to its home (a settled call → a `DECISIONS.md` row) and move the
  message to `cur/`; carry genuinely **open** ones forward (urgents surfaced in
  `STATE.md`). The inbox ends a wrap holding open questions only — never resolved ones.

## 2. Capture insights

Offer to harvest the session's noteworthy findings to
`tracks/00_insights/<type>.md` (surprises · workarounds · decisions with
hidden depth · task-closing gotchas), per the *Active insight captures* config.
Mirrors the `/resume` / boundary insight prompt.

## 3. Persist — each durable thing in its home

Per the Persistence *"Where does it go?"* table:

- Write any owed **`DECISIONS.md`** rows.
- Mark **brief STATUS** / close finished tasks; cut any owed **tickets**.
- Update **`TODOLIST.md`** — mark `[x]` closed items with DEC/bump pointers; record
  any new ideas the session surfaced. Then **run the two-marker prune machine — this is
  its tick** (keystone *Persistence → TODOLIST pruning cadence*), automatic and unasked:
  (1) **prune** every existing `[X]` item (collapse a fully-done theme to a one-line
  *CLOSED → DEC/changelog* stub), then (2) **promote** each surviving `[x]` → `[X]`. So
  this session's done items stay visible (as `[X]`) through the next session's `/resume`,
  then prune at that session's `/wrap`. The edit rides the boundary commit.
- Refresh **`STATE.md`** to a one-screen snapshot (snapshot, not journal).

## 4. Assert cold-resume-readiness (the distinct value)

More than "everything saved" — verify the *next* chat can start cold:

- **`STATE.md` *Next action* must be concrete enough that a fresh `/resume`
  starts there without this conversation** — a specific next step **plus the
  file(s) to open**, not "continue the work". If it isn't, rewrite it until it
  is.
- *Current focus* and *Where execution stands* reflect reality — no closed step
  narrated as active; no just-finished work missing.
- *Open questions / blockers* are current.

## 5. Propose the boundary commit

A **CC-authored, User-approved** commit (per `guidance/01_standing.md`) covering
the session's landed work; path-scoped where it makes sense. **Offer to push.**
Never rewrite history (no amend/rebase).

## 6. Report what's owed / deferred

End with a tight close-out summary (per `01_standing` → *Reporting output*): **lead with**
what was persisted; **table** the reconcile findings / owed items (and their disposition);
**end with** the proposed boundary commit — so nothing is silently dropped.

---

**Relationship to other commands.** `/wrap` *composes* `/check`'s reconciliation,
`/status`'s snapshot discipline, and `/commit`'s boundary commit into one exit
pass — it does not replace them, and it does not replace the Persistence floor
(which runs whether or not you call `/wrap`).
