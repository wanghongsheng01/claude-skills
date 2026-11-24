---
name: sigmod-industrial-acceptance-craft
description: Empirical SIGMOD Industrial Track acceptance-bar playbook distilled from published SIGMOD '24–'27 Industrial & Systems papers (FinSQL, Data-Juicer, Measures in SQL, AlayaDB, Enzyme, DIVER, WAIR, SALUS). Use when framing an industrial database paper's thesis (立意), structuring contributions for maximum systems depth (含金量), organizing dual production+public experiments, or reviewing a draft against the real SIGMOD Industrial acceptance bar.
---

# SIGMOD Industrial Track Acceptance Craft

This skill captures the **empirical acceptance bar** of the ACM SIGMOD Industrial Track (and closely related database systems tracks) based on direct dissection of eight published SIGMOD 2024–2027 papers (detailed in [references/SIGMOD_INDUSTRIAL_DISSECTION.md](references/SIGMOD_INDUSTRIAL_DISSECTION.md)).

## When to Use This Skill
- Before drafting or revising a SIGMOD Industrial Track paper's **Abstract, Introduction, Contributions, System Overview, or Evaluation**.
- When an author asks: *"Does our thesis framing (立意), contribution structure (贡献组织), systems substance (含金量), and experimental design actually reach the SIGMOD Industrial acceptance bar?"*
- During pre-submission internal review to identify exact gaps between an engineering project report and an accepted SIGMOD Industrial paper.

---

## The 6 Non-Negotiable Laws of Accepted SIGMOD Industrial Papers

### Law 1 — Elevate Thesis Framing (立意) from "Company Tool" to "Universal Systems Abstraction"
Reviewers reject papers that read like internal product manuals ("we built tool X for company Y"). Accepted papers anchor an urgent industrial pain point and immediately elevate it into a **transferable database systems abstraction**:
- **Google `Measures in SQL` (SIGMOD '24 Ind)**: Frames *"Tables are broken"* for multi-dimensional analytics → introduces *Context-Sensitive Expressions (CSEs)* applicable to any SQL engine.
- **Databricks `Enzyme` (SIGMOD '26 Ind)**: Frames *"IVM pipelines require brittle manual tuning"* → introduces *cost-based multi-MV incremental planning + transactional provenance* over Spark/Delta primitives.
- **`AlayaDB` (SIGMOD '25 Ind)**: Frames *"Long-context LLM inference couples compute and KV memory"* → introduces a *new decoupling layer* + *DIPR vector query*.

**Mandatory Artifact (Positioning Matrix)**: Include a crisp 4–6 column architectural comparison table in Section 2 or 3 contrasting your system against the 3–4 dominant existing paradigms (e.g., naive LLM/Direct-SQL, prompt/RAG glossaries, traditional BI semantic layers / catalogs) across concrete database invariants. A reviewer should grasp in 10 seconds *why* existing categories structurally fail.

### Law 2 — Structure Contributions Around Formal Database Primitives, Not LOC or Microservice Counts
Never headline LOC counts, microservice port numbers, or test-suite totals as your primary scientific contributions (place engineering scale in Section 3/5 implementation details). Every contribution bullet in Section 1 must follow the **Problem → Formal Primitive → Quantified Impact** triad:
1. **Named Architectural Decoupling / Data Model** (what state/contract boundary is newly formalized).
2. **Core Algorithmic or Formal Correctness Mechanism** (Algorithms + at least one crisp **Soundness / Invariant Proposition** proved by construction, e.g., AlayaDB's definitions, WAIR's cost bound, Measures' operational semantics).
3. **Production Enforcement & Closed-Loop Verification** (how correctness survives live data/schema churn — cf. Enzyme's dual RQG + production A/B correctness verification).
4. **Dual Empirical Evidence + Reusable Industrial Lessons** (what the community learns even if they never adopt your exact codebase).

### Law 3 — Dual-Track Experimental Proof (Production Telemetry + Standardized Public Benchmark)
A purely proprietary evaluation triggers *"does this generalize outside your schema?"*; a purely synthetic evaluation triggers *"why is this in the Industrial Track?"*. Accepted SIGMOD Industrial papers pair **both**:
- **Track A (Real Industrial Grounding)**: Live multi-month operational telemetry (drifts caught, queries audited, latency/cost curves), real business verification suites grounded against ERP/production ground truth, and manual error audits exposing metrics that automated checks hide.
- **Track B (Authoritative Public Benchmark)**: Standard database benchmark (`TPC-DS`, `TPC-H`, `TPC-DI`, `DSB`, `BIRD`, `Spider`) demonstrating that the exact algorithms, overheads, and failure patterns hold on public schemas independent of proprietary business quirks.
- **Model / Baseline Breadth**: When evaluating LLM-assisted database systems, cover **both domestic and international frontier/open models** (never a single model), include realistic competitive baselines (e.g., Direct-SQL + Prompt-Glossary), and isolate every mechanism via strict orthogonal ablation.

### Law 4 — Explicit Hypothesis-to-Takeaway Traceability
Every experimental subsection must explicitly state:
1. **RQ / Hypothesis**: What concrete systems claim is being tested?
2. **Metric & Fair Protocol**: Exact dataset, seed, model set, and why the evaluation is fair to baselines (e.g., manual verbatim audit, zero truncation bias, handling API refusals fairly).
3. **Industrial Takeaway**: One bold sentence explaining what practitioners should change in their own systems based on this result.

### Law 5 — Honest Operating Regimes & Non-Trivial Lessons Learned
SIGMOD Industrial reviewers actively penalize hype ("wins everywhere"). Credibility spikes when you dedicate explicit space to:
- **Operating Regimes**: Exactly where lightweight baselines (e.g., Prompt-Glossary on $\le 10$ static exploratory tables) *suffice and win on setup cost*, versus the exact failure threshold where your deterministic engine becomes indispensable.
- **Operational Experience & Lessons Learned** (cf. Databricks `Enzyme` Sec. 5): 4–5 sharp, surprising, counter-intuitive lessons backed by real incident data (not generic advice like "testing is important").

### Law 6 — Visual & Narrative Coherence
- Pair architectural prose with a single crisp end-to-end running example traced from raw input to compiled SQL/plan.
- Ensure all figures follow SIGMOD publication craft (see companion skill `sigmod-industrial-figure-craft`): unified restrained palette, vector DB primitives, zero line-box crossings, and direct data alignment with frozen JSON logs.

---

## 10-Dimension SIGMOD Industrial Acceptance-Bar Review Rubric

Score any draft from `1` (Reject) to `5` (Strong Accept) on each dimension before submission:

| # | Dimension | Reject Signal (1–2) | Strong Accept Bar (4–5) |
|---|---|---|---|
| 1 | **Industrial Pain Point Authenticity** | Toy/synthetic motivation | Quantified real production failures (silent errors, drifts, cost) |
| 2 | **Thesis Abstraction (立意)** | "We built an internal company platform" | Generalizable database systems principle + clear positioning table |
| 3 | **Contribution Depth (含金量)** | Feature list / LOC / UI screenshots | Formal algorithms + explicit soundness/invariant guarantees |
| 4 | **Design Trade-Off Rigor** | Only happy path described | Explicit failure modes, quarantine/refusal paths, scope boundaries |
| 5 | **Production Evidence** | Only offline unit tests | Multi-month live telemetry, real drift counts, ERP/ground-truth audit |
| 6 | **Public Benchmark Generality** | Enterprise-only proprietary data | Standardized public benchmark (`TPC-DS`/`TPC-H`/`BIRD`) confirming claims |
| 7 | **Baseline & Model Breadth** | 1 weak baseline or 1 LLM | Competitive baselines + multi-model (Intl + Domestic) + orthogonal ablation |
| 8 | **Deployment Honesty** | Vague or overstated prod claims | Crystal-clear UAT vs. pilot vs. prod boundary; honest audit gaps |
| 9 | **Lessons Learned Value** | Generic engineering platitudes | 4–5 surprising, incident-backed lessons reusable across companies |
| 10 | **Presentation & Page Discipline** | Dense wall of text, rainbow boxes | Running example, clean SIGMOD figures, exact ≤12p body compliance |

**Verdict Gate**: Zero dimensions $\le 2$; at least 7/10 dimensions $\ge 4$; every Gap at `3` must have a documented mitigation before submission.
