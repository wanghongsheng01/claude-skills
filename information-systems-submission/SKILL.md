---
name: "information-systems-submission"
description: "Pre-submission checklist for the Elsevier journal Information Systems (ISSN 0306-4379, CCF B, data management). Use before submitting, resubmitting or transferring any manuscript to Information Systems: scope fit, required files, elsarticle formatting, highlights, declarations (CRediT, competing interests, data availability, generative-AI statement), reproducibility material and the portal steps. Includes a script that checks a LaTeX submission folder."
---

# Information Systems submission checklist (投稿前须知)

Use this skill whenever a manuscript is being prepared for, or moved to, **Information Systems** (Elsevier, ISSN 0306-4379). It is not the Wiley *Information Systems Journal* and not *Information Systems Research*; check the ISSN before using anything below.

Every rule carries a status:
- **[VERIFIED]** read on an official journal or Elsevier page (sources at the end);
- **[ELSEVIER]** Elsevier-wide policy that applies unless the journal overrides it;
- **[CHECK]** could not be confirmed because ScienceDirect blocks automated access. Confirm it in the Guide for Authors before submitting, then update this file and its date.

Last researched: 2026-10-21. If the user supplies the Guide for Authors (PDF or text), read it first and resolve every [CHECK] item before anything else.

## Workflow
1. **Confirm the journal and the guide.** Ask the user for the current Guide for Authors if it is not in the conversation: https://www.sciencedirect.com/journal/information-systems/publish/guide-for-authors (ScienceDirect refuses bots and the in-app browser; the user must save it from a normal browser). Do not route around the block with caches or mirrors.
2. **Scope test (desk-reject risk).** Answer the four questions in "Scope fit" in writing. If any answer is weak, fix the framing of the title, abstract and introduction first; a desk rejection for scope wastes weeks.
3. **Build the file set** in "Required files". Keep one folder per submission with a manifest.
4. **Format** with elsarticle as in "Formatting".
5. **Run the checker**: `python3 scripts/check_submission.py <latex-folder> --main main.tex --highlights highlights.txt [--forbid 'P19|DKE']`. Fix every ERROR; read every WARN.
6. **Compile and look.** Compile twice, check undefined references and overfull boxes, render each page with a figure or table, and open the final PDF.
7. **Portal pass.** Walk the portal fields in "Editorial Manager" with the user. Never click Submit, accept terms or pay on the user's behalf; the user does that.

## Scope fit
Information Systems publishes work on "languages, data and process models, algorithms, software and hardware for data-intensive systems", motivated by real or potential applications. Systems papers must show "serious experimentation on real systems or simulations based on real-system traces" [VERIFIED]. Typical areas are those of SIGMOD/PODS, VLDB, ICDE and ICDT/EDBT, plus data mining over structured data, web and cloud data management, business process management and data science [VERIFIED].

Before submitting, write one sentence for each:
1. Which data-intensive system, model or process does the paper study?
2. Which of the venues above would its reviewers normally publish in? Name two or three cited papers from them.
3. What is the experimental evidence, and on which real systems, datasets or traces?
4. Can a reader reproduce it? The journal runs a reproducibility programme (below), so editors value runnable artifacts.

Papers that measure or audit systems without proposing a new algorithm are acceptable when the measurements are on real systems and the conclusions are useful to builders or evaluators. Say this plainly in the cover letter; do not let the editor guess the contribution type. Cite genuinely related Information Systems papers where they exist (for data quality, e.g., Mohammed et al., Inf. Syst. 132 (2025) 102549).

## Article types [VERIFIED]
- Research articles (systems, theory, application domains).
- Experimental reproducible survey papers: must run a substantial portion of the surveyed techniques on at least one existing benchmark and be reproducible.
- Reproducibility papers: by invitation only, as companions to accepted Information Systems papers. Code and data are deposited as one self-contained dataset on Mendeley Data (ReproZip or Docker recommended); reproducibility reviewers become co-authors and the review is not anonymized.
- Retrospective articles: invited by the Editors-in-Chief.

## Required files
| File | Rule | Status |
|---|---|---|
| Manuscript PDF | Compiled from elsarticle; line and page numbers help reviewers | [ELSEVIER] |
| LaTeX source archive | One archive with .tex, figures, .bib/.bbl and any non-TeX-Live class; item type "LaTeX source files", never "Supplementary" | [ELSEVIER]; whether required at first submission [CHECK] |
| Highlights | Separate editable file, 3–5 bullets, each at most 85 characters including spaces; usually requested at final-files stage but harmless at first submission | [ELSEVIER]; mandatory or not [CHECK] |
| Graphical abstract | Optional unless the guide says otherwise; at least 1328×531 px (2.5:1), 300 dpi; no general-purpose generative-AI images | [ELSEVIER]; [CHECK] |
| Cover letter | State contribution type, fit to scope, prior submissions or rejections if asked, related submissions by the same authors | portal field |
| Declaration of competing interest | Corresponding author fills Elsevier's Declaration Tool for all authors and uploads the generated document; the statement also appears in the manuscript | [ELSEVIER] |
| CRediT statement | "Name: Role, Role, ..." using the 14 CRediT roles | [ELSEVIER] |
| Data availability statement | Say what is shared, where, under which licence, and what is restricted and why | [ELSEVIER]; journal data option A–E [CHECK] |
| Generative-AI declaration | Separate section before the references (see below) | [ELSEVIER] |
| Supplementary archives | Neutral names (e.g., `Supplement_S1_reference_experiment.zip`); no internal project codes or the name of another journal | good practice |

## Formatting
- **Class.** `\documentclass[preprint,12pt]{elsarticle}` is the safe submission layout (single column, wide spacing). `review` gives double spacing; `3p,twocolumn` or `5p` only imitate final layout. `doubleblind` exists if the journal turns out to be double-anonymized [VERIFIED class options; review model CHECK].
- **Journal line.** `\journal{Information Systems}` exactly.
- **Front matter.** `\title`, `\author` with `\affiliation[...]{organization=..., city=..., country=...}`, `\cortext`, `\ead`; abstract inside `frontmatter`; keywords separated by `\sep`.
- **Abstract.** One paragraph, no citations, no undefined abbreviations; keep it at or under 250 words [CHECK exact limit].
- **Keywords.** 1–7, avoid repeating title words where possible [CHECK].
- **References.** Numbered style: `\bibliographystyle{elsarticle-num}` with a .bib file, or a hand-built `thebibliography` in the same format. Give DOIs. Keep journal and conference names consistent. Elsevier's "Your Paper Your Way" allows any consistent style at first submission [ELSEVIER; participation CHECK].
- **Figures.** Vector PDF/EPS with embedded fonts for diagrams and plots; raster at least 300 dpi (photos), 500 dpi (combination), 1000 dpi (line art); RGB colour; fonts Arial/Helvetica, Times, Courier or Symbol [ELSEVIER]. Every figure and table is cited in the text before it appears.
- **Sections.** Numbered sections; appendices after the main text with `\appendix`; declarations (CRediT, competing interests, funding, data availability, AI statement) as unnumbered sections before the references.

## Declarations: exact wording
**Generative AI** [ELSEVIER]. Heading, verbatim:

> Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

Body template:

> During the preparation of this work the author(s) used [NAME OF TOOL / SERVICE] in order to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.

List every tool actually used (for example both an earlier tool and a later one), not only the latest. Basic spelling and grammar checkers are exempt. AI used as part of the research method belongs in the Methods section. AI cannot be an author or a cited source of facts.

**CRediT** [ELSEVIER]. Roles: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing – original draft, Writing – review & editing, Visualization, Supervision, Project administration, Funding acquisition.

**Competing interests.** Disclose employment, joint centres and long-standing industrial collaborations explicitly; editors prefer over-disclosure. Use the Declaration Tool output for the upload.

**Funding.** One sentence naming each funder and grant number, or state that the work received no specific grant.

## Editorial Manager
- Site: https://www.editorialmanager.com/infosys/ appears in search results [CHECK that it is current].
- Typical fields: article type, title, abstract, keywords, authors with ORCID, funding, suggested and opposed reviewers, cover letter, declarations, file uploads in the item types above, open-access choice.
- The journal is listed as subscription with an open-access option (hybrid). Open access is optional and carries an APC; third-party sources quote about US$3,400 or €3,200 [CHECK on the journal's open-access page]. Choosing subscription publishing costs nothing.
- Preprints may be posted at any time; after acceptance, an arXiv copy may be updated to the accepted manuscript under CC BY-NC-ND with a DOI link [ELSEVIER].

## Desk-reject prevention (lessons from a 2026 scope rejection at a sister Elsevier journal)
- The first page must make the reviewer pool obvious: the title, abstract and first two paragraphs should name the systems and community (for example data cleaning systems and their benchmarks), not an abstract procedure.
- Remove every trace of an earlier target: `\journal{...}`, "Recent [journal] studies" paragraphs, supplement file names, cover-letter text.
- Remove internal codes (project numbers, file versions such as `v7`, "version-3 certificate") from the paper, captions, tables and file names.
- Keep caveats, but state each one once, in the place where it matters and in Limitations; long runs of negations read as uncertainty about the contribution.

## Before pressing Submit
- [ ] Guide for Authors read; all [CHECK] items resolved and this file updated.
- [ ] `check_submission.py` reports no ERROR.
- [ ] PDF compiled from the exact uploaded source; references resolve; figures readable at 100% zoom.
- [ ] Highlights, cover letter, declarations and supplements named neutrally.
- [ ] Competing-interest document from the Declaration Tool attached.
- [ ] AI declaration lists every tool used.
- [ ] Related submissions by the same authors disclosed if the portal asks.
- [ ] The user, not the assistant, presses Submit.

## Sources (accessed 2026-10-21)
- Journal page, scope and article types: https://shop.elsevier.com/journals/information-systems/0306-4379
- Reproducibility section editorial, Inf. Syst. 59 (2016) 95–97: https://cs.nyu.edu/~shasha/papers/43707JIScollaborative.html ; guidelines: https://cs.nyu.edu/~shasha/papers/reproducibilityguidelines
- elsarticle documentation (v3.5): https://ctan.org/pkg/elsarticle
- Elsevier LaTeX submission: https://www.elsevier.com/latex
- Highlights: https://www.elsevier.com/highlights
- Graphical abstracts: https://www.elsevier.com/authors/journal-authors/graphical-abstract
- Artwork: https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions/artwork-types
- Generative AI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- CRediT: https://www.elsevier.com/authors/policies-and-guidelines/credit-author-statement
- Declaration of interests: https://www.elsevier.com/connect/something-to-declare
- Research data guidelines: https://www.elsevier.com/authors/tools-and-resources/research-data/data-guidelines
- Sharing policy: https://www.elsevier.com/sharingpolicy
- Guide for Authors (manual check required): https://www.sciencedirect.com/journal/information-systems/publish/guide-for-authors

See `references/verification-log.md` for what was and was not readable and how to update this skill.
