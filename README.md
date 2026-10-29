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
