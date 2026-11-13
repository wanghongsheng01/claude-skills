---
name: ccfa-b1-benchmark-writing
description: >-
  Use when writing a CCF-A benchmark, evaluation-protocol, or EA&B paper on a
  scientific problem the literature has already defined (B1-benchmark): how to
  justify a new suite, avoid turning a recommended configuration into a method
  hero, profile the strongest callable systems, and report insights that can
  invert a leaderboard. Do not use for a method paper's SOTA gate, and do not
  treat a new dataset as sufficient without a reproducible protocol and a
  clear gap in existing benches.
---

# Writing a B1 benchmark / EA&B paper

Official venue guidelines take precedence. For PVLDB Volume 20, EA&B papers must include a **complete reproducibility package at initial submission** (confirm on the live official page). This draft expands `skills-drafts/benchmark-paper-building/SKILL.md`. The scientific claim is an insight plus a reproducible protocol, not "our method is #1".

## When to use / when not

**Use** when the front-loaded research skill has classified the paper as B1-benchmark (dataset, diagnostic suite, empirical profile, or evaluation protocol on an existing problem).

**Do not use** as a stand-in for a method SOTA gate; do not hide a new model as the protagonist of a benchmark paper; do not claim to replace a neighbour that measures a different object.

## Inputs and outputs

**In:** the stage 1–6 document; existing benches and what they do and do not measure; a draft task design and a candidate baseline list.

**Out:** a gap statement against living neighbours; a data-construction and quality-control plan; a frozen official protocol; a profile matrix of strong systems; insight sentences a reviewer can quote; a reproducibility package checklist.

## Process (condensed from the existing note, plus lessons from papers below)

1. Re-read current venue benchmark papers a reviewer will compare you to. For each, write what it measures and what it leaves out. The new bench must be complementary on at least one axis.
2. If the phenomenon is rare, report its rate on a complete population before showing selected tasks. Publishing only flagship examples is selection bias.
3. Freeze the official test (hash, `evaluated=false`) before any official score. Gold-blind deterministic baselines may be scored after that commit. Paid or stochastic official evaluation is one-shot.
4. Design at least one official metric that can **invert** a leaderboard that the community already trusts, and report the old metric too, with rank correlation.
5. A reference protocol or "recommended configuration" is a profile point, never bolded as "our method wins SOTA".
6. Ship the reproducibility package at submission, not after acceptance. Isolate sister method papers: no shared official folds.

## Evidence standard

Same as the method skill: official PVLDB PDFs fetched 2026-11-12 from vldb.org. Numbers below appear in the papers' abstracts or opening as read.

## Papers read this round (seven; five are primary)

### 1. The Dawn of Natural Language to SQL — EA&B profile, not a new model as hero

- Boyan Li, Yuyu Luo, Chengliang Chai, Guoliang Li, Nan Tang. *The Dawn of Natural Language to SQL: Are We Fully Ready?* PVLDB, 17(11): 3318–3331, 2024. doi:[10.14778/3681954.3682003](https://doi.org/10.14778/3681954.3682003). Official PDF: https://www.vldb.org/pvldb/vol17/p3318-luo.pdf. Title carries the EA&B intent (the camera-ready may drop a bracketed label; do not rely on suffixes to count EA&B papers).
- **Thinking to reuse:** the title is a question about deployment readiness, not a new accuracy claim. They build a multi-angle framework (NL2SQL360) and compare leading methods across domains and SQL characteristics, then search a design space for a configuration (SuperSQL) that is competitive on Spider and BIRD (abstract: 87% and 62.66% execution accuracy on the Spider and BIRD test sets). SuperSQL is presented as what the framework **identifies**, which is the correct register for a recommended configuration.
- **Do not copy:** advertising the identified configuration as a standalone method paper's protagonist if the submission is EA&B.

### 2. DAIL-SQL — systematic prompt comparison that also proposes a solution

- Dawei Gao, Haibin Wang, Yichen Qian, Yaliang Li, Bolin Ding, Xiuyu Sun, Jingren Zhou. *Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation.* PVLDB, 17(5): 1132–1145, 2024. doi:[10.14778/3641204.3641221](https://doi.org/10.14778/3641204.3641221). Official PDF: https://www.vldb.org/pvldb/vol17/p1132-gao.pdf
- **Thinking to reuse:** they first compare existing prompt-engineering choices (question representation, example selection, organisation) and discuss pros and cons, **then** propose DAIL-SQL (abstract: 86.6% execution accuracy on the Spider leaderboard). They also report token efficiency, and they study open-source LLMs with and without fine-tuning—including disadvantages. A benchmark-evaluation paper is allowed to propose a system, but the evaluation of prior methods must come first and remain complete.
- **Caution:** this paper sits on the method/benchmark boundary. If our paper is EA&B, keep the insight and the protocol first; if it is a method paper, use the method skill's gate.

### 3. TACO — a new setting because existing benches exclude it

- Chao Deng, Ju Fan, Yuyu Luo, Qinliang Xue, Meihao Fan, Yuxin Zhang, Min Zhang, Xiaofeng Jia, Jing Zhang, Xiaoyong Du. *TACO: A Benchmark for Open-Domain Text-to-SQL with Ambiguous and Cross-Database Queries.* PVLDB, 19(6): 1386–1399, 2026. doi:[10.14778/3797919.3797942](https://doi.org/10.14778/3797919.3797942). Official PDF: https://www.vldb.org/pvldb/vol19/p1386-fan.pdf. Artifact: https://github.com/Akanezora0/TACO-Benchmark
- **Thinking to reuse:** Table 1 of the paper (comparison with Spider, BIRD, and TACO splits) is the model of a gap table: closed-domain, well-specified questions versus ambiguous, unspecified-database, cross-database queries. They mix 1,500 real smart-city examples with 13,000 synthetic ones and describe a synthesis pipeline that aims to preserve real-query complexity. A baseline (TACO-SQL) is introduced **to illustrate the difficulty and the limits of existing methods**, not as a SOTA hero; the abstract states that even the best method leaves a significant gap.
- **Do not copy:** a synthesis pipeline whose quality is not audited; they at least state the goal of preserving complexity. Gold quality remains a reviewer's question (see paper 5).

### 4. SemBench — a benchmark for a newly named system class

- Jiale Lao, Andreas Zimmerer, Olga Ovcharenko, Tianji Cong, Matthew Russo, Gerardo Vitagliano, Michael Cochez, Fatma Özcan, Gautam Gupta, Thibaud Hottelier, H. V. Jagadish, Kris Kissel, Sebastian Schelter, Andreas Kipf, Immanuel Trummer. *SemBench: A Benchmark for Semantic Query Processing Engines.* PVLDB, 19(8): 1754–1767, 2026. doi:[10.14778/3811243.3811249](https://doi.org/10.14778/3811243.3811249). Official PDF: https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf. Artifact: https://sembench.org
- **Thinking to reuse:** they define the object (semantic query processing engines that extend SQL with LLM-evaluated semantic operators on multi-modal data) before the tasks. Diversity is designed along three axes (scenarios, modalities, operators), which is how to argue coverage without a huge item count. This paper is also used in the B2 skill, as an example of naming a system class; here the lesson is evaluation design.
- **Do not copy:** claiming a "novel class" without saying how engines in that class differ from Text-to-SQL or from RAG; they do this in the opening. Our paper must do the same for its object.

### 5. Pervasive Annotation Errors — a negative result as the insight

- Tengjun Jin, Yoojin Choi, Yuxuan Zhu, Daniel Kang. *Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards.* PVLDB, 19(5): 931–944, 2026. doi:[10.14778/3796195.3796206](https://doi.org/10.14778/3796195.3796206). Official PDF: https://www.vldb.org/pvldb/vol19/p931-jin.pdf
- **Thinking to reuse:** the insight is that trusted benches are unreliable. Expert analysis reports error rates of 52.8% on BIRD Mini-Dev and 62.8% on Spider 2.0-Snow (abstract). Re-evaluation of 16 open-source agents on original versus corrected BIRD Dev subsets: relative performance changes from −7% to 31%, rank changes from −9 to +9. Rankings on the uncorrected subset correlate strongly with the full Dev set (Spearman's \(r_s=0.85\), \(p=3.26\times 10^{-5}\)) but only weakly with the corrected subset (\(r_s=0.32\), \(p=0.23\)). This is the model for: report the population rate, correct a subset, show both performance and **rank** movement, and test whether the distorted ranking generalises. A high error rate on a beloved bench is a result, not something to soften.
- **Do not copy:** correcting gold in a way that cannot be audited, or reporting only the agents that improve.

### Extra primary reads

- Shizheng Hou, Wenqi Pei, Nuo Chen, Quang-Trung Ta, Peng Lu, Beng Chin Ooi. *NL2SQLBench: A Modular Benchmarking Framework for LLM-Enabled NL2SQL Solutions.* PVLDB, 19(5): 1001–1015, 2026. doi:[10.14778/3796195.3796211](https://doi.org/10.14778/3796195.3796211). Official PDF: https://www.vldb.org/pvldb/vol19/p1001-hou.pdf — module-level metrics (schema selection, candidate generation, revision) plus efficiency; they also report gold-SQL and evaluation-rule problems. Lesson: a framework paper still needs insights that change how one would pick a method, including cost.
- Xinjie Hu, Zhengjie Miao. *Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting.* PVLDB, 19(11): 3772–3785, 2026. doi:[10.14778/3836663.3836724](https://doi.org/10.14778/3836663.3836724). Official PDF: https://www.vldb.org/pvldb/vol19/p3772-miao.pdf — they benchmark a **pipeline** (enumerate, select, rewrite) and industrial engines with limited observability, and they ask whether the pipeline is "solved", including regressions. Lesson for systems EA&B: end-to-end and per-stage questions; do not assume a rewrite is always a win.
- Tengjun Jin, Yuxuan Zhu, Daniel Kang. *ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines.* PVLDB, 19(2): 84–98, 2025. doi:[10.14778/3773749.3773750](https://doi.org/10.14778/3773749.3773750). Official PDF: https://www.vldb.org/pvldb/vol19/p84-jin.pdf — existing data-engineering benches cover isolated tasks; they define an end-to-end agent task (100 pipelines, 835 source tables, 203 models). Strongest reported agent correctly generates only 11.3% of data models, at mean $1.41 and 72.2 steps (abstract). Lesson: a low absolute score of strong agents is the insight; cost and step count belong next to accuracy.

## Transferable habits

- Gap tables against named living benches (TACO Table 1; ELT-Bench's "isolated vs end-to-end").
- Insights that a reviewer can quote, including negative and rank-inverting ones (annotation errors; ELT-Bench 11.3%; Dawn's "are we ready?").
- Recommended systems are profile points (Dawn's SuperSQL; TACO-SQL).
- Gold quality is part of the contribution or a threat (annotation-errors paper; NL2SQLBench's closing remarks).
- Efficiency and dollar cost are first-class (DAIL-SQL token efficiency; NL2SQLBench; ELT-Bench).
- Full-pipeline and cross-engine protocols when the object is a system (MV rewriting).

## Checklists and gates

- [ ] Neighbour gap table written from official PDFs.
- [ ] Population rate before selected tasks, if the claim is about a rare phenomenon.
- [ ] Official fold hash-frozen before scores; evaluated once; sister papers isolated.
- [ ] At least one metric that can change a familiar ranking; old metric also reported.
- [ ] Recommended protocol not bolded as a method SOTA win.
- [ ] Strongest callable published systems and models actually run, or listed as not-yet-profiled.
- [ ] Reproducibility package ready at submission (confirm live venue rules).
- [ ] Means have 95% CIs; W/T/L against a declared comparison; small denominators shown.

**Failure:** if official scoring shows that mid-tier models do not beat a naive baseline, that is a result. If gold errors are found, quantify them; do not silently edit gold to raise a score except to fix a factual error, and record the reason.

## Version

- 0.1 (2026-11-12, America/Los_Angeles): expands `benchmark-paper-building/SKILL.md` with seven official PVLDB papers (five primary). To be expanded to 15–25, including ICDE and SIGMOD EA&B papers.
