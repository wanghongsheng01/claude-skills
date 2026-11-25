# Visual Dissection & Comparison: Published SIGMOD vs. PVLDB Figures (2024–2027)

Synthesized from 13 published papers across ACM SIGMOD (`WAIR` '26, `Enzyme` '26 Ind, `AlayaDB` '25 Ind, `Measures in SQL` '24 Ind, `FinSQL` '24 Ind, `Data-Juicer` '24, `DIVER` '26, `SALUS` '27) and PVLDB (`LOTUS` '25, `DocETL` '25, `FlockMTL` '25, `DAIL-SQL` '24).

---

## 1. Figure Archetype Matrix

| Figure Slot | SIGMOD Industrial Best Practice | PVLDB Research Best Practice | Critical Upgrade Rule |
|---|---|---|---|
| **Fig. 1: System / Operator Overview** | Asymmetric Offline Governance Plane $\to$ Immutable Snapshot Fence $\to$ Spotlighted Online Execution Core $\to$ Closed-Loop Audit (`FinSQL` '24, `AlayaDB` '25). | Concrete input tuple/doc trace $\to$ Algebraic Operators ($\pi^{\text{sem}}, \bowtie_{\text{asof}}, \sqcup$) $\to$ Grounded relational output (`LOTUS` '25, `DocETL` '25). | Zero port numbers (`4444`, `7211`); include concrete running example + dual-track step badges + explicit Pass vs. Quarantine outcomes. |
| **Fig. 2: Production Evolution / Multi-Model Dual Benchmark** | Multi-month operational trajectory + Accuracy-Latency/Cost Pareto (`Enzyme` '26, `WAIR` '26). | Dual-Dataset (`Public` vs. `Enterprise`) $\times$ Multi-Model grouped comparison (`LOTUS` '25, `DAIL-SQL` '24). | **Zero `International` / `Domestic` banners or dividers**; order models cleanly by baseline score or consistent model-family sequence; annotate exact gains (`+73.6 pp`). |
| **Fig. 3: Scaling, Latency & Theoretical Bound Validation** | **3-panel `figure*`**: (a) Path latency distribution, (b) **Estate-scale sweep (`36` $\to$ `1,599` tables) vs. unscoped baseline**, (c) End-to-end log-scale breakdown (`AlayaDB` '25, `WAIR` '26). | **Multi-panel Triage & Sample-Size Sensitivity**: (a–b) Defect recall vs. budget $q$, (c) **Sample-size crossover $N^*$ (`20` $\to$ `640`) confirming EB theory** (`LOTUS` '25). | Every analytical paper needs at least one **continuous scaling or sensitivity curve** overlaid with its theoretical regime boundary! |
| **Fig. 4: Cross-Model Safety / Operator Overhead** | Dual-Warehouse (`Enterprise` vs. `Public TPC-DS`) 6-Model Safety & Trap Breakdown (`FinSQL` '24). | Temporal `As-Of` Join Scaling ($10^3 \to 10^6$ versions) + Operator Latency Share (`<0.05%` vs. LLM API). | Full `figure*` width (`7.0–7.1 in`) when showing $\ge 6$ models side-by-side so labels never crowd or rotate awkwardly past $25^\circ$. |

---

## 2. Typography, Palette & Spacing Specifications

- **Target Canvas Sizes**:
  - Full-width `figure*`: `width = 7.05 in`, `height = 2.25–2.65 in` (`dpi=300` PNG preview + vector PDF with `pdf.fonttype = 42`, `ps.fonttype = 42`).
  - Single-column `figure`: `width = 3.35 in`, `height = 2.0–2.4 in`.
- **Colorblind-Safe Academic Palette**:
  - Hero / Primary Method: Deep Navy `#0B4F8C`
  - Certified / Pass / Secondary Curve: Teal `#0F766E`
  - Mid-Tier / Prompt Baseline / Warning: Warm Amber `#D97706`
  - Naive / Ungoverned Baseline / Violation: Vermilion `#C2410C`
  - Neutral / Reference / Infrastructure: Slate `#64748B`
- **Redundancy Encoding**: Pair every line series with distinct markers (`o`, `s`, `^`, `D`, `v`) and line styles (`-`, `--`, `-.`, `:`); pair bar series with subtle hatches (`///`, `...`, none) so monochrome printouts remain 100% legible.
