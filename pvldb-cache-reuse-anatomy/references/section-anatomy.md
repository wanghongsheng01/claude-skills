# Section-by-section anatomy (rules with exemplar evidence)

Evidence keys: STS = STsCache PVLDB 18; CRY = Crystal PVLDB 14; SIE = Sieve PVLDB 13; PUR = Purview PVLDB 16 (industrial).
Each rule: **rule** — why — evidence. Check every rule as met / partial / gap with the manuscript location.

## 1. Title
- **`<Name>: <distinguishing property> <artifact type> for <domain/workload>`.** Each word maps to a claim and a section.
  CRY ("Unified … Cache Storage …"), STS (semantic cache + time-series + hybrid storage), SIE (middleware + scalable access control).
- **Pattern the title on the closest baseline so the delta is readable from the title** (STS vs its baseline's title).

## 2. Abstract (STS 8 sentences ≈178 words; SIE 7; CRY no numbers)
- S1 problem + scale threshold (SIE); S2 two-sided gap mapping onto the two baseline families (STS); S3 the idea;
  S4–S5 mechanisms, one sentence per cost term or bottleneck (SIE, STS); S6 evaluation objects; S7–S8 headline results,
  one sentence per baseline family with baselines named (STS).
- **Every abstract number must appear verbatim in the evaluation** (STS violates this once — do not).
- No disclaimers in the abstract beyond one scoping clause.

## 3. Introduction (≈1.3–1.4 pages)
- **Challenges → Opportunities → Introducing X** (CRY) or problem → named-system critique → 2–4 bolded challenges →
  mechanisms mapped back to challenges → results → contributions (STS).
- **Critique prior work by name and mechanism**, with numbered drawbacks (STS), and argue one shared bottleneck mechanism
  (SIE: query rewriting that appends predicates).
- **Derive the scale/regime claim arithmetically** from a concrete deployment with labelled conservative assumptions (SIE).
- **State scope restrictions once and argue they are exploited, not tolerated**; list deferred aspects with a one-line
  reason each (CRY). Do not re-disclaim in every paragraph.
- **Contributions:** 3–4 verb-led bullets, each with a § pointer (CRY); separate the conceptual contribution (formal model)
  from system contributions (STS). Quantified headline with § pointers is good practice (CRY), never a priority claim
  repeated three times (STS anti-pattern).
- A motivating figure is optional (STS has none) but a small conceptual example figure early helps (CRY Fig. 3).

## 4. Background / problem / model
- **Example first, then symbols, then an immediate worked example** (STS Q1–Q4 → Def. → Example; SIE running example;
  PUR Ex 2.1–2.5). Notation table when symbols exceed ≈8 (STS Table 1).
- **State the correctness precondition of the cache in the model** (PUR: determinism of the decision function) and the
  case that breaks it (PUR time predicates).
- **Anchor security semantics to an established criterion and show where it breaks** (SIE: sound/secure; set-difference
  counterexample), then reuse that constraint when configuring baselines.
- Related work may sit early (STS §2, SIE §2.2) when positioning needs the background; each group ends with the failure on
  a property of *your* scenario (SIE).

## 5. Design / method
- **Architecture figure first; modules ↔ subsections ↔ experiment subsections** (STS Fig. 5; CRY overview).
- **Naive design → "However" + flaw → refined design → numbered benefits** for each component (STS).
- **Cost model before algorithm**; formulate as a known problem and say exactly why the textbook version fails, then give
  complexity and admit lost guarantees (CRY knapsack; SIE read vs evaluation cost, NP-hardness + greedy credit).
- **Turn theorems into operational tests** (SIE θ > C) and validate every adaptive switch with a crossover experiment
  (SIE Figs. 3–4).
- **Justify each design decision with a small measurement inside the design section** (CRY Fig. 5) and forward-reference
  the experiment that justifies each constant (STS).
- **Invalidation/revocation in one place:** what is flushed, when, by which check; update-channel guarantees; adversarial
  interleaving examples; crash ordering (PUR §4.3, §5.1–5.3). A permission-aware cache must also *prove* or test it
  (SIE/PUR leave this to prose — a gap to exceed, not copy).
- Hot-path complexity with and without the index (STS); integration cost in LOC (CRY).

## 6. Experimental evaluation (24–33 % of the body)
- Setup: exact hardware, cloud tier, software versions (commit hash), cache budget as % of data for every system (CRY),
  repetition count and aggregation rule (STS).
- **Baselines:** at least one outside system run as released; unavailable ones reimplemented on the same code base
  "strictly following [ref]"; a resource-matched configuration if you add resources (STS dual server); if a baseline cannot run
  your benchmark, say why and give it an equal-resource tailored workload (STS).
- **Two engines/hosts** to support generality (CRY, SIE).
- **Workloads that each stress one property** (CRY long-term, bursts, shift, standard benchmark); a larger synthetic
  workload to push scale beyond the real data, with the reason (SIE).
- **Metrics:** measured latency/throughput first; hit ratio split by reuse source (STS full/partial); online vs background
  cost separately (CRY); setup/preprocessing overhead with an absolute anchor (SIE); distributions, not only means (CRY violins).
- **Mechanistic explanation of every win** (2–3 reasons tied to design sections, STS) and of baseline anomalies by plan
  analysis (SIE).
- **Trade-off sweep:** jointly vary the property that drives reuse and the one that drives overhead; state losing regimes in
  the same paragraph as the wins (CRY cold cache, >100 % cache; STS −6–15 % throughput for −75 % memory).
- **Ablate every claimed component, including the central idea** (CRY and STS fail here — exceed them).
- Robustness/adversarial workload for the pathology the design targets (STS cache penetration); policy churn and revocation
  storms for a permission cache (PUR fails here — exceed it).
- Timeout and partial-completion conventions in tables (SIE).

## 7. Figures and tables
- Results are mostly figures (STS 16, CRY 10 result figures); tables carry setups or compact matrices (1–4 tables).
- Claim-first captions help skimming (STS uses descriptive captions — weaker).
- Every exhibit is cited and earns a headline sentence (SIE Table 3 is never cited — do not).

## 8. Related work
- 3–5 groups; each group: what it does → why it fails on the property your problem requires; reuse your own measurement to
  refute a competitor design (CRY vs Dar et al.).

## 9. Conclusion
- 3–5 sentences: object, mechanisms, headline number repeated (PUR, STS); optionally one limitation sentence. No new claims,
  no list of failures.

## 10. References
- 34–80 entries; DB-venue core (PVLDB/SIGMOD/ICDE) is the backbone (CRY 25/52); product/web references only where the
  product itself is discussed. Verify volume/issue against the PDF (SIE's PDF prints issue 11).
