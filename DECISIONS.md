<!--
INSTANCE FILE — the decision log. Append-only, one table row per decision.
This is the INDEX of settled calls, not the analysis. Reasoning lives in the
brief/ticket/git; this file only records *what was decided and the one-clause
why*. Use `/decide` to append a row.
-->

# DECISIONS

Append-only: **one Markdown table row per decision**. Plain lines collapse into
one run-on paragraph when rendered; a table keeps each decision on its own row
and stays scannable as the log grows. `/decide` appends a row. Escape any
literal `|` inside a cell as `\|`.

Terse by default. Expand to a short block **only** for genuinely
architecture-level calls. More than ~25 words means it is an explanation, not
a decision record — put that in the brief/ticket/git. Anti-versioning: git
history + this log are the version record; no `_v1`/`_v2` files.

The aim is for most reasoning to live **in the project** (brief/ticket/STATE), but
a row's *fuller why* often also sits in its **boundary commit message** — readily
digestible for CC. When a row is terse and the rationale isn't obvious, CC may
consult `git log`/`git show` for the commit that landed it.

| #  | Date       | Decision — one-clause why · [revisit if W] |
|----|------------|--------------------------------------------|