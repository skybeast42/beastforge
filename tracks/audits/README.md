# tracks/audits/

Assessment **of** the work. An audit is commentary *about* the work, not an input
to re-running it — so it's a track (the beast's trail about itself), never inside a
task's `04_Output/`. The boundary is bidirectional: nothing outside a task is
needed to run it; nothing inside it is assessment of it. (Mirrors regulated
practice — audit reports are separate controlled records.)

```
tracks/audits/
└── <scope>/
    ├── 00_charter.md     ← scope, objectives, specialist roster (Origin: plan)
    ├── 01_findings.md    ← severity-ranked findings (the deliverable)
    └── 02_resolution.md  ← closure log: every finding → disposition + reference
```

A re-audit is a new `<scope>/` folder. **Git-tracked** — the assurance trail is
institutional memory, not disposable state.

`/audit` plans and runs it (fans out specialist subagents that read `guidance/`,
including any domain docs). `/audit-resolve` walks the findings to closure —
routing fixes to `/ticket`s on `work/` tasks and accept/won't-fix calls to
`/decide`. An audit with no `02_resolution.md`, or with deferred findings, is
**open**.
