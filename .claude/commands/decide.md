---
description: Append a decision row to DECISIONS.md
argument-hint: [decision — why; or leave blank to infer from the conversation]
---

Record a decision in `DECISIONS.md`. Input: $ARGUMENTS

- If input is given, use it. If blank, infer the just-settled decision from the conversation and **propose the one-liner for confirmation** before writing.
- Append exactly one Markdown table row, below the existing rows, in this format:
  `| NN | YYYY-MM-DD | <decision> — <one-clause why> [revisit if W] |`
  where `NN` is the next sequential number and the date is today. Escape any literal `|` in the decision text as `\|`.
- **Hard rule: one row.** If it needs more than ~25 words, it is an explanation, not a decision record — the explanation belongs in the brief/ticket/git. Expand to a short block *only* for genuinely architecture-level calls.
- **If the decision changes a task's *contract*** (alters its inputs / outputs / behaviour, vs. merely recording a fact), **propose a matching ticket** on that task the same turn (`/ticket`) — don't log the decision and move on. This is the proactive hook the brief/ticket layer otherwise lacks mid-flow (why briefs rot on long iterative tasks); fact-recording decisions need no ticket.
- **If this decision answers an open relay ask** (a question is now settled), this row **is** its outcome → **close that ask** the same turn (route-and-close: move the relay message to `cur/`; `DECISIONS.md` is now the record). Don't leave it open.
- `DECISIONS.md` is the index of settled calls, not the analysis. Do not narrate.
