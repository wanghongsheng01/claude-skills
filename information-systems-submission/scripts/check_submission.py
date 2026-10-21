#!/usr/bin/env python3
"""Pre-submission checks for an Information Systems (Elsevier) LaTeX manuscript.

Usage:
  python3 check_submission.py FOLDER [--main main.tex] [--highlights highlights.txt]
                              [--forbid REGEX] [--abstract-limit 250] [--max-keywords 7]

Prints ERROR / WARN / OK lines and exits 1 if any ERROR is found.
It reads files only; it never edits them.
"""
import argparse
import pathlib
import re
import sys

AI_HEADING = ("Declaration of generative AI and AI-assisted technologies "
              "in the manuscript preparation process")

problems = {"ERROR": 0, "WARN": 0}


def report(level, msg):
    if level in problems:
        problems[level] += 1
    print(f"{level:5s} {msg}")


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def words(s):
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}$~]", " ", s)
    return [w for w in s.split() if re.search(r"[A-Za-z0-9]", w)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--highlights", default=None)
    ap.add_argument("--forbid", default=None,
                    help="regex of strings that must not appear, e.g. old journal names or project codes")
    ap.add_argument("--abstract-limit", type=int, default=250)
    ap.add_argument("--max-keywords", type=int, default=7)
    a = ap.parse_args()

    folder = pathlib.Path(a.folder)
    tex_path = folder / a.main
    if not tex_path.exists():
        report("ERROR", f"main file not found: {tex_path}")
        sys.exit(1)
    raw = tex_path.read_text(errors="ignore")
    tex = strip_comments(raw)

    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]*)\}", tex)
    if not m or m.group(2) != "elsarticle":
        report("ERROR", "documentclass is not elsarticle")
    else:
        report("OK", f"elsarticle with options {m.group(1) or '[]'}")

    j = re.search(r"\\journal\{([^}]*)\}", tex)
    if not j:
        report("ERROR", "no \\journal{...} line")
    elif j.group(1).strip() != "Information Systems":
        report("ERROR", f"\\journal is '{j.group(1)}', expected 'Information Systems'")
    else:
        report("OK", "\\journal{Information Systems}")

    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    if not ab:
        report("ERROR", "no abstract environment")
    else:
        n = len(words(ab.group(1)))
        if "\\cite" in ab.group(1):
            report("ERROR", "abstract contains a citation")
        report("ERROR" if n > a.abstract_limit else "OK", f"abstract has {n} words (limit {a.abstract_limit})")

    kw = re.search(r"\\begin\{keyword\}(.*?)\\end\{keyword\}", tex, re.S)
    if not kw:
        report("ERROR", "no keyword environment")
    else:
        k = [x.strip() for x in kw.group(1).split("\\sep") if x.strip()]
        report("ERROR" if not 1 <= len(k) <= a.max_keywords else "OK", f"{len(k)} keywords: {'; '.join(k)}")

    for label, pat in [("CRediT statement", r"CRediT"),
                       ("competing-interest declaration", r"competing interest"),
                       ("data availability statement", r"[Dd]ata (and code )?availability"),
                       ("funding statement", r"\\section\*\{Funding|Funding\}|[Ff]unding")]:
        report("OK" if re.search(pat, tex, re.I) else "ERROR", f"{label} {'found' if re.search(pat, tex, re.I) else 'missing'}")

    ai = re.search(r"\\section\*\{([^}]*generative AI[^}]*)\}", tex, re.I)
    if not ai:
        report("WARN", "no generative-AI declaration section (required if any AI tool was used)")
    elif " ".join(ai.group(1).split()) != AI_HEADING:
        report("WARN", f"AI heading differs from Elsevier wording: '{ai.group(1)}'")
    else:
        report("OK", "generative-AI declaration heading matches Elsevier wording")
    if ai:
        after = tex[ai.end():]
        if re.search(r"\\section", after.split("thebibliography")[0]) and "\\appendix" not in after:
            report("WARN", "AI declaration is not the last section before the references")

    if re.search(r"\\bibliographystyle\{([^}]*)\}", tex):
        st = re.search(r"\\bibliographystyle\{([^}]*)\}", tex).group(1)
        report("OK" if st.startswith("elsarticle") else "WARN", f"bibliography style {st}")
    elif "thebibliography" in tex:
        n = len(re.findall(r"\\bibitem", tex))
        report("OK", f"hand-built thebibliography with {n} items")
    else:
        report("ERROR", "no bibliography found")

    keys = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", tex))
    cited = set(k.strip() for grp in re.findall(r"\\cite[pt]?(?:\[[^\]]*\])?\{([^}]*)\}", tex) for k in grp.split(","))
    if keys:
        for k in sorted(cited - keys):
            report("ERROR", f"cited but not defined: {k}")
        for k in sorted(keys - cited):
            report("WARN", f"bibitem never cited: {k}")
        items = re.split(r"\\bibitem", tex.split("\\begin{thebibliography}")[-1])[1:]
        nodoi = []
        for it in items:
            km = re.match(r"(?:\[[^\]]*\])?\{([^}]*)\}", it)
            body = it.split("\\end{thebibliography}")[0]
            if km and not re.search(r"doi|\\url|https?://", body, re.I):
                nodoi.append(km.group(1))
        if nodoi:
            report("WARN", f"{len(nodoi)} references without DOI or URL: {', '.join(sorted(nodoi)[:10])}")

    labels = set(re.findall(r"\\label\{([^}]*)\}", tex))
    for r in sorted(set(re.findall(r"\\ref\{([^}]*)\}", tex)) - labels):
        report("ERROR", f"\\ref to undefined label: {r}")
    for env in ("figure", "table"):
        for lab in re.findall(r"\\begin\{" + env + r"\*?\}.*?\\label\{([^}]*)\}.*?\\end\{" + env, tex, re.S):
            if not re.search(r"\\ref\{" + re.escape(lab) + r"\}", tex):
                report("WARN", f"{env} {lab} is never referenced in the text")

    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        cands = [folder / g] + [folder / (g + e) for e in (".pdf", ".png", ".jpg", ".eps")]
        if not any(c.exists() for c in cands):
            report("ERROR", f"figure file missing: {g}")

    if a.forbid:
        for f in sorted(folder.rglob("*")):
            if f.is_file() and f.suffix in {".tex", ".txt", ".md", ".bib"}:
                for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                    if re.search(a.forbid, line):
                        report("ERROR", f"forbidden string in {f.name}:{i}: {line.strip()[:90]}")
            if re.search(a.forbid, f.name):
                report("ERROR", f"forbidden string in file name: {f.name}")

    if a.highlights:
        hp = folder / a.highlights
        if not hp.exists():
            report("ERROR", f"highlights file not found: {hp}")
        else:
            hl = [x.strip().lstrip("-•* ").strip() for x in hp.read_text().splitlines() if x.strip()]
            report("OK" if 3 <= len(hl) <= 5 else "ERROR", f"{len(hl)} highlights (need 3-5)")
            for x in hl:
                if len(x) > 85:
                    report("ERROR", f"highlight has {len(x)} characters (max 85): {x}")
    else:
        report("WARN", "no highlights file given (--highlights)")

    log = tex_path.with_suffix(".log")
    if log.exists():
        lg = log.read_text(errors="ignore")
        und = len(re.findall(r"undefined", lg))
        ov = len(re.findall(r"Overfull \\hbox", lg))
        report("WARN" if und else "OK", f"log: {und} 'undefined' messages")
        report("WARN" if ov else "OK", f"log: {ov} overfull hboxes")
    else:
        report("WARN", "no .log file; compile before checking")

    print(f"\nSummary: {problems['ERROR']} error(s), {problems['WARN']} warning(s)")
    sys.exit(1 if problems["ERROR"] else 0)


if __name__ == "__main__":
    main()
