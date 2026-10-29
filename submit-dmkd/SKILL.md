---
name: "submit-dmkd"
description: "Submission guide for the Springer journal Data Mining and Knowledge Discovery (DMKD, ISSN 1384-5810 / 1573-756X). Use before submitting, resubmitting or transferring a manuscript to DMKD (投稿 DMKD / 改投 DMKD): article-type choice, scope and research-gap test, Springer Nature sn-jnl LaTeX template with author-year sn-basic references, abstract 150-250 words, 4-6 keywords, mandatory Statements and Declarations, LLM disclosure in Methods, single-anonymous review, the Snapp portal (submission.springernature.com) and its LaTeX zip rules. Includes a checker for the LaTeX folder and a builder for the Snapp upload package."
---

# Submit to Data Mining and Knowledge Discovery (投稿 DMKD 指南)

Use this skill whenever a manuscript is prepared for, moved to, or resubmitted at **Data Mining and Knowledge Discovery** (Springer, journal no. 10618). Do not confuse it with the ECML PKDD journal track, which is a separate route into the same journal (see "ECML PKDD journal track").

Status tags used below:
- **[VERIFIED]** read on an official DMKD or Springer page on 2026-10-29 (sources in `references/guide-digest.md`);
- **[SN]** Springer Nature-wide policy that applies to DMKD;
- **[INFERRED]** conclusion drawn from the evidence, not stated anywhere;
- **[UNKNOWN]** only visible after login or not published.

Re-read the submission guidelines when this file is more than six months old and update `references/verification-log.md`.

## Language convention (permanent agreement with the author)
- **English** for everything reviewers, editors or the portal see: manuscript, cover letter, declarations, supplementary README files, every value typed into Snapp, responses to reviewers.
- **Chinese (中文)** for every report to the author: progress, check results, step-by-step portal instructions, decisions, internal notes and package READMEs.

## Workflow
1. **Choose the article type** (below) and pass the research-gap test in writing.
2. **Port to sn-jnl** with `assets/dmkd_skeleton.tex`: `\documentclass[pdflatex,sn-basic]{sn-jnl}`, author-year citations, one flat `.tex`.
3. **Write the Statements and Declarations** block and the LLM disclosure in the Methods/experimental section.
4. **Run the checker**: `python3 scripts/check_dmkd_submission.py <folder> --main main.tex --forbid 'Information Systems|elsarticle|OLDCODE'`. Fix every ERROR, read every WARN.
5. **Compile with pdflatex** (TeX Live 2021 or newer, or Overleaf with the pdfLaTeX compiler). Snapp recompiles the zip itself; a file that fails there is returned.
6. **Build the upload package**: `python3 scripts/build_snapp_package.py <folder> --main main.tex --out <upload_dir>`; it writes a flat LaTeX zip, a manifest with SHA-256 hashes and a list of the files Snapp needs.
7. **Run the `review-dmkd` skill** (independent reviewer and action-editor pass) before the portal step.
8. **Portal pass** with the author using `references/snapp-walkthrough.md`. Never click Submit, accept policies, pick open access or pay on the author's behalf.

## Article types [VERIFIED]
Select the type in the portal. Each type has its own criteria:
- **Regular Paper.** (i) The main contribution is clear from the abstract. (ii) The motivation is a clearly defined research gap; "it is typically not enough that a paper presents a new method". (iii) Success is shown by experiments that answer clearly formulated research questions, or by formal proofs. Extended conference papers go here.
- **Survey Paper.** Includes "extensive independent experimental comparisons of different competing approaches to a problem class". Judged on comprehensiveness, balance and novel insight; a concatenation of summaries is not of interest.
- **Application Paper.** Comparing well-known algorithms on a newly collected dataset "is not sufficiently interesting for data mining researchers".
- **Special-issue contribution** (only for an open call) and **Editorial** (guest editors).

There is no benchmark or datasets article type. An audit or evaluation-methodology paper with a new procedure is a **Regular Paper**; a large independent experimental comparison is a **Survey Paper** [INFERRED].

### Scope and research-gap test (desk-rejection risk)
The editor-in-chief screens first, typically within two weeks [VERIFIED]. Answer each in one sentence before submitting, and make the answers visible in the abstract and introduction:
1. Which part of the knowledge discovery process does the paper address? The aims and scope list "data pre-processing for data mining, including data cleaning", "evaluating, consolidating, and explaining discovered knowledge" and "data mining systems and tools".
2. What is the research gap that existing methods cannot address? State it as a gap, not as "we propose".
3. Which research questions do the experiments answer, and on which datasets or systems?
4. Why would data-mining researchers, not only database or software-engineering readers, change what they do? Name DMKD, KDD, ECML PKDD, ICDM, SDM or NeurIPS Datasets and Benchmarks papers the work speaks to.
5. How can a reader reproduce it (code and data repository with a persistent identifier)?

## Peer review [VERIFIED]
Single-anonymous: keep author names and affiliations on the manuscript. Hierarchical: the editor-in-chief (Eyke Hüllermeier, LMU Munich, in 2026) assigns an action editor, who invites reviewers. Regular review usually takes 1-3 months; acceptance after the first round is "very rare", and accepted papers often go through two or three rounds. Reviews are not published.

## Manuscript format
| Item | Rule | Tag |
|---|---|---|
| Template | Springer Nature LaTeX template (December 2024, sample v3.1): `\documentclass[pdflatex,sn-basic]{sn-jnl}`; no `Numbered` option. Word is also accepted. | [VERIFIED] |
| Compiler | pdflatex; Snapp compiles with TeX Live 2021 | [SN] |
| Files | One `.tex` file, no `\input`/`\include`; no subfolders; figures referenced by local file name; no custom fonts; diacritics as TeX codes | [VERIFIED]/[SN] |
| Title page | Concise informative title; full author names; affiliations with department, institution, city, state, country; corresponding author with active email; 16-digit ORCID if available | [VERIFIED] |
| Abstract | 150-250 words, no undefined abbreviations, no citations | [VERIFIED] |
| Keywords | 4-6 | [VERIFIED] |
| Headings | Decimal numbering, at most three levels | [VERIFIED] |
| Length | No page limit for regular papers | [VERIFIED] |
| Citations | Author-year in parentheses, e.g. "(Thompson 1990)", "Becker and Seligman (1996)"; use `\citep`/`\citet` | [VERIFIED] |
| Reference list | Alphabetical, Springer basic style, full DOI links; abbreviate journal names (ISSN LTWA); cite datasets and software with persistent identifiers | [VERIFIED] |
| Figures | Vector (PDF/EPS) for line art; 1200 dpi line art, 300 dpi halftones; fonts embedded; 8-12 pt sans-serif lettering; no titles inside figures; width 84 mm or 174 mm, height up to 234 mm; colour plus patterns; caption starts "Fig. 1" | [VERIFIED] |
| Tables | Arabic numbering, cited in order, caption above; table footnotes with superscript lower-case letters | [VERIFIED] |
| Supplementary files | Cited as "Online Resource 1"; name files ESM_1.pdf, ESM_2.zip; each file carries title, journal, authors and corresponding email | [VERIFIED] |
| Line numbers | Not required; the class option `lineno` helps reviewers | [INFERRED] |
| Acknowledgements | `\bmhead{Acknowledgements}` in `\backmatter`; funders written in full | [VERIFIED] |

The sample `sn-article.tex` ships with the numbered `sn-mathphys-num` option: always change it to `sn-basic`. Without bibtex, write the bibliography as a natbib-compatible `thebibliography` with entries `\bibitem[{Author et~al.(2015)}]{key}` in sn-basic format (this is what pasting the `.bbl` produces); otherwise ship `.bib` + `sn-basic.bst` and paste the generated `.bbl` before upload.

## Statements and Declarations [VERIFIED]
Required before the reference list; "submissions that do not include relevant declarations will be returned as incomplete". Use `\section*{Statements and Declarations}` after `\backmatter` with these paragraphs (write "Not applicable" when a heading does not apply):
- **Funding** (also entered in the portal): "This work was supported by … (Grant numbers …)" or "No funding was received for conducting this study."
- **Competing interests** (also entered in the portal; only the portal version is published): financial and non-financial interests of the last three years, including employment and editorial-board roles. Default wording: "The authors have no competing interests to declare that are relevant to the content of this article."
- **Ethics approval and consent to participate**; **Consent for publication**.
- **Data availability** (mandatory for original research; SN standard data policy): repository, persistent identifier, and the access conditions of anything not shared. Reviewers may request data and code.
- **Materials availability**; **Code availability**.
- **Author contributions** (also entered in the portal): free text or CRediT roles.

### LLM and AI use
- DMKD page: LLMs are not authors; "Use of an LLM should be properly documented in the Methods section"; AI-assisted copy editing (grammar, style, tone) need not be declared [VERIFIED].
- SN risk framework: extensive writing support, method suggestions or analysis assistance are permitted with human oversight and disclosure; fabricated data or hallucinated citations are prohibited [SN].
- Practice: describe AI tools used in the research pipeline in the experimental-setup section, and add one sentence in the Methods (or the closest equivalent section) for writing and code assistance beyond copy editing. A repeat in the Declarations is optional.

## Prior versions, preprints and transfers
- Simultaneous submission elsewhere is not allowed [VERIFIED].
- Extended conference papers: declare at submission, cite the conference paper, and add a statement of revisions; there is no fixed percentage of new material [VERIFIED].
- arXiv preprints are allowed; give the preprint DOI and licence at submission and link the published version later [VERIFIED]/[SN].
- A paper rejected by another publisher's journal carries no DMKD restriction. Do not describe it as a resubmission; revise it substantively and address the earlier criticism in the paper itself [INFERRED].
- ECML PKDD journal-track rejections cannot be resubmitted to a later track deadline but may come back as regular papers [VERIFIED].

## Required files for Snapp
| File | Rule |
|---|---|
| LaTeX source zip | Flat zip: `main.tex`, `sn-jnl.cls`, `sn-basic.bst` (if bibtex is used), `.bib` or pasted `.bbl`, all figure files. Must compile with pdflatex. |
| Compiled PDF | Upload with the source; Snapp also builds its own PDF for peer review |
| Cover letter | One page is advised; title, what was done and found, why it suits DMKD; suggested reviewers with institutional email and ORCID/Scopus ID; prior-version statement if any |
| Figures | Inside the zip; separate figure uploads only if the portal asks |
| Supplementary material | ESM_n files, or a persistent repository cited in the Data availability statement |

`scripts/build_snapp_package.py` assembles and checks this set. The `.cls` is Springer's file: ship it inside the manuscript zip, but do not commit it to public repositories; download it from https://www.springernature.com/gp/authors/campaigns/latex-author-support.

## Fees and copyright [VERIFIED]
Hybrid journal. The subscription route is free (exclusive licence to Springer). Open access (Open Choice) is chosen after acceptance: GBP 2390 / USD 3390 / EUR 2790 plus VAT, CC BY 4.0 or CC BY-NC-ND 4.0. Colour online is free. In 2026 the China transformative-agreement list contains essentially no mainland universities; check eligibility per institution.

## ECML PKDD journal track (separate route)
Submission through both CMT and Snapp with the "ECMLPKDD <year>" collection, ≤20 pages recommended (>23 desk reject), a two-page cover letter answering fixed questions, no conference extensions, no surveys, presentation at the conference required. For a regular submission, never select an ECML PKDD collection.

## Final checklist
- [ ] Article type chosen; research gap and research questions explicit in abstract and introduction.
- [ ] `sn-jnl` with `pdflatex,sn-basic`; single flat `.tex`; compiles with pdflatex; no `??` or undefined citations.
- [ ] Abstract 150-250 words without citations; 4-6 keywords.
- [ ] Author-year citations; alphabetical list; DOIs; datasets and software cited with persistent identifiers.
- [ ] Statements and Declarations complete; same text as the portal entries for funding, competing interests and author contributions.
- [ ] LLM use documented in the Methods/experimental section.
- [ ] Figures vector, fonts embedded, readable at 174 mm width; captions "Fig. n".
- [ ] No leftovers from the previous journal (journal name, `elsarticle`, highlights, CRediT-only headings, Elsevier AI heading).
- [ ] Cover letter one page; suggested reviewers independent, from several countries, with institutional emails.
- [ ] `review-dmkd` pass completed and its blocking issues fixed.
