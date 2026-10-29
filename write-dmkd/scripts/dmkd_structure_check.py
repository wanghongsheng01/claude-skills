#!/usr/bin/env python3
"""Structure and register check of a LaTeX manuscript against observed DMKD conventions.

Usage: python3 dmkd_structure_check.py main.tex

Compares the manuscript with the medians of 30 published DMKD papers (see
references/observed-papers.md). Prints observations; it never edits files.
"""
import re
import sys

AI_WORDS = [r"delve\w*", r"crucial(?:ly)?", r"notably", r"importantly", r"landscape", r"underscore[sd]?",
            r"pivotal", r"seamless(?:ly)?", r"nuanced?", r"sheds? light", r"paves? the way", r"in the realm of",
            r"testament", r"leverag\w+", r"holistic", r"intricate", r"multifaceted", r"meticulous(?:ly)?",
            r"tapestry", r"unlock\w*", r"empower\w*", r"foster\w*", r"streamlin\w+"]


def braced(s, start):
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i]
    return ""


def arg(tex, name):
    m = re.search(r"\\" + name + r"\s*(\[[^\]]*\])?\s*\{", tex)
    return braced(tex, m.end() - 1) if m else ""


def plain(s):
    s = re.sub(r"\$[^$]*\$", "X", s)
    s = re.sub(r"\\(cite[pt]?|ref|label|url|includegraphics)(\[[^\]]*\])?\{[^}]*\}", "R", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    return re.sub(r"[{}~]", " ", s)


def line(label, value, note=""):
    print(f"{label:34s} {value}{('   ' + note) if note else ''}")


def main():
    raw = open(sys.argv[1], errors="ignore").read()
    tex = re.sub(r"(?<!\\)%.*", "", raw)
    body = tex.split("\\maketitle")[-1]
    main_body = re.split(r"\\backmatter|\\begin\{appendices\}|\\appendix", body)[0]

    title = re.sub(r"\s+", " ", arg(tex, "title"))
    tw = len(plain(title).split())
    line("Title words", tw, "DMKD median 10; 20/30 use a colon" + ("" if ":" in title else "  <- no colon"))
    ab = plain(arg(tex, "abstract"))
    line("Abstract words", len(ab.split()), "limit 150-250; evaluation-paper median 232")
    kw = [k for k in arg(tex, "keywords").split(",") if k.strip()]
    line("Keywords", len(kw), "limit 4-6; include an evaluation term for evaluation papers")

    intro = re.split(r"\\section\{", main_body)
    intro = intro[1] if len(intro) > 1 else ""
    rqs = sorted(set(re.findall(r"RQ\s?\d", intro)))
    line("Research questions in intro", ", ".join(rqs) or "none", "criterion (iii); 6/20 evaluation papers list RQs")
    answers = len(re.findall(r"answer to RQ\s?\d", main_body, re.I))
    line("'The answer to RQk' sentences", answers)
    line("Contribution list", "yes" if re.search(r"contribution", intro, re.I) and "\\item" in intro else "no",
         "16/28 papers")
    line("Roadmap paragraph", "yes" if re.search(r"Section~?\\ref|rest of (the|this) paper", intro) else "no",
         "21/28 papers")

    secs = re.findall(r"\\section\{([^}]*)\}", main_body)
    line("Top-level sections", len(secs), "median 7; " + " | ".join(s[:28] for s in secs))
    nfig = len(re.findall(r"\\begin\{figure", tex))
    ntab = len(re.findall(r"\\begin\{table", tex))
    line("Figures / tables", f"{nfig} / {ntab}", "medians 13.5 / 6")
    items = re.findall(r"\\bibitem", tex)
    bibs = re.split(r"\\bibitem", tex)[1:]
    n = len(items)
    dmkd = sum(bool(re.search(r"Data Min(ing)? (and )?Knowl(edge)? Disc", b)) for b in bibs)
    kdd = sum(bool(re.search(r"\bKDD\b|SIGKDD|Knowledge Discovery and Data Mining", b)) for b in bibs)
    jmlr = sum(bool(re.search(r"J Mach Learn Res|JMLR", b)) for b in bibs)
    line("References", n, "median 65; evaluation papers 83")
    line("  DMKD / KDD / JMLR references", f"{dmkd} / {kdd} / {jmlr}", "23/30 cite DMKD; 27/30 cite KDD")
    bare = len(re.findall(r"\\cite\{", tex))
    line("Bare \\cite{} (use citep/citet)", bare)
    stats_terms = re.findall(r"Wilcoxon|Friedman|Nemenyi|Holm|critical difference|effect size|significance test|binomial|bootstrap|DeLong|confidence interval",
                             main_body, re.I)
    line("Statistics vocabulary", len(stats_terms), "13/28 use formal tests; otherwise justify their absence")
    line("Threats to validity / limitations", "yes" if re.search(r"threats to validity|limitation", main_body, re.I)
         else "no")

    flat = re.sub(r"\s+", " ", plain(re.sub(r"\\begin\{(table|figure|equation|tabular)\*?\}.*?\\end\{\1\*?\}", " ",
                                            main_body, flags=re.S)))
    sents = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", flat) if len(s.split()) > 3]
    L = [len(s.split()) for s in sents] or [0]
    words = len(flat.split())
    line("Body words (main text)", words, "evaluation papers about 11k-22k")
    line("Mean sentence length", f"{sum(L) / len(L):.1f}", "aim 18-26")
    line("Sentences > 35 words", f"{sum(l > 35 for l in L) / len(L):.0%}", "aim <= 20%")
    line("Parentheses per 100 words", f"{flat.count('(') * 100 / max(words, 1):.2f}", "aim <= 1.8")
    hits = [m.group(0) for w in AI_WORDS for m in re.finditer(r"\b" + w + r"\b", flat, re.I)]
    line("AI-tell words", len(hits), ", ".join(sorted(set(hits)))[:120])


if __name__ == "__main__":
    main()
