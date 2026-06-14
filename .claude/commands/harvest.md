---
description: Inherit a guidance topic from a sibling beast — semantic match against the habitat registry, anti-wizard manifest, copy-with-provenance into this beast
argument-hint: <seed task brief>
---

Inherit `guidance/` from the **pool**: given a one-line task **seed**, match it
against sibling beasts' topics, propose what to copy, and **copy-with-provenance**
the approved topics into **this** beast's `guidance/`. The payoff of the habitat —
a beast onboards itself from the pool. **Harvest = copy-with-stamp, not
re-grounding.** **Harvest pulls `guidance/` only — never `work/`.**

**Default-open:** any habitat sibling's `guidance/` topics are harvestable;
the only boundary is `.fleetignore` (on either side — see step 1) and the
`guidance/`-only scope. No membership, no opt-in.

**OS-agnostic (DEC 75):** CC's own tools only (Glob / Read / Write); no shell
assumed. **Inherit profile only** (copy `guidance/`); *Study* / *Orient* are
out of scope.

## 1. Guard — `.fleetignore` self-check

If any ancestor of this beast carries a `.fleetignore`, this beast is **fully
isolated** — out is out: nothing to harvest. Say so and stop. (Isolation is the
only opt-out; it cuts both directions.)

*(**Co-ignored siblings** — two beasts under one wrapper folder's `.fleetignore` —
are isolated from **each other** too: the ancestor-walk is unbounded and doesn't
stop at a `.habitat/`, so the guard fires before any pool resolves. `.fleetignore` =
"hide this subtree," never a private inner pool; a cooperating-but-hidden cluster is
a **separate habitat**. See `fleet.md` step 1 / DEC 131.)*

## 2. Ensure a current registry

Recompute per `/fleet`'s **§ Recompute the registry** (never trust a stale
`registry.md`). Harvest reads the resulting *Topic detail* — every habitat
sibling **except** those carrying a `.fleetignore` (a sibling with one is
isolated and invisible; skip it).

## 3. Seed

Take the one-line task brief from `$ARGUMENTS` (e.g. *"set up X with framework
Y"* — enough domain keywords to match on). If empty, ask for one.

## 4. Match (semantic — this is why harvest is a command, not a script)

For each sibling topic in the registry, judge its *Read when:* line against the
seed → **STRONG inherit / borderline / no**. Use the Read-when framing as written;
do **not** keyword-grep. (Default-open: every habitat sibling's `guidance/` topics
are visible — the registry already excludes `.fleetignore`'d siblings.)

## 5. Propose the anti-wizard manifest (present — do not auto-act)

- **Inherit** — topics to copy, each with its one-line Read-when justification.
- **Borderline** — offered, **never** auto-copied; the User decides.
- **Gap** — what the seed needs that **no** pool topic covers → **propose**
  grounding it from scratch (`/ground`, research → place → ground). **Do NOT
  auto-do it.**

Get explicit approval before copying anything.

## 6. Copy-with-provenance (approved topics → this beast's `guidance/`)

For each approved topic, source = `<source-beast>/guidance/<topic>/`,
destination = `./guidance/<topic>/` (this beast — **production, not a sandbox**):

- **Refuse-if-exists.** If `./guidance/<topic>/` already exists, skip it and say
  so (refresh-from-source is a later phase). Non-destructive.
- **Capture provenance** (read-only against the source): source beast name; its
  `.template_version`; its commit — `git -C <source> rev-parse --short HEAD`
  (+ `-dirty` if uncommitted) **only if a shell is available**, else
  `(commit unavailable)`; today's date (you supply it).
- **Copy the text guidance, byte-faithfully.** Clone `README.md`, `distilled.md`,
  `MANIFEST.md`, and the `agents/` trail.
  - **Tier 1 (required, OS-agnostic):** Glob the source tree, then **Read each
    file → Write it** to the destination path **verbatim** — a clone, not a
    re-grounding: do not reformat, re-wrap, or "improve" the content.
  - **Tier 2 (optional, never required):** *if a shell is available* you MAY
    `cp -r` the folder for speed and guaranteed byte-fidelity, then stamp.
    Otherwise fall through to Tier 1.
  - **`material/` is recorded-not-copied** (bulky / possibly binary; the lens
    lives in `distilled.md`). The stamp notes the omission; refresh-from-source or
    manual copy is a later phase.
- **Stamp the provenance** (the brief-27 schema — append, never edit prior rows):
  - **MANIFEST** — append (or **create** the file if the source had none) an
    `## Inheritance provenance` section:

    ```markdown
    ---

    ## Inheritance provenance

    _Inherited (copied with provenance) from a sibling beast by `/harvest` — not
    grounded here. Any Extracted/Excluded tables and `agents/` trail above are the
    source beast's work, preserved verbatim._

    | Field | Value |
    |---|---|
    | Inherited from (beast) | <SOURCE_BEAST> |
    | Source path | `guidance/<topic>` |
    | Source template version | <SRC_VER> |
    | Source commit | `<SRC_SHA or (commit unavailable)>` |
    | Harvested into | `<this beast>/guidance/<topic>` |
    | Harvested by | <this beast> (`/harvest`) |
    | Date | <date> |
    | Harvest profile | Inherit (copy guidance with provenance) |
    | Seed | "<seed>" |
    | material/ copied? | no — recorded-not-copied (refresh-from-source later) |

    _Floor-not-equality (stance S3): source version is recorded for lineage /
    staleness, **not** a compatibility gate — guidance is copyable across template
    versions. This is a point-in-time copy._
    ```
  - **README** — append a one-line note: *"**Inherited (fleet harvest).** Copied
    with provenance from **<SOURCE_BEAST>** `guidance/<topic>` (template <ver>,
    commit `<sha>`) on <date> — see MANIFEST § Inheritance provenance."*

## 7. Report + close

Report what was inherited and where; surface any **gap** for a follow-up
`/ground`. Recommend a boundary commit; never gate.
