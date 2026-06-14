---
description: Walk audit findings to closure — route fixes to tickets, accepts to /decide
argument-hint: [audit folder — defaults to the latest unresolved]
---

Drive an audit to closure. Target: $ARGUMENTS (default: the most recent `tracks/audits/*` lacking `02_resolution.md`).

1. Read the target audit's `01_findings.md`.
2. Walk **every** finding. For each, propose a disposition for the User to decide (CC proposes, User decides):
   - **fix** → for a `work/` task: `/ticket` on it (or a new `/brief` if substantial). For an **`apps/`** finding or a **spine / template-doc** finding (no task to ticket): a **direct edit recorded via `/decide`**, or the app's own issue/PR flow. The fix work happens via the normal primitives — not here.
   - **accept / won't-fix** → a `/decide` one-liner in `DECISIONS.md`.
   - **defer** → record it, with a reason.
3. Write `tracks/audits/<scope>/02_resolution.md`: every finding → disposition + reference (ticket/decision id).
4. **Capture-sweep** (audit close is a strong boundary — keystone *Persistence*): before closing, confirm any reusable lessons this audit surfaced were distilled to `tracks/00_insights/<type>.md` — or note explicitly there were none. One line, not a gate.
5. **Closure guarantee:** no finding may be left without a disposition. Deferred findings keep the audit **open**.

Non-destructive: this routes consequences into existing primitives; it does not modify `work/` directly.
