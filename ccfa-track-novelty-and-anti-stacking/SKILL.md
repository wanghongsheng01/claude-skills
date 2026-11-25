---
name: ccfa-track-novelty-and-anti-stacking
description: "Mandatory pre-writing and pre-submission gate for CCF-A database venues (PVLDB Regular Research, PVLDB EA&B, PVLDB SDS, SIGMOD Research, SIGMOD/VLDB Industrial). (1) Calibrates theoretical vs. systems vs. empirical novelty expectations per target track before drafting or reviewing; (2) Reverse-engineers how published enterprise-motivated PVLDB papers (DBSP '23, SPADE '24, LOTUS '25, DocETL '25, Semantic Integrity Constraints '25, Deequ '18) unify multi-stage engineering pipelines into ONE core data-management problem and ONE algebraic/optimization abstraction, defeating reviewer accusations of 'too engineering / thin DB theory' and 'gains only come from stacking many modules'."
---

# CCF-A Track Novelty Calibration & Anti-Module-Stacking Craft

**MANDATORY RULE FOR ALL SUBMISSIONS:** Before drafting, revising, or reviewing any manuscript, first identify the exact target venue and track in Section 1, calibrate the required theoretical/algorithmic/empirical depth, and then apply Section 2's anti-stacking structural blueprint and `scripts/anti_stacking_lint.py`.

---

## 1. Venue & Track Novelty Calibration Matrix (Survey First!)

Different tracks at PVLDB and SIGMOD apply fundamentally different novelty bars and desk-reject criteria. Treating a Research Track paper like an Industrial report—or treating an EA&B paper like a "my method wins" paper—causes preventable rejections.

| Target Track | What Reviewers Count as Novelty | Required Formal & Architectural Depth | Top Fatal / Desk-Reject Triggers |
|---|---|---|---|
| **PVLDB Regular Research — Foundations & Algorithms** | New data model, query algebra, complexity bound, approximation/statistical guarantee, or exact verification algorithm (`DBSP` '23, `QED` '24). | Formal problem definition + non-trivial theorems/proofs (tight bounds, necessary & sufficient barriers, or convergence/optimality) + precise algorithms. | Ad-hoc rule lists; trivial 2-line "sanity-check" theorems that restate an `if` branch; missing DB-core engagement. |
| **PVLDB Regular Research — Systems** | Principled new system abstraction, query rewrite space, or execution architecture that solves a general data-management bottleneck (`LOTUS` '25, `DocETL` '25, `SPADE` '24). | **One unifying system abstraction** (e.g., semantic operator algebra, subsumption ILP, provenance-semilattice view maintenance) + working end-to-end engine + public & real workloads against living SOTA. | **"Frankenstein / Module-Stacking" smell**: listing 5–7 domain-specific engineering filters (`"five operators... four guarantees"`) where gains appear to come from piling up heuristics rather than one core DB abstraction. |
| **PVLDB Experiment, Analysis & Benchmark (`EA&B`)** | Counter-intuitive empirical insights across living SOTA systems, new evaluation methodology/metrics, or real-world fleet characterization (`DAIL-SQL` '24, `Redset` '24). | Title suffix `[Experiment, Analysis & Benchmark]`; frozen fairness protocol; conditional operating-regime findings (may refuse a blanket winner); **complete reproducibility package mandatory at initial submission** (Vol. 20+). | Pitching authors' own new method as champion; incomplete initial artifact link; testing outdated/strawman baselines. |
| **SIGMOD / VLDB Industrial Track** | Principled architectural solution to real production constraints (scale, drift, multi-tenant ACLs, auditability), transparent deployment scope, multi-month telemetry, and hard-won operational lessons (`FinSQL` '24, `AlayaDB` '25, `Enzyme` '26, `Cortex AISQL` '26). | Non-academic industry co-author; exact UAT vs. production vs. pilot disclosure; formalization proportional to the production invariant (`AlayaDB` Def. 1–3 + Thm. 1); 4–5 incident-backed lessons. | Product brochure tone; hiding deployment boundaries; opaque internal port/codename jargon; unmotivated bag of microservices. |

---

## 2. Defeating the "Engineering Module-Stacking" Critique in Enterprise-Motivated Research Papers

When a paper originates from a real enterprise production system (e.g., B2B stream labeling, LLM pipeline validation, warehouse governance), the codebase naturally contains 5–8 engineering stages. If the paper mirrors the codebase 1-to-1 (*"Module 1 does A; Module 2 does B; Module 3 does C; Module 4 does D; Module 5 does E"*), PVLDB Research reviewers attack on **two lethal fronts**:
1. *"Too engineering / weak database-management theory: each individual module is a thin heuristic (regex/offset slicing, timestamp filter, if-else rules, logistic regression, max-stage counter)."*
2. *"Unfair / stacked gains: the +8 pp accuracy improvement only happens because five post-processing modules are stacked on top of the LLM."*

### How Published PVLDB Papers Solved This Exact Dilemma (Reverse-Engineered Blueprint)

Study of `DBSP` (PVLDB '23), `SPADE` (PVLDB '24), `LOTUS` (PVLDB '25), `DocETL` (PVLDB '25), `Semantic Integrity Constraints` (PVLDB '25), and `Deequ` (PVLDB '18) reveals a **6-Move Structural Blueprint** (detailed in [`references/PVLDB_ENTERPRISE_TO_THEORY_ANATOMY.md`](references/PVLDB_ENTERPRISE_TO_THEORY_ANATOMY.md)):

1. **Move 1 — Elevate the Enterprise Bottleneck into ONE Canonical Database Problem (`§1 P1–P2` & `§2`)**:
   - Do **not** frame the problem around a company workflow (*"labeling B2B sales emails and updating CRM stages"*).
   - Frame it as a **fundamental violation of a classic database abstraction**:
     - `SPADE`: Prompt tinkering $\to$ *Synthesizing Minimum-Cost Data Quality Assertions under Subsumption*.
     - `DocETL`: Multi-prompt scripts $\to$ *Accuracy-Preserving Logical Query Rewriting for Unstructured Document Pipelines*.
     - `LedgerTag`: Email tagging + ERP checks $\to$ *Contract-Governed Incremental View Maintenance (IVM) over Unstructured-Relational Streams under Budgeted Provenance*.
2. **Move 2 — Prove Why Single-Mechanism Fixes Fail (`§1 P3` Causal Necessity Chain)**:
   - Explicitly show why **no single existing primitive suffices** because the failure modes are algebraically coupled:
     - Without coordinate provenance, historical quotes masquerade as new stream tuples;
     - Without bi-temporal as-of prefixing, joining versioned relations leaks future commits;
     - Without monotonic semilattice reconciliation, non-idempotent LLM extractions corrupt entity views;
     - Without calibrated risk shrinkage, binary quarantine exhausts finite human audit budgets.
   - This turns "multiple components" from *arbitrary engineering bloat* into **minimal necessary conditions** of one theorem!
3. **Move 3 — Group Operators Under ONE Unifying Abstraction (Max 2–3 Theoretical Pillars, NEVER "5 Operators + 4 Guarantees"!)**:
   - **BANNED in Abstract & Intro**: `"behind five deterministic database operators: A; B; C; D; and E. We establish four formal guarantees..."`
   - **REQUIRED**: Name **one unifying formalism** (e.g., *a Provenance-Semilattice View Algebra paired with Empirical-Bayes Quarantine Allocation*), where sub-operators appear as homomorphic stages of a single algebraic pipeline $\mathcal{M} \bowtie_{\text{asof}} \mathcal{E}_{\text{rel}} \xrightarrow{\pi^{\text{sem}}_{\mathcal{G}}} \mathcal{K} \times \{\mathsf{conf},\mathsf{rev},\mathsf{supp}\} \xrightarrow{\sqcup} \mathcal{L}_\perp$, governed by a **closed-form multiplicative residual-risk law**!
4. **Move 4 — Build a Connected Theoretical Spine Instead of Fragmented Per-Module Mini-Theorems**:
   - Four disconnected 3-line theorems make reviewers think each module is trivial.
   - Instead, build a **chained theoretical spine**:
     - *Structural Soundness & Confluence Spine*: Prove end-to-end view soundness, bi-temporal non-leakage, order-invariant semilattice convergence, and **tight minimality** (dropping any stage admits an adversarial counterexample trace that corrupts the materialized view).
     - *Statistical-Database Optimality Spine*: Prove non-trivial finite-sample concentration / variance-damping bounds (e.g., Empirical-Bayes $O(n_g/\alpha^2)$ cold-start variance vs. $O(1/n_g)$ empirical blowup + closed-form sample crossover $N^*$).
5. **Move 5 — Preempt "Module Stacking" Directly in the Evaluation (`Orthogonal Factor Attribution`)**:
   - Dedicate an explicit paragraph in the ablation subsection to **Orthogonality vs. Stacking**:
     - Show that the zero-parameter structural algebra *alone* achieves 100% of safety invariants (`0.0%` violations at minimal review overhead), while statistical routing acts on an **orthogonal recall/precision axis**, and each stage removes a disjoint failure mode matching the analytical decomposition (`MAE < 0.5 pp`).
6. **Move 6 — Abstract Four-Beat Discipline (`160–220` words)**:
   - **Sentence 1–2 (DB Context & Fundamental Bottleneck)**: Name the general data-management operator class and why production streams break it.
   - **Sentence 3–5 (System + Unifying Insight + Two Synergistic Pillars)**: `"We present X, a ... engine. Our key insight is to lift probabilistic LLM projections into a provenance-indexed tri-state semilattice..."` (NO semicolon-separated 5-item inventory!).
   - **Sentence 6 (Unified Formal Spine)**: State the core soundness/confluence and finite-sample crossover guarantees in plain, authoritative prose.
   - **Sentence 7–8 (3–4 Headline Numbers on Public + Production Workloads)**: Exact match to main tables.

---

## 3. Automated Gate

Run on every draft iteration:
```bash
python3 scripts/anti_stacking_lint.py path/to/main.tex --track pvldb-research
```
Must return **`0 FAILs`** before compilation delivery.
