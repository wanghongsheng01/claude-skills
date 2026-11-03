# SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation (ICDE 2026, Experiment-Analysis-Benchmark)
- Source of full text: arXiv 2609.08950v1（2026-09-08，cs.DB）；FULL TEXT READ: yes
- Length: 正文约 12 页 + 参考文献约 1 页（PDF 共 13 页）；5 张图（Fig.1 流水线示意、Fig.2 JQE 流水线、Fig.3 EX vs join 数、Fig.4 命名自然度分布、Fig.5 失败查询上的 EXP/EXR/F1 分布）；11 张表（Table I–XI）；41 条参考文献；约 6 个公式（多为无编号的定义式）；1 个算法（Alg.1 EXPAND JOINED TABLES）；0 个定理
- 作者：Polytechnique Montréal（Amine Mhedhbi 组，前作有 "The death of schema linking?"、LLM routing for SQL）；代码 github.com/dais-polymtl/sql-morph

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：Text-to-SQL 评测太"静态"：公开 benchmark 查询短、join 简单、命名自然；私有评测集构造贵且不可复现；EX 是 0/1 指标，无法诊断"差多少、错在哪"。
- **本质问题**：两个子问题——(a) **评测集的受控变异（metamorphic/mutation-based test generation）**：给定种子 NL–SQL 对与 schema 图，生成语义可控、可执行、结构上更难（更多 join、环状 JQG）或词汇上更难（缩写化命名）的新测试样例；(b) **结果关系之间的部分匹配度量**：给定预测结果关系与 GT 结果关系（多重集），定义 cell 级 precision/recall，含列对齐（精确 / 语义 bipartite matching / 不对齐）、行匹配（精确 / 贪心部分匹配）、多余列处理（惩罚 / 忽略）三个维度的可配置组合。
- **根因 / gap**（引言 P2–P5）：
  1. 公开 benchmark 结构与命名过于简单，企业 workload 多 join、多缩写（证据：Table III BIRD dev 中环状 JQG 仅 0.27%；Fig.4 BIRD dev 约 80% 标识符属于自然命名 N1）。
  2. 私有评测集构造代价高、LLM 生成不确定，难复现。
  3. EX 是二值的，把"差一个条件"与"完全无关"等同。
  最终归为一个统一根因："评测是静态的（固定 NL–SQL 对 + 粗粒度二值指标）"。
- **问题定义形式**：**没有** 形式化 Problem Definition；JQE 用输入/输出/流水线（Stage A–E）+ 算法描述；schema graph G_S、JQG G_Q 的定义用于 JQE；指标以公式定义（EXP = |MatchedCells|/|PCells| 等）。无复杂度结论（虽然用到图同构判定，作者只引用 Ullmann 算法，未讨论代价）。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把 Text-to-SQL 评测从"固定 benchmark + 二值 EX"改成"以确定性算法变异查询来制造针对特定流水线阶段的 choke point（join 结构 → 生成阶段；命名 → 检索阶段）+ 可配置的 cell 级 precision/recall"。
- **技术组件**：
  1. **Join Query Expansion (JQE)**（§IV）：在 schema graph 上枚举与当前 JQG 相邻的候选表（Stage A），枚举 join 条件幂集（B），**去除可由传递性推出的冗余 join**（B′，通过 JQG 上的环检测），**按 JQG 同构去重做多样性剪枝**（C），程序化注入 SQL（D），最后仅在 NL 改写这一步用 LLM（E，固定 few-shot prompt）。设计原则是"确定性 + 限制幻觉 + 用户可控（join 复杂度偏好、中心性、查询预算、模式覆盖数）"。针对 gap1 的结构维度。真正新意在于"图驱动的确定性扩展 + 非冗余/非同构约束"。
  2. **Textual Query Augmentation (TQA)**（§V）：用 SNAILS 命名自然度分类器（SIGMOD'25）标注 N1/N2/N3，LLM（温度 0、固定 seed）把标识符去自然化（如把完整单词缩成辅音缩写），SQL `ALTER` 克隆库改名，正则改写 GT SQL，few-shot 改写 NL 与 evidence 中的 schema 提及；**每个变体须通过 EX=1 等价性检查**。四种设置 O/O、L/O、O/L、L/L。针对 gap1 的词汇维度，属较工程化的组合。
  3. **Fine-grained execution metrics EXP / EXR / F1**（§VI）：列匹配 3 种（EC/SC/NC，SC 用 embedding + 类型约束 + 最大权二分匹配，阈值 0.7）× 行匹配 2 种（EC/PC，PC 为两阶段：先精确，再按"相等 cell 比例"贪心配对）× 多余列 2 种（PE/IE）。针对 gap3。
- **真正新的**：JQE 的非冗余 + 同构剪枝扩展；EXP/EXR 的配置化框架（思路与 partial-match reward 类似，但作者强调可解释的过/欠预测分解）。**工程组合**：TQA（复用 SNAILS 分类器 + LLM 改写）。
- **理论保证**：无。没有证明 JQE 保持语义意图（只能靠人工验证 58 条，74.1% 完全对齐、12.1% 丢失意图）；没有证明 EXP/EXR 满足某些公理（如单调性），而是用"单错误变异"实验（Table IX/X）经验性验证方向正确。

## 3. 实验设计 (Experiments)
- **研究问题**：没有统一 RQ 编号，按三大贡献分节，每节末尾用 **"Takeaway" 方框** 总结；§VI 内有 2 个显式 Research Question（受控错误敏感性；系统级对比是否揭示更细差异）。
- **数据集**：**仅 BIRD dev**（1,534 题，11 个库）。JQE 生成 6,873 条（generated set），其中只有 **58 条** 非同构新模式（expansion set），来自 30 个种子；另按 JQG 大小 (2,1)…(5,4) 采样 4 组 × 120 = 480 条做 join 复杂度实验。TQA 作用于全部 dev。
- **被测系统**（3 个，均为开源、较早期）：DIN-SQL（NeurIPS'23）、MAC-SQL（COLING'25）、CHESS（IR+CG+UT 配置）。**没有 2025 年的 SOTA 系统**（如 CHASE-SQL、XiYan-SQL、OmniSQL 系列），对 EAB 论文而言覆盖面偏窄。Table I 引用的各系统官方 dev EX 与 Table IV 作者复现值不同（CHESS 68.3 vs 64.86），文中未解释。
- **LLM backbone**：统一使用 **GPT-4o** + text-embedding-3-small（OpenAI 单 vendor）；框架虽支持 OpenAI/Hugging Face/Ollama，实验中未跨 vendor 对比。
- **指标**：EX；schema 检索用 FPR 与 SLR（Schema Linking Recall）；新提出 EXP/EXR/F1；JQG 平均度 d̄ = 2|E|/|V| 与环比例。
- **实验类型**：
  - JQE：输出结构分布（Table II/III；平均度 0.82→1.35→1.80，环 0.27%→4.31%→51.72%）；EX 下降（Table IV，CHESS 63.33→44.83，DIN-SQL 60.00→32.76）；ΔEX 分布（Table V）；join 数 vs EX（Fig.3，降至 ≤15%）；**控制实验**（Table VI：固定扩展后的上下文、换回原 NL，恢复率从 54.90% 降到 24.05%，用于区分"join 推理难度"与"上下文噪声"）——这是 EAB 论文中很好的因果隔离设计。
  - TQA：系统级 ΔEX（Table VII，DIN-SQL 在 L/L 下 −23.9%）；阶段级检索（Table VIII，Full-Schema/SCSL/TCSL 的 FPR/SLR）；定性例子（toxicology 库）。
  - 指标：单错误变异敏感性（Table IX 15 种变异算子及预期方向，Table X 实测 Δ）；共同失败的 410 题系统对比（Table XI、Fig.5；排名不变但揭示过/欠预测差异）；定性例子。
- **成本报告**：Section III 声称"medium-token-budget、cost-conscious、可集成进 CI/CD"，但 **全文没有报告任何 token 数、$ 或延迟数字**——声明与证据不符，是明显缺口。
- **统计**：无多次运行、无方差、无显著性检验；58 条扩展集样本小。
- **结果呈现**：以表为主（11 张），图少；用 "up to 17%/20%" 表述最大下降；每节 Takeaway 框。

## 4. 写作结构 (Writing)
- **标题模式**："<系统名>: <技术 1> and <技术 2> for <任务> Evaluation"——直接列出两个贡献。
- **摘要逐句功能**：S1 背景（Text-to-SQL 民主化数据访问）→ S2 gap（评测是瓶颈：公开 benchmark 不够复杂，私有评测贵且不确定）→ S3 方案（SQLMorph，query mutation）→ S4–S5 两个技术（JQE、TQA）及其"choke point"定位 → S6–S7 两个数字发现（join 增多准确率降、缩写最多降 17%）→ 第二段 S8–S9 指标贡献（EXP、EXR、F1）→ S10 发现（揭示二值指标掩盖的差异）→ S11 总结意义。**两段式摘要**，每个贡献配一个实证发现，典型 EAB 写法。
- **引言逐段功能**：P1 愿景与进展（LLM、Spider/BIRD）；P2 公开 benchmark 与企业 workload 不匹配（引 Beaver）；P3 私有评测集代价与不可复现；P4 EX 指标的粗粒度（举"漏一个条件 vs 完全无关"例子）；P5 统一根因"静态评测" + 提出 SQLMorph 与 choke point 概念；I-A 贡献列表 **3 条**（每条带章节号、带一个量化结果）。**无 Figure 1 motivating example**（Fig.1 是 Background 里的流水线示意图）。
- **章节顺序与篇幅**：I Intro（~1.2 页）→ II Background（Text-to-SQL 流水线三阶段 Retrieval/Generation/Correction，~0.7 页；用来说明每种变异针对哪个阶段）→ III Experimental Setup（**统一前置**，~0.8 页）→ IV JQE（~3 页，方法 + 实验合在一节）→ V TQA（~2 页）→ VI Fine-grained Metrics（~3 页）→ **VII Related Work and Challenges（放在最后，~0.8 页，按 benchmark / 企业 schema / 可复现性 / 命名 / 指标 / RL reward 六个主题组织）** → VIII Conclusion。
- **写作技巧**：
  - **"每个贡献 = 方法 + 实验 + Takeaway"自包含成节**，适合 EAB 类论文，读者可独立阅读每部分。
  - 用 Background 中的流水线阶段图建立"choke point → 阶段"的映射，让 benchmark 设计有明确的诊断目的（作者称其为 targeted choke points）。
  - 用 running example（Customer–Purchase–Product）贯穿 JQE 解释。
  - Table IX 先写"预期方向"（↑↓=×），Table X 再给实测值——"先假设后验证"，让一个没有理论的指标显得有原则性。
  - Related Work 末尾提出 EXP/EXR 可作为 RL reward，为后续工作埋点。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **EAB 轨道契合**：不追 SOTA，而是提供可复现的评测框架 + 新发现（join 与命名是主要失败模式），开源工具，符合 ICDE Experiment-Analysis-Benchmark 的评价标准。
2. **数据库视角的问题建模**：schema graph、JQG、图同构去重、传递性冗余检测、多重集结果关系匹配——都是 DB 社区熟悉的概念，区别于 NLP 社区的 benchmark 论文。
3. **因果隔离实验**（Table VI 固定上下文换回原 NL）显示了实验设计的严谨性，审稿人通常欣赏。
4. **指标设计有诊断价值**：过预测/欠预测分解直观，并给出 15 种变异算子的系统验证。
5. 可借鉴的缺口：(a) 只用 BIRD dev、3 个旧系统、单一 GPT-4o；(b) 扩展集仅 58 条，NL 改写有 12.1% 意图漂移，缺乏自动意图一致性验证；(c) 声称低成本却没报告成本；(d) EXP/EXR 只用于离线诊断，未用于 **在线候选选择/重排序**（在无 GT 时无法计算）——这是一个可以连接"多候选 SQL 选择"的切入点：例如用候选间的 EXP/EXR 相似度做软投票/聚类。
