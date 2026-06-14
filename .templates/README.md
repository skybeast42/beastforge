# .templates/

Reusable shipped assets — starting points for project deliverables that
benefit from a consistent house style. **Identical at rest in root + `apps/template/`**
(like `CLAUDE.md` / `.template_changelog.md`); a field project inherits this
folder when it copies the template.

Most templates need **no dedicated command** — the asset itself is the
spec. CC, asked to produce a deliverable with a template here, reads it
and uses it as a starting point. The exception today is
`slide_deck.html`, which has a dedicated **`/deck`** command (harvest-
driven; see below); other templates can earn their own command if/when
richer machinery justifies it.

## What's here

### `slide_deck.html` — SkyBeast-themed slide deck

Self-contained, offline-capable, embeddable HTML presentation. The file's
top comment is the canonical convention spec; the short version:

- **Five layouts:** `slide--title` · `slide` (default statement) ·
  `slide--split` (text + media) · `slide--full` (wide band) ·
  `slide--photo` (full-bleed image + optional caption overlay).
- **Primitive:** `<pre><code>…</code></pre>` for code/config blocks
  (works inside any layout's `.wrap`).
- **Authoring vocabulary:** `kicker · h1/h2 · sub · ul/li · tok` — primitives
  styled by the deck's `<style>` block.
- **Dual-mode:** standalone view (full deck, keyboard nav ↓/↑ Space PgDn/PgUp
  Home/End) and embedded preview (via `?preview` query string — auto-cycling
  card at any iframe size).

**Usage with `/deck` (preferred):** run `/deck <topic>` — it reads
`MASTERPLAN` + `DECISIONS` + the publication-capture harvest (when
present), proposes a **graphic-forward** outline (it proposes a visual
wherever a slide benefits from one — including just reinforcing the point
through a second channel — never gratuitously), generates the populated
deck on approval, and saves to the right output channel. See
`.claude/commands/deck.md`.

### `deck_svg_kit.html` — in-theme SVG primitive kit

A companion gallery of ready-to-paste inline-SVG shapes that match the deck
theme automatically (every fill uses the deck's CSS vars). Open it to browse
the primitives rendered in-theme; it doubles as the visual documentation.

- **~10 primitives:** flow-arrows · stack/layers · before/after · big-stat ·
  node-graph · checklist · comparison bars · cycle/loop · funnel/triage ·
  annotation-callout.
- **Use:** copy a shape's `<svg>` into a slide's media slot (usually a
  `slide--split .col--media .wrap`, or a `slide--full .wrap` for a wide
  diagram); relabel the text; emphasize one element by swapping a fill to
  `var(--accent)`.
- **Extend:** the kit is a starting set, not a closed list — when no shape
  fits, author a new one in the same idiom (viewBox-based, `var(--…)` fills,
  one accent, a short label) and optionally add it back.
- **Other graphics:** images and R-generated charts embed too — see the
  *external-graphics route* in `.claude/commands/deck.md` (convert PDFs to
  SVG/PNG for an offline-portable deck; annotate with the callout primitive,
  a `slide--photo .caption`, or by pre-marking the image).

**Manual usage** (no command):

1. Copy `.templates/slide_deck.html` as the starting point.
2. Replace the demo `<section class="slide …">` blocks with the deck's
   actual content; **keep** the `<style>` and `<script>` blocks intact.
3. Save the populated deck:
   - **Beast-level deliverable** (for external use, an event, the blog) →
     `tracks/00_decks/<date>_<name>.html` (a beast-laid track, per `CLAUDE.md` →
     *Output channels*).
   - **Task-internal draft** (part of an active task's work) →
     that task's `05_Reports/deck.html` (or a date-stamped name).

**Brand notes.** The template carries the SkyBeast visual identity (dark
void · Swiss-red accent · system fonts · propeller-beast mark) — SkyBeast is
the template author's house style; swap it freely for your own. For
SkyBeast-published content (the blog, related presentations) that's
deliberate. For a non-SkyBeast context (a client deck, a domain-neutral
training), **fork this file** rather than dilute the canonical.

## Adding new templates

A new shipped template earns a slot here when it (a) is reusable across
projects and (b) has a clear convention worth standardizing. Document each
addition as a sibling subsection: *what it is · what's in it
(layouts/primitives) · how to use · where to save the output*.
