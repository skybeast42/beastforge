---
description: View/edit the habitat home (.habitat/) at the habitat root — beasts_root, origins_root, template_source; bootstrap it if absent
argument-hint: [show | edit | init]
---

Manage the **habitat home** — `.habitat/`, the shared config + registry that lives
at the **habitat root** (the directory holding sibling beasts), **outside any
single beast**. It is the one configured place the lifecycle commands read:
`/spawn` and `/rename` resolve `beasts_root` / `origins_root` / `template_source`
from here, and the pool **registry** (`/fleet`'s recomputed cache) lives here too.
The habitat home **absorbs the pre-2.1 `_fleet/`** — fleet root and habitat home
are now the same folder. It also hosts the **asks relay** (`.habitat/asks/`) — the
file-based inbox `/inbox` reconciles, where beasts (and the human, as `operator`)
deliver async questions/answers.

**OS-agnostic (DEC 75).** All file work uses CC's own tools (Glob / Read / Write);
no shell assumed.

## 1. Locate the habitat home (name-agnostic)

Walk this beast's ancestor directories for a folder containing the marker file
**`habitat.md`** (or `registry.md`). The nearest such directory is the habitat
home; its parent is the **habitat root**. **Detect by the marker, never hardcode
the folder name** — the conventional name is `.habitat/`, but discovery keys on
content (same rule `/fleet` step 4 uses).

- **Found** → resolve its config for the requested action.
- **Not found, but a legacy `_fleet/` exists** at the root → treat it as the home
  and offer to migrate (step 4).
- **Neither** → this is the cold-create path; go to `init` (step 4).

## 2. Parse the argument

- **`show`** (default if a home exists) → read-only: print the resolved config +
  a one-line registry summary. No writes.
- **`edit`** → surgically change one config field (propose → confirm → Write);
  **never silently overwrite** the file.
- **`init`** → bootstrap the home if absent (step 4).

## 3. Show / edit

- **show:** Read `.habitat/habitat.md` and echo `beasts_root`, `origins_root`,
  `template_source`, the flags, and whether `registry.md` exists (+ its generated
  date). Point to `/fleet show` to refresh the registry.
- **edit:** Identify the field, show the current value, propose the new one,
  confirm, then Write the single change back. Leave every other line untouched.

## 4. Bootstrap (`init`) — the cold-create path

When no home exists, **propose** creating `.habitat/` at the **habitat root** (the
parent dir holding this beast and its siblings — the same place `/fleet` would
establish the fleet root). On approval:

1. **Derive each value from where it actually lives** — environmental values live, but record
   `template_source` as a **portable** coordinate:
   - `beasts_root` = the habitat root just resolved (where beasts live as siblings).
     *(Genuinely environmental — derive live, never hardcode.)*
   - `origins_root` = the bare-repo store, the **root directory under which** `/spawn` runs
     `git init --bare` (note: `origins_root`, *not* "origins" — a folder, not a remote).
     **Optional — default it to blank/uninitialized**, never to `beasts_root` (a shared store
     should be deliberate, never the beast folder itself). **Offer** a path (e.g.
     `/path/to/bare-origins`), but accept "leave it blank": blank ⇒ `/spawn` produces
     **local-only** beasts. *(Also environmental.)*
   - `template_source` = the canonical BeastForge source, resolved **provenance-first per
     `/reforge` §1a** — prefer the beast's own clone `origin` / launch-front-matter **URL**, or
     the published BeastForge URL; a local sibling only as a **confirmed last resort**. **Record
     the portable form (a git URL), not a machine-local path** — this config travels (every
     sibling reads it). *(Here "never hardcoded" means no machine-local literal; the canonical
     published **URL is a legitimate portable value**, not a forbidden hardcode.)*
2. **Write `.habitat/habitat.md`** in the schema below.
3. **Migrate a legacy `_fleet/`** if present: **recompute the registry fresh** into
   `.habitat/registry.md` via `/fleet`'s § Recompute (the registry is a derived cache — prefer
   recompute over moving the stale file). Announce it; leave the old `_fleet/` empty folder for
   the User to remove (don't force-delete).
4. **Recompute the registry** into `.habitat/registry.md` per `/fleet`'s
   **§ Recompute the registry** (this command does **not** duplicate that logic —
   it calls it).
5. **Scaffold the asks relay** — create `.habitat/asks/` and the reserved
   **`operator`** participant's inbox (`operator/tmp/`, `operator/new/`,
   `operator/cur/`, `operator/sent/`) — the habitat-wide **human inbox**. Each
   beast's own participant inbox is scaffolded here too — **every habitat sibling
   is a relay participant by default** simply by living in the habitat (no join
   step); a sibling carrying a `.fleetignore` is isolated and gets none. The
   relay is the transport `/inbox` reconciles. *(The `.habitat/` home is a derived
   store outside any repo — these dirs aren't committed; regenerable.)* *(The relay also
   **self-bootstraps**: `/inbox` establishes whatever is missing — the home, `asks/`, an
   inbox — on first delivery, so this explicit scaffolding is a convenience, not a prerequisite.)*

### `.habitat/habitat.md` schema — plain `key: value`

**One canonical shape, used by `/habitat init` AND by `getstarted.md`** (so there is no drift
between the chat on-ramp and `/habitat`). Each `key: value` on its own line; **an empty value
means unset** — the config file carries *values only*, never an annotation-as-value. The
*meanings* live here in the command doc, not in the file.

```markdown
# Habitat

beasts_root: <habitat root>
origins_root: <bare-repo store — or empty = local-only beasts (no bare repos)>
template_source: <canonical BeastForge — a git URL (portable, preferred) or a local path>

# Flags (optional; omit a line to take its default)
spawn.nest_default:           # default `--in <sub>` for /spawn (empty = beasts_root direct)
spawn.bare_suffix: .git       # bare-repo name suffix in origins_root
rename.rename_origin: ask     # /rename upstream bare-repo rename: ask | yes | no
relay.max_hops: 15            # asks-relay loop-guard depth net: surface a thread to the human once its derived hop count (messages on one thread_id) reaches this. Tune freely.
relay.escalate_after_k: 3     # asks-relay disagreement escalation: surface to the operator once the same point is unresolved across this many exchanges (distinct from no-progress and max_hops).
```

**Reading it (every consumer — `/spawn`, `/rename`, `/habitat show`):** parse each `key: value`;
an **empty value (or an absent line) = unset**. `origins_root` empty ⇒ local-only spawns. Never
treat a comment/annotation as a value. *(Back-compat: a legacy habitat may use a Markdown table —
read the same keys from its cells, treating an empty or annotation-only cell as unset.)*

Edited via `/habitat edit`; the pool registry is the sibling file `registry.md` (recomputed by
`/fleet`, not edited) — `/habitat` does not invent a second schema for it.

## 5. Show + close

Show the resolved config (and registry summary). The habitat home is a derived/
config store outside any single repo — not committed to a beast; regenerable.
Recommend nothing to commit unless the action also touched this beast's files.
