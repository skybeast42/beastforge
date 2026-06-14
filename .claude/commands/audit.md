---
description: Plan and run a multi-specialist audit (lives in tracks/audits/)
argument-hint: [what to audit — defaults to all of work/]
---

Plan and run an audit. Scope: $ARGUMENTS (default: all of `work/`).

1. **Scope it.** Confirm what is in scope (all of `work/`, a subset of tasks, `apps/`, or the management docs). One confirmation; don't interrogate.
2. **Propose a specialist roster sized to the scope** — N as required, not a fixed number (propose; the User confirms). Each specialist reads the relevant `guidance/` (`01_standing.md`, `02_derived.md`, and any domain doc, if present) so the audit is project- and domain-grade.
3. Create `tracks/audits/<scope>/00_charter.md` — scope, objectives, roster, method. `Origin: plan`. Propose a short `<scope>` slug; never rename. (If the slug collides with an existing `tracks/audits/<scope>/`, disambiguate — e.g. `<scope>_2`.)
4. **Fan out** the specialist subagents, one per dimension, each auditing against the guidance and the work.
5. Synthesize into `tracks/audits/<scope>/01_findings.md` — severity-ranked; each finding: id, severity, location, what, why it matters, suggested action.

**Audit only — fix nothing here.** Resolution is `/audit-resolve`. Non-destructive; propose the roster before spawning anything.
