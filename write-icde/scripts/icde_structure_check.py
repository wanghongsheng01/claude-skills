#!/usr/bin/env python3
"""Compare a LaTeX manuscript with the structure of accepted ICDE papers (observations from 21 deep-read papers and
1058 titles/abstracts of ICDE 2024-2027R1). Usage: python3 icde_structure_check.py FOLDER [--main main.tex]
Prints observations and WARN lines; the numbers are medians/ranges seen in accepted papers, not rules. Reads files only.
"""
import argparse, pathlib, re


def strip(s): return re.sub(r"(?<!\\)%.*", "", s)


def expand(root, name, seen=None):
    seen = seen or set()
    p = root / (name if name.endswith(".tex") else name + ".tex")
    if p in seen or not p.exists(): return ""
    seen.add(p)
    return re.sub(r"\\(?:input|include)\{([^}]+)\}", lambda m: expand(root, m.group(1), seen), strip(p.read_text(errors="ignore")))


def words(s):
    s = re.sub(r"\\begin\{(equation|align|algorithm|table|figure|lstlisting)\*?\}.*?\\end\{\1\*?\}", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " x ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    return len(re.findall(r"[A-Za-z][A-Za-z'-]*", s))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--main", default="main.tex")
    a = ap.parse_args(); root = pathlib.Path(a.folder); s = expand(root, a.main)
    w = lambda m: print("WARN ", m)
    o = lambda m: print("OBS  ", m)

    t = re.search(r"\\title\{(.+?)\}\s*\n", s, re.S); title = re.sub(r"\\[a-z]+|[{}]", "", t.group(1)) if t else ""
    n = len(title.split()); o(f"title {n} words (accepted median 9; 55% use a colon)")
    if n > 16: w("title longer than most accepted ICDE titles")

    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", s, re.S); na = words(ab.group(1)) if ab else 0
    o(f"abstract {na} words (median 203)");
    if ab and not re.search(r"\d", ab.group(1)): w("abstract states no number (accepted abstracts give 1-2 headline numbers)")

    secs = re.findall(r"\\section\{([^}]*)\}", s); o("sections: " + " | ".join(secs))
    low = [x.lower() for x in secs]
    if not low or "intro" not in low[0]: w("first section is not the Introduction")
    if not any(re.search(r"experiment|evaluation", x) for x in low): w("no Experiments/Evaluation section")
    if not any("related" in x for x in low): w("no Related Work section (needed to position against ICDE/VLDB/SIGMOD)")
    if not any(re.search(r"problem|prelim", x) for x in low): w("no Preliminaries/Problem section (accepted papers state the problem formally)")

    parts = re.split(r"\\section\{", s)
    body = {p.split("}", 1)[0].lower(): p for p in parts[1:]}
    intro = next((v for k, v in body.items() if "intro" in k), "")
    items = 0
    m = re.search(r"\\begin\{(itemize|enumerate)\}(.*?)\\end\{\1\}", intro, re.S)
    if m: items = len(re.findall(r"\\item", m.group(2)))
    o(f"contribution items in the introduction: {items} (3 most common, 3-6 seen)")
    if not re.search(r"\\ref\{fig:", intro): w("introduction cites no figure (Figure 1 showing the gap is near-universal)")
    if not re.search(r"C1|Challenge", intro): w("no numbered challenges in the introduction (3 challenges <-> 3 components is the common frame)")

    exp = next((v for k, v in body.items() if re.search(r"experiment|evaluation", k)), "")
    tot = words(s); o(f"body words ~{tot}; experiments {100 * words(exp) / max(tot, 1):.0f}% of words (25-55% seen)")
    cnt = {k: len(re.findall(r"\\begin\{" + k, s)) for k in ["theorem", "lemma", "definition", "figure", "table"]}
    o("theorems %(theorem)d, lemmas %(lemma)d, definitions %(definition)d" % cnt)
    o("figures %(figure)d, tables %(table)d (5-24 figures, 2-10 tables seen)" % cnt)
    if not re.search(r"Takeaway|\\textbf\{(Finding|Observation|Lesson|Summary)", exp): w("experiments have no takeaway sentences (common in 2026-2027 papers)")

    bib = "".join(p.read_text(errors="ignore") for p in root.glob("*.bib"))
    nb = len(re.findall(r"^@\w+\{", bib, re.M)); core = len(re.findall(r"VLDB|SIGMOD|Manag\.? Data|ICDE|Data Engineering", bib))
    o(f"bib entries {nb} (56-85 seen), mentions of core DB venues {core}")
    if nb < 40: w("fewer references than accepted ICDE papers")
    if not re.search(r"AI-Generated|Generative AI|AI-generated", s): w("no AI-generated content acknowledgment (ICDE 2026+ papers carry one)")
    hedges = len(re.findall(r"\b(might|may possibly|somewhat|arguably|it seems)\b", s, re.I))
    o(f"hedging phrases: {hedges}")

    # Self-negation (references/limitations-writing.md): 0/10 accepted cohesive-subgraph papers state a loss in the
    # abstract or conclusion, none has a "where we fail" heading, and none uses the phrases below for its own method.
    NEG = re.compile(r"does not help|do not help|cannot help|not help\b|vanish\w*|\bfails?\b|\bonly\s+\$?\d[\d.,]*(--[\d.,]+)?\$?\s*\\?\$?\\times"
                     r"|\bonly\s+[\d.]+(--[\d.]+)?\s*(\$\\times\$|x)|is slower than|are slower than|worse than|not (as )?(fast|good)", re.I)
    def neg(txt):
        return [m.group(0) for m in NEG.finditer(txt)]
    concl = next((v for k, v in body.items() if "conclu" in k), "")
    for name, txt in (("abstract", ab.group(1) if ab else ""), ("introduction", intro), ("conclusion", concl)):
        hits = neg(txt)
        if hits:
            w(f"self-negating wording in the {name}: {hits[:6]} - state scope as a qualifier of the positive claim, "
              "keep losses in the experiment that measures them (limitations-writing.md R1-R3, R11)")
    for h in re.findall(r"\\textbf\{([^}]*)\}|\\(?:sub)*section\{([^}]*)\}", s):
        h = " ".join(h)
        if re.search(r"not help|fail|limitation|weakness|drawback|does not", h, re.I):
            w(f"heading or run-in label announces a failure: '{h.strip()}' - use a regime/trade-off title such as 'When does X pay off?'")
    allneg = neg(s)
    o(f"self-negating phrases in the whole paper: {len(allneg)} (accepted papers: each negative result once, 1-4 sentences)")
    if len(allneg) > 8:
        w("negative results appear to be repeated across sections; state each once, where its number is shown")


if __name__ == "__main__":
    main()
