<!-- STANDING guidance — universal and stable. Applies to all work. Edit rarely. -->

# Standing guidance

The floor. `02_derived.md` and any domain doc layer on top and win where they
are more specific.

- Match the surrounding code/document conventions; don't impose a new style.
- No secrets, credentials, or tokens in the repo.
- Cite reputable, primary sources for factual or technical claims.
- Don't add dependencies or abstractions without a concrete reason.
- Prefer the simplest thing that works; leave the place tidier than you found it.
- No personal, identifying, or otherwise restricted data in a task's `01_DataSource/` (or anywhere in the repo) without recording its classification and handling in the task's brief.
- At each brief/ticket boundary, propose a commit for the User to approve — CC-authored message `TASK_NNN_name: <what/why>`, path-scoped to that task's folder (or the relevant home unit); a checkpoint, never a gate; never rewrite existing history (no amend/rebase); tolerate ad-hoc manual commits.
- **Reporting output to the User** — command and task results are *read*, so keep them scannable and consistent run-to-run (a command may add its own shape on top; this is the default floor):
  - **Lead with the outcome** — the first line is the bottom line (what changed / was found / is proposed), not preamble.
  - **Table for 3+ comparable items; prose for one or two** — tasks, beasts, files touched, findings, version steps → a Markdown table with a fixed column order; one or two items → a tight sentence.
  - **Say where it landed** — name the exact file path(s) written or proposed (the Persistence *"say where"* rule, as an output requirement).
  - **End with one concrete next action** — a single proposed next step; a purely read-only report ends with its headline instead.
  - **Terse, no narration** — short labelled lines over paragraphs; don't restate at length what you just did (the `DECISIONS`/`STATE` terseness, applied to chat).
