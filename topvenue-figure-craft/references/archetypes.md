# Figure 1 archetypes

Each entry has a sketch, when to use it, how strong examples emphasise the contribution, and published
examples (venue, year, figure number). "Prior" = existing approach, "ours" = the paper's contribution.
Sketch legend: `[box]`, `==>` accent edge, `-->` neutral edge, `xx` failure mark, `**` accent region.

---

## A1 Motivating measurement plot
```
 latency |        .prior
         |      .'      .ours-only-phase
  SLA ---+----:-------:------------
         |  .':     .'
         +---+-------+-----> load
           1.6     5.6      <- the only labels: the numbers the argument needs
```
- **Use when** one measurement proves the problem exists and the number is striking.
- **Emphasis:** a threshold line, dashed drop-lines to the axis, a difference arrow with "51% diff."; the bar the method selects is saturated and the others are tinted.
- **Examples:** DistServe (OSDI'24, Fig. 1); Take Out the TraChe (OSDI'23, Fig. 2); Affinity-aware leasing for stateful serverless workflows (ATC'25, Fig. 1, 100% stacked bars); When Not to Trust Language Models (ACL'23, Fig. 1); Blinded by Generated Contexts (ACL'24, Fig. 1); Unbiased Learning to Rank Meets Reality (SIGIR'24, Fig. 1).
- **Pitfalls:** plotting-library defaults, a legend covering an axis label, every baseline in a saturated colour.

## A2 Isomorphic contrast panels (prior vs ours on the same input; 2×2 or N+1)
```
            benign input           attack input
 prior   [in]->[sys]->[ok]     [in+ATTACK]->[sys]->[xx LEAK]
 ours    [in]->[sys]->[ok]     [in+ATTACK]->[sys]->[ok]
```
- **Use when** the contribution is a defence, a new paradigm or interface, or a fix, and one variable can be changed in isolation.
- **Emphasis:** exactly one cell in the alert colour; the concrete attack string or input written in the figure; ours placed last or bottom-right.
- **Examples:** StruQ (USENIX Security'25, Fig. 1); KG-CoT (IJCAI'24, Fig. 1, (a)(b) challenges + (c) ours); A Setwise Approach for Zero-shot Ranking (SIGIR'24, Fig. 1); Astute RAG (ACL'25, Fig. 1, 2×2 table of real statistics); Text2SQL evaluator on unlabeled data (ICDE'26, Fig. 1, top/bottom).

## A3 Timeline / execution-trace contrast
```
 success  --[1]--[2]--[3]------------------>
 failure  --[1]--xx--[3]--[3]--[3]---------> "invariant never reached"
          shared code / desired state on top
```
- **Use when** the problem is temporal: a crash mid-operation, leases, concurrency, incremental generation, or overlap that saves time.
- **Emphasis:** the alert colour appears only at the violation; both lanes share the time axis; in a trace, only the newly added step is coloured.
- **Examples:** Anvil (OSDI'24, Fig. 1); S/C bounded-memory materialization (ICDE'23, Fig. 1, before/after timelines, caption "Our intuition: …"); Fast Inference via Speculative Decoding (ICML'23, Fig. 1 trace, Fig. 5 aligned wall-time bars); Strongly Tail-Optimal Scheduling (SIGMETRICS/POMACS'24, Fig. 1.1, boost as a directed length on the time axis).

## A4 Concrete data / query instance
```
 SELECT ... WHERE sal = ANY(...)   ==rules [r1,r2,r3]==>   SELECT ... JOIN ...
 colour links clause <-> plan node (no connector lines)     Execution: > 5 min -> 1.67 s
```
- **Use when** the problem lives in data, in queries, or in a structural condition in theory work.
- **Emphasis:** the same colour links corresponding parts instead of lines; red/green spans mark wrong and gold answers; the result number closes the reading path; theory uses minimal pairs that differ in one spot.
- **Examples:** LLM-R2 (PVLDB'24, Fig. 1); R-Bot (PVLDB'25, Fig. 1); PURPLE (ICDE'24, Fig. 1, three strong systems failing on one question); Consistent Query Answering on Rooted Tree Queries (PODS'24, Fig. 1 minimal pair, Fig. 5 instance with underlined keys and dashed blocks); Take Out the TraChe (OSDI'23, Fig. 1, three-node transaction graph).

## A5 Insight sketch / reformulation
```
 outputs y0 xx  y1 xx  y2 ok          state space
      ^ equivalence                   |  serve-small | serve-big
      v                               |  ----threshold----
 nested sets E(y0) c E(y1) c E(y2)    +-------------------> work
```
- **Use when** the contribution is a way of seeing the problem: a guarantee, a set, a state space or a decision boundary. Typical for ML theory, conformal methods, scheduling and caching policy.
- **Emphasis:** the core symbol or definition written inside the figure (E(y) := {y′ : y′ ⇒ y}); 2–3 semantic hues encoding one binary state; often paired with a small evidence curve.
- **Examples:** Language Models with Conformal Factuality Guarantees (ICML'24, Fig. 1); Heavy-Traffic Optimal Size- and State-Aware Dispatching (SIGMETRICS/POMACS'24, Fig. 1.1 + 1.2); Strongly Tail-Optimal Scheduling (POMACS'24, Fig. 1.1).

## A6 Minimal reproducing code
```
 x = lib.op(t, min=0, max=-1)   # CPU: [...]   GPU: [...]   <- wrong
 ...                            # expected: [...]            <- correct
```
- **Use when** the paper is about testing, fuzzing, repair or differential testing.
- **Emphasis:** oracles written as end-of-line comments; red/green diff lines; the mutated token in red; real identifiers.
- **Examples:** Large Language Models are Zero-Shot Fuzzers (ISSTA'23, Fig. 1); Keep the Conversation Going (ISSTA'24, Fig. 1); AutoCodeRover (ISSTA'24, Fig. 1).
- **Pitfalls:** 4–5 pt code; curved arrows that leave the panel.

## A7 Annotated text teaser (coloured spans)
```
 Q: ...?   LM: "... [Frankfort] ... [Kentucky]"
                  ~~~~~~~~ red: wrong   ____ green: fixed
```
- **Use when** the paper is in NLP/IR: verification, hallucination, attribution, RAG. Put it on page 1, single column, right column.
- **Emphasis:** only the deciding tokens are coloured; red strikethrough plus green bold for edits; colour words in the caption act as the legend.
- **Examples:** RARR (ACL'23, Fig. 1); FactCHD (IJCAI'24, Fig. 1); Don't Listen To Me (USENIX Security'24, Fig. 1, side-by-side chat mock).

## A8 Aligned before/after on data units
```
 (a) prior   [q1][a1][q2][a2][q3] | prefill all
 (b) ours    [**][**][**][**][q3] | load cached, prefill 1
```
- **Use when** you need to show what caching or reuse saves, or what a rewrite or access-control rule changes.
- **Emphasis:** an identical grid in both panels with exactly one visual variable changed (saturation, or a highlighted injected filter).
- **Examples:** CachedAttention (ATC'24, Fig. 3); Membrane (PVLDB'24, Fig. 7, two plans that differ only in the injected filter); affinity-aware leasing (ATC'25, Fig. 6, ❶❷❸ with a red frame only on changed cells).

## A9 Positioning / trade-off plot
```
 quality |            * ours (bold label)
         |   o prior (bold label)     o  o
         +--------------------------> cost
```
- **Use when** the contribution breaks a trade-off: accuracy × cost, footprint × isolation, speed × quality.
- **Emphasis:** ours sits in the best corner with a bold label; one bold prior for reference; a single point colour.
- **Examples:** Large Language Models can Accurately Predict Searcher Preferences (SIGIR'24, Fig. 1); EAGLE (ICML'24, Fig. 1, headline result bars placed before the abstract).

## A10 Complexity / reduction landscape and proof roadmap
```
 [P1: PTIME] --> [P2: coNP-c] ==red: new==> [P3: Pi2p-c]
                      ^ grey: known
```
- **Use when** the paper proves a classification or dichotomy, or chains several lemmas into a theorem.
- **Emphasis:** new edges in the one accent colour (often red), known results in gray or green; the caption states the encoding ("an arrow from A to B means …").
- **Examples:** When is Shapley Value Computation a Matter of Counting? (PODS'24, Fig. 1); Outperforming Multiserver SRPT at All Loads (SIGMETRICS'26, Fig. 3 lemma roadmap); C-RAG (ICML'24, Fig. 2, definitions in solid boxes and theorems in dashed boxes).

## A11 Policy × scenario grid / small multiples
```
            future A          future B
 policy 1   |==|-----|       |==|--|
 policy 2   |=|------|       |===|-|
```
- **Use when** you analyse scheduling or caching policies across scenarios, or need several situations side by side.
- **Emphasis:** existing state in gray, only new events coloured; event times marked with vertical dashes in the same colour; values written inside the bars.
- **Examples:** Outperforming Multiserver SRPT at All Loads (SIGMETRICS'26, Fig. 1); Llumnix (OSDI'24, Fig. 1).

## A12 Annotated architecture (one contribution colour, numbered zoom-ins)
```
 [dev]->[template]->[LLM]->[output]      |** ours column **|
                     \--------------->   | (1) generate    |
                                         | (2) filter      |
```
- **Use when** the paper is an industry or platform paper, or the contribution *is* where something plugs into an existing workflow.
- **Emphasis:** the existing system in black and white, the contribution as one tinted region; ①②③ anchors repeated in zoom-in panels, the caption and the text.
- **Examples:** SPADE (PVLDB'24, Fig. 1); DataLab (ICDE'25, Fig. 1, full-width overview + three zoom-ins); C-RAG (ICML'24, Fig. 1). Counter-examples with diagonal edges crossing containers: TGW cloud gateway (ATC'25, Fig. 1); on-demand container loading (ATC'23, Fig. 3).

## A13 Concept sketch + result inset
```
 [new memory structure sketch]   |  bars: baselines .. ours* .. human-upper-bound
```
- **Use when** the reviewer needs both the new concept and the proof that it helps, in one figure.
- **Examples:** AriGraph (IJCAI'25, Fig. 1); CachedAttention (ATC'24, Fig. 1).

---

## Why the "pipeline band + running-example band" template reads as generic
1. It shows what was built, not why it matters.
2. Every box has equal weight, so there is no focal point.
3. Two horizontal bands mean two reading paths.
4. The example is written as prose, not drawn.
5. Nested containers force edges through borders and titles.
6. The same template across many papers reads as mass-produced.
7. A full-width page-1 figure crowds out the introduction.

The one published case where it works (C-RAG, ICML'24) uses the lower band for *numbered guarantees*. That is new information, not a retelling of the pipeline.
