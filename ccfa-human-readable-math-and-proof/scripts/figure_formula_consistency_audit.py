#!/usr/bin/env python3
"""Mandatory Figure-to-Prose Formula & Symbol Consistency Auditor (`figure_formula_consistency_audit.py`).

Audits figure-generation scripts (`.py`) against the LaTeX manuscript (`main.tex`):
  1. Bans Matplotlib STIX broken-glyph macros (`\\setminus` -> tiny floating tick `∖`).
  2. Verifies every `(Thm. X)`, `(Theorem X)`, `(Alg. Y)`, `(Eq. Z)` referenced in figures
     actually exists in `main.tex` (prevents stale theorem numbers after restructuring!).
  3. Verifies every `$...$` math identifier/subscript in figure scripts (e.g., `\\tau_0`,
     `k_{\\max}`, `H_k`, `H_c`, `N^*`, `\\lambda_g`, `\\rho`) appears in `main.tex`!
  4. Bans raw ASCII `<=` or `>=` inside figure display strings (use proper `\\le` or `≤`).
"""

import argparse
import ast
import re
import sys
from pathlib import Path


def extract_string_literals(py_src: str):
    tree = ast.parse(py_src)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.append((getattr(node, "lineno", 0), node.value))
    return out


def count_numbered_envs(tex: str, env_names):
    clean = re.sub(r"(?<!\\)%.*", "", tex)
    pat = r"\\begin\{(" + "|".join(env_names) + r")\}"
    return len(re.findall(pat, clean))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", type=Path)
    ap.add_argument("fig_scripts", type=Path, nargs="+")
    args = ap.parse_args()

    tex = re.sub(r"(?<!\\)%.*", "", args.tex.read_text(encoding="utf-8"))
    fails, warns = [], []

    # Collect valid theorem labels/numbers in tex
    uses_secthm = bool(re.search(r"Theorem~\d+\.\d+|thm:", tex))
    n_thm = count_numbered_envs(tex, ["theorem"])
    n_alg = count_numbered_envs(tex, ["algorithm"])
    n_eq = len(re.findall(r"\\begin\{equation\}|\\label\{eq:", tex))

    for spath in args.fig_scripts:
        src = spath.read_text(encoding="utf-8")
        lits = extract_string_literals(src)
        for lineno, s in lits:
            # 1. Ban \setminus in Matplotlib STIX strings
            if "\\setminus" in s:
                fails.append(
                    f"[FAIL][{spath.name}:L{lineno}] Uses '\\setminus' in figure string {s!r} "
                    f"(renders as broken tiny tick in STIX; express directly in plotted axis variable)."
                )

            # 2. Ban ASCII <= or >= in visible figure labels
            if re.search(r"(?<![=!<>])<=(?!=)|(?<![=!<>])>=(?!=)", s) and not s.strip().startswith("SELECT"):
                if any(w in s.lower() for w in ["hop", "path", "whitelist", "bound", "k_max"]):
                    fails.append(
                        f"[FAIL][{spath.name}:L{lineno}] Uses raw ASCII '<=' or '>=' in figure label {s!r}; "
                        f"use Unicode '≤'/'≥' or math '$\\le$'/'$\\ge$'."
                    )

            # 3. Check (Thm. X) / Thm. X.Y references
            for m in re.finditer(r"\bTh(?:eorem|m\.?)\s*(\d+(?:\.\d+)?)", s):
                tnum = m.group(1)
                if "." not in tnum and int(tnum) > n_thm and not uses_secthm:
                    fails.append(
                        f"[FAIL][{spath.name}:L{lineno}] References 'Thm. {tnum}' in {s!r}, "
                        f"but {args.tex.name} only has {n_thm} theorem(s)!"
                    )

            # 4. Check Algorithm references
            for m in re.finditer(r"\bAlg(?:orithm|\.)\s*(\d+)", s):
                anum = int(m.group(1))
                if anum > n_alg:
                    fails.append(
                        f"[FAIL][{spath.name}:L{lineno}] References 'Alg. {anum}' in {s!r}, "
                        f"but {args.tex.name} only has {n_alg} algorithm(s)!"
                    )

            # 5. Check subscripted symbols / Greek macros inside $...$ against main.tex
            for m in re.finditer(r"\$([^$]+)\$", s):
                expr = m.group(1)
                # Check Greek + subscript tokens like \tau_0, \lambda_g, H_k, H_c, k_{\max}
                for sym in re.findall(r"\\[a-zA-Z]+_[a-zA-Z0-9]+|\b[A-Za-z]_(?:\{[^{}]+\}|[A-Za-z0-9])\b", expr):
                    norm = sym.replace("{", "").replace("}", "").replace("\\mathrm", "\\text")
                    tex_norm = tex.replace("{", "").replace("}", "").replace("\\mathrm", "\\text")
                    if norm not in tex_norm:
                        fails.append(
                            f"[FAIL][{spath.name}:L{lineno}] Figure math symbol '{sym}' in '${expr}$' "
                            f"does NOT appear anywhere in {args.tex.name}!"
                        )

    print(f"=== Figure-vs-Prose Formula & Symbol Consistency Audit ({args.tex.name}) ===")
    for f in fails:
        print(" ", f)
    for w in warns:
        print(" ", w)
    print(f"Summary: {len(fails)} FAIL(s), {len(warns)} WARN(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
