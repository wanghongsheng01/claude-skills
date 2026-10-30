---
name: "submit-dse"
description: "Submission guide for the Springer journal Data Science and Engineering (DSE, ISSN 2364-1185 / 2364-1541, CCF B, official journal of the CCF Technical Committee on Database). Use before submitting, resubmitting or transferring a manuscript to DSE (投稿 DSE / 改投 DSE): scope test, double-blind anonymization, separate title page, sn-jnl LaTeX with numeric citations, abstract 150-250 words, 4-6 keywords, Declarations, LLM disclosure in Methods, Online Resource supplements, Editorial Manager portal (editorialmanager.com/dsej) and APC. Includes a checker and a package builder."
---

# Submit to Data Science and Engineering (投稿 DSE 指南)

Use whenever a manuscript is prepared for, moved to or resubmitted at **Data Science and Engineering** (Springer Nature, journal no. 41019). Do not confuse it with *Data & Knowledge Engineering* (DKE, Elsevier).

Status tags:
- **[VERIFIED]** read on the official DSE or Springer page on 2026-10-30 (`references/guide-digest.md`);
- **[OBSERVED]** counted in 39 published DSE articles (`write-dse/references/dse_paper_survey.csv`);
- **[INFERRED]** conclusion from the evidence, not stated anywhere;
- **[UNKNOWN]** only visible after login.

Re-read the guidelines when this file is more than six months old and update `references/verification-log.md`.

## Language convention (permanent agreement with the author)
**English** for everything reviewers, editors or the portal see. **Chinese (中文)** for every report, plan and instruction to the author.

## Workflow
1. **Scope test** (below), in writing.
2. **Port to sn-jnl**: `\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}`, one flat `.tex`.
3. **Anonymize** the manuscript and every supplement (below). This is the step authors from single-blind journals forget.
4. **Write the separate title page** from `assets/title_page_template.md`.
5. **Document LLM use** in the Methods section of the manuscript.
6. **Run the checker**: `python3 scripts/check_dse_submission.py <folder> --main main.tex --forbid 'AuthorName|Institution|email'`.
7. **Compile with pdflatex** (or Tectonic for a local check) and fix every error; Editorial Manager recompiles and returns an error log on failure.
8. **Build the package**: `python3 scripts/build_em_package.py <folder> --main main.tex --out <upload_dir>`.
9. **Run `review-dse`** and fix blocking issues.
10. **Portal pass** with the author, `references/portal-walkthrough.md`. Never click Submit, accept terms, choose payment or apply for a waiver on the author's behalf.

## Scope test [VERIFIED]
DSE covers "(i) the data itself, i.e., the nature and quality of the data, especially big data; (ii) the principles of information extraction from data; (iii) the theory behind data-intensive computing; and (iv) the techniques and systems used to analyze and manage big data". Answer in one sentence each, and make the answers visible in the abstract and introduction:
1. Which of the four areas and which listed topic does the paper address?
2. Which gap does it fill? Published abstracts state it directly ("they lack mechanisms for ...; to address this gap, we present ...").
3. What is the artefact: framework, system, algorithm, benchmark or experimental study?
4. What does the evaluation show, on which data?

Article labels seen on the journal site: Research Papers, Review/Survey, Editorial. No separate benchmark or experiments category exists [OBSERVED]; an audit or evaluation-methodology paper is a Research Paper [INFERRED].

## Peer review [VERIFIED]
**Double-blind.** "It is the responsibility of the author to anonymize the manuscript and any associated materials." Median submission to first decision: 26 days (journal home page, 2026-10-30). Editors-in-Chief: Elena Ferrari (University of Insubria), Xuan Zhou (East China Normal University). Authors may suggest and exclude reviewers.

### Anonymization checklist [VERIFIED rule; INFERRED details]
- No author names, affiliations, emails, ORCID, funding, acknowledgements or disclosures in the manuscript or its supplements; they go on the title page.
- Self-citation only in the third person, and not in a way that reveals identity.
- Supplements: remove README author lines, `CITATION.cff`, `LICENSE` copyright holders, `.zenodo.json`, user names in paths, git metadata and PDF metadata. Regenerate any hash a change invalidates.
- Repositories: the Research Data Policy "strongly" suggests blinded authorship for data given to reviewers. Do not cite a public DOI that shows the authors. Upload a blinded copy as Online Resource and restore the DOI at the revision after acceptance.
- Reused title: if a public deposit or preprint carries the same title and the authors' names, a title search breaks the blinding. Change the title or accept the risk knowingly.
- Do not write "our earlier work [12]" where [12] is the authors' own.

## Manuscript format
| Item | Rule | Tag |
|---|---|---|
| Template | Springer Nature LaTeX template (December 2024) is recommended for mathematical content; Word otherwise | [VERIFIED] |
| Source files | Editable sources are mandatory at every submission and revision, or "your article [will] not [be] considered for review" | [VERIFIED] |
| Title | Concise and informative | [VERIFIED] |
| Abstract | 150-250 words; no undefined abbreviations or unspecified references (up to 450 only if the topic dictates) | [VERIFIED] |
| Keywords | 4-6 | [VERIFIED] |
| Headings | Decimal, at most three levels | [VERIFIED] |
| Citation style | The generic guideline text shows author-year, but **39/39 sampled articles print numeric citations**. Use numbers, `sn-mathphys-num`. Production re-typesets references | [VERIFIED]/[OBSERVED] |
| Reference list | Alphabetize by first author's last name; full DOI links; LTWA journal abbreviations; only published or accepted works | [VERIFIED] |
| Footnotes | Not reference-only; table footnotes with superscript lower-case letters | [VERIFIED] |
| Tables | Arabic numerals in citation order; caption above; never rotated (author's standing rule) | [VERIFIED] |
| Figures | File names `Fig1.eps`; EPS preferred for vector, PDF works with pdflatex; fonts embedded; lines at least 0.3 pt; Helvetica/Arial lettering 8-12 pt; no title inside the figure; width 84 or 174 mm, height up to 234 mm; patterns as well as colour; lettering contrast 4.5:1; RGB | [VERIFIED] |
| Appendix figures | Continue the main numbering; do not use A1, A2 | [VERIFIED] |
| Captions | "Fig. 1" bold, no punctuation after the number or at the end of the caption | [VERIFIED] |
| Supplements | "Online Resource 1", files `ESM_1.zip`, each with a caption; normally each file carries title, journal and authors, which **must be left out under double-blind review** [INFERRED] | [VERIFIED] |
| Length | No limit stated. Observed median 7 sections, 10.9k words, 53 references | [OBSERVED] |

The guidelines say manuscripts "should be submitted in Word", and that those "with mathematical content can also be submitted in LaTeX" [VERIFIED]. Any paper with formulas qualifies.

## Title page and declarations [VERIFIED]
Upload a **separate title page** containing the title, authors, affiliations with city and country, the corresponding author's active email, 16-digit ORCID, Acknowledgements, and a section "Declarations": Funding, Competing interests, Ethics approval, Consent, Data, Materials and/or Code availability, and Authors' contribution statements. The wording of the guidelines differs by section ("Statements and Declarations", "Declarations"); under double-blind review they go on the title page, not in the manuscript. "Submissions that do not include relevant declarations will be returned as incomplete."

The manuscript keeps a blinded `Data availability` paragraph that points to the Online Resource [INFERRED; 16/39 sampled articles print a data availability section].

Competing interests cover the 3 years before the work began: funding, employment including multiple affiliations, financial and non-financial interests.

## LLM use [VERIFIED]
LLMs are not authors. "Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part)." AI-assisted copy editing need not be declared; generative editorial work and autonomous content creation are outside that exception. Keep the statement factual, in the methods or procedure section, and tool-specific.

## Prior versions and simultaneous submission [VERIFIED]
- Submission "implies ... that it is not under consideration for publication anywhere else". The manuscript "should not be submitted to more than one journal for simultaneous consideration". **Check this gate first: if the same core results are under review at another journal, withdraw or wait for the decision before the portal step.**
- A rejection elsewhere carries no restriction and need not be declared, but re-use of material must be transparent in the cover letter.
- Salami-slicing is prohibited: one study may not be split across journals or over time.
- The journal may screen with plagiarism software.

## Required files for Editorial Manager
| File | Rule |
|---|---|
| Title page | Separate, not blinded (`.docx`) |
| Blinded manuscript | LaTeX: `main.tex`, `sn-jnl.cls`, `.bst` if bibtex is used, all figures; compiled PDF as a check |
| Cover letter | Title; what was done and found; why DSE; non-simultaneity; suggested and excluded reviewers with institutional emails or homepages |
| Online Resource | `ESM_1.zip`, blinded |

Item types and order are only visible after login [UNKNOWN]: record them in `references/portal-walkthrough.md` the first time the portal is used.

## Fees [VERIFIED]
Fully open access, CC BY. An APC applies to each accepted article: **GBP 940 / USD 1390 / EUR 1140** plus VAT (2026-10-30). The price is fixed at the date of acceptance. Waivers and discounts apply per country list; discretionary waivers must be requested **at the point of manuscript submission**. Check whether the institution has a Springer agreement. Budget this before submitting.

## Final checklist
- [ ] Simultaneous-submission gate passed.
- [ ] Scope sentences written; gap and artefact visible in the abstract.
- [ ] Manuscript and supplements blind; checker passes with `--forbid`.
- [ ] sn-jnl numeric; alphabetized references with DOIs; abstract 150-250; 4-6 keywords; no more than three heading levels.
- [ ] Figures named `FigN`, vector, fonts embedded; continuous numbering; captions without final period.
- [ ] Title page complete with Declarations; LLM use documented in Methods.
- [ ] Cover letter one page; reviewers independent, from several countries, none from the authors' institutions.
- [ ] APC budget confirmed; waiver request, if any, made at submission.
- [ ] `review-dse` pass completed.

## Lessons from use (2026-10-30)
- Blinding scan of supplements must cover logs (proxy hosts in `native.log`), JSON identity fields, temp paths, figure-script salts and stale references to other versions. A name search alone misses them.
- `textutil -convert docx page.html -output file.docx` makes the title page and cover letter on macOS without extra packages.
