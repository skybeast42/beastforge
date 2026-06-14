---
description: Generate a slide deck from project material, using the .templates/ deck
argument-hint: [topic — defaults to current focus inferred from STATE/MASTERPLAN]
---

Produce a slide deck. Focus: $ARGUMENTS (default: infer from `STATE.md` / `MASTERPLAN.md`; ask if unclear).

1. **Read sources** (proportional to scope):
   - `.templates/slide_deck.html` — canonical style + the five layouts + the code-block primitive.
   - `.templates/deck_svg_kit.html` — the in-theme **SVG primitive kit** (flow-arrows, stack, before/after, big-stat, node-graph, checklist, bars, cycle, funnel, annotation-callout). Copy a shape into a slide; recolor/relabel; or invent new ones in the same idiom.
   - `.templates/README.md` — folder conventions + where to save output.
   - `MASTERPLAN.md` — the *what & why* (the durable story).
   - `DECISIONS.md` — settled calls relevant to the topic.
   - `tracks/00_insights/deck.md` — the **deck-insights harvest** if present (pre-distilled, slide-ready). **When present, prefer it over re-derivation.**
   - a task's `05_Reports/` + relevant `04_Output/` — concrete results to point at.
   - The User-provided topic/focus.

2. **Bootstrap capture if missing** (one-time per project). If `tracks/00_insights/deck.md` doesn't exist AND `guidance/02_derived.md` lacks an *Active insight captures* section (or it lacks a **Decks** type), propose creating both / adding the type. On approval: create the harvest file (with the schema header — *Mechanic → Design choice → Slide angle ("so what")* — plus an honesty caveat) AND add the `02_derived` section/type. From that point on CC harvests during regular work, not just at `/deck` time.

3. **Propose an outline before producing** (~7–12 slides). For each: one-line title · layout (`title · statement · split · full · photo`) · source(s) (which DECISIONS rows / harvest entries / MASTERPLAN bullets / work artifacts) · **a graphic plan (see below)**. **Include the proposed save destination** (per step 4 rule) so the User approves it with the outline. **Flag thin slides — ask, don't fabricate.**

   **Be graphic-forward — propose a visual wherever a slide _benefits from visualization_.** That bar is *low on purpose*: a graphic earns its place not only when a concept is hard to word, but also when it **reinforces the point through a second channel** (text + visual = two routes to the same idea, which lands harder and lightens a dense deck). Lead toward `slide--split` (point left, graphic right), `slide--full` (a wide diagram), or `slide--photo` (a full-bleed image) — don't default everything to `statement`. The one guard: **no purely decorative graphics** — every visual carries or reinforces a point. For each slide that benefits, propose **one of four routes** in the outline and let the User pick:
   - **kit SVG** — name the `deck_svg_kit.html` primitive that fits the shape (e.g. *flow-arrows for the research→place→ground seam*).
   - **invented SVG** — no kit shape fits → CC authors a new in-theme SVG in the same idiom (viewBox-based, `var(--…)` fills, one accent, a short label).
   - **external asset** — an image or R-generated chart/output (see *External graphics* below).
   - **text** — keep it as a statement (the User opts back to text).

   Mark each outline slide with its chosen route so the approved outline is the build spec.

4. **On approval, generate**:
   - Copy `.templates/slide_deck.html` as the starting point.
   - Replace the demo `<section class="slide …">` blocks with the agreed slides; **keep `<style>` + `<script>` intact**.
   - **Save destination — default to beast-laid.** Save to `tracks/00_decks/<date>_<topic>.html` (a beast-laid deliverable track — date-prefixed, per `CLAUDE.md` → *Output channels*) by default. Save to a task's `05_Reports/deck.html` only when the deck is that task's own deliverable (part of an active task's work, not a standalone).
   - **External graphics (images, charts, R-generated output).** A slide's graphic route may be an external asset, not an SVG. To keep a deck **offline-portable** (its whole point — self-contained, opens anywhere):
     - **Embed** via `slide--split` (`.col--media`), `slide--full` (`<img style="width:100%">`), or `slide--photo` (full-bleed + optional `.caption`).
     - **Format for portability:** prefer **SVG** (vector, crisp, themeable) or **PNG**. R output → `ggsave("plot.svg", …)` is ideal; a PDF must be **converted** (e.g. to SVG/PNG) before embedding — PDFs don't render as `<img>` and break the single-file story. For a *truly* single-file deliverable, inline the asset as a **data-URI**; otherwise reference it by relative path and keep it beside the deck.
     - **Where assets live:** beside the saved deck (a task's `04_Output/` if it's task-internal); never reach outside the task for a reproducible artifact.
     - **Annotate / mark up** when the point is *a region* of the image: overlay a `slide--photo .caption`, drop the kit **annotation-callout** SVG on top (ring + leader + label), or pre-mark the exported image. Keep annotations in the accent colour so they read against the theme.

5. **Honesty floor.** Every factual claim must be traceable to a `DECISIONS.md` row, a work artifact, a harvest entry, or User-confirmed input. If a claim isn't grounded, **soften or drop it.** See `tracks/00_insights/deck.md` *Insight 7* for the canonical example (the autonomous-vs-prompted caveat: *"designed for"* not *"proven"*).

6. **Close the loop.** After saving, briefly report what was generated and where. If new deck-worthy insights surfaced *while making the deck*, append them to `tracks/00_insights/deck.md` (the harvest convention).
