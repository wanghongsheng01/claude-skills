"""Shared helpers: follow a LaTeX \\input chain, collect citations, parse .bib files, and optionally compile a
scratch copy of the paper to read the authoritative .aux/.bbl/.blg/.log.

Standard library only (Python 3.9+)."""
import os, re, shutil, subprocess, tempfile

TEXBIN = [os.path.expanduser("~/Library/TinyTeX/bin/universal-darwin"), "/Library/TeX/texbin", "/usr/local/bin",
          "/opt/homebrew/bin", "/usr/bin"]


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def find_main(root):
    if os.path.isfile(root):
        return root
    for name in ("main.tex", "paper.tex", "ms.tex"):
        p = os.path.join(root, name)
        if os.path.exists(p):
            return p
    for f in sorted(os.listdir(root)):
        if f.endswith(".tex") and "\\documentclass" in open(os.path.join(root, f), errors="ignore").read():
            return os.path.join(root, f)
    raise SystemExit(f"no main .tex in {root}")


def expand(path, seen=None, root=None):
    """Return the text of `path` with \\input/\\include expanded, comments removed, plus the list of files.
    Paths resolve against the main file's folder (as LaTeX does), then against the including file's folder."""
    seen = seen if seen is not None else []
    root = root or os.path.dirname(path)
    seen.append(path)
    text = strip_comments(open(path, errors="ignore").read())

    def rep(m):
        p = m.group(2).strip()
        p = p if p.endswith(".tex") else p + ".tex"
        for f in (os.path.join(root, p), os.path.join(os.path.dirname(path), p)):
            if os.path.exists(f):
                break
        if f in seen or not os.path.exists(f):
            return ""
        return expand(f, seen, root)[0]
    return re.sub(r"\\(input|include)\{([^}]+)\}", rep, text), seen


CITE_RX = re.compile(r"\\(no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")


def cited_keys(text):
    keys, order = set(), []
    for m in CITE_RX.finditer(text):
        for k in m.group(2).split(","):
            k = k.strip()
            if k and k not in keys:
                keys.add(k); order.append(k)
    return order


def bib_files(text, root):
    out = []
    for m in re.finditer(r"\\bibliography\{([^}]+)\}", text):
        for b in m.group(1).split(","):
            b = b.strip()
            b = b if b.endswith(".bib") else b + ".bib"
            out.append(os.path.join(root, b))
    for m in re.finditer(r"\\addbibresource\{([^}]+)\}", text):
        out.append(os.path.join(root, m.group(1).strip()))
    return out


def _braced(s, i):
    """s[i] is '{' or '"'; return (content, index after)."""
    if s[i] == '"':
        j = s.index('"', i + 1)
        return s[i + 1:j], j + 1
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def parse_bib(path):
    """Minimal BibTeX parser: returns {key: {'_type':..., '_file':..., '_line':..., field: value}}."""
    s = open(path, errors="ignore").read()
    strings, entries = {}, {}
    for m in re.finditer(r"@(\w+)\s*\{", s):
        typ = m.group(1).lower()
        if typ in ("comment", "preamble"):
            continue
        body, _ = _braced(s, m.end() - 1)
        line = s.count("\n", 0, m.start()) + 1
        if typ == "string":
            mm = re.match(r"\s*(\w+)\s*=\s*[{\"](.*)[}\"]\s*$", body, re.S)
            if mm:
                strings[mm.group(1).lower()] = mm.group(2)
            continue
        key, _, rest = body.partition(",")
        e = {"_type": typ, "_file": os.path.basename(path), "_line": line}
        i = 0
        while i < len(rest):
            mm = re.compile(r"\s*([\w\-:]+)\s*=\s*").match(rest, i)
            if not mm:
                break
            name, j = mm.group(1).lower(), mm.end()
            if j < len(rest) and rest[j] in "{\"":
                val, j = _braced(rest, j)
            else:
                mv = re.compile(r"[^,]*").match(rest, j)
                raw = mv.group(0).strip()
                e.setdefault("_bare", {})[name] = raw
                val = " # ".join(strings.get(p.strip().lower(), p.strip()) for p in raw.split("#"))
                j = mv.end()
            e[name] = re.sub(r"\s+", " ", val).strip()
            k = rest.find(",", j)
            i = k + 1 if k >= 0 else len(rest)
        entries[key.strip()] = e
    return entries


def plain(s):
    """LaTeX field -> plain text (accents dropped, braces and simple macros removed)."""
    s = s or ""
    s = re.sub(r"\\(url|href)\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\\[\"'`^~=.uvHckr]\s*\{?(\w)\}?", r"\1", s)
    s = re.sub(r"\\(ss|o|O|l|L|ae|AE|oe|OE|aa|AA|i)\b", lambda m: {"ss": "ss", "i": "i"}.get(m.group(1), m.group(1)[0]), s)
    s = s.replace("\\&", "&").replace("--", "-").replace("~", " ")
    s = re.sub(r"\\(emph|textit|textbf|textsc|texttt|mathrm|mbox|text)\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\$([^$]*)\$", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()


def authors(field):
    out = []
    for a in re.split(r"\s+and\s+", field or ""):
        a = plain(a).strip()
        if not a:
            continue
        if a.lower() in ("others", "et al.", "et al"):
            out.append("others"); continue
        last = a.split(",")[0].strip() if "," in a else a.split()[-1]
        out.append(last)
    return out


def which(tool):
    for d in TEXBIN:
        p = os.path.join(d, tool)
        if os.path.exists(p):
            return p
    return shutil.which(tool)


def compile_scratch(root, main):
    """Compile a copy of the paper (pdflatex, bibtex, pdflatex x2). Returns dict with aux/bbl/blg/log text and
    the PDF path, or None when no TeX engine is installed. The source folder is never modified."""
    pdflatex, bibtex = which("pdflatex"), which("bibtex")
    if not (pdflatex and bibtex):
        return None
    tmp = tempfile.mkdtemp(prefix="sic_")
    dst = os.path.join(tmp, "src")
    shutil.copytree(root, dst, ignore=shutil.ignore_patterns(".git", "*.pdf.bak"))
    base = os.path.splitext(os.path.basename(main))[0]
    env = dict(os.environ, PATH=os.path.dirname(pdflatex) + os.pathsep + os.environ.get("PATH", ""))
    run = lambda cmd: subprocess.run(cmd, cwd=dst, env=env, capture_output=True, text=True, errors="ignore", timeout=600)
    run([pdflatex, "-interaction=nonstopmode", base])
    run([bibtex, base])
    run([pdflatex, "-interaction=nonstopmode", base])
    run([pdflatex, "-interaction=nonstopmode", base])
    rd = lambda ext: open(os.path.join(dst, base + ext), errors="ignore").read() if os.path.exists(os.path.join(dst, base + ext)) else ""
    return {"dir": dst, "aux": rd(".aux"), "bbl": rd(".bbl"), "blg": rd(".blg"), "log": rd(".log"),
            "pdf": os.path.join(dst, base + ".pdf")}
