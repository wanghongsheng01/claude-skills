# Empirical Dissection of Published ACM SIGMOD Industrial & Systems Papers (2024–2027)

This reference summarizes direct structural analysis of eight peer-reviewed SIGMOD papers (2024–2027) inspected to calibrate the `sigmod-industrial-acceptance-craft` rubric.

## 1. Corpus Overview

| Paper | Venue | Affiliation | Core Systems Abstraction | Formal Depth | Evaluation Pairing |
|---|---|---|---|---|---|
| **FinSQL** | SIGMOD '24 Ind | Zhejiang Univ. + Hundsun | Model-agnostic financial Text-to-SQL (PEFT + Parallel Schema Linking + Output Calibration) | 2 Algorithms, problem formulation | Proprietary financial benchmark (`BULL`, released) + cross-DB transfer + multi-model |
| **Data-Juicer** | SIGMOD '24 Ind | Alibaba Group | Standardized composable operator pool + feedback-driven data recipe optimization | Unified data repr., 50+ operators | Downstream LLM quality gains (+7.45%) + distributed execution throughput |
| **Measures in SQL** | SIGMOD '24 Ind | Google Inc. (Looker) | Context-Sensitive Expressions (CSEs) elevating BI measures into SQL semantics | Formal lambda & evaluation-context semantics | Expressiveness proofs, join/self-join equivalence, Looker Open SQL + NL2SQL |
| **AlayaDB** | SIGMOD '25 Ind | HKBU / NTU / Industry | Decoupling KV cache & sparse attention into a vector DB (`DIPR` query) | 12 Defs/Propositions, 3 Algorithms, 4-way taxonomy table | Multi-LLM long-context benchmarks + ablation + memory/TTFT latency |
| **Enzyme** | SIGMOD '26 Ind | Databricks + Google | Cost-based multi-MV Incremental View Maintenance + transactional provenance over Spark/Delta | Operator-level delta plans, `MERGE INTO`/`REPLACE WHERE` | Standardized `TPC-DI` benchmark + thousands of live Databricks production pipelines + RQG & A/B verification |
| **DIVER** | SIGMOD '26 | BUPT / Industry | Dynamic interactive value linking + CoTF evidence workspace for evidence-free Text-to-SQL | Structured multi-agent workspace | 4 public benchmarks (`BIRD`, `Spider`, `DR.Spider`, `Spider-DK`) + ablation + dedicated Sec. 7 Error Analysis |
| **WAIR** | SIGMOD '26 | Tsinghua / CMU | Policy-key decoupled incremental reclustering via boundary micro-partitions | 5 Algorithms, 6 Defs/Theorems (cost upper bound) | Public `TPC-H` + `DSB` + real-world production workload `Mirrors` |
| **SALUS** | SIGMOD '27 | UC Irvine / Cornell | Weakly supervised multi-agent automated auditing of NL-to-SQL benchmark errors | Weak-supervision vote matrix | Cross-benchmark audit (`BIRD`, `Spider`) exposing hidden annotation error rates |

## 2. Structural Patterns Distinguishing Accepted SIGMOD Industrial Papers

### A. Opening & Positioning (Pages 1–3)
- **Hook with a quantified industrial failure mode**, not a vague trend ("LLMs are popular").
- **Positioning Taxonomy (AlayaDB Table 1 / Fig. 2 pattern)**: Classify existing approaches into 3 clear paradigms and show in a compact table *which exact invariants each paradigm fails*.
- **Contributions List (3–4 bullets)**: Never brag about LOC or UI widgets as contributions. Frame every bullet around a **reusable database abstraction, algorithm/invariant, verification primitive, and empirical finding**.

### B. Technical Core (Pages 3–7)
- **Worked Running Example**: Concrete end-to-end trace showing a naive failure versus the system's governed execution (prevents abstract hand-waving).
- **Explicit Invariants / Soundness Properties**: Even in Industrial Track papers (where full asymptotic proofs are optional), stating 2–3 crisp **Soundness / Safety Properties** guaranteed by construction of your algorithms dramatically elevates perceived academic rigor (`Measures in SQL`, `AlayaDB`, `Enzyme`, `WAIR`).
- **Closed-Loop Correctness**: Industrial reviewers know metadata and pipelines drift. Highlighting automated correctness verification (`Enzyme` Sec. 5 RQG + A/B production checks; transactional provenance) directly earns trust.

### C. Experimental Section (Pages 7–10)
1. **Standardized Public Benchmark** (`TPC-DI`, `TPC-H`, `DSB`, `TPC-DS`, `BIRD`): Proves claims hold without proprietary schema assumptions.
2. **Real Industrial Workload & Live Telemetry**: Multi-month production/UAT logs, real ground-truth reconciliation (e.g., ERP audit), and latency/cost breakdown.
3. **Competitive Baselines + Model Breadth**: Compare against strong practical baselines (e.g., Prompt-Glossary, commercial/open models across both international and domestic providers) and perform strict per-component ablation.
4. **Honest Error Analysis & Operating Regimes**: Quantify residual gaps (e.g., manual audit vs. automated pass rate) and explicitly define when simpler baselines suffice.

### D. Operational Experience & Lessons Learned (Page 10–11)
- Dedicated section (`Enzyme` Sec. 5) with 4–5 concrete, surprising operational lessons tied to measured incidents and explicit architectural scope boundaries.
