# work/

Bounded, **briefed** work — organised **task-first** (reproducible *when a task
fills its stages*). Each unit is a self-contained `TASK_NNN_<name>/` holding all
its own stages:

```
work/
└── TASK_NNN_<name>/
    ├── 00_Briefs/        ← the contract: 00_brief.md + NN_ticket_*.md (+ optional WORKLOG.md)
    ├── 01_DataSource/    ← raw, immutable input
    ├── 02_Data/          ← processed / derived
    ├── 03_Scripts/       ← scripts ONLY (+ Resources/ method assets, AIterritory/ AI assessment) + SCRIPT_00_RUNALL.*
    ├── 04_Output/        ← results, one subfolder per script
    └── 05_Reports/       ← the task's deliverable
```

**Per-task reproducibility:** each task re-runs end-to-end from its own
`01_DataSource/` via `03_Scripts/SCRIPT_00_RUNALL.*`. Nothing outside the task is
needed — that's what lets a task be zipped and stand alone. Assessment *about* a
task (audits) lives in `tracks/audits/`, never in `04_Output/`. **Rerun hygiene:** each
script deletes its own per-script output first, so re-runs leave no stale files (dated
`05_Reports/` deliverables exempt; full rules in CLAUDE.md).

**Stages are lazy** — created as needed; a notebook-ish task may be just
`00_Briefs/`, as is a **brief-only** task whose deliverable lives in
`apps/`/`tracks/` (the brief contracts it; the stages stay empty, and its
*Deliverables* points to where the output lives). `03_Scripts/` holds scripts
only; things they *load* (helper
functions, structural-model templates, config — the *method*, not the data) go in
`03_Scripts/Resources/`, the AI's assessment scripts + reasoning in `03_Scripts/AIterritory/`
(CLAUDE.md → *AI territory*). Open-ended design/exploration is **not** a task — it's a
`tracks/` notebook.

### Brief · ticket · worklog (all under `00_Briefs/`)

- **Brief** — `00_brief.md`, exactly one; the contract (schema in [CLAUDE.md](../CLAUDE.md)).
- **Tickets** — `NN_ticket_<desc>.md` (count from `01_`); amendments that never replace the brief.
- **Worklog** *(optional)* — `WORKLOG.md`, a freeform living record for long iterative tasks.

Use `/brief` to scaffold a task, `/ticket` to amend one. Full rules: `/conventions`.
