---
description: Tally this project's token use across all its sessions; write the report to tracks/00_insights/token_usage.md
argument-hint: [<note> — optional, what this session worked on]
---

Measure how much token usage this project has accumulated — summed across **every
session (chat window)** you have run for it — and write a report into the project.

**Run the shipped tally script from the project root:**

```
python .templates/token_tally.py
```

**With a note (`/tokens "this is what I did"`)** — pass it straight through as `--note`:

```
python .templates/token_tally.py --note "this is what I did"
```

This tags the **current session** (identified as the most-recently-active transcript) with
your note and surfaces it in the per-session table's **Note** column — a light way to link
spend to what was worked on. Notes live in `tracks/00_insights/token_notes.json` (keyed by
session id) so they **survive re-tallies**; a second note on the same session **appends**
(`old · new`). Plain `/tokens` (no arg) just re-tallies and preserves existing notes. Best-effort,
not exact — but useful for "where did the tokens go?" review.

It derives this project's Claude Code transcript directory from the current working
directory (`${CLAUDE_CONFIG_DIR:-~/.claude}/projects/<encoded-cwd>/*.jsonl`), sums the
**four token classes** — output, input (uncached), cache-creation, cache-read — across
all of that project's sessions, and writes/refreshes
`tracks/00_insights/token_usage.md` (totals, a per-session table — **with a Note column**
when any session has been annotated — the date range covered, and a retention warning). The
per-session table is **sorted ascending by session start time** and records each session's
**start + end timestamp (date *and* time, UTC)** — so sessions read in chronological order, not
by opaque session id. Then **report the headline numbers** to the User (new-work and
grand-total, sessions, turns, coverage dates; mention the note if one was just added).

**Append-only ledger (survives transcript pruning).** The script keeps a persistent ledger,
`tracks/00_insights/token_history.json` (keyed by session id, like the notes file). A re-run
**recomputes every still-retained transcript** (a completed transcript is immutable, so its
numbers are stable — re-tallying never alters a previous entry; only the live current session
grows) and **preserves any session whose transcript has been pruned** — so a session stays in
the report (marked **†**) even after Claude Code prunes it, and the **totals sum the whole
ledger** rather than only the retained transcripts (they no longer shrink over time). The
ledger is committed with the report (the permanent record).

Notes:
- **Counts only — no money.** Per-token prices change; convert later against whichever
  classes you choose (the report labels how each class is billed).
- **This is the one command that needs a shell/Python.** Transcripts can hold tens of
  millions of tokens — far too large to read into context — so they must be
  stream-processed. The script is pure Python 3 stdlib (runs anywhere Python does); this
  is a deliberate, documented exception to the otherwise no-shell command machinery. If
  Python is unavailable, say so rather than improvising.
- **Per project.** It measures the *current* project only — run it inside each beast you
  want a figure for (e.g. once per agent in a multi-beast experiment).
- **Includes subagents** this project spawned (their usage is in these transcripts).
- **Retention:** Claude Code prunes transcripts older than `cleanupPeriodDays` (default
  30). The **append-only ledger** preserves any session it has already tallied past that
  pruning (so history and totals don't shrink) — the only gap is a session that aged out
  *before* `/tokens` ever ran while it was retained. So **run `/tokens` at least once per
  retention window** to capture every session; raising `cleanupPeriodDays` (or archiving
  the `*.jsonl`) widens the safety margin.
