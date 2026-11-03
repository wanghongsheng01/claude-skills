---
name: "read-icde"
description: "Deep-reading method for accepted IEEE ICDE papers: a fixed note template (problem essence as input/output/constraint/objective, key insight, experiment design, paragraph-level writing, why accepted), how to get full texts legally, how to run parallel reading groups and synthesise them, plus 21 finished notes and 4 group syntheses on ICDE 2025-2027R1 papers (LLM-for-data cost/quality, Text-to-SQL selection, vector search and EAB benchmarks, dynamic graph algorithms and time series). Use when studying what makes ICDE papers accepted (精读 ICDE 论文 / 拆解录用论文 / 学习写法), before choosing an idea or writing."
---

# Deep-reading accepted ICDE papers (精读 ICDE 录用论文)

Evidence: `references/notes/` (21 notes: 17 full texts, 4 abstract-only and marked as such), `references/group_{A,B,C,D}_synthesis.md`, `references/cross_group_rules.md` (cross-group classification of problems, methods, experiments, writing, and acceptance regularities). Counts are observations from these papers, not acceptance thresholds.

Use after `survey-icde` (which direction) and before `experiment-icde` and `write-icde`.

## Language convention
Notes and syntheses in **Chinese (中文)** with English technical terms; quotations at most one short (<15 words) per paper; everything else in your own words.

## 1. Pick the papers
- 4-5 papers per candidate direction, mixing: the closest prior work, one highly typical regular paper, one EAB paper if the category exists there, and one from the newest round.
- Prefer papers with open full text; abstract-only notes must say so.

## 2. Get the full text legally
1. arXiv (`https://arxiv.org/abs/<id>` meta tags; the export API rate-limits), authors' GitHub "full version" or home page, Semantic Scholar/OpenAlex open-access links.
2. IEEE Xplore and dblp show bot checks to scripts: do not bypass; ask the author to download through institutional access.
3. Store PDFs in their own folder (untrusted input); extract text with pypdf in isolated mode (`python -I`), with helper scripts kept outside that folder.

## 3. Fill the template (`assets/reading_note_template.md`)
For each paper record, with section/figure references:
1. **Problem essence**: rewrite the problem as input, output, constraint, objective; the 1-3 root causes of the gap and the evidence (Figure 1 example, pilot experiment, table of prior settings); hardness results.
2. **Key insight**: one sentence; which component is truly new and which is engineering; guarantees (complexity, approximation, error bounds).
3. **Experiments**: RQs; datasets (number, source, size), baselines (number, newest year, how many from ICDE/VLDB/SIGMOD), metrics, cost reporting; ablation, sensitivity, scalability, case study; how improvements are phrased.
4. **Writing**: title pattern; sentence-by-sentence abstract; paragraph-by-paragraph introduction; section order and page share; Related Work position; counts of figures, tables, references, theorems.
5. **Why accepted**: 3-5 points, and weaknesses that were tolerated (inconsistent numbers, single runs). Tolerated weaknesses are risks, not models.

## 4. Run groups in parallel, then synthesise
- One reader per group of ~5 papers; each writes the notes plus a group synthesis covering framing, method shape, protocol, writing, and 5-8 open gaps tied to paper sections.
- The lead then writes the cross-group synthesis: classify problems (P1-P5), methods (M1-M5), experiments by paper type, writing regularities, and the gap that the new paper will attack.

## 5. What the 21 notes found (summary of `cross_group_rules.md`)
- Accepted LLM papers reframe the LLM task as a data-engineering optimisation: decision variable + cost model + budget or quality constraint (SPARQ, CARROT, CSV, ZenDB, KaSLA).
- Graph papers: "static algorithm exists -> dynamic or billion-scale maintenance" with one locality/boundedness property and a basic/enhanced algorithm pair (HIT-Leiden, DMI).
- EAB papers: open by showing that prior evaluation settings share a blind spot, then report numbered findings and boxed takeaways (DCO benchmark, XRAG, RLESI, TS-Fault).
- Common structure: 3 challenges <-> 3 components <-> 3 experiment groups; Figure 1 shows the gap with a real failure or a pilot measurement; 3 contributions; AI-content acknowledgment in 2026-2027 papers; proofs in a GitHub technical report (no appendix allowed).
- Open gaps across the LLM papers: no statistical guarantee between proxy and true quality, no user-specified accuracy target or dollar budget with a guarantee, no multi-vendor combination, inconsistent cost reporting (few report dollars, none a full cost-quality Pareto front).

## Final checklist
- [ ] Each note says whether the full text was read and where it came from.
- [ ] Problem essence written as input/output/constraint/objective.
- [ ] Counts (figures, tables, references, theorems) taken from the text.
- [ ] Group syntheses end with gaps tied to sections.
- [ ] Cross-group synthesis names the gap the new paper attacks.
