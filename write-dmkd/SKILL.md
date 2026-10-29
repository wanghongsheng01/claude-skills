---
name: "write-dmkd"
description: "Writing guide for papers aimed at the Springer journal Data Mining and Knowledge Discovery (DMKD), built from 30 published DMKD papers (22 evaluation, benchmark and methodology papers, 8 method papers): titles, abstracts, introduction moves with research questions, related-work organization, definitions, procedure and experiment sections, how evaluation papers argue generality across domains, statistics, results, limitations, figures and tables, references and length. Use when drafting, restructuring or repositioning a manuscript for DMKD (写 DMKD / 改投 DMKD 写作), especially evaluation-methodology, benchmark, reproducibility or data-cleaning papers coming from database venues. Includes a structure checker."
---

# Writing for Data Mining and Knowledge Discovery (Write-DMKD 写作指南)

Evidence base: 30 DMKD papers published 2016-2026 (`references/dmkd_paper_survey.csv`, DOIs 10.1007/s10618-...), 28 read in full, plus the DMKD submission guidelines. `references/observed-papers.md` gives every observation with counts and DOIs; this file gives the rules. Counts such as "20/30" are observations, not acceptance thresholds.

Use with `submit-dmkd` (format, declarations, portal) and `review-dmkd` (simulated review before submission).

## Language convention (permanent agreement with the author)
Manuscript, captions, cover letter and responses to reviewers in **English**; notes, plans and reports to the author in **Chinese (中文)**.

## What DMKD reviewers read for first
The guidelines judge a Regular Paper on three questions, and the manuscript must answer each where a reviewer looks for it:
1. **Contribution clear from the abstract** → abstract sentence 3 or 4 states it in one sentence.
2. **A clearly defined research gap** that existing methods cannot address → introduction paragraph 3, phrased as a gap, not as "we propose".
3. **Experiments that answer clearly formulated research questions** → RQ1-RQn listed in the introduction and answered one-to-one, each results subsection ending with "The answer to RQk is ...".

## Title
- About 9-14 words with a colon (20/30 papers; median 10 words). Put the object or the named concept first and the genre after the colon.
- Evaluation papers name their genre (19/22): evaluation, benchmark(ing), review, comparative, pitfalls, challenges, taxonomy. Templates: "On the evaluation of X: ..."; "X: a review and experimental evaluation of ..."; "X: common pitfalls and best practices"; "Challenges in benchmarking X with real-world data".
- No product or tool names in an evaluation-paper title (0/22). Question titles are rare (1/30). A playful main title always has a literal subtitle.

## Abstract (150-250 words, journal rule)
Evaluation-paper median 232 words. Order:
1. one sentence of field context;
2. the gap as a list of concrete deficiencies (Campos et al. 2016 lists four, Bagnall et al. 2017 names three reasons earlier comparisons were incomparable);
3. what was done, with scale numbers (12/30 give counts of datasets, methods or runs);
4. the headline finding with its largest effect;
5. the generality claim;
6. a recommendation to the community (Sánchez Vinces et al. 2025: should be "included as baselines"; Bagnall et al. 2017: reproducibility).
No citations, no undefined abbreviations. Spell out tool names once or describe them ("the BART error generator").

## Keywords
4-6 (journal rule). Evaluation papers include "Evaluation" or a close variant plus the task name (Campos 2016: Unsupervised outlier detection; Evaluation; Measures; Datasets).

## Introduction (8 moves)
1. Context: why the task is compared on benchmarks.
2. A concrete motivating failure: one paragraph, one number.
3. The gap as a list of deficiencies, and why existing studies do not close it.
4. The paper's angle, with the named concept (give the problem a name: "data documentation debt", "pooling bias", "comparison contract").
5. Explicit research questions, RQ1-RQ4 (6/20 evaluation papers do this; it is criterion iii).
6. A contribution list of 4-6 items, the last being the released artifact (16/28).
7. One sentence on reproducibility.
8. A roadmap (21/28).
Declare any earlier version (conference or workshop) here and in the cover letter.

## Related work
Section 2 (16/28 call it "Related work"; others use "Background"). Organize by category, not chronology, and end each subsection with one sentence on how this paper differs. For a paper arriving from database venues, the first subsection should be **evaluation methodology and benchmark validity in data mining**: Keogh and Kasetty 2003; Campos et al. 2016; Bagnall et al. 2017; Souza et al. 2020; Fabris et al. 2022; Hewamalage et al. 2023; Marques et al. 2023; Sørbø and Ruocco 2024; Middlehurst et al. 2024; Demšar 2006; Berrar 2022. Keep the database core: 15/22 DMKD evaluation papers cite VLDB/SIGMOD/ICDE/EDBT work.

## Definitions and procedure
- 13/28 papers have numbered Definitions or a notation section. Make the named concept a Definition, and state desired properties before testing against them (Sørbø and Ruocco 2024 list ten properties; Röchner et al. 2024 require sharpness, refinement and calibration).
- Protocol papers present the evaluation procedure as the method (Grzenda et al. 2020; Le et al. 2023). Close with implementation details and reproducibility (Middlehurst et al. 2024 §3.2; Sánchez Vinces et al. 2025 §1.3).
- If LLMs were used, say so in the Methods section (journal rule); keep it factual and short.

## Experiments
- Several datasets are the norm; a single case study is rare (1/28). State selection criteria early (Middlehurst et al. 2024 give three inclusion criteria).
- Include simple baselines; reviewers ask "is there an easier way?".
- **Statistics, proportionately.** Where methods are ranked over many datasets: Friedman/Wilcoxon with Holm, critical-difference diagrams (8/28), effect sizes (Berrar 2022 warns against reading p-values as evidence strength). Where the evidence is a deterministic check, a constructed counter-example or variants that are not independent samples, say why no test applies (11/20 evaluation papers argue this way).
- Sensitivity analysis replaces ablation in evaluation papers: one "Effect of X" subsection per factor (Iglesias Vázquez et al. 2025).
- Runtime: report it when efficiency is claimed (16/28), with hardware, repetitions and what is excluded; cite Kriegel et al. 2017 on implementation effects.

### Arguing generality across domains (answer to "extend this to other domains")
Seven moves seen in DMKD evaluation papers: (1) domain breadth of the testbed; (2) the same evaluation template repeated across data modalities (Bodria et al. 2023: tabular, image, text sections each ending in a quantitative comparison); (3) controlled factor sweeps; (4) meta-feature or instance-space analysis; (5) an "Extensions" section carrying the protocol to other tasks (Grzenda et al. 2020); (6) a survey of how the literature evaluates; (7) a real-world application section. Moves 2 and 5 transfer a method across domains most directly; add a cross-domain synthesis table that uses the same columns for every domain.

### Lessons from use (2026-10-29)
- Report rates of change against the producer's own replicate variation (noise floor) and give the test; with few comparisons, say "consistent direction, not established effect".
- When the contribution is a procedure, include a planted-cause validation and report its failures.
- State the attribution or decision convention as a numbered Definition before the results that depend on it.
- Wide tables: in sn-jnl `\scriptsize` is 9 pt and the single-column text width is 31 pc; wrap wide tables in `\resizebox{\linewidth}{!}{...}` or cut columns.

## Results, discussion, conclusion
- One results subsection per RQ, each opening or closing with its one-sentence answer; then a "lessons for benchmark designers and users" subsection (Fanourakis et al. 2023; Hewamalage et al. 2023).
- A Discussion with a "Threats to validity" subsection pre-empts objections (Le et al. 2023). Limitations are mentioned in 24/28 papers.
- "Conclusions and recommendations" (Fabris et al. 2022): what was shown, recommendations (a checklist or card), outlook.
- Pair critique with a constructive artifact: repository, checker, taxonomy, card or crosswalk.

## Figures and tables
- Median 13.5 figures and 6 tables; large per-dataset tables go to appendices.
- Figure 1 is often a toy example (12/28) or a pipeline diagram showing which step owns which choice.
- Captions are descriptive, two or three sentences, starting "Fig. n" (class does this), no final period in Springer style.
- Vector PDF, fonts embedded, sans-serif 7-9 pt at final size (174 mm full width; sn-jnl single column text is 31 pc ≈ 131 mm), colour-blind-safe with a second encoding (shape or line style).

## References
- Median 65 (25-617); evaluation papers median 83. Target 45-100 for an evaluation paper.
- Author-year, Springer basic (`sn-basic`); alphabetical; DOIs.
- At least a few DMKD papers (23/30 cite DMKD) and KDD papers (27/30). Cite datasets, software and repositories with versions or commits and persistent identifiers.
- Verify every reference against Crossref, the publisher page or DBLP before submission; hallucinated references are prohibited by Springer policy.

## Length
Median 45 journal pages (evaluation 48, method 35); about 11k-22k body words for evaluation papers; 6-8 top-level sections; at most three heading levels.

## Repositioning a database-venue paper for DMKD
1. Submit as a Regular Paper; the procedure or concept is the contribution.
2. Open with the consequence for comparative conclusions ("methods may be ranked differently"), not with an implementation detail.
3. DMKD has almost no data-repair papers: explain the task in about a page, translate jargon (row correspondence → record matching), define every abbreviation.
4. Add a cross-domain section in a core DMKD task (outlier detection, time-series evaluation, entity alignment) using the same template.
5. Use DMKD's own literature to frame the gap and the evaluation choices.
6. End with community recommendations and a released tool.

## Checker
`python3 scripts/dmkd_structure_check.py main.tex` reports title length and colon, abstract words, keywords, research questions, contribution list, roadmap, number of references and DMKD/KDD citations, bare `\cite`, top-level sections, figures and tables, statistics vocabulary, and English register statistics (sentence length, parentheses, AI-tell words). It reads files only.

## Final checklist
- [ ] Claim stateable in one sentence from the abstract alone.
- [ ] Gap stated as deficiencies; RQs listed and answered one-to-one.
- [ ] DMKD evaluation-methodology literature cited and contrasted.
- [ ] Generality argued by at least one of the seven moves.
- [ ] Statistics used where rankings are claimed, or their absence justified.
- [ ] Constructive artifact released and cited with a DOI.
- [ ] Threats to validity; conclusions with recommendations.
- [ ] 45+ verified references, author-year, DOIs.
