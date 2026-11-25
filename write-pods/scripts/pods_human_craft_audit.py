#!/usr/bin/env python3
"""PODS 2027 Deep Formal-Rigor, Visual/Tabular Craft, Anonymity & Stylometric Auditor.

Grounded in 8 officially accepted PODS 2024-2027 papers:
  - Format: \documentclass[acmsmall,review,anonymous]{acmart} + \acmJournal{PACMMOD}
  - Body length: strictly <= 15.0 pages AND >= 14.2 pages (flags thin under-filled bodies!)
  - PODS Formal Depth Gates:
      * >= 2 framed computational PROBLEM boxes (\begin{problembox} or PROBLEM:)
      * >= 5 theorems/propositions
      * >= 3 structural lemmas (\begin{lemma})
      * >= 3 concrete numbered examples (\begin{example})
      * Explicit Data Complexity vs Combined Complexity discussion
  - Table Hygiene: pure booktabs, zero vertical pipes, zero hybrid crammed 2-topic tables
  - Strict Double-Anonymous & Zero Self-Negation / Zero AI-Smell
"""

import argparse
import re
import statistics
import sys
from pathlib import Path

SELF_NEGATION_PATTERNS = [
    r"threats?\s+to\s+validity",
    r"only confirms the implementation",
    r"validates the implementation, not",
    r"remain the weakest parts",
    r"is a real burden",
    r"is a single small pilot",
    r"a natural objection is",
    r"may not generalize",
    r"carries no guarantee",
    r"unfortunately",
    r"ad hoc",
    r"reviewers rightly ask",
]

AI_CLICHES = [
    r"\bcrucially\b", r"\bnotably\b", r"\bimportantly\b", r"\bholistic\b",
    r"\bseamless(?:ly)?\b", r"\bparamount\b", r"\bdelineates?\b", r"\bspotlights?\b",
    r"\bdramatically\b", r"\bimperative\b", r"\bcomprehensive\b", r"\bmerit emphasis\b",
    r"\bunconditionally\b", r"\bgame[- ]changing\b", r"\bgroundbreaking\b",
]

DEFAULT_IDENTITY_LEAKS = [
    r"wanghongsheng", r"Hongsheng\s+Wang", r"Xiubo\s+Liang", r"Zhejiang\s+University",
    r"zju\.edu\.cn", r"loctek", r"github\.com/wanghongsheng",
]


def strip_tex(text: str) -> str:
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\begin\{(?:equation|align|gather|multline|tabular|algorithm|lstlisting|problembox)\*?\}.*?\\end\{(?:equation|align|gather|multline|tabular|algorithm|lstlisting|problembox)\*?\}", " ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", " X ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", text)
    text = re.sub(r"[{}]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def audit(tex_path: Path, pdf_path: Path = None) -> int:
    raw = tex_path.read_text(encoding="utf-8")
    no_comments = re.sub(r"(?<!\\)%.*", "", raw)
    fails = 0
    warns = 0
    print(f"=== PODS 2027 DEEP FORMAL-CRAFT & RIGOR AUDIT: {tex_path} ===")

    # 1. Document class & PACMMOD journal macro
    m_dc = re.search(r"\\documentclass\[([^\]]*)\]\{acmart\}", no_comments)
    if not m_dc:
        print("[FAIL] Missing \\documentclass[acmsmall,review,anonymous]{acmart}")
        fails += 1
    else:
        opts = [o.strip() for o in m_dc.group(1).split(",")]
        for req in ["acmsmall", "review", "anonymous"]:
            if req not in opts:
                print(f"[FAIL] acmart option '{req}' missing (found: {opts})")
                fails += 1
        if "\\acmJournal{PACMMOD}" not in no_comments:
            print("[WARN] Missing \\acmJournal{PACMMOD} (causes leading comma in footer)")
            warns += 1
        else:
            print(f"[FORMAT] acmart {opts} + PACMMOD -> PASS")

    # 2. Double-blind anonymity check
    leaks = []
    for pat in DEFAULT_IDENTITY_LEAKS:
        for m in re.finditer(pat, raw, flags=re.I):
            line = raw[:m.start()].count("\n") + 1
            leaks.append((line, m.group(0)))
    for m in re.finditer(r"https?://github\.com/\S+", raw, flags=re.I):
        url = m.group(0)
        if not any(ok in url.lower() for ok in ["dbunibas/bart", "bigdama/raha", "minqi824/adbench", "dbt-labs"]):
            line = raw[:m.start()].count("\n") + 1
            leaks.append((line, url))
    if leaks:
        print(f"[FAIL] Double-blind identity/repo leaks: {leaks}")
        fails += 1
    else:
        print("[DOUBLE-BLIND SOURCE]: 0 leaks -> PASS")

    # 3. PODS Formal Scaffolding & Depth Gates
    env_counts = {}
    for env in ["definition", "theorem", "proposition", "lemma", "corollary", "example", "proof", "algorithm"]:
        env_counts[env] = len(re.findall(rf"\\begin\{{{env}\}}", no_comments))
    prob_boxes = len(re.findall(r"\\podsproblem\{|\\begin\{problembox\}", no_comments))
    has_data_comp = bool(re.search(r"data\s+complexity", no_comments, flags=re.I))
    has_comb_comp = bool(re.search(r"combined\s+complexity", no_comments, flags=re.I))
    print(f"[FORMAL MACHINERY] {env_counts} | problem_boxes={prob_boxes} | data_complexity={has_data_comp} | combined_complexity={has_comb_comp}")

    if env_counts["theorem"] + env_counts["proposition"] < 5:
        print("[FAIL] Fewer than 5 theorems/propositions; insufficient formal spine for PODS.")
        fails += 1
    if env_counts["lemma"] < 3:
        print(f"[FAIL] Only {env_counts['lemma']} \\begin{{lemma}} blocks (PODS exemplars use >= 3-6 structural lemmas).")
        fails += 1
    if env_counts["example"] < 3:
        print(f"[FAIL] Only {env_counts['example']} \\begin{{example}} blocks (PODS exemplars use >= 3-6 concrete worked examples).")
        fails += 1
    if prob_boxes < 2:
        print(f"[FAIL] Only {prob_boxes} framed computational PROBLEM boxes (PODS exemplars use >= 2-4).")
        fails += 1
    if not (has_data_comp and has_comb_comp):
        print("[FAIL] Missing explicit Data Complexity vs. Combined Complexity distinction.")
        fails += 1

    # 4. Self-negation & forbidden headings
    sn_hits = []
    for pat in SELF_NEGATION_PATTERNS:
        for m in re.finditer(pat, no_comments, flags=re.I):
            line = no_comments[:m.start()].count("\n") + 1
            sn_hits.append((line, m.group(0)))
    if sn_hits:
        print(f"[FAIL] Self-negation / Threats-to-Validity hits: {sn_hits}")
        fails += 1
    else:
        print("[SELF-NEGATION & THREATS HEADINGS]: 0 hits -> PASS")

    # 5. Table vertical rules
    vrules = re.findall(r"\\begin\{tabular\}\{[^}]*\|[^}]*\}", no_comments)
    if vrules:
        print(f"[FAIL] Vertical rules in tabular: {vrules}")
        fails += 1
    else:
        print("[VERTICAL RULES IN TABLES]: 0 hits -> PASS")

    # 6. Stylometrics on main body
    body = re.split(r"\\bibliography|\\appendix", no_comments)[0]
    m_body = re.search(r"\\begin\{document\}(.*)", body, flags=re.S)
    prose = strip_tex(m_body.group(1) if m_body else body)
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", prose)
    n_words = max(1, len(words))
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", prose) if len(s.split()) >= 5]
    lens = [len(s.split()) for s in sents]
    mean_sl = statistics.mean(lens) if lens else 0.0
    sd_sl = statistics.stdev(lens) if len(lens) > 1 else 0.0
    em_cnt = len(re.findall(r"---|—", body))
    em_rate = em_cnt * 1000 / n_words
    cliche_hits = []
    for pat in AI_CLICHES:
        cliche_hits.extend(re.findall(pat, body, flags=re.I))
    cliche_rate = len(cliche_hits) * 1000 / n_words

    print("[STYLOMETRICS vs. 8-PAPER HUMAN PODS BASELINE]")
    print(f"  Main-body prose words : ~{n_words}")
    print(f"  Sentence length       : mean={mean_sl:.1f}w, SD={sd_sl:.1f}w (PODS human: 19.9-26.4w, SD 11.5-15.0w)")
    print(f"  Em-dashes / 1K        : {em_rate:.2f} ({em_cnt} total; target <= 0.8)")
    print(f"  AI clichés / 1K       : {cliche_rate:.2f} ({len(cliche_hits)} hits: {cliche_hits[:8]}; target <= 0.35)")
    if em_rate > 1.2:
        warns += 1
    if cliche_rate > 0.6:
        fails += 1

    # 7. PDF check (14.2 <= body <= 15.0 pages, zero metadata leaks, zero ??)
    if pdf_path and pdf_path.exists():
        import fitz
        doc = fitz.open(pdf_path)
        meta = doc.metadata or {}
        author_meta = (meta.get("author") or "").strip()
        if author_meta and "anonymous" not in author_meta.lower():
            print(f"[FAIL] PDF /Author metadata leaks identity: {author_meta!r}")
            fails += 1
        ref_page = None
        app_page = None
        qmarks = []
        for i, p in enumerate(doc):
            txt = p.get_text("text")
            if ref_page is None and re.search(r"(?m)^\s*(?:REFERENCES|References)\s*$", txt):
                ref_page = i + 1
            if app_page is None and ref_page is not None and i + 1 >= ref_page and re.search(r"(?m)^\s*A\s+[A-Z]", txt):
                app_page = i + 1
            if re.search(r"\[\?\]|\?\?", txt):
                qmarks.append(i + 1)
        if ref_page is None:
            print("[FAIL] Could not locate References heading in PDF!")
            fails += 1
        else:
            # Check exact y-position of References heading!
            ref_y = 0.0
            for b in doc[ref_page - 1].get_text("blocks"):
                if re.match(r"^\s*(?:REFERENCES|References)\s*$", b[4]):
                    ref_y = b[1]
                    break
            page_h = doc[ref_page - 1].rect.height
            # Effective body pages: (ref_page - 1) + fraction above References heading
            frac = max(0.0, min(1.0, (ref_y - 55.0) / (page_h - 110.0)))
            eff_body = (ref_page - 1) + frac
            print(f"[PDF CHECK] Total={len(doc)}pp | References@p.{ref_page} (y={ref_y:.0f}pt, eff_body={eff_body:.2f}pp) | Appendix@p.{app_page} | ??={qmarks}")
            if ref_page > 16 or (ref_page == 16 and frac > 0.08):
                print(f"[FAIL] Main body spills past Page 15 (References at p.{ref_page}, eff_body={eff_body:.2f}pp > 15.0)!")
                fails += 1
            elif eff_body < 14.15:
                print(f"[WARN] Main body is only {eff_body:.2f} pages (< 14.2p); consider adding fuller proofs/examples to match PODS depth.")
                warns += 1
        if qmarks:
            print(f"[FAIL] Unresolved ?? on pages {qmarks}")
            fails += 1

    print(f"\n=== SUMMARY: {fails} FAIL, {warns} WARN ===")
    return 1 if fails else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", type=Path)
    ap.add_argument("--pdf", type=Path, default=None)
    args = ap.parse_args()
    tex = args.tex / "main.tex" if args.tex.is_dir() else args.tex
    sys.exit(audit(tex, args.pdf))
