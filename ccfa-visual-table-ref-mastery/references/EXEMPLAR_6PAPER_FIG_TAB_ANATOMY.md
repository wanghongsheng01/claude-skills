# Six-Exemplar Figure, Table & Float-Proximity Anatomy (SIGMOD Industrial & PVLDB)

Reverse-engineered directly from the official published PDFs of:
- **SIGMOD Industrial (3)**: `FinSQL` (SIGMOD '24 Ind, 13 pp.), `AlayaDB` (SIGMOD '25 Ind, 14 pp.), `Enzyme` (SIGMOD '26 Ind, 14 pp.);
- **PVLDB Research (3)**: `DAIL-SQL` (PVLDB '24, 22 pp.), `LOTUS` (PVLDB '25, 14 pp.), `DocETL` (PVLDB '25, 22 pp.).

---

## 1. Figure Inventory & Design Secrets Across the 6 Exemplars

| Paper | Fig. 1 / Overview Architecture | Mechanism / Operator Sub-Figures | Experimental Plots | Float Proximity (`Δp`) |
|---|---|---|---|---|
| **`FinSQL` (SIGMOD '24 Ind)** | 3-column dark-header pipeline (`I Prompt Construction \| II LoRA Tuning \| III Output Calibration`) with **embedded mini schema graphs, SQL cards, and AST trees** + circled training (`①–⑦`) vs. squared inference (`1–3`) step badges. | Figs. 2–11: Data augmentation, parallel cross-encoder, weight merging, SQL calibration AST rewrites — every sub-module gets a concrete mini dataflow trace. | Figs. 12–13: Few-shot transfer bar/line charts placed on exact analysis page. | `Δp = 0` on 12/13 figures (`Δp = 1` on 1). |
| **`AlayaDB` (SIGMOD '25 Ind)** | Layered 3-tier engine stack (`User Interface -> Query Processing Engine -> Vector Storage Engine`) with **embedded Session/DB icons, Query/Index sub-cards, and Cached vs. Vector block arrays**. | Figs. 4–8: Sparse attention windowing, late materialization timeline, vector file block layout. | Figs. 9–12: Multi-context (`32K–256K`) throughput/latency curves & memory breakdown. | `Δp = 0` on 10/12 figures (`Δp = 1` on 2). |
| **`Enzyme` (SIGMOD '26 Ind)** | Medallion Bronze/Silver/Gold pipeline (Fig. 1) + concrete SQL running example MV card (Fig. 2). | Figs. 3–7: Query plan tree + **4-stage bottom-up delta plan composition (`ψ, ψ', Δψ`)** + normalization pipeline. | Figs. 8–10: Log-scale speedup grouped bars across 8 TPC-DI tables with rotated $30^\circ$ clean labels (`0` collisions). | `Δp = 0` on 9/10 figures (`Δp = 1` on 1). |
| **`LOTUS` (PVLDB '25)** | Concrete Python program card $\to$ **3-stage optimizer progression (`Logical Plan -> Unoptimized Gold Plan -> Optimized Plan with LM/sem_index operator pills`)** + speedup callout banner. | Figs. 3–5: Proxy-oracle cascade threshold diagram & `sem_join` vs. `sem_sim_join` tuple flow. | Figs. 6–9: Accuracy-vs.-Execution-Time scatter/Pareto frontiers (`gold` circle vs. `proxy` circle vs. `LOTUS` stars). | `Δp = 0` on 8/9 figures (`Δp = 1` on 1). |
| **`DocETL` (PVLDB '25)** | Concrete police-report document thumbnail $\to$ `User-Defined Map` $\to$ extracted records $\to$ **tree of candidate agentic plan rewrites (`Map->Map` vs. `Split->Gather->Map->Reduce`)** with key legend. | Figs. 2–4: Iterative batch scratchpad fold trace, `Split-Gather` context rendering modes, validation gleaning loop. | Fig. 5: Cost-vs.-F1 Pareto scatter across 30 synthesized plans. | `Δp = 0` on 5/6 figures (`Δp = 1` on 1). |
| **`DAIL-SQL` (PVLDB '24)** | Prompt representation comparison cards + skeleton-similarity selection flow. | Figs. 1–4: Full-width paired grouped bar charts with **green `↑` / red `↓` ablation delta arrows** directly on bars and generous `0.65 in` group spacing. | Figs. 5–12: Token-efficiency vs. execution accuracy trade-off curves across 4 LLMs. | `Δp = 0` on 10/12 figures (`Δp = 1` on 2). |

---

## 2. Table Inventory & `booktabs` Patterns Across the 6 Exemplars

1. **Zero Vertical Rules (`|`)**: Not a single experimental table in `FinSQL`, `LOTUS`, `DocETL`, or `DAIL-SQL` uses vertical `|` pipes across `\toprule/\midrule/\bottomrule`. Hierarchy is expressed strictly via `\toprule`, `\cmidrule(lr){a-b}`, `\midrule`, and `\bottomrule`.
2. **Footnote Explanations Below `\bottomrule`**: Nuances (such as infeasible baselines or 3-run averages in `LOTUS` Tables 3–6) appear in compact `\footnotesize` table notes right below `\bottomrule`, keeping column headers short (`<= 2` words per column!).
3. **Co-Location With Prose**: Tables are placed at `[t]` of the exact page whose left/right column reads `"Table X shows..."`, never stranded after *Related Work*!
