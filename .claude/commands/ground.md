---
description: Distil grounding material at one or more paths into project/domain guidance (opt-in, path-scoped)
argument-hint: <path-into-background>... [--to <output-path>] [--into <existing-topic>]
---

Distil grounding material at `$ARGUMENTS` into project/domain guidance. **Opt-in, path-scoped, non-destructive.** Triage-first, goal-first; subagent fan-out; the User approves every move/write; never auto-overwrite or auto-delete silently. **One grounding = one topic** (one `Read-when` scope), but its sources may be **plural and heterogeneous** — see §0.

## When to use `/ground` — and when to gather first

`/ground` distils **material you already have** into a reusable lens. It is not a research tool; it has no gather stage of its own. Pick the path by where the material is and what you want out:

| Situation | Path |
|---|---|
| Material is **on disk** (one or more local dumps under `background/`) | `/ground <path>...` directly — this command. |
| **No local material**, but the topic is **web-knowable** | **research → place → ground**: gather with `deep-research` → it stages a cited report at `background/research/<topic>/` (the 7.7 convention) → `/ground` distils it (light pass, §4). `/ground` will **offer** this when pointed at an empty/absent path (§0). |
| You want a **one-off factual answer**, no reusable lens | `deep-research` **alone** — don't ground. Grounding is for material you'll consult again. |
| You **have sources** and just need the lens | `/ground` alone — this command. |
| The output is the **application to one specific case** (this analysis, these hypotheses) | not guidance at all → a task's `04_Output/` (the guidance-vs-work boundary; *grounding builds the textbook, the work steps apply it*). |

`deep-research` is a **separate skill** (it gathers + synthesises a cited report); `/ground` *distils into reusable guidance*. They are **chained, not merged** — the seam is the `background/research/<topic>/` staging convention. `/ground` never silently invokes `deep-research`; it only ever **offers** (§0).

## 0. Parse arguments

- **`<path>...`** — **one or more** directories under `background/` (typically `background/<dump>/`, `background/tmp/<dump>/`, or `background/research/<topic>/`). Required for distillation.
  - **One grounding = one topic, but sources may be plural.** A single topic's material often spans **heterogeneous sources** — e.g. manual chapters + man pages + a source tree + a staged web report — that can't sensibly be co-located (a source tree won't move into a docs dump). Pass them together: `/ground <path-A> <path-B> <path-C>`. They distil into **one** `guidance/<ground_name>/` with **one** `Read-when` scope. Each source is triaged **independently** (§1) and curated **independently** (§3), because each naturally carries unneeded material. (Co-locating sources as subfolders of one dir and grounding that dir also works — reach for multiple paths only when the sources can't or shouldn't move.)
  - If **omitted**, report the shape of `background/` (top-level subdirs + sizes + READMEs) and ask which subtree(s) to ground. **Do not assume a default scope.**
  - A bare topic name (e.g. `/ground some_topic`) is **not** a path — but **don't just refuse.** If material exists, the User points you at it; if it **doesn't** exist locally and the topic is web-knowable, this is the **offer-to-trigger** case below.
  - **Offer-to-trigger (no local material → research → place → ground).** When a path is **absent or empty** (or the User names a topic with nothing on disk) **and** the topic looks **web-knowable**, do not dead-end. **Offer:** *"No local material for `<topic>`. It looks web-knowable — want me to run `deep-research` to gather it, stage the report at `background/research/<topic>/`, then ground that? (Y/n)"* On **yes**: **pre-create `background/research/<topic>/`** (+ a one-line README on the *research → place → ground* lifecycle) **before** launching, so the artifact never floats (the 7.7 behavioural rule); run `deep-research`; then resume `/ground` on the staged report (light pass, §4). On **no**: ask where the material is. **Never auto-invoke `deep-research` without the offer**; and a request that only wants a **one-off answer** should go to `deep-research` alone, not grounding.
  - **Inbound grounding material (CC-generated case).** A source path may be **CC-staged research** at `background/research/<topic>/`, not only a User dump — and it may be **one of several** sources passed together (a staged web report alongside local dumps). When CC gathers material *in order to ground it* (e.g. the offer-to-trigger flow above, or any `deep-research` run), it **pre-creates `background/research/<topic>/`** (+ a one-line README) **before** launching, so the artifact has a declared home; the output stages there, then `/ground` distils it. Applies to *any* CC-produced artifact destined for grounding — never improvise a home; if no convention fits, flag the gap (CLAUDE.md → Persistence: *ask when the home is unclear*).
- **`--to <out>`** — optional; redirects output away from canonical `guidance/<ground_name>/` to a custom path. Used for template-validation runs (e.g. validation-style writes to a task's `04_Output/<sub-step>/run_<date>/`). **In regular project use, omit.**
  - **Recommended convention under `--to`:** use a `run_<date>/` (or `run_<datestamp>/`) per-run subfolder so future re-runs don't collide. E.g. `--to work/TASK_0NN_<topic>/04_Output/01_validate/run_<date>/`. Not enforced; helpful for traceability when re-running the same grounding under varying conditions.
- **`--into <existing-topic>`** — optional; **incremental-update mode.** Instead of a fresh grounding, distil `<path>`'s new material and *merge* it into an already-grounded `guidance/<existing-topic>/` (or a `--to` run path), **extending** its `distilled.md` rather than overwriting. See **§ Incremental update** below. Also triggerable conversationally — *"update the grounding of `<topic>` with `<material>`"* resolves to the same flow (CC confirms the existing topic + the new material path, then runs it).

## 1. Triage (shape only, no substantive reads)

Report the shape of each source. **With multiple `<path>`s, report per source** (a short header per source root) so the curation lesson in §3 can be read source-by-source:

- Top-level subdirectories with file counts and sizes
- Top-level READMEs (one-line gist if present)
- Major file types (counts)
- Likely sub-areas (heuristic — top-level subdirs that look thematically distinct become candidate fan-out targets)

Then give the **combined candidate sub-area set** across all sources (a sub-area may be served by one source or several — that mapping shapes the §4 fan-out).

**Do not read substantive content yet.** End with: *"What is the goal of this grounding? One line minimum; longer is welcome."*

## 2. Goal solicitation (refuse without it)

Refuse to proceed without a stated goal. Accept whatever length the User provides — line, paragraph, page. **Do not summarise the goal back at the User** (no truncation, no rephrasing). Record it verbatim for the MANIFEST.

**Light preflight (a checklist, not a gate).** Once the goal lands, run three quick questions with the User — they settle scope before any reading, and they're cheap:

- **(i) Reusable lens or case-specific?** Grounding is for the *reusable, not-about-this-case lens*. If what's wanted is the **application to one specific case** (this analysis, these results), that's **work output → a task's `04_Output/`**, not guidance — redirect and stop (the guidance-vs-work boundary: *grounding builds the textbook, the work steps apply it*).
- **(ii) Source origin — web / user / hybrid?** All on disk → proceed. None on disk + web-knowable → the offer-to-trigger flow (§0). Hybrid → some sources are local paths, one may be a staged `background/research/<topic>/` report.
- **(iii) Clustering — one broad topic or split?** One grounding is **one topic / one `Read-when` scope**. A broad topic gives a coarse trigger (fewer runs, looser activation); splitting gives finer triggers (more runs, sharper activation). Decide the scope now — it fixes the single `<ground_name>`.

After the preflight, propose a `<ground_name>` (lowercase_underscore, short, reflects the goal). Confirm before continuing.

## 3. Triage report → curation lesson

With the goal in hand, classify each top-level sub-area against the goal. **With multiple sources, classify per source** — each carries its own unneeded material, so the curation lesson reads source-by-source (*"from source X, keep Y, skip Z"*):

- **In scope** — likely contributes
- **Out of scope** — does not contribute *(state why; this is the curation lesson)*
- **Unclear** — ask the User

The in/out-of-scope breakdown serves two purposes: (a) constrains the fan-out in step 4, (b) teaches the User what to dump and what to skip next time. Future dumps from the same User get smaller and more targeted. Anti-wizard: explain, don't decide silently.

## 4. Fan-out distillation (subagents)

**Inline vs. fan-out — when to delegate.** Fan-out is for **bounded distillation**: *"read this known region and distill,"* over separable, read-heavy sources. The **discovery** that *locates* those regions stays **inline** (you, with Bash/web) — triage, recon, any adaptive search where each finding shapes the next probe; you can't delegate a search before you know what you're looking for. **The tell:** delegate once a task becomes *read a known region and distill*; keep inline the work that *finds* the region. A sub-area being large is fine for fan-out (large-but-bounded is the sweet spot); large-and-unmapped means recon inline first.

**Pass-weight is per-source, not per-run — match effort to how synthesised each source already is.**

- **An already-synthesised report → light pass.** If a source is *one already-synthesised report* (e.g. a `deep-research` report staged at `background/research/<topic>/`), skip the heavy fan-out *for that source* — the synthesis is largely done, so one distillation pass over it suffices. Running multi-subagent fan-out over an already-synthesised report just double-distils.
- **A raw multi-file source → full fan-out.** Genuinely multi-file / raw dumps get the subagent fan-out below.
- **A mixed grounding gets both.** When sources differ in synthesis level — e.g. a staged web report **plus** a raw source tree — the report gets the light pass while the raw sources get full fan-out, and the §4 synthesis pass merges the results. (This is the multi-source generalisation of the original single-report light-pass.) Either way, produce the full `distilled.md` + `MANIFEST` + `material/`.

**Keep `distilled.md` general — the reusable lens, never the worked case.** `distilled.md` is the *harvestable* artifact (a sibling may `/harvest` it onto entirely different data), so it must carry the **reusable method/pattern only** — never the worked case's literal particulars: subject / record IDs, dataset / compound / study names, one-off numeric results, case file/path names, or other case-specific tokens (on another beast's data they are noise). This bites hardest when **grounding *by doing*** — distilling from a live `work/TASK_NNN` walkthrough — where it's easy to bake the worked case *into* the lens (the guidance-vs-work boundary, §0 row / the §2(i) preflight, applied at the token level). Route concrete worked instances to the task's `04_Output/AIterritory/LEARNINGS.md` / `ASSESS_*`, or render them as **clearly-marked generic illustrations** (`<subject_id>`, `<study>`, round placeholder numbers) — never as the case's literal data in `distilled.md`. Every §4 subagent is told this; the §8 close lints for leaks.

For each **in-scope** sub-area (across all sources), spawn a subagent in parallel. A sub-area may draw from one source or several; give each subagent its assigned region(s). Each subagent:

- Reads its assigned sub-area only
- Distils for the stated goal — the **reusable lens only**: write the general method/pattern, not the worked case's subject/record IDs, dataset/compound/study names, or one-off numeric results (see *Keep `distilled.md` general* above; route concrete instances to `LEARNINGS`/`ASSESS_*` or mark them generic)
- Returns a structured object: `{sub_area, key_concepts, syntax_patterns, examples, gotchas, citations}` (or domain-appropriate schema — adapt; this is a default, not a contract)

After all subagents return:

- If returns are **homogeneous** (same conceptual frame, easy to concatenate) → assemble directly.
- If returns are **heterogeneous** (different frames, overlaps, ordering matters) → run a synthesis pass: merge overlapping content, order topics logically, cross-link concepts. **Multi-source groundings are heterogeneous by nature → the synthesis pass is the default here** (the same concept may surface in two sources; the pass reconciles and de-duplicates).

Judge per run. Synthesis is on-demand, not baked-in (but expect it whenever sources are plural).

## 5. Materialise the folder-per-grounding output

Resolve the output base:

- Default: `guidance/<ground_name>/`
- With `--to <out>`: `<out>/` (e.g. a task's `04_Output/<sub-step>/run_<date>/`)

Inside the output base, propose this layout for User approval **before** writing:

```
<output_base>/
├── README.md          ← one paragraph: scope + "Read when:" activation line
├── distilled.md       ← the actual guidance (single file; split later if it grows)
├── MANIFEST.md        ← source attribution + structured inventory (see below)
├── agents/            ← three-tier audit trail — one folder per subagent
│   ├── 01_<sub_area>/
│   │   ├── prompt.md  ← the brief given to this subagent (verbatim)
│   │   └── return.md  ← the subagent's distillation as returned
│   ├── 02_<sub_area>/
│   │   └── ...
│   └── ...
└── material/          ← source material (populated in step 6)
```

**`README.md` structural expectation — the "Read when:" line.** The README is the activation hook for guidance discovery (see `/resume`'s session-start scan). Format:

```markdown
# <ground_name>

This guidance covers <one sentence>.

**Read when:** <the contextual trigger — e.g. "the conversation involves
writing or reviewing files in the grounded format/language, or structural
questions in this domain">. <Optional sentence on what NOT to apply this to.>
```

CC reads each guidance topic's `README.md` at session start (cheap); when subsequent task context matches the "Read when:" line, CC pulls the topic's `distilled.md`.

**`agents/` subfolder rationale.** Three-tier audit trail: **source** → **subagent reports** → **synthesised distillation**. Without `agents/`, the audit trail breaks at the synthesis layer — you can't reconstruct what each subagent was asked or what it found. With it, every claim in `distilled.md` is traceable to a specific subagent's return; every subagent's scope is traceable to its prompt. Mandatory at both canonical and `--to` paths.

**MANIFEST.md shape (structured table):**

```markdown
# MANIFEST — <ground_name>

**Goal (verbatim from User):** <goal>
**Sources:** <one path per line — all roots grounded into this topic; a single-source grounding lists one>
**Grounded:** <date>

## Extracted

| Source root | Source (relative) | Size | Extracted to | Notes |
|---|---|---|---|---|

## Excluded (deliberately, with reason)

| Source root | Source (relative) | Size | Reason excluded |
|---|---|---|---|
```

The MANIFEST grows through the run: the triage report drafts the *Extracted* / *Excluded* rows; subagents populate *Notes*; the close step in §8 finalises totals.

## 6. Material lifecycle — copy or move

Ask the User: *"Keep this material at its original `background/` location?"* (ask once; applies to all sources unless the User differentiates).

- **Yes → COPY** source files into `<output_base>/material/` (default for canonical groundings; the original stays in `background/` untouched). Default answer.
- **No → MOVE** source files into `<output_base>/material/` (the original is removed from `background/`).

With **multiple sources**, copy each into its own subfolder of `material/` (e.g. `material/<source-root-name>/`) so provenance stays legible; the MANIFEST *Extracted* table's **Source root** column maps each back to its origin.

**Gitignore policy:**

- **Canonical path** (`guidance/<ground_name>/material/`) — **committed by default**. User opts out per grounding if a specific case warrants it (size, sensitivity, redundancy). The manifest records provenance regardless.
- **`--to` path** (e.g. a task's `04_Output/.../material/`) — **add a `.gitignore` rule** in the run's folder (validation evidence is *distilled + manifest + agent reports + probes*, not a second copy of the source — which already lives at the `<path>` argument).

**Legitimacy is the User's responsibility.** The manifest records source attribution but does not launder bad provenance.

## 7. Probe loop *(optional, user-controlled)*

**Purpose:** confirm synthesis quality + push to edges + surface curation gaps. **Not** "rescue bad synthesis" — the empirical evidence is that synthesis quality is usually high; the loop's job is discovery and curation teaching.

### 7.0 — Open

Propose: *"Optional: I can probe the new guidance by writing a minimal example and seeing if you accept it. Want me to? (Y/n / specify your own probe)"*

If declined, skip to §8 close. If the User names a specific probe, jump to §7.3 with that probe.

### 7.1 — Write

CC writes the probe using **only the new `distilled.md`** — do not consult `material/` directly during writing (that would defeat the test of whether the guidance is self-sufficient). Show the output verbatim.

For domains where the natural artifact is code: write it inline in chat for a quick check, and **persist execution-tested probes** to `<output_base>/probes/NN_<name>/` — one folder per probe, densely numbered, holding the probe source + any run script + output artifacts (plots, logs). The MANIFEST's *Probe history* records the verdict; `probes/` holds the artifacts behind it. (Structured location decided 2026-05-31 by the `run_2026-05-31` validation — closes the 1.14.0 deferral.)

### 7.2 — Three-branch diagnostic on rejection

If the User rejects, ask:

> *"Which specifically is wrong?
> (a) The guidance got the rule wrong.
> (b) The guidance is missing a case I expected.
> (c) I misread the guidance.
> (d) Something else."*

Branch by answer:

- **(a) Rule wrong** → CC re-reads the relevant section of `material/` (targeted, not full re-read), proposes a `distilled.md` correction, User approves / revises / skips. On approval, the edit lands in `distilled.md` and a row is added to MANIFEST's *§ Probe history*.
- **(b) Missing case** → CC flags as a **curation gap** — the source dump didn't cover this case. Offer to add a row to MANIFEST's *§ Known gaps*: *what's missing · why it matters · suggested re-curation*. The User can later re-ground with additional material covering the gap.
- **(c) Misread** → simple retry with the User's correction noted in MANIFEST *§ Probe history*.
- **(d) Other** → free chat to figure it out; outcome captured in MANIFEST *§ Probe history* as a freeform entry. **If what surfaces is _out-of-domain craft_** — a sound finding that isn't about the grounded subject (e.g. a general practice rule surfacing while grounding a specific syntax or domain) — route it to the **craft-spillover accumulator** (§7.5) rather than forcing it into `distilled.md`.

### 7.3 — Ladder-up on accept

If the User accepts, offer: *"Good. Want me to try [next rung up]?"* — propose a concrete harder probe based on what was just demonstrated and the apparent scope of the guidance. User can accept, name their own probe, or stop.

The ladder is **user-driven**; CC suggests but doesn't force. Stop when the User picks "stop" or stops responding to ladder offers.

### 7.4 — Loop bound

- **Soft**: user-controlled. The loop continues as long as the User picks "next probe" / "retry" / "name a probe".
- **Hard backstop**: ~10 failures on the *same* probe → CC stops and says *"This probe keeps failing — likely a dead-end. Skipping; recording in MANIFEST as unresolved."* User can override and force another iteration.

The point of the backstop is preventing infinite loops on genuinely unresolvable probes, not enforcing a rescue-iteration ceiling.

### 7.5 — Craft-spillover accumulator (capture)

Findings surface during a grounding session that are *sound but not about the grounded subject* — general craft true across domains/tools, a User preference, or a note that belongs to a different topic. They have no home in the current `distilled.md` (they'd pollute its *Read when:* trigger) and shouldn't be dropped.

**Capture during, route at close.** When such a finding appears (in the probe loop, in synthesis, or in free chat):

- **Do not interrupt** to file it. Append a one-liner to a running *Craft findings* list in the run record (a sibling to *Probe history*) and acknowledge in passing.
- Routing happens once, in batch, at **§8 close** — see *Craft-spillover routing* there.

Applies whether or not the probe loop ran; any grounding session can accumulate craft findings.

## 8. Close

- Finalise `MANIFEST.md` (totals, summary).
- **If the probe loop ran**, append three new sections:

```markdown
## Probe history

| # | Probe | Outcome | distilled.md edit? | Notes |
|---|---|---|---|---|

## Known gaps (curation lessons for next grounding)

| Gap | Why it matters | Suggested re-curation |
|---|---|---|

## Curation lesson (free-form)

<a short paragraph: what to consider adding / skipping next time this domain
is grounded; written for the User's future self.>
```

**Craft-spillover routing (if the _Craft findings_ accumulator is non-empty).** Surface the whole list and propose a **home per finding**, one batch round:

| If the finding is… | Home |
|---|---|
| a **preference** (subjective taste) | `guidance/03_user.md` |
| **this project's** methodology / tooling | `guidance/02_derived.md` |
| an **enrichment of the just-grounded domain** | that topic's own `distilled.md` |
| **portable craft** that outlives the project | a craft-topic folder (`<craft>/` — e.g. a general-practice or tool-quirks topic) — a normal `guidance/<name>/` topic (README + distilled.md), authored on confirm |
| too **thin to file** (n=1, no sibling) | held as a noted lesson in the run record; graduate later |

CC proposes bucket + name per finding; the User confirms / redirects / renames / merges / "hold" (one-word replies). **Anti-clutter defaults:** broadest reasonable bucket first (a lone tool-specific quirk goes into the general craft file; split a narrower topic out only when a cluster ~3+ would clutter it); names are provisional. The table is a prompt for CC, **not a schema the User must follow** — best-effort; learn the real buckets on live projects. Write only on approval; tell the User where each finding landed.

**Generality lint on `distilled.md` (case-specific token sweep).** Before the summary, scan the finished `distilled.md` for likely **case-specific leaks** — subject / record-ID patterns, ALL-CAPS dataset / compound / study codes, bare one-off numeric results, file/path names from the worked case — and **surface any hits** for the User to *confirm or generalize* (replace with a generic placeholder, or move the worked instance to the task's `LEARNINGS` / `ASSESS_*`). Judgment, not a hard gate; especially load-bearing when the grounding was done **by doing** a live task (where the worked case is right there to bleed in). A clean sweep keeps the topic harvestable to a sibling whose data differs.

- One-line summary to the User: where the guidance landed; which sub-areas were in / out of scope; whether the probe loop ran and what it surfaced.
- For canonical groundings: remind the User that the new `guidance/<ground_name>/` folder is **active immediately** — `/resume` discovers it at the next session start (passive scan reads the README's *Read when:* line) and CC consults it on demand when the *Read when:* trigger matches. **No registration step** — discovery is authoritative.
- Recommend a boundary commit; never gate on it.

## Incremental update (`--into`)

Triggered by `--into <existing-topic>` or conversationally (*"update the grounding of `<topic>` with `<new material>`"*). **Extends** an existing distillation with new material **without re-grounding from scratch** — the alternative to a full overwrite re-run.

**Resolve two things first** (confirm both before any work): the **existing topic** (`guidance/<topic>/`, or a `--to` run path) and the **new material path(s)** (under `background/` — one or more, same multi-source rules as a fresh grounding). Then run §1 triage + §2 goal on the *new* material — the goal is usually a delta (*"fill the thin EVENTS/FUNCTIONS sections"*); if the User doesn't state one, propose it from the existing `distilled.md`'s coverage notes.

### Merge mechanic — protected baseline + three verbs

**The existing `distilled.md` is a protected baseline: update is additive/corrective by explicit approval, never a rewrite.** Its section skeleton (§1, §2, §3.x…) is the routing structure. Each §4 fan-out subagent is given the current `distilled.md` as reference and tags every finding relative to it:

- **ADD** — covers something the doc lacked → routed to the target section, appended. *Automatic.*
- **CONFIRM** — agrees with existing → no prose rewrite; firm up the doc's own coverage hedges (e.g. promote a *Weak spot* to *Strong coverage*) and add the citation. *Automatic.*
- **CORRECT / CONFLICT** — contradicts an existing claim → **never silent.** Surface the existing line + the new evidence; the User rules (A wins / B wins / both-under-conditions → the doc gains a conditional, not a winner). *Always interactive.*

Only ADD + CONFIRM land on their own; CORRECT always stops for the User.

### Diff-before-write

Before anything touches the file, show the section-by-section proposed changes (and every CONFLICT) for approval — the same propose-then-write rhythm as the rest of `/ground`.

### Provenance — a dated layer, never a replacement

- MANIFEST gains an **_Update history_** table: `| date | material added | sections touched | conflicts resolved |`.
- A new `agents/NN_<subarea>/` for the update's fan-out (the three-tier trail extends, not replaces).
- `material/` accretes the new source beside the original; MANIFEST *Extracted* gains the new rows (dated).
- `distilled.md` footer notes the seam: *"synthesised `<d1>`; extended `<d2>` with `<material>`."*

### Re-probe the delta

At close, offer to probe **only the newly-covered cases** (reuse §7, scoped to the change) — validates the merge worked, not just that text was appended.

## Re-run policy

If `<ground_name>` already exists at the output base:

- **At canonical** (`guidance/<ground_name>/`): **warn the User, show what exists, confirm before overwriting.** Git history preserves the prior version, so overwrite is non-destructive in the audit-trail sense. *"`guidance/<ground_name>/` exists (last touched <date>, distilled.md is <N> lines). Overwrite (the prior version stays in git history) or pick a new name?"*
- **At `--to` paths**: same warn-confirm-overwrite; recommend the User adopt the `run_<date>/` convention going forward so re-runs naturally land at sibling paths instead of colliding.

Never silently overwrite. Confirmation is the gate; refusal is no longer.

**Overwrite vs. extend:** a re-run *replaces* the distillation from scratch (use it when the source itself changed or the synthesis needs redoing). To *add* new material while keeping what's already good, use **§ Incremental update (`--into`)** above — it merges, it doesn't overwrite.
