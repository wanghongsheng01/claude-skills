---
name: "write-icde"
description: "Writing guide for IEEE ICDE (CCF A) research papers, built from 21 deep-read accepted papers (ICDE 2025-2027R1: LLM-for-data, Text-to-SQL, vector search, EAB benchmarks, dynamic graph algorithms), ten accepted cohesive-subgraph maintenance papers, nine accepted ICDE benchmark papers and twelve accepted AQP/sampling/LLM-query-with-guarantees papers (ICDE 2022-2027, PVLDB), eleven accepted reachability-index/IVM/access-control papers (ICDE 2023-2026, PVLDB, SIGMOD) read for how they state limitations, asymptotic guarantees, LLM oracles and proprietary data, and statistics of 1058 accepted titles/abstracts: data-engineering framing, title and abstract patterns, paragraph-by-paragraph introduction, problem definition, method sections with theorems, experiment sections by RQ with takeaways, related work positioning against ICDE/VLDB/SIGMOD, figures/tables, references, the 12-page budget and the AI-content acknowledgment. Has a dedicated Experiment, Analysis and Benchmark (EAB) guide (references/eab.md) built from 16 accepted EAB/benchmark papers (ICDE 2024-2027R1 and PVLDB EA&B: CDC chunking, WPBench, entity-matching re-evaluation, SemBench, UDA-Bench, NL2SQL360, learned-optimizer ML perspective, plus the nine in limitations-writing-eab.md): title and abstract patterns, gap tables, RQs/findings/lessons, repetitions/statistics/cost/LLM-version reporting, figures, references, and ten patterns for stating limits and threats to validity without self-negation. Use when drafting, restructuring or polishing a paper for ICDE (写 ICDE 论文 / 投 ICDE 写作 / 改写成 ICDE 风格 / 写 EAB 论文 / benchmark paper / experimental survey / threats to validity / 局限性怎么写). Includes a structure checker with an EAB mode."
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

## 9. Limitations without self-negation (`references/limitations-writing.md`)
Ten accepted papers on exact or dynamic cohesive-subgraph computation were read in full:
- none states a loss in the abstract or the conclusion;
- none has a "where we fail" heading;
- all keep every losing cell in their tables;
- each loss is said once, in 1–4 sentences, in the experiment that measures it.

Rules:
- **Abstract**: scope goes in as a qualifier of the positive claim ("under repeated deletions in a large
  dense region", "for k ≤ 2"), never as a closing negative sentence.
- **Introduction**: at most one scope sentence, with a section pointer. The contribution list holds
  contributions only.
- **Experiments**: write each loss once, in the order fact → mechanism (a measured property of the
  instance) → regime → bound ("still", an absolute gap, a positive count such as "46 of 50 cells").
  Title the paragraph by the regime ("When does X pay off?"), not by the failure.
- **One-off costs** (index, warm-up): report them once with a break-even count or an amortisation
  argument.
- **Ablation losses**: present losses of your own basic variants as the motivation for the next
  component.
- **Theory scope**: state it once, as a named Assumption or Condition in the method section, with how
  often it holds.
- **Conclusion**: fold the scope into the main claim and add at most one sentence on the open problem.
- **Never write** "does not help", "fails", "vanishes", or "only N×" about your own method's gains.
- **Classical building blocks** (MFMC, Neyman allocation, PPI): attribute them once where they are used
  ("Building on X [c], we derive ... for finite relations") and once in Related Work. Do not repeat
  "restates" or "is classical" in the abstract, introduction, method and limitations: four mentions read as
  "no contribution" (Ladder, ICDE 2027 R2 review).
- **Failed-target cells** (marked †): fix them in the method (fallback, larger top-up) before writing;
  a sentence saying the method "missed the target" is read as a correctness failure.

Integrity: never delete measured numbers, never hide the strongest competitor, never write a sentence
that the tables contradict. That contradiction is a top rejection reason.


### 9a. EAB papers: the full guide (`references/eab.md`)
Start an EAB paper from `references/eab.md`. It is built from 16 accepted papers: ICDE 2024–2027R1 and
PVLDB EA&B.
- **Title**: one of five patterns, with the ICDE tag as a prefix.
- **Abstract**: scale numbers; 2–3 numeric findings about the evaluated methods; one recommendation;
  the artifact URL; no limits of the study itself (15/16 of the accepted papers follow this).
- **Gap**: a Figure 1 measurement or a criteria table with an "Ours" row that your own setup meets.
- **Findings**: RQs in the introduction, a boxed finding per experiment, and a lessons section with a
  decision table or figure.
- **Reporting**, beyond the accepted norm (the norm is often missing it):
  - runs plus dispersion and a claim rule or test;
  - seeds;
  - pinned model versions and temperature;
  - $ and tokens with price dates;
  - timeouts;
  - ground-truth agreement.
- **Limits**: 2/16 have a labelled block (about 110 words); 0/16 concede limits in the conclusion;
  12/16 answer a threat with a measurement. Use the ten patterns in section 8.2: design choice with a
  reason, domain of validity, "we do not claim X", inclusion criteria, concede-then-neutralise,
  reimplementation caveat, versioned snapshot, not a universal ranking, threat → measurement, scale →
  headroom. ICDE has no revision round, so add one scope paragraph of 80–150 words in advance.

### 9b. EAB papers: two registers (`references/limitations-writing-eab.md`)
Nine accepted ICDE benchmark papers (DCO, RLESI, XRAG, SQLMorph, TS-Fault; HCT-QA, CITBench, RDL-Bench,
Text2VectorSQL; read in full) keep two registers apart:
- **Negatives about the evaluated methods are the contribution.** State them with numbers in the abstract
  (4/5), the findings, the takeaways and the conclusion (3/5). "fail" about evaluated methods: 5/5.
- **Limits of your own benchmark** never appear in the abstract or conclusion (0/5). The word "limitation"
  is never used for them (0/5), nor "bug", "rerun", "mistake", "flaw" or "unfortunately" (0/5). Each limit
  is stated once, where it applies, with a one-clause technical reason and a mitigation or counter-evidence (5/5).
- A threats section is optional (1/9). If present: about four one-sentence items, each answered by a result
  already in the paper (TS-Fault, about 110 words).
- Apply your own Table I criteria to yourself: reviewers turn a criticism of prior evaluations against a
  setup that does not meet it.
- Prefer an incremental experiment over an admission: turning a validity threat into an RQ, metric, control
  experiment or finding is the most common device (7/9) and turns "may be an artifact" into a result.
- Process problems in your own harness that were fixed and rerun need no narrative in the paper; record
  them in the artifact's changelog. Keep every validity fact a reviewer needs (runs, models, synthetic data,
  judges) once in the setup.
`scripts/icde_structure_check.py` switches to EAB rules when the title contains "Benchmark" (or `--eab`):
it flags self-deprecating wording about the benchmark and threats sections longer than about five items.
It also flags:
- limits of your own study in the abstract or conclusion;
- missing RQs or lessons;
- missing reporting facts: runs, dispersion, seeds, a claim rule, and for LLM papers temperature and cost.
It counts the finding boxes.

### 9c. AQP, sampling and LLM-query papers with guarantees (`references/limitations-writing-aqp.md`)
Twelve accepted papers (KG-AQP, ExSample, JanusAQP, BATCHER, ZenDB, spatial-join sampling, CactusDB,
OptiAQP, SemiBonsai at ICDE; SUPG, ABae, LOTUS at PVLDB), read in full:
- **Abstract** reports gains only (10/12); a no-gain regime becomes "outperforms or matches" or a worst-case
  bound in the body. 1/12 states a loss, paired with its gain in one clause.
- **Asymptotic guarantees are the norm** (0/6 CLT-based papers give a finite-sample bound for the main
  estimator). Say "asymptotic" once with its condition, in the theorem; back it with empirical coverage at
  the smallest sample sizes used (5/6); one sentence on finite-sample bounds as a direction.
- **Weak regimes cost efficiency, not correctness** - say so in the same sentence (SUPG, ABae, LOTUS).
- **Model/LLM oracle**: define truth relative to it in the problem definition; add a human-truth variant or
  agreement number; a few-hundred-row audit is above the norm.
- **Limitations heading**: 1/12. Use one Discussion unit of 80-200 words.
- **Proprietary data**: 0/12 rely on it; public data must carry the headline claims; the non-release reason
  goes in the CMT form.
- **Planner/ablation that looks useless on cost**: find the second metric where it wins (blocked queries,
  latency, certified targets) before the reviewer concludes it is dispensable.
- Worked before/after table from a real submission (23 statements found, 6 kept) is in the reference.

### 9d. Reachability indexes, IVM and access control (`references/limitations-writing-reachability.md`)
Eleven accepted papers (TOL, BatchHL at SIGMOD; P2H+, DLCR, M2HL, Sieve, DBSP at PVLDB; IFCA, RLC, HL-index at
ICDE; F-IVM), read in full on 2026-11-08 for the AuthZ-Graph submission:
- **"Online search is fast on easy graphs"** is a citable finding (IFCA states it in its introduction; Hanauer
  et al. for dynamic TC), not a confession. Put the regime into the positive claim ("on deeply nested graphs"),
  pre-register the expectation at the start of the latency RQ, and turn the loss into a crossover (queries per
  update, break-even q*): 5/11 papers quantify one. Cite the field's own primary source when it motivates the
  hard regime (Zanzibar section 3.2.4 built Leopard for deeply nested groups).
- **Never raise the reviewer's objection yourself** ("A natural objection is...") and never let an RQ announce
  a null result ("offers no benefit", "the gain is small", "suffices"): state what the RQ establishes
  (correctness, share of cases that benefit, cost), each cost once, with its mechanism.
- **Ablation, not concession**: write the full method's increment over its ablated variant ("frontier hubs cut
  update cost 1.9-7.9x at equal check speed"), not "much of the speedup comes from X".
- **Synthetic labels/updates/policies** (8/11 use them, 0/8 apologise): two setup sentences, a precedent or
  real-data grounding, optionally a tick column in the dataset table.
- **Own baseline implementations** (4/11): provenance plus the fairness control (same store, same binary,
  single thread); 0/4 doubt their own baseline code.
- **Model limits** go into the preliminaries as an assumption, reduction or extension pointer (6/11).
- **No Limitations or Threats heading** (0/11) and no losses in the conclusion (0/11); at most a two- or
  three-sentence "scope of the comparison" unit at the end of the setup.
- `icde_structure_check.py` flags the concession phrases found on AuthZ-Graph (17 hits in one manuscript).

## 10. Readability and layout (with `manuscript-writing-review`)
- **Math**: put conditions, case distinctions (`cases`), set-builder definitions, sums and chains of
  inequalities in displays. Theorem statements should not be walls of inline symbols. Under IEEEtran,
  use `IEEEproof` and print no end-of-proof box (`\renewcommand{\IEEEQED}{}`).
- **Figures**: legends above the axes, never over data. Notes such as "labels in ms" go in the
  caption.
- **Tables**: a one-column table must fit 252 pt. Use short headers, sensible precision, and
  `>{\raggedright\arraybackslash}p{}` for text cells.
- **Before any handover**: compile, then run `manuscript-writing-review` (layout and figure checks, every
  page) and `manuscript-proofcheck`.

## 11. End matter
Conclusion: what was shown, with the scope folded into the claim, then future work. Do not end on what
was not shown. Then the unnumbered **AI-Generated Content Acknowledgment** (systems, sections, level of use; LLMs used in experiments included).

## 12. Checker
`python3 scripts/icde_structure_check.py paper/` reports title/abstract length, section order, contribution count, Figure 1 and challenges in the introduction, experiment share, theorem/figure/table counts, takeaways, reference counts, AI acknowledgment and hedging, self-negating wording (abstract, introduction, conclusion) and failure headings.

## Final checklist
- [ ] Data-engineering framing and core-venue lineage explicit.
- [ ] Figure 1 measures the gap.
- [ ] C1-C3 <-> components <-> RQs.
- [ ] Problem Definition + at least one theorem.
- [ ] Cost reported in dollars/tokens; negative regions reported once, as regimes with a mechanism (no failure heading, nothing negative in the abstract or conclusion).
- [ ] Compiled and checked with `manuscript-writing-review` (0 layout errors, every page seen).
- [ ] 12 body pages, no appendix; AI acknowledgment present.
- [ ] EAB: the checklist in `references/eab.md` section 10 is done, and `icde_structure_check.py --eab`
      gives no self-limit in the abstract or conclusion.
