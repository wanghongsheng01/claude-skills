#!/usr/bin/env python3
"""Build a reviewer packet from a LaTeX manuscript so that reviewer agents can cite exact lines.

  python3 review_packet.py manuscript.tex --out review_packet.md [--numbers tables/numbers.tex]

The packet holds: a section map with source line ranges, every caption, every sentence that
contains a number or a comparative claim (with its source line), the abstract, and the
contribution list. With --numbers, macros \\res{..}, \\stat{..} defined in a generated numbers
file are expanded so the reviewer sees the values. It reads files only.
"""
import argparse
import pathlib
import re


def load_numbers(path):
    vals = {}
    if path:
        for k, v in re.findall(r"\\csname ([^\\]+)\\endcsname\{([^}]*)\}", pathlib.Path(path).read_text()):
            vals[k] = v.replace("$\\pm$", "±").replace("\\%", "%")
    return vals


def expand(line, vals):
    line = re.sub(r"\\res\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}",
                  lambda m: vals.get(f"r@{m.group(1)}@{m.group(2)}@{m.group(3)}@{m.group(4)}", m.group(0)), line)
    line = re.sub(r"\\stat\{([^}]*)\}", lambda m: vals.get(m.group(1), m.group(0)), line)
    return line


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--out", default="review_packet.md")
    ap.add_argument("--numbers")
    a = ap.parse_args()
    vals = load_numbers(a.numbers)
    lines = pathlib.Path(a.tex).read_text(errors="ignore").splitlines()
    out = ["# Reviewer packet", f"Source: {a.tex} ({len(lines)} lines). Line numbers refer to the source file.", ""]

    out.append("## Section map")
    for i, l in enumerate(lines, 1):
        m = re.match(r"\s*\\(sub)*section\*?\{(.*)\}", l)
        if m:
            out.append(f"- L{i}: {'  ' * (len(m.group(1) or '') // 3)}{m.group(2)}")
    out.append("")

    out.append("## Captions")
    text = "\n".join(lines)
    for m in re.finditer(r"\\caption\{", text):
        start = text.count("\n", 0, m.start()) + 1
        depth, j = 1, m.end()
        while depth and j < len(text):
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        out.append(f"- L{start}: " + " ".join(expand(text[m.end():j - 1], vals).split()))
    out.append("")

    out.append("## Sentences with numbers or comparative claims")
    claim = re.compile(r"\d|\\res|\\stat|significan|better|cheaper|lower|higher|outperform|improv|reduc", re.I)
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("%") or l.lstrip().startswith("\\expandafter"):
            continue
        if claim.search(l) and not re.match(r"\s*\\(begin|end|label|input|includegraphics|usepackage)", l):
            out.append(f"- L{i}: {expand(l.strip(), vals)}")
    pathlib.Path(a.out).write_text("\n".join(out) + "\n")
    print("wrote", a.out, len(out), "lines")


if __name__ == "__main__":
    main()
