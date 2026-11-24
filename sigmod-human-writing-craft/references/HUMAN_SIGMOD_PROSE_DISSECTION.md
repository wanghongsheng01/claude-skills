# Reverse-Engineered Prose & Structure Dissection of Published Human SIGMOD Industrial Papers (2024–2026)

Direct quantitative and paragraph-move analysis of five human-authored ACM SIGMOD Industrial Track papers inspected to build `sigmod-human-writing-craft`.

## 1. Quantitative Stylometric Benchmark

| Published Paper (SIGMOD Industrial) | Body Words | Mean Sent. Len (SD) | Em-Dashes / 1K | Colons / 1K | AI-Tic / 1K |
|---|---:|---:|---:|---:|---:|
| **Measures in SQL** (Google, SIGMOD '24) | 7,988 | 23.3 (13.5) | 1.38 | 6.6 | **0.88** |
| **Enzyme** (Databricks + Google, SIGMOD '26) | 9,467 | 21.8 (9.1) | 2.32 | 5.0 | 3.27 |
| **FinSQL** (ZJU + Hundsun, SIGMOD '24) | 9,617 | 21.3 (11.0) | 0.00 | 6.3 | 3.43 |
| **AlayaDB** (HKBU/NTU/Ind., SIGMOD '25) | 10,617 | 21.2 (11.3) | 0.28 | 6.5 | 2.92 |
| **Data-Juicer** (Alibaba, SIGMOD '24) | 10,210 | 23.4 (11.3) | 0.10 | 6.0 | 4.31 |
| **Human 5-Paper Average** | **9,580** | **22.2 (11.2)** | **0.82** | **6.1** | **2.96** |

*Note*: Across all 5 human papers, **0** used mechanical `\noindent\textbf{Takeaway (RQk).}` stamps and **0** addressed "reviewers" inside body prose.

## 2. Section Page-Budget Proportions (12-Page SIGMOD Industrial Norm)

| Section Role | `AlayaDB` (12p body) | `FinSQL` (12p body) | `Enzyme` (12p body) | Recommended Target |
|---|---:|---:|---:|---:|
| Abstract + Introduction | 12.5% | 20.8% | 15.0% | **14% – 18%** |
| Background / Motivation / Context | 25.0% | 12.5% | 12.5% | **12% – 16%** |
| Core System Design, Algorithms & Serving | 37.5% | 41.7% | 42.0% | **36% – 44%** |
| Experimental Evaluation | 16.7% | 16.7% | 20.0% | **20% – 27%** |
| Operational Lessons + Related + Conclusion | 8.3% | 8.3% | 10.5% | **10% – 14%** |

## 3. Verbatim Human Paragraph Craft Exemplars

### A. Opening with Plain Tension & Rhetorical Clarity (Julian Hyde, *Measures in SQL*, SIGMOD '24)
> *"About thirty years ago the first Business Intelligence (BI) tools were introduced. They had a semantic model based on the multidimensional model, and good support for data exploration and visualizations. Since then, the SQL language has expanded immeasurably in its capabilities... An increasing proportion of business data resides in powerful cloud SQL engines. But today's BI tools continue to use semantic models based on the multidimensional model. Why?"*
- **Why it reads 100% human**: Short declarative opener (11 words), historical contrast, plain `"But..."`, 1-word question (`Why?`), zero em-dashes, zero buzzwords.

### B. Mechanistic Experimental Analysis Without Bullet Walls (Databricks, *Enzyme*, SIGMOD '26, Sec. 6.2.1)
> *"Prospect performs poorly under incremental refresh because a large fraction of the dataset is updated in each batch. The column SK_RecordDateID represents the most recent date a prospective customer appears in the input. Since more than 95% of prospects persist across batches, nearly all rows in the dataset are rewritten during each refresh to update this column. In such cases, identifying and applying fine-grained row-level updates incurs more overhead than simply performing a full table refresh."*
- **Why it reads 100% human**: Names the exact failure case first (honesty!), traces the exact column and physical cause (95% row churn), and states the engineering conclusion in plain active prose without bold labels or exclamation hype.

### C. Causal Comparison Analysis (*AlayaDB*, SIGMOD '25, Sec. 9.1)
> *"By analyzing the breakdown of latency of LMCache and AlayaDB in Figure 10(b), LMCache suffers from the slow KV cache loading, including decompressing and transferring from CPU to GPU. The loading time increases linearly with the context length. Instead of loading the KV cache, AlayaDB can directly decode on the offloaded KV cache..."*
- **Why it reads 100% human**: Links the figure directly to the underlying physical bottleneck, uses simple sequential logic, and keeps sentences crisp (10–25 words).
