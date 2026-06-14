---
description: Stamp out a new sibling beast from the BeastForge template — bare-repo init, clone, populate, identity, push
argument-hint: <name> [--in <sub>] [-- <one-line description>]
---

Stamp out a **new sibling beast** from the template: create its bare origin, clone
it, populate it from BeastForge's payload, give it an identity + window color +
lineage, and push. The "fleet grows itself" command. Args: `$ARGUMENTS`
(`<name>` required; `--in <sub>` nests it under a sub-folder of `beasts_root`;
everything after `--` is the new beast's **one-line description** — if omitted,
`/spawn` **asks for it** at the identity step, it does **not** leave a placeholder).

**OS / git exception (declared up front).** Unlike most commands, `/spawn`
**requires a shell with `git`** — `git init --bare`, `git clone`, `git remote`,
and `git push` have no CC-tool equivalent. This is one of the few documented
exceptions to the OS-agnostic-commands rule (alongside `/tokens`). If no shell/git
is available, **say so and stop** — do not improvise a partial beast. The *file
population* step still prefers CC's own Read→Write (Tier 1), shelling out only for
git and the optional `cp -r` fast-path.

## 0. HARD GUARD — never spawn inside a beast

**One beast = one repo.** Resolve the intended target path
(`beasts_root[/<sub>]/<name>`) and walk **its ancestors**: if any carries
`.template_version` **or** `CLAUDE.md`, the target would nest inside an existing
beast → **refuse and stop**. Reject an `apps/` target explicitly (offspring don't
live in another beast's `apps/`). The new beast must be a **sibling** at
`beasts_root`, never a child of a beast.

Then resolve the **habitat config**: locate `.habitat/habitat.md` (per `/habitat`
step 1). If absent, **offer `/habitat init`** (recommended — it's the natural home for
spawn config); if the User declines, you may still proceed by **deriving the two essentials**:
`beasts_root` = this beast's parent directory, `template_source` = this beast's own provenance
(per `/reforge` §1a — its recorded coordinate / origin / launch URL). **`origins_root` is
optional**: set → the new beast gets a bare origin there; **blank/absent → the new beast is
local-only** (no bare repo, no remote). Never default `origins_root` to `beasts_root` (that
would scatter bare repos among the working beasts).

## 1. Resolve coordinates

- `beasts_root`, `origins_root` (may be blank), `template_source`, flags ←
  `.habitat/habitat.md`.
- `--in <sub>` (or `spawn.nest_default`) → target = `beasts_root/<sub>/<name>`;
  else `beasts_root/<name>`.
- Validate `<name>`: folder-safe, no collision with an existing sibling — and, if
  `origins_root` is set, no collision with an existing `origins_root/<name><bare_suffix>`.

## 2. Resolve the source + payload (defer to `/reforge` §1)

**Use the shared "resolve template payload" routine — `/reforge` §1.** It resolves: the
**coordinate** (configured `template_source` is authoritative; else provenance-first; a URL is
preferred over a machine path), the **source type** (a **URL** → `git clone --depth 1` to a temp
dir, read the payload from the clone, discard after; a **local path** → use directly), and the
**payload layout** (the resolved root if it carries `.template_version` + `CLAUDE.md` — a path-B
published repo — **else** `<root>/apps/template/`). Read `.template_version` from the **resolved
payload root** — the new beast inherits it. *(So a habitat configured with the published GitHub
**URL** spawns correctly: clone-to-temp + payload-at-root, no `apps/template/` assumption.)*

## 3. Create the repo

**Default branch = `main`** — set it explicitly so the beast doesn't inherit the host's git
default (which may be `master`); the published repo and the beast pool use `main`. Use
`git init -b main` (git ≥ 2.28) — or `git init` then `git branch -m main` / `git symbolic-ref
HEAD refs/heads/main` on the bare. Branch on whether `origins_root` is configured:

- **`origins_root` set (beast with a bare origin):**
  1. `git init --bare -b main <origins_root>/<name><bare_suffix>` (suffix default `.git`).
  2. `git clone <that bare> <target>` → the working clone (tracks `main`).
- **`origins_root` blank/absent (local-only beast):**
  1. `git init -b main <target>` → a fresh local repo on `main`, **no remote**. (No bare repo
     is created; tell the User the beast is local-only and how to add a remote later —
     set `origins_root` and re-spawn, or `git remote add origin <url>`.)

Then, either way, **populate** the working tree from the **resolved payload root** (§2 — the
temp clone's root for a URL/path-B source, or `<path>/apps/template/` for a local maintenance checkout).
**Never copy the payload's own `.git`** — the payload root for a URL/path-B source is a *clone*, so it
carries a `.git` pointing at the template; copying it would clobber the new beast's fresh history and
origin (a silent provenance leak). Exclude it in both tiers:
- **Tier 1 (preferred, OS-agnostic):** Glob the payload tree **(skip `.git/`)**, Read each file →
  Write it verbatim into the clone (a faithful copy of the shipped payload).
- **Tier 2 (optional, shell):** copy the payload contents **excluding `.git`** — e.g.
  `rsync -a --exclude .git <payload-root>/ <target>/`, or
  `find <payload-root> -mindepth 1 -maxdepth 1 ! -name .git -exec cp -r {} <target>/ \;`.
  (A bare `cp -r <payload-root>/. <target>/` with dotglob would drag the payload's `.git` in — don't.)
- If the payload root is a **path-B published repo**, it carries the launch front-matter
  (`getstarted.md`, `banner.*`, the landing `README.md` marker); `/setup` (step 1) strips these
  per-beast, so no extra cleanup is needed here.
- Set the clone's `.template_version` to the payload's version. The new beast
  gets **one** `.template_version` (a consumer beast — no template-bearing
  payload under `apps/`; it keeps real apps in `apps/`).

## 4. Identity + lineage (run the **full** `/setup`)

- **Get the one-line description NOW — the single input `/spawn` cannot derive.**
  The **name** is the `<name>` arg; the **description** is the one piece of genuinely
  user-supplied content. Take it from the `-- <description>` arg if given, **else ask
  for it inline** (one short line — the cheap, non-annoying path). **Do not drop a
  placeholder and defer it to a later `/setup` run** — making the User re-run `/setup`
  for the one thing that should have been asked up front is exactly the annoyance to avoid.
- **Run the complete `/setup` bootstrap for the *new* beast — every step, not just
  the nameplate** (feeding it the name + description above). In particular it must reach
  **step 9 (flip `STATE.md` `Status: uninitialised → active`)**, or the spawned beast is
  detected as *virgin* on its first `/resume` and re-proposes `/setup` — the loop 2.2.8
  closed. `/setup` also writes the README nameplate (step 1), runs the **window color**
  (step 6 — so `/spawn` does **not** run `/vscolor` separately; setup owns it), and its
  *settle-origin* step (3) is a **no-op here** — `/spawn` already wired the origin (or left
  it local-only), and the new beast's origin is its own bare, never the template → `/setup`
  keeps it. *(Minimal ≠ skip the description: asking one line is the bootstrap working as
  intended, not "wizard" behavior.)*
- **Lineage stamp:** record where it came from — propose a `DECISIONS.md` row in
  the **new** beast: *"Spawned from `<template_source>` (BeastForge `<ver>`) on
  `<date>` via `/spawn`."* Also write a `guidance/02_derived.md` *Environment &
  coordinates* "BeastForge source: …" line so the child's `/reforge` already knows its
  source — record the **portable form**: the URL `template_source` when it is one, **not** a
  machine-local path (a path is meaningless on the child's machine / another sibling).

## 5. Commit + push

Initial commit in the new beast (`spawn: bootstrap <name> from BeastForge <ver>`).
**Push only if a remote exists** (`origins_root` was set): `git push -u origin main`
to its bare origin. A local-only beast (no `origins_root`) has nothing to push —
say so. Per-step, reversible.

## 6. Register + report

Recompute the pool registry (`/fleet`'s § Recompute) so the new sibling appears in
`.habitat/registry.md`. **Report (per `01_standing` → *Reporting output*):** lead with
`Spawned <name> — BeastForge <ver>`; then a short **table** — path · origin · branch · version ·
window color · lineage row; end with the next action. **`/setup` already ran in full at §4 (incl. the
description) — do NOT suggest re-running it.** The next action: open the new beast (its own VS
Code workspace, or `cd` there on the CLI — commands only load in the beast's own folder) and run
**`/masterplan`** to set strategy, or jump into the first task.
