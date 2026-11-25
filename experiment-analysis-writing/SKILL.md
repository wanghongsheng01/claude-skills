---
name: "experiment-analysis-writing"
description: "How to write the experiment-analysis section of a CCF-A data-management paper so that a two-minute reader can see (i) that the method is first on the vast majority of metrics and (ii) why any second-place or losing cell is not a mystery. Distilled from 12 PVLDB Vol. 17–19 papers (2023–2026) in NL2SQL, semantic benchmarks, materialized-view rewriting, k-plex, and empirical format studies, plus 邓老师's meeting guidance (bold/underline, count or mean row, takeaways, analyse losses with a scenario rule). Use when drafting or revising an evaluation section, an ablation, a 'when we are not first' paragraph, a Lesson/Takeaway, or a workload→method decision rule (实验分析 / 第二名机制 / Takeaway / 消融 / 何时选用)."
---

# Experiment-analysis writing

This skill is about **how to write the analysis**, not how to run the experiments. Numbers must already exist in a repository record. Do not invent a cell, drop a measured loss, or promote a development-set score to the main table.

It does **not** replace `results-presentation-review` (S01–S11), `paper-presubmission-review`, or the venue skills (`write-vldb`, `write-icde`, …). After drafting, run those checklists. **Do not edit those skills from here.**

Language: manuscript English; reports to the author in Chinese.

The PVLDB sample and the advisor notes were read on **2026-11-12**. Official venue rules always win over advisor or sample habits (for example PVLDB appendices count toward the 12-page body; ICDE forbids an appendix). See `write-vldb` and `paper-presubmission-review/references/venue-conflicts.md`.

## 1. What reviewers look for (and what 邓老师 asked to see)

Two questions, in order:

1. **Performance at a glance.** Is the method first on the vast majority of metrics against the strongest *run* baseline? If a cell is second, can I see it in two minutes (bold / underline / a count row)?
2. **A precise story for every standing.** For a *first-place* metric: which component addresses which problem, and where is the ablation that isolates the gain? For a *second-place or losing* metric: why is the winner good there, in which regimes is ours better, and when should a practitioner pick theirs versus ours?

邓老师's meeting records (ICDE review with 王宏升; figure review) add: mark the best and the second; add a summary row when signs differ across datasets; if the method loses to a baseline, write the analysis and the takeaway — do not leave the cell hanging; compress captions to one or two lines and do not repeat the body's numbers in the caption; do not keep a dataset-statistics table that adds no method signal.

A historical request to "reduce honest disclosure" is **not** adopted.

## 2. Section shape (recurring in the PVLDB sample)

Use this order, named as RQs or as numbered subsections. It matches Dawn of NL2SQL (Q1/Q2), SemBench (5.1 setup → 5.5 system comparison), REDSQL (performance then ablation), and the MV-rewriting benchmark (stage-wise analysis then a decision rule).

1. **Setup.** Datasets, metrics (higher-is-better and lower-is-better stated once), baselines with a fair protocol ("we follow [X] for metric M"), hardware, repetition and dispersion, budget (tokens, time, memory) held constant across LLM systems. PVLDB Artifact Availability statement for EA&B, at *initial* submission on Vol. 20.
2. **Main quality table (RQ1).** One question per table. Bold the best printed value, underline the second, including when a baseline wins. A Best / 2nd / worse **count row**. End with a bold **Takeaway**.
3. **Where we are not first (RQ2).** Its own subsection, not a footnote. Fact → mechanism → regime → choice rule (templates in §4).
4. **Ablation (RQ3).** One row per claimed component. A "w/o C" row should return the affected metric near the baseline if C is truly the cause. Visually separate a summary row.
5. **Robustness / cost / other backbones (RQ4).** LLM papers include **GPT and Claude**, not only domestic or small open models. Report cost as well as quality (Evaporate's crossover; REDSQL's accuracy–cost figure; SemBench's cost–quality trade-off from prompt length).
6. **Lessons.** Three to five numbered lessons, each one sentence of finding + one sentence of "because" or "therefore". Columnar storage (Zeng et al., Vol. 17) is the cleanest model: "Lesson 1. … because … Future designs should …". EA&B papers may also close with research opportunities (Dawn of NL2SQL lists ambiguous queries and trustworthiness — useful neighbour for BindOrClarify).

Do not put a raw experiment log, a mostly-empty table, or a two-column "Experiment / Result" sheet in the body (梁老师; S11).

## 3. How published PVLDB papers write a gain (first place)

Patterns observed in the 12-paper sample (full list in `references/pvldb-sample-2023-2026.md`):

- **Lead with a measured delta, then the mechanism.** Sphinteract: report the execution-accuracy lift (e.g. +42.3% on Kaggle with GPT-4 Turbo), then "This is consistent with our expectations since addressing the different types of ambiguity… On the other hand, the simple feedback consistently yields lower accuracy. **This is because** the binary feedback does not directly resolve ambiguities." The clause *this is because* is the sentence the analysis must contain.
- **Name the component, not the whole system, as the cause.** REDSQL: "We observe that REDSQL performs optimally when integrated with [different] NL2SQL approaches… We attribute this difference to the refinement process acting as a model ensemble." Ablation and multiple backbones are what make "we attribute" legitimate.
- **Ask a question as a subsection title when the result could be misread.** Dawn of NL2SQL: "Q2: Are LLM-based Models the Clear Winner?" then splits EX vs EM, and linguistic phenomena — they refuse a blanket "LLM always wins". Annotation Errors: "Why does the EX of CHESS increase?" then answers with a false-negative pattern in the gold SQL. Use this when a headline number would otherwise over-claim.
- **If two implementations trade quality for cost, report both and the crossover.** Evaporate (Vol. 17): Evaporate-Code is on average 21.9 pair-F1 *worse* than Evaporate-Direct, and the authors say so in one sentence; they then give document-count and attribute-count crossover points. Losing on quality at a lower cost is written as a **trade-off with a numeric frontier**, not hidden and not apologised for in the abstract.

Template (first place, ablation-backed):

> *X improves metric M by Δ on workload W. Removing component C (Table n, row “w/o C”) returns M to approximately the baseline value, which indicates that C, rather than a change in the backbone or the prompt budget, accounts for the gain. C targets problem P (instance I, where the baseline exhibits behavior B).*

If there is no "w/o C" row yet, do not write this paragraph; run the ablation or weaken the claim to a correlation.

## 4. How they write a loss or a second place

This is the paragraph Dr.Wang asked to have in every paper. The sample does it in four moves. All four are required.

1. **State the standing in numbers**, with the winner bolded. Do not bury the loss in a "slightly lower" adjective.
2. **Why the winner is strong here** — a *design* or *workload* reason, not "it is a strong baseline". Columnar (Zeng et al.): "When the NDV ratio grows larger (e.g., > 0.1), this additional layer of Dictionary Encoding becomes less effective than ORC’s more sophisticated integer encoding." The regime is a measurable threshold. SemBench: Palimpzest vs LOTUS on semantic joins — LOTUS is cheaper because of embedding pre-filtering, **but** "pre-filtering can miss valid matches and leads to lower quality". Ahmad et al. on k-plex (Vol. 18): some pruning "only improve[s] performance for small k … but can lead to catastrophic performance when k is large", and they call out prior papers for not reporting this.
3. **Where ours is better** — a different metric, a different workload regime, or a constraint the winner does not meet (a certificate, a refusal, a permission scope). The MV-rewriting benchmark (Miao et al., Vol. 19): "The best enumerator varies by workload … indicating that enumerators differ not just in how many candidates they generate but in the types of views." They close with a **workload-feature → method-choice** rule. Copy that table shape: two or three rows, features a practitioner can observe, a recommended method, and a "do not use when".
4. **A practical choice rule**, one or two sentences, in the same subsection. Never only in the appendix.

Template (second place or loss):

> *On metric M, B* is first (v₁ vs. our v₂). B* is strong here because R (a property of its design, or of workload regime S₁). The same regime is exactly where B* fails on metric M′ (… ). Our method is first on M′ and on workloads S₂ with property Q. A practical rule is: choose B* when the deployment matches S₁ and M is the binding constraint; choose ours when Q holds or when M′ cannot be relaxed.*

Special case — **a baseline "wins" a metric by construction.** Example: an always-answer Text-to-SQL system has unnecessary-clarification rate 0, because it never clarifies; an always-refuse system never emits an illegal number. Write this as a **protocol signature**, not as a quality victory, and immediately point to the metric where that signature is costly (FAR, TA). Do not delete the cell; explain it. Dawn of NL2SQL's "are they the clear winner?" move is the model: split the headline.

If a failure is a single instance, name the instance, the predicted vs gold behavior, and the mechanism (family miss, budget starvation, bound that does not fire). Say what did *not* happen (e.g. "no silent wrong number"). Do not retune the method against a frozen held-out fold to erase the cell.

## 5. Paragraph, caption, title, and citation habits (sample)

**Paragraphs.** Academic present for method facts, past for what "we evaluated / we found". Lead with the number. "We observe that", "We find that", "This is because", "We attribute this to", "In contrast, on [workload]" are the common hinges. Hedge with "indicating that" / "suggests that" only when the evidence is correlational. Report exact deltas, not "significantly better" alone. SemBench states a significance rule in setup ("all comparative claims are based on a gap of at least three standard deviations") — if you use a rule, write it once in 5.1 and keep it.

**Captions.** The 12-paper sample is often *descriptive* ("Figure 6: Benchmark results with predefined workloads"; "Table 3: Baseline Performance on the TACO benchmark"). 邓老师 asked to *compress* captions to 1–2 lines and not repeat body numbers; S02 asks for a **claim-first** first sentence. These are compatible: first sentence = takeaway a two-minute reader can see; second sentence = setting (dataset, protocol). Do not paste the result table into the caption. Failure-case figures deserve a name ("Figure 9: Rewriting Failure Case of Sys-B" in the MV benchmark). DAIL-SQL uses green/red arrows in ablation figures for increase/decrease — acceptable if colour-blind-safe (S05) and also readable in grayscale.

**Titles (for the paper, not the figure).** Method papers in the sample: `Name: mechanism over setting` (Sphinteract, AltRB / Maximum k-Plex Search). EA&B and critiques often use a question or a verdict ("Are We Fully Ready?", "Pervasive Annotation Errors Break … Leaderboards", "Choices of Pruning Techniques Matter!"). PVLDB EA&B **suffix** is `[Experiment, Analysis & Benchmark]` (ampersand), in both the PDF and CMT, dropped in the camera-ready. ICDE uses a different prefix — do not mix (see `paper-presubmission-review`).

**Citations.** In related work, author + venue + year, and end the paragraph on *how this paper differs*. In the evaluation, use the **method name** with a citation, and describe the protocol you actually ran (prompt, model, budget), so "DAIL-SQL" is not an underspecified label. Do not attack a baseline for a failure that is the published protocol (always-answer Text-to-SQL has high FAR by design). For concurrent submissions by the same authors, PVLDB requires a self-declaration and an "under submission" citation; advisor advice to "not mention sibling papers" is overridden on this venue.

**Related-work placement.** In this sample, related work is often §2 or §2.x, not uniformly last. No official PVLDB rule forces it last. Do not move a section solely because "ICDE always does".

## 6. Workflow

1. Freeze the split and the metric definitions; record hashes and commits. Held-out numbers used in the main table must not have been used to edit the method.
2. Build the standing table (best / second / worse counts) against the strongest *completed* baseline. Missing GPT/Claude in an LLM paper is a gap, not a "N/A" that can be treated as a win.
3. For every first-place metric, write the §3 template only after the ablation row exists.
4. For every second-place or loss, write the four-move §4 paragraph and, if several losses share a regime, one decision-rule table.
5. Write 3–5 lessons. Run `results-presentation-review` and `paper-presubmission-review`. Check the venue page limit: in PVLDB this analysis lives in the 12-page body.

## 7. What this skill will not do

- Invent or interpolate missing baseline rows.
- Promote a template-set 100% or a single successful seed to a SOTA claim.
- Splice wall-clock numbers from two machines into one table.
- Move a loss to the appendix in order to "keep the story clean", or add a "Limitations: we are not always best" heading that self-negates in the abstract or the conclusion.
