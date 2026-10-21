#!/usr/bin/env python3
"""Register and AI-flavor check for a LaTeX paper aimed at Information Systems.

Usage: python3 is_style_check.py main.tex [more.tex ...] [--codes 'P19|DKE|v[0-9]+']

Reports sentence length, share of long sentences, parentheses, semicolons,
negation/contrast devices, em dashes, AI-tell words and internal codes,
for the whole text and per \\section. Read-only.
"""
import re
import sys

TARGETS = {"meanlen": (20, 26), "long": (0.10, 0.20), "paren": (0.0, 1.8), "semi": (0.0, 0.5)}

AI_WORDS = [r"delve\w*", r"crucial(?:ly)?", r"notably", r"importantly", r"it is worth not\w+",
            r"landscape", r"underscore[sd]?", r"pivotal", r"seamless(?:ly)?", r"comprehensive",
            r"robust(?:ly|ness)?", r"nuanced?", r"sheds? light", r"paves? the way", r"in the realm of",
            r"testament", r"leverag\w+", r"holistic", r"intricate", r"multifaceted",
            r"meticulous(?:ly)?", r"tapestry", r"unlock\w*", r"empower\w*", r"elevat\w+", r"foster\w*",
            r"streamlin\w+", r"it should be emphasi[sz]ed", r"we deliberately", r"needless to say"]
CONTRAST = [r"\bnot\b[^.]{0,80}\bbut\b", r"\brather than\b", r"\binstead of\b", r"\bdoes not\b",
            r"\bdo not\b", r"\bcannot\b", r"\bnot\b"]


def clean(s):
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\begin\{(equation|align|table|figure|tabular|thebibliography)\*?\}.*?\\end\{\1\*?\}", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", "X", s)
    s = re.sub(r"\\(cite[pt]?|ref|eqref|label|url|includegraphics)(\[[^\]]*\])?\{[^}]*\}", "R", s)
    s = re.sub(r"\\(emph|textbf|textit|texttt)\{([^}]*)\}", r"\2", s)
    return s


def stats(name, t):
    flat = re.sub(r"\s+", " ", t)
    flat = re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", " ", flat)
    sents = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", flat) if len(x.split()) > 3]
    if not sents:
        return
    L = [len(x.split()) for x in sents]
    words = max(1, len(flat.split()))
    paren = flat.count("(") * 100 / words
    semi = flat.count(";") * 100 / words
    neg = sum(len(re.findall(p, flat, re.I)) for p in CONTRAST[:3]) * 100 / words
    nots = len(re.findall(r"\bnot\b|n't\b|\bcannot\b|\bneither\b|\bnor\b", flat, re.I)) * 100 / words
    dash = t.count("---") + flat.count("\u2014")
    mean = sum(L) / len(L)
    long_ = sum(l > 35 for l in L) / len(L)
    flag = lambda v, k: "" if TARGETS[k][0] <= v <= TARGETS[k][1] else " <-"
    print(f"{name[:38]:38s} words={words:6d} sents={len(L):4d} mean={mean:5.1f}{flag(mean,'meanlen')} "
          f">35w={long_:4.0%}{flag(long_,'long')} paren/100w={paren:4.2f}{flag(paren,'paren')} "
          f"semi/100w={semi:4.2f}{flag(semi,'semi')} contrast/100w={neg:4.2f} negation/100w={nots:4.2f} emdash={dash}")


def main():
    args = sys.argv[1:]
    codes = None
    if "--codes" in args:
        i = args.index("--codes"); codes = args[i + 1]; del args[i:i + 2]
    raw = "".join(open(f, errors="ignore").read() for f in args)
    t = clean(raw)
    body = t.split("\\begin{document}")[-1]
    print("Targets: mean 20-26 words, 10-20% >35 words, parentheses <=1.8 and semicolons <=0.5 per 100 words\n")
    stats("WHOLE TEXT", body)
    parts = re.split(r"\\section\*?\{([^}]*)\}", body)
    for k in range(1, len(parts) - 1, 2):
        stats("  " + parts[k], parts[k + 1])
    print("\nAI-tell words:")
    hits = 0
    for w in AI_WORDS:
        for m in re.finditer(r"\b" + w + r"\b", body, re.I):
            hits += 1
            ctx = re.sub(r"\s+", " ", body[max(0, m.start() - 50):m.end() + 50])
            print(f"  {m.group(0)!r}: ...{ctx}...")
    print(f"  total {hits}")
    if codes:
        print("\nInternal codes / previous-journal traces:")
        for i, line in enumerate(raw.splitlines(), 1):
            if re.search(codes, line):
                print(f"  line {i}: {line.strip()[:100]}")
    heads = re.findall(r"\\(?:sub)*section\*?\{([^}]*)\}", raw)
    bad = [h for h in heads if "(" in h]
    if bad:
        print("\nParentheses in headings:", bad)


if __name__ == "__main__":
    main()
