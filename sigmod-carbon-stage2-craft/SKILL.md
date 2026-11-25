---
name: "sigmod-carbon-stage2-craft"
description: "Stage-2 high-reasoning scientific, formal, modeling, verification, and experimental upgrade playbook for ACM SIGMOD (Research & Industrial Track) papers. Distilled from reverse-engineering published SIGMOD 2024-2026 papers (WAIR SIGMOD'26, Enzyme SIGMOD'26 Ind, AlayaDB SIGMOD'25 Ind, Measures in SQL SIGMOD'24 Ind, FinSQL SIGMOD'24 Ind). Enforces the permanent Two-Stage Paper Convention: after Stage-1 end-to-end drafting and live benchmarking, invoke this skill on a high-reasoning model to review and upgrade (1) non-trivial necessary-and-sufficient theorem derivations & constructive proofs, (2) multivariate analytical risk/cost models predicting exact regime boundaries, (3) executable 10,000-state property-based / RQG formal verification, (4) multi-scale & multi-factor sensitivity experiments, and (5) authentic human-prose integration with strict international-venue model naming neutrality (zero 'international/domestic' labels)."
---

# SIGMOD Stage-2 Formal, Modeling, Verification & Experimental Craft (`sigmod-carbon-stage2-craft`)

## Permanent Two-Stage Paper Engineering Convention

Every CCF-A database systems submission follows a strict **Two-Stage Workflow**:
- **Stage 1 (Foundation, Live Systems & Human Draft)**: Establish problem framing, real enterprise telemetry + public reproducible benchmark (e.g., TPC-DS), live multi-LLM evaluation via `llmhub`, clean functional component naming, and human-style academic prose (`sigmod-human-writing-craft`).
- **Stage 2 (High-Reasoning Scientific Upgrade — THIS SKILL)**: Switched to a frontier deep-reasoning model, perform an adversarial mathematical, formal-verification, and experimental-design audit, upgrading the manuscript across **Four High-Barrier Scientific Pillars** so that even the most theoretical PC reviewer recognizes deep, non-trivial database science beneath the production system.

> **Permanent Model-Naming Neutrality Rule (Global Redline)**: Top-tier database venues (SIGMOD, PVLDB, ICDE) are international forums. **NEVER** partition, label, or contrast LLMs as *"international vs. domestic"* (`国外模型 / 国内模型`, `Intl. / Dom.`) anywhere in prose, tables, figures, captions, or scripts. Always refer to models directly by their concrete family/version names (e.g., *"six foundation models spanning distinct model families: `GPT-6.2-Sol`, `Claude-Opus-5.5`, `Gemini-4-Argon`, `DeepSeek-V4-Pro`, `Kimi-K3.1-Pro`, and `Qwen3.8-27B`"*).

---

## 1. What Published SIGMOD '24–'26 Papers Actually Do (Reverse-Engineered Anatomy)

Detailed page-level dissections live in `references/SIGMOD_FORMAL_MODELING_DISSECTION.md`. Summary of the four mechanisms separating accepted SIGMOD papers from shallow "engineering report" rejections:

| Dimension | Shallow Stage-1 Anti-Pattern (Rejected) | Published SIGMOD Standard (Accepted) | Exemplar |
|---|---|---|---|
| **1. Complex Theorem Derivation** | Restating `if-else` branches of Algorithm 1 as a 3-line "Proposition" (*"since Gate 2 checks 6 flags, invalid reuse is blocked"*). | Prove **algebraic / structural impossibility & necessary-and-sufficient conditions** (e.g., fiber cardinality $|F_u|=1$ for ratio rollup homomorphisms with explicit adversarial witness construction when $|F_u|\ge 2$), paired with **inductive termination, uniqueness, and scale-invariance proofs**. | `WAIR` (SIGMOD '26 Lemmas 1–3, Thms 4–5); `Measures in SQL` (SIGMOD '24 Sec. 3–4) |
| **2. Multivariate Analytical Modeling** | Verbal intuition (*"big schemas confuse LLMs and schema drift breaks queries"*). | Explicit **multivariate risk / cost equations** over interacting schema, workload, and drift variables (e.g., $P_{\text{silent}}(|T|, R, \lambda_{\text{break}}, \Delta t)$ vs. lineage-scoped planning cost $C_{\text{plan}}$), predicting **regime crossover points** and explaining empirical curves. | `WAIR` (SIGMOD '26 Sec. 4.2 $\Delta \widehat{\text{cost}}_q$); `Enzyme` (SIGMOD '26 Sec. 4.5) |
| **3. High-Difficulty Formal Verification** | Only testing 20–30 hand-crafted benchmark queries. | **Automated Property-Based / Random Query & Mutation Generator (RQG)** executing $10^4+$ randomized DAG topologies, grain/join mutations, currency assignments, and snapshot hash perturbations against a ground-truth reference oracle (`0` invariant violations). | `Enzyme` (SIGMOD '26 Sec. 5 RQG equivalence checker) |
| **4. Multi-Factor Experimental Design** | Single fixed schema scale (`105` tables) + flat bar charts. | **Orders-of-magnitude scale sweep** (`36 → 105 → 500 → 1,599` tables) $\times$ **operating-point sensitivity** (e.g., materialization hit ratio $\rho \in [0\%, 100\%]$, hop bound $h_{\max}$), overlaying empirical P50/P99 latency against theoretical complexity bounds. | `WAIR` (SIGMOD '26 Sec. 6); `AlayaDB` (SIGMOD '25 Figs. 5–11) |

---

## 2. Three-Step Stage-2 Execution Protocol

Whenever invoked on an existing SIGMOD draft, execute **three sequential deliverables**:

### Step A — Adversarial Stage-2 Scientific Audit Report
Inspect the full paper (`main.tex`), system source code, and Stage-1 experiment JSONs. Produce a structured Markdown audit report diagnosing:
1. **Theorem Depth Audit**: Are current propositions tautological restatements of code branches? Where is the underlying algebraic/relational barrier (e.g., non-homomorphic quotient aggregation, lossy many-to-many join fan-out, non-serializable metadata-snapshot read skew)?
2. **Modeling Gap Audit**: Which interacting system parameters ($|T|$, rule coupling $k_q$, drift arrival rate $\lambda_{\text{break}}$, staleness window $\Delta t$, precomputation hit rate $\rho$) lack a unified analytical equation?
3. **Verification & Scale Gap Audit**: Can a reviewer challenge that 24–36 benchmark queries miss corner-case DAG topologies or full-estate (`1,500+` tables) scaling?
4. **Neutrality & Prose Audit**: Scan for any `international/domestic` (`Intl./Dom.`) terms, port/codename leaks, or formula dumps lacking intuitive framing.

### Step B — Executable Formal Verification & Multi-Scale Sensitivity Suite
Write and execute a deterministic, seeded Python verification & scaling suite (`seed=42`, frozen to JSON):
1. **10,000-Trial Property-Based Model Checker**:
   - Randomly generate diverse schema/metric DAGs (varying depth $1..8$, fan-out, additive vs. non-additive ratio nodes, FX heterogeneity, SCD2 bridge vs. missing-key topologies, DWS-to-DWS trap edges, 7-tuple hash mutations).
   - Verify **every formal theorem** empirically against an exact row-level relational reference evaluator:
     - *Soundness*: `0 / 10,000` uncertified plans leak into `ok` primary status; whenever `status == ok`, numerical deviation vs. row-level ground truth is `< 10^{-12}`.
     - *Completeness on Valid Certified Subspace*: `100%` of valid specifications with complete certified assets resolve to `ok`.
     - *Bounded Termination*: `100%` terminate within recursion/BFS bounds even under injected cyclic metadata mutations.
2. **Multi-Scale & Parameter Sensitivity Benchmark**:
   - Measure real planner & gate latency across **4 realistic warehouse scales** (e.g., `36` TPC-DS → `105` Governed Core → `500` Multi-Domain → `1,599` Full Enterprise Estate) $\times$ **5 materialization hit ratios** ($\rho \in \{0, 0.25, 0.50, 0.75, 1.0\}$), contrasting lineage-scoped $O(1)$-in-$|T|$ resolution against unscoped schema-wide graph search.

### Step C — Human-Style Mathematical Prose Integration (Within 12-Page Budget)
Weave the upgraded model, theorems, proofs, and verification results into `main.tex` following **Four Human-Math Writing Rules** (`Measures in SQL` & `WAIR` style):
1. **Intuition $\to$ Formalism $\to$ Operational Meaning**:
   - *Before* every equation or theorem: 1–2 plain English sentences stating the physical database failure it captures.
   - *Inside* the theorem/proof: crisp notation, explicit quantifiers, zero hand-waving, constructive counterexample or inductive step.
   - *After* the proof: 1 sentence linking the theorem directly to an implemented engine mechanism and its empirical verification count (`10,000/10,000` randomized topologies).
2. **Zero Space Bloat**: Tighten verbose narrative repetitions in later sections so the entire upgraded paper (including Acknowledgments) still lands cleanly within **$\le 12.0$ body pages** with `0` `acmart` template hacks.
3. **Cross-Artifact Consistency (`R16`)**: Every symbol, latency number, and trial count in text, tables, and figure callouts must match the frozen JSON artifacts to the exact decimal.
4. **Run Mandatory Post-Edit Gates**:
   - `tectonic` / `pdflatex` (`0` undefined references/citations, body `<= 12` pages);
   - `layoutlint.py` (`0 Blocker`, `0 Major`);
   - `ai_smell_audit.py` (`0` banned AI clichés, em-dash density `<= 1.0 / 1K words`);
   - Geopolitical & redaction grep (`0` hits for `international|domestic|Intl\.|Dom\.` on models, `0` internal port numbers, `0` engineer names, `0` currency amounts).

---

## 3. Reference Files
- `references/SIGMOD_FORMAL_MODELING_DISSECTION.md` — Concrete mathematical patterns, proof structures, RQG verification harnesses, and prose templates extracted from `WAIR` (SIGMOD '26), `Enzyme` (SIGMOD '26 Ind), `AlayaDB` (SIGMOD '25 Ind), `Measures in SQL` (SIGMOD '24 Ind), and `FinSQL` (SIGMOD '24 Ind).
