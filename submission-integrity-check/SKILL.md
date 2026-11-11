---
name: submission-integrity-check
description: "Final pre-submission gate for a LaTeX paper: (1) the must-follow items of the venue's call (ICDE 2027 profile: IEEEtran conference template, 12 body pages excluding references and the AI-generated-content declaration, no appendix, PDF <= 20 MB, US Letter, single-blind author block, mandatory AI declaration naming the system and sections, EAB title tag, public artifact URL, no negative spaces/margin/font hacks, no unresolved ?? or [?], embedded fonts); (2) reference format (IEEE numeric, required fields, full author lists, years, duplicates, venue spellings, arXiv entries that have a published version); (3) reference EXISTENCE, checking every cited entry online against Crossref, OpenAlex, arXiv and the entry's own URL, with verdicts VERIFIED/CHECK/SUSPECT/NOT_FOUND to catch invented or mangled references; (4) citation ACCURACY, a worksheet that puts every citing sentence next to the cited work's record and abstract so each claim is judged OK/IMPRECISE/WRONG. Use before every submission, replacement upload or camera-ready (投稿前最终核查 / 合规检查 / 页数限制 / 参考文献核查 / 参考文献是否真实存在 / AI 编造文献 / 引用是否准确 / 引用格式), together with submit-icde, icde-cmt-submission, manuscript-proofcheck and manuscript-writing-review."
---

# Submission integrity check

A last gate that answers four questions about the PDF that will actually be uploaded:

1. Does it follow every must-follow item of the call? (desk-reject risks)
2. Is every reference correctly formatted?
3. Does every cited work exist, with the title, authors, year and venue the bib entry gives?
   (AI-written drafts invent references or merge two real ones.)
4. Does every sentence that cites a work describe that work correctly?

Built on 2026-11-11 for four ICDE 2027 Round 2 submissions. The ICDE rules were re-read that day from the official
pages (see `references/icde2027-must-follow.md`).

## Inputs

- The LaTeX source folder that produced the PDF: main file, `\input` chain, `.bib`.
- The exact PDF that will be uploaded.
- The venue profile (`profiles/icde2027.json`). Add a profile for another venue by copying it and editing the values from that venue's call.
- Network access to `api.crossref.org`, `api.openalex.org` and `export.arxiv.org`. DBLP and Semantic Scholar often block scripts, so they are not used.

## Workflow

Write all outputs into a scratch folder per paper. Never edit the source before the report is written.
Never delete anything: write a new output folder for each run instead of removing an old one.

1. **Compliance.**
   ```bash
   python3 scripts/compliance_check.py <src_dir> --pdf <upload.pdf> --profile icde2027 [--eab] --out <out>
   ```
   Rules C01–C12 are listed in `references/rules.md`. Every ERROR is a desk-reject risk and must be fixed.
   WARN items are explained in the report: either fix them, or say why they are fine.
   Also run the venue checker of `submit-icde` (`check_icde_submission.py`) when it is installed. It covers the CMT side and the remaining call rules.

2. **References: format and existence.**
   ```bash
   python3 scripts/ref_check.py <src_dir> --out <out> [--compile]
   ```
   - Use `--compile` when a TeX engine is installed. It compiles a scratch copy and takes the cited keys from the `.aux`, and bibtex and LaTeX warnings from the `.blg` and `.log`. The source folder is not touched.
   - Results are cached in `<out>/ref_cache.json`, so a re-run only queries changed entries.
   - What to do with each verdict:
     - `VERIFIED`: title (similarity ≥ 0.93), first author and year (±1) match a Crossref, OpenAlex, arXiv or URL record.
     - `CHECK`: the work exists, but a field differs. Examples: the title wording, a year, the first author, a venue (ICLR vs NeurIPS), a DOI, or an arXiv citation that now has a published version. Fix the entry from the record and cite the published version.
     - `SUSPECT`: there is only a weak title match. Open the closest record and decide whether the entry is a garbled version of it or invented.
     - `NOT_FOUND`: there is no candidate. Treat the entry as possibly invented until a person finds the source through the publisher, DBLP in a browser, or Google Scholar.
       - If the source is found, correct the entry and add its DOI or URL, so the next run verifies it.
       - If it is not found, remove the citation and rewrite the sentence.
     - `WEB`: software, datasets and web pages. Only URL reachability is checked; the IEEE style also wants an access date.
   - The script is a filter, not a judge.
     - Read every non-VERIFIED row yourself.
     - Spot-check a few VERIFIED rows: open the record and confirm it is the same work, not a namesake.

3. **Citation accuracy.**
   ```bash
   python3 scripts/cite_contexts.py <src_dir> --refcheck <out>/refcheck.json --out <out>/cite_worksheet.md
   ```
   - The worksheet shows, for every cited work, the record that was found, its abstract, and every sentence of the paper that cites it.
   - Give each work a verdict:
     - `OK`;
     - `IMPRECISE`: right work, wrong detail (a number, a year, "first"/"only", the method, the venue);
     - `WRONG`: the cited work does not say this, or a different work is meant;
     - `UNSURE`: the abstract is not enough.
   - For `UNSURE`, and for **every number attributed to another paper** (speed-ups, accuracies, sizes), open the paper itself before deciding.
   - Long worksheets: give each paper's worksheet to one subagent. Give it the worksheet path and the rule "verdict + one-line reason + suggested fix for each non-OK claim". Do not give it your expectations.

4. **Fix and re-run.**
   - Correct the bib entries and the sentences with minimal edits, recompile, and re-run steps 1–3 until all of the following hold:
     - no ERROR remains;
     - no NOT_FOUND or SUSPECT remains;
     - every CHECK is fixed;
     - every claim is OK.
   - Then run the paper's own gates again (`manuscript-writing-review`, `manuscript-proofcheck`, `results-presentation-review`, `icde-cmt-submission`), because the PDF changed.
   - Write the new PDF under a new file name and keep the old one.

5. **Report** (for the author, in the author's language). Write one row per paper:
   - compliance (each rule);
   - reference counts per verdict;
   - each fixed entry: old text, new text, and the source of the correction;
   - each citation claim changed, with the reason;
   - what was not checked;
   - the new PDF path and SHA-256.

   Keep it separate from any submission material.

## Known limits

- **Venues that Crossref and OpenAlex index poorly** (CIDR, workshops, technical reports, very recent papers): these are verified through the entry's own URL. Add a `url` or `doi` to such entries.
- **Title similarity alone cannot tell two real papers with the same title apart.** The first author and the year disambiguate them.
- **Abstracts are missing for some records** (Crossref often has none). The worksheet says so; open the paper.
- **The page counter reads the PDF's text.** A body that ends in a float-only column, or a references heading that is an image, needs a visual check of the last body page.

## Lessons (2026-11-11, four ICDE 2027 papers)

- Typical defect found in otherwise clean bib files: a title word changed by a hand-copied entry ("RouteLLM: Learning to Route LLMs **from** Preference Data" vs the published "**with** Preference Data"). Only an online check catches this.
- Crossref keeps the part of a PVLDB title after the colon in `subtitle`. The checker joins them; without that, real PVLDB papers came out NOT_FOUND.
- Free-text Crossref and OpenAlex search sometimes returns noise for one query. The checker therefore also runs a title-only query and several arXiv queries before giving up.
- A NOT_FOUND on the first run is not proof of invention. Re-run it, then search by hand.

### Defects the first run found in four papers that had already passed every other gate

- **Wrong author order:** the CIDR paper's author line reads Kossmann, Lindner, Naumann, Papenbrock; the bib had Naumann before Lindner. The checker compares the order with the record.
- **Wrong title of an arXiv preprint:** the bib said "Text2GQL-Bench: A Text to Graph Query Language Benchmark", but arXiv 2602.11745 is titled "Text2GraphQuery-Bench: A Text to Graph Query Benchmark". The checker looks up the entry's own arXiv id.
- **A preprint cited although the journal version exists:** the bib cited arXiv 1003.3967 (2017) instead of JAIR 42:427-486 (2011).
- **Bare month names:** `month=June`, `month=Sept` and `month=July` are not BibTeX macros, so bibtex warns and silently drops the month. Use `jun`, `sep` and `jul`.

### What the citation-accuracy pass found (about 260 citations, after every other gate had passed)

- **One WRONG citation.** A claim that "experiments find simple traversal competitive" cited a study that concludes the opposite: BFS/DFS are "far from competitive". The competitive result belongs to the earlier studies that this study re-examined. Typical cause: the cited paper's related-work summary is mistaken for its finding.
- **27 IMPRECISE citations.** The typical patterns were:
  - a broader contribution attributed to a tool (a dependency profiler said to find keys);
  - an error statistic attributed to a benchmark that never reports it;
  - an RDF/SPARQL study cited as if it used property graphs;
  - a number from the introduction of a paper presented as a measured result;
  - a term of art attributed to a book that does not use it;
  - five different systems grouped under one technique (2-hop labels).
- **Ten arXiv citations of papers that have peer-reviewed versions** (ICLR, ICML, PVLDB, JAIR, EMNLP, workshops).
- **Proceedings titles can differ from arXiv titles.** RouteLLM is "...from Preference Data" at ICLR 2025 but "...with Preference Data" on arXiv. Before "fixing" a CHECK title, confirm which version the entry cites.

### False alarms the checker now avoids

- IEEE Xplore records whose year is the indexing date (2002) rather than the conference year (2000/1997): the year check is skipped when the DOI is identical.
- An "et al." match inside a surname (Hi**etal**a).
- CJK name order in OpenAlex ("LI Yufei"): authors are matched on full names.
- Author-order false positives (15 in one paper): a short surname such as "Li" matched inside another name ("Lin", "Oliveira"). Surnames are now matched as whole words, and each record author is used at most once.
- Titles with accents or symbols ("KÙZU∗ Graph ..."): symbols become spaces and accents are folded before comparison, so the URL fallback finds the title in the PDF.
- A URL that prints an underscore as a rule (url.sty) copies as "n1 kg eab" from the PDF. The compliance check now reaches the paper's own repository link, and this defect was found in an already submitted PDF.

### Source outages

OpenAlex has a free daily budget per IP; it was exhausted after about 300 lookups. The checker reports source errors ("NOTE source errors ...") instead of turning them into silent NOT_FOUND verdicts. Re-run the next day or with an OpenAlex key, and verify the remaining rows by hand: publisher page, DBLP in a browser, a web search.
