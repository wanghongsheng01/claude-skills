# Exemplar deconstruction: Sieve (PVLDB 13, 2020)

Source read in full: `official PDF p2424-pappachan.pdf` (14 pages) and its `pdftotext -layout` text; page images of pp. 3, 10, 11, 12 were rendered to check figure axes and layout. Page numbers below are **PDF page numbers (1-14)**; the printed proceedings page is PDF page + 2423 (PDF p.1 = 2424, p.14 = 2437). Everything is paraphrased; quoted fragments are short term-level phrases only.

---

## 1. Bibliographic facts

| Item | Value (evidence) |
|---|---|
| Title (as printed) | "Sieve: A Middleware Approach to Scalable Access Control for Database Management Systems" (p.1) |
| Authors / affiliation types | Primal Pappachan, Roberto Yus, Sharad Mehrotra (University of California, Irvine), Johann-Christoph Freytag (Humboldt-Universität zu Berlin). 4 authors, 2 institutions, **all academia**, no industry author (p.1). |
| Volume / issue / pages as printed in the PDF | Reference-format box: PVLDB 13(11): 2424-2437, 2020; copyright box: "Vol. 13, No. 11", ISSN 2150-8097 (p.1). **Discrepancy:** the task metadata says 13(12). The PDF itself prints issue 11; I did not resolve this online. Use the DOI as the stable identifier. |
| DOI | 10.14778/3407790.3407835 (printed twice on p.1) |
| Total pages | 14 (pdfinfo) |
| Page where references start | p.13 (printed 2436), "8. REFERENCES"; they spill 4 entries onto p.14 (2437) |
| Body pages | 12 (p.1-p.12: abstract, Sections 1-7 and the Acknowledgement all end on p.12); references take ~1.1 pages |
| Reference count | **34** numbered entries [1]-[34] (counted) |
| Figures | **6** (Fig. 1 p.3; Fig. 2 p.10; Figs. 3-4 p.11; Figs. 5-6 p.12) |
| Tables | **4** (Table 1 p.4 notation; Tables 2-3 p.10; Table 4 p.11) |
| Algorithms | **1** (Algorithm 1 "Selection of guards", p.8, 14 numbered lines) |
| Definitions / theorems / lemmas | 0 numbered definitions (models defined in prose under bold run-in headers, p.4-5); **2 theorems** (Thm 1 p.6 with proof, Thm 2 p.7 with proof by contradiction); 0 lemmas; 1 un-numbered NP-hardness claim with reduction sketch (p.7) |
| Equations | 11 numbered (Eq. 1-11, p.6-7) + 2 un-numbered displayed case definitions (eval of policy expression and of object conditions, p.5) = 13 displayed; approx 6 more inline cost formulas (benefit, utility, read cost p.7; cost(Guard&Δ), cost(Guard&Inlining) p.8-9; cost(IndexQuery), cost(IndexGuards) p.9) |
| SQL listings | 4 displayed, un-numbered: running-example query (p.3), basic WITH-clause rewrite (p.8), FORCE INDEX rewrite (p.8), full Sieve rewrite of the running example (p.9); plus inline SQL-like policy tuples (p.4-5) |
| Footnotes | **7** (fn1 notice vs consent p.1; fn2 TIPPERS URL p.2; fn3 histogram cardinality p.6; fn4 inclusion-exclusion p.7; fn5 code URL p.8; fn6 MySQL hints URL p.8; fn7 PostgreSQL EXPLAIN URL p.8) |
| Artifact / code availability | Footnote 5 (p.8): implementation with connectors for MySQL and PostgreSQL at github.com/primalpop/sieve. Extended version on arXiv [30] (2004.07498) holds dynamic guard generation, persistence, full Δ operator, schemas, sample policies, more results (p.2). Data: TIPPERS data collected with special university permission for research, not stated as released (p.10). No reproducibility badge text. |
| Funding | DARPA agreement FA8750-16-2-0021; NSF 2032525, 1545071, 1527536 (p.12) |

---

## 2. Title anatomy

Components: **[System name] : [architecture class] + [quality attribute] + [problem] + [target platform]**.

- "Sieve" - a one-word, metaphorical system name; the metaphor (filtering out what need not be checked) matches the core mechanism of discarding policies and tuples early (p.5-6). Memorable and searchable.
- "A Middleware Approach" - declares the architectural stance up front; this pre-empts the reviewer question "do you modify the DBMS?" and is defended in the intro as enabling DBMS independence (p.2).
- "Scalable" - names the axis of evaluation (number of policies), which is exactly what Exps. 4-5 sweep (p.12).
- "Access Control" - the problem class; fine-grained is implied, made explicit in the abstract's first sentence.
- "for Database Management Systems" - target platform; signals a DB-venue (not security-venue) contribution.

Why it works: every noun phrase maps to a section or experiment (middleware = Sec. 5; scalable = Exp. 5; DBMSs = MySQL + PostgreSQL). It promises no specific number and no novelty adjective beyond "scalable".

---

## 3. Abstract (7 sentences, p.1)

| # | Content (paraphrase) | Rhetorical function | Concrete object / number carried |
|---|---|---|---|
| S1 | Existing FGAC enforcement in DBMSs fails to scale once policies number in the thousands. | Problem + gap in one sentence | "thousands" of policies (the scale regime) |
| S2 | The paper identifies such a use case in smart spaces, where laws like GDPR and CCPA may require users to control who sees their data and why. | Motivation / legitimacy of the regime | GDPR, CCPA; "who" and "for what purposes" (foreshadows querier + purpose conditions) |
| S3 | Sieve is presented: a layered FGAC implementation over existing DBMSs that leverages built-in features to scale. | Solution statement + architecture | Named features: UDFs, index usage hints, query explain |
| S4 | For a given query, Sieve uses query context to prune the policies to check. | Technique 1 | Query context (later QM: querier, purpose) |
| S5 | It also builds guarded expressions that group policies (saving evaluation cost) and exploit indices (saving read cost). | Technique 2 | "guarded expressions"; two cost terms (evaluation vs read) |
| S6 | Experiments show existing DBMSs using Sieve cut query-time policy evaluation cost substantially. | Result claim | **No number**; qualitative "significantly" |
| S7 | Hence DBMSs can support real-time access control for applications such as smart environments. | Impact / broader claim | "real-time" (not quantified here; queries ~0.4-0.5 s in Table 4, p.11) |

Observations: no dataset names, no speedup factor, no baseline name in the abstract. The two techniques map 1:1 onto the two cost terms of the later cost model (Eq. 2-3, p.6). The abstract's feature list (UDFs, hints, explain) is precisely what Sec. 5 uses (p.8-9), so the abstract doubles as an implementation map.

---

## 4. Introduction (Section 1, p.1-2)

| Para | Page | Function | Key moves |
|---|---|---|---|
| P1 "Organizations today capture..." | p.1 L to R col | Context: mass personal-data capture, privacy implications [6,7,33]; regulations [1-3] require transparency, minimisation, retention, and choice/consent [21] (fn1 contrasts notice vs consent) | Broad context -> legal pressure |
| P2 "While such coarse level policies..." | p.1 R | Shift: smart spaces will need finer-grained user control; lists open challenges (policy languages [28]); narrows to the one addressed: scaling enforcement when the policy set dominates cost; cites a survey [17] naming this an open challenge | Problem narrowing; external validation that the problem is open |
| P3 "In the envisioned system..." | p.1 R | Points to the smart-campus case study (Sec. 2.1), asserts hundreds to thousands of policies for a simple analytic query, states this is beyond today's DBMSs, and claims generality beyond IoT | Problem made concrete + generality hedge |
| P4 "Today, DBMSs implement FGAC by one of two mechanisms" | p.1 R -> p.2 L | State of practice: policy-as-schema (authorization views [31]) vs policy-as-data [5,9,13,15]; both reduce to query rewriting [32] appending predicates to WHERE; cost explodes with many policies; ends by labelling scalable policy-driven execution a "novel challenge" | Gap: the shared mechanism (rewrite) is the bottleneck |
| P5 "In this paper we propose Sieve..." | p.2 L | Idea: general-purpose middleware exploiting index support, UDFs, hints; justifies middleware (DBMS independence, IoT systems differ [18], easier exploration, precedent [14]) | Idea + architecture justification |
| P6 "Sieve incorporates two distinct strategies..." | p.2 L | Technique 1: guarded expressions chosen to use the best existing indexes (inspired by predicate factorisation [11]); Technique 2: filtering policies per tuple using tuple context and query metadata (querier, purpose) via operator Δ implemented as a UDF | Two-pronged mechanism, each tied to a prior idea |
| P7 "Sieve combines the above two strategies..." | p.2 L -> R | Adaptive choice by cost model; evaluation preview: real WiFi data from the UCI building (>40K devices), synthetic policies, synthetic mall dataset, two DBMSs (MySQL, PostgreSQL) | Results preview (qualitative only) |
| P8 "Outline of the paper." | p.2 R | One sentence per section 2-7 | Roadmap |
| P9 "Extended version." | p.2 R | Lists what was moved to the arXiv version [30] | Scope/space disclosure |

Move sequence: context -> legal driver -> problem narrowing (survey-backed) -> concrete scale claim (forward ref to case study) -> state of practice and why it fails -> idea -> mechanism (two strategies) -> adaptivity + evaluation preview -> roadmap -> extended-version disclosure.

**Contribution list: none.** There is no bulleted or enumerated contributions list; contributions are embedded in P5-P7 as prose ("we propose", "incorporates two distinct strategies", "combines ... adaptively chooses", "we evaluate"). Verbs: propose, exploit, define, present (implementation as UDF), combine, evaluate. Objects: middleware; guarded expressions; policy evaluation operator Δ; cost-model-driven strategy selection; evaluation on real + synthetic data over two DBMSs. **No quantitative headline** (no speedup factor) appears anywhere in the intro.

First figure/table: none in the intro. The first figure is Fig. 1 on p.3 (Sec. 2.1), an ER diagram of campus entities annotated with population sizes, used to derive the policy-count estimate. The first table is Table 1 (notation) on p.4.

Inconsistency to note: the intro says over 40K unique devices (p.2), while Sec. 6.1 reports 36K / 36,436 devices (p.10).

---

## 5. Remaining sections in order

### Section 2 Problem Setting (p.2-3)
Purpose: ground the scale claim in a real deployment, then review prior approaches against that scale. One framing paragraph says the case study will be used to show prior strategies fall short (p.2).

**2.1 Smart Campus Case Study (p.2-3).**
- Para 1: smart campus services (queue monitoring, occupancy, attendance [20]); privacy challenges [29]; authority claim: the authors have built and operated TIPPERS [26] for 4 years, in daily use (fn2) (p.2).
- Para 2: Fig. 1 entities with counts; running-example analytic query (professor correlates attendance with grades), displayed as SQL (p.3).
- Para 3: back-of-envelope policy count: privacy profiles from Lin et al. [24] (20% default, 18% advanced, rest split 2/3-1/3), applied to a 200-student class -> 120 default + 80 advanced users -> 560 policies, rising to 880 or 1.2K under slightly less conservative assumptions (p.3).
- Para 4: over a year of classes -> 3.3K to 7.2K policies for one query; explicitly flags conservative choices (one data type, two conditions per policy, group-level policies) (p.3).
Craft: the "thousands" claim from the abstract is derived arithmetically from cited preference distributions, with each assumption labelled conservative. (Minor slip: semester vs quarter units mixed, p.3.)

**2.2 Related Work (p.3)** - see Section 8 below. Placed early, inside the problem setting, so that the gap is argued before the model.

### Section 3 Sieve Approach to FGAC (p.3-6)
Purpose: formal model (data, query, policy), access-control semantics, and an overview of the approach. Opens with a 3-sentence roadmap (p.3). Table 1 (notation, ~20 symbols) is placed at the top of p.4 "for perusal".

**3.1 Modeling Policy Driven Data Processing (p.4-5).** Bold run-in headers, no numbered definitions:
- *Data Model* (p.4): database D = relations, tuples, indexes, users; hierarchical groups with group(u); every tuple has an owner (shared ownership allowed). Assumption stated inline.
- *Query Model* (p.4): SELECT-FROM-WHERE queries with metadata QM containing querier and purpose; instantiated immediately on the running example (querier = Prof. Smith, purpose = Analytics).
- *Access Control Policy Model* (p.4): policy = triple of Object Conditions (conjunction of attribute-operator-value predicates; values may be constants or derived via expensive UDF/subquery), Querier Conditions (inspired by Purpose-Based Access Control [9]; at least querier and purpose), Action. Scoping sentences placed right where the construct is introduced: focuses on constant-valued object conditions; default action deny, so explicit actions are allow only (p.4).
- Two sample policies right after the model: John allows Prof. Smith during class time at AP 1200 for attendance; a derived-value variant ("only when with Prof. Smith") written as a subquery (p.4-5).
- Deny policies handled by rewriting into allow policies with narrowed scope; example given; then explicitly restricts discussion to allow policies (p.5).
- *Access Control Semantics* (p.5): the accessible tuple set is the subset satisfying the policy expression E(P) (a DNF over object conditions); two displayed case definitions for eval. **Guarantee argued by citation**: the semantics is said to satisfy the sound and secure properties of the correctness criterion of Wang et al. [34] (p.5); opt-out by default. Then a correctness argument about operator ordering: policies must be evaluated before aggregation/projection and before non-monotonic operators; a worked set-difference (MINUS) counterexample shows why evaluating afterwards gives wrong answers (p.5). This later justifies why UDF baselines cannot be pushed late (p.11).

Formalism pattern: running example first (Sec. 2.1), then symbols, then the example re-instantiated in the symbols, then scoping restrictions, then semantics.

**3.2 Overview of Sieve Approach (p.5-6).**
- Para 1: two cost drivers (number of complex policies, number of tuples) -> two building blocks (p.5).
- Bullet "Reducing Number of Policies": filter by query metadata to P_QM (formal membership condition given), then further by tuple attributes such as owner (p.5).
- Bullet "Reducing Number of Tuples": rewrite E(P) as guarded policy expression G(P) = disjunction of guarded expressions, each a guard predicate AND a policy partition; partitions are disjoint and cover P; guard properties: simple indexed predicate, and implied by every policy in its partition (p.5). These two properties are the (implicit) basis for equivalence of G(P) and E(P); the paper never states an explicit equivalence theorem.
- Example: John's and Mary's policies share wifiAP = 1200, which becomes a guard (p.5).
- Adaptive pipeline: filter by QM, replace each relation by a WITH-projection filtered by G(P); generation can be offline, on policy change, or at query time (claimed efficient enough, forward-referenced to Sec. 6) (p.6).
- Δ operator introduced as an alternative to evaluating the full partition (p.6).
- Ends with an explicit two-item "main challenges" list mapped to Sec. 4 and Sec. 5 (p.6).

### Section 4 Creating Guarded Expressions (p.6-8)
Purpose: optimisation problem and algorithm.
- Opening: objective Eq. 1 (minimise sum of guarded-expression costs); cost model Eq. 2 (alpha x partition size x per-policy eval cost, with stated assumption of short-circuit disjunction) and Eq. 3 (guard cardinality x (read cost + eval cost)); cardinality from DBMS histograms (fn3); constants determined experimentally from sample policies/tuples (p.6). Two-step plan: generate candidate guards, then select (p.6).
- **4.1 Generating Candidate Guards (p.6-7).** Any constant-valued object condition on an indexed attribute is a candidate; every policy is guaranteed one (owner or profile) (p.6). Range merging to improve grouping, motivated by a numeric example (3-10 and 4-15 -> 3-15) (p.6). **Theorem 1** (merging only beneficial if ranges overlap), proof by cost comparison Eqs. 4-9, yielding a closed-form test theta > C (overlap/union cardinality ratio vs a constant) (p.6-7). Transitive merges motivated by a third range (12-18); **Theorem 2** (transitive merge not beneficial when outer ranges are disjoint), proof by contradiction via Eqs. 10-11 (p.7). Then a 5-step procedure (sort by left endpoint, greedy pairwise/transitive merge) in prose (p.7).
- **4.2 Selecting Guards To Minimize Cost (p.7-8).** Problem: choose guards covering each policy exactly once at minimum cost; NP-hardness via reduction from weighted Set Cover, given as a one-paragraph prose mapping (elements -> policies, sets -> candidate guards, weight -> read cost) (p.7). Heuristic: utility = benefit / read cost, benefit defined as eval cost x partition size x tuples filtered out; credited as similar to Hellerstein's expensive-predicate ranking [19] (p.7). **Algorithm 1** (p.8): priority queue by utility, extract max, remove covered policies from other candidates, recompute utility, reinsert. No complexity bound and no approximation ratio are given; the text says the result "minimizes" cost, which overstates a greedy heuristic (p.8).

### Section 5 Implementing Sieve (p.8-9)
Purpose: turn the abstraction into SQL that existing optimisers execute well. Opens with a roadmap (rewrite, two optimisations, sample) and the code footnote (p.8).
- **5.1 Query Rewrite with Guarded Expressions (p.8):** each relation replaced via a WITH clause (so the policy check runs once even for self-joins); optimisers may pick bad plans, so platform-dependent connectors use extensibility hooks; MySQL-style FORCE INDEX rewrite as a UNION of per-guard index scans; PostgreSQL lacks hints, so the same rewrite relies on the optimiser (assumption stated) (p.8).
- **5.2 Policy Evaluation Operator (p.8-9):** names two strategies, Guard&Inlining vs Guard&Δ; Δ as a per-relation UDF that fetches only policies relevant to QM and tuple context, then evaluates; concrete invocation example with parameter-by-parameter explanation (p.8). Cost model: Guard&Δ = UDF invocation + execution, measured and averaged, constant across guards; Guard&Inlining = alpha x partition size x eval cost; choose per guard; empirical threshold partition size > 120 (forward-ref to Sec. 6) (p.9).
- **5.3 Exploiting Selective Query Predicates (p.9):** IndexGuards vs IndexQuery; IndexQuery cost from the DBMS EXPLAIN selectivity (infinite if no index); IndexGuards cost = sum of guard cardinalities x read cost, explicitly called an upper bound (ignores index merge); decided per query at execution time (p.9).
- **5.4 Sieve generated Query Rewrite (p.9):** revisits the Sec. 2.1 running query and shows the full rewrite with FORCE INDEX on guards and one partition replaced by a delta(...) call, then explains which strategy choices produced it (p.9). Closes the running-example loop.

Claim scoping in Secs. 3-5: assumptions are stated locally where each construct appears (constant values p.4; allow-only p.4-5; short-circuit DNF p.6; experimentally fitted constants p.6; offline/online generation p.6; hint availability p.8; upper-bound cost p.9), not collected in a separate assumptions section.

### Section 6 Experimental Evaluation (p.9-12) - see Section 6 below.

### Section 7 Conclusion + Acknowledgement (p.12) - see Section 10 below.

---

## 6. Experiments in depth (Sec. 6, p.9-12)

**Experiment goals (no formal RQs).** A roadmap paragraph at the start of 6.2 lists five experiments (p.10): (1) cost and quality of guarded-expression generation; (2) validation of design choices (2.1 inlining vs Δ; 2.2 query index vs guard index); (3) comparison with baselines on MySQL; (4) behaviour on PostgreSQL (no index hints); (5) stress/scalability with very many policies. Exps. 1-4 use TIPPERS, Exp. 5 uses Mall (p.10).

**Hardware/software (p.10).** One machine in a cluster: CentOS 7.6, Intel Xeon E5-4640 at ~2.8 GHz, 20 MB cache, 132 GB shared memory. MySQL 8.0.3 with InnoDB, buffer pool 4 GB (chosen because it supports index hints); PostgreSQL 13.0, shared_buffers 4 GB. No disk type, no core count used, no concurrency settings.

**Datasets / workloads and scale.**
- TIPPERS (real): 64 WiFi APs, CS building at UCI, 3 months; 3.9M events, 36K devices (passers-by included) (p.9). Devices classified into profiles by connectivity heuristics: 31,796 visitors, 1,029 staff, 388 faculty, 1,795 undergrad, 1,428 grad out of 36,436 (p.10); 56 affinity groups averaging 108 devices (p.10).
- TIPPERS policies (synthetic): profile-based generator motivated by the authors' town halls/surveys and [22,24]; unconcerned users get admin defaults, advanced users ~40 policies each; total 869,470 policies, 472 defined per individual on average, 188 per individual as querier (p.10).
- Mall (synthetic): generated with the SmartBench IoT data generator [18] over a mall floorplan; 1.7M events, 2,651 devices (p.9); 19,364 policies for 35 shops, 551 per shop on average; six shop types, regular/irregular customers (p.10).
- Queries: three templates from SmartBench [18]: Q1 devices at a list of locations over time; Q2 given MACs over time; Q3 count of a group/profile at a location; each at low/medium/high selectivity (p.9-10). Exp. 3: posed by five queriers from four profiles (p.11). Exps. 4-5 use SELECT ALL queries and cumulative policy sets (p.12).

**Baselines (Exp. 3, p.11), all author-implemented rewrite strategies on the same DBMS and policies:**
| Baseline | What it is | Fairness / disclosure |
|---|---|---|
| Baseline_P | Append querier's policies to the WHERE clause (classic query-modification rewrite) | Represents state of practice from Secs. 1-2; no tuning beyond buffer size disclosed |
| Baseline_I | One forced index scan per policy, combined with UNION | Described as "careful rewriting"; it is the strongest baseline and is reused as the MySQL reference in Exp. 4 |
| Baseline_U | Like Baseline_P but evaluates policies through a UDF taking all tuple attributes | Motivated as a sensible low-cardinality optimisation; authors explain UDFs cannot be deferred past non-monotonic operators for correctness (ties back to p.5, cites [19]) |
In Exp. 4 the PostgreSQL baseline is Baseline_P(P) (p.12); in Exp. 5 Fig. 6 shows a series labelled only "Baseline" (by the "same process as Exp. 4", presumably Baseline_P on PostgreSQL, not stated explicitly) (p.12). **No research-system baseline** (e.g., Colombo-Ferrari enforcement, VPD, view-based) is run; the view-based approach is dismissed analytically in 2.2 (p.3).

**Metrics reported (every one):**
1. Guarded-expression generation time per querier (ms) (Fig. 2, p.10; 150 ms for 160 policies quoted).
2. Policies affecting a user, |P_u| (min/avg/max/SD) (Table 2).
3. Guards per user |G| (Table 2).
4. Policies per partition |P_Gi| (Table 2).
5. Guard cardinality rho(G_i) as % of table (Table 2).
6. "Savings": fraction of policy evaluations avoided by guards (Table 2; ~0.99, on an unspecified smaller sample) (p.11).
7. Total guard cardinality rho(G) by low/high |G| (Table 3).
8. Policy evaluation time (s) as a function of partition size (Fig. 3) and of query cardinality (Fig. 4).
9. Query execution time (ms), warm, with TO (timeout 30 s) and t+ (partial completion) markers (Table 4, Figs. 5-6).
10. Speedup factor of Sieve over baseline (stated in text only: 1.6x at 100 to 5.6x at 1,200 policies, p.12).

**Per figure/table results:**
| Exhibit | Varied | Measured | Headline the text draws |
|---|---|---|---|
| Fig. 2 (p.10) | # policies per querier (~125-275; costs averaged in groups of 50 users) | generation time (ms) | Generation grows linearly with policies, occasional dips due to selectivity/overlap; overhead minimal (~150 ms at 160 policies) |
| Table 2 (p.10) | across users | 5 guard statistics + Savings | ~187 policies per user, ~31 guards, mean partition 7, low guard cardinality; guards remove ~99% of policy checks |
| Table 3 (p.10) | |G| low/high x rho(G) low/high | total cardinality | **Not referenced or discussed in the text** |
| Fig. 3 (p.11) | policies in a guard partition (0-200) | evaluation time (s) | Δ's UDF overhead is amortised around 120 policies; beyond that Δ wins (visual crossover looks closer to ~140) |
| Fig. 4 (p.11) | query cardinality (0-0.23), averaged over 3 guard cardinalities | evaluation time (s) | IndexQuery better at low cardinality; IndexGuards better above ~0.07 |
| Table 4 (p.11) | Q1/Q2/Q3 x low/mid/high selectivity x 4 methods | mean warm execution time (ms) | Baseline_P/U degrade with query cardinality (TO cases); Sieve and Baseline_I flat; Sieve fastest in all 9 cells (407-523 ms vs Baseline_I 881-3,543 ms) |
| Fig. 5 (p.12) | # policies 75-300 (10 cumulative sets, 5 queriers, 3 random orders) | execution time (ms) on MySQL and PostgreSQL | Sieve beats the PostgreSQL baseline, with larger speedup than on MySQL, largest at most policies; explained by PostgreSQL bitmap OR of guard index scans |
| Fig. 6 (p.12) | # policies 100-1,200 on Mall (5 shops with >=1,200 policies) | execution time (ms) | Speedup grows linearly from 1.6x to 5.6x; generality across datasets |

**Negative results / trade-offs / losing regimes.**
- Design-internal losses, reported as cost-model thresholds rather than as weaknesses: Guard&Δ loses below ~120 policies per partition (p.9, p.11); IndexGuards loses at query cardinality below ~0.07 (p.11).
- Guards with high cardinality (up to 24%) are not forced through an index (p.11).
- Fig. 2 non-monotone dips are explained, not hidden (p.10).
- Baseline anomalies explained by plan analysis: Baseline_P Q3 improves via nested-loop index join; Baseline_I Q3 degrades because the optimiser joins first (p.11-12).
- **Sieve never loses end-to-end** in any reported cell or curve; no regime where Sieve is slower than a baseline is shown. Guard-generation time is reported separately and it is not stated whether it is included in Table 4 timings.

**Ablations.** Exp. 2.1 and 2.2 are component ablations of the two adaptive choices (p.11). There is no ablation removing guards entirely vs only Δ in the end-to-end setting, and no ablation of range merging (Theorems 1-2) or of the greedy heuristic vs alternatives.

**Sensitivity / scalability sweeps.** Query selectivity (3 levels, Table 4); partition size (Fig. 3); query cardinality (Fig. 4); number of policies 75-300 (Fig. 5) and 100-1,200 (Fig. 6); DBMS (MySQL vs PostgreSQL). No sweep over data size (number of tuples), number of concurrent queriers, or policy update rate.

**Statistical treatment.** Exp. 3: each query run 5 times, averaged, warm cache, 30 s timeout with explicit TO / t+ conventions (p.11). Exp. 4: 5 queriers x 3 random policy orderings, averaged (p.12). Exp. 1: averages over groups of 50 users (p.10). Table 2 reports SD. **No error bars, confidence intervals or variance** on any timing figure or table.

---

## 7. Figure and table inventory

| # | Page | Type | Purpose | What a reviewer can recover | Caption style |
|---|---|---|---|---|---|
| Fig. 1 | 3 | ER-style diagram with population counts | Ground the policy-count estimate in a campus model | Entity hierarchy and cardinalities used in the 560-7.2K estimate | Descriptive ("Entities and relationships in a Smart Campus Scenario.") |
| Table 1 | 4 | Notation table (~20 rows) | Symbol reference | All symbols of Secs. 3-5 | Descriptive |
| Fig. 2 | 10 | Line plot (wrapped in text, small) | Guard generation overhead | ms vs #policies; linear trend | Descriptive, 3 words |
| Table 2 | 10 | Summary stats (min/avg/max/SD) | Guard quality | Policies per user, guards, partition sizes, cardinality, savings | Descriptive |
| Table 3 | 10 | 2x2 matrix | Total guard cardinality by |G| and rho | Four numbers; meaning unexplained in text | Descriptive; never cited |
| Fig. 3 | 11 | Two-line crossover plot | Justify Δ threshold | Crossover point between strategies | Descriptive ("Inlining vs. Δ.") |
| Fig. 4 | 11 | Two-line crossover plot | Justify index choice | Crossover at ~0.07 query cardinality | Descriptive ("Index choice.") |
| Table 4 | 11 | Results matrix 9 rows x 4 methods, ms | Main end-to-end comparison | Absolute times, timeouts, partial completions; speedups computable by reader | Descriptive (includes unit) |
| Fig. 5 | 12 | Four-line plot | Cross-DBMS generality | Times for Sieve/baselines on MySQL and PostgreSQL vs #policies | Descriptive |
| Fig. 6 | 12 | Two-line plot | Scalability to 1,200 policies | Diverging baseline vs flat Sieve; speedup 1.6x-5.6x | Descriptive ("Scalability comparison.") |

All captions are short and descriptive; none is claim-first. Headlines live only in the body text. Two of six figures are design-validation crossover plots, which is a compact way to justify cost-model thresholds.

---

## 8. Related work

- **Position:** early, Section 2.2 (p.3), inside "Problem Setting", right after the case study and before the model. ~4 paragraphs, ~0.6 page. No separate related-work section at the end.
- **Groups and refs:**
  1. FGAC in DBMSs, view-based vs policy-as-data (survey [8]; views [31], Oracle VPD [25]; Hippocratic DBs [5] and follow-ups [23,4]) - 6 refs; argued infeasible at scale: views need per-querier/purpose materialisation, policy-as-data yields huge DNF WHERE clauses (p.3).
  2. Pre-processing / tuple augmentation at ingestion ([10]; partial pre-processing [12,14]) - 3 refs; argued costly at high ingest rates, wasted on unqueried tuples, cannot handle query-context-dependent or dynamic policies; recent work still defers tuple-level FGAC to query-time rewriting "as is the case in our paper" (p.3).
  3. Access control for IoT / smart spaces (streaming punctuations [27]; MQTT architecture [16]) - 2 refs; argued not designed for many policies at run time or analytical queries, and [27] needs DBMS modification (p.3).
- Intro additionally cites background/precedent: [1-3,6,7,17,21,28,33] (context), [9,13,15,32] (rewrite mechanisms), [11] (predicate factorisation inspiration), [14,18] (middleware precedent).
- **Positioning sentence pattern:** "[Approach class] does X; this reduces cost Y, but in our setting (many fine-grained, dynamic, context-dependent policies) it fails because Z." Each group closes with a limitation tied to a property of the motivating scenario, not to a generic weakness. Credit is given where Sieve borrows (predicate factorisation [11], expensive-predicate ranking [19], Pur-BAC [9], correctness criterion [34]).

---

## 9. References (34 total, counted)

**By type:**
| Type | Count | Entries |
|---|---|---|
| DB conferences (VLDB/PVLDB, SIGMOD, ICDE, EDBT) | 9 | [4] ICDE, [5] VLDB, [7] EDBT, [11] SIGMOD, [15] ICDE, [18] PVLDB, [23] VLDB, [31] SIGMOD, [34] VLDB |
| DB journals / monographs | 6 | [8] FnT Databases, [10] VLDB Journal (printed as "PVLDB"), [12] TKDE, [13] TKDE, [14] Data Sci. Eng., [19] TODS |
| Security / privacy venues | 7 | [6] PoPETs, [9] SACMAT, [16] SACMAT, [17] Cybersecurity (journal), [24] SOUPS, [27] CODASPY, [28] CODASPY |
| Pervasive / ubiquitous / distributed systems | 4 | [21] UbiComp, [22] PerCom, [26] PerCom Workshops, [29] ICDCS Workshops |
| Other journal / conf | 2 | [33] J. Network and Computer Applications, [20] Learning Analytics & Knowledge |
| Web pages (legislation) | 3 | [1] CCPA, [2] CalOPPA, [3] GDPR |
| Book / product manual | 1 | [25] Oracle 11g reference |
| Preprint (own extended version) | 1 | [30] arXiv |
| Classic 1974 conference paper | 1 | [32] Stonebraker and Wong |

Journals overall: 8 ([8,10,12,13,14,17,19,33]).

**By year:** <=2010: 12 ([4,5,9,10,11,19,21,23,25,31,32,34]); 2011-2020: 19; undated web pages accessed 2020: 3; 2021+: 0 (paper is 2020).

**Flagship DB venue counts:** printed as PVLDB: 5 ([5,10,18,23,34]; of these [5,23,34] are actually VLDB conference proceedings pre-PVLDB and [10] is the VLDB Journal, so only [18] is a true PVLDB article); SIGMOD: 2 ([11,31]); ICDE: 2 ([4,15]). Self-citations (any author): 5 ([18,26,28,29,30]). One author group (Colombo and Ferrari) supplies 6 refs ([12]-[17]).

---

## 10. Limitations / discussion / conclusion

- **No dedicated limitations or discussion section.** Conclusion is 2 paragraphs (~0.4 column, p.12), followed by Acknowledgement.
- Conclusion para 1 restates the approach (two optimisations), the middleware design on two DBMSs, and the evaluation on real + synthetic data; claims Sieve significantly outperforms rewrite-based strategies, speedup grows with policies, and query time stays low "even for thousands of policies per query" (p.12). No numbers repeated.
- Conclusion para 2 = future work: tighter optimiser integration; combining insertion-time pre-processing with query-time checking; co-optimising query and policy workloads (p.12). These implicitly concede the middleware limitation (cannot steer the optimiser fully) and the dynamic-policy cost.
- **Where honest trade-offs actually live:** scattered at point of use - constant-only object conditions (p.4); allow-only model with deny translation (p.4-5); ordering constraints for correctness with non-monotonic operators (p.5); experimentally fitted cost constants (p.6); NP-hardness forcing a heuristic (p.7); PostgreSQL lacks hints so Sieve depends on its optimiser (p.8); IndexGuards cost is an upper bound (p.9); thresholds where each sub-strategy loses (p.9, p.11); details deferred to the extended version (p.2).
- Not discussed: correctness testing of rewritten queries, policy-update cost at query time, data-size scaling, concurrency, security of the middleware itself (bypass), synthetic-policy realism threats.

---

## 11. Transferable rules and anti-patterns

### DO (transferable rules)
1. DO derive the scale regime (e.g., "thousands of policies per query") from a concrete deployment with labelled conservative assumptions: because it turns an adjective into an arithmetic claim reviewers can check (evidence: Sec. 2.1, p.3; 560 -> 3.3K-7.2K).
2. DO establish operational credibility of the motivating setting (years of deployment, daily use): because it pre-empts "toy problem" objections (evidence: p.2, TIPPERS 4 years, fn2).
3. DO state the problem and gap in the first abstract sentence with the scale threshold: because it fixes the evaluation axis from line one (evidence: abstract S1, p.1).
4. DO make each abstract technique sentence correspond to one cost term of your later model: because it lets the reader map claims to equations (evidence: S4-S5 vs Eq. 2-3, p.1/p.6).
5. DO name the DBMS features you exploit (UDFs, hints, EXPLAIN) in the abstract when the contribution is a middleware/rewrite layer: because it signals deployability without engine changes (evidence: abstract S3; Sec. 5, p.8-9).
6. DO justify the architectural choice (middleware vs in-engine) explicitly in the intro with portability and exploration arguments plus precedent: because reviewers will ask why not modify the optimiser (evidence: p.2, refs [14,18]).
7. DO argue that prior approaches share a single bottleneck mechanism (query rewriting appending predicates): because a mechanism-level gap is stronger than a list of weaknesses (evidence: p.1-2, p.3).
8. DO close each related-work group with a failure tied to a property of your scenario (dynamic, context-dependent, many policies): because positioning is then non-generic (evidence: Sec. 2.2, p.3).
9. DO introduce the formal model after a running example, then immediately re-instantiate the example in the new symbols: because it makes the policy triple (object/querier/action) concrete (evidence: p.4-5, John/Prof. Smith).
10. DO place scoping restrictions right where a construct is defined (constant values only, allow-only, deny-to-allow translation): because it keeps claims honest without a separate caveat section (evidence: p.4-5).
11. DO anchor security semantics to an established correctness criterion (sound/secure) and show by counterexample where operator ordering breaks it: because correctness of rewrites under non-monotonic operators is a standard reviewer attack (evidence: p.5 set-difference example, ref [34]).
12. DO reuse the correctness constraint later to explain why a seemingly better baseline configuration is not allowed: because it shows baseline handling is principled (evidence: Baseline_U ordering, p.11).
13. DO express the optimisation goal as an explicit cost model (read cost vs evaluation cost, cardinality from histograms) before giving theorems: because theorems then become cost inequalities with checkable conditions (evidence: Eq. 1-3, p.6; Thm 1-2, p.6-7).
14. DO turn a theorem into an operational test (theta > C) and a step-by-step procedure: because it connects theory to the implementation (evidence: Eq. 9 and 5-step procedure, p.7).
15. DO prove NP-hardness by a short reduction (weighted Set Cover) and then credit the source of your greedy heuristic: because it legitimises a heuristic and shows awareness of prior optimisation theory (evidence: p.7, ref [19]).
16. DO make every adaptive decision in the system cost-model driven and validate each with a dedicated crossover experiment: because thresholds become evidence rather than magic numbers (evidence: Sec. 5.2-5.3 p.8-9; Figs. 3-4 p.11).
17. DO close the running-example loop by showing the actual generated rewrite of the motivating query: because reviewers can see the system output end-to-end (evidence: Sec. 5.4, p.9).
18. DO report setup-time overhead (e.g., guard or cache construction) separately with an absolute anchor figure: because it addresses "what does preprocessing cost?" (evidence: Exp. 1, Fig. 2, ~150 ms at 160 policies, p.10).
19. DO quantify the filtering power of your structure (fraction of checks avoided): because it explains end-to-end speedups mechanistically (evidence: Table 2 Savings ~0.99, p.10-11).
20. DO evaluate on two engines with different capabilities (hints vs no hints) to support a middleware/portability claim: because one engine cannot support "general purpose" (evidence: Exp. 4, Fig. 5, p.12).
21. DO explain baseline anomalies by query-plan analysis (nested-loop choice, bitmap OR): because it shows results are understood, not just measured (evidence: p.11-12).
22. DO define explicit conventions for timeouts and partial completions in result tables (TO, t+): because it avoids hiding failed runs while keeping tables readable (evidence: Table 4 and text, p.11).
23. DO add a second, larger (synthetic) workload specifically to push the scaling axis beyond what the real data allows, and say why: because it separates realism from stress (evidence: Mall, p.9-10, p.12).
24. DO state the speedup trend as a range across the sweep (1.6x to 5.6x): because a growing speedup with scale is the strongest scalability statement (evidence: Exp. 5, p.12).
25. DO disclose what was moved to an extended version and link code: because PVLDB space is tight and reviewers value artifacts (evidence: p.2, fn5 p.8).

### Anti-patterns (do NOT copy blindly)
- No explicit contribution list and no numbers in abstract or intro (p.1-2): modern PVLDB reviewers expect enumerated contributions and a quantified headline.
- Table 3 is never referenced or interpreted in the text (p.10): every exhibit must be cited and earn its headline.
- Internal inconsistencies: 40K devices in intro vs 36K in Sec. 6.1 (p.2 vs p.10); Δ threshold stated as 120 while the Fig. 3 crossover looks nearer 140 (p.9, p.11); semester/quarter mixing (p.3). Audit numbers across sections.
- Greedy Algorithm 1 is said to minimise cost although it is a heuristic with no approximation ratio or complexity analysis (p.8): state complexity and avoid optimality language.
- Equivalence of the guarded expression and the original policy expression is never stated as a theorem; security correctness rests on a citation (p.5): for an access-control paper, state and prove (or test) rewrite equivalence.
- No correctness validation in experiments (e.g., result-set equality vs a reference enforcement): performance-only evaluation leaves the security claim unverified.
- All baselines are author-built rewrite variants; no prior research system or commercial mechanism (VPD, row-level security) is run; Fig. 6 baseline is not named (p.11-12).
- No error bars, variance or CIs on any timing (Table 4, Figs. 2-6); "Savings" computed on an unspecified smaller sample (p.11).
- Unclear whether guard-generation time is included in end-to-end times; not disclosed (p.10-11).
- Synthetic policies on real data without a threats-to-validity discussion of policy realism (p.10).
- No sweep over data volume, concurrent queriers, or policy update rate, despite claiming dynamic scenarios are supported (p.6).
- Very short descriptive captions ("Index choice.") that carry no takeaway; claim-first captions help skimming reviewers.
- Reference list mislabels VLDB proceedings and the VLDB Journal as "PVLDB" ([5,10,23,34], p.13-14): cite venues accurately.
- Experiments occupy only ~24% of the body; for a systems-style PVLDB paper today, a thinner theory section and a richer evaluation (more baselines, correctness, variance) would be safer.

---

## 12. Quantified fingerprint

| Metric | Value |
|---|---|
| Total pages | 14 |
| Body pages (abstract through acknowledgement) | 12 (p.1-12) |
| References | 34 (start p.13) |
| Figures | 6 (1 conceptual ER diagram + 5 result plots) |
| Tables | 4 (1 notation + 3 results/statistics) |
| Algorithms | 1 |
| Theorems / lemmas / numbered definitions | 2 / 0 / 0 (+1 prose NP-hardness reduction) |
| Numbered equations | 11 (13 displayed) |
| Footnotes | 7 |
| Contribution bullets | 0 (prose only) |
| Baselines | 3 end-to-end (Baseline_P, Baseline_I, Baseline_U) on MySQL; Baseline_P on PostgreSQL in Exps. 4-5; plus 2 internal design ablations (Inlining vs Δ; IndexQuery vs IndexGuards) |
| Metrics | 10 distinct (3 performance: generation time, evaluation/execution time, speedup; 7 structural/diagnostic: |P_u|, |G|, |P_Gi|, rho(G_i), Savings, rho(G), TO/t+ completion status counted within execution time) |
| Datasets / workloads | 2 datasets (TIPPERS real 3.9M events/36K devices; Mall synthetic 1.7M events/2,651 devices); 2 policy sets (869,470 and 19,364 policies); 3 query templates x 3 selectivities; 2 DBMSs |
| RQs | 0 formal; 5 numbered experiments (6 counting 2.1/2.2) stated as goals |
| Pages on experiments (Sec. 6 incl. setup) | approx 2.9 (p.9 right column to p.12 upper right) |
| % of body on experiments | approx 24% (page-based); approx 23% by word count (~2,970 of ~12,830 body words) |
| Approx page split | Intro ~1.4; Sec. 2 (case study + related work) ~1.1; Sec. 3 model/semantics/overview ~2.3; Sec. 4 algorithm/theory ~2.3; Sec. 5 implementation ~1.4; Sec. 6 experiments ~2.9; conclusion+ack ~0.4 |
