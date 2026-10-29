#!/usr/bin/env python3
"""Assemble the Snapp upload set for a DMKD LaTeX manuscript.

Usage:
  python3 build_snapp_package.py FOLDER --main main.tex --out UPLOAD_DIR [--pdf compiled.pdf]
                                 [--cover cover_letter.docx] [--extra FILE ...]

Copies only what main.tex needs (main file, sn-jnl.cls, bst/bib if \\bibliography is used, every
\\includegraphics target) into a flat zip, writes MANIFEST.sha256 and UPLOAD_LIST.md, and refuses to
build if a needed file is missing or if main.tex uses \\input. Never modifies FOLDER.
"""
import argparse
import hashlib
import pathlib
import re
import shutil
import sys
import zipfile


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--out", required=True)
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--cover", default=None)
    ap.add_argument("--extra", nargs="*", default=[])
    a = ap.parse_args()

    src = pathlib.Path(a.folder)
    out = pathlib.Path(a.out)
    tex = strip_comments((src / a.main).read_text(errors="ignore"))
    if re.search(r"\\(input|include)\{", tex):
        sys.exit("ERROR main file uses \\input/\\include; flatten it first")
    need = [a.main, "sn-jnl.cls"]
    bib = re.search(r"\\bibliography\{([^}]*)\}", tex)
    if bib:
        need += [b.strip() + ".bib" for b in bib.group(1).split(",")]
        st = re.search(r"\\bibliographystyle\{([^}]*)\}", tex)
        need.append((st.group(1) if st else "sn-basic") + ".bst")
    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        if "/" in g:
            sys.exit(f"ERROR figure in a subfolder: {g}")
        hit = [c for c in [g, g + ".pdf", g + ".eps", g + ".png", g + ".jpg"] if (src / c).exists()]
        if not hit:
            sys.exit(f"ERROR figure not found: {g}")
        need.append(hit[0])
    need += a.extra
    missing = [n for n in need if not (src / n).exists()]
    if missing:
        sys.exit(f"ERROR missing files: {missing}")

    out.mkdir(parents=True, exist_ok=True)
    zpath = out / "LaTeX_source.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for n in dict.fromkeys(need):
            z.write(src / n, arcname=pathlib.Path(n).name)
    rows = [(zpath.name, sha(zpath))]
    for opt, name in ((a.pdf, "Manuscript.pdf"), (a.cover, None)):
        if opt:
            p = pathlib.Path(opt)
            dst = out / (name or p.name)
            shutil.copyfile(p, dst)
            rows.append((dst.name, sha(dst)))
    with open(out / "MANIFEST.sha256", "w") as f:
        for n, h in rows:
            f.write(f"{h}  {n}\n")
        f.write("\n# zip contents\n")
        for n in dict.fromkeys(need):
            f.write(f"{sha(src / n)}  LaTeX_source.zip:{pathlib.Path(n).name}\n")
    with open(out / "UPLOAD_LIST.md", "w") as f:
        f.write("# Snapp upload list (上传清单)\n\n")
        f.write("| 文件 | 门户用途 |\n|---|---|\n")
        f.write("| LaTeX_source.zip | Manuscript source (LaTeX zip, compiled by Snapp with pdflatex) |\n")
        if a.pdf:
            f.write("| Manuscript.pdf | Compiled PDF of the same source |\n")
        if a.cover:
            f.write(f"| {pathlib.Path(a.cover).name} | Cover letter |\n")
        f.write("\nZip 内文件：" + ", ".join(pathlib.Path(n).name for n in dict.fromkeys(need)) + "\n")
    print(f"OK wrote {zpath} with {len(dict.fromkeys(need))} files")


if __name__ == "__main__":
    main()
