#!/usr/bin/env python3
"""
token_tally.py — shipped asset for the /tokens command.

Sums Claude Code token usage for the CURRENT project across ALL of its session
transcripts (every chat window you opened for this project), and writes a report
to tracks/00_insights/token_usage.md. Counts only — no money conversion
(per-token prices change; do that later against whichever classes you choose).

Why a script (the one command that needs one): the transcripts can hold tens of
millions of tokens of content, far too large to read into an agent's context, so
they must be stream-processed. Pure Python 3 stdlib; runs anywhere Python does.

Append-only, time-sorted ledger:
  Each session, once tallied, is recorded in tracks/00_insights/token_history.json
  (keyed by session id) with its start + end timestamps. Re-running recomputes each
  still-retained transcript (a completed transcript is immutable, so its numbers never
  change between runs — only the live current session grows) and PRESERVES any session
  whose transcript has been pruned by cleanupPeriodDays — so a session survives in the
  report even after it ages out. The per-session table is sorted ASCENDING by session
  start time (date + time), and the totals sum the whole ledger (so they no longer
  shrink when old transcripts age out).

Usage:
  python .templates/token_tally.py                  # run from the project root
  python .templates/token_tally.py --note "TEXT"    # also tag the CURRENT session

Notes are stored in tracks/00_insights/token_notes.json (keyed by session id) so
they SURVIVE re-tallies, and surface in the per-session table's Note column — a
light way to link spend to what was worked on. A second note on the same session
appends. Plain runs preserve existing notes.

Env:    CLAUDE_CONFIG_DIR overrides ~/.claude
"""
import os, re, sys, json, glob, datetime

FIELDS = ["output_tokens", "input_tokens",
          "cache_creation_input_tokens", "cache_read_input_tokens"]

INSIGHTS_DIR = os.path.join("tracks", "00_insights")
NOTES_REL = os.path.join(INSIGHTS_DIR, "token_notes.json")
HISTORY_REL = os.path.join(INSIGHTS_DIR, "token_history.json")

def transcript_dir(cwd):
    cfg = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")
    encoded = re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(cwd))
    return os.path.join(cfg, "projects", encoded)

def usage_of(obj):
    m = obj.get("message")
    u = m.get("usage") if isinstance(m, dict) else None
    if not isinstance(u, dict):
        u = obj.get("usage")
    return u if isinstance(u, dict) else None

def tally_file(path):
    sums = dict.fromkeys(FIELDS, 0)
    turns = 0
    ts = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            u = usage_of(obj)
            if u:
                turns += 1
                for k in FIELDS:
                    v = u.get(k, 0)
                    if isinstance(v, int):
                        sums[k] += v
            t = obj.get("timestamp")
            if isinstance(t, str):
                ts.append(t)
    return sums, turns, (min(ts) if ts else None), (max(ts) if ts else None)

def fmt(n):
    return f"{n:,}"

def dt(s):
    """ISO timestamp → 'YYYY-MM-DD HH:MM' (date + time, for sorting/display)."""
    return s.replace("T", " ")[:16] if s else "?"

def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
            return d if isinstance(d, dict) else {}
    except Exception:
        return {}

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

def parse_note_arg(argv):
    """--note "text"  or  --note=text  → the note string (None if absent)."""
    if "--note" in argv:
        i = argv.index("--note")
        return argv[i + 1] if i + 1 < len(argv) else ""
    for a in argv:
        if a.startswith("--note="):
            return a[len("--note="):]
    return None

def current_session(files):
    """The live/current session = the most-recently-modified transcript."""
    return max(files, key=os.path.getmtime) if files else None

def main():
    cwd = os.getcwd()
    tdir = transcript_dir(cwd)
    files = sorted(glob.glob(os.path.join(tdir, "*.jsonl")))
    cur_path = current_session(files)
    cur_key = os.path.basename(cur_path) if cur_path else None

    # --note mode: tag the current session first, then regenerate as usual.
    note = parse_note_arg(sys.argv[1:])
    notes = load_json(NOTES_REL)
    tagged = None
    if note:
        if cur_key:
            existing = (notes.get(cur_key) or "").strip()
            if not existing:
                notes[cur_key] = note
            elif note not in existing:
                notes[cur_key] = existing + " · " + note
            save_json(NOTES_REL, notes)
            tagged = cur_key[:8]
        else:
            print("token_tally: --note given but no transcripts found; nothing tagged.")

    # Freshly tally every RETAINED transcript (turns>0 only).
    fresh = {}
    for f in files:
        sums, turns, t0, t1 = tally_file(f)
        if turns == 0:
            continue
        fresh[os.path.basename(f)] = {"turns": turns, "t0": t0, "t1": t1,
                                      **{k: sums[k] for k in FIELDS}}

    # Append-only ledger: recompute every still-retained transcript (a completed one is
    # immutable, so its numbers are stable — re-tallying never changes a previous entry;
    # only the live session grows), and PRESERVE any session whose transcript was pruned.
    history = load_json(HISTORY_REL)
    run_stamp = datetime.datetime.now().isoformat(timespec="seconds")
    for key, data in fresh.items():
        first = (history.get(key) or {}).get("first_recorded") or run_stamp
        history[key] = {**data, "first_recorded": first, "last_tallied": run_stamp}
    # Sessions in the ledger but absent from `fresh` are pruned → left untouched (preserved).
    save_json(HISTORY_REL, history)

    # Build rows from the LEDGER (so pruned sessions persist), sorted by start time.
    rows = []  # (key, sid, entry, preserved)
    for key, entry in history.items():
        if entry.get("turns", 0) == 0:
            continue
        rows.append((key, key[:8], entry, key not in fresh))
    rows.sort(key=lambda r: (r[2].get("t0") or "9999"))

    total = dict.fromkeys(FIELDS, 0)
    total_turns = 0
    all_ts = []
    for _key, _sid, entry, _pres in rows:
        for k in FIELDS:
            total[k] += entry.get(k, 0)
        total_turns += entry.get("turns", 0)
        if entry.get("t0"):
            all_ts += [entry["t0"], entry["t1"]]

    n_preserved = sum(1 for r in rows if r[3])
    new_work = total["input_tokens"] + total["cache_creation_input_tokens"] + total["output_tokens"]
    grand = sum(total.values())
    earliest = min(all_ts)[:10] if all_ts else "?"
    latest = max(all_ts)[:10] if all_ts else "?"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    os.makedirs(INSIGHTS_DIR, exist_ok=True)
    out_path = os.path.join(INSIGHTS_DIR, "token_usage.md")

    L = []
    L.append("# Token usage — this project, all sessions\n")
    L.append(f"_Generated {now} by `/tokens`. Counts only; money conversion left to you "
             f"(per-token rates change). Source: `{tdir}`._\n")
    if not rows:
        L.append("\n**No session transcripts found for this project.** Either none exist yet, "
                 "or they live under a different `CLAUDE_CONFIG_DIR`.\n")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(L))
        print("token_tally: no transcripts found at", tdir)
        return

    L.append("\n## Totals (four token classes)\n")
    L.append("| class | tokens | billed (per-token API) |")
    L.append("|---|--:|---|")
    L.append(f"| output (generated) | {fmt(total['output_tokens'])} | output rate (highest) |")
    L.append(f"| input (uncached) | {fmt(total['input_tokens'])} | base input rate |")
    L.append(f"| cache-creation (writes) | {fmt(total['cache_creation_input_tokens'])} | input rate + premium |")
    L.append(f"| cache-read (reuse) | {fmt(total['cache_read_input_tokens'])} | input rate, deep discount |")
    L.append(f"| **new work** (in+create+out) | **{fmt(new_work)}** | the 'how much work' figure |")
    L.append(f"| **grand total** (incl. cache reads) | **{fmt(grand)}** | full throughput |")
    cov = f"\n**Coverage:** {len(rows)} sessions"
    if n_preserved:
        cov += f" ({n_preserved} preserved — transcript pruned)"
    cov += f" · {fmt(total_turns)} assistant turns · {earliest} → {latest}.\n"
    L.append(cov)
    L.append("> **Retention + the append-only ledger:** Claude Code prunes transcripts older "
             "than `cleanupPeriodDays` (default 30). This report is backed by an append-only "
             "ledger (`token_history.json`): once a session has been tallied it is **preserved "
             "here even after its transcript is pruned** (marked **†**), so totals and history "
             "don't shrink over time. The only gap is a session that aged out *before* `/tokens` "
             "ever ran while it was retained — so run `/tokens` at least once per retention "
             "window (or raise `cleanupPeriodDays` / archive the `*.jsonl`) to capture every one.\n")
    L.append("> Includes any subagents this project spawned (their usage is in these "
             "transcripts).\n")

    has_notes = any(notes.get(key) for key, *_ in rows)
    L.append("\n## Per session\n")
    L.append("> Sorted oldest → newest by session start time (transcript timestamps, **UTC**). "
             "A **†** marks a session preserved from the ledger (its transcript has been pruned; "
             "values are the last tally taken while it was still retained).\n")
    if has_notes:
        L.append("> _Note_ column: free-text labels added via `/tokens \"what I did\"` — what each "
                 "session worked on (best-effort; kept in `token_notes.json`, preserved across re-tallies).\n")
    L.append("| session | turns | output | input | cache-create | cache-read | started | ended | note |")
    L.append("|---|--:|--:|--:|--:|--:|---|---|---|")
    for key, sid, entry, preserved in rows:
        n = (notes.get(key) or "").replace("|", "\\|")
        mark = " †" if preserved else ""
        L.append(f"| {sid}{mark} | {entry.get('turns', 0)} | {fmt(entry.get('output_tokens', 0))} | "
                 f"{fmt(entry.get('input_tokens', 0))} | {fmt(entry.get('cache_creation_input_tokens', 0))} | "
                 f"{fmt(entry.get('cache_read_input_tokens', 0))} | "
                 f"{dt(entry.get('t0'))} | {dt(entry.get('t1'))} | {n} |")
    L.append("")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    if tagged:
        print(f"token_tally: tagged current session {tagged} with note: {note}")
    print(f"token_tally: {len(rows)} sessions ({n_preserved} preserved), {fmt(total_turns)} turns "
          f"({earliest}→{latest})")
    print(f"  new work (in+create+out): {fmt(new_work)}")
    print(f"  grand total (incl reads): {fmt(grand)}")
    print(f"  report -> {out_path}")

if __name__ == "__main__":
    main()
