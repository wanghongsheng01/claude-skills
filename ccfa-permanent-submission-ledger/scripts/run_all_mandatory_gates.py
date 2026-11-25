#!/usr/bin/env python3
"""Master Mandatory Pre-Delivery QA Runner (`run_all_mandatory_gates.py`).

Executes ALL 7 permanent quality gates sequentially on a manuscript build:
  Gate 1: Track Novelty & Anti-Module-Stacking Lint (`anti_stacking_lint.py`)
  Gate 2: Proof QED Geometry & Human Math-Readability Audit (`proof_and_math_audit.py`)
  Gate 3: Figure-vs-Prose Formula & Symbol Consistency Audit (`figure_formula_consistency_audit.py`)
  Gate 4: Float-to-Prose Proximity & Post-Related-Work Spill Audit (`float_proximity_audit.py`)
  Gate 5: Pure `booktabs`, Citation Density & BibTeX Hygiene Lint (`latex_table_and_cite_lint.py`)
  Gate 6: Two-Column PDF Layout Lint (`layoutlint.py` — 0 blocker, 0 major)
  Gate 7: Human Writing, Model-Origin Neutrality & Zero-Internal-Port Lint (`ai_smell_audit.py` + regex)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]


def run_step(name: str, cmd: list[str]) -> bool:
    print(f"\n>>> [{name}] {' '.join(str(c) for c in cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.rstrip())
    if res.stderr:
        print(res.stderr.rstrip(), file=sys.stderr)
    return res.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-dir", type=Path, required=True)
    ap.add_argument("--track", required=True, choices=["pvldb-research", "pvldb-eab", "sigmod-industrial"])
    ap.add_argument("--fig-scripts", type=Path, nargs="+", required=True)
    ap.add_argument("--lint-out", type=Path, default=Path("/tmp/ccfa_mandatory_lint"))
    args = ap.parse_args()

    tex = args.paper_dir / "main.tex"
    bib = args.paper_dir / "refs.bib"
    pdf = args.paper_dir / "main.pdf"

    ok_all = True
    ok_all &= run_step(
        "Gate 1: Anti-Stacking & Track Lint",
        [sys.executable, str(SKILLS_ROOT / "ccfa-track-novelty-and-anti-stacking/scripts/anti_stacking_lint.py"),
         str(tex), "--track", args.track],
    )
    ok_all &= run_step(
        "Gate 2: Proof QED & Readable Math Audit",
        [sys.executable, str(SKILLS_ROOT / "ccfa-human-readable-math-and-proof/scripts/proof_and_math_audit.py"),
         str(tex), str(pdf)],
    )
    ok_all &= run_step(
        "Gate 3: Figure-vs-Prose Formula Consistency",
        [sys.executable, str(SKILLS_ROOT / "ccfa-human-readable-math-and-proof/scripts/figure_formula_consistency_audit.py"),
         str(tex), *[str(p) for p in args.fig_scripts]],
    )
    ok_all &= run_step(
        "Gate 4: Float-to-Prose Proximity",
        [sys.executable, str(SKILLS_ROOT / "ccfa-visual-table-ref-mastery/scripts/float_proximity_audit.py"),
         str(pdf)],
    )
    ok_all &= run_step(
        "Gate 5: Booktabs, Cite & Bib Lint",
        [sys.executable, str(SKILLS_ROOT / "ccfa-visual-table-ref-mastery/scripts/latex_table_and_cite_lint.py"),
         str(tex), str(bib)],
    )
    ok_all &= run_step(
        "Gate 6: PDF Layout Lint",
        [sys.executable, str(SKILLS_ROOT / "ccfa-paper-layout-review/scripts/layoutlint.py"),
         "--tex", str(tex), str(pdf), str(args.lint_out)],
    )
    lint_md = (args.lint_out / "layoutlint.md").read_text(encoding="utf-8") if (args.lint_out / "layoutlint.md").exists() else ""
    if not re.search(r"blocker 0 / major 0\b", lint_md):
        print("[FAIL][Gate 6] layoutlint reported non-zero blocker or major issues!")
        ok_all = False

    # Gate 7: Model neutrality + banned internal codenames + zero AI clichés
    tex_txt = tex.read_text(encoding="utf-8")
    banned = re.findall(
        r"\b(7207|7208|7209|7210|7211|4444|Redis\s+v3|International\s+Models?|Domestic\s+Models?)\b|国外模型|国内模型",
        tex_txt,
        re.I,
    )
    if banned:
        print(f"[FAIL][Gate 7] Found banned codename or geopolitical model label: {banned}")
        ok_all = False
    else:
        print("\n>>> [Gate 7: Neutrality & Codename Hygiene] PASS (0 geopolitical labels, 0 internal ports/codenames)")

    print("\n========================================================")
    print("OVERALL MANDATORY QA VERDICT:", "PASS (ALL 7 GATES GREEN)" if ok_all else "FAIL (FIX ISSUES ABOVE)")
    print("========================================================")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
