---
name: "write-icde"
description: "Writing guide for IEEE ICDE (CCF A) research papers, built from 21 deep-read accepted papers (ICDE 2025-2027R1: LLM-for-data, Text-to-SQL, vector search, EAB benchmarks, dynamic graph algorithms) and statistics of 1058 accepted titles/abstracts: data-engineering framing, title and abstract patterns, paragraph-by-paragraph introduction, problem definition, method sections with theorems, experiment sections by RQ with takeaways, related work positioning against ICDE/VLDB/SIGMOD, figures/tables, references, the 12-page budget and the AI-content acknowledgment. Use when drafting, restructuring or polishing a paper for ICDE (写 ICDE 论文 / 投 ICDE 写作 / 改写成 ICDE 风格). Includes a structure checker."
---

# Writing for ICDE (Write-ICDE 写作指南)

Evidence: `references/observed-structure.md` (per-paper counts and structures), and the notes in `read-icde`. Numbers such as "3 contributions in 4/5 papers" are observations, not rules.

Use with `submit-icde` (format, rules) and `review-icde` (simulated review). Polish English with `academic-latex-polish` if installed.

## Language convention
Manuscript, captions, rebuttal in **English**; plans and reports to the author in **Chinese (中文)**.

## 1. Frame it as data engineering
ICDE desk-rejects pure ML/DM. State the task as a data-management problem: a query/operator, a cost model, a constraint (budget, error target, latency), an objective, and a guarantee or complexity. Name the classical DB concept you build on (AQP, cost-based optimisation, index maintenance, provenance, scheduling) and cite the ICDE/VLDB/SIGMOD line.

## 2. Title (median 9 words)
Patterns: `Acronym: A <Cost-Efficient|Learned|Co-Designed> Framework for X` (2026 LLM papers); `Maintaining <structure> in Large Dynamic Graphs`; `<Claim phrase>: <object> over/for <setting>`; EAB: `[Experiment, Analysis, and Benchmark] ...`. Put the technical paradigm or the hard setting in the title.

## 3. Abstract (150-250 words, median 203)
Context (1-2 sentences) -> gap, as the assumption existing methods share -> "We present X" -> key insight -> 2-3 components -> evaluation scope -> 1-2 headline numbers with the same wording as in the body ("up to", "on average") -> artifact availability. No citations.

## 4. Introduction (5-7 paragraphs, ~1.3 pages)
1. Scenario and why its cost/scale matters (a concrete number helps).
2. Existing solutions and the assumption they share.
3. Figure 1: a real measurement or failure example showing that the assumption breaks.
4. Challenges C1-C3 (bold run-in labels).
5. The approach: "To address C1, ..." mapping each challenge to a component; mention the special cases it contains.
6. Contributions: 3 items (3-6 seen), each with its section number; the last item states the experiments and headline results; mention released code.
Answer one obvious reviewer objection inside the introduction.

## 5. Problem definition and method
- Preliminaries with notation, then a `Definition` of the problem with all inputs, the constraint and the objective; frame the two baselines that bracket it.
- Each method section: motivation sentence, definitions/equations, `Theorem` with proof (short proofs inline; long proofs to a public technical report, because no appendix is allowed), one paragraph on the practical meaning, and an algorithm box.
- Accepted LLM papers often lack guarantees; a guarantee is a differentiator.

## 6. Experiments (25-55% of the body)
Setup: datasets, baselines (include ICDE/VLDB/SIGMOD methods and your method's special cases), metrics, cost unit with list prices and date, hardware. Then one subsection per RQ, each ending with a bold **Takeaway** sentence. Required blocks: main result (quality and cost in one table), validity of guarantees, factor sweeps (where it helps and where not), ablation, other backbones/vendors, extensions, overhead and parameter sensitivity. Say how many repetitions; report dispersion.

## 7. Related work
3-5 themed paragraphs; finish each with how this paper differs. Accepted LLM and theory papers often place it after the experiments; problem-driven and EAB papers after the introduction.

## 8. Figures, tables, references
- Vector figures, readable at column width, units on axes, log axes across orders of magnitude, colour-blind-safe palette; table with booktabs, best in bold.
- Published papers: 5-24 figures, 2-10 tables, 56-85 references; median 14 printed pages (12 body + references).
- Verify every reference against Crossref/OpenAlex/arXiv/publisher; at least ~10 ICDE/VLDB/SIGMOD papers.

## 9. End matter
Conclusion: what was shown, then future work; do not end on what was not shown. Then the unnumbered **AI-Generated Content Acknowledgment** (systems, sections, level of use; LLMs used in experiments included).

## 10. Checker
`python3 scripts/icde_structure_check.py paper/` reports title/abstract length, section order, contribution count, Figure 1 and challenges in the introduction, experiment share, theorem/figure/table counts, takeaways, reference counts, AI acknowledgment and hedging.

## Final checklist
- [ ] Data-engineering framing and core-venue lineage explicit.
- [ ] Figure 1 measures the gap.
- [ ] C1-C3 <-> components <-> RQs.
- [ ] Problem Definition + at least one theorem.
- [ ] Cost reported in dollars/tokens; negative regions reported.
- [ ] 12 body pages, no appendix; AI acknowledgment present.
