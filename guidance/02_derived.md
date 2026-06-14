<!--
INSTANCE FILE — this project's specifics (tooling, style, testing). Do NOT
fill this in by hand: while it shows `Status: uninitialised`, ask CC to derive
it from MASTERPLAN.md (CC proposes, you approve). After that it is a normal
owned file — edit it freely; git is its history.
-->

# Derived guidance

Status: uninitialised

_CC: while this says `uninitialised` and `MASTERPLAN.md` has content, propose
filling the sections below from the strategy, then remove this Status line on
the User's approval._

## Expertise framing
_The expert lens CC adopts for this project — seeded at `/setup` once the purpose
is clear, evolving as the project does. State it as a role: **"act as a world-class
`<domain>` practitioner"**, or a small **panel** ("a team of `<A>` / `<B>` / `<C>`
specialists") when the work spans fields. It sharpens how CC frames domain work._

**Floor — sharpens framing, never licenses confidence.** The persona must NOT
produce unhedged, overconfident first answers. CC still surfaces assumptions,
uncertainty, sources, and counter-views — *especially* inside the framed domain,
where an unquestioned wrong answer does the most damage. Where `03_user.md` records
a self-questioning preference, it governs here too.

_Empty until set; CC proposes from `MASTERPLAN.md` / the stated purpose, the User approves._

## Language & tooling
_Languages, package manager, formatter, linter, type checker, test runner —
the exact commands. Also how the environment is pinned (lockfile, versions,
container) so a task's `SCRIPT_00_RUNALL.*` reproduces from its `01_DataSource/`._

## Environment & coordinates
_Project-wide pointers: endpoints, URLs, deploy targets, dashboards, key
paths — "where things live." Task-specific runbooks stay in that task's
`04_Output/`. Not secrets (never in-repo); a credential *location*
only if a project genuinely needs to record one — else ask._

## Style
_Naming, structure, what "idiomatic" means here. Default: match surrounding code._

## Testing
_What must be tested, how, and when. The definition of done for code._

## Don'ts
_Patterns or dependencies to avoid in this project._

## Self-review
_What CC checks before declaring code done._
