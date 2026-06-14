<!--
INSTANCE FILE — current operational state. This is the first thing /resume
reads. Keep it SHORT and CURRENT: it answers "where are we right now and what
is next", nothing durable (that is MASTERPLAN.md) and nothing settled (that is
DECISIONS.md). Flip Status to "active" once the project is initialised — the
/resume cold-start detection keys on this.

See CLAUDE.md → "STATE.md — the rule" for the hygiene discipline.

Shape for `Where execution stands` (itemized bullets):

  - `step_name` — **<status>**: <one-line description / pointer>

Status vocabulary: planned · in flight · closed (DEC NN) · paused · blocked.
Use a final `- Earlier:` rollup bullet for older steps not worth listing.
-->

# STATE

**Status:** uninitialised

## Current focus

_What is being worked on right now (one short paragraph). **NOT** an
achievement log of closed steps — those compress to one line elsewhere._

## Where execution stands

_One terse line per active or recently-touched step — narrative, not a
re-render of `/status`. Closed steps stay as one-liners; older closed steps
roll into a final `- Earlier:` bullet._

## Open questions / blockers

_Anything waiting on a decision or an input. Empty is good._

## Next action

_The single concrete next thing to do. `/resume` will surface this._
