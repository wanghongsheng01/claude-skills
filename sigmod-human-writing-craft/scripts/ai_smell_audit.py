#!/usr/bin/env python3
"""Quantitative AI-Smell & Human-Prose Audit Tool calibrated against 5 published human SIGMOD Ind. papers."""
import re, sys, statistics

AI_TICS = [
    (r'\bcrucially\b', 'crucially'),
    (r'\bnotably\b', 'notably'),
    (r'\bimportantly\b', 'importantly'),
    (r'\bmoreover\b', 'moreover'),
    (r'\bfurthermore\b', 'furthermore'),
    (r'\bmerit emphasis\b', 'merit emphasis'),
    (r'\bexposes?\b', 'expose(s)'),
    (r'\bbridges?\b', 'bridge(s)'),
    (r'\bcleanly\b', 'cleanly'),
    (r'\bstrictly\b', 'strictly'),
    (r'\bunconditionally\b', 'unconditionally'),
    (r'\bdelivers?\b', 'deliver(s)'),
    (r'\bquantif(?:y|ies)\b', 'quantify/ies'),
    (r'\bgeneralizable\b', 'generalizable'),
    (r'\btransferable\b', 'transferable'),
    (r'\bdelineat(?:e|es|ing)\b', 'delineate'),
    (r'\bdistill(?:s|ing)?\b', 'distill'),
    (r'\bspotlights?\b', 'spotlight'),
    (r'\bleverag(?:e|es|ing)\b', 'leverage'),
    (r'\bholistic\b', 'holistic'),
    (r'\bcomprehensive\b', 'comprehensive'),
    (r'\bseamless(?:ly)?\b', 'seamless(ly)'),
    (r'\bdramatically\b', 'dramatically'),
    (r'\bnovel\b', 'novel'),
    (r'\btakeaway\s*\(rq', 'Takeaway(RQ)'),
    (r'reviewers?\s+rightly\s+ask', 'META:reviewers-rightly-ask'),
    (r'following\s+this\s+[a-z\-]+\s+discipline', 'CLICHE:following-discipline'),
]

def strip_latex(tex: str) -> str:
    # Remove comments, preamble, algorithms, tables, bibliography
    tex = re.sub(r'(?m)^%.*$', '', tex)
    m = re.search(r'\\begin\{document\}', tex)
    if m: tex = tex[m.end():]
    m2 = re.search(r'\\bibliographystyle', tex)
    if m2: tex = tex[:m2.start()]
    for env in ('algorithm', 'tabular', 'CCSXML', 'quote'):
        tex = re.sub(rf'\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}', ' ', tex, flags=re.S)
    tex = re.sub(r'\\(?:cite|ref|label|includegraphics|caption|code|texttt|textbf|emph|textsc)\*?\[?[^\]]*\]?\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?', ' ', tex)
    tex = re.sub(r'[{}~]', ' ', tex)
    return re.sub(r'\s+', ' ', tex).strip()

def audit(path: str):
    raw = open(path, encoding='utf-8').read()
    lines = raw.splitlines()
    plain = strip_latex(raw)
    words = re.findall(r"[A-Za-z][A-Za-z0-9'-]*", plain)
    n_words = max(len(words), 1)
    em_dashes = len(re.findall(r'---|—', raw))
    bold_colons = len(re.findall(r'\\textbf\{[^}]+:\}', raw))
    takeaways = len(re.findall(r'Takeaway\s*\(RQ', raw, re.I))
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', plain) if 5 <= len(s.split()) <= 80]
    slens = [len(s.split()) for s in sents] or [20]

    print(f"=== AI-Smell & Human Prose Audit: {path} ===")
    print(f"Prose words: {n_words} | Sentences: {len(slens)} | Mean len: {statistics.mean(slens):.1f}w (SD={statistics.stdev(slens):.1f})")
    print(f"Em-dashes (---): {em_dashes} ({em_dashes/n_words*1000:.2f}/1K)  [Human SIGMOD target <= 1.2/1K]")
    print(f"Bold-colon lead-ins (\\textbf{{X:}}): {bold_colons} ({bold_colons/n_words*1000:.2f}/1K)")
    print(f"Mechanical Takeaway(RQ) stamps: {takeaways}  [Human SIGMOD target = 0]")

    total_tics = 0
    print("\n--- Flagged AI Tics & Line Numbers ---")
    for pat, label in AI_TICS:
        hits = []
        for idx, l in enumerate(lines, 1):
            if l.lstrip().startswith('%'): continue
            if re.search(pat, l, re.I):
                hits.append(idx)
        if hits:
            total_tics += len(hits)
            print(f"  {label:28s}: {len(hits):2d}x at lines {hits}")
    print(f"\nTOTAL AI-TIC RATE: {total_tics} ({total_tics/n_words*1000:.2f} / 1K words)  [Target <= 1.0/1K]")

if __name__ == '__main__':
    audit(sys.argv[1])
