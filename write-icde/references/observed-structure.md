# Observed structure of accepted ICDE papers (extracted from the four group syntheses)

Source notes: read-icde/references/notes/. Chinese text is the original analysis; counts are observations.



# Group A

## (4) 写作与论文结构

- **标题**：三种模式——(a) `缩写: A [Cost-Efficient / Learned Cost-Constrained / Co-Designed] Framework/System for X`（SPARQ、CARROT、BOND，全部 2026 年）；(b) `Querying <数据性质> <数据> with LLMs`（ZenDB，把洞见写进标题）；(c) `Tailoring <经典理论> for <问题> towards <任务>`（CSV）。2026 年的三篇都在标题里放了成本/系统类修饰语。
- **摘要**：都是"背景 → gap（2–4 个并列缺点）→ 提出 X → 2–3 个组件 → 带 up to / on average 的数字 → 代码/可用性声明"。数字口径常不严谨（SPARQ 的 10.19× 在摘要是 up to、正文是 average；CSV 的 5.90% 在摘要是 average、贡献列表是 up to）。
- **引言**：
  - 都有 Figure 1 motivating example（CARROT Eiffel Tower chunks、SPARQ 足球比赛表、ZenDB 市政议程报告、CSV 实体匹配 prompt）；ZenDB 和 SPARQ 还有第二个"定位图"（ZenDB Fig.2 cheap vs accurate；SPARQ Fig.2 预实验）。
  - 段首加粗短语串联逻辑（ZenDB、CSV、CARROT 的 "Challenge k:"）。
  - 贡献列表 4–6 条，2026 年的论文倾向于在每条后标注章节号或 "addressing Challenge k"。
  - 预先回应审稿人质疑：CARROT（Agentic RAG 是否让标准 RAG 过时）、SPARQ（为何不用 VPC）、CSV（为何不直接塞满上下文）。
- **章节结构**：Intro → Preliminaries/Problem → (Motivation/预实验) → Overview → 2–3 个方法节 → Experiments → Related Work（CSV、ZenDB 放末尾；CARROT 放在问题定义之后；SPARQ 与 Preliminary 合并放在前面）→ Conclusion。实验约占 3–4 页（全文 25–30%）。
- **"外放"策略**：CARROT、CSV 把证明放在 GitHub Technical Report；SPARQ 发布带 12 页附录的 full version。ICDE 页数紧，这已是常规做法。
- **ICDE 2026 新增**：CARROT 和 SPARQ 都有 "AI-Generated Content Acknowledgment" 段（ICDE 2026 政策），我们的 ICDE 2027 投稿需要注意。
- **ICDE 对小瑕疵容忍度不低**（SPARQ 的图号/数字不一致，CSV 的交叉引用错误与模型名笔误），但这些仍是风险点，我们应避免。



# Group B

## 0. 阅读覆盖情况（先说清楚读了什么）
| 任务编号 | 论文 | 笔记文件 | 全文 |
|---|---|---|---|
| 1 | CYANSQL（ICDE'26，复旦 + 腾讯云） | `B_cyansql.md` | **否**——IEEE 闭源，无 arXiv/GitHub；只有元数据（16 页、70 篇参考文献）和一条厂商二手描述（BIRD EX 73.47%） |
| 2 | Beyond Majority Voting: Hint-guided SQL Selection with LLM（ICDE'27 R1） | —— | **未找到**（arXiv、OpenAlex、Web 均无），未写笔记 |
| 2′ 替代 | CycleSQL: Grounding NL2SQL with Data-Based Self-Explanations（ICDE'25，复旦，与 CYANSQL 同组） | `B_cyclesql_substitute.md` | 是 |
| 3 | FusionSQL: Efficient & Effective Evaluator on Unseen and Unlabeled Data（ICDE'26） | `B_fusionsql_evaluator.md` | 是 |
| 4 | SQLMorph（ICDE'26，EAB） | `B_sqlmorph.md` | 是 |
| 5 | KaSLA: Knapsack Optimization-based Schema Linking（ICDE'26） | `B_kasla.md` | 是 |
| 1′ 补充 | HEXGEN-FLOW: LLM Inference Scheduling for Agentic Text-to-SQL（ICDE'26） | `B_hexgenflow_substitute.md` | 是 |

下文的结论基于 **5 篇全文精读**（CycleSQL、FusionSQL、SQLMorph、KaSLA、HEXGEN-FLOW）；CYANSQL 只在书目层面提及，不对其内容下结论。

---

## 4. 写作结构的共同模式
1. **标题**：三种模式——"<系统名>: <技术> for <任务>"（SQLMorph、HEXGEN-FLOW、CYANSQL）、"<技术>-based <任务> for <场景>"（KaSLA）、"Grounding/An Efficient and Effective <X> on <困难设定>"（CycleSQL、FusionSQL）。都在标题中点出 **技术范式**（knapsack、clustering-based TTS、query mutation、data-based self-explanations）或 **困难设定**（unseen and unlabeled）。
2. **摘要**：背景 → gap（常带"why"一句）→ 系统名 + 一句核心思想 → 2–3 个技术点 → 实验规模 → 1–2 个亮点数字（"up to 17%"、"1.42∼1.56×"、"82.0% (+2.6%)"）。FusionSQL 是例外：完全不放数字，强调应用价值。
3. **引言**：5–7 段；第 2–4 段建立 gap（例子或编号挑战）；倒数第二段方法概述，常用 **圆圈编号/"To tackle C1"** 与图对应；**贡献列表 3 条为主**（KaSLA、SQLMorph、CycleSQL、HEXGEN-FLOW 各 3 条，FusionSQL 5 条）。Figure 1 有三种：性能差距柱状图（KaSLA）、pass@k 预实验（CycleSQL）、概念/流水线图（FusionSQL、HEXGEN-FLOW）；SQLMorph 没有 motivating figure。
4. **Related Work 放在实验之后**：5 篇中 4 篇（KaSLA、SQLMorph、CycleSQL、HEXGEN-FLOW）放在最后，只有 FusionSQL 紧随引言。分类通常为"Text-to-SQL 方法"+"本文所借用的技术领域"（provenance、LLM serving、label-free estimation 等）两类。
5. **实验节占 40–55% 篇幅**，按 RQ（KaSLA 4 个、FusionSQL 5 个）或按贡献分节 + Takeaway 框（SQLMorph）。
6. **常用技巧**：给现象起名字并加粗（Seesaw Problem）；一个 running example 贯穿全文（CycleSQL 的 Airbus 例子、SQLMorph 的 Customer–Purchase）；Oracle/上限实验（CycleSQL）；"先写预期方向、再给实测"（SQLMorph Table IX/X）；单列 Limitation 节（KaSLA）；"AI-Generated Content Acknowledgement" 已成为 ICDE 2026 的标配（KaSLA、FusionSQL、SQLMorph 都有）。



# Group C

## 0. 阅读覆盖情况
| # | 论文 | 类别 | 全文 | 笔记 |
|---|------|------|------|------|
| 1 | Tag-Filtered ANNS (ICDE'25) | Regular | **否**（仅摘要 + GitHub README；无开放版本） | C_tag-filtered-anns.md |
| 2 | Effective and General Distance Computation for ANNS (ICDE'25) | Regular | 是（arXiv 2404.16322v4） | C_ddc-distance-computation.md |
| 3 | DCOs Are Not Silver Bullets (ICDE'26) | EAB | 是（arXiv 2604.02801v1，含附录） | C_dco-benchmark.md |
| 4 | ~~Pitfalls in Learned Indexes (ICDE'27 R1)~~ → **替代**：Benchmarking RL-Enhanced Spatial Indices (ICDE'26) | EAB | 原文无任何公开版本；替代论文全文已读（arXiv 2512.11161v1） | C_rlesi-learned-index-benchmark.md |
| 5 | XRAG (ICDE'26) | EAB | 是（arXiv 2412.15529v4） | C_xrag-benchmark.md |

注意：论文 2 与论文 3 构成一个很有价值的"被评测者—评测者"配对——论文 3 的 8 个被测方法中有 3 个（DDC_res/DDC_pca/DDC_opq）就是论文 2 提出的，可直接看到 ICDE 审稿体系如何同时接受"方法论文"与"推翻其部分结论的 EAB 论文"。

基本数据对比（已读全文的 4 篇）：
| | 论文 2 | 论文 3 | 替代 4 | 论文 5 |
|---|---|---|---|---|
| 正文页数 | ~12 | 12（+9 页附录 arXiv 版） | ~12 | ~12 |
| Figure | 10 | 14（正文） | 24 | 8 |
| Table | 3 | 4 | 3 | 14 |
| 参考文献 | 40 | 54 | 59 | 57 |
| 定理/引理 | 1 Thm + 2 Lemma | 0（3 Def） | 0（4 Def） | 0 |
| 主结果载体 | recall-QPS 曲线 | recall-QPS 曲线网格 | 柱状图 + 雷达图 | 大表（±std） |
| AI 使用声明 | 无 | 有（DeepSeek-R1） | 有（ChatGPT） | 有（DeepSeek-R1） |

## 4. 写作结构 (Writing structure)：EAB 与 Regular 的差异
| 维度 | Regular（论文 2，及论文 1 摘要） | EAB（论文 3、替代 4、XRAG） |
|---|---|---|
| 标题 | "Effective and General X for Y" / 新问题命名"Tag-Filtered ANNS" | 结论式（"Are Not Silver Bullets…Merits and Limits"）或对比范围式（"Against Traditional, Advanced, and Learned Counterparts"）或缩写 + 双关（XRAG） |
| 摘要 | 背景 → SOTA 缺陷 → 方法 → "1.6–2.1×" → 工业落地 | 研究问题 → 规模（方法数、数据集数、最大维度/规模、硬件）→ 负面发现 → 正面发现 → 总体结论（论文 3 最佳范例；XRAG 摘要无数字是反例） |
| 引言 | SOTA 机制 → 加粗"Effectiveness/Generality"两段 gap → "Our Idea"研究问句 → 4 条带章节号的贡献 → 引言内嵌 Related Work | 先前评测局限（bullet / 表）→ **在引言中直接列出编号 findings**（论文 3 四条加粗；替代 4 预告 O1–O22 分 7 组）→ 贡献 3–4 条（"first comprehensive benchmark" + 分析 + 指南/开源）→ Road Map |
| 主体 | Prelim → Problem Analysis（剖析 SOTA）→ 方法 1 → 方法 2 → 复杂度分析 → 实验 | Prelim/Definitions → 方法综述 + taxonomy（占 2–3 页，兼具 survey 功能）→ Benchmark Setup → 按因素分节的实验 |
| 结论组织 | Exp-1..Exp-8 叙述 | 每节结尾 **"Takeaway #n"**（论文 3）/ **编号 Observation Oi**（替代 4）/ **罗马数字加粗 lesson**（XRAG）；结尾有 Summary：推荐决策图（论文 3 Fig.14）或雷达图（替代 4 Fig.23）+ Merits/Limitations + 未来方向 |
| Related Work | 压缩进引言 | 末尾独立短节（论文 3）、前置（XRAG）、或融入方法综述（替代 4） |
| 篇幅分配 | 方法 ~45%、实验 ~30% | 方法综述 ~20%、实验 ~45–50% |
- ICDE 2026 起，三篇 2026 论文都有 **"AI-Generated Content Acknowledgement"** 小节（ICDE 2025 的论文 2 没有）——ICDE 2027 投稿需准备。
- EAB 的"fundamentally new insight"在这三篇里有三种形态：(a) **推翻/修正前作结论**（论文 3：DCO 的加速在 SIMD/OOD/低维/超高维下消失）；(b) **揭示被忽略的成本或机制**（替代 4：调参 >30h、采样训练导致页面局部性失真；论文 3：O(D²) 查询旋转在 HNSW 的 O(log N) 次 DCO 中无法摊销）；(c) **反直觉的组件关系**（XRAG：检索的 top-3 常优于 golden context；context 数量增加收益有限）。(a)(b) 的说服力明显强于 (c)，因为它们有机制解释。



# Group D

## 0. 本组实际阅读清单与全文获取情况

| # | 论文 | 会议/赛道 | 来源 | 全文 | 笔记 |
|---|---|---|---|---|---|
| 1 | Maintaining Leiden Communities in Large Dynamic Graphs | ICDE 2027 R1, Regular | arXiv 2601.08554v5（含附录的 full version） | 是 | D_hit-leiden.md |
| 2 | ~~Maintaining Ego-Betweenness Centrality at Billion Scale~~ → **替代**：Fast Maximization of Current Flow Group Closeness Centrality | ICDE 2025, Regular | arXiv 2504.04472v1 | 是 | D_cfcm-centrality.md |
| 3 | Scalable Algorithm for Dynamic Quasi-clique Detection | ICDE 2027 R1, Regular | arXiv 2605.26235v2 | 是 | D_dynamic-quasi-clique.md |
| 4 | TS-Fault: Benchmarking Time Series Forecasters Against Structural Faults | ICDE 2027 R1, EAB | arXiv 2606.18539v1 | 是 | D_ts-fault.md |
| 5 | （自选）Maximal Clique Enumeration with Hybrid Branching and Early Termination | ICDE 2025, Regular | arXiv 2412.08218v1（含附录） | 是 | D_hbbmc-mce.md |

- Ego-betweenness 论文（Kaiyu Chen, Dong Wen 等，UNSW）在 arXiv、OpenAlex（尚未出版、无摘要）、Web 与 GitHub 上均无公开版本，**未读**，以同为 centrality 主题的 ICDE 2025 论文替代。其直接前身为 ICDE 2022 "Efficient Top-k Ego-Betweenness Search"（arXiv 2107.10052）。
- 自选 #5 的理由：它是 ICDE 2025/2026 cohesive-subgraph 论文中有 arXiv 全文且注明 ICDE 录用的代表；它是静态算法，正好和 #1/#3 的"动态维护"题型对照。

### 量化对照

| 指标 | HIT-Leiden | DMI (quasi-clique) | CFCM | HBBMC (MCE) | TS-Fault (EAB) |
|---|---|---|---|---|---|
| 正文页数 | ~12 | ~12.3 | ~12.3 | ~12 | ~13.5 |
| 附录 | 有（证明 + 补充实验 + 应用），在 full version | 无 | 无 | 有（证明 + 例子 + 合成数据） | 无 |
| Figures / Tables | 24 / 3 | 9 / 10 | 5 / 2 | 5 / 7 | 9 / 9 |
| References | 56 | 56 | 73 | 66 | 85 |
| Theorem / Lemma | 1 / 4（+3 Observation, 1 Assumption） | 0 / 3 | 2 / 15 | 6 / 2 | 0 / 0 |
| Definition / Algorithm | 9 / 6 | 3 / 5 | 3 / 5 | 1 / 10 | 2 / 1 |
| Running example | 有，贯穿全文（Example 1–6） | 无 | 无 | 仅附录小例子 | 无（用示意图 Fig.2–4） |
| 数据集数 / 最大规模 | 5 / 4.0B 边（ByteDance） | 9 / 22M 边 | 27 / 106M 边 | 16 real + ER/BA / 106M 边 | 6 / 321 通道 |
| 基线数 | 4 | 3 外部 + 4 自有变体 | 4 | 4 | 21 个被测模型 |
| 硬件披露 | Xeon 8336C, 2TB RAM | Xeon 8358, 512GB | 72 核, 256GB, 72 线程 | 2.1GHz Intel, 128GB | **未披露** |
| 头条数字 | up to 10^5× | up to 10^4× | up to 370× | up to 4.38× | ρ = −0.544 |
| 代码开源 | 是（GitHub full version） | 是 | 未在正文见到链接 | 是 | 是 |

## 4. 写作结构的共性

- **章节顺序**：Intro → (Related Work) → Preliminaries/Problem → [Theory] → Algorithm(s) → Experiments → (Related Work) → Conclusion。Related Work 的位置与论文类型相关：问题驱动/动态论文（HIT-Leiden、DMI）和 EAB（TS-Fault）放在第 II 节，用来定位问题空白；理论/算法驱动论文（CFCM、HBBMC）放在实验之后，因为引言和 Preliminaries 已经交代了 SOTA。
- **引言**：一般 5–7 段，结构为 应用背景 → 经典模型/SOTA → gap（可能不止一个，常附工业或理论证据）→ 方法概览 → 贡献（3–4 条 bullet，常带 Section 编号）→ 章节安排。理论型论文引言中没有 Figure 1；HIT-Leiden 在引言放了 3 张流程/示例图。
- **定义与引理的位置**：所有定义集中在 Preliminaries，记号表（Table I）几乎是标配（HIT-Leiden、CFCM）；Lemma 紧挨使用它的算法；证明要么放附录 / full version（HIT-Leiden 用 GitHub 托管 full version 并在正文引用 [53]），要么省略（DMI 的 Lemma 3 "omitted due to space"）。
- **伪代码风格**：algorithm2e 风格，Input/Output 明确，正文逐行引用（"lines 2–7"）；递归过程以 Procedure XXX_Rec 命名；复杂算法拆成多个子过程，彼此用"lines x–y of Algorithm k"引用以节省篇幅。
- **值得学习的单点技巧**：HIT-Leiden 的"design rationale"图（Fig.7，画出 Assumption/Lemma/Observation → 算法组件的依赖关系）与贯穿全文的 running example；CFCM 每节开头的"本节推导路线图"；HBBMC 的数据集表直接列出理论参数 δ、τ、ρ，以及"与自己前作的差异"专段；TS-Fault 的"RQ 先答后证"（每个 RQ 第一句就是答案）与 Threats to Validity。
- **新规范**：DMI 包含 "AI-Generated Content Acknowledgment"（声明 ChatGPT/Gemini 只用于润色与实验代码辅助）——ICDE 2027 投稿应准备同类声明。
