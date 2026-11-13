# 本轮精读论文清单（正式发表，已核验）

- **核验日：** 2026-11-12（America/Los_Angeles，PST）
- **入口：** PVLDB 官方 PDF（https://www.vldb.org/pvldb/volumes/{17,18,19} 及各篇官方链接）。全文用 `pdftotext` 通读首页、问题定义、方法/基准设计与摘要中的结果；结论页因 PDF 编码未全部自动切出，数字只采用摘要或正文已抽出的原句，不补写未见数字。
- **本轮目标：** 每类至少 5 篇代表作。后续补到 15–25 篇（含 ICDE、SIGMOD）。
- **不得把本清单写成已完成 15–25 篇。**

| # | 类型 | 题目 | 作者（第一/通信可见者） | 会刊 | 页码 | 年份 | DOI | 官方 PDF |
|---|---|---|---|---|---|---|---|---|
| M1 | B1-方法 | Sphinteract: Resolving Ambiguities in NL2SQL Through User Interaction | Zhao, Deep, Psallidas, Floratou, Agrawal, El Abbadi | PVLDB 18(4) | 1145–1158 | 2024 | [10.14778/3717755.3717772](https://doi.org/10.14778/3717755.3717772) | https://www.vldb.org/pvldb/vol18/p1145-zhao.pdf |
| M2 | B1-方法 | The Power of Constraints in Natural Language to SQL Translation (REDSQL) | Ren, Ke, Fan, Jing, He, Zhang, Wang | PVLDB 18(7) | 2097–2111 | 2025 | [10.14778/3734839.3734847](https://doi.org/10.14778/3734839.3734847) | https://www.vldb.org/pvldb/vol18/p2097-ren.pdf |
| M3 | B1-方法 | LLM-R2: A Large Language Model Enhanced Rule-based Rewrite System for Boosting Query Efficiency | Li, Yuan, Wang, Cong, Bing | PVLDB 18(1) | 53–65 | 2024 | [10.14778/3696435.3696440](https://doi.org/10.14778/3696435.3696440) | https://www.vldb.org/pvldb/vol18/p53-yuan.pdf |
| M4 | B1-方法 | Magneto: Combining Small and Large Language Models for Schema Matching | Liu, Pena, Santos, Wu, Freire | PVLDB 18(8) | 2681–2694 | 2025 | [10.14778/3742728.3742757](https://doi.org/10.14778/3742728.3742757) | https://www.vldb.org/pvldb/vol18/p2681-freire.pdf |
| M5 | B1-方法 | CHORUS: Foundation Models for Unified Data Discovery and Exploration | Kayali, Lykov, Fountalis, Vasiloglou, Olteanu, Suciu | PVLDB 17(8) | 2104–2114 | 2024 | [10.14778/3659437.3659461](https://doi.org/10.14778/3659437.3659461) | https://www.vldb.org/pvldb/vol17/p2104-kayali.pdf |
| M6 | B1-方法（增读） | OpenForge: Probabilistic Metadata Integration | Cong, Nargesian, Xing, Jagadish | PVLDB 18(9) | 2914–2927 | 2025 | [10.14778/3746405.3746417](https://doi.org/10.14778/3746405.3746417) | https://www.vldb.org/pvldb/vol18/p2914-cong.pdf |
| B1 | B1-基准 | The Dawn of Natural Language to SQL: Are We Fully Ready? | Li, Luo, Chai, Li, Tang | PVLDB 17(11) | 3318–3331 | 2024 | [10.14778/3681954.3682003](https://doi.org/10.14778/3681954.3682003) | https://www.vldb.org/pvldb/vol17/p3318-luo.pdf |
| B2 | B1-基准（亦方法边界） | Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation (DAIL-SQL) | Gao, Wang, Qian, Li, Ding, Sun, Zhou | PVLDB 17(5) | 1132–1145 | 2024 | [10.14778/3641204.3641221](https://doi.org/10.14778/3641204.3641221) | https://www.vldb.org/pvldb/vol17/p1132-gao.pdf |
| B3 | B1-基准（设定新） | TACO: A Benchmark for Open-Domain Text-to-SQL with Ambiguous and Cross-Database Queries | Deng, Fan, Luo 等 | PVLDB 19(6) | 1386–1399 | 2026 | [10.14778/3797919.3797942](https://doi.org/10.14778/3797919.3797942) | https://www.vldb.org/pvldb/vol19/p1386-fan.pdf |
| B4 | B1-基准（新系统类） | SemBench: A Benchmark for Semantic Query Processing Engines | Lao, Zimmerer, …, Trummer | PVLDB 19(8) | 1754–1767 | 2026 | [10.14778/3811243.3811249](https://doi.org/10.14778/3811243.3811249) | https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf |
| B5 | B1-基准 | Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards | Jin, Choi, Zhu, Kang | PVLDB 19(5) | 931–944 | 2026 | [10.14778/3796195.3796206](https://doi.org/10.14778/3796195.3796206) | https://www.vldb.org/pvldb/vol19/p931-jin.pdf |
| B6 | B1-基准（增读） | NL2SQLBench: A Modular Benchmarking Framework for LLM-Enabled NL2SQL Solutions | Hou, Pei, Chen, Ta, Lu, Ooi | PVLDB 19(5) | 1001–1015 | 2026 | [10.14778/3796195.3796211](https://doi.org/10.14778/3796195.3796211) | https://www.vldb.org/pvldb/vol19/p1001-hou.pdf |
| B7 | B1-基准（增读） | Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting | Hu, Miao | PVLDB 19(11) | 3772–3785 | 2026 | [10.14778/3836663.3836724](https://doi.org/10.14778/3836663.3836724) | https://www.vldb.org/pvldb/vol19/p3772-miao.pdf |
| B8 | B1-基准（增读；亦 B2 任务论证） | ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines | Jin, Zhu, Kang | PVLDB 19(2) | 84–98 | 2025 | [10.14778/3773749.3773750](https://doi.org/10.14778/3773749.3773750) | https://www.vldb.org/pvldb/vol19/p84-jin.pdf |
| P1 | B2（新对象） | spade: Synthesizing Data Quality Assertions for Large Language Model Pipelines | Shankar, Li, Asawa, …, Parameswaran, Wu | PVLDB 17(12) | 4173–4186 | 2024 | [10.14778/3685800.3685835](https://doi.org/10.14778/3685800.3685835) | https://www.vldb.org/pvldb/vol17/p4173-shankar.pdf |
| P2 | B2（新抽象；8 页短文） | Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems | Lee, Chan, Fu, Kim, Mehta, Raghavan, Çetintemel | PVLDB 18(11) | 4073–4080 | 2025 | [10.14778/3749646.3749677](https://doi.org/10.14778/3749646.3749677) | https://www.vldb.org/pvldb/vol18/p4073-lee.pdf |
| P3 | B2（新系统类的定义，正文为基准） | SemBench（同上 B4） | Lao 等 | PVLDB 19(8) | 1754–1767 | 2026 | 同上 | 同上 |
| P4 | B2（新设定的论证，正文为基准） | TACO（同上 B3） | Deng, Fan 等 | PVLDB 19(6) | 1386–1399 | 2026 | 同上 | 同上 |
| P5 | B2（新端到端任务的论证，正文为基准） | ELT-Bench（同上 B8） | Jin, Zhu, Kang | PVLDB 19(2) | 84–98 | 2025 | 同上 | 同上 |

**计数（不重复篇）：** 独立正式发表论文 **16 篇**。按「本轮每类至少 5 篇代表作」：B1-方法 5+1，B1-基准 5+3，B2 5（其中 3 篇与基准清单交叉，已在 skill 中写明交叉用途，不把同一篇算成两类「各 5 篇新文章」的凑数）。

**尚待补读（不假装已读）：** ICDE 2023–2026、SIGMOD 2023–2026 的同类全文；查询等价方面的 SQLSolver（SIGMOD 2023）、VeriEQL（SIGMOD 研究全文，PVLDB 17 仅有 4 页 Demonstration）；访问控制与结果缓存方面的 Membrane（PVLDB 17）、ContextCache（PVLDB 18 Demo）等——后者在 09 补课缺口中列出，本轮未做全文精读卡片。
