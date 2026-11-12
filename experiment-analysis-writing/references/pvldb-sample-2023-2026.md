# PVLDB sample (Vol. 17–19) used for experiment-analysis-writing

Read on 2026-11-12 from official open-access PDFs at vldb.org. This file records *what was studied and which habit was taken*; it is not a substitute for reading the PDF and does not reproduce body text.

| Paper | Vol. | PDF | Direction | Habit taken |
|---|---|---|---|---|
| Gao et al., Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation (DAIL-SQL) | 17 | https://www.vldb.org/pvldb/vol17/p1132-gao.pdf | NL2SQL EA-style | Ablation figures with explicit increase/decrease marks; "best performances … in bold"; fair-protocol sentence ("we follow prior study [X] to use EM and EX") |
| Luo et al., The Dawn of Natural Language to SQL: Are We Fully Ready? [EA&B] | 17 | https://www.vldb.org/pvldb/vol17/p3318-luo.pdf | NL2SQL EA&B | Question-titled RQs ("Are LLM-based Models the Clear Winner?"); split EX vs EM rather than a blanket win; closing "research opportunities" (ambiguity, trustworthiness, cost) |
| Arora et al., Language Models Enable Simple Systems for Generating Structured Views… (Evaporate) | 17 | https://www.vldb.org/pvldb/vol17/p92-arora.pdf | LLM structured views | Honest quality loss (Code worse than Direct on F1) + numeric cost–quality crossover |
| Zeng et al., An Empirical Evaluation of Columnar Storage Formats | 17 | https://www.vldb.org/pvldb/vol17/p148-zeng.pdf | EA&B / formats | Numbered Lessons with "because" and a measurable regime ("when NDV > 0.1, dictionary encoding becomes less effective") |
| Zhao et al., Sphinteract: Resolving Ambiguities in NL2SQL Through User Interaction | 18 | https://www.vldb.org/pvldb/vol18/p1145-zhao.pdf | NL2SQL ambiguity | "This is because" after a numeric comparison; simple vs clarification feedback |
| Ren et al., The Power of Constraints in Natural Language to SQL Translation (REDSQL) | 18 | https://www.vldb.org/pvldb/vol18/p2097-ren.pdf | NL2SQL constraints | Accuracy–cost trade-off figure; "we attribute this difference to…"; ablation + multiple LLM backbones |
| Gao et al. / Liu et al., Maximum k-Plex Search: An Alternated Reduction-and-Bound Method | 18 | https://www.vldb.org/pvldb/vol18/p363-liu.pdf | k-plex | Certificate-adjacent graph algorithm: compare on time with a named RB method; keep competitive baselines |
| Ahmad et al., Maximum k-Plex Finding: Choices of Pruning Techniques Matter! | 18 | https://www.vldb.org/pvldb/vol18/p2928-ahmad.pdf | k-plex EA-style | Reports when a technique *hurts* (small k vs large k); calls out unreported negative results — model for honest second-place analysis |
| Fan et al., TACO: A Benchmark for Open-Domain Text-to-SQL with Ambiguous and Cross-Database Queries | 19 | https://www.vldb.org/pvldb/vol19/p1386-fan.pdf | NL2SQL benchmark + ambiguity | Benchmark-first structure; human check of synthetic pairs; baselines under a new protocol |
| Trummer / Lao et al., SemBench: A Benchmark for Semantic Query Processing Engines | 19 | https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf | Semantic query EA&B | Pre-declared significance rule; cost–quality trade-off (prompt length, pre-filtering misses matches); strengths and weaknesses in the contribution list |
| Jin et al., Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards | 19 | https://www.vldb.org/pvldb/vol19/p931-jin.pdf | Benchmark critique | "Why does EX of X increase?" instance-level analysis; ranking changes after gold fixes |
| Hu & Miao, Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting | 19 | https://www.vldb.org/pvldb/vol19/p3772-miao.pdf | MV / caching | "Best X varies by workload"; failure-case figure; **workload-feature → method-choice** decision table — the model for "when to choose ours vs theirs" |

Advisor meetings used for the same skill (topic selection and analysis emphasis, not as a substitute for the CFP): 邓老师 × 王宏升 ICDE 评审（从五篇里挑最好的两三篇；重叠稿不要同会；表要标最优/次优；输给基线必须写分析和 takeaway）；邓老师 × Magii 图评审（caption 压到 1–2 行，不在图注重复正文数字；架构图标清自己的贡献与上游）。

EA&B official rules (Vol. 20): full reproducibility package at *initial* submission; title suffix `[Experiment, Analysis & Benchmark]` in PDF and CMT. https://www.vldb.org/2027/submission-guidelines.html
