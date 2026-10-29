---
name: "write-eswa"
description: "How to write a paper that Expert Systems with Applications (ESWA, Elsevier) publishes: title patterns, abstract moves and length, keywords and highlights, introduction paragraph plan with contribution bullets and roadmap, related-work tables, method/setup/results/discussion structure, experiments ESWA reviewers expect (repeated runs, baselines, ablation, sensitivity, cost/complexity, significance), figures and tables, APA author-year citation practice, reference counts and recency, and practical-guideline framing that turns a method into an intelligent-system contribution. Use while drafting or restructuring any manuscript for ESWA (写 ESWA 论文 / 改写为 ESWA 风格), including papers moved from another journal. Measured on 251 ESWA papers and 10 full texts (2026)."
---

# Write-ESWA: writing guide for Expert Systems with Applications (ESWA 写作指南)

Evidence base: metadata of 251 ESWA articles (51 on LLM annotation, uncertainty/conformal/selective prediction, hierarchical text classification, active learning/HITL; 200 random 2024–2026 articles), 10 ESWA papers read in full from their arXiv versions, the live 2026 Guide for Authors and archived 2023/2024 copies. Details and DOIs: `references/observed-papers.md`; raw statistics: `references/eswa_stats_summary.txt`, `references/eswa_title_abstract_ref_stats.csv`. Numbers are observations, not acceptance thresholds.

Companion skills: `submit-eswa` (rules, files, portal) and `review-eswa` (editor/reviewer simulation). Formatting rules live in `submit-eswa`; this skill is about content and style.

## Language convention (permanent agreement with the author)
English for everything the journal sees; Chinese (中文) for reports to the author.

## 1. What ESWA wants from a paper (the framing test)
ESWA publishes the "design, development, testing, implementation, and/or management of expert and intelligent systems" applied in industry, government and universities, "and also … practical guidelines" for building and managing them. A method is welcome when it is presented as **part of an intelligent system that someone deploys**. Before writing, fill in:
- *System*: what the intelligent system is (e.g. "a quality-control component between an LLM annotator and a database").
- *User and decision*: who operates it and which decision it automates or supports.
- *Cost*: what error or effort it saves, in units the user cares about.
- *Evidence*: which real data, users or traces show it works.
- *Guideline*: what a builder should do differently after reading it.

Each of the five must be visible in the abstract, the first two introduction paragraphs and the conclusion. Worked example (2026): an LLM-annotation method desk-rejected by a data-engineering journal as "NLP, out of scope" was re-framed, unchanged in substance, as "a certified acceptance component of human–LLM annotation systems with a review-cost model and deployment guidelines".

## 2. Title
- Median **12 words** (IQR 10–15) in both the topic sample and the random sample; sentence case in published metadata.
- Patterns (shares in the random sample): colon in ~45%; coined "NAME:" prefix ~29% (22% in the topic sample); "for <application/task>" in ~60%.
- LLM papers name a concrete application domain in about 2/3 of titles (15/23).
- The guide asks to avoid abbreviations; spelling out "large language model" is the safe choice, an acronym prefix is tolerated.
- Templates: "<What it does> for <application/goal>" · "<NAME>: <what it does> for <application>" · "<Problem>: <a/an …> approach/framework for <…>".

## 3. Abstract, keywords, highlights
- **≤250 words** (2026 guide); published abstracts measure median ~200–206 words, one paragraph.
- Moves: (1) context and stakes → (2) gap of existing methods → (3) "We propose NAME, a …" → (4) two to three sentences of mechanism → (5) evaluation scope with counts (datasets, models, runs) → (6) quantified headline result **with its statistical significance** (the guide asks for it) → (7) practical implication (optional code mention, but not under double-anonymized review).
- No citations; define every abbreviation once.
- **Keywords**: 1–7 (2026 guide; older guides said ≤6, so 6 is the safe maximum when unsure). Mix method family, problem and application.
- **Highlights**: 3–5 bullets, ≤85 characters including spaces each; method, guarantee/property, and one result with a number. Count characters with a script.

## 4. Section plan (observed in the 10 full texts)
| Section | Observed practice |
|---|---|
| 1 Introduction | ~960 words (536–1540). Stakes → existing approaches and limits (dense author–year citations) → explicit gap/question → "To address this, we propose NAME" with a one-paragraph sketch → contribution list (8/10 papers; 2–6 verb-led bullets, last one empirical with numbers) → roadmap "The remainder of this paper is organized as follows" (7/10). Optional: research questions (RQ1–RQ5), Figure 1 in the introduction. |
| 2 Related work | Own section in 7/10; 2–4 thematic subsections, each ending in the gap; a **comparison table** of prior work (4/10) with columns for the properties the paper claims. |
| 3 Problem formulation | Notation, definitions, objective; a notation table when there are many symbols. |
| 4 Proposed method | Opens with an overview/pipeline figure (6/10 papers have one); subsections per component; algorithm box; theorem with proof in an appendix; **complexity/cost subsection**. |
| 5 Experimental setup | Separate from results: datasets (with sources), baselines (one short paragraph each, with citation), protocol and metrics, implementation details, research questions. |
| 6 Results and discussion | Subsections named by finding or by RQ; ablation; sensitivity; robustness to a second model/dataset; "where the method does not help". |
| 7 Discussion | Practical guidelines/implications, comparison of design choices, **Limitations** subsection (explicit in most papers; "limitations" appears in 77% of full texts). "Managerial implications" is rare in CS-style ESWA papers (0/10). |
| 8 Conclusion(s) and future work | 1–3 paragraphs: what was done, quantified results, limits of evidence, concrete future work. |
| Back matter | Data availability, Funding, (CRediT, competing interests, acknowledgements on the title page under double-anonymized review), Appendix, generative-AI declaration last before references. |

Typical size: ~10k words of body text (7.3k–19.1k), 6 figures (3–14), 9 tables (1–18), ~58 references.

## 5. Experiments that ESWA reviewers look for
- **Data**: 2–6 public benchmarks plus any real deployment data; describe sources, sizes, preprocessing and licences.
- **Baselines**: 3–11 observed; include the strongest recent (≤2 years) method and the common practitioner rule; describe each in one paragraph; state any oracle advantage given to a baseline.
- **Repetition**: mean ± SD (or CI) over repeated runs or splits; ESWA papers rarely run Friedman/Nemenyi (≈1–2% of full texts) but reviewers ask for significance — paired tests with corrected variance (e.g. Nadeau–Bengio for overlapping splits) are a strong answer; report win/tie/loss counts.
- **Ablation** (32% of full texts), **sensitivity** to key hyperparameters (17%), **computational complexity or runtime** (24%; a dedicated subsection in 3/10). Include API/LLM cost when LLMs are used.
- **Negative results**: a subsection on where the method does not help builds credibility.
- **Reproducibility**: public code and data (41% link GitHub); under double-anonymized review cite the deposit on the title page and keep the manuscript anonymous.
- **Research questions**: number them and answer each in a named results subsection.

## 6. Figures and tables
- Figure 1 = system/pipeline overview showing where the method sits in the application workflow (not only an architecture); panel (b) can show a worked example.
- Plots: one message per figure; consistent method colours/markers across figures; colour-blind-safe palette; vector PDF with embedded fonts; readable at 100% (≥6.5 pt text).
- A forest plot of paired differences with CIs is a compact way to show significance across many settings.
- Tables: booktabs, no vertical rules or shading; caption on top states what the numbers are, the number of runs, what bold and symbols mean; notes below the table.
- Captions are self-contained (2–4 sentences): what is shown, how to read it, what to notice.

## 7. References and citation practice
- APA 7 author–year. `\citet{key}` for "Huang et al. (2025) propose …", `\citep{a,b}` for parenthetical groups; never "Huang et al. \cite{x}".
- Count: median **50** (topic sample; IQR 39–63), **57** for LLM papers, 52 random → aim for **50–65**.
- Recency: median share from the last five years 0.57 (0.64 for LLM papers) → aim ≥55%.
- ESWA papers cite a median of ~2 earlier ESWA papers (≈4 in hierarchical text classification). Cite **3–6 genuinely relevant ESWA articles** (verify each by DOI and read the abstract); never pad.
- LLM papers cite arXiv preprints (median 4); mark them as preprints and prefer formal versions.
- Verify every reference against Crossref/OpenAlex/arXiv before submission; keep the check log.

## 8. Language and style
- Register of applied CS journals: short declarative sentences, past tense for experiments, present tense for claims about the method, no hype words ("novel", "groundbreaking", "revolutionary"), no rhetorical questions.
- One claim per sentence; quantify ("from 0.31 to 0.58") instead of qualifying ("substantially").
- State every caveat once where it applies and once in Limitations.
- Consistent American or British spelling (not mixed).
- Run `scripts/eswa_style_check.py` and fix flagged items.

## Workflow
1. Write the five framing answers (Section 1) and the title/abstract first.
2. Build the section skeleton from Section 4; add Figure 1 and the related-work comparison table early.
3. Map each experiment to an RQ and a results subsection; add cost/complexity and "does not help".
4. Search ESWA for related work (OpenAlex: `filter=primary_location.source.issn:0957-4174&search=<topic>`), read abstracts, cite what is genuinely related.
5. Run the checker:
   ```bash
   python3 scripts/eswa_style_check.py paper/manuscript.tex --bib paper/references.bib
   ```
6. Hand over to `review-eswa` for an independent pre-submission review, then `submit-eswa`.

## Files
- `scripts/eswa_style_check.py` — section plan, intro length, contribution list, roadmap, RQs, limitations, practical guidelines, complexity subsection, figure/table counts, reference count and recency, ESWA references, AI-tell words, sentence length.
- `references/observed-papers.md` — the 10 full-text papers and topic examples with DOIs and observations.
- `references/eswa_stats_summary.txt`, `references/eswa_title_abstract_ref_stats.csv` — raw statistics (OpenAlex/Crossref, 2026-10-29).
