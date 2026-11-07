# CVIU requirements and verification status

Use [the official journal guide](https://www.sciencedirect.com/journal/computer-vision-and-image-understanding/publish/guide-for-authors) as the controlling source. It was read in full in the author's ordinary browser on 2026-11-05; direct automated access returned HTTP 403. Browser-readable does not change that verifier result. On 2026-11-07 the same journal URL again returned HTTP 403 through both the registered DataHub verifier and the public web reader. Therefore the journal-specific rows below remain supported by the 2026-11-05 full snapshot, not a newly read 2026-11-07 guide. Refresh before submission when accessible; preserve access failures.

Legend: **Required** = explicit journal requirement; **Recommended** = journal encouragement/preference; **Unverified** = absent from current public guide or dependent on the live submission UI. A recommendation made by the agent is never a journal rule.

## Journal-specific rules from the 2026-11-05 full snapshot

| Item | Requirement and status | Official guide section |
|---|---|---|
| Review | Single anonymized; author identities remain. Typically at least two reviewers after editor screening | Peer review |
| Destination | Current guide links to https://submit.elsevier.com/CVIU. Public landing is not proof that a logged-in submission can be completed | Submit online |
| Types/length | No complete article-type menu, main-text word limit, page limit, numeric font/spacing requirement, or compulsory cover-letter limit found in the current full guide; verify actual system | Unverified |
| Source | Editable .doc/.docx or .tex; PDF is not a source-file substitute | File format |
| Columns | Word single-column; double-column permitted only for LaTeX | File format |
| LaTeX | Encouraged official CAS template: single-column cas-sc or two-column cas-dc. Both supplied in CAS Bundle 2.4 | LaTeX |
| Title page | Concise title, full author names, final order, affiliations/postal addresses/countries, corresponding author's email | Title page |
| Correspondence | One corresponding author for editorial workflow; final authorship before submission | Corresponding author; Changes to authorship |
| Abstract | At most 250 words; self-contained purpose, method, main findings, conclusion | Abstract |
| Keywords | 1–7 English keywords | Keywords |
| Highlights | Required separate editable file; name includes highlights; 3–5 bullets; each ≤85 characters including spaces | Highlights |
| Graphical abstract | Encouraged, not required. Separate file if used; width ≥1328px, landscape longest side, readable at 13cm width; TIFF/EPS/PDF/MS Office preferred | Graphical abstract |
| Headings | Numbered sections/subsections; abstract unnumbered; Appendix A/B with separate A.1 figure/table/equation numbering | Article structure |
| CRediT | Required, author-confirmed contributions | Author contributions |
| Vitae | Guide asks editable biography ≤100 words per author plus separate passport-style photo; upload stage not explicit | Vitae |
| References | Any consistent complete style accepted initially; target author–year, alphabetical then chronological bibliography, same-year letters. DOI where available; verify every source; published version preferred over preprint | References |
| Declarations | All authors disclose conflicts; complete official declarations tool and upload resulting .doc/.docx; signatures unnecessary. Disclose funding and sponsors' roles | Declaration of competing interests; Funding sources |
| AI | Substantive AI manuscript preparation requires declaration before references on first submission; identify tool/purpose/human review/responsibility. Basic grammar/spelling/punctuation checks are exempt; substantive restructuring is disclosed. AI is not an author | Declaration of generative AI use |
| Data | Option C: deposit research data, cite/link it; if sharing impossible, explain. Data definition includes code/models/algorithms. Do not falsely claim deposit or invent access restrictions | Research data |
| Supplements | Optional/encouraged; cite each; submit with main manuscript; caption each; production publishes as supplied; later add/replace at revision | Supplementary material |
| Video | Accepted/encouraged; descriptive reference in text, clear filenames, still per clip; preferred max 150MB each/1GB total | Video |
| Ethics | No simultaneous consideration elsewhere; all authors approve submission; verify prior venue status rather than treating a major-revision letter as rejection | Submission declaration |
| Optional services | SSRN posting needs coauthor approval and makes manuscript immediately public; Data in Brief/MethodsX co-submission optional and can add APC | Preprints; Co-submission |

## Figures and math

Supply separate figures with sequential text citations and captions. EPS/PDF vector: embed fonts or outline. Photographs/renderings TIFF/JPG/PNG: minimum 300dpi (single column1063px/full-page2244px). Bitmap line art:1000dpi (3543px/7480px). Guide recommends XLS/XLSX for charts/large shaded tables and PPT/PPTX for annotated images, whose embedded images need300dpi. Avoid combining unrelated figures; comparative image panels can be an exception. All labels must remain legible at intended output size. Current guide does not state the older generic 500dpi mixed-image rule.

Tables and equations must be editable. Tables need sequential citations, captions, notes below; avoid vertical rules/shading. Equations numbered as cited, variables italic. No image alteration to hide/change scientific evidence; disclose nonlinear adjustments. Preserve underlying data and original images.

## Current AI artwork distinction

The journal now permits AI-supported explanatory images with human oversight and disclosures; reproducible visualizations must derive from real data. Research-method AI belongs in Methods. Image captions and general AI declaration must reflect actual use. The [Elsevier journal AI policy](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals) updated June2026 prohibits general-purpose generative-AI image tools for graphical abstracts; use dedicated scientific/professional illustration tools. Never apply this permission to fabricate/retouch experimental evidence.

## Official template and supporting sources

- Journal-linked [CAS ZIP](https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip), verified CAS2.4, 3305507bytes, SHA256 `36d97da01c6bbd134f315bff6c3de553735e2550444a6ddd4f869ddc67a20757`. Includes cas-sc/cas-dc templates and `cas-model2-names.bst`, default natbib author–year. On 2026-11-07, the registered exact ZIP returned HTTP 200 with identical byte count and SHA256. Retain the official license/notices and remove template sample prose from the manuscript.
- [Elsevier LaTeX instructions](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions): generic guidance. Its “most journals accept PDF initially” does not override CVIU editable-source rule. On 2026-11-07 its full official text was fetched successfully. It specifically requires a single folder level for Editorial Manager (EM). If that is the target workflow, supply a flat submission variant with collision-free names and rewritten relative references, preserve the organized editable master, and verify both local rebuilding and the actual system proof. A locally compiling nested ZIP does not establish EM compatibility. Correct manuscript source files must not be designated as supplementary LaTeX merely to bypass conversion. No confirmed CVIU-specific Word-template download in this guide.
- [Data options](https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines): explains OptionC; journal explicitly selects it.
- [Declarations tool](https://declarations.elsevier.com/): required output comes from tool, not a locally fabricated document. Account actions require applicable authorization.

## Remaining live checks and readiness vocabulary

Article type label; required file designations; cover letter/reviewer/ORCID fields; upload-stage biography requirement; generated proof and attachment completeness; current fees/license choices; current closing status at the previous venue. Distinguish files complete, locally rebuilt, platform-compatible, uploaded, and submitted. Mark unresolved mandatory inputs or central scientific issues precisely; do not invent a need for renewed author approval when the same facts and action were already confirmed. A successful local build is evidence of local portability, not a claim that the publisher portal accepted those files. The skill itself grants no authority to log in, submit, post a preprint, contact an editor, publish data, or change authorship.
