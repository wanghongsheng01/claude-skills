# Deep Visual, Structural & Theoretical Anatomy of Published ACM PODS Papers (2024–2027)

Distilled from direct page-by-page visual and full-text inspection of 8 officially accepted ACM PODS papers (`PACMMOD` Vol. 2–4 & PODS 2027 Cycle 1), focusing on **why genuine PODS papers read as deep foundational database theory rather than polished systems notes**.

---

## 1. Ten Non-Negotiable Hallmarks of Authentic Published PODS Papers

### Hallmark 1 — Framed Computational Problem Boxes (`PROBLEM / INPUT / OUTPUT`)
- **Exemplar Evidence**:
  - `Karmakar, Monet, Senellart, Bressan (PODS '24, pp. 3, 5)`: Every core computational task (`Score_c(F)`, `EV_*(F)`, `ENV_{*,*}(F)`) is displayed in a clean framed box with aligned `PROBLEM:`, `INPUT:`, and `OUTPUT:` rows.
  - `Kolaitis, Pardal, Virtema, Wijsen (PODS '25, p. 6)`: `PROBLEM: mCA_K(q, \Sigma)` / `INPUT:` / `OUTPUT:` framed box anchors Section 4.
  - `Esmailpour, Galhotra, Raychaudhury, Sintos (PODS '25, p. 4)`: Formal `PROBLEM 1 (PTILE)` and `PROBLEM 2 (PREF)` environments anchor the entire technical contribution.
- **Anti-Pattern to Reject**: Describing decision, counting, or certification problems only informally inside prose paragraphs.
- **PODS Rule**: Define **at least 2–4 framed `PROBLEM / INPUT / OUTPUT` boxes** for the paper's central computational problems.

### Hallmark 2 — Explicit `Data Complexity` vs. `Combined Complexity` & Complete Dichotomies / Trichotomies
- **Exemplar Evidence**:
  - `Kolaitis et al. (PODS '25, §4 p. 6)`: Explicitly opens Section 4 with Vardi's distinction between **data complexity** (schema and query/constraints fixed, only database instance varies) and **combined complexity** (schema arity unbounded), then proves an exact acyclicity dichotomy.
  - `Karmakar et al. (PODS '24, §3 & §5)`: Proves polynomial interreducibility (`\equiv_P`) separating tractable circuit classes from `#P`-hard classes.
  - `Surianarayanan, Kumar, Sintos (PODS '26, Table 1 p. 6)`: Maps the complete tractability/approximation frontier across parameter regimes (`f=1`, `f>1`, `d=O(1)`, relational join width).
- **Anti-Pattern to Reject**: Proving a single `#P`-hardness reduction that requires unbounded schema arity $m = n$ while ignoring whether the problem becomes tractable or stays `#P`-hard for fixed schema arity $m = 1, 2, 3$ (data complexity) or fixed finite domain $|\mathcal{V}| = O(1)$!
- **PODS Rule**: Always classify complexity across **both data complexity (fixed schema arity $m$) and combined complexity (unbounded $m$)**, identifying exact tractability boundaries (e.g., $m=1$ vs. $m \ge 2$, fixed vs. unbounded domain).

### Hallmark 3 — Connection to Core PODS Semantics (`Certain` / `Possible Answers` over Repair Worlds)
- **Exemplar Evidence**:
  - `Arenas–Bertossi–Chomicki (PODS '99)` & `Kolaitis et al. (PODS '25, Def. 3.5)`: When multiple minimal repairs $\mathrm{Rep}(D, \Sigma)$ exist, semantics is defined via extremal bounds ($\min$ / $\max$) across all repair worlds.
- **PODS Rule for Data-Quality & Evaluation Papers**: When an underspecified contract admits a set of optimal worlds (such as $\Pi^*(D, D')$), do not stop at testing whether $|\Pi^*| = 1$; characterize the complexity of computing **certain (pessimistic, $\min_{\pi \in \Pi^*}$)** and **possible (optimistic, $\max_{\pi \in \Pi^*}$)** evaluation outcomes!

### Hallmark 4 — Rich Formal `\begin{example}` Threads & `\begin{lemma}` Scaffolding
- **Exemplar Evidence**:
  - `Karmakar et al. (PODS '24)`: **6 numbered `Example` environments** (`Ex. 2.1, 2.2, 2.4, 3.6, 4.1, 5.1`) + **7 `Lemma`s** scaffolding the 6 `Theorem`s!
  - `Kolaitis et al. (PODS '25)`: **9 `Definition`s, 3 `Example`s, 4 `Lemma`s, 8 `Proposition`s**!
  - `Liu & Zhang (PODS '26)`: **10 `Lemma`s and 6 `Claim`s** decomposing variance/expectation bounds cleanly!
- **Anti-Pattern to Reject**: Zero `\begin{example}` and zero `\begin{lemma}` environments (jumping straight from `Definition` to `Theorem` with compressed 6-line proof sketches, which makes a paper feel skeletal and thin).
- **PODS Rule**: Maintain **at least 3–5 numbered `\begin{example}` environments** tracing concrete relational instances and **at least 3–6 structural `\begin{lemma}`s** decomposing key invariants (LP dual slackness, degree-constrained orientation gadgets, perturbation Lipschitz bounds).

### Hallmark 5 — Mathematical Concrete-Instance Schematics (`Fan–Koutris–Roy PODS '25 Fig. 1` Style)
- **Exemplar Evidence**:
  - `Fan, Koutris, Roy (PODS '25, Fig. 1 p. 4)`: Side-by-side concrete mathematical objects: `(a) Relation Instance E` (actual bordered tuple grid), `(b) Induced Directed Graph`, `(c) Derivation / Proof Structure` — zero pastel PowerPoint marketing boxes!
- **Anti-Pattern to Reject**: Big colored rounded boxes containing generic phrases (`Raw Snapshots -> Loaded Snapshots`) with lots of empty background fill.
- **PODS Rule**: Figure 1 in a PODS paper must display **actual concrete relational tables, matrices, dual potentials, and graph/algebraic structures** so a theorist can verify the theorem on the figure's instance by hand in 60 seconds!

### Hallmark 6 — Dedicated, Single-Purpose Tables (`Karmakar et al. PODS '24 Tables 1–3`, `Surianarayanan et al. PODS '26 Table 1`)
- **Anti-Pattern to Reject**: Cramming two unrelated experiments side-by-side into one hybrid table (`Planted Attribution` on columns 1–3 and `Runtime Scaling + Stress Test` stuffed into columns 4–6) to save vertical space.
- **PODS Rule**: Every table has **ONE clear domain and ONE schema**:
  - Table 1: Master Theoretical & Complexity Frontier Summary (Problem, Regime, Bound/Characterization, Complexity, Reference);
  - Subsequent tables: One dedicated table per experimental family (e.g., Alignment & `CertEval` Scaling; Per-Dataset Consumer Normalization Audit; Outlier Redistribution & Attribution Breakdown).

### Hallmark 7 — Full Utilization of the 15-Page PACMMOD Body (`14.5–15.0` Pages) + Deep Self-Contained Appendix
- **Exemplar Evidence**: Accepted PODS papers fill **14.5–15.0 full body pages** with complete definitions, problem boxes, running examples, lemmas, full proofs of flagship theorems, and thorough experimental interpretation (e.g., `Karmakar et al. PODS '24 p. 16` gives 6 numbered analytical observations `(1)–(6)` dissecting experimental behavior!), followed by References and a rigorous multi-page Appendix.
- **Anti-Pattern to Reject**: Under-filling the body at 13 pages by over-compressing proofs into terse sketches, OR spilling past Page 15.0 into desk-reject territory.
