#!/usr/bin/env python3
"""Compare a LaTeX manuscript with the observed shape of published ESWA papers.

  python3 eswa_style_check.py manuscript.tex [--bib references.bib] [--year 2026]

Reports INFO/WARN lines (never edits). Targets come from write-eswa/SKILL.md:
intro ~550-1550 words with contribution list and roadmap, related-work section,
method overview figure, complexity/cost subsection, limitations, practical guidelines,
50-65 references with >=55% from the last five years and a few ESWA references.
"""
import argparse
import pathlib
import re
import statistics

AI_TELLS = r"\b(delve|crucial(ly)?|pivotal|seamless(ly)?|leverag(e|es|ing)|groundbreaking|revolutioni[sz]e|" \
           r"cutting-edge|state-of-the-art|novel|paradigm shift|in today's|ever-evolving|landscape|" \
           r"underscore[sd]?|showcase[sd]?|holistic|robust(ly)? (and|yet)|furthermore,|moreover,)\b"


def strip(tex):
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    return tex


def plain(s):
    s = re.sub(r"\$[^$]*\$", " X ", s)
    s = re.sub(r"\\(cite[pt]?|ref|eqref|label|res|stat|dif)\*?(\{[^}]*\})+", " X ", s)
    s = re.sub(r"\\begin\{(table|figure|algorithm)\*?\}.*?\\end\{\1\*?\}", " ", s, flags=re.S)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}~]", " ", s)
    return s


def sections(tex):
    parts = re.split(r"\\section\*?\{((?:[^{}]|\{[^{}]*\})*)\}", tex)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def say(level, msg):
    print(f"{level:4s} {msg}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--bib")
    ap.add_argument("--year", type=int, default=2026)
    a = ap.parse_args()
    tex = strip(pathlib.Path(a.tex).read_text(errors="ignore"))
    secs = sections(tex)
    names = [n for n, _ in secs]
    say("INFO", "sections: " + " | ".join(names))

    intro = next((b for n, b in secs if n.lower().startswith("introduction")), "")
    iw = len(plain(intro).split())
    say("OK" if 550 <= iw <= 1550 else "WARN", f"introduction ~{iw} words (ESWA median ~960, range 536-1540)")
    say("OK" if re.search(r"contributions? (of this (paper|work|study) )?(are|is)|main contributions", intro, re.I)
        and re.search(r"\\begin\{(enumerate|itemize)\}", intro) else "WARN", "contribution list in the introduction")
    say("OK" if re.search(r"remainder of (this|the) paper|rest of (this|the) paper|organi[sz]ed as follows", intro, re.I)
        else "WARN", "roadmap paragraph at the end of the introduction")
    say("OK" if re.search(r"\bRQ\d|research questions?", tex) else "INFO", "research questions stated")
    for label, pat in [("related-work section", r"related work|literature review|background"),
                       ("problem formulation", r"problem|preliminar|formulation"),
                       ("experimental setup section", r"experiment|evaluation"),
                       ("discussion / implications", r"discussion|implication|guideline"),
                       ("conclusion", r"conclusion")]:
        say("OK" if any(re.search(pat, n, re.I) for n in names) else "WARN", label)
    subs = re.findall(r"\\subsection\*?\{((?:[^{}]|\{[^{}]*\})*)\}", tex)
    say("OK" if any(re.search(r"limitation", s, re.I) for s in subs + names) else "WARN", "explicit Limitations (sub)section")
    say("OK" if any(re.search(r"complexit|computational|cost|runtime|efficien", s, re.I) for s in subs) else "WARN",
        "complexity / computational cost subsection (24% of ESWA full texts mention complexity)")
    say("OK" if any(re.search(r"guideline|practical|implication|deploy", s, re.I) for s in subs + names) else "WARN",
        "practical guidelines / implications (ESWA aims ask for practical guidelines)")
    say("OK" if re.search(r"ablation", tex, re.I) else "WARN", "ablation study")
    say("OK" if re.search(r"sensitiv", tex, re.I) else "WARN", "sensitivity analysis")
    say("OK" if re.search(r"significan|confidence interval|p-value|Wilcoxon|t-test", tex, re.I) else "WARN",
        "statistical significance of the main comparison")

    nfig = len(re.findall(r"\\begin\{figure\*?\}", tex))
    ntab = len(re.findall(r"\\begin\{table\*?\}", tex))
    say("INFO", f"{nfig} figures, {ntab} tables (ESWA medians 6 and 9; ranges 3-14 and 1-18)")
    first_fig = re.search(r"\\begin\{figure\*?\}(.*?)\\end\{figure", tex, re.S)
    if first_fig and not re.search(r"overview|pipeline|framework|architecture|workflow", first_fig.group(1), re.I):
        say("WARN", "first figure is not an overview/pipeline figure (6/10 ESWA papers open the method with one)")

    body = plain(re.split(r"\\bibliography\{|\\begin\{thebibliography\}", tex)[0])
    sents = [s for s in re.split(r"(?<=[.!?])\s+", body) if len(s.split()) > 3]
    if sents:
        lens = [len(s.split()) for s in sents]
        say("INFO", f"body ~{len(body.split())} words; mean sentence {statistics.mean(lens):.1f} words; "
                    f"{sum(l > 40 for l in lens)} sentences over 40 words")
    tells = re.findall(AI_TELLS, body, re.I)
    if tells:
        say("WARN", f"{len(tells)} AI-tell/hype words: " + ", ".join(sorted(set(t[0].lower() for t in tells)))[:200])
    if re.search(r"et al\.(~|\s)\\cite\{", tex):
        say("WARN", "'et al. \\cite' pattern: use \\citet in author-year style")

    if a.bib:
        bib = pathlib.Path(a.bib).read_text(errors="ignore")
        cited = set(k.strip() for g in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}", tex) for k in g.split(","))
        entries = dict(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", bib, re.S))
        used = [entries[k] for k in cited if k in entries]
        years = [int(m.group(1)) for e in used for m in [re.search(r"year\s*=\s*\{?(\d{4})", e)] if m]
        recent = sum(y >= a.year - 4 for y in years) / max(1, len(years))
        eswa = sum(bool(re.search(r"Expert Systems with Applications|j\.eswa", e)) for e in used)
        say("OK" if 45 <= len(used) <= 80 else "WARN", f"{len(used)} cited references (ESWA median 50; LLM papers 57)")
        say("OK" if recent >= 0.5 else "WARN", f"{recent:.0%} of cited references from {a.year - 4}-{a.year} (ESWA median 57%; LLM 64%)")
        say("OK" if 2 <= eswa <= 12 else "WARN", f"{eswa} ESWA references (median ~2; 3-6 relevant ones signal fit)")


if __name__ == "__main__":
    main()
