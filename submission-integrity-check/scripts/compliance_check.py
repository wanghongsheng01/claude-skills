#!/usr/bin/env python3
"""Must-follow items of a venue's call for papers, checked on the LaTeX source and the PDF that will be uploaded.

The rules come from a profile (profiles/<venue>.json), so the same script serves other venues. The ICDE 2027
profile encodes the research-track call (re-read 2026-11-11): IEEE conference template, 12 pages excluding
references and the AI-generated-content declaration, no appendix, PDF only, single-blind, mandatory AI
declaration, EAB title prefix, public artifact URL (all artifacts for EAB), no negative spaces or margin
intrusions or font changes.

Usage: compliance_check.py <paper_dir> --pdf <file.pdf> [--profile icde2027] [--eab] [--out <dir>]
Exit code 1 if any ERROR."""
import argparse, json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texbib as tb

HERE = os.path.dirname(os.path.abspath(__file__))
res = []


def rep(level, rule, msg):
    res.append((level, rule, msg)); print(f"{level:5} {rule:4} {msg}")


def heading_page(pages, rx):
    for i, p in enumerate(pages):
        for line in p.splitlines():
            if re.fullmatch(rx, re.sub(r"\s+", " ", line).strip(), re.I):
                return i
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper"); ap.add_argument("--pdf", required=True)
    ap.add_argument("--profile", default="icde2027"); ap.add_argument("--eab", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    prof = json.load(open(os.path.join(HERE, "..", "profiles", a.profile + ".json")))
    main_tex = tb.find_main(a.paper); text, files = tb.expand(main_tex)
    raw_main = open(main_tex, errors="ignore").read()

    # C01 template
    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]+)\}", text)
    cls, opts = (m.group(2), m.group(1) or "") if m else ("?", "")
    ok = cls == prof["class"] and all(o in opts for o in prof.get("class_options", []))
    rep("OK" if ok else "ERROR", "C01", f"template \\documentclass{opts}{{{cls}}} (required: {prof['class']} {prof.get('class_options')})")
    bad_opts = [o for o in ("9pt", "11pt", "12pt", "draftcls", "onecolumn") if o in opts]
    if bad_opts:
        rep("ERROR", "C01", f"class options that change the IEEE format: {bad_opts}")

    # C02 spacing / margin / font hacks (desk-reject: negative spaces, margins, font changes)
    hacks = []
    for rx, what in [(r"\\vspace\*?\{\s*-", "negative \\vspace"), (r"\\hspace\*?\{\s*-\s*\d", "negative \\hspace"),
                     (r"\\usepackage(\[[^\]]*\])?\{geometry\}", "geometry package"), (r"\\enlargethispage", "\\enlargethispage"),
                     (r"\\(set|addto)length\{\\(textheight|textwidth|columnsep|topmargin|oddsidemargin|evensidemargin|headsep|footskip)\}", "page geometry changed"),
                     (r"\\renewcommand\{?\\baselinestretch", "\\baselinestretch"), (r"\\linespread\{", "\\linespread"),
                     (r"\\(set|addto)length\{\\(abovecaptionskip|belowcaptionskip|textfloatsep|floatsep|intextsep|dbltextfloatsep)\}\{\s*-", "negative float/caption skip"),
                     (r"\\fontsize\{\s*[0-8](\.\d+)?pt", "body text set below 9 pt"), (r"\\usepackage(\[[^\]]*\])?\{(times|mathptmx|helvet|palatino|lmodern)\}", "font package that overrides the template font")]:
        n = len(re.findall(rx, text))
        if n:
            hacks.append(f"{what} x{n}")
    rep("ERROR" if hacks else "OK", "C02", "spacing/margin/font changes: " + (", ".join(hacks) if hacks else "none"))
    small = len(re.findall(r"\\(tiny|scriptsize)\b", text))
    if small:
        rep("WARN", "C02", f"\\tiny/\\scriptsize used {small}x (tables/figures may become unreadable; reviewers may read it as a length workaround)")

    # PDF checks
    try:
        import fitz
    except ImportError:
        rep("ERROR", "C00", "PyMuPDF (fitz) is not installed: pip install pymupdf"); return finish(a)
    doc = fitz.open(a.pdf)
    pages = [p.get_text() for p in doc]
    size_mb = os.path.getsize(a.pdf) / 1e6
    rep("OK" if size_mb <= prof["max_pdf_mb"] else "ERROR", "C03", f"PDF {size_mb:.2f} MB (limit {prof['max_pdf_mb']} MB), {len(pages)} pages")
    w, h = doc[0].rect.width, doc[0].rect.height
    rep("OK" if abs(w - 612) < 3 and abs(h - 792) < 3 else "ERROR", "C03", f"page size {w:.0f}x{h:.0f} pt (US Letter 612x792)")

    # C04 page limit: body ends before the AI declaration or the references, whichever comes first
    ref_p = heading_page(pages, r"(R\s?EFERENCES|References|REFERENCES|Bibliography)")
    ai_p = heading_page(pages, r"((A\s?I|AI)[- ]?(G\s?ENERATED|Generated)?.{0,40}(A\s?CKNOWLEDG|Acknowledg|D\s?ECLARATION|Declaration|D\s?ISCLOSURE|Disclosure).*)")
    cut = min([p for p in (ref_p, ai_p) if p is not None] or [len(pages)])
    # if the heading is not at the top of its page, the body occupies part of that page too
    body_pages = cut + 1
    if cut < len(pages):
        page_txt = pages[cut]
        hd = re.search(r"(R\s?EFERENCES|References|A\s?I[- ]G\s?ENERATED|AI-Generated|AI Generated)", page_txt)
        if hd and len(page_txt[:hd.start()].strip()) < 80:
            body_pages = cut
    lim = prof["body_page_limit"]
    rep("OK" if body_pages <= lim else "ERROR", "C04", f"body pages {body_pages} (limit {lim}, excluding references and the AI declaration); "
        f"references start on p.{(ref_p or 0) + 1}, AI declaration on p.{(ai_p + 1) if ai_p is not None else '-'}")
    if ref_p is None:
        rep("ERROR", "C04", "no References heading found in the PDF")

    # C05 no appendix
    app = [i + 1 for i, p in enumerate(pages) if re.search(r"^\s*(A\s?PPENDIX|Appendix|APPENDICES)\b", p, re.M)]
    app_tex = re.findall(r"\\appendix\b|\\begin\{appendices\}|\\section\*?\{\s*Appendix", text)
    if prof.get("no_appendix"):
        rep("ERROR" if (app or app_tex) else "OK", "C05", "appendix: " + (f"found in PDF pages {app} / source {app_tex[:2]}" if (app or app_tex) else "none"))
        online = re.findall(r"(?i)(extended|full|technical)[ -](version|report)[^.]{0,80}", " ".join(pages[:cut]))
        if online:
            rep("WARN", "C05", f"text points to an extended version ({online[:2]}): reviewers are not required to read it; the paper must stand alone")

    # C06 AI-generated content declaration
    if prof.get("ai_declaration_required"):
        if ai_p is None and not re.search(r"(?i)\\section\*?\{[^}]*(AI|artificial intelligence)[^}]*(acknowledg|declar|disclos)", text):
            rep("ERROR", "C06", "no AI-generated content declaration section (mandatory)")
        else:
            seg = " ".join(pages[ai_p:]) if ai_p is not None else text
            named = re.search(r"(?i)(gpt|claude|chatgpt|gemini|llama|qwen|deepseek|copilot|kimi|glm|doubao|llm)", seg)
            sec_named = re.search(r"(?i)(section|sec\.|§)\s*[IVX\d]", seg)
            rep("OK" if named else "WARN", "C06", "AI declaration present" + ("" if named else ": no AI system named (the call requires identifying the system)"))
            if not sec_named:
                rep("WARN", "C06", "AI declaration does not name the sections where AI content appears (the call asks for specific sections)")
            if ai_p is not None and ref_p is not None and ai_p < ref_p and ai_p + 1 > lim:
                rep("WARN", "C06", "AI declaration placed before the references and beyond the page limit: check how the venue counts it")

    # C07 single-blind: authors visible; no anonymisation leftovers
    first = pages[0]
    anon = re.search(r"(?i)anonymous author|author names? (withheld|hidden)|paper id\s*\d+", first)
    if prof.get("review") == "single-blind":
        has_names = re.search(r"\\author\{", text) and not re.search(r"\\author\{\s*\}", text)
        rep("ERROR" if anon or not has_names else "OK", "C07", "single-blind: author block " + ("missing or anonymised" if anon or not has_names else "present"))
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", first)
    rep("OK" if emails else "WARN", "C07", f"e-mails on page 1: {emails[:4] if emails else 'none'}")

    # C08 EAB title prefix
    title = re.sub(r"\s+", " ", tb.plain((re.search(r"\\title\{(.*?)\}\s*\n", text, re.S) or re.search(r"\\title\{(.*)\}", text) or [None, ""])[1]))
    prefix = prof.get("eab_title_prefix")
    if a.eab and prefix:
        rep("OK" if title.startswith(prefix) else "ERROR", "C08", f"EAB title starts with '{prefix}': '{title[:90]}'")
    elif prefix and title.startswith(prefix):
        rep("ERROR", "C08", "EAB prefix in the title of a paper not checked with --eab")

    # C09 artifact URL in the paper and reachable
    urls = sorted(set(re.findall(r"https?://(?:github\.com|gitlab\.com|zenodo\.org|figshare\.com|osf\.io|doi\.org/10\.5281)[^\s}\])>,]*", " ".join(pages) + text)))
    if not urls:
        rep("ERROR" if a.eab else "WARN", "C09", "no artifact URL (GitHub/Zenodo/...) in the paper" + (" -- EAB papers must provide all artifacts" if a.eab else ""))
    urls = [u.rstrip(".") for u in urls if not re.fullmatch(r"https?://[^/]+/?", u.rstrip("."))]
    for u in urls[:10]:
        try:
            st = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).status
        except Exception as ex:
            st = getattr(ex, "code", 0)
        rep("OK" if st == 200 else "ERROR", "C09", f"artifact URL {u} -> HTTP {st}")
    personal = re.findall(r"https?://(?:sites\.google|[\w-]+\.github\.io|dropbox|drive\.google|pan\.baidu|onedrive)[^\s}]*", text)
    if personal:
        rep("WARN", "C09", f"links to personal pages or private sharing services {personal[:3]} (the call asks for standard open services)")

    # C10 unresolved references / citations / draft leftovers in the PDF
    whole = "\n".join(pages)
    q = len(re.findall(r"\?\?|\[\?\]", whole))
    rep("ERROR" if q else "OK", "C10", f"unresolved '??' or '[?]' in the PDF: {q}")
    todo = re.findall(r"\b(TODO|FIXME|XXX|TBD)\b", whole)
    rep("ERROR" if todo else "OK", "C10", f"draft markers in the PDF: {len(todo)}")

    # C11 fonts embedded, no Type 3
    fonts = {}
    for p in doc:
        for f in p.get_fonts(full=True):
            fonts[f[3]] = (f[1], f[2])
    t3 = [n for n, (ext, typ) in fonts.items() if typ == "Type3"]
    nemb = [n for n, (ext, typ) in fonts.items() if ext == "n/a" and typ != "Type3"]
    rep("OK" if not nemb else "ERROR", "C11", f"{len(fonts)} fonts; not embedded: {nemb[:5] or 'none'}")
    if t3:
        rep("WARN", "C11", f"Type 3 fonts {t3[:5]} (usually from matplotlib PDFs; set pdf.fonttype 42 before the camera-ready)")

    # C12 references section sanity: the PDF list size matches the cited keys
    if ref_p is not None:
        reflist = " ".join(pages[ref_p:(ai_p if ai_p is not None and ai_p > ref_p else len(pages))])
        nums = [int(n) for n in re.findall(r"(?m)^\s*\[(\d{1,3})\]", reflist)]
        cited = [k for k in tb.cited_keys(text) if k != "*"]
        n_pdf = max(nums) if nums else 0
        rep("OK" if n_pdf == len(cited) or not nums else "WARN", "C12", f"reference list has {n_pdf} entries; {len(cited)} distinct keys cited in the source")
        if prof.get("citation_style") == "ieee-numeric" and re.search(r"\\usepackage(\[[^\]]*\])?\{natbib\}", text) and "numbers" not in text:
            rep("WARN", "C12", "natbib without the numbers option: IEEE uses numeric [n] citations")
        if re.search(r"\\bibliographystyle\{(?!IEEEtran)", text) and prof.get("bst"):
            rep("WARN", "C12", f"bibliography style is not {prof['bst']}")
    return finish(a)


def finish(a):
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump([{"level": l, "rule": r, "msg": m} for l, r, m in res], open(os.path.join(a.out, "compliance.json"), "w"), indent=1)
    n_err = sum(1 for l, _, _ in res if l == "ERROR")
    print(f"\n{n_err} errors, {sum(1 for l, _, _ in res if l == 'WARN')} warnings")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
