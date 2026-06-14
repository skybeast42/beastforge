# apps/

Self-contained software/apps — **one subfolder per app** (`apps/<name>/`). Each
app brings its own framework, build, tests, dependencies, and deployment; the
project conventions in `CLAUDE.md` deliberately **do not reach inside** an app —
follow the app's own framework there.

- One subfolder per app; name it for the app. Many apps may live here.
- **Not brief-gated** — apps are governed by the spine (decisions → `DECISIONS.md`,
  findings → `tracks/00_insights/`, status → `STATE.md`), not the `work/` reproducibility
  discipline; each app keeps its own internal docs (README / ADRs / CHANGELOG). You *may*
  still contract a bounded slice of app work from a `work/` brief when a plan helps — the
  brief lives in `work/`, the code in `apps/<name>/`.
- Anti-versioning still applies: no `app_v2/` — the canonical name is current.
- Non-software beasts have no apps — this folder may stay empty (harmless).

This README is the git-tracking placeholder for the otherwise-empty home.
