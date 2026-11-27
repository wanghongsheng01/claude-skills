# PVLDB Lineage, Schema-Drift & Incremental Validation Final-Review Rubric

Distilled from adversarial PVLDB Program Committee & Associate Editor pre-submission audits of database systems papers addressing **SQL lineage graphs, schema/premise drift detection, incremental maintenance, and dual-plane (deterministic + LLM) validation**. Use alongside `review-pvldb/SKILL.md` and `paper-presubmission-review/SKILL.md`.

---

## 1. Proof, Algorithm & Edge-Case Soundness Checks (Blocking Triggers)

1. **Compiled-PDF `algorithmic` Line-Number Verification**:
   - LaTeX `algorithmic` numbers `else` and `end if` lines automatically. Whenever a Theorem or Proposition proof cites `Line k` of an Algorithm block, verify every single cited line number directly against the **compiled PDF** (not raw `.tex` mental counts) to prevent embarrassing off-by-one references pointing at control keywords.
2. **Per-Branch vs. Global Predicate Checks in Multi-Branch `UNION ALL` Queries**:
   - In lineage/view-drift analyzers, checking predicate absence globally (`p \notin \Psi(Q)`) fails on hybrid `UNION ALL` queries where Branch 1 carries explicit predicate `p` while Branch 2 silently degrades to a proxy `q`. Audit both the formal algorithm and executable engine to ensure verification runs **per non-exempt branch**.
3. **Four Mandatory Production-Warehouse Edge Cases (Proven & Stress-Tested)**:
   - Every lineage/incremental-validation paper must bound and empirically verify (`>= 500` adversarial tests each):
     1. **Cyclic feedback lineage graphs** (BFS visited-set termination & exact delta equivalence);
     2. **Out-of-band physical DDL mutations** (column renames/splits occurring outside the catalog commit pipeline);
     3. **Empty views / zero-denominator aggregations** (division-by-zero protection with zero false alarms);
     4. **Hybrid multi-branch queries** mixing explicit predicates and degraded proxies.

---

## 2. Claim-to-JSON Reconciliation, Rounding & Baseline Fairness

4. **Headline-Range vs. Min-Cell & `±` Confidence-Interval Audit**:
   - Whenever Abstract, Introduction, Figure 1, or captions advertise a speedup range `[a×, b×]`, programmatically check every cell in the scaling table so no intermediate scale point falls below `a×` (e.g., claiming `8.7×–49.7×` when a mid-scale cell measures `7.85×`).
   - Reconcile every `±` interval in LaTeX tables directly against raw JSON `ci95`/`std` fields via script—never hand-copy stale numbers from earlier runs.
5. **Uncached Latency Persistence & IEEE-754 Double-Rounding Prevention**:
   - For evaluations involving LLM/API baselines, persist 100% uncached end-to-end latency and cost rows directly inside the primary `results/*.json` (not only local side logs).
   - Keep `>= 4` decimal digits in intermediate JSON metrics to eliminate IEEE-754 half-to-even double-rounding drift (`82.3529% -> 82.35 -> 82.3` instead of `82.4`), and avoid dividing rounded display cells when reporting multi-order-of-magnitude latency ratios (preventing rounding-induced ratio paradoxes).
6. **Union-of-Deterministic-Tools Baseline & Standalone Public-Benchmark Significance**:
   - Whenever a unified multi-plane validator outperforms individual single-plane tools (e.g., data-quality checks, SQL AST linters, catalog diffs), PVLDB R2 will immediately ask: *"What if we simply take the union of all existing lightweight deterministic tools?"* Include a real measured **`Combined-Classic`** union baseline AND explicitly break out **standalone public-benchmark** (e.g., TPC-DS / BIRD) F1 and exact nonparametric $p$-values proving core claims do not depend on proprietary enterprise data.

---

## 3. 180 DPI Visual Craft & PVLDB Anti-Self-Negation Gate

7. **180 DPI Narrow-Column Equations, Serif Figures, Ties & Non-Self-Negating Conclusions**:
   - Visually inspect 180 DPI PNGs of every page to catch wrapped equation tags `(k)` inside two-column `align` blocks (tighten via `\!`/`\;`).
   - Match all vector figures to `acmart`/`pvldb.sty` body typography (Times/STIX serif fonts, `mathtext.fontset: stix`, zero raw ASCII `<=` or `x` math operators, zero label-curve collisions).
   - Enforce **shared bolding on tied best values**, **underlined second-best**, and an automated **`Best/2nd` count column** in every primary comparison table; keep **zero** non-PVLDB `\textbf{Takeaway.}` stamps.
   - Strip self-negating future-work closings from the Conclusion ("our system does not yet handle X, which we leave to future work"): state technical scope boundaries **once** objectively in the method section, and close the Conclusion with a forward-looking research connection.
