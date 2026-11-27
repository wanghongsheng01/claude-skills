# ACM PODS View-Rewriting, Determinacy & Complexity-Dichotomy Final-Review Rubric

Distilled from adversarial Program Committee pre-submission audits of database-theory papers involving **view determinacy**, **authorization-safe query rewriting**, **dependency constraints (TGDs/EGDs)**, **$\Pi_2^p$/$\mathrm{coNP}$ hardness reductions**, and **Dinkelbach fractional-optimization algorithms**. Use alongside `review-pods/SKILL.md` and `write-pods/references/pods-view-rewriting-and-authz-craft.md`.

---

## 1. Proof-Completeness Red-Team Checklist (Blocking Triggers)

1. **QBF / $\Pi_2^p$ Relational Reduction — Singleton-Value & Functional-Dependency EGD Audit**:
   - Whenever a hardness reduction encodes Boolean truth domains (`Zero(w)`, `One(w)`) and assignment relations (`Assign_i(x, w)`) using first-order constraints (TGDs + denial constraints), writing only mutual exclusion (`\neg(Zero(w) \land One(w))`) and domain coverage (`Dom(w) \to Zero(w) \lor One(w)`) is **insufficient**: a model `D |= \Sigma` may still instantiate multiple distinct `0`-constants or `1`-constants, breaking the forward direction when a universal TGD fires on only one pair.
   - **Mandatory check**: Verify explicit **singleton-uniqueness EGDs** (`\forall a,b\,(Zero(a) \land Zero(b) \to a=b)`, `\forall a,b\,(One(a) \land One(b) \to a=b)`) and **functional-dependency EGDs** (`\forall x,w_1,w_2\,(Assign_i(x,w_1) \land Assign_i(x,w_2) \to w_1=w_2)`), AND confirm the companion small-model lemma proves full-EGD preservation under induced subinstances.
   - **Machine verification**: Run `>= 50` randomized small $\forall\exists\text{-3SAT}$ instances directly checking both directions of the reduction gadget on finite models.

2. **Information-Determinacy Two-Instance Witness — Zero Implicit Anchor-Tuple Assumptions**:
   - In non-determinacy proofs (`V(D_1) = V(D_2)` yet `Q(D_1) \neq Q(D_2)`), reviewers aggressively hunt for hidden existence assumptions—especially in false-positive witness branches that shift weight using an anchor tuple `t_0` satisfying both target predicate `\phi(t_0)=1` and proxy predicate `\psi(t_0)=1`.
   - **Mandatory check**: Derive `\exists t_0` with `\phi(t_0)=1` strictly from the well-definedness premise of the query/ratio (e.g., positive group denominator `Q_D(D)[\bar{g}] > 0`), and then branch exhaustively on `\psi(t_0) \in \{0, 1\}` (routing `\psi(t_0)=0` cleanly to the false-negative branch and `\psi(t_0)=1` to the anchor-shift branch).

3. **Fractional Optimization (Dinkelbach) Over Non-Empty-Option Domains (`\emptyset \notin \mathcal{F}`)**:
   - When the feasible space enforces mandatory choice per item (e.g., `k`-option partition constraints `\sum_r x_{i,r} = 1` where choosing nothing is infeasible), initializing Dinkelbach's Newton iteration at an unconstrained base ratio `\lambda^{(0)} = N_0 / D_0` can make `\lambda^{(0)}` infeasible, yielding a negative parametric gap `g(\lambda^{(0)}) < 0` and premature wrong termination.
   - **Mandatory check**: Both the theorem proof and the implementation MUST initialize `\lambda^{(0)}` from **any feasible assignment** (e.g., selecting option `0` for every tuple), verified via exhaustive brute-force property testing (`>= 500` random instances) to machine precision (`< 1e-14`).

---

## 2. Complexity-Axis Clarity & Body Self-Containment

4. **Explicit Separation of Data, Combined, and Parameterized (`FPT`) Complexity**:
   - Whenever an algorithm runs in `O(2^w \cdot \mathrm{poly}(n))` for bounded treewidth `w`, explicitly label it **`FPT` (parameterized by treewidth `w`)** in both the theorem statement and the master complexity summary table, cleanly decoupled from **Data Complexity (`PTIME`)** and **Combined Complexity (`coNP` / `\Pi_2^p`)**.

5. **15-Page Body Self-Containment & 1-to-1 Body-to-Appendix Proof Accounting**:
   - Because PODS PC members are **not obligated to read appendices**, every main-body Theorem and Proposition MUST carry a crisp `Proof Idea` containing the core construction or reduction skeleton inside the `14.3–15.0` page body.
   - Run a strict **1-to-1 theorem-to-proof checklist**: zero unproved Propositions or Lemmas anywhere in the paper; every stated claim must map cleanly to a complete proof in the body or Appendix.

---

## 3. Visual, Typography & Cleanroom Verification Checks

6. **Character-Exact Figure-to-Prose Symbol Alignment & 180 DPI Raw-Markup Scan**:
   - Run `figure_formula_consistency_audit.py` on every figure-generation script to catch dropped bar/vector decorations (e.g., `\rho_g` vs. `\rho_{\bar{g}}`, `g(t)` vs. `\bar{g}(t)`) and raw ASCII comparison operators (`<=` instead of `\le`).
   - Visually inspect 180 DPI PNGs of all body and key appendix pages to catch stray Markdown backticks (rendering as curly quotes instead of `\texttt{...}`), awkward page breaks before Propositions (`\goodbreak`), crowded table headers, and dense appendix proof bricks (split long proof directions into 4–7 line breathing paragraphs).

7. **Isolated `/tmp` Cleanroom Execution & Native PODS Style Discipline**:
   - Copy the anonymous artifact bundle to an isolated `/tmp` directory and execute `bash run_all.sh` end-to-end (`exit 0`), confirming every table count and exact verification count reproduces verbatim with zero host-path or identity leaks.
   - Enforce pure PODS published conventions: **zero** `\textbf{Takeaway.}` database-engineering stamps, **zero** `Limitations` or `Threats to Validity` section headings, **zero** AI clichés or em-dashes, and **zero** arXiv citations where peer-reviewed versions exist.
