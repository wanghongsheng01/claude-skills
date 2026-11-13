---
name: "write-pvldb"
description: "Writing guide for PVLDB / VLDB (CCF-A), built from officially published PVLDB, SIGMOD, ICDE and VLDBJ papers read in full: title and abstract patterns, introduction and contribution lists, method sections with theorems, experiment sections structured by RQ with takeaways and W/T/L tables, related work, figures and tables, references, the 12-page body budget, EA&B-specific writing, and a dedicated guide on how to state limitations, losses and not-done work without self-negation — the practice of accepted papers, not a licence to hide facts. Use when drafting, restructuring or polishing a PVLDB paper (写 PVLDB / 写 VLDB / 局限怎么写 / 不要自我否定 / EA&B 写法 / 实验怎么写)."
---

# Writing for PVLDB (Write-PVLDB 写作指南)

Evidence comes from accepted papers, not from this skill's opinions. Primary corpora (full-text reads; details and paper-by-paper notes in `references/` and in the sibling skills named below):

- Ten accepted papers on exact or dynamic cohesive-subgraph computation (ICDE 2025–2027 R1, TKDE 2022, VLDBJ 2019, **PVLDB 2021/2025**, **SIGMOD 2023**), used for limitation-writing rules: `write-icde/references/limitations-writing.md`.
- Sixteen accepted EAB/benchmark papers (ICDE 2024–2027 R1 and **PVLDB EA&B**), used for EAB limits: `write-icde/references/limitations-writing-eab.md`.
- Twelve **PVLDB 2023–2026** papers used for experiment-analysis habits: `experiment-analysis-writing` and `write-vldb/references/experiment-analysis-from-pvldb-2023-2026.md` (Dawn of NL2SQL, DAIL-SQL, Sphinteract, TACO, SemBench, Annotation Errors, REDSQL, and others).
- Caching, view-reuse and access-control papers (ICDE, PVLDB, SIGMOD) in `write-icde/references/limitations-writing-caching-access.md`.

Use with `submit-pvldb` (official rules) and `review-pvldb` (simulated review). Official PVLDB pages always win. This skill **supersedes** the shorter `write-vldb` for new drafts; it does not change any official rule.

## Language convention

Manuscript, captions and revision letters in **English**. Author-facing plans in **Chinese (中文)**.

## Integrity boundary (non-negotiable)

Rules in this skill change **placement, frequency, wording and framing only**:

- every measured number stays in the tables;
- no claim becomes false;
- no competitor or losing cell is hidden;
- venue-mandatory statements stay (related-submission declaration, AI acknowledgment if required, artifact URL, honest-annotation or protocol premises).

A text that contradicts its own tables is a common rejection reason. Honesty and persuasion point the same way. “Do not self-negate” is **not** “do not disclose.”

## 1. Title

Regular research: a precise technical object, often `Acronym: … for X`, or a claim phrase with the setting. Median length in neighbouring ICDE/PVLDB samples is about 9–12 words. Do not put a limitation in the title.

EA&B: append the submission suffix **`[Experiment, Analysis & Benchmark]`** to the title in the PDF and in CMT (`submit-pvldb`). The suffix is removed in the camera-ready.

## 2. Abstract (about 150–250 words; no citations)

Context → the assumption existing methods share → “We present X” → key insight → components → evaluation scope → one or two headline numbers with the **same wording** as the body (“up to”, “on average”, “in every run”) → artifact.

**Limits in the abstract, as accepted papers write them.** In the 10-paper algorithm corpus, **0/10 abstracts state a loss** against a baseline. **4/10** put a *scope qualifier* on the positive claim (approximate, a condition, a class of updates). In the EAB corpus, **method** negatives can be the headline (they are findings about systems under test); **benchmark** negatives appear in **0/5** (Part A) and **0/4** (Part B) abstracts. Never use the abstract to list what you did not implement.

## 3. Introduction (about 5–7 paragraphs, ~1.3 pages)

1. Scenario and why scale or cost matters (a concrete number helps).
2. Existing solutions and the assumption they share.
3. A figure or measurement that shows the assumption breaking.
4. Challenges C1–C3 with bold run-in labels.
5. The approach, mapping each challenge to a component.
6. Contributions, 3–5 items with section numbers; the last item states the experiments and headline results, and mentions released code.

**Limits in the introduction.** At most **one** scope sentence, with a section pointer, phrased as what the result covers: “X is guaranteed for A; case B is discussed in Section Z” (template of IMCE, Das et al., *VLDB Journal* 28, 2019). Or declare the design focus (HCM, Lin et al., *PVLDB* 14(5), 2021). Do **not** list every weak regime, and do **not** tell the reviewer that a result “would not survive review.”

## 4. Problem, method, theorems

Preliminaries and a `Definition` of the problem (inputs, constraints, objective). Each method subsection: motivation, definitions, `Theorem` or `Lemma` with a short proof or a pointer to a public technical report (appendices **count toward** the 12-page PVLDB body — unlike SIGMOD research). One paragraph on practical meaning, and an algorithm box. Scope of a theorem belongs **in the theorem statement** (e.g. “date-grain only”), not in a later humility paragraph that retracts it.

## 5. Experiments (typically 25–55% of the body)

Setup: datasets, baselines (include PVLDB/SIGMOD/ICDE methods and special cases of your method), metrics, cost units with list prices and date if money is reported, hardware, freeze and SHA if folds are frozen, number of repetitions and dispersion.

Then **one subsection per RQ**, each ending in a bold **Takeaway**. Required blocks in a method paper: main result (quality and cost together), validity of guarantees, factor sweeps (where it helps **and** where not), ablation, other backbones or vendors, overhead and sensitivity.

Presentation (Deng S01–S11, already in `results-presentation-review`):

- claim-first captions;
- **bold** the best, **underline** the second best;
- a W/T/L or count row; an average or geometric-mean row when a table goes up and down;
- colour-blind-safe figures;
- **keep every losing cell**;
- explain a loss **once**, in the experiment that measures it, in the order **fact → mechanism → regime → bound** (2–4 sentences).

First-place metric: name the *component*, the *problem* it targets, and the ablation row that returns the metric to the baseline when the component is removed (REDSQL’s “we attribute this difference to…” is legitimate only with that row). Lead with a numeric delta, then “This is because…” (Sphinteract, *PVLDB* Vol. 18). Structure evaluation as RQs; Dawn of NL2SQL’s “Q2: Are LLM-based Models the Clear Winner?” is the model for **refusing a blanket win** — that is a finding, not self-negation.

Close with three to five numbered **Lessons** that contain a “because” and, where useful, a measurable regime (Zeng et al., *PVLDB* Vol. 17: “When the NDV ratio grows larger (e.g., > 0.1), dictionary encoding becomes less effective”).

Public data carries the main table. Any conclusion drawn on non-public enterprise data must also hold on public data; say so and show it.

## 6. Related work

Three to five themed paragraphs; end each with how this paper differs. **Actively declare** related concurrent submissions, marked “under submission”, as PVLDB requires (`submit-pvldb`). Position against the nearest published neighbour; a missing citation of a close system is a review risk, but the cure is to **cite and position**, not to write “we did not cite X.”

## 7. How to state limitations without self-negation

This is the section that accepted PVLDB/SIGMOD/ICDE papers actually follow. Full counts: `references/limitations-without-self-negation.md` and the `write-icde` limitation files.

### 7.1 What the corpora never do

| Practice | Algorithm corpus (10 papers) | EAB corpus (own benchmark) |
|---|---|---|
| Abstract states a loss of the authors' method / a limit of their own benchmark | **0/10** | **0/9** (Part A 0/5, Part B 0/4 strict) |
| Conclusion lists cases where the method loses, or limits of the authors' own benchmark | **0/10** | **0/9** |
| A dedicated “where we fail” heading about the authors' own method | **0/10** | “Limitations” headings, when used, are about **evaluated methods** (2/5), not the benchmark |
| The word “limitation(s)” applied to the authors' own method or benchmark | essentially unused | **0/9** |
| “does not help”, “fails” (about themselves), “the advantage vanishes”, “only N×” for their own speedup | **never** | “fail” is used freely about **systems under test**, never about the benchmark |
| “bug”, “rerun”, “mistake”, “unfortunately”, “honest residual”, “we report rather than paper over” | **never** | **never** (0/5 for the first four) |
| Typical length of a negative result | **1–4 sentences, once**, next to the number | same; a labelled Threats block, when present, is about **110 words** (TS-Fault, 1/5) |

Typical vocabulary of accepted papers: *comparable, on most datasets, slightly, marginal, nevertheless, on the whole, still, we recommend, we focus on, out of the present scope, not supported in this version.*

### 7.2 Rules (wording only; numbers stay)

**R1. Abstract: scope qualifier, not a separate negative sentence.** At most one qualifier clause per claim. No abstract sentence that the gain shrinks or vanishes.

**R2. Introduction: one scope sentence with a section pointer.** After the contribution it qualifies. Do not preview every weak cell.

**R3. State each negative result once, where its number is shown.** No “where we fail” heading. Takeaways and the conclusion summarise scope without repeating exceptions.

**R4. Fact → mechanism → regime → bound, in 2–4 sentences.** (1) Name the cells. (2) Why, with a measured statistic. (3) Which regime, or what the design targets. (4) Bound the impact (“nevertheless”, an absolute gap, or a count). Star (Sun et al., *SIGMOD* 2023) is the clearest example; also LazyMC (TKDE 2022) and HCM (*PVLDB* 14(5)).

**R5. Explain losses by properties of the instance or workload, not by deficits of the method.** Prefer statistics already in the paper (core size, number of fallbacks, support-set size, eligible-service count). Example pattern: “With only *k* eligible services, the bound lists have little to prune.” That is a regime, not “our method fails at production size.”

**R6. Frame weak regimes as design trade-offs and give operating guidance.** HCM recommends rebuilding for very large batches. DMI announces a rebuild-frequency trade-off in the method section. Star points out that its target workload is star insertions. An industrial paper (SIGMOD Industrial) says where the payoff is (e.g. maintenance vs single-query latency) as guidance for operators.

**R7. Report one-off costs once, in a cost paragraph or table, and justify them by amortisation.** A break-even count, or a price-versus-benefit judgement.

**R8. Not-done work is a scope sentence or a silent omission, not a checklist of “we did not.”** If a reviewer *needs* the fact to judge validity (a standard baseline was not run; a fold is DEV-only; a companion theorem is outside the frozen rule), state it **once**, next to the affected claim, as a bounded design or protocol fact: “CodeS is profiled on DEV under the official checkpoint; we do not estimate an official-TEST row.” If the fact does **not** affect a headline and is only internal audit (process language, “we will not retune”, “no cell was invented”, “this would not survive review”, “we do not claim December readiness”), **delete it**. If deleting a fact would be read as concealment, **keep** it and reframe; flag it as `保留` in any revision plan.

**R9. Conclusion: fold scope into the headline; do not end with a laundry list of remaining limits or future work.** 0/10 algorithm papers list losses in the conclusion; 3/10 fold scope into the claim; only 1/10 names a technical gap as future work (HCM), hedged. 0/9 EAB papers put benchmark limits in the conclusion. Future work, if any, is one short sentence on a technical extension, not a confession.

**R10. “Threats to Validity” is optional and short.** Algorithm papers: 0/10 dedicated failure sections. EAB: 1/9 have a labelled threats block of about 110 words, at the end of the Discussion, about construct/internal/external validity — not a process diary, and never “we are not ready for this cycle.” Preferred: put each threat next to the design decision it affects (0/4 Part-B EAB papers have a separate threats section at all).

**R11. Keep “limitation”, “fail”, “honest”, “bug” off your own method or benchmark.** Use them for prior work or for systems under test. Preferred frames: *scope, design choice, operating regime, protocol, frozen rule, future extension.*

### 7.3 Templates (English, for the manuscript)

- **Loss cell:** “On *D*, seed *s*, *M* uses *n* executions against *n′* for *B*. The selector kept configuration *C* because the validation slice of *v* calls was too short to accumulate the unpinning evidence; *g* ghost hits then unpinned *k* views. This is the only loss against *B* on the *N*-cell headline grid (*W*/*T*/*L*).”
- **Regime / operating guidance:** “At a portfolio of *n* services the compiled single query is within *p*% of brute force; the production payoff at this size is maintenance of stored answers (*s*× on logged edits).”
- **Frozen rule / not retuning:** “The residual-time identity is stated for date-grain summaries (Lemma *L*). The four held-out paths fall outside that statement. The certifier is not modified after a held-out evaluation.”
- **Missing run that cannot be estimated:** “System *S* is evaluated on the development split under the authors' official checkpoint; an official-TEST number is reported only from a completed run, and is not estimated.”
- **Companion / related submission:** “Join safety is the object of a companion submission [under submission] and is outside the present claim.” (This is a PVLDB-required declaration, not a humility sentence.)
- **What not to write:** “This result would not, by itself, survive a PVLDB review.” “The remaining limits are *A, B, C, D, E*.” “A limitation, which we report rather than paper over.” “We do not claim December readiness.” “No cell was invented.” “The official drop is the honest generalization gap.” “Where we are not first.”

## 8. EA&B-specific writing

An EA&B paper's contribution is insight, a protocol, and reusable artifacts — not “our method wins.” Report a reference protocol as a **profile point**. Findings about systems under test (a naive always-answer system leads EX and trails TA; a frontier model does not significantly beat naive) **belong** in the abstract and conclusion: they are the scientific claim. Limits **of the benchmark itself** do not.

Turn a validity threat into a measured RQ when you can (7/9 EAB papers in the combined corpus do this). Inter-annotator agreement is **not** required by the EAB corpus (0/4 Part B report it, and 0/4 apologise for not collecting it): if gold is mechanical verification of a generator, say that as a protocol, not “we did not collect a κ.”

Volume 20 requires the **full reproducibility package at the initial submission** (`submit-pvldb`). Describe what a third party can regenerate; do not describe the package as a list of things it does **not** contain, except for legally necessary exclusions (raw enterprise data, a companion's official test fold).

## 9. Figures, tables, references

Claim-first captions, one or two lines; do not restate the body. Colour-blind-safe, no decorative 3-D, readable at print size. References: ACM Reference Format as in the official PVLDB template; cite DB-venue neighbours in a way that goes “beyond a syntactic citation” (PVLDB scope policy). Embed fonts. The body must end by page 12; references may continue.

## 10. Workflow

1. Re-open `submit-pvldb` official pages; record the access date.
2. Draft against the 12-page body; move only references beyond page 12.
3. Run a **self-negation pass** (Section 7 checklist, also in `review-pvldb`): abstract and conclusion free of method/benchmark laundry lists; each loss stated once with a mechanism; no process language; mandatory disclosures kept.
4. Run `results-presentation-review` and `academic-latex-polish` if available.
5. Related-submission declaration; artifact URL; AI acknowledgment if the cycle requires it, shortened to the venue form.
