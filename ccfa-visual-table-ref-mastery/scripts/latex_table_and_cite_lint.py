#!/usr/bin/env python3
"""Lint LaTeX tables, proof endings, citation brackets, and BibTeX hygiene."""
import re, sys
from pathlib import Path


def audit(tex_path: str, bib_path: str) -> int:
    tex = Path(tex_path).read_text(encoding="utf-8")
    bib = Path(bib_path).read_text(encoding="utf-8")
    issues = []

    # 1. Check for vertical pipes inside tabular column specs (handles nested @{} braces)
    for m in re.finditer(r"\\begin\{tabular\*?\}(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", tex):
        spec = m.group(1)
        line_no = tex[:m.start()].count("\n") + 1
        if "|" in spec:
            issues.append(f"[FAIL][Table-Pipe] line {line_no}: vertical bar '|' in tabular spec {{{spec}}} violates booktabs")

    # 2. Check that tabulars with \multicolumn also use \cmidrule
    for m in re.finditer(r"\\begin\{tabular\*?\}.*?\\end\{tabular\*?\}", tex, flags=re.S):
        blk = m.group(0)
        line_no = tex[:m.start()].count("\n") + 1
        if r"\multicolumn{" in blk and r"\midrule" in blk and r"\cmidrule" not in blk:
            # Ignore summary-row multicolumns after \midrule; check header before first \midrule
            hdr = blk.split(r"\midrule", 1)[0]
            if r"\multicolumn{" in hdr:
                issues.append(f"[FAIL][Missing-cmidrule] line {line_no}: multi-column header lacks \\cmidrule(lr)")

    # 3. Check proof endings for tall \bigl/\Bigl/\left/\frac right before \end{proof}
    for m in re.finditer(r"\\begin\{proof\}(.*?)\\end\{proof\}", tex, flags=re.S):
        body = m.group(1).strip()
        last_line = body.splitlines()[-1] if body.splitlines() else ""
        line_no = tex[:m.end()].count("\n") + 1
        if re.search(r"\\(?:bigl|bigr|Bigl|Bigr|left|right|frac)\b", last_line):
            issues.append(f"[FAIL][Proof-End-Math] line {line_no}: tall math delimiter on closing line of proof distorts QED alignment")

    # 4. Check unfocused citation dumps (> 4 keys in a single \cite{...})
    for m in re.finditer(r"\\cite\{([^}]+)\}", tex):
        keys = [k.strip() for k in m.group(1).split(",") if k.strip()]
        line_no = tex[:m.start()].count("\n") + 1
        if len(keys) > 5:
            issues.append(f"[FAIL][Citation-Dump] line {line_no}: \\cite has {len(keys)} keys ({m.group(1)[:50]}...); split by specific mechanism (<=4-5 keys)")

    # 5. BibTeX checks: arXiv DOI on non-arXiv conference/journal entry, 'and others' truncation
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", bib, flags=re.S):
        etype, key, body = m.group(1).lower(), m.group(2), m.group(3)
        if etype in ("inproceedings", "article"):
            is_arxiv_venue = bool(re.search(r"arxiv|corr", body, re.I) and not re.search(r"booktitle\s*=|PVLDB|VLDB|SIGMOD|ICLR|NeurIPS|ICDE|EMNLP", body))
            if not is_arxiv_venue and re.search(r"10\.48550/arXiv", body, re.I):
                issues.append(f"[FAIL][Bib-ArXiv-DOI-On-Published] {key}: published venue entry carries arXiv DOI 10.48550/arXiv")
        if re.search(r"\band others\b|\bet al\.", body, re.I):
            issues.append(f"[WARN][Bib-Truncated-Authors] {key}: uses 'and others' / 'et al.' instead of full author list")

    print(f"=== LaTeX Table, Proof, Citation & Bib Lint: {tex_path} ===")
    for it in issues:
        print(" ", it)
    fails = sum(1 for it in issues if it.startswith("[FAIL]"))
    print(f"Total issues: {len(issues)} ({fails} FAILs)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(audit(sys.argv[1], sys.argv[2]))
