---
name: "submit-ipm"
description: "Submission guide and checklist for the Elsevier journal Information Processing & Management (IPM, ISSN 0306-4573 / online 1873-5371). Use before submitting, resubmitting or transferring any manuscript to IPM (投稿 IPM / 改投 IPM): scope test at the computing and information-science intersection, four manuscript types, double-anonymized review (separate title page + anonymized manuscript), the no-preprint rule, abstract/keyword limits, required CRediT, artwork files, Option C research data, exact declaration wording (generative AI, competing interests, funding), new submission service at submit.elsevier.com/IPM, APC and timelines. Includes a LaTeX checker, a PDF anonymity/font checker and a docx builder."
---

# Submit-IPM: Information Processing & Management submission guide (投稿 IPM 指南)

Use this skill whenever a manuscript is prepared for, or moved to, **Information Processing & Management** (Elsevier). Companion skills: `write-ipm` (how IPM papers are written) and `review-ipm` (how to simulate the screen and review). Order of use: `write-ipm` while writing, then `review-ipm`, then `submit-ipm` to build and check the package.

Status tags:
- **[GUIDE]** read in full from the IPM Guide for Authors on ScienceDirect on **2026-10-31** through Claude in Chrome;
- **[SD]** read from the journal's other ScienceDirect pages on 2026-10-30;
- **[ELSEVIER]** general Elsevier policy or support page, not specific to IPM;
- **[CHECK]** not seen for IPM. Confirm in the portal and update this file.

ScienceDirect blocks WebFetch and the built-in browser. Claude in Chrome reads it; the page is client-rendered, so if `get_page_text` returns nothing, wait and retry. Re-read the guide when this file is older than six months.

**Do not open `submit.elsevier.com/IPM` for reading the rules.** In a signed-in browser it lands on the author's private submission list. Open it only when the author asks for a portal pass.

## Language convention (permanent agreement with the author)
- **English** for everything editors, reviewers or the portal see.
- **Chinese (中文)** for every report to the author.

## Workflow
1. **Scope test** (first decision in 2–5 days [SD], so the first page decides). Answer the four questions in "Scope fit".
2. **Check public versions.** Search the code repository, its archive and preprint servers for the manuscript (see "Preprints"). This can block the anonymity of the whole submission; settle it first.
3. **Split the manuscript** into the anonymized manuscript and a separate title page.
4. **Use author-year citations** (see "References").
5. **Decide the data route** (Option C) with the author.
6. **Build the file set** in "Upload items".
7. **Run the checker**, fix every ERROR and read every WARN:
   ```bash
   python3 scripts/check_ipm_submission.py paper/ --main manuscript.tex --bib references.bib \
     --title-page title_page.md --highlights highlights.txt \
     --identity 'Surname1|Surname2|university|company|github-user|zenodo\.12345' --forbid 'Old Journal Name' \
     --package ../upload_folder
   ```
8. **Compile** on Overleaf, TeX Live or Tectonic, then check the PDF:
   ```bash
   python3 scripts/verify_ipm_pdf.py --pdf Manuscript.pdf --identity '<same regex>' \
     --expect '<newest sentence>' --forbid 'Old Journal Name'
   ```
9. **Make the Word files** with `python3 scripts/make_docx.py in.md out.docx`.
10. **Portal pass** with the author. Never click Submit, tick declarations, choose open access, accept terms or pay for the author. Record every item seen and replace the [CHECK] tags here.

## Scope fit [GUIDE]
IPM publishes original research at the intersection of computing and information science, covering theory, methods or applications, in domains including advertising, business, health, information science, information technology marketing and social computing. It serves primary researchers and practitioners. The guide publishes no list of rejected topics.

Four manuscript types: **research**; **methods** (novel methods applied at the intersection); **review** (critical, in-depth, integrating prior work, with recommendations); **critical application** (system design research).

Answer in writing before submitting:
1. Which manuscript type is it, and which sentence on page 1 shows the information-science angle?
2. Who uses the information, score or system, and which decision changes because of this paper?
3. What does a reader learn that transfers beyond this dataset, model or benchmark?
4. Which IPM papers is it in conversation with? Cite them only after reading them.

Companion journal: *IPM: Applications* (gold OA) for work carried through to application [SD]. The Article Transfer Service may suggest another Elsevier journal [GUIDE].

## Peer review [GUIDE]
- **Double anonymized.** Editors screen first; suitable papers typically go to at least two reviewers; editors decide.
- One formal appeal per submission (Elsevier Appeal Policy), and that decision is final.
- Editors stay out of papers by themselves, family or colleagues, or about products in which they have an interest.
- Special issues follow the same process, but a guest editor may send papers out and recommend a decision.
- Editors and reviewers may not upload unpublished manuscripts into generative-AI tools. They may use AI tools in a supportive role to improve the language of reports or to search background literature.

## Double-anonymized review [GUIDE]
Submit **two separate files**:
- **Title page:** article title; given and family names in portal order (own script optional in parentheses); affiliations with lowercase superscript letters and full postal address including country; corresponding author with full address and e-mail (published); present address as Arabic-numeral footnote; **acknowledgments** (only here, including help with language, writing or proofreading); **competing interests** when no separate declaration file is submitted.
- **Anonymized manuscript:** main body, references and tables, with no names, affiliations or acknowledgments. Supplementary material must be clean as well.

Practical anonymization (our rules; the guide is silent on these):
- Remove `\author`, `\ead`, `\affiliation`, `\cortext`; never set `pdfauthor`; check PDF metadata.
- Move CRediT (names) and acknowledgments to the title page or the portal.
- Rewrite "colleagues at <company>" as "colleagues of the first author" in the manuscript. Keep that relationship visible to reviewers when it bears on the validity of a method.
- Self-citations in the third person.
- Repository links name the authors. Use an anonymized mirror created by the author, or write that the repository is identified on the title page and in the submission system.
- File names, figure text, source comments and supplementary files must be clean (`--identity` scans them).

## Preprints [GUIDE]
A preprint does not count as prior publication, but IPM says that **because of double anonymized review, submissions should not be published as a preprint before a final decision**. The guide does not address a version already public before submission [CHECK]. So:
- Search GitHub, Zenodo, arXiv and SSRN for the manuscript before uploading.
- Zenodo versions cannot be withdrawn. A public copy that names the authors must be disclosed to the editor in the cover letter, and in the portal if asked. Hiding it is a publishing-ethics risk.
- Remove manuscript sources from any public repository going forward, and keep them out of anything cited in the submission.
- Do not choose an SSRN option if the portal offers one [CHECK].

## Upload items
The portal is **https://submit.elsevier.com/IPM**, labelled a new submission service [GUIDE link]. Do not assume the ESWA Editorial Manager walkthrough applies. `editorialmanager.com/ipm` showed a "site under development" notice on 2026-10-30, so use the guide's link [CHECK its purpose]. Peer review and revisions may still run in Editorial Manager [ELSEVIER]. Elsevier's general steps for the new experience: article type, ethical declaration, upload, verify extracted metadata, funding, open access, journal questions, review and submit [ELSEVIER].

| Item | Rule |
|---|---|
| Title page | Separate editable file with everything listed above [GUIDE] |
| Manuscript (anonymized) | Editable `.tex` or `.docx`; "A PDF is not an acceptable source file" [GUIDE]. Word must be single-column; LaTeX may be double-column [GUIDE] |
| LaTeX sources | All editable source files at submission or revision [GUIDE]. If PDF is allowed, Elsevier's route is PDF as the manuscript item plus one archive of sources; otherwise sources as manuscript items; no subfolders [ELSEVIER]. IPM's route [CHECK] |
| Figures | Separate files named Figure_1, Figure_2; EPS or PDF with embedded fonts; photographs at least 300 dpi; bitmapped line art at least 1000 dpi; charts XLS/XLSX; no several unrelated graphs in one file; text not disproportionately small. Text graphics may be embedded in the LaTeX file [GUIDE] |
| Tables | Editable, not images; no vertical rules or shading; used sparingly [GUIDE] |
| Declaration of competing interests | Mandatory: complete the declarations tool, upload its .doc/.docx, no signatures [GUIDE; mandatory per ELSEVIER] |
| Highlights | **Guide silent.** Prepare them anyway: 3–5 bullets, at most 85 characters with spaces, separate editable file named "Highlights" [ELSEVIER]; published IPM articles show them. Required or not [CHECK] |
| Graphical abstract | Guide silent [CHECK]. General-purpose generative AI is prohibited for one [ELSEVIER] |
| Cover letter | Guide silent; prepare one page: aim, findings, scope fit, what is new; state any public earlier version [ELSEVIER + our rule] |
| CRediT | **Required of corresponding authors** [GUIDE]; on the title page under anonymization (placement [CHECK]) |
| Suggested/opposed reviewers | Guide silent; offered by some journals [ELSEVIER]. Prepare them [CHECK] |
| ORCID, institutional e-mail | Guide silent. ESWA's portal demanded these, so collect them first [CHECK] |
| Supplementary | Cited in the text, submitted together, concise caption, replaceable only at revision, published as received [GUIDE] |
| Co-submission | Optional *Data in Brief* or *MethodsX* article [GUIDE] |

No word or page limit appears in the guide [GUIDE silent]. Published PDFs run about 13–31 pages.

## Formatting [GUIDE]
- **Template:** the guide names Elsevier's LaTeX instructions (`elsarticle`) and the Overleaf CAS LaTeX Single-Column Template, and "encourages" a template. A safe preamble:
  ```latex
  \documentclass[preprint,12pt,authoryear]{elsarticle}
  \journal{Information Processing \& Management}
  \bibliographystyle{model5-names}   % assets/model5-names.bst
  ```
- **Title:** concise, informative; avoid abbreviations and formulae unless established.
- **Abstract:** at most **250 words**; purpose, basic procedures, main findings with statistical significance where applicable, principal conclusions; emphasise what is new; stand-alone; avoid references (author and year if essential); define non-standard abbreviations.
- **Keywords:** **1–7**, English; avoid multi-word terms built with "and" or "of"; abbreviations only if firmly established.
- **Sections:** clearly defined with headings; no numbering scheme stated.
- **File:** remove strikethrough and underline unless scientifically relevant.
- **Captions:** brief title not on the figure, plus description; explain every symbol.
- **Appendices:** A, B; Eq. (A.1), Table A.1, Fig. A.1.
- **Colour:** accessible to impaired colour vision; free online.
- **Language:** inclusive; plural neutral forms; avoid "he, she" and "he/she". Sex and gender analysis applies when research pertains to humans; address it or declare it a limitation when relevant.

## References [GUIDE]
- **The guide names no style.** It points to a "reference style section" that is absent from its text. Published IPM articles and Paperpile's style show **author-year with an alphabetical list** [observed, 3RD]. Use `authoryear` + `model5-names`, and confirm in the portal [CHECK].
- Write `\citet{key}` for "Huang et al. (2025)" and `\citep{key}` for "(Huang et al., 2025)". Never "Huang et al.~\cite{key}".
- Every reference real, correct and complete; DOIs where available; text and list match.
- **Data references:** authors, title, repository, version, year, persistent identifier, with **`[dataset]` immediately before the reference** (not printed). This differs from ESWA's placement after the title.
- **Preprints:** cite if central; mark "preprint" or the server name and give the DOI; use the formal version once it exists.
- **Web:** full URL and last access date, in the list or under a heading directly after it.
- Prefer not to list unpublished results or personal communications. "In press" means accepted.

## Research data: Option C [GUIDE]
**Required:** deposit research data (including software, code, models, protocols) in a repository and cite and link it; if impossible, state why. Link it when prompted at submission; inline format `Database: ID`. Where the link goes under anonymization is not stated [CHECK]; keep the real link on the title page and in the portal.

## Declarations: exact wording [GUIDE]
**Generative AI:** at first submission, at the end of the manuscript, in a new section before the reference list. Published with the article.
> Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

> During the preparation of this work the author(s) used [NAME OF TOOL/SERVICE] to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

Not needed for basic grammar, spelling or reference checkers, or for accessibility tools. AI can never be an author. **AI used in the research itself goes in Methods, described reproducibly** [ELSEVIER]; the declaration alone does not cover it. Editing and adapting AI output so that it reflects the authors' own analysis is the authors' duty [GUIDE]. AI-created images are disclosed in each caption and in the statement; AI may support explanatory images and reproducible data visualizations, never primary observed data [GUIDE].

**Competing interests:** always complete the declarations tool; "I have nothing to declare" if none. Journal-affiliated authors use the guide's "Other Activities" text.

**Funding:** "Funding: This work was supported by [funder] [grant numbers ...]"; state the sponsor's role or that it had none. If none: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."

**CRediT roles:** Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, Writing – review and editing.

**Authorship:** definitive at submission; changes only before acceptance with the Authorship Change Request form and editor approval; none after acceptance. One corresponding author; only that affiliation decides agreement eligibility.

**Human participants:** the guide has no dedicated section. Elsevier's new submission experience asks whether the study involves human research and generates a published declaration [ELSEVIER]. Have the consent and exemption details ready, and state them in the manuscript [ELSEVIER].

## Publishing and metrics
- Subscription (no fee) or gold OA; the choice does not affect review. **APC USD 3,350** excl. tax on direct read, with USD 3,720 in older search snippets [SD; CHECK the personalized price].
- Accepted manuscript via institutional repository after a 24-month embargo [SD]. Proof corrections within two days [GUIDE].
- CiteScore 16.8, Impact Factor 8.1 [SD, 2026-10-31]; older values circulate. CCF B (seventh edition).
- Timeline on direct read: 2 days to first decision, 61 to decision after review, 145 to acceptance, 13 to online [SD]; snippets showed 5/66/154/12, so the period is unclear [CHECK]. Crowd reports are slower and small-sample [3RD].
- Editor in Chief: Bernard (Jim) Jansen; Senior Editor Ben He (NLP, IR, LLMs); ten Associate Editors; 199 board members, 130 from China [SD, 2026-10-30].
- Open special issues change often; read the call-for-papers page. Several are tied to the IP&M Conference, and direct submission is unstated [CHECK].

## Before approving the submission
- [ ] Guide re-read if this file is older than six months.
- [ ] Public copies searched; any existing one disclosed in the cover letter; none cited in the anonymized files.
- [ ] `check_ipm_submission.py`: 0 errors. `verify_ipm_pdf.py`: RESULT PASS.
- [ ] Title page separate and complete. Manuscript anonymized in text, figures, file names, PDF metadata, supplements and source comments.
- [ ] Author-year citations; alphabetical list; DOIs; preprints marked; `[dataset]` placed immediately before data references.
- [ ] Abstract at most 250 words; 1–7 keywords; 3–5 highlights at most 85 characters.
- [ ] Figures as separate Figure_N files, vector, fonts embedded; tables editable without vertical rules.
- [ ] Option C satisfied; AI in research described in Methods; AI statement last before references with the exact wording.
- [ ] CRediT on the title page; funding sentence; declarations-tool file attached.
- [ ] Author, not assistant, approves and submits.

## Files
- `scripts/check_ipm_submission.py`: LaTeX folder checker (journal line, author-year setup, bare `\cite`, `[dataset]` references, abstract, keywords, anonymity, identity regex, declarations, labels, figures, title page, `--package` completeness).
- `scripts/verify_ipm_pdf.py`: PDF metadata and text identity scan, `??`, placeholders, Type 3 and non-embedded fonts, expected and forbidden text (needs `pypdf`).
- `scripts/make_docx.py`: Markdown-lite to .docx.
- `assets/manuscript_skeleton.tex`, `assets/title_page_template.md`, `assets/model5-names.bst`.
- `references/guide-digest.md`: every rule with its source URL, tag and the full [CHECK] list.
- `references/verification-log.md`: what was read when, and how to refresh.

## Sources
- Guide for Authors: https://www.sciencedirect.com/journal/information-processing-and-management/publish/guide-for-authors
- Insights: https://www.sciencedirect.com/journal/information-processing-and-management/about/insights
- Open access: https://www.sciencedirect.com/journal/information-processing-and-management/publish/open-access-options
- Editorial board: https://www.sciencedirect.com/journal/information-processing-and-management/about/editorial-board
- Elsevier GenAI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier LaTeX instructions: https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions
