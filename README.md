<p align="center">
  <img src="banner.png" alt="BeastForge — Verifiable Agentic Engineering. Because you can't audit a vibe." width="100%">
</p>

# BeastForge

> **Verifiable Agentic Engineering. Because you can't audit a vibe.**

AI coding agents write code fast and forget *why*. Close the chat and the plan, the
decisions, the dead ends are gone. **BeastForge** is an open project template that keeps a
project's memory in the **repo, not the chat**: the plan, the live state, every decision,
and the open questions live in version-controlled files the agent re-reads each session. So
it resumes cold, every change traces back to a logged decision, and a human can read it,
check it, and re-run it **without the AI**.

**What that looks like.** You close your laptop mid-task and reopen it next week — `/resume`
reads the repo and picks up exactly where you were, nothing re-explained. Every change is one
line in `DECISIONS.md`, with its reasoning. Months later someone re-runs the work from a single
command and can see *why* each call was made — no agent in the loop.

**Is this for you?** If you run *any* multi-session project with an AI and want it to outlast
the chat window — code and data analysis, yes, but also a book, a research area, a knowledge
base, a planning effort — then yes. You don't need to be a programmer: the agent does the
file-wrangling, you read and decide. The one prerequisite is **[Claude Code](https://claude.com/claude-code)**
(Anthropic's agentic coding tool — a free download that drives everything here), plus **git**.

## Get started — three ways

All three end the same way: open your new project **as a folder/workspace** in Claude Code and
run **`/setup`** (it names the project, settles the git origin, and tidies the launch files),
then **`/resume`** to begin. Tip: keep your beasts together inside one **"habitat" folder** (any
name you like) rather than scattered — it's tidier and it's what `/spawn` and the fleet commands
expect.

1. **From a chat (easiest, nothing to clone yourself).** In Claude Code, paste and send:
   > Fetch the full raw text of https://raw.githubusercontent.com/skybeast42/beastforge/main/getstarted.md and follow it exactly, step by step (it's a short instruction file to execute, not to summarize).

   Claude Code reads [`getstarted.md`](getstarted.md) and walks you through your first beast in
   one conversation — including where to put it. You need git, an internet connection, and Claude Code.
2. **Clone it.** `git clone https://github.com/skybeast42/beastforge <habitat>/my-project`, then
   open `my-project` in Claude Code and run `/setup`. Note: a plain clone's `origin` points at
   *this* template — `/setup` gives the beast its own clean history and (by default, unless you've
   configured a habitat origin) leaves it **local-only**, so you never accidentally push into the template.
3. **Use this template (on GitHub) — best if you want it backed up online from day one.** On the
   repo page, click **Use this template** to create *your own* GitHub repo, clone *that* into your
   habitat folder, then run `/setup`. Because it is already your repo, `origin` is yours and
   pushable — the cleanest path to a hosted, backed-up beast.

**A worked example — coming soon.** [ROASTBEAST](https://github.com/skybeast42/roastbeast) is a
complete modelling problem taken end to end inside a beast — study design, simulation, analysis,
a scored report, reproducible from one command. The plans are public now; the run and write-up
land soon and will become a worked example right here.

MIT licensed ([LICENSE](LICENSE)) — anything you build with it is yours. New account, decades
behind it — the story's on the [GitHub profile](https://github.com/skybeast42); more at
[skybeast.ch](https://skybeast.ch).

<!-- BEAST-README-BELOW: /setup replaces everything above this line with your project's nameplate, and removes getstarted.md + banner files. Everything below is the generic explainer your beast keeps. -->

## What a beast is

A **beast** is one project run by its own Claude Code — a capable colleague that
**doesn't forget**. A chat window forgets the moment it scrolls away; a folder of
scripts can't explain itself. A beast keeps its memory, decisions, and trail in
the repo, so the work is **reproducible, auditable, and continuous** — value that
compounds across sessions instead of restarting every time.

That memory is just **plain files you can read** — no database, no magic. A row in
`DECISIONS.md`:

```text
| 14 | 2026-06-12 | Cache the parsed feed in 02_Data/ — re-parsing on every run was the bottleneck |
```

…a `STATE.md` that says where things stand and what's next, a brief that pinned down the task.
Text you — or the next person, or an auditor — can check without taking the AI's word for it.

One shape of worker, many shapes of work:

- **An assistant that remembers** — notes, ideas, and areas live in `tracks/`;
  `/resume` brings any later session up to speed deterministically.
- **Reproducible analysis** — `work/` holds task-first units that re-run
  end-to-end (brief → scripts → data/output → report); every change is a decision
  row and a boundary commit.
- **Software & apps** — `apps/` carries self-contained software, each with its own
  framework, decisions flowing back to the shared spine.
- **A living reference** — `/ground` distils domain material into `guidance/` the
  beast consults on demand, so it learns your domain once, not every session.
- **A team that shares and passes work along** — beasts living as siblings: more than
  an assistant, a team you can stand behind.
    - **Learn from each other** — any beast can inherit another's `guidance/`
      (`/harvest`); `/fleet` shows the pool; grow it with `/spawn` and `/rename`.
    - **Leave each other notes** — a question for another beast, or for *you* once
      you've stepped away, goes in the **asks relay** (*the next section*).
    - **Wall one off** — a `.fleetignore` fully isolates a beast — or a whole folder
      of them — in both directions.

## Where this fits

BeastForge isn't a model and isn't an agent runtime — it's a **layer on top of one**. Claude
does the reasoning; **Claude Code is the harness** that runs the loop and calls tools; BeastForge
adds the part neither of them keeps — the **project's durable, auditable memory**:

```text
   BeastForge     ← your project's memory, decisions, conventions  (files in your repo)
  ──────────────
   Claude Code    ← the harness: runs the loop, calls tools        (this is what you install)
   Claude         ← the model: the reasoning
```

Most of the "agent stack" is about making one agent capable *right now*. BeastForge is about a
different axis: making the *project* it works on survive across sessions and agents, and checkable
by a human **without the AI**. Swap the model or the harness — the repo, the memory and the trace,
is the part that stays yours.

## Siblings that pass work along — the asks relay

A lone beast just talks to you in the chat. Put a few beasts side by side in one
**habitat** and they get a way to reach each other — and reach *you* — without
anyone having to be in the same conversation at the same time: the **asks relay**.

It's plain and concrete — **a shared inbox of notes, kept as files**. When a beast
hits a question it can't settle this session, or one that's really for a *different*
beast, it leaves a note in that recipient's inbox; the recipient reads it next time
it runs and writes an answer back. You are a **first-class participant** — the
`operator` inbox is yours. A beast running on its own with nobody watching files its
open questions to you there instead of guessing. You have **no commands of your own**,
so you read and reply **through whatever beast you're already in**: its **`/inbox`**
shows you your inbox and, when you give an answer, **relays it back to the asker for
you** — you never touch the files. (Or just open the beast that asked and answer it
live.) `/inbox` also reconciles the siblings' own asks and routes each settled outcome
to `DECISIONS.md`.

What it is **not**: beasts working while you sleep. A beast runs **only when a session is
open in its folder** — the relay moves notes *between* running sessions, it doesn't start
anything; to get work out of another beast you leave it a note and **wake it**. You stay the
**end-auditor** throughout: beasts investigate and draft, but anything irreversible (a push, a
publish, a delete) waits for your say-so. A team that passes work along — not an autonomous swarm.

A beast *can* work a little on its own: run **`/loop /inbox`** and it keeps checking
its inbox on an interval — picking up and acting on relayed tasks without you
re-prompting, bounded autonomy with you still gating anything irreversible. Same catch,
though: it only runs **while that beast is awake** (a session open in its folder), and
every awake beast spends tokens — so you `/loop` the few that earn it, not the whole pool.
(Leaving one looping unattended? Run it contained — a sandbox, no push credentials, backups;
relay notes are untrusted input and BeastForge won't sandbox for you. The loop-guard mechanics —
goal-on-disk, escalation and hop limits — live in `CLAUDE.md` if you want the depth.)

## How a beast is organised

The entry point for Claude Code is [CLAUDE.md](CLAUDE.md) — read it first; it's the
single source of truth for all rules (run `/conventions` for a rendered summary) — and it's
auto-loaded every session, so it costs some tokens every turn: a deliberate trade, worth it for
multi-session auditable work, overkill for a quick throwaway. The shape is a **global spine**
(the beast's memory + governance, always present) plus a few
**homes** that do the work — a beast specialises by which homes it fills:

```text
my-beast/
├── CLAUDE.md        ← the rules (CC reads this first, every session)
├── MASTERPLAN.md    ← durable strategy & why
├── STATE.md         ← where things stand right now (one screen)
├── DECISIONS.md     ← every settled call, one line each
├── TODOLIST.md      ← backlog / icebox
├── work/            ← bounded, reproducible, briefed tasks
├── apps/            ← self-contained software (each its own framework)
├── tracks/          ← notes, ideas, areas — the informal trail
├── guidance/        ← how-to practices CC follows (learned once or harvested)
└── background/      ← a reference shelf (consulted on demand, not auto-loaded)
```

The **top five files are the spine** — the beast's memory and governance, there from day
one. The folders below are the **homes**, each filling out only as the work needs it.
Here's what the main three look like in use.

**`apps/` — software, an app, a website.** Each app brings its own framework and
lifecycle; only its cross-cutting decisions flow back to the spine.

```text
apps/
└── my-site/         ← its own README, src/, build — whatever the stack needs
```

**`tracks/` — a notebook, a book, an area you keep notes on.** Free-form, no ceremony.

```text
tracks/
├── 00_insights/     ← reserved capture channel (surprises, gotchas, lessons)
└── my-book/         ← chapters, outline, research — shape it however you like
```

**`work/` — a reproducible analysis.** The disciplined home: each task is a
self-contained, re-runnable unit with a fixed stage order and a brief (its contract).

```text
work/
└── TASK_001_sales_analysis/
    ├── 00_Briefs/        ← the contract: a brief (+ numbered tickets)
    ├── 01_DataSource/    ← raw input, never modified by a script
    ├── 02_Data/          ← processed / derived
    ├── 03_Scripts/       ← scripts in run order + SCRIPT_00_RUNALL (one command re-runs it all)
    │   └── AIterritory/  ← the AI's own assessment code (see below)
    ├── 04_Output/        ← results
    │   └── AIterritory/  ← + the AI's reasoning, written down
    └── 05_Reports/       ← the deliverable
```

Stages are **lazy** — a task creates only the ones it needs (a quick note-task might be
just `00_Briefs/`).

**`AIterritory/` — where the AI shows its work.** A genuinely nice piece. Where a person
would eyeball a deck of plots, an AI can't — so it **writes code to see**: the exploratory
probes, the sanity checks, the "is this actually real?" digging it does before drawing a
conclusion. Those scripts and their output live in `AIterritory/`, each beside a short
narrative (*question → method → what it found → honest caveats*), and **written to the same
coding style** as the rest so a person can actually read them. They stay **outside** the
delivered `RUNALL` pipeline — the AI's working-out, not the final product — so the reasoning
behind every conclusion that reaches the results is **there to review and audit** when you
want it, instead of lost in a chat. The human stays the end-auditor.

**Beyond one beast — `.habitat/`.** Stand several beasts side by side in one folder (a
"habitat") and they share a small **`.habitat/` home** that lives *outside* any single
beast: the config `/spawn` and `/reforge` read (where the template lives, where to keep
optional backups), the **pool registry** `/fleet` shows, and the **asks-relay** inboxes.
A lone beast needs none of it — it appears the moment you have siblings. (One operator, though:
BeastForge is single-user by design — the "team" is your agents, not several people sharing a repo.)

Hidden machinery (`.templates/`, `.claude/`, `.template_version`, the changelog) wears a
leading dot and stays out of the way.

## Teaching it your way — grounding

Most templates make you **write the rules** — fill in a style guide, document your
conventions, keep a contributing doc current. BeastForge inverts that. You don't describe
how you want things done; you **show it**, and CC distils that into guidance it can
actually follow. The bet: an agent is better at turning your examples into a clean,
followable rule than you are at writing the rule by hand — and won't leave it vague.

Point **`/ground`** at almost anything:

- **Examples** — a few files done the way you like them; CC reads the pattern and writes it down.
- **The web** — hand it a topic and it can run **deep research**, then distil what it finds.
- **Just the chat** — explain it in your own words; that counts too.

Each becomes a `guidance/<topic>/` the beast **consults on demand** — only when the work
calls for it — so it learns your domain *once* instead of being re-told every session. And
because guidance is portable, you **ground it once and `/harvest` it to a sibling**: the
pool gets smarter as a whole.

The payoff is concrete. Want a beast to write code in *your* style? Often that's **one
command** — point `/ground` at a handful of your files and it's captured. The same holds
for a whole body of know-how: a stack of past work, or even a multi-day workshop, grounds
into a set of guidance topics the beast then works from.

## Working in it

You don't have to memorise commands — **just say what you want in plain language**
and CC routes it to the right one (or does it directly); the table is a map, not a
vocabulary you must learn first.

**The handful you'll reach for first:**

| You want to… | Command |
|---|---|
| Bootstrap a new project (once) | `/setup` |
| Pick up where you left off | `/resume` |
| Start a task | `/brief` |
| Teach it your way | `/ground` |
| Close out the session | `/wrap` |

<details>
<summary><b>▸ The full command set</b> (click to expand)</summary>

**Day-to-day**

| You want to… | Command | What it does |
|---|---|---|
| Pick up where you left off (or cold-start dumped code) | `/resume` | Reads `STATE` + `MASTERPLAN`, runs `/inbox` + the integrity checks, proposes the next action; on a fresh template points you to `/setup` |
| See progress at a glance | `/status` | Counts tasks; lists open tickets, audits, asks, recent decisions |
| Close out the session | `/wrap` | The `/resume` bookend: reconcile, persist, assert cold-resume-readiness, propose the boundary commit |
| Measure token use | `/tokens` | Sums token use across all the project's sessions → `tracks/00_insights/token_usage.md` |
| Check filesystem invariants | `/check` | Task-integrity + reconciliation; offers to retro-wrap brief-less tasks (never gates) |

**Doing the work**

| You want to… | Command | What it does |
|---|---|---|
| Start / amend a task | `/brief` · `/ticket` | Scaffolds `work/TASK_NNN_name/00_Briefs/`; tickets add numbered amendments |
| Record a decision · commit at a boundary | `/decide` · `/commit` | Appends a `DECISIONS.md` row; proposes a CC-authored commit you approve |
| Run / close a multi-specialist audit | `/audit` · `/audit-resolve` | Specialist subagents → ranked findings in `tracks/audits/`; each routed to ticket / decision / defer |
| Shape the strategy | `/masterplan` | Helps formulate `MASTERPLAN.md` — strategy + a conceptual step sequence |
| Ground the project in a domain | `/ground` | Distils material at one or more paths into `guidance/` (path-scoped, opt-in) |
| Generate a slide deck | `/deck` | Harvest-driven deck using `.templates/slide_deck.html` |
| Tidy the README · see the rules | `/readme` · `/conventions` | Reorganises this file; renders the rules & command index from `CLAUDE.md` |

**Fleet & communication** (only once beasts live as siblings in a habitat)

| You want to… | Command | What it does |
|---|---|---|
| Pick up cross-beast & operator asks | `/inbox` | Reconciles the asks-relay inbox — answer incoming, collect replies, route outcomes to `DECISIONS.md`, skip resolved; **surfaces your `operator` inbox to read & reply through this beast** |
| See the pool | `/fleet` | Shows the pool registry (read-only) — every habitat sibling, minus any walled off with a `.fleetignore` |
| Inherit a guidance topic from a sibling | `/harvest` | **Default-open** — any sibling's `guidance/`; semantic match → anti-wizard manifest → copy-with-provenance |
| Configure the habitat home | `/habitat` | Views/edits `.habitat/` (`beasts_root`/`origins_root`/`template_source`); bootstraps it if absent |
| Spawn / rename a sibling beast | `/spawn` · `/rename` | Stamps a new sibling from the template (bare-init → clone → populate → identity); renames folder + origin and recomputes the registry |

**Setup & upkeep**

| You want to… | Command | What it does |
|---|---|---|
| Bootstrap a new project (one-time) | `/setup` | Two questions, fills the README, sets the window color |
| Set this window's color | `/vscolor` | Writes a window color into `.vscode/settings.json` |
| Upgrade to a newer BeastForge | `/reforge` | Walks the changelog migration notes; safe, human-approved, per-step commits |

</details>

Roles: **CC** (Claude Code) plans in plan mode and implements; the **User** decides.
CC proposes, User decides.

## Reproducing the work

Each `work/TASK_NNN/` reproduces end-to-end on its own: run
`03_Scripts/SCRIPT_00_RUNALL.*`; input comes from the task's `01_DataSource/`,
processed data lands in `02_Data/`, artifacts in `04_Output/`, the deliverable in
`05_Reports/`. The `.*` is deliberate — scripts are whatever the work needs (R, Python, shell, …),
and the environment that lets them re-run (language versions, packages via renv/conda/venv) is
recorded in `guidance/02_derived.md`, so *reproducible* means on a fresh machine, not just yours.
See `MASTERPLAN.md` for the intended sequence and `STATE.md` for
where execution currently stands. *(Not every task fills every stage — tasks that
produce reproducible artifacts do; brief-only tasks, where the deliverable is the
change itself or lives in `apps/`/`tracks/`, don't.)*

## This README is yours to adapt

It ships with the full generic explainer above so a fresh beast reads well from day
one. **Read it, then adapt it** — trim what doesn't fit, keep the nameplate current
as the project takes shape. A `/reforge` upgrade refreshes the shared body + command
table but **never overwrites your nameplate** — your adaptations survive. (And yes,
the template documents itself. It's that kind of project.)
