---
name: "write-ipm"
description: "How to write a paper that Information Processing & Management (IPM, Elsevier) publishes: framing as an information-use problem, title patterns, one-paragraph abstract moves and length, highlights, introduction with research questions or objectives, gap arguments, the distinct conventions of evaluation and method papers, two-level measurement, statistics, how limitations and negative results are written, theoretical and practical implications sections, hedging, figures and tables, reference targets and self-citation. Built from counts over 1,497 IPM articles (2024–2026) and 9 full texts. Use while drafting or revising for IPM (写 IPM 论文 / Write-IPM)."
---

# Write-IPM: writing guide for Information Processing & Management (IPM 写作指南)

Evidence base: Crossref metadata of 1,497 IPM research articles (2024–2026), 158 abstracts, 34 full texts with machine counts, **9 full texts read end to end** (3 published versions, 6 preprint or accepted copies). The sample of full texts is not random; it favours authors who post preprints. These are observed habits of published papers, not journal rules. Rejected papers are not in the sample. Rules live in `submit-ipm`; simulated review lives in `review-ipm`. Details and DOIs are in `references/observed-papers.md`.

## Language convention
English for everything the journal sees; Chinese (中文) for reports to the author.

## 1. Framing test
IPM sits at the intersection of computing and information science. State on page 1:
- **Who relies on the information or score**, and **which decision changes** because of this paper.
- **What transfers** beyond this dataset, model or benchmark.
- **What to do**: when to trust, avoid or check.

An evaluation paper is framed as an evaluation of a measure people act on, not as a contest among methods.

## 2. Two paper types with different conventions
| | Method papers | Evaluation papers |
|---|---|---|
| Core evidence | Baselines, ablation (11/18 mention ablation) | Agreement and correlation measures, error analysis (ablation 1/9) |
| "Outperform/superior" in abstract | common (27% overall) | 0 of 15 in the evaluation group |
| Default structure | Intro, Related work, (Preliminaries), Method, Experiments, (Ablation), (Discussion and implications), Conclusion | Intro, Related work, Data or gold standard, Method, Results, Error analysis, Implications and limitations, Conclusion |
| Title | `Name: what it does, via how` | Claim or question, then scope after a colon |

A paper that proposes a tool and evaluates a measure should choose the second as its spine.

## 3. Title
Median 11 words overall, 13 among LLM-evaluation papers; colon in 49–62%; question titles rare (2–3%). Evaluate, assess, benchmark, empirical or comparative appear in 52% of LLM-evaluation titles, "novel" in 2%. "Audit" appears in 1 of 1,497 titles; the closer vocabulary is evaluate, assess, measure, reliability.

## 4. Abstract and highlights
- **One unstructured paragraph** (no labels found in 158), median 208 words and 9 sentences; 82% contain numbers. Keep to 190–240 words.
- Moves: context (1–2 sentences), contrast or gap (1), what this paper does (1), data and design with counts (1–3), results with values (2–4), one closing sentence on meaning or use.
- First person is normal (84% use we/our).
- **Negative results belong in the abstract when central**, in exact scope and next to a usable recommendation. Useful clause forms: "though X on Y", "with no lead on Z", "this interval does not establish equivalence". Avoid abstract-level sentences that state doubt without a result.
- Highlights: 3–5 fragments, one point each, median 81 characters; keep to at most 85. Published examples name a number in most bullets.

## 5. Introduction
Domain and stakes → current practice → what recent work offers → the specific open question → labelled RQs or research objectives, each justified in a line → contribution bullets → optional road map.
- Labelled RQs appear in 10/34; a dedicated "Research objectives" heading in 6/34; a contribution list in 20/34. Labels are common, not mandatory.
- **Map RQs one-to-one to result headings.**
- Gap arguments seen: coverage (does it transfer?), metric (does the result depend on one metric?), anomaly (a prior result does not fit), benchmark flaws (named faults), integration, practical bridge. Bound any "to the best of our knowledge" with the nearest prior study.
- Criticise prior work on scope, not on error. Contrast is carried by "however", not polemic.

## 6. Related work
Thematic subsections ending in the gap, then an explicit comparison subsection or table against nearest neighbours. Cite IPM neighbours only after reading them.

## 7. Experiments
**Two-level measurement is the strongest template for evaluation papers:** item-level disagreement, then the downstream effect on the decision people make (e.g. pair-level κ of 0.32–0.53 with ranking τ ≥ 0.90 on some metrics and not on others).

Practices worth copying:
- Name the reference standard and **measure its own uncertainty**; measure human-human disagreement before comparing an LLM with humans.
- Compute what an imperfect proxy could possibly show (a theoretical ceiling), then read results against it.
- Compare with individual human annotators on the downstream task, not only with an aggregate.
- Interpretive thresholds with a citation. Give the coefficient, raw agreement, marginals and interval; κ falls under skewed marginals.
- Intervals over the correct sampling unit; paired tests for paired outcomes; effect sizes including small ones; multiplicity control.
- Pin model IDs, dates and parameters; report repeated runs or justify single runs; state cost as a design constraint; release prompts and raw outputs.
- Error analysis with cases.

Inferential statistics appear in 19/34 (evaluation 6/9, method 8/18). They differentiate rather than form a bar. Weak practice exists in print (no tests, single database, "significantly" without tests); do not copy it.

## 8. Discussion, implications, limitations
- **Implications are IPM's clearest signature.** Headed sections appear in 7 of 8 published versions. Use "Theoretical implications" (name what understanding has changed; a theory-free statement is acceptable) and "Practical implications" as finding → recommendation bullets.
- **Limitations are normal: 300–500 words** (median about 409 across 8 read papers, range 70–946), usually just before the conclusion. Ordered items, each with its effect on the claims and, where possible, its remedy or next step. Defending a limitation by comparison with established practice is accepted. Pair items with future work.
- "Threats to validity" appears in only 2 of 34. Use "Limitations".
- **Do not stack hedges on findings.** Measured findings in flat statements; hedge explanations and generalisations. Median hedge rate 2.8 per 1,000 words (evaluation 3.2); information-science authors reach 9–11.
- **Scope limits must stay.** IPM papers report non-replications, failed prompts and non-significant comparisons when these answer a usable question, and evaluation papers lose credibility without them. Compress wording and move procedural minutiae to a deposit, but keep any limit that changes how a headline claim should be read.
- Avoid revolutionize, outstanding, impressive even though examples exist.

## 9. Figures and tables
Median 5–6 figures and 4–8 tables. Figure 1 is often a framework or a worked example. Heatmaps for agreement, interval plots with a threshold line, comparison table with sibling studies, model rows and metric columns. Captions state the takeaway. Prompts in a figure or appendix.

## 10. References
Median 58 (NL-to-query 50.5), median 54% from the last three years (NL-to-query 80%). IPM self-citation about 6%; 158 of 1,496 papers have none, so no quota is visible. Target 50–70, with 3–6 IPM papers when honestly relevant. Keep foundational items for evaluation theory.

## 11. End matter
CRediT and data availability in all 8 published copies read. Under double anonymization, put names on the title page. AI in research goes in Methods; AI in writing goes in the declaration (see `submit-ipm`).

## 12. Check
```bash
python3 scripts/ipm_style_check.py manuscript.tex --bib references.bib --year 2026
```

## Files
- `references/observed-papers.md`: counts, examples and DOIs, with evidence tiers.
- `references/ipm_paper_survey.csv`: 219 surveyed papers.
- `scripts/ipm_style_check.py`: compares a manuscript with these observed shapes.
