---
description: Rename a beast (this one, or a sibling) — folder, optional upstream bare-repo rename, remote re-url, registry recompute, then the harness-relink instructions
argument-hint: [<sibling>] <new-name>
---

Rename a beast: its working-clone folder, optionally its upstream bare repo
(+ `git remote set-url`), recompute the pool registry, then the **harness-relink**
instructions. Args: `$ARGUMENTS`.

**Two modes (by arg count):**
- **Self** — `/rename <new-name>` (one arg): renames *this* beast. The current
  session's cwd changes mid-flight → the relink is **urgent** (your session orphans
  until you relink + reopen).
- **Sibling** — `/rename <sibling> <new-name>` (two args): renames *another* beast
  from here. **Preferred when you can** — the renamer's session is untouched, so the
  folder move is clean (no live-cwd fight); the relink becomes a calm *"before you
  next open `<sibling>`"* note, not a mid-session scramble.

Below, **`<target>`** = the beast being renamed — *this* beast in self-mode, the
named sibling in sibling-mode.

**OS / git exception (declared up front).** Like `/spawn`, `/rename` **requires a
shell with `git`** (folder move + `git remote`); a documented exception to the
OS-agnostic rule. If no shell is available, say so and stop.

## 0. Guard

- Require **`<target>`'s clean working tree** (`git -C <target> status`); if dirty,
  stop and ask (mirror `/reforge` §0 — confirm a rollback point first). **Sibling-mode:**
  also confirm **no live session is running in `<target>`** (you're renaming it from here).
- **Sibling-mode resolve + guard:** `<sibling>` must resolve to a real sibling beast
  under `beasts_root` (has `.template_version` **and** `CLAUDE.md`). **Reject self-as-
  sibling** (use self-mode) and **reject any nested / non-sibling path** (one beast =
  one repo — never rename a payload or a beast-in-a-beast).
- Validate `<new-name>`: folder-safe, no collision with an existing sibling or an
  existing `origins_root/<new><bare_suffix>`.
- Resolve `.habitat/habitat.md` for `beasts_root` / `origins_root` (per `/habitat`
  step 1). `<old>` = `<target>`'s current folder basename. **If no `.habitat/` exists**
  (a standalone beast — `.habitat` is optional), proceed anyway: derive `beasts_root` =
  `<target>`'s parent directory, treat `origins_root` as blank → **the folder rename still
  happens, the upstream bare-repo rename (§2) is simply skipped** (nothing to rename, no
  registry to recompute). A standalone beast must be renamable.

## 1. Rename the working-clone folder

Move `<target>`'s folder `beasts_root[/<sub>]/<old>` → `…/<new>`. **Self-mode:**
this is the current session's cwd — it changes mid-flight (see §4), so the harness
must be pointed at the new path. **Sibling-mode:** the renamer's session is
unaffected — a clean move.

## 2. Upstream bare-repo rename (opt-in)

Per the `rename.rename_origin` flag (default **ask**): offer to rename the bare
repo `origins_root/<old><suffix>` → `origins_root/<new><suffix>` and
`git -C <target> remote set-url origin <new bare path>` (in sibling-mode the
`set-url` runs in `<target>`, not here). **Default-offer, not forced** — a
consumer may not own the origin, or may want the remote name unchanged. If
declined, the folder is renamed but the remote still points at the old bare repo
(note this in the report).

## 3. Registry recompute

Run `/fleet`'s **§ Recompute the registry** so the renamed beast self-heals in
`.habitat/registry.md` (recompute-not-incremental — nothing edits the registry by
hand). **Skip if there is no habitat home** (a standalone beast has no registry).

## 4. Harness relink — informed-manual finish

The Claude Code harness keys session state by a **folder-encoded path** under
`~/.claude/projects/<encoded-cwd>/`. A mid-session auto-relink is fragile, and
writing under `~/.claude/projects/` is adjacent to the banned internal-memory
write (Persistence rule) — so **CC never auto-`mv`s session state**.

- **Probe** whether `~/.claude/projects/<old-encoded>/` exists for `<target>`
  (read-only) so the instructions are concrete.
- **Hand the User** the exact command + restart note:
  > `mv ~/.claude/projects/<old-encoded> ~/.claude/projects/<new-encoded>`
  >
  > — **Self-mode:** your *current* session keys off the old path until you relink —
  > relink, then **reopen** in the `<new>` folder. Until then, history/resume keys off
  > the old location.
  > — **Sibling-mode:** `<target>` has **no live session here**, so nothing is broken
  > now — relink **before you next open `<target>`**. This session (the renamer) is
  > untouched.
- Default is **fully manual**: print the command, do not run it. (Probe-for-a-safe-
  auto-path is a future enhancement; today = informed-manual.) The win of sibling-mode
  is a *clean move + calm relink*, not *no relink* — `<target>`'s path key still changes.

## 5. Report

Old → new; whether the origin was renamed (or left); registry status; the exact
relink command; and the restart reminder. Recommend a boundary commit for any
in-repo changes; the folder/origin/relink are filesystem/harness ops, not commit
content.
