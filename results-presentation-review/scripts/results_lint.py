#!/usr/bin/env python3
"""Results-presentation lint for a LaTeX paper: what a senior co-author or PC member notices in the experiments
section within two minutes (rules S01-S10 of ../SKILL.md). Static checks on the .tex sources, the figure scripts
and the figure PDFs; it never edits anything.

Usage:
  python3 results_lint.py <paper_dir> --method Ladder [--figscripts code/make_figs.py ...] [--figs figs/*.pdf]
    S01 caption too long (tables > 40 words, figures > 60 words): compress the header, move protocol to the text
    S02 caption does not open with the takeaway (first sentence states no claim)
    S03 results table without winner marks (bold best AND underline second best)
    S04 marked results table without a Best/2nd (or Cheapest/2nd, Wins) count row
    S05 one column printed with different numbers of decimals
    S06 ablation / relative-change table without a visible summary row (mean or geo. mean, separated by a rule)
    S07 our method loses rows to a baseline, but no sentence says why (baseline name + because/when/since/...)
    S08 jittered strip plot with a mean bar in a figure script: check skew, prefer a box plot or median + IQR
    S09 scatter panel with a large empty band between point clusters: explain it, or split/zoom the panels
    S10 experiments text without a takeaway per RQ, or without a where-it-wins / where-it-loses paragraph
    S11 descriptive table (dataset statistics) that shows nothing about the method: a constant or near-constant column,
        or a caption that never says which statistic matters for the method (AuthZ-Graph, second author, 11-11)
Exit code 1 if any WARN is found. --method is the name used in the table header (\\textsc{Ladder} -> Ladder).
"""
import argparse, glob, os, re, sys

WARN, INFO = "WARN", "INFO"
CLAIM = re.compile(r"\b(is|are|stays?|remains?|costs?|beats?|reach(es)?|holds?|never|always|outperforms?|saves?|"
                   r"cheapest|fastest|best|lowest|highest|wins?|dominates?|matches|grows?|drops?|falls?|keeps?|"
                   r"improves?|reduces?|cuts?|matters?|helps?|pays? off|hurts?)\b", re.I)
EXPLAIN = re.compile(r"\b(because|since|due to|the reason|this is why|as a result|when|whenever|whereas|explains?|"
                     r"caused by|owing to|which makes|so that)\b", re.I)
RESULTY = re.compile(r"cost|time|latency|runtime|accuracy|f1|error|throughput|speed|recall|precision|coverage|"
                     r"memory|usd|\$|saving|qps|ndcg|mrr|auc", re.I)
ABLATION = re.compile(r"\bablation|relative to (the )?full|\bw/o\b|removes? one component", re.I)
SUMMARY_ROW = re.compile(r"^\s*(\\[a-z]+\s*)*(\{)?\s*(avg|average|mean|geo\.?\s*mean|geometric mean|overall|all|total|"
                         r"median|summary)\b", re.I)
COUNT_ROW = re.compile(r"best\s*/\s*2nd|cheapest\s*/\s*2nd|1st\s*/\s*2nd|wins?|#\s*best|ranks?", re.I)


def strip_tex(s):
    s = re.sub(r"\\(textbf|underline|emph|textsc|textit|mathrm|text)\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\$([^$]*)\$", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    return re.sub(r"[{}~]", " ", s)


def braced(s, i):
    """Return the content of the {...} group starting at s[i] == '{' and the index after it."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{": depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0: return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def read_tex(root):
    files = {}
    main = os.path.join(root, "main.tex")
    for f in sorted(glob.glob(os.path.join(root, "**", "*.tex"), recursive=True)):
        files[os.path.relpath(f, root)] = open(f, errors="ignore").read()
    return files


def resolve_inputs(text, root, seen=None):
    seen = seen or set()
    def rep(m):
        p = m.group(1); p = p if p.endswith(".tex") else p + ".tex"
        f = os.path.join(root, p)
        if f in seen or not os.path.exists(f): return ""
        seen.add(f)
        return resolve_inputs(open(f, errors="ignore").read(), root, seen)
    return re.sub(r"\\input\{([^}]+)\}", rep, text)


def floats(text):
    """Yield (kind, caption, body) for every table/figure environment."""
    for m in re.finditer(r"\\begin\{(table|figure)\*?\}(.*?)\\end\{\1\*?\}", text, re.S):
        body = m.group(2)
        c = body.find("\\caption{")
        cap = braced(body, c + len("\\caption"))[0] if c >= 0 else ""
        yield m.group(1), cap, body


def first_sentence(cap):
    t = re.sub(r"\s+", " ", strip_tex(cap)).strip()
    return re.split(r"(?<=[.;:])\s", t, 1)[0]


def table_rows(body):
    tab = re.search(r"\\begin\{tabular\*?\}(\{[^}]*\})?(\{[^}]*\})(.*?)\\end\{tabular\*?\}", body, re.S)
    if not tab: return [], []
    rows = [r.strip() for r in re.split(r"\\\\", tab.group(3))]
    rows = [re.sub(r"\\(toprule|midrule|bottomrule|hline|cline\{[^}]*\})", "", r).strip() for r in rows]
    rows = [r for r in rows if r and "&" in r]
    if not rows: return [], []
    header = [strip_tex(c).strip() for c in rows[0].split("&")]
    return header, [r.split("&") for r in rows[1:]]


NUM = re.compile(r"^[+\-−]?\$?-?\$?\s*(\d[\d,{}]*)(\.(\d+))?\s*(\\%|%|\$?\\times\$?|×|x)?$")


def decimals(cell):
    c = re.sub(r"\\(textbf|underline)\{([^{}]*)\}", r"\2", cell).strip()
    c = c.replace("$-$", "-").replace("\\,", "").replace("{,}", ",").replace("\\$", "").strip()
    m = NUM.match(c)
    if not m or "/" in c: return None
    return len(m.group(3)) if m.group(3) else 0


MACROS = {}


def expand_macros(s, macros):
    """Expand zero-argument \\newcommand macros (e.g. \\sys -> FLIX) so that captions written with them are read."""
    for _ in range(3):
        s = re.sub(r"\\([A-Za-z]+)\b", lambda m: macros.get(m.group(1), m.group(0)), s)
    return s


def check_tables(text, method, out):
    tables = [(cap, body) for kind, cap, body in floats(text) if kind == "table"]
    beaten_by = {}
    for cap, body in tables:
        label = (re.search(r"\\label\{([^}]+)\}", body) or re.search(r"\\label\{([^}]+)\}", cap) or [None, "?"])[1] \
            if re.search(r"\\label\{", body + cap) else "?"
        words = len(strip_tex(cap).split())
        if words > 40:
            out.append((WARN, "S01", label, f"table caption has {words} words: keep the claim and what is measured "
                                            "(<= 40 words); move protocol details to the setup text"))
        elif words > 30:
            out.append((INFO, "S01", label, f"table caption has {words} words: aim for about two printed lines "
                                            "(<= 30 words); define only the abbreviations a reader cannot guess"))
        fs = first_sentence(cap)
        if fs and not CLAIM.search(fs):
            out.append((WARN, "S02", label, f"caption opens without a claim: '{fs[:70]}...'"))
        header, rows = table_rows(body)
        if not rows: continue
        # S05 decimals per column
        for j in range(max(len(r) for r in rows)):
            ds = {decimals(r[j]) for r in rows if j < len(r)} - {None}
            if len(ds) > 1:
                name = header[j] if j < len(header) else f"column {j + 1}"
                out.append((WARN, "S05", label, f"column '{name}' mixes {sorted(ds)} decimals: one precision per metric"))
        # S11 descriptive tables: constant columns, and a caption that says what the table shows about the method
        data = [r for r in rows if not SUMMARY_ROW.search(strip_tex(r[0])) and not COUNT_ROW.search(strip_tex(r[0]))
                and "multicolumn" not in "&".join(r)]
        # only descriptive tables: in a results table (our method as a column or a row, or winner marks) a constant
        # column is a finding (e.g. 0/0 = always exact), not a defect
        rowtxt = " ".join(strip_tex(expand_macros(r[0], MACROS)).lower() for r in rows)
        ours_any = bool(method) and (any(method.lower() in strip_tex(expand_macros(h, MACROS)).lower() for h in header[1:])
                                     or method.lower() in rowtxt)
        is_results = ours_any or "\\textbf" in body or "\\underline" in body
        for j in range(1, len(header) if not is_results else 1):
            vals = [re.sub(r"\\(textbf|underline)\{([^{}]*)\}", r"\2", r[j]).strip() for r in data if j < len(r)]
            vals = [v for v in vals if v not in ("", "--", "-", "n/a")]
            if len(vals) >= 5:
                top = max(set(vals), key=vals.count)
                if vals.count(top) == len(vals):
                    out.append((WARN, "S11", label, f"column '{header[j]}' is {top} in every row: state it once in the "
                                                    "setup text and drop the column"))
                elif vals.count(top) == len(vals) - 1 and len(vals) >= 8:
                    out.append((INFO, "S11", label, f"column '{header[j]}' is {top} in all rows but one: state the value "
                                                    "and the exception in the text and drop the column"))
        descriptive = bool(method) and not any(method.lower() in h.lower() for h in header[1:]) and \
            re.search(r"dataset|graph|statistic|benchmark", cap, re.I) and not RESULTY.search(cap)
        if descriptive and method.lower() not in strip_tex(expand_macros(cap, MACROS)).lower():
            out.append((INFO, "S11", label, "descriptive table never names the method: say in the caption which "
                                            "column matters for it (the statistic it exploits), or trim the table"))
        # S03/S04 winner marks on results tables
        # a comparison table has our method as one of its columns (descriptive and summary tables are exempt)
        ours = bool(method) and any(method.lower() in h.lower() for h in header[1:])
        resulty = ours and RESULTY.search(cap) and len(header) >= 3 and not ABLATION.search(cap)
        bold, under = "\\textbf" in body, "\\underline" in body
        if resulty and not (bold and under):
            out.append((WARN, "S03", label, "results table without " + ("underline for the second best" if bold else
                        "bold best and underlined second best") + " (rank by the printed value; ties share the mark)"))
        if resulty and bold and not any(COUNT_ROW.search(strip_tex(r[0])) for r in rows):
            out.append((INFO, "S04", label, "no Best/2nd count row: add one per method so the standing is visible"))
        # S06 ablation summary row
        relchg = sum(1 for r in rows for c in r if re.search(r"[+−-]\s*\d+(\.\d+)?\s*\\?%", c)) >= 4
        if ABLATION.search(cap) or relchg:
            idx = [i for i, r in enumerate(rows) if SUMMARY_ROW.search(strip_tex(r[0]))]
            if not idx:
                out.append((WARN, "S06", label, "ablation/relative-change table without a mean (or geo. mean) row: add it, "
                                                "with the share of rows that improve, so the effect of each component is visible"))
            else:
                tab = re.search(r"\\begin\{tabular.*?\\end\{tabular", body, re.S).group(0)
                last = rows[idx[-1]][0].strip()
                k = tab.find(last)
                if k > 0 and "\\midrule" not in tab[max(0, k - 40):k]:
                    out.append((INFO, "S06", label, "summary row is not set off by a \\midrule; separate it and name it in the "
                                                    "caption ('last row: geometric mean')"))
        # S07 who beats our method
        if method and bold:
            col = [j for j, h in enumerate(header) if method.lower() in h.lower()]
            if col:
                j = col[0]
                for r in rows:
                    if j < len(r) and "\\textbf" not in r[j]:
                        win = [k for k, c in enumerate(r) if "\\textbf" in c and k != j]
                        for k in win:
                            if k < len(header) and header[k].strip(): beaten_by.setdefault(header[k].strip(), set()).add(label)
    return beaten_by


def check_text(text, method, beaten_by, out):
    exp = text
    m = re.search(r"\\section\{Experiments?[^}]*\}", text) or re.search(r"\\section\{[^}]*(Evaluation|Experiment)[^}]*\}", text)
    if m:
        nxt = re.search(r"\\section\{", text[m.end():])
        exp = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]
    plain = re.sub(r"\s+", " ", strip_tex(exp))
    sents = re.split(r"(?<=[.!?])\s+", plain)
    for base, labels in sorted(beaten_by.items()):
        if not base.split(): continue
        b = re.escape(base.split()[0].rstrip("."))  # header abbreviations ("Strat-shr.") match the full name as a prefix
        if not any(re.search(b, s, re.I) and EXPLAIN.search(s) for s in sents):
            out.append((WARN, "S07", ",".join(sorted(labels)), f"'{base}' beats {method or 'our method'} in some rows, but no "
                        "sentence explains why or when (name the baseline with because/when/since)"))
    rqs = len(re.findall(r"\\subsection\{RQ", exp)) or len(re.findall(r"\\subsection\{", exp))
    take = len(re.findall(r"Takeaway|Lesson|In summary|\\takeaway\{", exp))   # also the \takeaway{...} macro that prints "Takeaway."
    if rqs and take < rqs - 1:
        out.append((WARN, "S10", "experiments", f"{take} takeaways for {rqs} result subsections: close each RQ with one"))
    if not re.search(r"(when|where) (does|do|is) .{0,40}(win|lose|help|pay|cheaper|faster|better)|"
                     r"falls? behind|second (cheapest|best)|loses? to|is (slightly )?(more expensive|slower|worse) than",
                     plain, re.I):
        out.append((WARN, "S10", "experiments", "no where-it-wins / where-it-loses discussion: add one paragraph naming "
                                                "the scenarios in which a baseline is better, and the mechanism"))


def check_scripts(scripts, out):
    for f in scripts:
        s = open(f, errors="ignore").read()
        if re.search(r"normal\([^)]*,\s*0\.\d+", s) and re.search(r"np\.mean\(|\.mean\(\)", s) and re.search(r"ax\.plot\(\[", s):
            out.append((WARN, "S08", os.path.basename(f), "jittered strip plot with a mean bar: a skewed set (a few low "
                        "points) pulls the mean below the visual mass; check the data, then draw a box plot or median + IQR"))


def check_figs(figs, out):
    try:
        import fitz
    except ImportError:
        out.append((INFO, "S09", "-", "PyMuPDF missing: figure band check skipped (pip install pymupdf)")); return
    for f in figs:
        p = fitz.open(f)[0]
        dr = [x for x in p.get_drawings() if x.get("fill") is not None]
        panes = [x["rect"] for x in dr if min(x["fill"]) > 0.97 and x["rect"].width > 40 and x["rect"].height > 25]
        marks = [x["rect"] for x in dr if min(x["fill"]) <= 0.97 and 1 < x["rect"].width < 12 and 1 < x["rect"].height < 12]
        words = [w for w in p.get_text("words") if re.fullmatch(r"[\d.,\-−×%$^]+", w[4])]
        for pane in panes:
            # a plot panel has numeric tick labels next to it; diagrams (nodes drawn as dots) do not
            near = fitz.Rect(pane.x0 - 30, pane.y0 - 5, pane.x1 + 5, pane.y1 + 25)
            if sum(1 for w in words if near.intersects(fitz.Rect(w[:4]))) < 3: continue
            ys = sorted((m.y0 + m.y1) / 2 for m in marks if pane.contains(fitz.Point((m.x0 + m.x1) / 2, (m.y0 + m.y1) / 2)))
            if len(ys) < 6: continue
            gaps = [(ys[i + 1] - ys[i], i) for i in range(len(ys) - 1)]
            g, i = max(gaps)
            if g > 0.35 * pane.height and min(i + 1, len(ys) - i - 1) >= 2:
                out.append((WARN, "S09", os.path.basename(f), f"panel with {len(ys)} points has an empty band of "
                            f"{100 * g / pane.height:.0f}% of its height between two clusters: say in the caption/text what "
                            "separates them, or split/zoom the panels"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper"); ap.add_argument("--method", default="")
    ap.add_argument("--figscripts", nargs="*", default=[]); ap.add_argument("--figs", nargs="*")
    a = ap.parse_args()
    main_tex = os.path.join(a.paper, "main.tex")
    text = resolve_inputs(open(main_tex, errors="ignore").read(), a.paper) if os.path.exists(main_tex) else \
        "\n".join(read_tex(a.paper).values())
    text = re.sub(r"(?<!\\)%.*", "", text)
    out = []
    for m in re.finditer(r"\\(?:re)?newcommand\*?\{?\\([A-Za-z]+)\}?\s*\{((?:[^{}]|\{[^{}]*\})*)\}", text):
        MACROS[m.group(1)] = re.sub(r"\\xspace", "", m.group(2))
    beaten = check_tables(text, a.method, out)
    check_text(text, a.method, beaten, out)
    check_scripts(a.figscripts, out)
    figs = a.figs if a.figs is not None else sorted(glob.glob(os.path.join(a.paper, "figs", "*.pdf")))
    used = set(re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text))
    figs = [f for f in figs if not used or any(os.path.basename(u).split(".")[0] == os.path.basename(f).split(".")[0] for u in used)]
    check_figs(figs, out)
    for lev, rule, where, msg in out:
        print(f"{lev:5} {rule}  {where}: {msg}")
    nw = sum(1 for o in out if o[0] == WARN)
    print(f"\n{nw} warnings, {len(out) - nw} notes")
    sys.exit(1 if nw else 0)


if __name__ == "__main__":
    main()
