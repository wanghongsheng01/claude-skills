#!/usr/bin/env python3
"""Reference integrity check for a LaTeX paper.

1. Format lint of every CITED BibTeX entry (IEEE/ICDE conventions): required fields, 'and others'/'et al.',
   future or implausible years, arXiv/CoRR entries that may have a published version, inconsistent venue
   spellings, duplicate titles, cited keys missing from the .bib, malformed DOIs.
2. Online existence check of every cited entry against Crossref and OpenAlex (and arXiv for preprints):
   title similarity, first-author surname, year and venue. Verdicts:
     VERIFIED   title matches (>= 0.93), first author matches, year within 1
     CHECK      the work exists but a field differs (year, authors, venue, DOI): fix the entry
     SUSPECT    only a weak title match (0.75-0.93): read the record and decide; may be invented or mangled
     NOT_FOUND  no candidate: treat as possibly invented until a human finds the source
     WEB        @misc/@online with a URL (software, dataset, web page): URL reachability only
   Results are cached in <out>/ref_cache.json so a re-run only queries changed entries.

Usage: ref_check.py <paper_dir> --out <dir> [--compile] [--offline]
Writes <out>/refcheck.json and <out>/refcheck.md. Exit code 1 if any ERROR, NOT_FOUND or SUSPECT remains."""
import argparse, json, os, re, sys, time, difflib, datetime, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texbib as tb

UA = "submission-integrity-check/1.0 (https://github.com/wanghongsheng01/claude-skills)"
THIS_YEAR = datetime.date.today().year
REQUIRED = {"article": ["author", "title", "journal", "year"],
            "inproceedings": ["author", "title", "booktitle", "year"],
            "incollection": ["author", "title", "booktitle", "year"],
            "book": ["title", "year"], "phdthesis": ["author", "title", "school", "year"],
            "techreport": ["author", "title", "institution", "year"]}
VENUE_ALIASES = [  # (canonical, regex) used to spot two spellings of one venue inside a paper
    ("PVLDB", r"\b(pvldb|proc(eedings)?\.? (of )?(the )?vldb endow(ment)?\.?|vldb j(ournal)?)\b"),
    ("SIGMOD", r"\bsigmod\b|management of data"), ("ICDE", r"\bicde\b|data engineering"),
    ("NeurIPS", r"\bneurips\b|\bnips\b|neural information processing"), ("ACL", r"\bacl\b|computational linguistics"),
    ("TKDE", r"\btkde\b|trans(actions)?\.? (on )?knowledge and data")]


CANON = [("VLDB", r"vldb|very large data"), ("SIGMOD", r"sigmod|management of data|pacmmod|proc\.? acm manag"),
         ("ICDE", r"\bicde\b|data engineering \(icde\)|international conference on data engineering"),
         ("KDD", r"\bkdd\b|knowledge discovery"), ("WWW", r"\bwww\b|world wide web|web conference"),
         ("NeurIPS", r"neurips|\bnips\b|neural information processing"), ("ICML", r"\bicml\b|international conference on machine learning"),
         ("ICLR", r"\biclr\b|learning representations"), ("ACL", r"^(proc[^ ]* )?(acl|annual meeting of the association for computational)"),
         ("EMNLP", r"emnlp|empirical methods in natural"), ("NAACL", r"naacl|north american chapter"),
         ("CIDR", r"\bcidr\b|innovative data"), ("TODS", r"\btods\b|trans[a-z.]* (on )?database sys"),
         ("TKDE", r"\btkde\b|knowledge and data eng"), ("PODS", r"\bpods\b|principles of database"),
         ("EDBT", r"\bedbt\b|extending database"), ("CIKM", r"\bcikm\b|information and knowledge management"),
         ("SIGIR", r"\bsigir\b|research and development in information retrieval"), ("AAAI", r"\baaai\b"),
         ("IJCAI", r"\bijcai\b"), ("OSDI", r"\bosdi\b|operating systems design"), ("SOSP", r"\bsosp\b|operating systems principles"),
         ("CCS", r"\bccs\b|computer and communications security"), ("USENIX Sec", r"usenix security")]


def canon_venue(v):
    v = tb.plain(v or "").lower()
    for name, rx in CANON:
        if re.search(rx, v):
            return name
    return None


def get_json(url, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode("utf-8", "ignore"))
        except Exception as ex:
            if k == tries - 1:
                return {"_error": str(ex)[:120]}
            time.sleep(1.5 * (k + 1))


def get_text(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.read().decode("utf-8", "ignore")
    except Exception:
        return ""


def url_status(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as ex:
        return ex.code
    except Exception:
        return 0


def norm(s):
    s = tb.plain(s).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    r = difflib.SequenceMatcher(None, a, b).ratio()
    # a subtitle dropped on one side ("X: a y for z" vs "X") should still match
    if (a.startswith(b) or b.startswith(a)) and min(len(a), len(b)) >= 25:
        r = max(r, 0.95)
    return r


def ascii_fold(s):
    import unicodedata
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def cand_crossref(item):
    t = (item.get("title") or [""])[0]
    st = (item.get("subtitle") or [""])
    if st and st[0] and st[0].lower() not in t.lower():
        t = f"{t}: {st[0]}"  # PVLDB records keep the part after the colon in 'subtitle'
    yr = None
    for k in ("published-print", "published-online", "issued", "created"):
        dp = (item.get(k) or {}).get("date-parts")
        if dp and dp[0] and dp[0][0]:
            yr = dp[0][0]; break
    return {"src": "crossref", "title": t, "year": yr, "doi": item.get("DOI"),
            "venue": ((item.get("container-title") or [""])[0]),
            "authors": [a.get("family", "") for a in item.get("author", [])],
            "full": [(a.get("given", "") + " " + a.get("family", "")).strip() for a in item.get("author", [])],
            "type": item.get("type"), "abstract": re.sub(r"<[^>]+>", " ", item.get("abstract", "") or "")}


def cand_openalex(w):
    inv = w.get("abstract_inverted_index") or {}
    words = sorted(((p, wd) for wd, ps in inv.items() for p in ps))
    loc = (w.get("primary_location") or {}).get("source") or {}
    return {"src": "openalex", "title": w.get("title") or "", "year": w.get("publication_year"),
            "doi": (w.get("doi") or "").replace("https://doi.org/", "") or None, "venue": loc.get("display_name") or "",
            "authors": [((a.get("author") or {}).get("display_name") or "").split()[-1:][0] if (a.get("author") or {}).get("display_name") else ""
                        for a in w.get("authorships", [])],
            "full": [((a.get("author") or {}).get("display_name") or "") for a in w.get("authorships", [])],
            "type": w.get("type"), "abstract": " ".join(wd for _, wd in words), "id": w.get("id")}


def cand_arxiv(xml):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        g = lambda tag: (re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", e, re.S) or [None, ""])[1]
        out.append({"src": "arxiv", "title": re.sub(r"\s+", " ", g("title")).strip(), "year": int(g("published")[:4] or 0) or None,
                    "doi": None, "venue": "arXiv", "authors": [n.split()[-1] for n in re.findall(r"<name>(.*?)</name>", e)],
                    "full": re.findall(r"<name>(.*?)</name>", e), "type": "preprint", "abstract": re.sub(r"\s+", " ", g("summary")).strip(), "id": g("id")})
    return out


def entry_url(e):
    if e.get("url"):
        return e["url"]
    m = re.search(r"https?://[^\s}]+", " ".join(e.get(k, "") for k in ("howpublished", "note")))
    return m.group(0) if m else None


def arxiv_id(e):
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", " ".join(e.get(k, "") for k in ("eprint", "howpublished", "note", "journal", "url")))
    return m.group(1) if m else None


SOURCE_ERRORS = []


def lookup(e):
    title = tb.plain(e.get("title", ""))
    first = (tb.authors(e.get("author", "")) or [""])[0]
    cands = []
    doi = (e.get("doi") or "").strip()
    if doi:
        d = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        if d.get("message"):
            c = cand_crossref(d["message"]); c["by_doi"] = True; cands.append(c)
    q = urllib.parse.quote(title[:250])
    d = get_json(f"https://api.crossref.org/works?query.bibliographic={q}"
                 + (f"&query.author={urllib.parse.quote(first)}" if first and first != "others" else "") + "&rows=5")
    cands += [cand_crossref(i) for i in (d.get("message") or {}).get("items", [])]
    t_oa = re.sub(r"[,:;!?|()\[\]]", " ", title)[:250]
    d = get_json("https://api.openalex.org/works?per-page=5&search=" + urllib.parse.quote(t_oa)
                 + "&select=id,title,publication_year,doi,authorships,primary_location,abstract_inverted_index,type")
    if "_error" in d or "error" in d:
        SOURCE_ERRORS.append("openalex: " + str(d.get("_error") or d.get("error"))[:60])
    cands += [cand_openalex(w) for w in d.get("results", [])]
    ax = arxiv_id(e)
    if ax:
        cands += [dict(c, by_id=True) for c in cand_arxiv(get_text("https://export.arxiv.org/api/query?id_list=" + ax))]
    if max([sim(title, c["title"]) for c in cands] or [0]) < 0.9:
        # second pass: title-only queries (the author filter and free-text search sometimes return noise)
        time.sleep(0.5)
        d = get_json(f"https://api.crossref.org/works?query.title={q}&rows=5")
        cands += [cand_crossref(i) for i in (d.get("message") or {}).get("items", [])]
        d = get_json("https://api.openalex.org/works?per-page=5&filter=title.search:" + urllib.parse.quote(t_oa.replace(",", " "))
                     + "&select=id,title,publication_year,doi,authorships,primary_location,abstract_inverted_index,type")
        cands += [cand_openalex(w) for w in d.get("results", [])]
    is_arxiv = re.search(r"arxiv|corr", " ".join(str(e.get(k, "")) for k in ("journal", "booktitle", "eprint", "archiveprefix", "url", "note", "howpublished")), re.I)
    if is_arxiv or max([sim(title, c["title"]) for c in cands] or [0]) < 0.9:
        words = [w for w in re.sub(r"[^\w\s]", " ", title).split() if len(w) > 3][:8]
        queries = ['ti:"' + re.sub(r"[^\w\s-]", " ", title)[:200] + '"', " AND ".join("ti:" + w for w in words)]
        head = title.split(":")[0].strip()
        if ":" in title and len(head) >= 4:
            queries.append('ti:"' + re.sub(r"[^\w\s-]", " ", head) + '"')
        for qq in queries:
            cands += cand_arxiv(get_text("https://export.arxiv.org/api/query?max_results=3&search_query=" + urllib.parse.quote(qq)))
            if max([sim(title, c["title"]) for c in cands] or [0]) >= 0.85:
                break
            time.sleep(1)
    return cands


def judge(key, e, cands):
    title = tb.plain(e.get("title", ""))
    auth = tb.authors(e.get("author", ""))
    first = ascii_fold(auth[0]) if auth else ""
    year = int(re.sub(r"\D", "", e.get("year", "0"))[:4] or 0)
    scored = []
    for c in cands:
        s = sim(title, c["title"])
        fa = ascii_fold(c["authors"][0]) if c.get("authors") else ""
        full = ascii_fold(" ".join(c.get("full") or c.get("authors") or []))
        a_ok = (not first or first == "others" or not full or first in ascii_fold(" ".join((c.get("full") or c["authors"])[:3])) or fa in first)
        y_ok = (not year or not c.get("year") or abs(c["year"] - year) <= 1)
        if c.get("by_doi") and (e.get("doi") or "").lower().strip() == (c.get("doi") or "").lower():
            y_ok = True if s >= 0.85 else y_ok
        if c.get("by_doi") and s < 0.93 and norm(c["title"]) and norm(title).startswith(norm(c["title"])):
            s = 0.95  # the DOI record carries only the short title
        scored.append((s + 0.05 * a_ok + 0.03 * y_ok, s, a_ok, y_ok, c))
    if not scored:
        return {"verdict": "NOT_FOUND", "issues": ["no candidate returned by Crossref/OpenAlex/arXiv"]}
    scored.sort(key=lambda t: -t[0])
    _, s, a_ok, y_ok, best = scored[0]
    # prefer a peer-reviewed record over a preprint of the same work when both match
    peer = [t for t in scored if t[1] >= 0.93 and t[4]["src"] != "arxiv" and "posted-content" not in str(t[4].get("type"))
            and "preprint" not in str(t[4].get("type")) and "arxiv" not in (t[4].get("venue") or "").lower()]
    issues = []
    byid = [c for c in cands if c.get("by_id")]
    if byid and sim(title, byid[0]["title"]) < 0.93:
        c = byid[0]
        return {"verdict": "CHECK", "similarity": round(sim(title, c["title"]), 3),
                "issues": [f"arXiv {arxiv_id(e)} is titled '{c['title'][:120]}' (bib title differs)"],
                "found": {"src": c["src"], "title": c["title"], "year": c["year"], "venue": c["venue"], "id": c.get("id"),
                          "authors": c.get("authors", [])[:6]},
                "abstract": (c.get("abstract") or "")[:2500]}
    if s >= 0.93:
        verdict = "VERIFIED"
        if not a_ok:
            verdict = "CHECK"; issues.append(f"first author '{auth[0] if auth else ''}' not in found authors {best['authors'][:4]}")
        same_doi = (e.get("doi") or "").lower().strip() and (e.get("doi") or "").lower().strip() == (best.get("doi") or "").lower()
        if not y_ok and not same_doi:
            verdict = "CHECK"; issues.append(f"year {year} vs found {best['year']}")
        elif not y_ok:
            issues.append(f"record year {best['year']} differs, but the DOI is the same (indexing date); keep the publication year")
        fulls = [ascii_fold(x) for x in (best.get("full") or [])]
        bl = [ascii_fold(x) for x in auth if x != "others"]
        if fulls and len(bl) >= 2 and len(fulls) >= len(bl):
            pos = [next((i for i, f in enumerate(fulls) if b and b in f), -1) for b in bl]
            if -1 not in pos and pos != sorted(pos):
                verdict = "CHECK"; issues.append("author order differs from the record: " + ", ".join(best.get("full", [])[:8]))
            elif -1 in pos and "others" not in auth:
                miss = [auth[i] for i, p_ in enumerate(pos) if p_ == -1]
                verdict = "CHECK"; issues.append(f"authors {miss} not in the record's list: " + ", ".join(best.get("full", [])[:8]))
            elif "others" not in auth and len(fulls) > len(bl) and len(fulls) <= 30:
                verdict = "CHECK"; issues.append(f"bib lists {len(bl)} authors, the record {len(fulls)}: " + ", ".join(best.get("full", [])[:8]))
        bibdoi = (e.get("doi") or "").lower().strip()
        if bibdoi and best.get("doi") and best.get("by_doi") is None and bibdoi != best["doi"].lower() and not any(
                (c.get("doi") or "").lower() == bibdoi for c in cands):
            verdict = "CHECK"; issues.append(f"DOI {bibdoi} not found; matching record has {best['doi']}")
        bibvenue = " ".join(e.get(k, "") for k in ("journal", "booktitle"))
        cb = canon_venue(bibvenue)
        cf = [canon_venue(t4[4].get("venue")) for t4 in scored if t4[1] >= 0.93]
        cf = [c for c in cf if c]
        if cb and cf and cb not in cf and not re.search(r"arxiv|corr", bibvenue, re.I):
            verdict = "CHECK"; issues.append(f"venue {cb} in the bib, but the matching records say {sorted(set(cf))}")
        if re.search(r"arxiv|corr", bibvenue + e.get("eprint", "") + e.get("note", ""), re.I) and peer:
            p = peer[0][4]
            issues.append(f"cited as arXiv/CoRR but a published version exists: {p['venue']} {p['year']} (doi {p.get('doi')})")
            verdict = "CHECK"
        elif year and year > THIS_YEAR:
            verdict = "CHECK"; issues.append(f"future year {year}")
    elif s >= 0.85 and a_ok and y_ok:
        verdict = "CHECK"; issues.append(f"title differs from the record (similarity {s:.2f}): '{best['title'][:120]}'")
    elif s >= 0.75:
        verdict = "SUSPECT"; issues.append(f"closest title (similarity {s:.2f}): '{best['title'][:110]}'")
    else:
        verdict = "NOT_FOUND"; issues.append(f"best similarity {s:.2f}: '{best['title'][:90]}'")
    found = {k: best.get(k) for k in ("src", "title", "year", "venue", "doi", "id")}
    found["authors"] = best.get("authors", [])[:6]
    return {"verdict": verdict, "similarity": round(s, 3), "issues": issues, "found": found,
            "abstract": (best.get("abstract") or "")[:2500]}


def url_fallback(e, r):
    """Venues that Crossref/OpenAlex index poorly (CIDR, workshops, reports): open the entry's URL and look for
    the title on the landing page or in the first page of the PDF."""
    url = entry_url(e)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read(8_000_000); ctype = resp.headers.get("Content-Type", "")
    except Exception as ex:
        r["issues"].append(f"URL fallback failed: {str(ex)[:80]}"); return r
    text = ""
    if data[:4] == b"%PDF" or "pdf" in ctype:
        try:
            import fitz
            doc = fitz.open(stream=data, filetype="pdf")
            text = " ".join(doc[i].get_text() for i in range(min(2, len(doc))))
        except Exception:
            text = ""
    else:
        text = re.sub(r"<[^>]+>", " ", data.decode("utf-8", "ignore"))
    nt, body = norm(e.get("title", "")), norm(text)
    if nt and nt in body:
        first = ascii_fold((tb.authors(e.get("author", "")) or [""])[0])
        ok_a = not first or first == "others" or first in ascii_fold(text)
        return {"verdict": "VERIFIED" if ok_a else "CHECK", "similarity": 1.0,
                "issues": ["verified from the entry's URL (not indexed by Crossref/OpenAlex)"] + ([] if ok_a else ["first author not seen on the page"]),
                "found": {"src": "url", "title": tb.plain(e.get("title", "")), "id": url}, "abstract": body[:2500]}
    r["issues"].append("title not found at the entry's URL either")
    return r


def lint(keys, bib):
    out = []  # (level, key, msg)
    seen_titles = {}
    venues = {}
    for k in keys:
        e = bib.get(k)
        if e is None:
            out.append(("ERROR", k, "cited but not defined in any .bib (prints as [?] in the PDF)")); continue
        t = e["_type"]
        for f in REQUIRED.get(t, []):
            if not e.get(f):
                if f == "author" and e.get("editor"):
                    continue
                out.append(("WARN", k, f"@{t} without '{f}'"))
        a = e.get("author", "")
        if re.search(r"\band\s+others\b|\bet\s+al\b", a, re.I):
            out.append(("WARN", k, "author list truncated ('and others'/'et al.'): give the full list (IEEE prints up to 6 names, then et al.)"))
        y = re.sub(r"\D", "", e.get("year", ""))[:4]
        if y and (int(y) > THIS_YEAR or int(y) < 1600):
            out.append(("ERROR", k, f"implausible year {y}"))
        if t == "misc" and not (e.get("url") or e.get("howpublished") or e.get("note")):
            out.append(("WARN", k, "@misc without url/howpublished: a reader cannot find it"))
        if t in ("misc", "online") and e.get("url") and not e.get("urldate") and not re.search(r"accessed", e.get("note", ""), re.I):
            out.append(("INFO", k, "web reference without access date (IEEE style: 'Accessed: Mon. DD, YYYY')"))
        bm = (e.get("_bare") or {}).get("month")
        if bm and bm.lower() not in ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec") and not bm.isdigit():
            out.append(("ERROR", k, f"month={bm} is not a BibTeX month macro: bibtex warns and drops the month; use jun/jul/sep... or braces"))
        d = e.get("doi", "")
        if d and not re.match(r"^10\.\d{4,9}/\S+$", d.replace("https://doi.org/", "")):
            out.append(("WARN", k, f"malformed DOI '{d}'"))
        nt = norm(e.get("title", ""))
        if nt and nt in seen_titles:
            out.append(("ERROR", k, f"duplicate of '{seen_titles[nt]}' (same title cited under two keys)"))
        seen_titles.setdefault(nt, k)
        v = (e.get("journal") or e.get("booktitle") or "")
        for canon, rx in VENUE_ALIASES:
            if re.search(rx, v, re.I):
                venues.setdefault(canon, {}).setdefault(re.sub(r"\s+", " ", tb.plain(v)), []).append(k)
        if re.search(r"\b(TODO|TBD|XXX|to appear|under review|submitted)\b", " ".join(str(x) for x in e.values()), re.I):
            out.append(("WARN", k, "placeholder or 'to appear/under review/submitted' text: check it is final and allowed"))
    for canon, forms in venues.items():
        if len(forms) > 2:
            listing = "; ".join(f"'{f}' ({', '.join(ks[:3])})" for f, ks in list(forms.items())[:5])
            out.append(("INFO", "-", f"{canon} written {len(forms)} ways: {listing} -- use one form (IEEE abbreviations)"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper"); ap.add_argument("--out", required=True)
    ap.add_argument("--compile", action="store_true", help="compile a scratch copy and use .aux for the cited keys")
    ap.add_argument("--offline", action="store_true"); ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    main_tex = tb.find_main(a.paper); root = os.path.dirname(main_tex)
    text, files = tb.expand(main_tex)
    keys = tb.cited_keys(text)
    comp = tb.compile_scratch(root, main_tex) if a.compile else None
    extra = []
    if comp:
        aux_keys = []
        for m in re.finditer(r"\\citation\{([^}]*)\}", comp["aux"]):
            for k in m.group(1).split(","):
                if k.strip() and k.strip() not in aux_keys:
                    aux_keys.append(k.strip())
        aux_keys = [k for k in aux_keys if not k.startswith("IEEEexample:")]  # IEEEtran's BSTcontrol entry
        if aux_keys:
            keys = aux_keys
        for m in re.finditer(r"Warning--(.*)", comp["blg"]):
            extra.append(("WARN", "bibtex", m.group(1).strip()))
        for m in re.finditer(r"Citation `([^']+)' .*undefined", comp["log"]):
            extra.append(("ERROR", m.group(1), "undefined citation in the LaTeX log"))
    bib = {}
    for b in tb.bib_files(text, root):
        if os.path.exists(b):
            for k, v in tb.parse_bib(b).items():
                bib.setdefault(k, v)
        else:
            extra.append(("ERROR", os.path.basename(b), "bibliography file named in \\bibliography is missing"))
    if "*" in keys:
        keys = [k for k in keys if k != "*"] + [k for k in bib if k not in keys]
    findings = extra + lint(keys, bib)

    cache_p = os.path.join(a.out, "ref_cache.json")
    cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
    results = {}

    def work(k):
        e = bib.get(k)
        if e is None:
            return k, {"verdict": "ERROR", "issues": ["missing from .bib"]}
        sig = norm(e.get("title", "")) + "|" + e.get("year", "") + "|" + e.get("doi", "") + "|" + e.get("author", "")[:60]
        if k in cache and cache[k].get("_sig") == sig:
            return k, cache[k]
        if e["_type"] in ("misc", "online", "manual", "software") and entry_url(e) and not e.get("doi") and not arxiv_id(e) and not re.search(
                r"arxiv", (entry_url(e) or "") + e.get("howpublished", "") + e.get("note", ""), re.I):
            st = url_status(entry_url(e)) if not a.offline else None
            r = {"verdict": "WEB", "issues": [] if st in (200, 301, 302, None) else [f"URL returns HTTP {st}"], "url_status": st}
            if a.offline is False and st not in (200, 301, 302):
                r["verdict"] = "CHECK"
        elif a.offline:
            r = {"verdict": "SKIPPED", "issues": ["offline"]}
        else:
            r = judge(k, e, lookup(e))
            if r["verdict"] in ("NOT_FOUND", "SUSPECT") and entry_url(e):
                r = url_fallback(e, r)
        r["_sig"] = sig
        return k, r
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for k, r in ex.map(work, keys):
            results[k] = r; cache[k] = r
    json.dump(cache, open(cache_p, "w"), indent=1, ensure_ascii=False)

    rows = []
    for k in keys:
        e = bib.get(k, {}); r = results[k]
        rows.append({"key": k, "type": e.get("_type"), "file": e.get("_file"), "line": e.get("_line"),
                     "title": tb.plain(e.get("title", "")), "authors": tb.authors(e.get("author", ""))[:6],
                     "year": e.get("year"), "venue": tb.plain(e.get("journal") or e.get("booktitle") or e.get("howpublished") or ""),
                     "doi": e.get("doi"), "url": e.get("url"), **{x: r.get(x) for x in ("verdict", "similarity", "issues", "found", "abstract", "url_status")}})
    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    json.dump({"paper": os.path.abspath(a.paper), "cited": len(keys), "counts": counts, "lint": findings, "refs": rows},
              open(os.path.join(a.out, "refcheck.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(a.out, "refcheck.md"), "w") as f:
        f.write(f"# Reference check: {a.paper}\n\nCited entries: {len(keys)}. Verdicts: {counts}\n\n## Format lint\n\n")
        for lv, k, m in findings:
            f.write(f"- {lv} `{k}`: {m}\n")
        f.write("\n## Online verification (entries that need attention first)\n\n| key | verdict | sim | bib | found | issues |\n|---|---|---|---|---|---|\n")
        order = {"ERROR": 0, "NOT_FOUND": 1, "SUSPECT": 2, "CHECK": 3, "WEB": 4, "SKIPPED": 5, "VERIFIED": 6}
        for r in sorted(rows, key=lambda r: order.get(r["verdict"], 9)):
            fd = r.get("found") or {}
            f.write(f"| {r['key']} | {r['verdict']} | {r.get('similarity') or ''} | {r['title'][:70]} ({r['year']}, {r['venue'][:30]}) "
                    f"| {(fd.get('title') or '')[:60]} ({fd.get('year')}, {(fd.get('venue') or '')[:30]}) | {'; '.join(r.get('issues') or [])[:200]} |\n")
    print(f"cited={len(keys)} verdicts={counts}")
    if SOURCE_ERRORS:
        print(f"NOTE  source errors during lookup ({len(SOURCE_ERRORS)}), e.g. {SOURCE_ERRORS[0]}: NOT_FOUND rows may be caused by the outage; re-run later")
    for lv, k, m in findings:
        if lv in ("ERROR", "WARN"):
            print(f"{lv:5} {k}: {m}")
    for r in rows:
        if r["verdict"] in ("ERROR", "NOT_FOUND", "SUSPECT", "CHECK"):
            print(f"{r['verdict']:9} {r['key']}: {'; '.join(r.get('issues') or [])[:220]}")
    bad = any(lv == "ERROR" for lv, _, _ in findings) or any(r["verdict"] in ("ERROR", "NOT_FOUND", "SUSPECT") for r in rows)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
