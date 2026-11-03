# Scalable Algorithm for Dynamic Quasi-clique Detection (ICDE 2027 round 1, Regular)
- Source of full text: arXiv 2605.26235v2（2026-09-30 修订版；作者 Jingbang Chen*, Weinuo Li*, Yingli Zhou†, Hao Wu, Can Wang, Yixiang Fang, Chenhao Ma†；CUHK-SZ / ZJU / SLAI）；FULL TEXT READ: yes（全部 14 页读完）
- Length: 全文 14 页 = 正文约 12.3 页（p1–p12，含 "Additional Experiment" 一节）+ 参考文献约 1.7 页；Figures 9 个；Tables 10 个；References 56 条；编号 Equations 5 个；Lemma 3 个（Lemma 1–2 是引用已有 MinHash 结构的复杂度，Lemma 3 是本文的"删一点即可恢复密度"的充分条件，证明 "omitted due to space"）；无 Theorem；Definition 3 个；Problem 2 个；Algorithm 5 个；无编号 Example。另有一段 "AI-Generated Content Acknowledgment"（声明 ChatGPT/Gemini 用于润色与实验代码辅助）——这是 IEEE 新要求的写法，值得注意。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：图的边不断插入/删除时，持续给出当前最大的 α-quasi-clique（边密度 ≥ α 的最大顶点集）。
- **本质问题**：一个 NP-hard 组合优化问题（MQCP）的 *近似解的在线维护*。
  - 输入：初始图 G(V,E)（顶点集固定）、密度阈值 α∈(0,1]、操作序列 AddEdge/DeleteEdge。
  - 输出：每次操作后的一个（尽可能大的）α-quasi-clique。
  - 约束：输出必须是合法的 α-quasi-clique（通过精确密度验证保证可行性）。
  - 目标：最大化 |S|，同时单次更新近似线性/亚线性代价。
- **作者给出的 gap**：(1) 已有 MQCP 算法都是静态的（Pang et al. 的 FastNBSim/NBSim、NuQClq 等），每次更新都要重跑；(2) "there is no prior work"——没有动态 quasi-clique 的研究（作者宣称 initiate the study）。gap 的证据主要是"文献空白"本身，没有预实验图；Fig.1 只是 clique vs. 0.75-quasi-clique 的概念插图（8 个顶点 28 条边 vs. 21 条边）。
- **问题定义形式**：Definition 1（edge density）→ Problem 1（MQCP）→ Problem 2（DMQCP：两种操作，"after each operation, find the α-quasi-clique with the most vertices"）。Hardness 只有一句："MQCP 是 NP-hard，所以 DMQCP 也是 NP-hard"——严格讲这是一个不完全的论证（动态版本的 hardness 应当就单次更新的代价来陈述，例如在已知旧解的情况下更新是否仍难），审稿人显然接受了这一简化。没有给出近似比，作者只说 "approximate maximum quasi-cliques in near-linear time after each operation"。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：静态 SOTA（Pang et al. FastNBSim）的"以每个顶点邻域为中心、按 MinHash 估计的 containment score 选邻居"这一 *局部* 抽取步骤天然可增量化——只要 Jaccard 签名支持插入/删除元素；再维护一个 *大小为 B 的候选 quasi-clique 列表*（而不是只保留一个最优解）并周期性重建，就能在低代价下保持质量。
- **技术组件**：
  1. **可更新的 MinHash 签名**：l-buffered k-MinHash 与 Bottom-k MinHash 两种（Lemma 1/2 给出 Init/Update/Query 复杂度，均来自已有文献 [24][25]）。这是"工程组合"：把已有 sketch 换成动态版本。
  2. **γ-degree 的增量维护 + 剪枝**：γ-degree d_γ(u) 是从 u 邻域能抽出的 quasi-clique 大小上界；插/删边时只需更新 u、v 两端点及其邻居的 d_γ，并只在 d_γ(w) ≥ 当前候选列表最小解时才重新 Detect——这是继承自静态算法的 upper-bound pruning 的动态版本。
  3. **候选列表 L + AddClique 规则**（Alg.2）：最多保留 B=5 个互不冗余（Jaccard > r_tol 视为冗余）的候选；新候选替换最相似且更小的，或替换最小者。消融（Table V: B=1 vs B=9）显示平均大小在部分数据集上从 92 提升到 129。
  4. **删除时的局部修复 CliqueDeleteEdge**（Alg.5）：若删边后密度 < α，尝试删去 1 个（u、v 或最小度点）或 2 个顶点以恢复密度；Lemma 3 给出删一个点即可恢复的三个充分条件（最小度足够大 / 最小度 ≤ 平均度-1 / u 或 v 本身是最小度点）。失败才丢弃（Table X：62 万次更新仅丢弃 14/6 次）。这是本文最"新"的理论小结果。
  5. **Batch reconstruction**：每 Batch=5000 次操作整体重建 L，以防偏差累积；是一个显式的 time–quality trade-off 参数。
  6. 副产品 **NSF**：为每个顶点存一个候选、只对受影响顶点重跑 Detect 的朴素增量框架，作为额外对照。
- **理论保证**：只有复杂度：Build 为 Õ(n+m)+Σ_C τ(C)；非重建插入 Õ(d_max²)+Σ_C τ(C)；非重建删除 Õ(d_max)；内存 Õ(n+m)。复杂度是按"每次更新"表述的，并把重建代价摊还为 T_Build/Batch。**无近似比、无质量界**；静态框架中 "δ(C) ≥ 1−(1−γ)/b" 的界在 γ=0.9、b=0.6 时只有 0.833 < α=0.9，因此必须依赖精确验证。

## 3. 实验设计 (Experiments)
- **实验目标**：Sec.VI-B 随机动态图上的效率与质量；VI-C 特殊动态图（只插入、只删除、时序图）；Sec.VII "Additional Experiment" 中七项：参数（γ,b；k；batch）、操作规模可扩展性（Q=10…10^5）、各阶段时间（Init vs Update，Table IV）、候选列表消融（B）、内存（Table VI/VII）、重建开销与更新时延（Table VIII/IX，median 2×10⁻⁶–1.2×10⁻⁵ 秒）、丢弃/重建统计（Table X）。
- **数据集（9 个，SNAP + KONECT）**：Ego-facebook (4K/88K)、Ca-HepPh (12K/118K)、Ca-CondMat (23K/93K)、Email-Enron (37K/184K)、Web-Stanford (282K/2.0M)、Web-BerkStan (685K/6.6M)、Web-Google (876K/4.3M)、Soc-Pokec (1.6M/22.3M)、dblp coauthor（时序，1.8M 顶点）。最多 10^5 次操作。操作生成：rand（随机插删）、inc、del、temp（时间窗转插删）、tinc。**最大图只有 2.2×10^7 边**——标题中的 "Scalable" 指的是相对静态重跑的更新效率，而非数据规模。
- **基线（3 个外部 + 4 个自有变体）**：FastNBSim、NBSim（Pang et al. [18]，静态 SOTA）、NuQClq（local search，[21]）——每次更新都从头重跑；以及 DMI-bf、DMI-bt、NSF-fn、NSF-ns。NuQClq 的密度阈值被设为 DMI 得到的平均密度（一个公平性处理的小细节）。
- **参数**：α=0.9, γ=0.9, b=0.6, r_tol=0.7, k=8, l=8, Batch=5000, B=5；NSF: R=20。
- **硬件**：Intel Xeon Platinum 8358 @2.60GHz，512 GB 内存，Ubuntu；C++；代码开源（GitHub freewh2005/DMI）。
- **实验类型**：主结果（效率 Fig.2/3 + 质量 Table II/III）、参数敏感性（Fig.4–6）、可扩展性（Fig.7/8）、阶段时间（Table IV）、消融（Table V, Fig.9）、内存（Table VI/VII）、时延分布（Table VIII/IX）、修复统计（Table X）。无 case study。
- **结果呈现**：效率用 log 轴柱状图（总时间），质量用表（Size, Density 两列/数据集）。提升表述："up to four orders of magnitude"（摘要），正文 "approximately 100× to over 10,000× faster"、"up to a 1,000× improvement"；质量用 "δ(S)∈[0.91,1.00], with similar size"。注意：DMI 的平均大小在若干数据集上明显小于 NBSim/NuQClq（如 rand_HP 上 DMI-bf 129 vs NBSim 238.6），作者以 "trade time for higher quality" 解释——即这是一个 *接受质量下降换速度* 的论文，但用"competitive"措辞包装。

## 4. 写作结构 (Writing)
- **标题模式**："Scalable Algorithm for Dynamic <经典问题>"——非常朴素，无方法名。
- **摘要逐句功能**：S1 背景（quasi-clique 在社交/生物/电商中重要）→ S2 gap（静态方法已有，但真实网络动态，静态方法低效）→ S3 我们 initiate DMQCP → S4 方法 DMI（两种可更新 MinHash）→ S5 batch reconstruction 保证稳定性 → S6 实验（up to 4 orders）→ S7 副产品 NSF → S8 意义（首个高效框架）。
- **引言逐段功能**：P1 稠密子图挖掘背景与经典模型（densest subgraph、k-core、k-clique densest）→ P2 clique 的地位与 NP-hard → P3 quasi-clique 作为松弛 + Fig.1 举例 + 应用（PPI、社区、协作）→ P4 静态 MQCP 已有工作 vs. 网络动态 → **"there is no prior work"（加粗/斜体强调）** → P5 我们的方法概述（扩展 [18]，两种 MinHash，候选列表，batch reconstruction）→ P6 贡献列表 **4 条 bullet** → P7 Outline。
- **章节顺序与篇幅**：I Intro（~1.3 页）→ II Related Works（~0.6 页，clique problems / quasi-clique problems 两类，各自含静态与动态）→ III Preliminaries（~0.8 页：记号、问题、MinHash）→ IV Similarity-based Algorithm（~3.3 页：回顾静态、Build、Insertion、Deletion、Overall）→ V NSF（~0.4 页）→ VI Evaluation（~2.2 页）→ VII Additional Experiment（~2.5 页）→ VIII Conclusion。实验占比约 40%，相当重。
- **伪代码风格**：每个操作一个算法（Detect / Build+AddClique / AddEdge / DeleteEdge / CliqueDeleteEdge），正文逐行解释（"Line 9 … Line 16"），每个小节以 "Time Complexity." 段落收尾——这种"算法 + 逐行解释 + 复杂度段"的三段式是 ICDE 图算法论文的标准模板。
- **Related work 分类**：按问题类型（clique counting/enumeration、maximal、maximum；vertex-based vs edge-based quasi-clique）。
- **好的写作技巧**：在 Sec.IV-B 用 4 个 bullet 列出"一系列更新可能迫使候选列表变化的四种情形"，然后说明框架如何覆盖它们——把设计需求显式枚举，再一一对应到机制。一句短引用："there is no prior work studying the dynamic quasi-clique extraction problem"（强调首创性）。
- **不足**：没有 running example 贯穿算法；Lemma 3 证明省略；"seven experiments" 放在独立的 Additional Experiment 一节而非附录，导致正文结构略散。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **"首个动态版本"叙事**：把一个有成熟静态 SOTA（Pang et al.）的 NP-hard 问题搬到动态设定，问题新、门槛低、易于理解。
2. **速度差距巨大**（10^2–10^4×）且质量有可信的"合法性"保证（精确密度验证）；更新时延中位数微秒级（Table VIII/IX）。
3. **实验非常全面**：9 个数据集 × 5 种动态生成方式 × 7 组附加实验，弥补了理论较薄的短板；明确的 ablation（B）与修复成功率统计（Table X）回应了"为何需要候选列表/局部修复"的潜在质疑。
4. **团队背景**：CUHK-SZ 稠密子图方向的连续工作（[1][2] 是同组的 densest subgraph 工作），领域积累可信。
5. **可借鉴**：(a) "静态 SOTA 的局部步骤 + 可更新 sketch + 候选池 + 周期性重建"是一个可迁移到其他 NP-hard 结构（k-plex、δ-clique、defective clique）的通用配方——作者自己在结论中也指出这些扩展方向；(b) 每个算法后紧跟 "Time Complexity." 段。
- **可追问的弱点**：无近似保证、无质量随时间漂移的理论界；数据规模偏小（≤22M 边），与标题 "Scalable" 不完全匹配；基线是"每次从头重跑"，缺少更强的增量基线（作者自建的 NSF 部分起此作用）；DMQCP NP-hard 的论证过于简单；同期 arXiv 上已出现另一篇 "Detecting Large Quasi-cliques on Dynamic Networks"（2606.05809），说明该方向竞争很快。
