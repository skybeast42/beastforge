# background/

Unstructured grounding material — reference docs, industry frameworks, prior
learnings, transcripts, screenshots. Consulted **on demand or when pointed
to**, never auto-loaded (this folder may be voluminous).

**Not part of the reproducible work.** The reproducibility invariant requires
that `work/` never depends on `background/` at runtime — if a script needs
something here, promote it into the consuming task's `01_DataSource/` instead.
Background is *input context* for CC and the User; it is not a work product.

No naming convention is enforced. Keep a short manual index below as the
contents grow.

## Index

_Empty until you add material. Keep a one-line entry per file you drop here, e.g.:_

- `<file>` — <what it is; when to consult it>

_(`/ground <path>` distils what you point it at into `guidance/`.)_

## `tmp/` — local-only scratch (gitignored)

`background/tmp/` is a gitignored, local-only scratch area for pasting external
example projects to review for insight (how the template performed in practice).
It is **never** consumed by `work/` — the reproducibility invariant forbids
`work/` depending on `background/`. These are others' projects / possibly
sensitive: keep them local, and sanitise anything before a derived finding
enters a task's `01_DataSource/`.