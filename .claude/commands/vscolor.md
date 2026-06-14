---
description: Set this project's VS Code window color (local-only, for telling windows apart)
argument-hint: [color name | "next" | blank = auto from folder name]
---

Set a per-project VS Code window color so two projects open side by side are visually distinct. Input: $ARGUMENTS

**Resolve the color:**
- Blank → derive *deterministically* from the project folder's basename. **Use this exact, model-reproducible rule** (so the same name always lands on the same color across machines and sessions — no library, no model-chosen hash): lowercase the basename, sum the UTF-8 byte values of its characters, take `sum mod 8`, and index into the **palette below in listed order** (0 = red, 1 = orange, 2 = yellow, 3 = green, 4 = teal, 5 = blue, 6 = purple, 7 = gray). Zero input needed.
- A palette name → use it.
- `next` → advance to the next palette entry (collision escape hatch).

**Palette** (each: a strong background + readable foreground):

| name | bg | fg |
|---|---|---|
| red | `#5f1e1e` | `#ffd6d6` |
| orange | `#5f3a1e` | `#ffe4c4` |
| yellow | `#5f561e` | `#fff4c4` |
| green | `#1e5f2e` | `#c8f7d4` |
| teal | `#1e5f5a` | `#c4f4f0` |
| blue | `#1e3a5f` | `#cfe2ff` |
| purple | `#3a1e5f` | `#e4d6ff` |
| gray | `#3a3a3a` | `#dddddd` |

**Apply:** edit `.vscode/settings.json`, creating `.vscode/` and the file if absent (it is gitignored — a fresh clone won't have it; `/vscolor` regenerates it, so gitignoring loses nothing) — **merge, do not overwrite**. Touch only the `workbench.colorCustomizations` block; preserve every other setting. Set, at minimum, `titleBar.activeBackground/activeForeground/inactiveBackground`, `activityBar.background/foreground`, and `statusBar.background/foreground` to the chosen color (activityBar + statusBar always render on Linux even when the title bar is native). Applies live — no reload needed. Report which color was set.
