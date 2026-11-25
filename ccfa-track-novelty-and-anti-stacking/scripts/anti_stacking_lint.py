#!/usr/bin/env python3
"""Anti-Module-Stacking & Track-Calibration Linter (`anti_stacking_lint.py`).

Audits a LaTeX manuscript (`main.tex`) for "Frankenstein / engineering bag-of-tricks"
signals in the Abstract, Introduction, and Method overview:
  1. Explicit numbered component/guarantee laundry lists in Abstract
     (e.g., "five deterministic database operators:", "six modules:", "four formal guarantees").
  2. Semicolon-chained enumerations (>= 4 semicolons in a single Abstract sentence).
  3. Contribution-bullet bloat (> 4 bullets in Section 1).
  4. Missing orthogonality / non-stacking explanation in the Evaluation ablation section.
"""

import argparse
import re
import sys
from pathlib import Path

STACKING_PATTERNS = [
    (
        r"\b(four|five|six|seven|eight|4|5|6|7|8)\s+"
        r"(deterministic\s+)?(database\s+)?(operators|modules|components|stages|filters|heuristics)\s*:",
        "Numbered operator/module laundry-list colon in Abstract/Intro (triggers 'module-stacking' critique)",
    ),
    (
        r"\bestablish\s+(four|five|six|seven|4|5|6|7)\s+(formal\s+)?(guarantees|theorems)\b",
        "Counted 'establish N formal guarantees' phrasing (frame as a unified theoretical spine instead)",
    ),
]


def extract_env(tex: str, env: str) -> str:
    m = re.search(rf"\\begin\{{{env}\}}(.*?)\\end\{{{env}\}}", tex, re.S)
    return m.group(1) if m else ""


def extract_intro(tex: str) -> str:
    m = re.search(r"\\section\{Introduction\}(.*?)(?=\\section\{)", tex, re.S | re.I)
    return m.group(1) if m else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", type=Path)
    ap.add_argument("--track", default="pvldb-research",
                    choices=["pvldb-research", "pvldb-eab", "sigmod-industrial"])
    args = ap.parse_args()

    tex = args.tex.read_text(encoding="utf-8")
    abstract = extract_env(tex, "abstract")
    intro = extract_intro(tex)

    fails = []
    warns = []

    # 1. Check Abstract & Intro for numbered stacking phrases
    for pat, msg in STACKING_PATTERNS:
        if re.search(pat, abstract, re.I):
            fails.append(f"[FAIL][Abstract] {msg}")
        if args.track == "pvldb-research" and re.search(pat, intro, re.I):
            fails.append(f"[FAIL][Intro] {msg}")

    # 2. Check semicolon laundry lists in Abstract (>= 4 semicolons in Abstract)
    semi_count = abstract.count(";")
    if semi_count >= 4:
        fails.append(
            f"[FAIL][Abstract] Contains {semi_count} semicolons (laundry-list enumeration of modules; max 2 allowed)."
        )

    # 3. Check contribution bullets count (3-4 is optimal)
    contrib_blocks = re.findall(r"\\begin\{(itemize|enumerate)\}(.*?)\\end\{\1\}", intro, re.S)
    if contrib_blocks:
        last_items = len(re.findall(r"\\item\b", contrib_blocks[-1][1]))
        if last_items > 4:
            fails.append(f"[FAIL][Intro] Contribution list has {last_items} bullets (keep to 3-4 cohesive bullets).")

    # 4. For PVLDB Research, check that Evaluation explicitly addresses orthogonality / non-stacking
    if args.track == "pvldb-research":
        if not re.search(r"\borthogon(al|ality)\b", tex, re.I):
            warns.append("[WARN][Eval] Missing explicit 'orthogonal / orthogonality' factor attribution in ablations.")

    print(f"=== Anti-Stacking & Track-Calibration Lint ({args.track}): {args.tex.name} ===")
    for f in fails:
        print(" ", f)
    for w in warns:
        print(" ", w)
    print(f"Summary: {len(fails)} FAIL(s), {len(warns)} WARN(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
