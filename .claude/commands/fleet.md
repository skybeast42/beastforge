---
description: Show the pool registry (read-only) — compute + display all habitat siblings (except .fleetignore'd), each with its guidance topics + STATE current focus
---

Show the **pool registry** for this beast's habitat — a clean table of every
sibling beast living in the habitat (except `.fleetignore`'d ones), each with its
`guidance/` topics + `STATE.md` *current focus*. `/fleet` is **read-only**: it
computes and displays; it writes nothing but the derived `registry.md` cache.
Then `/harvest <seed>` inherits a topic.

**Default-open within the habitat.** Living in the habitat *is* being in the
pool — every sibling can peek (read another's repo) and harvest (pull another's
`guidance/` topics, `guidance/` only). There is no opt-in, no membership marker,
no "join" step. The **only** opt-out is `.fleetignore` (manual, committed), which
isolates a folder+subtree **fully and symmetrically** ("out is out"): it neither
reads nor is read, and it does not appear in the registry at all.

**OS-agnostic (DEC 75).** This command does all its file work with CC's own tools
(Glob / Read / Write) — **no shell assumed** (Windows / macOS / Linux). A shell is
never required.

## 1. Guard — `.fleetignore` self-check

Walk this beast's own folder + ancestor directories. If **this beast** (or any
ancestor it sits under) carries a `.fleetignore` file, it is **fully isolated** —
cut off from the pool in both directions (it can't read or harvest siblings, and
siblings can't read or harvest it; it's absent from the registry and the relay).
Say so and stop — there is no pool to show from inside an isolated subtree.

**Co-ignored siblings are mutually isolated — by design.** The ancestor-walk is
**unbounded** (it does not stop at an enclosing `.habitat/` root), so two beasts
under one wrapper folder's `.fleetignore` are isolated from **each other** too — not
just from the outer habitat — because the guard fires on the ancestor `.fleetignore`
before any pool resolves. `.fleetignore` means *"hide this subtree, symmetrically,"*
and nothing more: it does **not** form a private inner pool, and nesting a `.habitat/`
beneath it does **not** rescue them. A cluster of *cooperating-but-hidden* beasts is a
**separate habitat** (its own `.habitat/` home), never a co-ignored wrapper. *(DEC 131
declined the "co-ignored = mini-pool" refinement to keep DEC 129's single "out is out"
invariant; revisit only if a recurring need for share-internally / hide-externally
clusters appears that a separate habitat genuinely can't serve.)*

## 2. Locate the habitat home

Find the **habitat home** = the nearest ancestor directory containing a
`.habitat/` home — detected by its marker file `habitat.md` (or `registry.md`),
walking up from this beast. The directory holding `.habitat/` is the **habitat
root**. If none exists, **establish** `.habitat/` at this beast's **parent**
directory (the habitat root) and announce it (Write creates `.habitat/`
implicitly in step 4). **Name-agnostic: detect by the marker file, never hardcode
the container name** — the conventional name is `.habitat/` but discovery keys on
content. `/habitat` configures this home (`beasts_root`/`origins_root`/
`template_source`); `/fleet` only reads/recomputes its `registry.md`.

**Legacy fallback.** If a pre-2.1 `_fleet/` exists at the root but no `.habitat/`,
treat `_fleet/` as the home for *discovery* (so an un-migrated pool still works),
and offer to migrate it to `.habitat/` via `/habitat init` (an instance op — not
forced here).

## 3. § Recompute the registry

> **This is the canonical registry procedure.** `/harvest` references this
> section — keep the logic here only.

The registry is a **recomputed cache, never authoritative** — the source of truth
is the filesystem (which sibling folders exist, and which carry a `.fleetignore`).
Every run is a full recompute, so removals self-heal (a retired or newly-isolated
beast simply isn't found).

1. **Discover candidate beasts.** Glob `<habitat-root>/**/.template_version`
   (depth-bounded, ≤ ~5 levels). Each match's parent dir is a candidate.
2. **Beast-test.** A candidate is a beast iff it has `.template_version` **and**
   `CLAUDE.md` **and** `STATE.md` (Read/Glob-check). Non-beasts (e.g. a bare repo)
   are recorded in a *skipped* footnote, not listed as beasts.
3. **Filter.** Drop any candidate inside a `.fleetignore` subtree (Glob
   `<habitat-root>/**/.fleetignore`, build the ignore-prefix set) — a
   `.fleetignore`'d beast is fully isolated and never appears, not even
   existence-only. Drop any candidate **nested under another beast's root** (so a
   beast's own template payload under `apps/` — e.g.
   `apps/template/.template_version` — is never mis-detected as a second beast).
4. **Model.** Read the beast's chosen **model** — `.claude/settings.json` `model`
   (→ `—` if unset, i.e. it inherits the session default) — for the registry's
   Model column, so the pool is model-aware.
5. **Read contents (every listed sibling).** For each beast that survives the
   filter, read its **guidance topics** + each topic's *Read when:* line (Glob
   `guidance/*/distilled.md`; Read each topic's `README.md`) and the `STATE.md`
   *Current focus* one-liner. Every listed sibling is harvestable, so every
   listed sibling shows full topic detail — there is no member/non-member split.
6. **Write** `<habitat-home>/registry.md` (i.e. `.habitat/registry.md`; Write —
   creates `.habitat/` if needed; on an un-migrated pool fall back to the legacy
   `_fleet/registry.md` per step 2). Shape:

   ```markdown
   # Fleet pool registry

   _Generated <date> by `<this beast>` — habitat root `<habitat-root>`._
   _Derived cache — **regenerate, do not edit.** Source of truth: the filesystem
   (sibling folders + `.fleetignore` opt-outs)._

   | Beast | Ver | Model | Topics | Current focus |
   |---|---|---|---|---|
   | …one row per beast — Model `—` if unset… |

   ## Topic detail

   ### <BEAST> — <ver>
   - **<topic>** — Read when: <one-line Read-when, both README styles>
   …

   ---
   _Skipped: <non-beast dirs> (no .template_version — not a beast)._
   _`.fleetignore`'d subtrees are fully isolated and absent from this registry._
   _Peek: to read **beyond** this index, open a sibling's path directly (its
   `STATE.md` / `MASTERPLAN.md` / `guidance/<topic>/distilled.md` / a task's `04_Output/…`)
   — pure read, no copy. Copying `guidance/` is `/harvest`._
   ```

   Copy content **byte-faithfully** from the sources; do not editorialize the
   Read-when / focus lines beyond trimming to one line.

## 4. Sibling read-access (local, machine-specific)

So peek / `/harvest` / `/reforge`-from-sibling can read other beasts **without a
per-path prompt**, add the listed siblings' absolute paths to this beast's
`.claude/settings.local.json` under `permissions.additionalDirectories` (create it
if absent; merge + dedupe). **Use `settings.local.json`, never the shared
`settings.json`** — these are absolute machine paths (non-portable; meaningless on
another machine or a spawned copy), so they must stay **local and gitignored**.

- **All listed siblings.** Grant read to every sibling in the registry; a
  `.fleetignore`'d beast is filtered out (§3) so it's never granted. Re-running
  `/fleet` re-syncs the list as siblings come and go.
- **Skip in `bypassPermissions` mode** (nothing to grant). Propose the change;
  it's local + reversible, so don't gate.
- *(Convenience, not a new permission: the `.fleetignore` + `guidance/`-only scope
  rule still governs what you **should** read/copy — this only removes the friction
  on what you already may.)*

## 5. Show + close

Show the registry (the table + per-sibling topic detail) to the User. The
`.habitat/registry.md` is a derived cache outside any single repo (it lives in
the habitat home `/habitat` configures) — regenerable anytime via `/fleet`.

## Peek — reading beyond the registry (no copy)

The registry is the cheap *index*; to read **more than** it shows, **peek**:
resolve a sibling's path and Read it directly — its `STATE.md`, `MASTERPLAN.md`, a
specific `guidance/<topic>/distilled.md` (to view without inheriting), or a
task's `04_Output/…` artifact. **Pure read — no copy, no provenance.** That is the
*Study* / *Orient* side of the pool; **copying `guidance/` is `/harvest`'s job**
(the *Inherit* side). Default-open: every listed sibling is readable; a
`.fleetignore`'d subtree is fully isolated and unreadable. No command needed —
just ask (*"read `<sibling>`'s MASTERPLAN"*, *"show `<sibling>`'s `<topic>`
distilled"*); the registry resolves the path. (Broad Study workflows — read a
whole sibling → produce new artifacts here — are a later phase.)
