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

## submission-integrity-check
The final gate before a paper is uploaded. It answers four questions about the exact PDF:
- Does it follow every must-follow item of the call?
- Is every reference correctly formatted?
- Does every cited work exist, with the title, authors, year and venue the bib entry gives? This catches invented or mangled references.
- Does every citing sentence describe the cited work correctly?

The ICDE 2027 profile encodes the research-track call as re-read on 2026-11-11:
- IEEEtran conference template;
- 12 body pages, excluding the references and the AI-generated-content declaration;
- no appendix;
- PDF of at most 20 MB, US Letter;
- single-blind author block;
- mandatory AI declaration;
- EAB title tag;
- public artifact URL;
- no spacing or margin hacks.

References are checked online against Crossref, OpenAlex, arXiv and the entry's own URL.

```
submission-integrity-check/
  SKILL.md                              workflow, verdicts, fix-and-rerun loop, lessons
  profiles/icde2027.json                venue rules (copy for another venue)
  references/icde2027-must-follow.md    the call's must-follow items with sources and consequences
  references/rules.md                   rule ids C01-C12 and reference verdicts
  scripts/compliance_check.py           call rules on the source and the PDF (needs PyMuPDF)
  scripts/ref_check.py                  bib format lint + online existence check (cached), optional scratch compile
  scripts/cite_contexts.py              worksheet: each citing sentence next to the cited work's record and abstract
  scripts/texbib.py                     shared LaTeX/BibTeX helpers
```

### Use
```bash
python3 submission-integrity-check/scripts/compliance_check.py paper/ --pdf paper.pdf --profile icde2027 [--eab] --out out/
python3 submission-integrity-check/scripts/ref_check.py paper/ --out out/ --compile
python3 submission-integrity-check/scripts/cite_contexts.py paper/ --refcheck out/refcheck.json --out out/cite_worksheet.md
```
Then judge every non-VERIFIED reference and every citing claim (OK / IMPRECISE / WRONG), fix, and re-run. Install like the other skills (`cp -r submission-integrity-check ~/.claude/skills/`).

## manuscript-proofcheck
Reviews and corrects the typesetting, rendering, bibliography and mechanical writing of any LaTeX paper before submission, for any venue. It lints the source, checks the compiled PDF (wrong glyphs, unresolved references, leftover TODO or red text, placeholder author blocks, dashes for repeated authors, title breaks, tables or text past the margin, fonts, body pages) and renders every page for a visual pass. A writing-mechanics pass checks that names, counts, symbols and generated numbers are consistent across text, tables and figures. It also verifies every bib entry online and fixes the source with minimal edits. Its defect catalog grows with every paper. It does not change claims or numbers; use the venue's review skill for content.

```
manuscript-proofcheck/
  SKILL.md                     workflow, per-page visual checklist, reporting rules
  references/defect-catalog.md cause, detection and fix of each defect class (T* source rules, P* PDF rules)
  scripts/tex_lint.py          source lint: \mathbb 1 glyph, amsthm under IEEEtran, IEEEtran dash for repeated names,
                               title line breaks, TODO, spacing hacks, tall inline math, bib year/author/key problems
  scripts/pdf_check.py         compiled-PDF checks (needs PyMuPDF) and page PNGs for the visual pass
```

### Use
```bash
python3 manuscript-proofcheck/scripts/tex_lint.py paper/
python3 manuscript-proofcheck/scripts/pdf_check.py paper.pdf --out /tmp/proof --body-limit 12
```
Then inspect every page PNG, verify the bibliography online, fix, and re-run. Install like the other skills (`cp -r manuscript-proofcheck ~/.claude/skills/`).

## results-presentation-review
A senior co-author's lens on the experiments section of an ICDE/VLDB/SIGMOD paper. It checks what a reader sees in
the first two minutes of the figures and tables, and whether the text explains where the method wins and where it
loses. The rules come from two rounds of a senior co-author's review of ICDE 2027 Round 2 manuscripts.
`results_lint.py` reads the LaTeX sources, the figure scripts and the figure PDFs and flags:
- S01: captions that are too long;
- S02: captions that do not open with the claim;
- S03/S04: tables without a bold best and underlined second best, or without a count row;
- S05: mixed decimals;
- S06: ablation tables without a visible average row;
- S07: baselines that win rows with no sentence explaining why;
- S08: mean bars on skewed strip plots;
- S09: unexplained empty bands in scatter panels;
- S10: missing takeaways or a missing where-it-wins/loses paragraph;
- S11: dataset tables with constant columns or a caption that never says what the table shows about the method.

The `write-icde`, `review-icde`, `submit-icde` and `manuscript-writing-review` workflows run it.

```
results-presentation-review/
  SKILL.md                      rules S01-S11, workflow, generator-side recipes, page budget
  references/round2-lessons.md  worked case (Ladder, ICDE 2027 R2), template sentences for win/loss analysis
  references/authz-round2-lessons.md  worked case (AuthZ-Graph, ICDE 2027 R2): dataset table, why LCR wins, captions
  scripts/results_lint.py       checker (needs PyMuPDF for the figure check)
```

### Use
```bash
python3 results-presentation-review/scripts/results_lint.py paper/ --method Ladder --figscripts code/make_figs.py
```
Install like the other skills (`cp -r results-presentation-review ~/.claude/skills/`).

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
## submit-ml
Submission guide for the Springer journal Machine Learning: Contribution Information Sheet, sn-jnl port, reference, figure and declaration rules.

## submit-kbs
Submission guide for the Elsevier journal Knowledge-Based Systems: guide-for-authors rules, elsarticle traps and the seven steps of Elsevier's new submission service, recorded on a real submission. The steps cover the 5-keyword limit, the competing-interest declaration tool and the data link.

## ICDE skills (IEEE ICDE research track, CCF A)
Six skills that cover one complete ICDE submission, built for ICDE 2027 Round 2 from the official CFP, all 1058 research papers of ICDE 2024–2027 R1, and 21 deep-read accepted papers. Use them in this order:

| Skill | Stage | Contents |
|---|---|---|
| `submit-icde` | guideline check, submission, rebuttal, camera-ready | CFP rules re-checked 2026-11-06 (rounds, 12 pages without appendix with only references and AI acknowledgment excluded, single-blind, stricter COI reading, CMT order of operations, AI disclosure, artifacts, scope), rebuttal (new in 2027) and camera-ready (IEEE CPS, PDF eXpress, eCF). `scripts/check_icde_submission.py` adds spacing-hack, title/abstract, template-text, font and body-end checks. Templates for the AI disclosure, scope statement and rebuttal; EAB Round 2 guide with cited rules (`references/eab.md`) and an EAB/artifact mode in the checker |
| `survey-icde` | direction survey | classified list of 1058 accepted papers, topic shares 2024–2027R1, scripts to repeat the survey |
| `read-icde` | deep reading | note template, 21 notes, 4 group syntheses, cross-group rules on problems, methods, experiments, writing, acceptance |
| `experiment-icde` | idea and real experiments | gap → hypothesis → pilot → experiment matrix; label-once/replay-many design; key-free cached LLM client; full example code |
| `icde-cmt-submission` | submission | prepares every field of the ICDE CMT "Create New Submission" page from the paper (title, plain-text abstract checked against the PDF, authors, subject areas, file, TPMS, ten additional questions with the Relevance and Availability texts) and checks limits before Submit (`scripts/prepare_cmt.py`) |
| `icde-subject-areas` | submission | picks the CMT "Subject Areas" (one Primary, 2-3 Secondary) for an ICDE paper: exact ICDE 2027 CMT list (29 areas + None Of Above, checked 2026-11-11), selection rules, and `scripts/suggest_areas.py`, which scores the areas from the LaTeX sources or the PDF and shows the evidence |
| `write-icde` | writing | paragraph-level guide; how to state limitations without self-negation, from 10 accepted cohesive-subgraph papers (`references/limitations-writing.md`); math, figure and table readability; `scripts/icde_structure_check.py`, which also flags self-negating wording and failure headings; EAB writing guide from 16 accepted EAB/benchmark papers (`references/eab.md`): titles, abstracts, RQs/findings, reporting, ten limitation patterns; reachability-index/IVM/access-control limitations corpus from 11 accepted papers (`references/limitations-writing-reachability.md`); baselines, hand-set constants and setup disclosures from 10 accepted papers (`references/limitations-writing-baselines-constants.md`) |
| `review-icde` | independent review and revision | 18-row desk screen, simulated review form (ICDE publishes none), reviewers may request added, supplemented, re-run or removed experiments and authors run them, a limitations-presentation lens, discussion, rebuttal and re-scoring, EAB questions, meta-review, adversarial checks; EAB review form, checklist, rejection reasons and three-column limitations lens (`references/eab.md`) |

```
submit-icde/      SKILL.md  scripts/check_icde_submission.py  assets/{ai_disclosure_template.tex,scope_statement_template.md,rebuttal_template.md}  references/{requirements-recheck-2026-11-06.md,eab.md}
survey-icde/      SKILL.md  scripts/{parse_accepted,fetch_openalex,match,classify,llm}.py  references/{findings.md,icde_2024_2027r1_classified.csv,figs/}
read-icde/        SKILL.md  assets/reading_note_template.md  references/{cross_group_rules.md,group_*_synthesis.md,notes/}
experiment-icde/  SKILL.md  scripts/llm.py  scripts/example_ladder/
write-icde/       SKILL.md  scripts/icde_structure_check.py  references/{observed-structure.md,limitations-writing*.md,eab.md}
review-icde/      SKILL.md  assets/{review_form.md,desk_screen.md}  references/{reviewer-lens.md,eab.md}
```

Install:
```bash
git clone https://github.com/wanghongsheng01/claude-skills.git
mkdir -p ~/.claude/skills && cp -r claude-skills/{submit,survey,read,experiment,write,review}-icde ~/.claude/skills/
```
Use: ask Claude to "check the ICDE submission with submit-icde", "survey ICDE directions", or invoke a skill by name. Scripts that call LLMs read keys from a file named by `LLM_KEYS_JSON`, outside the repository.

## manuscript-writing-review
A mandatory gate between "the paper is written" and "the author gets the package". It compiles the
paper and checks every figure and every page. It looks for readability and layout defects that source
lints miss:
- heavy inline math that should be displayed;
- legends cut off at the canvas edge or drawn over bars;
- annotations over data labels;
- single-column tables running into the other column or past the margin;
- justified table cells with word gaps;
- wrapped algorithm comments;
- end-of-proof boxes read as garbled glyphs;
- internal remarks in bib notes.

It fixes causes in the generating scripts, then recompiles and re-checks until clean. It never hands
over an uncompiled package. Every rule comes from a defect that reached an author (see the defect
catalog).

```
manuscript-writing-review/
  SKILL.md                     hard rules, compile-check-fix loop, per-page checklist, reporting rules
  references/defect-catalog.md what the reader saw, cause, detection, fix (R*, F*, L* rules)
  scripts/review_lint.py       source: heavy inline math, broken formulas, QED policy, p{} columns, algorithm
                               comments, unreferenced equation numbers, wide one-column tables, bib notes,
                               legend placement in figure scripts
  scripts/fig_check.py         figure PDFs: text cut off at the canvas, text over text, text over bars
  scripts/layout_check.py      compiled PDF: text into the other column / past the margin, text over text,
                               figure text over bars or cut off, end-of-proof boxes, missing glyphs; page PNGs
```

### Use
```bash
python3 manuscript-writing-review/scripts/review_lint.py paper/ --figscripts code/make_figs.py
python3 manuscript-writing-review/scripts/fig_check.py paper/figs/*.pdf --png /tmp/figs
pdflatex main && bibtex main && pdflatex main && pdflatex main
python3 manuscript-writing-review/scripts/layout_check.py paper/main.pdf --out /tmp/pages   # then open every page
```
The PDF scripts need PyMuPDF (`pip install pymupdf`). Install as for the other skills: copy the folder into
`~/.claude/skills/`.

## Pattern Recognition research skills

Eight skills support preparation for Elsevier *Pattern Recognition* (ISSN 0031-3203). They separate official requirements, publication-title observations, full-text evidence and research judgments; publication frequency is not acceptance probability. The guideline snapshot was directly read on 2026-11-09 and must be refreshed before submission.

| Skill | Purpose |
|---|---|
| [pr-venue-gate](pr-venue-gate/SKILL.md) | Current venue requirements, evidence locations and guide conflicts |
| [pr-literature-map](pr-literature-map/SKILL.md) | Reproducible publication landscape with date, coverage and classification limits |
| [pr-evidence-reading](pr-evidence-reading/SKILL.md) | Scientific problem → key mechanism → experimental evidence → writing structure |
| [pr-opportunity-screen](pr-opportunity-screen/SKILL.md) | Closest-work challenges, falsifiable candidate questions and planning-only experiment protocols |
| [pr-experiment-design](pr-experiment-design/SKILL.md) | Falsifiable hypotheses, decisive controls and real run records after literature learning |
| [pr-paper-craft](pr-paper-craft/SKILL.md) | Claim-evidence writing, paragraphs, figures and tables |
| [pr-review-revision](pr-review-revision/SKILL.md) | Independent evidence review and concrete revision closure |
| [pr-submission-package](pr-submission-package/SKILL.md) | Editable manuscript, Highlights, cover letter, declarations and submission-state checks |

Follow the user's requested stage: a request to learn published work first does not start experiments merely because model APIs are available. These skills contain reusable methods and public references, not private research data, API credentials or third-party paper PDFs. Copy the desired skill folders into the personal skills directory of the assistant being used.

## PVLDB, SIGMOD Industrial, TKDE, and baseline absorption (2026-11-12)

Four skills added for CCF-A data-management writing. They do **not** replace or edit the existing ICDE skills. Official dates and page limits were checked on 2026-11-12 and must be re-read on the official pages before submission. Presentation rules are Deng S01–S11 (`results-presentation-review`). These skills do **not** include a new full-PDF census of VLDB 2025–2026; structural habits are cross-referenced from `write-icde`, and `baseline-paper-absorption` is the process for doing a real sample later.

```
write-vldb/                      PVLDB Vol. 20 / VLDB 2027: monthly deadlines, 12-page body, single-blind,
  SKILL.md                       author caps, EA&B package at initial submission
  references/official-rules.md   snapshot of official URLs and numbers (re-read before use)
write-sigmod-industrial/         SIGMOD 2027 Industrial: 2026-11-24 23:59 AoE, 12 pages + unlimited refs,
  SKILL.md                       not double-blind, non-academic author, honest deployment scope
  references/official-rules.md
write-tkde/                      IEEE TKDE rolling journal: completeness, no dual submission with PVLDB;
  SKILL.md                       page limits must be re-read on the IEEE CS author page
  references/official-rules.md
baseline-paper-absorption/       Process: select official TOC → per-paper notes (title, outline, captions,
  SKILL.md                       citations, limitations) → aggregate → optionally update a venue skill
  references/this-turn-honesty.md
```

### Install
Copy the skill folder into the assistant’s skills directory, same as the other skills:

```bash
git clone https://github.com/wanghongsheng01/claude-skills.git
mkdir -p ~/.claude/skills
cp -r claude-skills/write-vldb ~/.claude/skills/
cp -r claude-skills/write-sigmod-industrial ~/.claude/skills/
cp -r claude-skills/write-tkde ~/.claude/skills/
cp -r claude-skills/baseline-paper-absorption ~/.claude/skills/
```

### Use
Ask to “write the paper with write-vldb” (or write-sigmod-industrial / write-tkde), and always also apply `results-presentation-review` and `academic-latex-polish`. For ICDE, keep using `write-icde` / `review-icde` / `submit-icde`. To study accepted papers’ writing before extending a skill, invoke `baseline-paper-absorption` and record the sample size honestly.

## Advisor-guided presubmission review (2026-11-12, added on this branch)

A fifth skill on this branch, still **without** modifying any previously existing skill.

```
paper-presubmission-review/          Advisor-guided self-check used before submission or a
  SKILL.md                           co-author review: SOTA-at-a-glance tables, decimals/units/fonts,
  references/venue-conflicts.md      no experiment-log tables, title and EAB tags, appendix and
  references/advisor-sources.md      related-work placement, public-data confirmation, international
  references/checklist-recipes.md    LLM baselines, novelty story. Every item is tagged (邓/梁/附件)
                                     and judged against official CFPs (VLDB, SIGMOD Industrial,
                                     ICDE, TKDE, KDD). Official pages win on conflicts.
```

Official URLs and conflict rulings were checked on **2026-11-12** and must be re-read before use. This skill complements, and does not replace, `results-presentation-review`, `write-vldb`, `write-sigmod-industrial`, `write-tkde` and the ICDE skill family.

### Install (same pattern)
```bash
cp -r claude-skills/paper-presubmission-review ~/.claude/skills/
```

### Use
Ask to “run the presubmission review / 投稿前自审” for a named venue. The skill produces a Chinese report with a SOTA 总表 and a conflict log. Apply presentation fixes in the table generator; do not change experimental numbers or frozen author lists.

## Advisor meeting lessons and CCF-A submission commander (2026-11-12)

- `paper-presubmission-review` now includes **邓-会议** items distilled from six meeting records (average row, empty-region captions, Figure 1 gap marks, dataset-only tables, 10-minute LLM-assisted review, one Overleaf+Git). Quotes: `paper-presubmission-review/references/deng-meeting-lessons.md`.
- `write-vldb` §7 (additive) and `write-vldb/references/deng-meeting-experiment-analysis.md` apply the same experiment-analysis lessons under PVLDB's 12-page-including-appendix rule. Existing §§1–6 and `official-rules.md` are unchanged.
- New skill **`ccfa-submission-workflow`**: a submission-prep commander playbook from Dr.Wang's ICDE 2027 R2 process log, generalized to other CCF-A venues. It orchestrates the venue skills and `paper-presubmission-review`; it does not replace them. Historical wording that "acceptance, not honesty, is the first priority" is **not** adopted.

## Experiment-analysis writing from a 12-paper PVLDB sample (2026-11-12)

Additive follow-up (this branch). Does **not** modify `paper-presubmission-review`, `ccfa-submission-workflow`, or `write-vldb` §§1–7 / `official-rules.md`.

- New skill **`experiment-analysis-writing`**: how to write first-place (component–problem–ablation) and second-place (winner mechanism, regime, choice rule) evaluation paragraphs, Lessons, captions, and titles. Distilled from 12 official PVLDB Vol. 17–19 PDFs (NL2SQL, SemBench, MV rewriting, k-plex, columnar EA&B) plus 邓老师's meeting guidance. Paper list and habits: `experiment-analysis-writing/references/pvldb-sample-2023-2026.md`.
- **`write-vldb` §8** (additive) and `write-vldb/references/experiment-analysis-from-pvldb-2023-2026.md` point at that skill. The previous honesty note that this skill “did not claim a new full-text census” is updated for the *evaluation* section only; title/abstract/introduction structure is still started from `write-icde`.

### Install
```bash
cp -r claude-skills/experiment-analysis-writing ~/.claude/skills/
# write-vldb is already installed; re-copy to pick up §8
cp -r claude-skills/write-vldb ~/.claude/skills/
```

### Use
When writing a PVLDB (or other CCF-A) evaluation section, run `write-vldb` (or the venue skill) and `experiment-analysis-writing`. Before submission, still run `paper-presubmission-review` and `results-presentation-review`.

## PVLDB and SIGMOD venue skills (submit / write / review, 2026-11-12)

Six new skills for PVLDB Volume 20 and SIGMOD (Industrial 2027, and research for later cycles). They follow the structure of `submit-icde`, `write-icde` and `review-icde`. Official pages were read on **2026-11-12 PT** and always win; each skill records URLs and the access date in `references/`. They **do not replace** the ICDE family. For new PVLDB or SIGMOD drafts they **cover and extend** the shorter `write-vldb` and `write-sigmod-industrial` (those skills are kept). They also reuse, and do not edit, `ccfa-paper-front-loaded-research`, the B1/B2 writing skills, `experiment-analysis-writing`, and the ICDE limitation-writing corpora.

The **write** skills include a dedicated guide on stating limitations, losses and not-done work **without self-negation**, based on counts from accepted PVLDB, SIGMOD, ICDE and VLDBJ papers (0/10 algorithm abstracts and conclusions state a loss of the authors' method; 0/9 EAB papers put limits of their own benchmark there). This changes wording, placement and frequency only: numbers, losing cells, and venue-mandatory statements stay. It is not a licence to hide facts.

- **`submit-pvldb`**: Volume 20 guidelines — four categories and page limits (regular/EA&B 12 pages excluding only references), mandatory abstract on the 25th and full paper on the 1st at 17:00 PT, monthly cap of two and yearly cap of twelve, single-blind, CMT `PVLDBv20_2027`, COI, related-submission declaration, Scope Policy and SAR, EA&B full reproducibility package at the **initial** submission, Light Load Reviewer nomination, 12-month embargo, ACM AI policy.
- **`write-pvldb`**: titles, abstracts, introductions, theorems, RQ-structured experiments, W/T/L tables, EA&B writing, and §7 limitation-writing rules (R1–R11) with English templates and a ban-list of self-negating phrases.
- **`review-pvldb`**: official process (AE, ≥3 reviews, one revision), EiC letters on desk-rejects (Vol. 18–19 front matter), common revision requests, permission to ask for added or dropped experiments, and a mandatory self-negation pass. For pre-submission self-review, not a real PC assignment.
- **`submit-sigmod`**: SIGMOD 2027 Industrial (12 pages + unlimited references, not double-blind, non-academic author required, CMT `SIGMODIND2027`, deadline 2026-11-24 23:59 AoE = 2026-11-25 19:59 Beijing) and a snapshot of the research track (already closed for 2027; double-anonymous, separate appendix, author feedback) for later cycles.
- **`write-sigmod`**: industrial structure (what is or is not in production, lessons as first-class, weak cells as operating guidance, public-data confirmation) and research-track writing aligned with `write-pvldb`, including the same limitation rules.
- **`review-sigmod`**: industrial dimensions (fit, overclaim, public confirmation, lessons), PACMMOD/SIGMOD official allowed and disallowed revision requests, and the self-negation pass (e.g. a 0.9× cell must stay, must not be repeated five times).

```
submit-pvldb/     SKILL.md  references/official-pages-2026-11-12.md
write-pvldb/      SKILL.md  references/limitations-without-self-negation.md
review-pvldb/     SKILL.md  references/official-process-2026-11-12.md
submit-sigmod/    SKILL.md  references/official-pages-2026-11-12.md
write-sigmod/     SKILL.md
review-sigmod/    SKILL.md  references/official-process-2026-11-12.md
```

### Install
```bash
cp -r claude-skills/submit-pvldb claude-skills/write-pvldb claude-skills/review-pvldb \
      claude-skills/submit-sigmod claude-skills/write-sigmod claude-skills/review-sigmod \
      ~/.claude/skills/
```

### Use
Ask to “prepare a PVLDB submission with submit-pvldb”, “write the paper with write-pvldb” (including “how to state limitations without self-negation”), or “run a simulated PVLDB review with review-pvldb”. For SIGMOD Industrial, use the `*-sigmod` triple. Re-read the official CFP of that cycle before every submission. For a plan-only task, the review skill reports and does not edit the manuscript until the author approves.

## ccfa-paper-front-loaded-research
Front-loaded research gate for any new CCF-A paper: stages 1–6 (template, venue fit, problem/SOTA/datasets, opportunity/novelty, type-specific reading, research and experiment plan) must finish and pass quality gates before methods or experiments start. The coauthor briefing PDF is a product of this process, not a post-hoc wrap. Companion file: `paper_reading_清单.md` (16 officially published PVLDB papers in the first tranche).

## ccfa-b1-method-writing
Lessons from formally published PVLDB 2024–2026 method papers (Sphinteract, REDSQL, LLM-R2, Magneto, CHORUS, OpenForge). SOTA gate on a majority of pre-registered metrics; constructed strongest controls; losses explained once; official fold not retuned.

## ccfa-b1-benchmark-writing
Lessons from formally published PVLDB EA&B and diagnosis papers (Dawn NL2SQL, DAIL-SQL, TACO, SemBench, Annotation Errors, plus NL2SQLBench, an MV pipeline paper, ELT-Bench). Insight plus a reproducible protocol; do not claim “our method is #1” as the paper’s contribution.

## ccfa-b2-first-problem-definition
Lessons from formally published papers that introduce a setting or task (SPADE, SIC, and the class/setting definitions in SemBench, TACO, ELT-Bench). Do not rename a known problem as a first definition.

## PVLDB paper craft (production pipeline, reviewer skim, layout, 2026-11-13)

Complementary to **`write-pvldb`** (section prose, W/T/L, limitation wording without self-negation) and **`submit-pvldb`** (official Volume 20 rules). This skill does **not** replace either, and this PR does **not** modify those folders.

- **`pvldb-paper-craft`**: end-to-end production pipeline (problem selection, SOTA/benchmark positioning, method design, experiment design, figures/tables, writing, self-review) with how each step is done in formally published PVLDB/SIGMOD papers; the reviewer’s 10–20 minute skim in the order **tables → figures → experiment analysis tied to each figure/table → title/abstract/intro**, plus how exemplars optimise for that skim; full paper anatomy, paragraph organisation, and a grounded what-NOT-to-write list; formula/figure/table/reference checklists; Volume 20 mandatory blocks (`\vldbtopmatter`, 12-page body, ALL-CAPS heads); a four-layer pre-delivery self-review protocol (compile log, 150 dpi visual pass, reviewer skim, consistency); and a read-only PDF layout lint.

```
pvldb-paper-craft/  SKILL.md  check_pdf_layout.py  check_pdf_layout.sh  requirements.txt
```

### Install
```bash
cp -r claude-skills/pvldb-paper-craft ~/.claude/skills/
# optional, for the layout lint:
pip install -r claude-skills/pvldb-paper-craft/requirements.txt   # pymupdf
```

### Use
Ask to “run the reviewer-skim and pre-delivery layout check with pvldb-paper-craft”, or lint a compiled PDF:

```bash
./pvldb-paper-craft/check_pdf_layout.sh paper.pdf --log main.log --out lint.txt
```

The lint is calibrated for letter, acmart two-column (612×792 pt). Errors (text overlap, margin overflow, tables at 6 pt) must be zero before delivery; warnings are inspected by eye. A 150 dpi pass on every page remains mandatory and is not replaced by the script.
