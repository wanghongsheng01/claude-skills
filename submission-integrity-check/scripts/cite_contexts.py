#!/usr/bin/env python3
"""Citation-accuracy worksheet: every sentence that cites a work, next to what that work actually is.

For each cited key it lists the verified record (title, venue, year from Crossref/OpenAlex/arXiv/URL, taken from
refcheck.json written by ref_check.py), its abstract when one is available, and every sentence of the paper that
cites it, with the section it occurs in. A reviewer (Claude or a co-author) then gives each claim a verdict:
  OK          the sentence describes the cited work correctly
  IMPRECISE   right work, but a detail is wrong or overstated (a number, a year, "first", "only", the method)
  WRONG       the cited work does not say this, or a different work is meant
  UNSURE      the abstract is not enough; open the paper
Numbers attributed to a cited work (speed-ups, accuracies, dataset sizes) are always checked against the paper.

Usage: cite_contexts.py <paper_dir> --refcheck <out>/refcheck.json --out <out>/cite_worksheet.md"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texbib as tb


def sentences_with_cites(text):
    body = re.sub(r"\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}", lambda m: " [FLOAT] " + " ".join(
        re.findall(r"\\caption\{(.*?)\}\s*(?:\\label|$)", m.group(0), re.S)), text, flags=re.S)
    section = "front matter"
    out = []
    for part in re.split(r"(\\(?:sub)*section\*?\{[^}]*\})", body):
        m = re.match(r"\\(?:sub)*section\*?\{([^}]*)\}", part)
        if m:
            section = tb.plain(m.group(1)); continue
        flat = re.sub(r"\s+", " ", part)
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\\])", flat):
            keys = []
            for mm in tb.CITE_RX.finditer(s):
                if mm.group(1):
                    continue  # \nocite
                keys += [k.strip() for k in mm.group(2).split(",") if k.strip()]
            if keys:
                shown = tb.CITE_RX.sub(lambda mm: "[" + mm.group(2) + "]", s)
                out.append((section, keys, tb.plain(shown)[:900]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper"); ap.add_argument("--refcheck", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    text, _ = tb.expand(tb.find_main(a.paper))
    refs = {r["key"]: r for r in json.load(open(a.refcheck))["refs"]}
    by_key = {}
    for sec, keys, s in sentences_with_cites(text):
        for k in keys:
            by_key.setdefault(k, []).append((sec, len(keys), s))
    with open(a.out, "w") as f:
        f.write("# Citation-accuracy worksheet\n\nVerdicts: OK / IMPRECISE / WRONG / UNSURE (see cite_contexts.py).\n\n")
        for i, k in enumerate(sorted(by_key, key=lambda k: list(refs).index(k) if k in refs else 999), 1):
            r = refs.get(k, {})
            fd = r.get("found") or {}
            f.write(f"## {i}. `{k}` [{r.get('verdict', '?')}]\n\n")
            f.write(f"- **Bib entry**: {r.get('title', '')} ({', '.join(r.get('authors') or [])}; {r.get('venue', '')} {r.get('year', '')})\n")
            if fd:
                f.write(f"- **Record found**: {fd.get('title', '')} ({fd.get('venue', '')} {fd.get('year', '')}; {fd.get('doi') or fd.get('id') or ''})\n")
            ab = (r.get("abstract") or "").strip()
            f.write(f"- **Abstract**: {ab[:1800] if ab else '(none available: open the paper)'}\n")
            f.write("- **Cited in this paper**:\n")
            for sec, n, s in by_key[k]:
                f.write(f"  - [{sec}]{' (group of %d)' % n if n > 1 else ''} {s}\n")
            f.write("- **Verdict**: \n\n")
    print(f"{len(by_key)} cited works, {sum(len(v) for v in by_key.values())} citing sentences -> {a.out}")


if __name__ == "__main__":
    main()
