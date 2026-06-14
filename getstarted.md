<!--
getstarted.md — the CC-guided on-ramp. Lives at the beastforge repo ROOT.
A newcomer pastes this file's link to Claude Code and says "follow it". It is
instructions FOR the agent: stand up the reader's first beast, conversationally.
Kept small + plain Markdown so it can be followed verbatim, step by step.
-->

# Get started with BeastForge

**You are Claude Code, helping someone set up their first BeastForge "beast" — a project
that keeps its own memory.** First, make sure you actually have this file's *full* text, not a
summary: WebFetch may condense it, and these are steps to **execute exactly**, not to paraphrase.
If what you have looks summarized/abridged, re-fetch the raw file in full before continuing —
e.g. `curl -fsSL https://raw.githubusercontent.com/skybeast42/beastforge/main/getstarted.md` (or
read the raw URL directly) — and follow *that*.

**They may not be technical, and that is fine. Be a calm guide:
do the work yourself, explain in plain language, ask only what you genuinely cannot work
out, and offer sensible defaults they can just say "yes" to. No jargon walls, one thing at
a time. Nothing happens on their machine without their approval.**

Work through the steps below, talking to them as you go.

## 0. Hello, and what is about to happen

In a sentence or two, plainly: you will make a folder on their computer to hold their
projects (each one is a "beast"), create their first one shaped to what they want to do,
and get it ready to use. Mention they will be asked to approve a couple of steps (fetching
a file, downloading the template); that is normal.

## 1. Check the basics

- Run `git --version`. If git is not installed, tell them gently how to get it
  (https://git-scm.com/downloads) and pause here; you can carry on once it is in place.
- Check `git config user.name` and `git config user.email`. If either is blank, ask for
  their name and an email and set them with `git config --global` (a beast records its
  history with git, so this is needed once).
- That is the whole list: git, an internet connection, and you.

## 2. Where the projects will live (the "habitat")

- See if they already have a habitat (look for a `.habitat/` folder, or just ask). If they
  do, use it.
- If not, suggest a default: a folder named `habitat` (their choice of name) in their home
  directory — a single place where their beasts live together, which stays tidier than
  scattering them around. Let them change the name or place; otherwise create it.
- Inside it, create `.habitat/habitat.md` in the **canonical shape** (the same plain
  `key: value` shape `/habitat` uses — one key per line, an empty value means unset):

  ```
  # Habitat

  beasts_root: <the habitat folder you just made>
  origins_root:
  template_source: https://github.com/skybeast42/beastforge
  ```

  `template_source` (the **URL** — keep it a URL, it travels) is what `/reforge` uses later to
  offer template updates. **Leave `origins_root` empty** — it is an *optional* place to keep
  backup copies of beasts, and a first beast does not need it; mention they can set one up later
  if they ever want their beasts backed up to a shared location. *(If they explicitly want backups
  from the start, this is the one knob that changes setup's behavior: set `origins_root` to a folder
  path now and `/setup`/`/spawn` will wire each beast a local backup origin there automatically.
  Most first-timers should leave it blank.)*

## 3. What do they want to build?

- Ask, in plain language, what they would like their first beast to help with. Offer a few
  concrete examples so it is easy to answer (organising a project, planning something, a
  piece of writing, some analysis) — but their own idea is best.
- Suggest a short lowercase name for the beast from their answer (e.g. `thesis`, `garden`,
  `accounts`); let them change it. This becomes the folder name.

## 4. Create the beast

- Clone the template into the beast folder:
  `git clone https://github.com/skybeast42/beastforge <habitat>/<beastname>`
- That is all the cloning you do by hand. **Do not strip git here** — the next step (setup)
  deliberately turns this clone into *their own* clean project. Just clone and move on.

## 5. Bring the beast to life

- Read `<habitat>/<beastname>/CLAUDE.md` (the beast's rulebook) and
  `<habitat>/<beastname>/.claude/commands/setup.md`, then **carry out that setup with them**
  in this conversation — **work through every step of `setup.md` directly** (you do not need
  the slash command loaded; don't skip steps). Among other things, setup:
  - names the project and writes its nameplate;
  - **makes it their own**: gives the beast a fresh, clean history with no leftover link back
    to my template repo — *they own it*. Because they cloned (rather than using GitHub's "Use
    this template"), and they left `origins_root` blank, the beast is **local-only** for now;
    tell them plainly that if they ever want it backed up online they can add their own remote
    later, or start a future beast from GitHub's "Use this template" (which gives a hosted copy
    from the start);
  - replaces this landing README with the project's own (everything above the
    `<!-- BEAST-README-BELOW -->` marker) and removes the launch-only files (`getstarted.md`,
    the banner);
  - confirms the habitat folder you set up in step 2;
  - **marks the beast ready** (so it won't ask to set itself up again next time).
- Then the one thing to remember: **a beast's abilities (the `/commands`) only switch on once
  Claude Code is running *in the beast's own folder*.** In **VS Code**, open that folder as the
  workspace; on the **command line**, close Claude, `cd` into the folder, and start it again.
  After that, just say `/resume` — everything the beast knows lives in the folder, so it picks
  up exactly where you left off.

## 6. A short tour (optional, skippable)

Once they have a working beast, offer: *"Want a quick tour of what it can do?"* If yes, show
it **on their own beast** — where decisions get written down (`DECISIONS.md`), the running
to-do list (`TODOLIST.md`) — and just *name* the bigger things for later: `/audit` (have it
check its own work), `/spawn` (make another beast), and that beasts can pass on what they
learn to each other. Keep it short and stop the moment they have what they need.

---

**Throughout:** infer before you ask, prefer defaults they can wave through, keep the
language human, and never make them feel they must understand the plumbing. If they are on
the **command line** and pasting text is fiddly, the terminal paste is usually `Ctrl+Shift+V`
or `Shift+Insert` (not `Ctrl+V`). If something goes wrong, explain it simply and fix it for them.
