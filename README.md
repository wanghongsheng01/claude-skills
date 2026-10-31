# Claude skills

## academic-latex-polish
Polishes the English of a LaTeX research paper to the register of published PVLDB/SIGMOD papers. It does not change any fact, number, macro, citation or reference. A preservation checker verifies this after every edited file.

```
academic-latex-polish/
  SKILL.md                  instructions: writing rules, workflow, preservation checker
  scripts/check_preserve.py check that macros, refs, cites, labels, math and numbers survive an edit
  scripts/fix_tt_quotes.py  upright quotes inside \texttt{}; Unicode quotes/dashes -> LaTeX
  scripts/style_stats.py    compare sentence length, parentheses and semicolons with published papers
```

### Install on another machine
- **Claude Code (CLI or desktop).** Clone this repository and copy the skill folder into your personal skills directory:
  ```bash
  git clone https://github.com/wanghongsheng01/claude-skills.git
  mkdir -p ~/.claude/skills && cp -r claude-skills/academic-latex-polish ~/.claude/skills/
  ```
  To make it available in one project only, copy it to `<project>/.claude/skills/` instead.
- **claude.ai.** Zip the `academic-latex-polish` folder and upload it under Settings → Capabilities → Skills, or ask Claude in a chat to install it from this repository.

### Use
Ask Claude to "polish the paper with academic-latex-polish", or invoke the skill by name. The scripts are run as:
```bash
python3 academic-latex-polish/scripts/check_preserve.py OLD.tex NEW.tex
python3 academic-latex-polish/scripts/fix_tt_quotes.py sections/*.tex
python3 academic-latex-polish/scripts/style_stats.py refpapers/* paper/
```

## amp-figure-design
AMP (antimicrobial peptide) / protein-generative-model paper figure design conventions. Use when creating or revising figures for AMP papers submitted to Briefings in Bioinformatics, Nature Biomedical Engineering, Nature Communications, Cell, Science, or Nature Methods. Grounded in 13+ published papers (Das 2021, Wan 2024, HydrAMP, Diff-AMP, AMPSphere, ESMFold, DOME).

```
amp-figure-design/
  SKILL.md                        core rules: color, panel labels, typography, grid figure do/don't
  references/design-conventions.md full observations with paper + figure number
  references/color-palette.md     hex values for every color
  assets/matplotlib_style.py     reusable matplotlib rcParams template
```

### Install on another machine
```bash
git clone https://github.com/wanghongsheng01/claude-skills.git
mkdir -p ~/.claude/skills && cp -r claude-skills/amp-figure-design ~/.claude/skills/
```

### Use
Ask Claude to "design this AMP figure following amp-figure-design", or invoke the skill by name. The skill offers observed examples rather than venue-wide prohibitions:
- choose a table, dot matrix or heatmap according to the data and research question;
- use semantic, readable colors and inspect labels at final size;
- keep compared quantities, experimental units and uncertainty explicit;
- learn from bbac343's controlled-design diagram, paired comparisons and complete heatmap matrix.

## bib-amp-evidence-writing
Review and revise AMP evaluation/generation papers for *Briefings in Bioinformatics*. This skill connects paragraph structure to scientific questions, keeps reconstruction/generation/activity evidence distinct, verifies references against primary sources and separates reviewer and editor roles when independent review is requested. It includes original analysis of all 37 scientific paragraphs in bbac343, actual figure/table observations, public-review search limits and a measured seven-paper bibliography/length sample. Counts are observations, not acceptance thresholds.

```
bib-amp-evidence-writing/
  SKILL.md                              concise workflow and evidence boundaries
  references/bbac343-writing-experiment-map.md  original paragraph/figure/experiment analysis
  references/source-verification.md     citation ledger and public-review identity checks
  references/review-editor-workflow.md   independent review, revision and recheck
  references/bib-publication-sample.md   seven verified publication records with counting limits
  scripts/check_citation_closure.py     offline direct-cite/bibitem coverage checker
```

```bash
python3 bib-amp-evidence-writing/scripts/check_citation_closure.py --tex paper/main.tex --out closure.json
```

The checker verifies explicit citation-key closure; it does not establish bibliographic truth or support for a scientific claim. Install only when requested, using the same folder-copy approach described above.

## information-systems-submission
Pre-submission checklist (投稿前须知) for the Elsevier journal *Information Systems* (ISSN 0306-4379, CCF B). Scope test, required files, elsarticle formatting, highlights, exact declaration wording (CRediT, competing interests, data availability, generative AI), reproducibility programme and portal steps. Rules are tagged [GUIDE] (read from the Guide for Authors on 2026-10-21), [ELSEVIER] or [CHECK].

```
information-systems-submission/
  SKILL.md                      checklist with VERIFIED / ELSEVIER / CHECK status and sources
  scripts/check_submission.py   checks a LaTeX folder: journal line, abstract words, keywords, declarations,
                                AI heading, citations, labels, figure files, highlights, forbidden codes
  references/verification-log.md what was readable on which date and how to update the skill
```

```bash
python3 information-systems-submission/scripts/check_submission.py paper/ --main main.tex \
        --highlights highlights.txt --forbid 'OLDJOURNAL|ProjectCode'
```

## information-systems-writing
Writing guide for *Information Systems* papers in data quality, data cleaning, entity resolution, benchmarking and reproducibility. Built from published IS papers (measured register, title, abstract and introduction moves, results and limitations style, captions, references) plus the rules of `academic-latex-polish`. Includes an AI-flavor and register checker and a matplotlib style for figures.

```
information-systems-writing/
  SKILL.md                         title, abstract, section plan, language targets, anti-AI-flavor rules,
                                   figures, references, highlights, final checklist
  scripts/is_style_check.py        sentence length, long sentences, parentheses, semicolons, negations,
                                   em dashes, AI-tell words and internal codes, per section
  references/observed-papers.md    the surveyed IS papers with DOIs and observations
  assets/is_figure_style.py        matplotlib defaults, colour-blind-safe palette, box/arrow helpers
```

```bash
python3 information-systems-writing/scripts/is_style_check.py paper/main.tex --codes 'P19|v[0-9]+'
```

## information-systems-portal
Submission-portal companion for *Information Systems* (投递 Information Systems 投稿窗口). Use it when the manuscript is ready and is about to be entered at https://submit.elsevier.com/INFOSYS. It builds the required Abstract file and page-by-page answers for all ten portal steps directly from `main.tex`, verifies the Overleaf-compiled PDF, and records the portal's traps (required Abstract upload, the "no competing interests" checkbox, many-file supplementary zips, stale Overleaf compiles). The full classification list is included, so no portal screenshots need to be parsed.

```
information-systems-portal/
  SKILL.md                         ten portal steps, upload folder layout, traps, consistency checks
  scripts/build_portal_kit.py      main.tex -> 00_Abstract/Abstract.docx + PORTAL_ANSWERS.md (every field)
  scripts/verify_final_pdf.py      fonts, ??/placeholders, expected/forbidden text, diff vs previous build,
                                   zip-vs-current main.tex
  references/classifications.md    the portal's fixed classification list and picks by paper type
```

```bash
python3 information-systems-portal/scripts/build_portal_kit.py --tex paper/main.tex --out upload_ready \
        --highlights paper/highlights.txt
python3 information-systems-portal/scripts/verify_final_pdf.py --pdf upload_ready/01_Manuscript/Manuscript.pdf \
        --expect "latest edited sentence" --previous old/Manuscript.pdf \
        --zip upload_ready/02_LaTeX_source/LaTeX_source.zip --tex paper/main.tex
```

Language convention for all three *Information Systems* skills: English for everything reviewers, editors or the portal see; Chinese for reports to the author.

Order of use for an *Information Systems* paper: `information-systems-writing` while writing, `information-systems-submission` to prepare and review the package, `information-systems-portal` at the upload step.

Install any of these skills like the others: `cp -r claude-skills/<skill> ~/.claude/skills/`.

## submit-eswa
Submission guide (投稿 ESWA 指南) for the Elsevier journal *Expert Systems with Applications* (ISSN 0957-4174). Built from the live 2026 Guide for Authors, read in full on 2026-10-29: scope test, **double-anonymized** review (separate title page and anonymized manuscript), APA author–year references (`elsarticle` + `authoryear` + `model5-names.bst`), the 250-word abstract limit, 1–7 keywords, highlights of at most 85 characters, Figure_N artwork files, Option C research data, exact declaration wording, Editorial Manager upload items, APC, timelines and desk-reject prevention.

```
submit-eswa/
  SKILL.md                          rules tagged [GUIDE]/[SD]/[EM]/[CHECK], workflow, checklist
  scripts/check_eswa_submission.py  LaTeX checker: journal line, author-year setup, bare \cite, abstract, keywords,
                                    scope words, anonymity (identity regex over all source files), declarations,
                                    labels, figure names, highlights, title page
  scripts/verify_eswa_pdf.py        PDF metadata/text identity scan, ??/placeholders, Type 3 or unembedded fonts,
                                    expected/forbidden text, stale-build check (pypdf)
  scripts/make_docx.py              Markdown-lite -> .docx (title page, highlights, cover letter, responses)
  assets/manuscript_skeleton.tex    anonymized ESWA manuscript skeleton
  assets/title_page_template.md     title page with everything the guide requires
  assets/model5-names.bst           Elsevier APA-style (name-year) BibTeX style (LPPL)
  references/guide-digest.md        section-by-section digest of the guide
  references/verification-log.md    what was read when; how to refresh
```

```bash
python3 submit-eswa/scripts/check_eswa_submission.py paper/ --main manuscript.tex --bib references.bib \
  --title-page title_page.md --highlights highlights.txt --identity 'Surname|University|github-user' --forbid 'Old Journal'
python3 submit-eswa/scripts/verify_eswa_pdf.py --pdf Manuscript.pdf --identity 'Surname|University|github-user'
```

## write-eswa
Writing guide (ESWA 写作指南) measured on 251 ESWA papers (OpenAlex/Crossref) and 10 full texts: title length and patterns, abstract moves, introduction plan (contribution bullets, roadmap, research questions), related-work comparison tables, method/setup/results/discussion structure, the experiments ESWA reviewers expect (repeated runs, significance, ablation, sensitivity, cost), figure and table practice, reference count (median 50–57), recency (57–64% from the last five years) and ESWA citations, and how to frame a method as an intelligent-system contribution with practical guidelines.

```
write-eswa/
  SKILL.md                              framing test, title, abstract, section plan, experiments, figures, references, style
  scripts/eswa_style_check.py           compares a manuscript with the observed ESWA shape
  references/observed-papers.md         surveyed papers with DOIs and observations
  references/eswa_stats_summary.txt     aggregated statistics
  references/eswa_title_abstract_ref_stats.csv, eswa_fulltext_survey.csv   raw data
```

```bash
python3 write-eswa/scripts/eswa_style_check.py paper/manuscript.tex --bib paper/references.bib
```

## review-eswa
Review guide (ESWA 审稿指南): how ESWA screens (editor desk check) and reviews (two or more reviewers, Accept/Minor/Major/Reject), with Elsevier's official reviewer criteria, publicly reported ESWA criticisms and timelines, each tagged by source reliability. Mode 1 runs an independent pre-submission self-review with editor and reviewer agents; Mode 2 helps a human reviewer draft an ESWA report within Elsevier's confidentiality and generative-AI rules; it also covers point-by-point responses to ESWA reviewers.

```
review-eswa/
  SKILL.md                         process facts, desk screen, reviewer checklist, editor decision, response practice
  scripts/review_packet.py         line-numbered reviewer packet (section map, captions, numeric claims, expanded macros)
  references/evidence.md           sources with URLs and reliability tags
  references/response_template.md  point-by-point response skeleton
```

```bash
python3 review-eswa/scripts/review_packet.py paper/manuscript.tex --out review_packet.md --numbers paper/tables/numbers.tex
```

Order of use for an ESWA paper: `write-eswa` while writing, `review-eswa` for the pre-submission review, `submit-eswa` to build, check and upload the package. Language convention for all three: English for everything the journal sees; Chinese for reports to the author.
## submit-dmkd
Submission guide (投稿 DMKD 指南) for the Springer journal *Data Mining and Knowledge Discovery* (ISSN 1384-5810 / 1573-756X). Article types and their judging criteria, the research-gap test, the Springer Nature `sn-jnl` template with author-year `sn-basic` references, abstract 150-250 words, 4-6 keywords, the mandatory Statements and Declarations, LLM disclosure in the Methods section, single-anonymous review, and the Snapp portal with its LaTeX zip rules. Rules are tagged [VERIFIED] (read on official pages on 2026-10-29), [SN], [INFERRED] or [UNKNOWN].

```
submit-dmkd/
  SKILL.md                          workflow, article types, format table, declarations, files, checklist
  scripts/check_dmkd_submission.py  checks a LaTeX folder: sn-jnl options, flat source, abstract, keywords,
                                    declarations, author-year bibitems, labels, figures, leftovers
  scripts/build_snapp_package.py    flat LaTeX zip + manifest with SHA-256 + upload list
  references/guide-digest.md        every rule with its source URL and tag
  references/snapp-walkthrough.md   portal steps and consistency checks (Chinese instructions)
  references/verification-log.md    what was read when, what is still unknown
```

```bash
python3 submit-dmkd/scripts/check_dmkd_submission.py paper/ --main main.tex --forbid 'Information Systems|elsarticle'
python3 submit-dmkd/scripts/build_snapp_package.py paper/ --main main.tex --out upload/ --pdf paper/main.pdf
```
The Springer class file is not included; download the template from https://www.springernature.com/gp/authors/campaigns/latex-author-support.

## write-dmkd
Writing guide (Write-DMKD 写作指南) built from 30 published DMKD papers (22 evaluation, benchmark and methodology papers; 8 method papers): titles, abstracts, the eight introduction moves with research questions, related work, definitions, experiments and statistics, seven ways DMKD evaluation papers argue generality across domains, results, threats to validity, figures, references and length, plus a section on repositioning database-venue papers for DMKD.

```
write-dmkd/
  SKILL.md                         rules with counts and the papers they come from
  scripts/dmkd_structure_check.py  compares a manuscript with the observed DMKD medians and checks register
  references/observed-papers.md    full observations with DOIs
  references/dmkd_paper_survey.csv one row per surveyed paper
```

```bash
python3 write-dmkd/scripts/dmkd_structure_check.py paper/main.tex
```

## review-dmkd
Simulated DMKD review (Review-DMKD 审稿指南): editor-in-chief desk screen, two or three independent reviewer personas scored on seven weighted criteria, an action-editor decision rule, the 25 most likely objections ranked by evidence, and what made accepted no-new-algorithm DMKD papers work. DMKD reviews are closed, so the form is derived from the journal's criteria, the ECML PKDD journal-track call, current action editors' public writings and 13 accepted DMKD precedents; inferences are labelled.

```
review-dmkd/
  SKILL.md                       procedure, criteria and weights, objections, precedents
  assets/review_form.md          reviewer report template
  assets/desk_screen.md          editor-in-chief screen
  references/evidence-notes.md   sources and evidence, with tags
```

Order of use for a DMKD paper: `write-dmkd` while writing, `review-dmkd` before submission, `submit-dmkd` to build and check the package and at the portal. Language convention: English for everything reviewers, editors or the portal see; Chinese for reports to the author.

## submit-dse
Submission guide (投稿 DSE 指南) for the Springer journal *Data Science and Engineering* (CCF B). Double-blind anonymization of the manuscript and supplements, separate title page, sn-jnl with numeric citations (39/39 published articles), declarations, LLM disclosure, Online Resource files, Editorial Manager portal, APC.

```
submit-dse/
  SKILL.md                         workflow, scope test, blinding checklist, format table, files, fees, checklist
  scripts/check_dse_submission.py  checks template, blinding, abstract, keywords, figures, references, leftovers
  scripts/build_em_package.py      flat LaTeX zip + SHA-256 manifest
  references/                      guide digest, verification log, portal notes
  assets/title_page_template.md
```

## write-dse
Writing guide (Write-DSE 写作指南) built from 39 published DSE articles: titles, abstracts, structure, experiments, limitations, references, repositioning an audit paper.

```
write-dse/
  SKILL.md
  scripts/dse_structure_check.py   compares a manuscript with DSE medians and counts hedging phrases
  references/dse_paper_survey.csv  one row per article
  references/observed-papers.md    closest models with DOIs
```

## review-dse
Simulated DSE review (Review-DSE 审稿指南): desk screen, independent reviewer personas, seven criteria, associate-editor letter, fix list. No public DSE reports exist, so inference is labelled.

```
review-dse/
  SKILL.md
  assets/review_form.md, assets/desk_screen.md
  references/evidence-notes.md
```

Order of use for a DSE paper: `write-dse` while writing, `review-dse` before submission, `submit-dse` to build and check the package and at the portal. Language convention: English for submitted material, Chinese for reports to the author.

## submit-ipm
Submission guide (投稿 IPM 指南) for *Information Processing & Management*: scope test, double anonymization, the no-preprint rule, exact declaration wording, required CRediT, `[dataset]` placement, the new submission service, fees and timelines. Portal details not yet seen are tagged [CHECK].

```
submit-ipm/
  SKILL.md                          rules with source tags, workflow, checklist
  scripts/check_ipm_submission.py   LaTeX folder checker
  scripts/verify_ipm_pdf.py         PDF anonymity and font checker
  scripts/make_docx.py              Markdown-lite to .docx
  assets/                           manuscript skeleton, title page template, model5-names.bst
  references/guide-digest.md        every rule with URL and tag, full [CHECK] list
  references/verification-log.md    what was read when
```

## write-ipm
Writing guide (Write-IPM 写作指南) from counts over 1,497 IPM articles and 9 full texts: framing, method versus evaluation conventions, abstracts, two-level measurement, implications, limitations, references.

```
write-ipm/
  SKILL.md                          rules with counts
  scripts/ipm_style_check.py        compares a manuscript with the observed shape
  references/observed-papers.md     observations with DOIs and evidence tiers
  references/ipm_paper_survey.csv   one row per surveyed paper
```

## review-ipm
Simulated IPM review (Review-IPM 审稿指南): editor desk screen, reviewer personas, likely questions, decision letter and fix plan, an integrity pass, and responses to reviewers. No public IPM reviewer form exists, so this is an assembled checklist.

```
review-ipm/
  SKILL.md                         procedure and questions
  scripts/review_packet.py         builds a numbered reviewer packet from .tex
  references/evidence.md           sources and tags
  references/response_template.md  response skeleton
```

Order of use for an IPM paper: `write-ipm` while writing, `review-ipm` before submission, `submit-ipm` to build and check the package.
