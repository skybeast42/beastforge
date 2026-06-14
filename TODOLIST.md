<!--
INSTANCE FILE — the backlog / icebox. A holding pen for ideas and feature
candidates NOT yet ready for a brief and not belonging in:
  - MASTERPLAN.md  → durable strategy (too tactical / not yet committed)
  - DECISIONS.md   → settled calls (these aren't settled)
  - STATE.md       → current focus only (must stay short)
When an item matures, it graduates to a brief (via /brief) and is struck
through here with a pointer. Ships empty.

Shape (itemized bullets, grouped by themes):

  ## Theme N — <theme name>

  - [STATUS] **N.M** *<headline>*: <one-line gist>. → <destination/routing>
      - sub-bullets ONLY for design decisions, caveats, or field evidence —
        their accumulation signals the item is ready to graduate to a brief.

Status:  [ ] open · [~] in flight · [x] done (this session) ·
         [X] done + survived one session (pruned at the next /wrap) ·
         [▲] promoted from MASTERPLAN deferred

Pruning is a two-marker, session-driven state machine — no counting, no
remembering. A done item is [x] when it finishes, [X] once it has survived one
session. At EVERY /wrap (session close), in order: (1) prune every existing [X]
(remove it, collapsing a fully-done theme to a one-line "CLOSED -> DEC/changelog"
stub), then (2) promote each surviving [x] -> [X]. So a done item lands as [x],
becomes [X] at this session's /wrap, stays visible through the next session (a
fresh /resume sees what just landed), then prunes at that /wrap — the marker IS
the memory. /commit does NOT touch the markers (a session has many commits).
Automatic and unasked (reversible + recorded: the DEC / .template_changelog.md
pointer is the permanent record, so pruning loses nothing). The done-pileup
check (/resume, /check) is only a backstop if the /wrap step ever gets skipped.
-->

# TODOLIST

_Backlog / icebox. Empty at start. Add ideas and feature candidates as they
surface; graduate them to briefs when ready._
