# 参考文献与引用规范（REFERENCE_PRINCIPLES）

> 版本 r1，2026-11-14（America/Los_Angeles）。作用：所有 CCF-A 投稿（PVLDB / SIGMOD 研究与工业轨道 / ICDE / ACL 系）在交付前都用本文件和 `reflint.py` 审一遍参考文献与引用；审稿人和修改人不能是同一个 agent。
> 证据：56 篇 2024–2026 已录用论文的 PDF 实测（4 页 demo 论文已剔除），逐篇表见 `references/corpus_table.md`，测量脚本见 `scripts/refcorpus_stats.py`（配合 `scripts/pdf2cols.py` 按栏抽取 PDF 文本）。

## 0. 样本与测量方法

| 类型 | 篇数 | 构成 |
|---|---|---|
| 方法（method） | 30 | PVLDB 17/18 方法论文 12 篇（Sphinteract、REDSQL、OmniSQL、EvoSchema、R-Bot、LLM-R2、UniClean、Long-Context NL2SQL、SLM+LLM NL2SQL、DocETL、SPADE、增量 DC 检测）；SIGMOD 2026/27 论文 7 篇（DIVER、增量重聚簇、SALUS、CADENZA、FlowPipe、RAG 查询规划、实体匹配 RAG）；ICDE 2026 论文 6 篇（Nezha、Living Databases、Text2SQL 评估器、CactusDB、图查询生成、数据校验错误）；ACL 系 5 篇（EMNLP 2024 PTD-SQL、EMNLP 2025 LinkAlign、NAACL 2025 MSc-SQL 与 Track-SQL、ACL 2026 SDE-SQL） |
| 基准 / EA&B | 13 | PVLDB：DAIL-SQL 评测、SQLStorm、ScienceBenchmark、Dawn of NL2SQL、LakeBench、UDFBench、PBench、Shades of Null；SIGMOD 2027：RBAC Text-to-SQL、InferQ；ICDE 2027：RDL-Bench、CDC chunking、WPBench |
| 工业 | 13 | PVLDB 工业轨道（Redshift fleet、ByteDance Spark、TDSQL、Databricks AQE、Apple Iceberg 行级操作、Meta Scribe、SiriusBI、CI/CD for pipelines、Snowflake workload、AnalyticDB-PG、Streaming View、在线实验指标计算）+ SIGMOD 2026 工业 Enzyme |

测量：PyMuPDF 按栏读取正文；参考文献数 = 文末 `[1..N]` 编号（ACL 系按作者-年份条目计数）；按一级标题把正文切成引言 / 相关工作 / 背景 / 方法 / 实验，数 `[..]` 引用括号次数。"近 3 年" = 出版年份 ≥ 论文年份−2。arXiv 版本可能比会议正式版多出附录，但参考文献表一般相同；有数字的地方都是实测值，不是估计值。自引用比例用作者姓氏匹配，是上界（中文常见姓氏会被误配）。

## 1. 实测规范（中位数 [P25, P75]）

| 指标 | 方法 | 基准 / EA&B | 工业 |
|---|---|---|---|
| 参考文献条数 | **51.5** [41, 64] | **57** [45.5, 75.5] | **47** [35.5, 60.5] |
| 正文引用括号总次数 | 60 [50, 74] | 71 [52, 116] | 52 [29.5, 67.5] |
| 引言引用次数 | 12.5 [9, 16.5] | 16 [11.5, 22.5] | 11 [3, 17] |
| 相关工作引用次数 | 16.5 [11.5, 25] | 12 [0, 26]（部分基准论文把相关工作并入背景） | 15 [7.5, 22] |
| 方法 / 设计章节引用次数 | 9 [2, 18] | 28 [9.5, 46.5]（基准构造章节大量引用数据源） | 10 [7, 25.5] |
| 实验章节引用次数 | 13 [7.75, 27.5] | 10 [3.5, 19.5] | 1 [0, 4.5] |
| 每个相关工作段落的引用次数 | 3.6 [2.2, 5.6] | 4.5 [3, 6] | 5 [2.6, 7.5] |
| 近 3 年文献占比 | 57% [43%, 70%] | 42% [26%, 67%] | 32% [22%, 45%] |
| 10 年以上经典文献占比 | 6% [3%, 19%] | 19% [7%, 23%] | 32% [16%, 43%] |
| 同行评审出版物占比 | 61% [47%, 70%] | 57% [50%, 69%] | 74% [48%, 79%] |
| 仅 arXiv 占比 | 13% [4%, 24%] | 14% [6%, 21%] | **0%** [0%, 1%] |
| 网页 / 软件文档占比 | 7% [0%, 13%] | 11% [9%, 20%] | 11% [4%, 17%] |
| 组合引用 [3,7,12] 占全部引用括号 | 22% [8%, 31%] | 22% [6%, 29%] | 16% [12%, 27%] |
| 未被正文引用的条目 | 0 [0, 1] | 0 [0, 2.5] | 0 [0, 0] |
| 图表标题（caption）中的引用 | 4 / 328 | 1 / 199 | 0 / 167 |
| 自引用（上界） | 全样本中位数 12.5% [3%, 27.5%] | | |

全样本：参考文献条数中位数 52 [42, 63.5]，最少 19 篇（9 页的工业短文），最多 116 篇。56 篇里只有 4 篇少于 30 篇：一篇 9 页的工业短文、两篇主题很窄的 ICDE/SIGMOD 论文（21 篇）、一篇 PVLDB 增量约束检测论文（21 篇）。**没有任何一篇已录用的 12 页研究论文只有 15 篇参考文献。**

先前的 n=21 小样本（`pvldb-paper-craft` 附录）得到：方法论文中位数 50、EA&B 60、工业 41，与本次结果一致。

## 2. 红线（违反一条 = BLOCKER，交付前必须清零）

R1. **数量下限。** 印出来的参考文献少于本类型 P25，即判 BLOCKER：方法 41、基准/EA&B 45、工业 35。目标值是中位数（约 50 / 57 / 47）。只能靠"正文确实依赖、却没有引用的工作"补齐，不准凑数。PVLDB Vol. 20 与 SIGMOD 2027 工业轨道的参考文献都不计入 12 页正文，补文献不会挤占篇幅（见 `submit-pvldb`、`submit-sigmod`）。

R2. **每个外部基线、数据集、基准、指标、工具、模型，在第一次出现的句子里就要带引用。** 证据：OmniSQL（PVLDB 18）的基线段落把 GPT-4o-mini [55]、DeepSeek-V3 [10]、Qwen2.5 [81]、Starcoder2 [49] 等每个模型都单独引用；Sphinteract 写的是"DAIL-SQL [18] … CHESS [50]"；EvoSchema 写的是"in-context learning [10] … CHESS [28]"；RBAC Text-to-SQL（SIGMOD 2027）连工具也引用了，写作"SQLGlot [32]""execution accuracy [53]"。在本样本里，DIN-SQL、MAC-SQL、CHESS、RESDSQL、Delta Lake、Iceberg 这类方法和系统名，在提到它们的论文里有 75%–100% 在前三次出现内就带了引用。PostgreSQL、DuckDB、TPC-H 这类通用工具不引用的情况较多（14%–45%），所以工具首次出现不引用只判 MINOR，**基线、数据集、对比方法首次出现不引用判 MAJOR**。凡是进入主表的行，都必须能在参考文献里找到对应条目，本文自己的系统和消融变体除外。

R3. **相关工作里每一句关于他人工作的论断都要有引用；没有一个引用的相关工作段落直接判 MAJOR。** 实测每段平均 3.6–5 次引用。段落结构固定为三步：主题句，然后点名并引用 3–6 个代表工作（逐个说明它做了什么），最后一句写本文和它们的差异。例：Sphinteract 的"NL2SQL has been an active area … dating back to 1980s [20, 56]. … As noted in study [33], rule based methods [41, 47] were popular before 2010s"。

R4. **本文作者同期在审、已投或计划投稿的相关工作，必须写进参考文献表，并标注"under submission"**（PVLDB Vol. 20 的 Self-Declaration of Related Submissions 要求，见 `submit-pvldb` 第 95 行）。正文提到同作者的姊妹稿、ICDE 稿或基准稿却不引用，就是 BLOCKER。按 PVLDB 单盲规则，可以写作者、标题和"under submission to PVLDB 2027"，不必写投稿号。

R5. **不准出现未核实或幻觉条目。** 每一条都必须能在 DBLP、Crossref、出版社页面、ACL Anthology、OpenReview 或官方文档之一查到；标题、作者、会议、年份和页码以这些记录为准。`reflint.py --online` 标为 unverified 或 mismatch 的条目，只能二选一：人工核实后修正，或者删掉。会议名写错（例如把 VLDB 2006 的"The Making of TPC-DS"写成 SIGMOD）判 MAJOR。DOI 指向别的论文判 BLOCKER。

R6. **已有正式版本的工作不准再引 arXiv 版。** 只有必须引用扩展版里的特定内容时才保留 arXiv，并在正文说明。证据：工业论文的 arXiv 占比中位数是 0%；方法论文的 arXiv 引用集中在没有正式版本的最新 LLM 技术报告上。

R7. **不准印出未被正文引用的条目**（禁止 `\nocite{*}`），也不准有引用了却在 .bib 里找不到、印成 [?] 的键。样本中未引用条目的中位数是 0。

R8. **不准把核实备注留在 .bib 的 `note` 字段里**，例如"verified from …"。它会被原样印进参考文献表。

## 3. 风格规则（MAJOR / MINOR，按证据强弱分级）

S1. **把引用分散到用到它的地方，不要堆在相关工作里。** 已录用的方法论文里，引言约 12 次、实验约 13 次、方法约 9 次，相关工作约 17 次，只占全部引用的 30% 左右。如果一篇稿子的引言少于 P25 的一半，或者方法论文的实验章节少于 P25 的一半，判 MAJOR。引言里每一句"现有系统 / 工业实践 / 已知问题"都要有引用。实验 setup 里每个数据集、基线、指标、引擎和工具都要有引用。

S2. **组合引用只用于同一个论断。** 实测组合引用占 16%–22%，而且通常是 2–4 篇。如果一个括号里有 6 篇以上（`[3–12]`），判 MINOR：应该拆开，逐个说明每篇做了什么。如果参考文献条数是引用括号数的 1.6 倍以上，说明大量文献只是成批引用一次，也判 MINOR。

S3. **图表标题（caption）不放引用。** 694 个 caption 里只有 5 个带引用。需要说明来源时，写在正文里第一次提到该图表的那一句。表格单元格里可以给对比工作加引用，例如 EvoSchema 的对比表写作"Spider [2] Rename ✗ ✓"，相关对比表允许这样做。

S4. **新旧要搭配。** 方法论文要覆盖近 3 年的 SOTA（中位数 57%）；如果近 3 年文献占比低于 20%，判 MINOR。工业论文要引用奠基系统和经典工作（10 年以上的占 32%），但同时要有近 3 年的同类工业系统。

S5. **以同行评审的出版物为主。** 网页、软件文档的占比超过 25%，判 MINOR。软件文档用 `@misc`，写全称、版本号或访问日期、URL，用来支撑"工具怎么工作"这类说明；方法、系统、观点要引论文。

S6. **字段一致。** 同一个会议只用一种写法（例如全稿统一写 `Proc. VLDB Endow.` 或统一写 `PVLDB`；SIGMOD 研究轨道统一写 `Proc. ACM Manag. Data`）。`@inproceedings` 和 `@article` 都要有年份、页码或 articleno（PACMMOD 用 articleno）。DOI：PVLDB 和 ACM 的模板一般不印 DOI（样本里 DOI 印出比例中位数只有 1%），所以缺 DOI 只判 MINOR。但 .bib 里应尽量填 DOI，方便核实。NeurIPS、ICLR、ICML、CIDR 没有 DOI，用官方 proceedings 或 OpenReview 的 URL。

S7. **不要过度自引。** 样本自引上界的中位数是 12.5%，P75 是 27.5%。同作者的稿子只引用确实相关的，引用时说清楚差异（见 R4）。

S8. **引用要承担论证作用。** 新增的每一条都要放在它真正支撑某个论断的位置，比如背景事实、基线来源、数据集来源、指标定义、设计依据或差异对比。不准为了凑数加一串"see also"。

## 4. 修改流程（审稿人 ≠ 修改人）

1. 审稿人运行 `reflint.py --online`，再人工通读引言、相关工作和实验 setup，写 `reviews/<paper>_refreview_rN.md`：写明严重度、位置、需要补引用的具体论断，以及已核实的候选文献（DOI 或 DBLP、一句话说明相关性）。
2. 修改人在 .bib 中按出版社或 DBLP 记录录入条目，在正文对应位置加 `\cite`，不改任何数字；编译后确认参考文献编号连续 `[1..N]`、没有 [?]、没有未引用的条目，正文仍在页数上限内。
3. 审稿人复审，直到 0 BLOCKER、0 MAJOR，再交付。

## 5. 典型反例（来自内部 r1 审查，已匿名）

- 12 页方法稿只有 15 篇参考文献、33 次引用，比样本里所有已录用的 12 页研究论文都少。
- 正文用一个"Concurrent work by the same authors"段落列出 4 篇 ICDE 稿和 2 篇 PVLDB 姊妹稿，却没有任何一条进入参考文献表，违反 R4。
- 主表里的基线 GPT / Claude / DeepSeek / Qwen 和工具 DuckDB 都没有引用，违反 R2。
- 评测协议章节定义了一组指标，这类"可回答 / 弃权"指标在选择性预测（selective prediction）文献中有先例，但没有引用。
- "The Making of TPC-DS"被写成 SIGMOD 2006，实际发表在 VLDB 2006，违反 R5。
- 相关工作里一个括号塞了 10 篇以上文献，引言却只有 3–5 次引用，违反 S1 和 S2。
