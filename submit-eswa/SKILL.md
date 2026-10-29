---
name: "submit-eswa"
description: "Submission guide and checklist for the Elsevier journal Expert Systems with Applications (ESWA, ISSN 0957-4174 / online 1873-6793). Use before submitting, resubmitting or transferring any manuscript to ESWA (投稿 ESWA / 改投 ESWA): scope test, double-anonymized review (separate title page + anonymized manuscript), APA author-year references with elsarticle + model5-names, abstract/keyword/highlight limits, artwork files, Option C research data, exact declaration wording (generative AI, competing interests, funding, CRediT), Editorial Manager upload items, APC and timelines. Includes a LaTeX checker, a PDF anonymity/font checker and a docx builder."
---

# Submit-ESWA: Expert Systems with Applications submission guide (投稿 ESWA 指南)

Use this skill whenever a manuscript is prepared for, or moved to, **Expert Systems with Applications** (Elsevier). Companion skills: `write-eswa` (how ESWA papers are written) and `review-eswa` (how ESWA screens and reviews). Order of use: `write-eswa` while writing → `review-eswa` for the pre-submission review → `submit-eswa` to build and check the package.

Status tags:
- **[GUIDE]** read in full from the ESWA Guide for Authors on ScienceDirect on **2026-10-29** through Claude in Chrome (`references/guide-digest.md` holds the digest with quotes);
- **[SD]** read from the journal's other ScienceDirect pages (open access, insights, editorial board) on 2026-10-29;
- **[EM]** read from the Editorial Manager landing page (https://www.editorialmanager.com/eswa/) on 2026-10-29;
- **[CHECK]** typical Elsevier/Editorial Manager behaviour not yet seen for ESWA itself; confirm in the portal and update this file.

ScienceDirect blocks WebFetch and the built-in browser. Claude in Chrome reads the guide (if `get_page_text` returns nothing, wait one second and retry; the page is client-rendered). Re-read the guide when this file is older than six months.

## Language convention (permanent agreement with the author)
- **English** for everything editors, reviewers or the portal see: manuscript, title page, highlights, cover letter, declarations, data statement, portal fields, responses to reviewers.
- **Chinese (中文)** for every report to the author: progress, check results, step-by-step instructions, decisions, internal README/logs.

## Workflow
1. **Scope test** (desk-reject risk is high; first decision in about 5 days [SD]). Write the four answers in "Scope fit" and fix title, abstract, highlights and the first two introduction paragraphs until each answer is explicit.
2. **Split the manuscript** into the anonymized manuscript and a separate title page (see "Double-anonymized review").
3. **Switch references to APA author-year** (see "References") and rewrite every citation as `\citet`/`\citep`.
4. **Decide the data route** (Option C) with the author. For double-anonymized review the repository link goes on the title page and in the portal, not in the manuscript, unless an anonymized mirror is used.
5. **Build the file set** in "Upload items", one folder per submission (template below).
6. **Run the checker** and fix every ERROR, read every WARN:
   ```bash
   python3 scripts/check_eswa_submission.py paper/ --main manuscript.tex --bib references.bib \
     --title-page title_page.md --highlights highlights.txt \
     --identity 'Surname1|Surname2|university|company|github-user|zenodo\.12345' --forbid 'Old Journal Name' \
     --package ../upload_folder
   ```
7. **Compile** on Overleaf or a full TeX Live (pdfLaTeX). Then check the PDF:
   ```bash
   python3 scripts/verify_eswa_pdf.py --pdf Manuscript.pdf --identity '<same regex>' \
     --expect '<newest sentence>' --forbid 'Old Journal Name'
   ```
   No Type 3 fonts, no `??`, no identity strings in text or metadata.
8. **Make the Word files** (title page, highlights, cover letter, response letter) with `python3 scripts/make_docx.py in.md out.docx`.
9. **Portal pass** with the author in Editorial Manager. Never click Submit, tick declarations, choose open access, accept terms or pay for the author.

## Scope fit [GUIDE]
ESWA publishes "original papers dealing with the design, development, testing, implementation, and/or management of expert and intelligent systems, and also to provide practical guidelines in the development and management of these systems", applied "in industry, government, and universities worldwide". Listed areas include finance, engineering, marketing, law, risk assessment, **information management, information retrieval, intelligent database management systems**, medicine, business, production management, energy; also **multi-agent systems, knowledge management, neural networks, knowledge discovery, data and text mining**, multimedia mining and genetic algorithms.
- **Excluded:** applications to military/defence systems.
- **Discouraged:** metaphor-based ("nature-, technical- or socially-inspired") algorithms that rename existing concepts; such papers must give formal, mathematically grounded differences from established methods and use standard optimisation terminology.

Answer in writing before submitting:
1. Which expert or intelligent system does the paper design, build, test or manage, and who would deploy it (industry, government, university)?
2. Which application problem and which real data or users make the evaluation concrete?
3. What practical guideline does a system builder take away (a decision rule, a default, a cost trade-off, a failure mode)?
4. Which ESWA topics from the list above does it match? Name the two or three that the cover letter will use.

A method paper fits when it is framed as a component of an intelligent system with a clear application and practical guidance. Pure NLP or statistics framing, with no system or deployment angle, invites "out of scope" (in 2026 a sister Elsevier journal desk-rejected an LLM-annotation method paper as out of scope and pointed it to ESWA).

## Peer review [GUIDE]
- **Double anonymized.** Editors screen first; suitable papers go to **at least two reviewers**; editors decide. One appeal per submission (Elsevier Appeal Policy).
- Editors do not handle papers by themselves, family or colleagues, or about products in which they have an interest.
- Special issues follow the same process; a guest editor may recommend, the journal editor decides.
- Reviewers and editors may not upload the manuscript into generative-AI tools.

## Double-anonymized review [GUIDE]
Submit **two separate files**:
- **Title page (with author details)**: title; given and family names in portal order; affiliations with lowercase superscript letters and full postal address including country; corresponding author marked, with full postal address and e-mail (published); present address as numbered footnotes; **acknowledgements** (only here, never in the manuscript); **declaration of competing interests** when no separate declaration file is submitted.
- **Anonymized manuscript**: main body, references and tables, **no** author names, affiliations, acknowledgements or other identifying information; the same applies to supplementary material.

Practical anonymization (our rules):
- Remove `\author`, `\ead`, `\affiliation`, `\cortext`; do not set `pdfauthor`; check PDF metadata.
- Move CRediT (names), acknowledgements, and any competing-interest text that names a person or company to the title page / portal. Keep funding text only if it names no person (grant numbers can identify; move them to the title page when in doubt).
- Self-citations in the third person ("Wang et al. (2026) showed"), never "our previous work [x]". Do not cite unpublished own work under review.
- Repository links: GitHub user names and Zenodo DOIs identify authors. Either use an anonymized mirror (e.g. anonymous.4open.science, created by the author) or write "available in a public repository (DOI given on the title page and in the submission system)". Put the real DOI back at revision/acceptance.
- File names, figure text, code comments in the source zip and supplementary README files must also be clean (`--identity` scans them).

## Article types [GUIDE]/[CHECK]
The guide lists original papers on expert and intelligent systems technology and application. Editorial Manager offers article types at step 1 (typically "Full Length Article" and "Review Article") [CHECK]. Choose the full-length research article for a method paper. Special-issue submissions choose the special-issue type. Software can additionally be published in *Software Impacts* [GUIDE].

## Upload items (Editorial Manager) [CHECK names; rules GUIDE]
| Item | Rule |
|---|---|
| Title page (with author details) | Separate editable file (.docx or .tex) with everything listed above [GUIDE] |
| Manuscript (anonymized) | Editable source required: `.tex` (or `.docx`); "A PDF is not an acceptable source file" [GUIDE]. Upload the compiled PDF too so reviewers see the typeset version; Word must be single-column, LaTeX may be double-column [GUIDE] |
| LaTeX source files | All editable source files "upon submission or revision" [GUIDE]; include `.bib`/`.bbl`, class, `.bst`, inputs |
| Figures | Each figure a separate file named `Figure_1`, `Figure_2`, ...; vector EPS/PDF with embedded fonts; photographs ≥300 dpi; bitmap line art ≥1000 dpi; no multi-panel files of unrelated graphs [GUIDE] |
| Tables | Editable text, not images [GUIDE] |
| Highlights | **Encouraged** (not mandatory) [GUIDE]; separate editable file whose name contains "highlights"; 3–5 bullets, each ≤85 characters including spaces |
| Graphical abstract | Not mentioned in the guide → optional [GUIDE] |
| Declaration of interest | Complete Elsevier's declarations tool for every submission; upload the resulting .doc/.docx; no signatures; "I have nothing to declare" if none [GUIDE] |
| Cover letter | Not required by the guide; recommended (scope, novelty, related submissions, prior rejection history if helpful) |
| Supplementary material | Cite every file in the text with a concise caption; submit together with the manuscript; replaceable only at revision; published exactly as received [GUIDE] |
| Video | ≤150 MB per file, 1 GB total, with stills and a text description [GUIDE] |
| Co-submission | Optional data/methods article to *Data in Brief* or *MethodsX* [GUIDE] |

## Formatting [GUIDE]
- **Template**: Elsevier LaTeX template encouraged. Safe preamble for ESWA:
  ```latex
  \documentclass[preprint,12pt,authoryear]{elsarticle}   % or [review,...] for double spacing
  \journal{Expert Systems with Applications}
  \bibliographystyle{model5-names}                        % Elsevier APA-style model; assets/model5-names.bst
  ```
  `assets/manuscript_skeleton.tex` and `assets/title_page_template.md` give the full anonymized layout. Line numbers (`lineno`) help reviewers and are allowed.
- **Title**: concise, informative; avoid abbreviations and formulae unless established ("DNA").
- **Abstract**: ≤**250 words**; purpose, basic procedures, main findings **with their statistical significance where applicable**, principal conclusions; emphasise what is new; stand-alone; avoid references (if essential, author and year in full); define non-standard abbreviations at first use.
- **Keywords**: **1–7**, English, avoid multi-word keywords built with "and"/"of"; abbreviations only if firmly established.
- **Sections**: numbered 1, 1.1, 1.1.1; cross-refer by number; abstract unnumbered. Optional "Theory and calculation" style sections.
- **Math**: editable; inline when simple; solidus for small fractions; italic variables; `exp` for powers of e; displayed equations numbered consecutively.
- **Tables**: editable; cited in order; caption with the table; notes below; no vertical rules or shading; no duplication of results shown elsewhere.
- **Artwork**: every figure cited and numbered in order; caption = brief title (not inside the image) + description; explain every symbol/abbreviation; colour accessible to colour-blind readers; no AI-generated or AI-altered primary data images; disclose AI-made images in the caption and the AI statement.
- **Footnotes**: sparingly, consecutive.
- **Appendices**: A, B, ...; Eq. (A.1), Table A.1, Fig. A.1.
- **Language**: American or British English, not mixed; inclusive language (avoid "he/she"; plural neutral forms).
- **Sex/gender**: only when research involves humans/animals (SAGER).
- **Maps**: show only the study area and carry the jurisdiction note.

## References [GUIDE]
- **APA 7th edition**: author–year citations in text; reference list **alphabetical, then chronological**; same author and year → 2020a, 2020b.
- Every reference must be real, complete and correct; include DOIs where available; references in the abstract given in full; avoid personal communications/unpublished results in the list; "in press" means accepted.
- Journal example: `Van der Geer, J., Handgraaf, T., & Lupton, R. A. (2020). The art of writing a scientific article. Journal of Scientific Communications, 163, 51–59. https://doi.org/...`
- Article number: `..., Heliyon, 19, Article e00205. https://doi.org/...`
- **Dataset**: prefix `[dataset]`; author(s), title, repository, version, year, persistent identifier.
- **Software**: creators, title, venue/repository with PID, date, identifier (DOI preferred), version, `[Computer software]`; cite a describing article in addition, not instead.
- **Preprints**: mark "preprint" or the server name and give the preprint DOI (arXiv: `10.48550/arXiv.<id>`); cite the formal version once it exists.
- **Web**: full URL and last access date.
- LaTeX: `elsarticle` + `authoryear` + `model5-names.bst` (shipped in `assets/`, LPPL, Elsevier) produces the APA-like list. Write `\citet{key}` for "Huang et al. (2025)" and `\citep{key}` for "(Huang et al., 2025)". Never "Huang et al.~\cite{key}" (duplicates the names).
- In BibTeX, protect acronyms in titles with braces, give `doi = {...}` without the https prefix (model5-names prints it), and for arXiv use `@misc` with `howpublished = {arXiv preprint arXiv:xxxx}` plus `doi = {10.48550/arXiv.xxxx}`.

## Research data: Option C [GUIDE]
**Required**: deposit research data (including software, code, models, protocols) in a relevant repository, **cite and link** it in the article; if impossible, state why. A data statement is required at submission and published with the article. Data can be linked in the portal and inline as `Database: ID`.

## Declarations: exact wording [GUIDE]
**Generative AI** — at submission, at the end of the manuscript, **in a new section before the reference list**:
> Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

> During the preparation of this work the author(s) used [NAME OF TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

Not needed for basic grammar/spelling/reference checkers or accessibility tools; nothing to disclose → no statement. AI cannot be an author or be cited as one. Authors remain accountable for verifying AI output, including references.

**Competing interests** — disclose employment, consultancies, stock, honoraria, paid testimony, patents, grants, editorial roles. Always complete the declarations tool; upload its Word file at "attach files". Journal editors who author must use the given "Other Activities" text.

**Funding** — "This work was supported by [funder] [grant numbers ...]"; state the sponsor's role in design, collection, analysis, interpretation, writing and the decision to submit, or that it had none. If none: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."

**CRediT** (encouraged): Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, Writing – review and editing. In double-anonymized review put it on the title page / portal.

**Authorship** — definitive list and order at submission; changes only before acceptance with the Authorship Change Request form and editor approval; none after acceptance. Group authorship declared on the title page. One corresponding author; only that author's affiliation determines publishing-agreement eligibility.

## Submission declaration, preprints, publishing [GUIDE]/[SD]
- Submission implies the work is unpublished (preprints, theses, lectures excepted), not under consideration elsewhere, approved by all authors and institutions; screening tools may check it.
- Free SSRN preprint posting can be chosen during submission; it does not affect the decision; needs all co-authors' approval; it makes the manuscript public at once (and weakens anonymity in practice).
- Article Transfer Service may suggest another Elsevier journal.
- Publishing options [SD]: subscription (no fee) or gold OA, **APC USD 3,630** excl. tax (personalised price shown in the portal); licences CC BY, CC BY-NC, CC BY-NC-ND; choice does not affect review. Self-archiving of the accepted manuscript: **24-month embargo**; published PDF not on ResearchGate/Academia.
- Proof corrections within **two days**; check AI-generated alt text in proofs.
- Journal metrics shown on 2026-10-29 [SD]: CiteScore 17.0, Impact Factor 9.4; timeline: **5 days** submission → first decision, **62 days** to decision after review, **147 days** to acceptance, **7 days** acceptance → online.
- Editor-in-Chief on 2026-10-29 [SD]: Prof. Ling Wang (Tsinghua University). 156 editors in 32 countries; associate editors with NLP/crowdsourcing/human-centred AI expertise exist, so name the application area clearly to reach them.

## Editorial Manager walkthrough [EM]/[CHECK]
Portal: https://www.editorialmanager.com/eswa/ — sign in with "Continue with Elsevier" (Elsevier account). Typical Elsevier EM sequence [CHECK each label]:
1. **Select Article Type** (full-length article / review / special-issue types).
2. **Attach Files**: choose item type per file — Title Page (with Author Details), Manuscript (anonymized; .tex + PDF), LaTeX source / supplementary, Figure (one per file), Table if separate, Highlights, Declaration of Interest Statement, Cover Letter. EM builds a review PDF; download and inspect it for identity leaks before approving.
3. **Review Preferences**: suggested/opposed reviewers if asked (real, independent experts; no co-authors or colleagues from the last few years).
4. **Additional Information**: questionnaire (prior submissions/related papers, data availability, generative-AI use, SSRN preprint choice, funding).
5. **Comments**: short note to the editor (optional).
6. **Manuscript Data**: full title, abstract (paste plain text), keywords, authors in order, funding, classifications/sections if offered.
7. **Build PDF for approval** → View Submission → **Approve Submission** (the author does this). Unapproved submissions stay in "Submissions Waiting for Author's Approval".

## Desk-reject prevention (ESWA-specific)
- Lead with the intelligent-system application in title, abstract, highlights and the first paragraph; name the users and the decision the system supports.
- Report statistical significance of the main claims in the abstract (the guide asks for it) and in tables.
- Give practical guidelines (when to use which variant, defaults, costs) in a dedicated subsection.
- Cover the recent literature, including relevant ESWA articles, but cite only what is used (editors flag citation padding and coercive self-citation).
- Remove every trace of the earlier journal (`\journal{}`, cover letter, file names, comments) and every identity string (double-anonymized).
- No metaphor-inspired algorithm branding; use standard terminology.

## Lessons from the first use (2026-10)
- `check_eswa_submission.py --identity` skips editor-only files whose names contain title, cover, declaration, response, portal or readme; everything else in the folder is treated as part of the anonymized upload.
- No local TeX: create a separate private Overleaf project for the journal version (never overwrite the earlier journal's project), push via git, set the main document, compile through the editor (or its compile endpoint) and read `output.log` for undefined references and overfull boxes before viewing the PDF.
- The plain-text abstract pasted into the portal counts more words than the LaTeX source (symbols such as 1 − δ become several tokens); keep the source at ≤246 words.
- Do not reuse a declarations-tool file from another journal (it names that journal); generate a new one.
- Figures must appear near their first mention, as in published ESWA articles. A tall figure placed with `[t]` only (no `p`) is deferred to the end of the document, and every later figure queues behind it, so all figures end up after the references. Use `[!tbp]`, put Figure 1 where it is first cited, and read the page numbers of the `fig:` labels in `output.aux` after compiling.
- A package script that names figure files one by one drops a figure added later (here Figure_5 was missing from both the upload folder and the source zip). Copy with a glob (`figures/Figure_[0-9]*.pdf`) and run the checker with `--package`, which compares every `\includegraphics` file with the upload folder and the source zip.

## Before approving the submission
- [ ] Guide re-read if this file is older than six months; tags updated.
- [ ] `check_eswa_submission.py`: 0 errors. `verify_eswa_pdf.py`: RESULT PASS.
- [ ] Title page separate, complete (names, affiliations with country, corresponding e-mail/address, acknowledgements, interests).
- [ ] Manuscript anonymized in text, figures, file names, PDF metadata, supplements and source comments.
- [ ] APA author-year citations; alphabetical list; DOIs; preprints marked.
- [ ] Abstract ≤250 words with significance stated; 1–7 keywords; 3–5 highlights ≤85 characters.
- [ ] Figures as separate Figure_N files, vector, fonts embedded; tables editable without vertical rules.
- [ ] Option C data statement; repository link on the title page/portal (or anonymized mirror).
- [ ] AI declaration last before references; funding sentence; declarations-tool .docx attached.
- [ ] Cover letter states scope fit, novelty and that the paper is not under consideration elsewhere.
- [ ] The author, not the assistant, approves and submits.

## Files
- `scripts/check_eswa_submission.py` — LaTeX folder checker (journal line, author-year setup, bare `\cite`, abstract, keywords, scope words, anonymity, identity regex over all source files, declarations, labels, figure names, highlights, title page).
- `scripts/verify_eswa_pdf.py` — PDF metadata/text identity scan, `??`, placeholders, Type 3 and non-embedded fonts, expected/forbidden text, stale-build check (needs `pypdf`).
- `scripts/make_docx.py` — Markdown-lite → .docx (python-docx or macOS textutil).
- `assets/manuscript_skeleton.tex`, `assets/title_page_template.md`, `assets/model5-names.bst`.
- `references/guide-digest.md` — section-by-section digest of the guide with quotes.
- `references/verification-log.md` — what was read when, and how to refresh.

## Sources
- Guide for Authors: https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/guide-for-authors (read 2026-10-29)
- Open access options: https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/open-access-options
- Journal insights: https://www.sciencedirect.com/journal/expert-systems-with-applications/about/insights
- Editorial board: https://www.sciencedirect.com/journal/expert-systems-with-applications/about/editorial-board
- Editorial Manager: https://www.editorialmanager.com/eswa/
- Community LaTeX template using model5-names + authoryear (not Elsevier's): https://github.com/Ravby/eswa-template
- Elsevier GenAI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier research-data guidelines: https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines
