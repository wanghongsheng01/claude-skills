---
name: ccfa-b1-method-writing
description: >-
  Use when writing a CCF-A method paper on a scientific problem that the
  literature has already defined (B1-method): how to set the increment over the
  nearest neighbour, choose the strongest fair baselines, organise main and
  ablation tables, and analyse wins, losses, and mixed results. Do not use for
  a benchmark or EA&B paper, and do not use to relabel a first-definition (B2)
  problem as a method improvement.
---

# Writing a B1 method paper (existing problem, new method)

Official venue guidelines take precedence over this skill. This draft expands the existing methodology notes on evaluation hygiene and pre-submission hardening. It is generic: no institution facts, no experimental scores from our papers, no hard-coded deadlines.

The scientific claim is a new mechanism, system, or guarantee on a **already defined** problem. The usual gate is: on a pre-registered majority of official metrics, match or beat the current strongest baseline; every metric a baseline wins must have a mechanism explanation. Tune only on development data; an official test fold is evaluated once.

## When to use / when not

**Use** after the front-loaded research skill has classified the paper as B1-method, and when designing the method, the experiment matrix, or the paper structure.

**Do not use** if the contribution is a dataset, protocol, or diagnostic suite (use `ccfa-b1-benchmark-writing`), or if the main claim is a newly defined problem (use `ccfa-b2-first-problem-definition`). Do not apply the method SOTA gate to an EA&B paper.

## Inputs and outputs

**In:** the stage 1–6 research document; the formal problem definition and nearest neighbours; candidate baselines and datasets; development-only scores if any.

**Out:** a method motivation chain; a baseline and ablation matrix; a writing plan for wins and losses; updates to this skill when a new formally published paper teaches a reusable lesson.

## Process

1. State the existing problem in the neighbours' language, then one falsifiable sentence of increment (mechanism, setting, guarantee, or efficiency—not "we also use an LLM").
2. Choose the strongest **fair** baselines: original author artefacts where possible, not a weakened reimplementation. If the strongest control is a constructed one (our mechanism under the neighbour's paradigm), say so.
3. Freeze the official protocol on development data. Register metrics, seeds, and the SOTA gate before the official run.
4. Analyse every loss and every narrow margin with a mechanism, once. Do not change the metric definition after seeing official numbers.
5. Structure the paper so that related work bounds the increment, the method section is executable, and the experiment section answers pre-stated questions. Tables: best in bold, second underlined, W/T/L, confidence intervals; lower-is-better metrics say so in the caption.

## Evidence standard

Lessons below come from **full official PDFs** of PVLDB 2023–2026 papers, retrieved from https://www.vldb.org/pvldb/ on 2026-11-12 (America/Los_Angeles). Each entry lists DOI and official PDF. Do not treat these notes as a substitute for reading the PDF. Numerical claims are only those stated in the paper's abstract or first pages as read; if a number was not extracted, it is omitted.

## Papers read this round (five, plus two extras)

### 1. Sphinteract — B1-method on an existing NL2SQL problem

- Fuheng Zhao, Shaleen Deep, Fotis Psallidas, Avrilia Floratou, Divyakant Agrawal, Amr El Abbadi. *Sphinteract: Resolving Ambiguities in NL2SQL Through User Interaction.* PVLDB, 18(4): 1145–1158, 2024. doi:[10.14778/3717755.3717772](https://doi.org/10.14778/3717755.3717772). Official PDF: https://www.vldb.org/pvldb/vol18/p1145-zhao.pdf
- **Problem already defined:** NL2SQL, including on Spider and WikiSQL; the paper isolates a remaining enterprise-grade difficulty (ambiguous user intent).
- **Thinking to reuse:** they do not claim a new task; they claim a new interaction paradigm (Summarize, Review, Ask) and three ways to consume feedback. Motivation starts from a precise failure of existing LLM pipelines. Evaluation is on existing hard benches (KaggleDBQA, BIRD), not a private set alone. A user study and a taxonomy of ambiguity types precede the method, so the mechanism is justified before the accuracy table.
- **Do not copy:** their specific SRA prompts, or a claim that interaction is always acceptable (some venues will ask about user burden; the paper itself lists "avoid unnecessary interactions" as a design goal).

### 2. REDSQL (The Power of Constraints) — B1-method, constraints as the increment

- Tonghui Ren, Chen Ke, Yuankai Fan, Yinan Jing, Zhenying He, Kai Zhang, X. Sean Wang. *The Power of Constraints in Natural Language to SQL Translation.* PVLDB, 18(7): 2097–2111, 2025. doi:[10.14778/3734839.3734847](https://doi.org/10.14778/3734839.3734847). Official PDF: https://www.vldb.org/pvldb/vol18/p2097-ren.pdf
- **Thinking to reuse:** the opening is a concrete, inspectable failure (a BIRD query that is wrong because content was retrieved by string similarity and a predicate landed in the wrong column). The method is a **database-side** increment (document constraints, verify them, expand context), not a larger prompt. Table 1 of the paper enumerates implemented constraint types—this is how a method paper makes the mechanism checkable. Closest neighbours (content retrieval, fine-tuning, prompting) are engaged as insufficient understanding of the database, not as "they did not do our system".
- **Do not copy:** treating every NL2SQL error as a constraint-violation problem; their constraint catalogue is scoped to data types and value relations they implement.

### 3. LLM-R2 — B1-method on classical query rewrite

- Zhaodonghui Li, Haitao Yuan, Huiming Wang, Gao Cong, Lidong Bing. *LLM-R2: A Large Language Model Enhanced Rule-based Rewrite System for Boosting Query Efficiency.* PVLDB, 18(1): 53–65, 2024. doi:[10.14778/3696435.3696440](https://doi.org/10.14778/3696435.3696440). Official PDF: https://www.vldb.org/pvldb/vol18/p53-yuan.pdf
- **Thinking to reuse:** the problem (equivalence-preserving rewrite for efficiency) is classical. The LLM is **not** the rewriter of record: it recommends rewrite **rules** for a rule-based system, so equivalence stays with the rules. That is a reusable pattern when a method paper uses an LLM on a problem that already has a formal guarantee. They also refuse to trust the DBMS cost model alone, and they test robustness across datasets. The increment is "how rules are chosen", not "we replace the rewriter".
- **Do not copy:** dropping the rule system and asking an LLM to emit rewritten SQL as the official answer, which would abandon the equivalence argument this paper is careful to keep.

### 4. Magneto — B1-method on schema matching, with a new expert-collaborative bench as support

- Yurong Liu, Eduardo H. M. Pena, Aécio Santos, Eden Wu, Juliana Freire. *Magneto: Combining Small and Large Language Models for Schema Matching.* PVLDB, 18(8): 2681–2694, 2025. doi:[10.14778/3742728.3742757](https://doi.org/10.14778/3742728.3742757). Official PDF: https://www.vldb.org/pvldb/vol18/p2681-freire.pdf
- **Thinking to reuse:** they first name the limits of each family (SLMs need training data; LLMs are expensive and context-limited), then design a two-phase pipeline (retrieve with SLM, rerank with LLM) that addresses both. A new biomedical benchmark, built with domain experts, is a **support** for the method paper, not the first contribution—they still evaluate on existing benches as well. Self-supervised data generation is justified as a way to avoid "costly, difficult-to-obtain training data".
- **Do not copy:** leading a method paper with a new benchmark as if that were the scientific claim; Magneto keeps the method first.

### 5. CHORUS — B1-method that unifies existing discovery tasks

- Moe Kayali, Anton Lykov, Ilias Fountalis, Nikolaos Vasiloglou, Dan Olteanu, Dan Suciu. *CHORUS: Foundation Models for Unified Data Discovery and Exploration.* PVLDB, 17(8): 2104–2114, 2024. doi:[10.14778/3659437.3659461](https://doi.org/10.14778/3659437.3659461). Official PDF: https://www.vldb.org/pvldb/vol17/p2104-kayali.pdf
- **Thinking to reuse:** three already-defined tasks (table-class detection, column-type annotation, join-column prediction) are kept as the evaluation surface; the claim is a unified foundation-model approach that outperforms task-specific SOTA and is compared, where possible, to human-expert performance. They investigate generalizability across foundation models and the effect of non-determinism—an honesty item method papers often skip. The future-work sentence ("disparate tasks can be unified") is bounded by what they actually measured.
- **Do not copy:** collapsing several tasks into one headline number; they report per-task.

### Extra (read, same standard)

- Tianji Cong, Fatemeh Nargesian, Junjie Xing, H. V. Jagadish. *OpenForge: Probabilistic Metadata Integration.* PVLDB, 18(9): 2914–2927, 2025. doi:[10.14778/3746405.3746417](https://doi.org/10.14778/3746405.3746417). Official PDF: https://www.vldb.org/pvldb/vol18/p2914-cong.pdf — formalises integration as an MAP assignment with an MRF that encodes transitivity; reports a large F1 gap over GPT-4 on a vocabulary-matching use case (25 F1 points, from the abstract). Lesson: a classical probabilistic formulation can be the increment, with the LLM only as a prior.

## Transferable writing and experiment habits

- **Motivation chain:** a single inspectable failure (REDSQL's BIRD example; Sphinteract's ambiguity) beats a survey-tone opening.
- **Keep the formal guarantee where it already exists** (LLM-R2's rule system). An LLM recommends, a checker or a rule decides.
- **Strong baselines:** task-specific published methods and, when relevant, human performance (CHORUS) or a strong LLM alone (OpenForge, Magneto).
- **Wins:** attribute them to a named mechanism (two-phase retrieve-rerank; constraint verification; rule recommendation), not to "we use a larger model".
- **Honesty:** non-determinism, cost, and robustness across datasets belong in the main text (CHORUS, LLM-R2).
- **A new dataset in a method paper is supporting evidence**, evaluated alongside existing benches (Magneto).

## Experiment checklist

- [ ] Nearest neighbour stated in one falsifiable sentence.
- [ ] Mandatory baselines include the strongest published and the strongest callable model or system a reviewer would name; constructed controls are labelled as such.
- [ ] Official metrics and the SOTA gate pre-registered; official fold evaluated once.
- [ ] Best bold, second underline, W/T/L, 95% CI; direction of each metric in the caption.
- [ ] Every loss or tie explained once, with a mechanism; no post-hoc metric change.
- [ ] Efficiency, cost, or robustness reported if the claim depends on them.

## Writing checklist

- [ ] Problem language matches the literature; increment is not a rename.
- [ ] Related work bounds the claim; concurrent submissions declared if required by the venue.
- [ ] Limitations and non-goals are in the main text.
- [ ] Venue guidelines (pages, artifacts, identity) re-read this cycle.

## Quality gates and failure handling

A method paper that is second on the majority of official metrics, or first only against a weakened baseline, is not "SOTA". Say so and either improve the method on development data or narrow the claim. If a published system cannot be run, leave the row empty and explain; do not invent it. If reading shows the problem was not actually pre-defined, switch to the B2 skill and restart the storyline.

## Version

- 0.1 (2026-11-12, America/Los_Angeles): first skeleton, five primary PVLDB papers plus OpenForge, all from official PDFs. To be expanded to 15–25 papers (ICDE and SIGMOD inclusive). Reuses hygiene rules from `skills-drafts/metric-certification-eval-hygiene.md` and `pre-submission-hardening.md` without copying project-specific scores.
