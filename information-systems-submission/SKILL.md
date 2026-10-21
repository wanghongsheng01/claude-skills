---
name: "information-systems-submission"
description: "Pre-submission checklist for the Elsevier journal Information Systems (ISSN 0306-4379, CCF B, data management). Use before submitting, resubmitting or transferring any manuscript to Information Systems: scope fit, single-anonymized review, required files (highlights at submission, editable source, separate figure files), elsarticle formatting, abstract and keyword limits, research-data Option C, declarations (CRediT, competing interests, funding, generative-AI statement) and the portal steps. Includes a script that checks a LaTeX submission folder."
---

# Information Systems submission checklist (投稿前须知)

Use this skill whenever a manuscript is being prepared for, or moved to, **Information Systems** (Elsevier, ISSN 0306-4379). It is not the Wiley *Information Systems Journal* and not *Information Systems Research*; check the ISSN first.

Status tags:
- **[GUIDE]** stated in the journal's Guide for Authors or its open-access page, read in full on 2026-10-21 through Claude in Chrome (see `references/verification-log.md`);
- **[ELSEVIER]** Elsevier-wide policy referenced by the guide;
- **[CHECK]** still unconfirmed.

The Guide for Authors lives at https://www.sciencedirect.com/journal/information-systems/publish/guide-for-authors and the open-access page at https://www.sciencedirect.com/journal/information-systems/publish/open-access-options. ScienceDirect refuses WebFetch and the in-app browser, but **Claude in Chrome (the person's real Chrome) reads both pages in full** with `get_page_text`; use it when the session has it and the person agrees. Otherwise ask the person to save the page from their own browser ("Print → Save as PDF"). Do not route around the block with caches or mirrors.

## Workflow
1. **Re-read the guide** if this file is more than about six months old, and update the tags.
2. **Scope test** (desk-reject risk): answer the four questions in "Scope fit" in writing and fix title, abstract and introduction if any answer is weak.
3. **Decide the research-data route** (Option C, below) with the user before writing the data statement.
4. **Build the file set** in "Required files", one folder per submission with a manifest.
5. **Format** with elsarticle as in "Formatting".
6. **Run the checker**: `python3 scripts/check_submission.py <latex-folder> --main main.tex --highlights highlights.txt [--forbid 'OLDJOURNAL|ProjectCode']`. Fix every ERROR; read every WARN.
7. **Compile on Overleaf or a full TeX Live** (pdfLaTeX), check fonts are embedded (`pdffonts`), references resolve, and figures are legible at 100% zoom.
8. **Portal pass** with the user. Never click Submit, accept terms, choose open access or pay on the user's behalf.

## Scope fit [GUIDE]
Information systems are "the software and hardware systems that support data-intensive applications". The journal publishes the design and implementation of languages, data models, process models, algorithms, software and hardware for information systems. Subject areas include the data-management topics of SIGMOD/PODS, VLDB, ICDE and ICDT/EDBT, plus data mining and machine learning, information retrieval over structured data, internet and cloud data management, business process management, web semantics, visual and audio information systems, scientific computing and data science. It welcomes systems papers, theory papers that break new ground or unify existing algorithms, and application-domain papers with high-performance, scalable solutions.

All papers must motivate their problems with compelling examples from real or potential applications, and systems papers "must be serious about experimentation either on real systems or simulations based on traces from real systems". Industrial papers are welcome.

Before submitting, write one sentence for each:
1. Which data-intensive system, model or process does the paper study?
2. Which of the venues above would its reviewers normally publish in? Name two or three cited papers from them.
3. What is the experimental evidence, and on which real systems, datasets or traces?
4. How can a reader reproduce it?

Measurement and audit papers without a new algorithm fit when they study real systems and their conclusions help builders or evaluators. Say so plainly in the cover letter.

## Article types and reproducibility [GUIDE]
- Research articles: systems, theory, application domains.
- Experimental reproducible survey papers: must apply a substantial portion of the surveyed techniques to at least one existing benchmark and be reproducible; reproducibility validation becomes a separate paper.
- Reproducibility papers: authors of selected accepted articles are invited by the Editors-in-Chief; the reproducibility reviewers become co-authors. Guidelines: https://cs.nyu.edu/~shasha/papers/reproducibilityguidelines (Mendeley Data deposit, ReproZip or Docker).
- Retrospective articles: by invitation, written in the first person.

## Peer review [GUIDE]
**Single anonymized.** Do not anonymize the manuscript. Editors screen first; suitable papers go to at least two reviewers. One appeal per submission under Elsevier's Appeal Policy.

## Required files
| File | Rule | Status |
|---|---|---|
| Editable manuscript source | `.tex` (or `.docx`); "A PDF is not an acceptable source file". All editable source files are requested "upon submission or revision"; upload them at first submission to avoid delay | [GUIDE] |
| Compiled PDF | Upload alongside the source for reviewers | [ELSEVIER] |
| Figures as separate files | Each figure a separate file with a logical name such as `Figure_1.pdf`, `Figure_2.pdf`; vector EPS or PDF with embedded fonts; photographs 300 dpi, bitmap line drawings 1000 dpi; one figure per file | [GUIDE] |
| Highlights | **Required at submission.** Separate editable file whose file name contains "highlights"; 3–5 bullets, each at most 85 characters including spaces | [GUIDE] |
| Graphical abstract | Not mentioned in the guide, so optional | [GUIDE] |
| Declaration of competing interests | Complete Elsevier's declarations tool for every submission; upload the resulting Word file (.doc/.docx) at the attach-files step; no signatures | [GUIDE] |
| Supplementary material | Cite every supplementary file in the text with a concise caption; submit all supplements together with the manuscript; after submission they can only be changed at revision; they are published exactly as received | [GUIDE] |
| Cover letter | Contribution type, scope fit, submission history, related submissions | portal field |

## Formatting
- **Template** [GUIDE]: Elsevier's LaTeX template is encouraged; `\documentclass[preprint,12pt]{elsarticle}` with `\journal{Information Systems}` is a safe single-column layout. Double-column layout is permitted for LaTeX.
- **Title page** [GUIDE]: concise, informative title without abbreviations or formulae unless widely understood; given and family names in the same order as in the portal; affiliations with lowercase superscript letters and full postal address including country; corresponding author's e-mail on the title page; present addresses as numbered footnotes.
- **Abstract** [GUIDE]: at most **250 words**; state purpose, basic procedures, main findings and principal conclusions; stand-alone; avoid references (if essential, give author and year); define any non-standard abbreviation.
- **Keywords** [GUIDE]: **1–7**, in English; avoid multi-word keywords built with "and" or "of"; abbreviations only if firmly established.
- **Sections** [GUIDE]: numbered sections and subsections (1.1, 1.2); cross-reference by number; abstract unnumbered.
- **Math** [GUIDE]: editable equations, variables in italics, solidus for small fractions, displayed equations numbered consecutively.
- **Tables** [GUIDE]: editable text, cited in order, captions with the table, notes below the body, no vertical rules or shading, no duplication of results given elsewhere.
- **Captions** [GUIDE]: every artwork has a caption made of a brief title and a description; minimal text, but explain every symbol and abbreviation.
- **Appendices** [GUIDE]: A, B, ...; equations (A.1), tables Table A.1, figures Fig. A.1.
- **Footnotes** [GUIDE]: sparingly, numbered consecutively.
- **Acknowledgements** [GUIDE]: separate section directly before the reference list; include people who helped with language or proofreading.
- **Language** [GUIDE]: American or British English, not a mixture. Use inclusive language.
- **Units** [GUIDE]: SI units, or give the SI equivalent.

## References [GUIDE]
- Any consistent style is accepted at submission; the journal style is applied at proof stage.
- Numbered citations in square brackets in order of appearance; author names may appear in text but always with the number ("Barnaby and Jones [8]").
- Include authors, titles, venue, year, volume, article number or pages, and DOIs where available. Every reference must be real and correct.
- Preprints: mark as "preprint" (or name the server) and give the preprint DOI (arXiv: `10.48550/arXiv.<id>`); cite the formal publication once it exists.
- Software: creators, title, venue or repository (preferably with a persistent identifier), date, identifier (DOI preferred, otherwise URL), version or access date. Cite a describing article in addition to, not instead of, the software.
- Data: author(s), dataset title, repository, version, year, persistent identifier; prefix the entry with `[dataset]`.
- Web references: full URL and last access date.
- Abbreviate journal titles per ISO 4/LTWA (applied at proof if needed).

## Research data: Option C [GUIDE]
The journal applies **Option C**: authors are **required** to deposit research data in a relevant repository and cite and link the dataset in the article; if that is not possible, they must state why the data cannot be shared. A data availability statement is required at submission and is published with the article. Research data includes software, code, models, protocols and methods. Co-submission of a data or methods article to *Data in Brief* or *MethodsX* is encouraged.

Practical route: deposit author-owned code and derived results (Zenodo or Mendeley Data, with a DOI), cite the deposit as a `[dataset]` or software reference, and state precisely which third-party or confidential inputs are excluded and why. "Release planned upon acceptance" alone does not meet Option C; ask the user before depositing anything, because deposit makes it public.

## Declarations: exact wording
**Generative AI** [GUIDE]. Required at first submission when AI tools were used in manuscript preparation; placed **at the end of the manuscript, in a new section before the reference list** (after appendices if appendices precede the references). Heading:

> Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

Statement template:

> During the preparation of this work the author(s) used [NAME OF TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

List every tool and purpose. Basic grammar, spelling and reference checkers and accessibility tools are exempt. AI tools cannot be authors. If AI generated an image, disclose it in that caption and in the statement. AI may help draw explanatory schematics and data plots derived reproducibly from data, never primary observational images.

**Competing interests** [GUIDE]. Disclose employment, consultancies, stock, honoraria, testimony, patents, grants and journal editorial roles. Use "I have nothing to declare" in the tool if none.

**Funding** [GUIDE]. List funders and grant numbers in the standard form ("This work was supported by ... [grant numbers ...]"). For block grants or institutional resources, name the institution. State the sponsor's role in design, analysis, writing and the decision to submit, or that it had no such involvement. If there was no funding: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."

**CRediT** [GUIDE]. Corresponding author lists roles from: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, Writing – review and editing.

**Authorship** [GUIDE]. Changes need editor approval and the Authorship Change Request form before acceptance and are not allowed after acceptance; fix the author list and order before submitting.

## Submission declaration and portal [GUIDE]
- Submitting implies the work is unpublished (preprints, theses and lectures excepted), not under consideration elsewhere, approved by all authors and institutions.
- The portal offers optional free preprint posting on SSRN after desk review; the corresponding author needs all co-authors' approval first. The choice does not affect the decision.
- Editors may suggest a transfer to another Elsevier journal through the Article Transfer Service.
- Two publishing choices [GUIDE]: subscription, with no publication fee, or gold open access with an APC of **USD 3150 excluding taxes** (all article types; a personalized price is shown during submission). Licences: CC BY, CC BY-NC, CC BY-NC-ND. The choice does not affect peer review.
- Self-archiving of the accepted manuscript for subscription articles has a **24-month embargo**; the published PDF may not be posted on ResearchGate or Academia.edu [GUIDE].
- Proof corrections are due within two days of the proof e-mail.
- Submission system [GUIDE]: https://submit.elsevier.com/INFOSYS (the "Submit your article" link on the guide). Journal metrics shown on the page in October 2026: CiteScore 11.8, Impact Factor 4.0.

## Desk-reject prevention (lessons from a 2026 scope rejection at a sister Elsevier journal)
- The first page must make the reviewer pool obvious: name the systems and the community in the title, abstract and first paragraphs.
- Remove every trace of an earlier target journal: `\journal{...}`, paragraphs written for that journal, supplement file names, cover-letter text.
- Remove internal codes (project numbers, file versions, "version-3") from text, captions, tables, figure labels and file names.
- State each caveat once where it applies and once in Limitations.

## Before pressing Submit
- [ ] Guide re-read if older than six months; tags current.
- [ ] `check_submission.py` reports no ERROR.
- [ ] Source `.tex`, class file and every figure uploaded as separate files; compiled PDF uploaded; fonts embedded.
- [ ] Highlights file named with "highlights", 3–5 bullets of at most 85 characters.
- [ ] Abstract at most 250 words, no references; 1–7 keywords.
- [ ] Data statement meets Option C (deposit with DOI, or a specific reason for each withheld item).
- [ ] Declarations tool document attached; funding statement names the sponsor's role.
- [ ] AI declaration is the last section before the references and lists every tool.
- [ ] Every supplementary file is cited in the text with a caption and named neutrally.
- [ ] Related submissions disclosed if asked; author list final.
- [ ] The user, not the assistant, presses Submit.

## Sources
- Guide for Authors, Information Systems, ScienceDirect (read 2026-10-21 from the user's saved copy).
- Journal page: https://shop.elsevier.com/journals/information-systems/0306-4379
- Reproducibility editorial, Inf. Syst. 59 (2016) 95–97: https://cs.nyu.edu/~shasha/papers/43707JIScollaborative.html
- elsarticle: https://ctan.org/pkg/elsarticle ; Elsevier LaTeX: https://www.elsevier.com/latex
- Elsevier GenAI policies: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Research data guidelines: https://www.elsevier.com/authors/tools-and-resources/research-data/data-guidelines
- Artwork instructions: https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions/artwork-types
