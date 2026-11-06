# Stating limitations without self-negation (ICDE / VLDB / SIGMOD practice)

Evidence: ten accepted papers on exact or dynamic cohesive-subgraph computation (ICDE 2025, ICDE 2027 R1,
TKDE 2022, VLDBJ 2019, PVLDB 2021/2025, SIGMOD 2023), read in full on 2026-11-06. Each item below is
an observation from those papers, not an official rule of the venue.

**Integrity boundary.** These rules change placement, frequency, wording and framing only:
- every measured number stays in the tables;
- no claim becomes false;
- no competitor is hidden.

A text that contradicts its own tables is one of the most common rejection reasons, so honesty and
persuasion point the same way.

## 0. Corpus and how it was read

| # | Paper (short name) | Venue | Full text used | Topic |
|---|---|---|---|---|
| P1 | Maintaining Leiden Communities in Large Dynamic Graphs (**HIT-Leiden**) | ICDE 2027 R1 | local arXiv 2601.08554v5 (full version) | dynamic community maintenance |
| P2 | Scalable Algorithm for Dynamic Quasi-clique Detection (**DMI**) | ICDE 2027 R1 | local arXiv 2605.26235v2 | dynamic maximum quasi-clique (approx.) |
| P3 | Maximal Clique Enumeration with Hybrid Branching and Early Termination (**HBBMC**) | ICDE 2025 | local arXiv 2412.08218v1 | exact static MCE |
| P4 | Fast Maximization of Current Flow Group Closeness Centrality (**CFCM**) | ICDE 2025 | local arXiv 2504.04472v1 | static approximation algorithm |
| P5 | Continuous Monitoring of Maximum Clique Over Dynamic Graphs (**LazyMC**, our baseline) | TKDE 34(4), 2022 | local publisher PDF (14_graph/refs) | exact dynamic maximum clique |
| P6 | Incremental Maintenance of Maximal Cliques in a Dynamic Graph (**IMCE**, Das, Svendsen, Tirthapura) | VLDB Journal 28, 2019 | arXiv 1601.06311 (preprint of the journal version) | exact dynamic maximal cliques |
| P7 | Hierarchical Core Maintenance on Large Dynamic Graphs (**HCM**, Lin, Zhang, Lin, Zhang, Tian) | PVLDB 14(5), 2021 | official vldb.org PDF (p757) | k-core hierarchy maintenance |
| P8 | Efficient Star-based Truss Maintenance on Dynamic Graphs (**Star**, Sun, Huang, Liu, Xu) | SIGMOD 2023 (PACMMOD 1(2)) | author PDF (HKBU homepage) | k-truss maintenance |
| P9 | Approximate Anchored Densest Subgraph Search on Large Static and Dynamic Graphs (**AADS**, Zhang, Zhang, Li, Wang) | PVLDB 18(3), 2024/25 | official vldb.org PDF (p623) | densest subgraph, static + maintenance |
| P10 | Finding Near-Optimal Maximum Set of Disjoint k-Cliques in Real-World Social Networks (**DkC**, Lin et al.) | ICDE 2025 (the arXiv comment says it was accepted in ICDE 2025) | arXiv 2503.20299 | disjoint k-cliques, static + maintenance |


## 2. Cross-paper observations

| Observation | Count | Papers |
|---|---|---|
| The abstract states a loss against a baseline | **0 / 10** | — |
| The abstract carries a scope or condition qualifier on the positive claim | 4 / 10 | P2 (approximate), P3 (condition), P8 (star updates), P9 (approximation bound); P7 does the same in the introduction, not the abstract |
| The introduction or contribution list states a limitation | 3 / 10, each in 1–2 sentences | P3 (condition, counted positively), P6 (fully dynamic case, 1 sentence + pointer), P7 (design focus) |
| The conclusion lists cases where the method loses | **0 / 10** | — |
| The conclusion folds the scope into the headline claim | 3 / 10 | P3, P7, P8 |
| The conclusion has future work that names a technical gap | 1 / 10, hedged; P1 and P8 list only extensions | P7 |
| A dedicated "where we fail" heading or paragraph | **0 / 10** | — |
| Losing cells in tables are shown unchanged | 10 / 10 | all |
| Losing cells are named in the text | 7 / 10 | P2, P3, P5, P6, P8, P9, P10. P7 says "most datasets". P1 and P4 have no runtime losses |
| A loss is followed by a mechanism within the next 1–3 sentences | 9 / 10 | all except the memory sentence of P2 |
| Costs (index, warm-up, memory) are reported in their own cost paragraph or table | 6 / 10 | P1, P2, P5, P8, P9, P10 |

Typical length: one negative result takes 1–4 sentences and appears **once**. The longest treatment is P5's deletion study (about 10 sentences), and most of it is explanation, not concession.

Typical vocabulary: comparable, on most datasets, slightly, marginal, nevertheless, on the whole, still, we recommend.

Never seen in the corpus: "does not help"; "fails" applied to the authors' own method; "only" applied to the authors' own speedup (it is used for costs, never for the method's gains); "the advantage vanishes".


Self-negating phrases about the authors' own method that the corpus never uses:
"does not help", "fails", "the advantage vanishes", "only N×" for the method's own speedup.
`scripts/icde_structure_check.py` flags them.

## 3. Writing rules

Each rule keeps every measured number. "Supported by" lists the papers that show the pattern.

**R1. Abstract: express limits as scope qualifiers of the positive claim, not as a separate negative sentence.**
Use at most one qualifier clause per claim, for example "under repeated harmful deletions in a large dense region", "for k ≤ 2", or "on graphs whose (ω−k)-core is large". No abstract in the corpus has a sentence saying that the gain shrinks or vanishes in some regime.
*Supported by: P3, P7, P8, P9, P2; 0/10 abstracts state a loss.*

**R2. Introduction: one scope sentence with a section pointer, phrased as what the result covers.**
Place it right after the contribution it qualifies. Template: "X is guaranteed for A; case B is discussed in Section Z." The template follows P6. Alternatively, declare the design focus as P7 does. Do not list every weak regime in the introduction.
*Supported by: P6, P7, P3.*

**R3. State each negative result once, where its number is shown; do not create a "where we fail" heading.**
Put the concession inside the paragraph of the experiment or RQ that measures it. The takeaways and the conclusion then summarise the scope without repeating the exceptions. No paper in the corpus has a dedicated failure heading.
*Supported by: all ten; clearest in P5 (6.2.3), P7 (5.1), P8 (Exp-I, Exp-V).*

**R4. Use the four-step order: fact → mechanism → regime/scope → bound.**
1. Name the cells.
2. Explain why in one sentence, using a measured statistic.
3. Say which regime the cells belong to, or what the design targets.
4. Bound the impact with a "nevertheless" sentence, an absolute gap, or a count.

Keep the whole unit to 2–4 sentences.
*Supported by: P8 (most explicit), P5, P7, P6, P4.*

**R5. Explain losses by measurable properties of the instance or workload, not by deficits of the method.**
Prefer statistics already in the paper, such as core size, number of fallbacks, cost-component share, or the probability that an update hits the optimum. Example: "When the dense core has about 460 vertices, an external solver call costs less than a budgeted local search."
*Supported by: P6 (cost breakdown 30–45% vs 2%), P3 (NA/DE ratios), P7 (more than 95% split candidates on small graphs), P5 (ω ≪ |V|), P1 (update ratio), P8 (onion-layer changes on LJ).*

**R6. Frame weak regimes as design trade-offs and give operating guidance.**
Examples from the corpus:
- P7 recommends rebuilding for very large batches.
- P2 announces the rebuild-frequency trade-off in the method section.
- P8 points out that its target workload is star insertions.
- P10 and P2 frame a faster but weaker method as a quality–time trade-off.

Example: an optional warm-up — say when to use it and when the external solver is the cheaper path; present it as an observation from the measurements, not as a new method feature.
*Supported by: P7, P2, P8, P10.*

**R7. Report one-off and auxiliary costs once, in a cost paragraph or table, and justify them by amortisation.**
Give the cost with its cause, then an amortisation argument:
- a break-even count (P10: one rebuild costs as much as millions of updates);
- an explicit price-versus-benefit judgement (P5);
- a share explained as a denominator effect (P2).

Describe warm-up and first-batch effects as protocol facts (P1). Do not repeat costs in takeaways or the conclusion.
*Supported by: P10, P5, P2, P1, P8 (index size/time table), P9 (small memory increase).*

**R8. Use calibrated, positively counted wording that keeps the minority identifiable.**
- Lead with the positive count ("faster in 46 of 50 cells", or P3's 111 of 139 graphs).
- Name the remaining cells in the same or the next sentence, or point to the table.
- Use "comparable" or "on par (0.9–1.1×)" with the measured range.
- Give absolute gaps for tiny losses (e.g., 0.5 µs per update).
- Avoid self-negating phrases about the method: "does not help", "vanishes", "only 1.1×".

*Supported by: P3, P7, P5, P2, P9, P8.*

**R9. Tables carry all numbers; the text summarises and names exceptions without editorial emphasis.**
- Do not add symbols that highlight losses beyond what correctness needs. Timeout or truncation marks are legitimate.
- Do not write a split "up to" headline that hides which competitor is faster (avoid the P10 pattern).
- Use one headline range per baseline.

*Supported by: P2, P3, P7, P10 (all show losing cells in tables, with brief text).*

**R10. Turn theoretical scope into named, numbered objects stated once in the method section.**
Use an Assumption, Observation or Condition, or a design-scope sentence such as "Certificates target deletions; insertions rely on two-seed locality". Add how often it holds in practice. Contrast the worst case with practice in one sentence, giving the concrete reasons.
*Supported by: P1 (Assumption 1, Observation 3), P3 (condition, 111/139), P6 (fully dynamic case), P9 (worst case vs practice).*

**R11. Conclusion: restate the contributions with scope folded into the claim; at most one forward-looking sentence on the main gap.**
- P8 restricts its headline to star insertions on large datasets.
- P7 restricts it to single edges or small batches.
- P3 restates its majority condition.
- Open problems appear as research directions, not as lists of losses.
- No paper in the corpus lists losing datasets in its conclusion.

*Supported by: P3, P7, P8, P1, P4, P9, P10.*

**R12. Present losses of your own ablation variants as evidence for the next component.**
When a basic variant is slower or weaker, that motivates the full method: ForestCFCM → SchurCFCM (P4), basic → improved maintenance and global → local search (P9), IMCENewClq → FastIMCENewClq (P6). This kind of loss is a positive argument and needs no hedging.
*Supported by: P4, P9, P6, P3.*

---


## Checklist before submission
- [ ] The abstract has no separate negative sentence. Scope appears as a qualifier of the positive claim.
- [ ] The introduction has at most one scope sentence, with a section pointer. The contribution list
      contains contributions only.
- [ ] Each negative result appears once, in the experiment that measures it, ordered as fact,
      mechanism, regime, bound.
- [ ] No "Where X does not help", "Limitations" or "Failure cases" heading inside the experiments. Use a
      regime title such as "When does X pay off?".
- [ ] One-off costs appear once, with a break-even count or an amortisation argument.
- [ ] Takeaways and the conclusion do not repeat the exceptions.
- [ ] The conclusion folds the scope into the main claim and has at most one sentence on the open
      problem.
- [ ] All losing cells are still in the tables and are named once in the text.
