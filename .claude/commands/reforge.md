---
description: Upgrade this beast to a newer BeastForge template by walking the CHANGELOG migration notes (safe, human-approved)
---

Bring **this project (beast)** up to a newer **BeastForge** template version by
walking `.template_changelog.md`'s per-version migration notes. **A guided,
human-approved migration — never a silent auto-migrator.** Always **plan →
approve → apply**, with per-step commits in *this* project's repo. (BeastForge
*re-forges* the beast to the latest.)

Args: `/reforge [--from <path>] [--to <version>]`.

## 0. Guard — am I a consumer, or the source?

If this beast contains a nested **`apps/<x>/`** that is itself a shipped-template
payload (it holds its own **`.template_version`** **and** `.claude/`), this *is*
the BeastForge maintenance project (the source) — it does not reforge from itself.
**Stop and say so.** `/reforge` runs in a *consumer* beast (a single root
`.template_version`, no template-bearing payload under `apps/`). *(Detection is
by content, not folder name — the **dev maintenance project** carries its payload in a
nested `apps/<x>/` that holds its own `.template_version` + `.claude/`. A **path-B
published-repo checkout** is the payload **at root** (root `.template_version` + the
`<!-- BEAST-README-BELOW -->` launch marker) — that is a fresh template, not the maintenance
project; it reforges as a consumer and will simply find current ≥ target, nothing to do.)*

Also: require a **clean working tree** (`git status`) and confirm a rollback
point (the latest commit SHA) before touching anything. If dirty, stop and ask.

## 1. Resolve the template source + payload  ·  the shared routine

> **This is the canonical "resolve template payload" routine** for the whole lifecycle realm.
> `/spawn` §2 and `/habitat` §4 **defer to it** — fix it here, they inherit it. Four parts:
> resolve the *coordinate*, the *source type*, the *payload layout*, then *pin + verify*.

**(a) Resolve the source coordinate — configured is authoritative, derivation is provenance-first.**
Resolve in this order; a **set value is used verbatim — never silently substitute a local checkout
that merely "looks canonical":**
1. `--from <path-or-url>` if given.
2. `template_source` from `.habitat/habitat.md`, if set → **authoritative** (use it; do not swap in a local copy).
3. the beast's own **recorded provenance** — a `guidance/02_derived.md` *Environment & coordinates*
   "BeastForge source: …" line, the spawn-lineage (`DECISIONS.md`), or its clone `origin` URL / the
   launch-front-matter URL.
4. the canonical **published** BeastForge URL.
5. **last resort** — offer to auto-detect a local sibling beast identified as BeastForge:
   **confirm-only**, and flag it as a **non-portable *local* coordinate** (show it before recording).

Prefer a **URL** (portable) over a machine-local path. *(The "derive live, never hardcoded" principle
applies to `beasts_root`/`origins_root` — genuinely environmental — but the canonical **published URL
is a legitimate portable value**, not a forbidden machine-local hardcode. Read it from provenance;
never bake the literal URL into a shipped command file.)*

**(b) Resolve the source TYPE.** If the coordinate is a **URL** (`https://…`, `git@…`, or ends `.git`):
`git clone --depth 1 <url> <tmp>` into a scratch dir, read the payload from the clone, discard after
*(declared shell/git exception, like §0)*. If it is a **local path**, use it directly.

**(c) Detect the payload LAYOUT — root vs `apps/template/`.** The payload lives at the resolved source
**root** when that root carries `.template_version` + `CLAUDE.md` (a **path-B published repo** — DEC 103),
**else** at `<root>/apps/template/` (a **dev maintenance checkout**). Read `.template_version` from the
**resolved payload root**, never a fixed sub-path. Template-generic files live under that payload root —
**distinct from any real apps the consumer keeps in `apps/`**; never overwrite or delete the consumer's
own `apps/<name>/`.

**(d) Pin versions + verify.** **current** = this project's `.template_version`; **target** = the payload
root's `.template_version` (or `--to <version>`). If current ≥ target, nothing to do — say so. **Verify
before upgrading:** the resolved source's version ≥ current **and** its identity matches the configured
`template_source`; on a mismatch (a found local sibling that is older or a different fork), **flag and
stop** rather than upgrade from a convenient-but-wrong checkout. Then read the source's
migration plan — **preferring precision when it's available** (DEC 119):

- **Full log present in the source** — look for `tracks/template_changelog_full.md` at the source's
  **repo root**. For a **dev-maintenance checkout** that's the **parent of the `apps/template/` payload**
  (*not* the payload root — the full log lives beside `DECISIONS.md` at the maintenance root); a **path-B
  published** source never ships it (instance-only). If found (you're reforging from the maintainer / source
  beast): walk its per-version **`Migration from X.Y.Z`** blocks for every version in `(current, target]`.
  The precise path — robust to structural / non-idempotent steps.
- **Shipped summary only** (a published / spawned consumer carries just `.template_changelog.md`): apply
  that file's single **`## Migration — any X.Y.x → current`** block for the target's minor. It is
  overwrite-based (idempotent), so applying the whole current-minor migration is safe from any point
  within the window; any **non-idempotent step** in the block is version-guarded (*"apply only if coming
  from before X.Y.Z"*) — honor the guard.

**Graceful degrade.** If neither source provides notes spanning `(current, target]` — the consumer's
version is **below the shipped window** (older than the summary's minor), or the summary flags a
non-idempotent step the consumer would cross **without** the full log — **stop and advise**: re-spawn the
beast fresh from current, or obtain the full log (`tracks/template_changelog_full.md`) to walk the
older / precise notes. Never skip a gap silently or fail opaquely.

## 2. Build the plan (dry-run) — present, do not apply

Walk the migration notes in order and synthesize a **per-step plan**, classifying
every touched path (the notes already say which is which):

- **Template-generic → overwrite from the source payload root (resolved in §1c — repo root if path-B, else `apps/template/`):** `CLAUDE.md`,
  `.claude/commands/*.md`, `.templates/*`
  (**verify-identical first**; if the consumer has hand-edited a shipped asset, **flag and confirm
  before overwriting** — don't silently clobber a customization), `.template_changelog.md`;
  `guidance/01_standing.md` (verify-identical first — skip if no diff, one less risk).
- **Merge-class → NEVER wholesale-overwrite (these carry instance config):** `.claude/settings.json`
  and `.gitignore`. Apply **only the additive change a migration note names** — e.g. the 2.2.15
  `permissions.deny` secret-file floor, or the 2.2.16 `.claude/settings.local.json` ignore — by **adding
  the missing key / entry**, and **never clobber** the consumer's own values: `permissions.defaultMode`,
  `model`, and any custom allow/deny in `settings.json`; the consumer's own lines in `.gitignore`. If a
  note touches these, it names which keys → merge exactly those, leave the rest. (Overwriting `settings.json`
  wholesale would reset a beast's chosen permission mode / model — never do it.)
- **Project-instance → preserve / surgical edit only:** `STATE.md`,
  `DECISIONS.md`, `MASTERPLAN.md`, `TODOLIST.md` (**split file — see below**),
  `README.md` (identity block), `guidance/02_derived.md`, `guidance/03_user.md`, `guidance/<domain>/*`, and all
  of `work/`, `apps/`, `tracks/`, `background/`. **"Preserve" means don't *overwrite
  from source* — NOT "don't restructure."** **Split file** — `TODOLIST.md` — carries a leading
  `<!-- … -->` **header comment block** (legend / prune-cadence machinery) that is
  *template-generic* → overwrite that block from source; the `#` heading and **everything below it** (the
  backlog items) is *project-instance* → keep verbatim. ("header only," in the
  migration notes, means **exactly that comment block and nothing below it**.) *(`ASK.md` was retired in 3.0 — its open rows migrate to the asks relay; see that migration note.)*
- **Judgment calls** the notes name explicitly — including **structural relocations**
  that legitimately *move* the preserve-class homes above **wholesale** (relocate, don't
  restructure): e.g. 2.0's old single `app/`→`apps/<name>/` (as-is), old `work/`+`audits/`
  → `tracks/legacy/` (intact, where real work was done), `work/output/00_insights`→
  `tracks/00_insights`; and smaller renames (`working_notes.md`→`03_user.md`; section
  inserts into `02_derived`; README layer-list updates). **The changelog's numbered
  structural steps are authoritative**; walk each as its own step (don't bundle them into
  the pure-overwrite pass). Prefer a wholesale `mv` over any per-item transform.

**Bundle** the pure-overwrite passes across versions into one step (the proven
strategy for a multi-version jump); keep judgment calls as their own steps. Present the whole
plan as a numbered list with per-step commit messages, and get approval. Offer a
**version-by-version** walk instead if the jump is large or risky.

## 3. Apply — one approved step at a time

For each step, honor the **five rails** (distilled from a real multi-version
migration walk):

- **F1 — explicit staging.** After *every* mutation (rename/edit/delete),
  `git add` explicitly; never trust `git mv` to also capture later content edits.
  Stage the whole step in one pass before committing, so the commit matches its
  message.
- **F2 — parity from the source, not memory.** When mirroring command-table rows
  or layer lists, copy from the source payload root's `README.md` / `CLAUDE.md`
  (the root resolved in §1c — repo root if path-B, else `apps/template/`).
- **F3 — project values come live from the project.** If a note inserts a section
  quoting project-specific values (paths, names, IDs), derive them **live from
  this project's `DECISIONS.md` + `STATE.md`** — the note gives the *shape*, the
  project gives the *values*. Never hardcode.
- **F4 — STATE prune is a proposal.** If the upgrade crosses a STATE-hygiene rule
  (1.7.0) and STATE narrates closed steps at length, **propose a prune diff and
  require approve/edit** — never overwrite `STATE.md` silently.
- **F5 — numbering reconciliation.** Older projects recorded a step-numbering
  mode (`## Step numbering` in `02_derived.md`, or in `working_notes.md` pre-1.5.0).
  **2.0 retires numbering modes** — tasks are plain-sequential `TASK_NNN`. When
  migrating to 2.0+, **offer to drop** the now-vestigial `## Step numbering` line.

Close each step with a **CC-proposed, User-approved commit** in this project
(message: `migration <current>→<target> step N: <what>`). Small, reversible,
atomic.

## 4. Set the version + verify

- Write the **target** version to `.template_version` (its own final commit) — match the source's
  byte form (e.g. `X.Y.Z\n`, trailing newline) so an identical version shows no spurious diff.
- Run `/resume` and confirm: task-integrity + reconciliation checks clean (or
  expectedly flagging — e.g. a STATE prune already handled); new shipped files
  present; commands refreshed; `.template_version` reads the target.
- Report the outcome (per `01_standing` → *Reporting output*): **lead with**
  `<current>→<target>`; **table** the steps / files touched / commits made; **end with**
  anything left for the User (e.g. an approved STATE prune, an F5 numbering move).

**Scope note.** `/reforge` is the *discipline* (locate · walk in order · the five
rails · per-step commits · verify); the judgment is CC reading the migration
notes. It shines on **incremental** jumps; a large multi-version jump is valid
but walk it carefully and offer the version-by-version mode.
