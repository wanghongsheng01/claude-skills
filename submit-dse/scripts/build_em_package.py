#!/usr/bin/env python3
"""Build the Editorial Manager upload set for DSE: flat LaTeX zip plus a SHA-256 manifest.

Usage: python3 build_em_package.py FOLDER --main main.tex --out UPLOAD_DIR [--pdf main.pdf] [--extra FILE ...]
Writes UPLOAD_DIR/LaTeX_source.zip (main file, .cls, .bst, figures) and UPLOAD_DIR/MANIFEST.sha256.
"""
import argparse, hashlib, pathlib, re, shutil, zipfile


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--out", required=True)
    ap.add_argument("--pdf")
    ap.add_argument("--extra", nargs="*", default=[])
    a = ap.parse_args()
    root, out = pathlib.Path(a.folder), pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    tex = (root / a.main).read_text(errors="ignore")
    files = [root / a.main] + [root / f for f in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex)]
    files += [p for p in root.iterdir() if p.suffix in (".cls", ".bst")]
    zip_path = out / "LaTeX_source.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(f, f.name)
    for f in ([a.pdf] if a.pdf else []) + a.extra:
        shutil.copy(f, out / pathlib.Path(f).name)
    names = sorted(p for p in out.iterdir() if p.is_file() and p.name != "MANIFEST.sha256")
    (out / "MANIFEST.sha256").write_text("".join(f"{sha(p)}  {p.name}\n" for p in names))
    for p in names:
        print(f"{p.stat().st_size:>10}  {p.name}")


if __name__ == "__main__":
    main()
