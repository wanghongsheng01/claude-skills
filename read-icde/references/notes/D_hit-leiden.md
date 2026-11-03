# Maintaining Leiden Communities in Large Dynamic Graphs (ICDE 2027 round 1, Regular)
- Source of full text: arXiv 2601.08554v5 (标注 "Full Version"，2026-01 首发，v5 含附录；作者：Chunxu Lin, Yumao Xie, Yixiang Fang [CUHK-SZ], Yongmin Hu, Yingqian Hu, Cheng Chen [ByteDance]); FULL TEXT READ: yes（正文 + 附录 A 证明 + 附录 B 补充实验 + 附录 C 两个应用研究全部读过）
- Length: 全文 18 页 = 正文约 12 页（p1–p12，含实验）+ 参考文献约 1.5 页（p13–14）+ 附录约 4 页（p14–18）；Figures 24 个（正文 Fig.1–17，附录 Fig.18–24）；Tables 3 个（Notation、复杂度/有界性对比、数据集）；References 56 条；Equations 正文仅 2 个编号公式（modularity、modularity gain），附录证明约 24 个；理论陈述：Theorem 1 个、Lemma 4 个、Observation 3 个、Assumption 1 个、Definition 9 个、Problem 1 个、Example 6 个、Algorithm 6 个（伪代码）

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：图在不断插入/删除边，如何快速得到更新后的 Leiden 社区，而不从头跑 Leiden。
- **本质问题**：一个"多层（hierarchical）、带连通性约束的迭代式优化算法"的 *增量计算（incremental computation）* 问题。
  - 输入：图 G、它的 P 层 Leiden 层次结构（每层 supergraph G^p、社区映射 f^p、子社区映射 s^p）、一批边更新 ΔG。
  - 输出：G⊕ΔG 上的 Leiden 社区（以及下一轮要用的全部辅助结构）。
  - 约束：要保留 Leiden 的两个性质——vertex optimality（任意顶点移走都不会让 modularity 增加）和 subpartition γ-density（子社区 γ-connected，且中间序列 locally optimized）。
  - 目标：在质量（modularity）与 Leiden 相当的前提下，代价只依赖于"受影响区域"，即满足 Fan et al. (SIGMOD'17) 的 *relative boundedness*。
- **作者给出的 gap（根因）**：
  1. 唯一已有工作 DF-Leiden/ND-Leiden/DS-Leiden（Sahu et al., SCI 2025）只在第一轮迭代做了局部化，后面直接调用原始 Leiden，所以每次更新仍是 O(Σ_p(|V^p|+|E^p|))——作者用 Theorem 1 证明这一点，并据此在 Table II 里给出"✗ relatively bounded"的判定。这是"用理论证明 baseline 不行"的写法，而非只靠实验。
  2. refinement 阶段要维护子社区内部的连通性，边删除可能把子社区断开，需要高效的动态连通性追踪。
  3. refinement 和 aggregation 紧耦合，底层的小变化会沿层次向上级联。
- **证据**：Fig.1 用一个 8 顶点小图展示一次插入 + 一次删除让 v3、v4 换社区；Fig.3 对比 DF-Leiden 与 HIT-Leiden 的流水线；引言给出 ByteDance 两个业务的规模（10^8 顶点、2–4×10^9 边，重算 Leiden 需小时级，而业务要求 10^5 条边的批量更新在分钟级完成）作为 *工业动机*。
- **问题定义形式**：非常简短。Problem 1（Maintenance of Leiden communities）只有两行："给定 G 及其 Leiden 社区 C 与边更新 ΔG，返回更新后的 Leiden 社区"，直接引用 [14]。没有 NP-hard 结论（modularity 最大化本身 NP-hard，但本文不是精确优化，而是"维护某个启发式算法的输出"），所以复杂度分析的焦点转向 *boundedness*（Definition 3–5）而不是 hardness。值得注意："维护一个启发式算法的输出"本身是一个定义不够严格的目标——"更新后的 Leiden 社区"并不唯一（Leiden 有随机性），作者用 modularity 相当 + 99% 子社区仍满足 γ-density 来做经验替代。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把 Leiden 的三个阶段都改成增量版本，并在 *每一层 supergraph 上复用同一套增量流程*（下层的社区变化变成上层 superedge 的变化），子社区的 γ-connectivity 用"动态连通分量（dynamic connected components）"近似维护，使代价只与 |N²(CHANGED)| + |N²(AFF)| 有关。
- **技术组件**：
  1. **inc-movement（Alg.2）**：只把"社区内边删除 / 跨社区边插入"的端点放入候选集 A（Observation 1，沿用 DF-Louvain 的启发式），顶点换社区后把其不在新社区的邻居加入 A（Lemma 1）——这是一个类似 label propagation 的 frontier 扩散。工程组合成分较多（来自 [10][11]）。
  2. **inc-refinement（Alg.3）**：真正的新东西之一。作者用 Lemma 2–4 分情况推导"边删/插后哪些顶点可能被逐出子社区"，给出 α（更新边权）必须超过的阈值；再用 Assumption 1（更新边权远小于 m）+ Observation 2（d(v), w(v,U), d(U) 差距通常很小）论证：**只有子社区内边删除导致子社区断开这一种情况需要处理**。于是把子社区当成 G_Ψ 中的连通分量，借用 Xu et al. (SIGMOD'24) 的 constant-time 动态连通性索引（CC-index）来检测分裂，分裂出的每个分量成为新子社区，再把单点子社区尝试并入邻近子社区。
  3. **inc-aggregation（Alg.4）**：把 ΔG 和换子社区的顶点翻译成上一层 supergraph 的 superedge 变化 ΔH，压缩同一 superedge 的多条变化（Example 5 展示了 6 条变化压缩为 2 条）。
  4. **def-update（Alg.5，deferred update）**：自顶向下同步各层的社区映射，避免在迭代中反复向下传播。属于工程优化。
- **"真正的新东西" vs. 工程组合**：理论部分（用 boundedness 框架分析 Leiden、Lemma 2–4 的阈值分析）和"用动态 CC 近似 γ-connectivity + 层次增量"是核心新意；inc-movement 基本继承 DF-Louvain；CC-index 直接复用他人成果。
- **理论保证**：
  - Theorem 1：已有三种算法单次更新代价 O(Σ_p(|V^p|+|E^p|))，因此 unbounded 且 relatively unbounded。
  - HIT-Leiden 每层代价 O(|N²(Γ_p)| + h_p|Γ_p| + |N²(Λ_p)| + h_p|Λ_p|)，h_p 是 CC 生成树平均深度；总代价写为 O(|N²(CHANGED)| + |N²(AFF)|)，宣称 relatively bounded；最坏情况退化为 Leiden + 重建 CC-index；空间 O(Σ_p(|V^p|+|E^p|))。
  - 注意：**质量没有理论保证**。subpartition γ-density 的保持依赖 Observation 3（"大多数情况成立"，由实验 Fig.13 >99% 支撑），作者明确说 case (1) of Lemma 2 被"忽略"。这是一个诚实但可被追问的弱点。AFF 的定义（"改变社区或子社区的超顶点"）也是由本算法自身行为定义的，略有循环论证的味道。

## 3. 实验设计 (Experiments)
- **实验目标**：Sec.VI-B 有效性（modularity；子社区 γ-density 比例），Sec.VI-C 效率（总体、各组件时间占比、batch size b 的影响、批次数 r 的影响）；附录 B：γ 的影响、各层顶点/边数（空间）、|AFF| 大小、999 个批次的长期稳定性；附录 C：两个应用（Graph-RAG on HotpotQA；ByteDance fraud-ring discovery）。
- **数据集（5 个）**：dblp-coauthor (1.8M/29.4M, KONECT)、yahoo-song (1.6M/256.8M, KONECT)、sx-stackoverflow (2.6M/63.4M, SNAP)、it-2004 (41.2M/1.0B, NetworkRepository，无时间戳→随机插删)、risk (201M/4.0B, ByteDance 内部金融交易图)。4 个带真实时间戳。最大规模到 4B 边——这是"large"的支撑。
- **动态设定**：前 80% 边建初始图，滑动窗口 b ∈ {10,…,10^5}（默认 10^3），滑动 r=9 次；排除前两个批次（因为 P=10 时社区尚未收敛）。γ=1、P=10。
- **基线（4 个）**：ST-Leiden（每次从头跑）、ND-Leiden、DS-Leiden、DF-Leiden（均来自 [14] Sahu et al. 2025）。没有 ICDE/VLDB/SIGMOD 的直接竞争者（因为该问题之前只有一篇工作），这也说明"开辟/重做一个几乎空白问题"可以接受小基线集。
- **硬件**：单台 Linux 服务器（Debian 5.4.56），Intel Xeon Platinum 8336C @2.30GHz，2.0 TB RAM；C++，gcc 8.3.0；单线程（未来工作才做并行）。
- **实验类型**：主结果（质量 Fig.11/12/13；效率 Fig.14）、组件分解（Fig.15，堆叠柱状）、参数敏感性（b: Fig.16，r: Fig.17，γ: Fig.18/19）、空间（Fig.20）、AFF 规模（Fig.21）、长期稳定性（Fig.22）、两个 case study（Fig.23/24）。没有严格意义上的消融（如去掉 def-update 或去掉 CC-index 的版本）——组件时间分解起了替代作用。
- **结果呈现**：全部用图（log-scale 折线/柱状），表只用于数据集。提升表述："up to five orders of magnitude"（摘要、引言、Effect of b）；it-2004 上"up to three orders of magnitude faster than the state-of-the-art"（默认 b）；应用中"56.1× faster"、"token cost only 0.8%"、"7.7× the speed"。质量用"差异在 0.01 以内"、"fluctuations around 0.0001"表述"comparable"。

## 4. 写作结构 (Writing)
- **标题模式**："Maintaining <经典算法名> in Large Dynamic Graphs"——动作（Maintaining）+ 对象（Leiden communities）+ 场景（large dynamic）。标题里没有方法名。
- **摘要逐句功能**：S1 背景（Leiden 广泛用于 LLM、异常检测、生物分析）→ S2 场景与痛点（图大且动态，从头算代价大）→ S3 已有工作 gap（只有一个工作，缺理论分析且对大图低效）→ S4 我们的理论贡献（boundedness 分析证明已有算法 relatively unbounded；分析顶点社区归属）→ S5 方法（HIT-Leiden，维护连通分量与层次社区结构，缩小受影响顶点范围）→ S6 实验结论（up to five orders of magnitude）。
- **引言逐段功能**：P1 modularity 概念 + Fig.1 例子 → P2 Louvain 及其两阶段（Fig.2a）→ P3 Louvain 的缺陷（社区内部不连通）→ Leiden 的 refinement（Fig.2b）→ P4 Leiden 的新应用（GraphRAG、eRiskComm）→ P5 动态性与 ByteDance 两个具体业务的规模和时延需求 → P6 Prior works（Louvain 维护有 4 个工作，Leiden 只有 [14]；Fig.3a）→ P7–P8 Our contributions（理论分析 + HIT-Leiden 三阶段，Fig.3b）→ P9 实验结果与 ByteDance 部署 → P10 Outline。**引言有 3 个图（Fig.1–3）**，贡献没有用 bullet 列表，而是两段散文。
- **章节顺序与篇幅**：I Intro（~1.6 页）→ II Related Work（~0.8 页，紧跟引言）→ III Preliminaries（~1.6 页：Leiden 回顾 + Alg.1 + Example 1 + Problem 1 + 记号表 + Def.1–2）→ IV Theoretical Analysis（~2.3 页：boundedness、Theorem 1、Table II、vertex optimality、γ-density、Lemma 1–4、Observation 1–3、扩展到 supergraph）→ V HIT-Leiden（~3 页：Fig.7 设计依据图，Alg.2–6，复杂度）→ VI Experiments（~2.5 页）→ VII Conclusion。
- **Related Work 分类**：按"社区检测指标"分两类：modularity-based CD（静态 → 动态维护）与 other metrics-based CD（SCAN、SBM、谱聚类、GNN，各自的动态扩展）。
- **好的写作技巧**：
  - 一个贯穿全文的 *running example*：Fig.1 的 8 顶点图依次出现在 Example 1（Leiden 静态过程，Fig.4/5）、Example 3（supergraph 上的变化）、Example 5（superedge 压缩）、Example 6（HIT-Leiden 第二轮迭代，Fig.9/10）。读者始终在同一张图上理解每一步。
  - **Fig.7 "design rationale" 图**：把 Assumption/Lemma/Observation 与算法组件之间的依赖画成箭头图，让审稿人一眼看出"理论是如何导出算法的"。这一手法很值得借鉴。
  - 用一张 Table II 把"已有方法 vs. 本文"的时间复杂度和是否 relatively bounded 并列，作为理论贡献的视觉摘要。
  - 伪代码风格：IEEE algorithm2e 风格，Input/Output 明确，正文逐行引用（"lines 2–7"）。
  - 一句短引用示例：作者把 boundedness 称为 "a powerful tool for analyzing incremental algorithms"——用权威框架为分析定调。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **"静态经典算法 + 动态维护"的稳定题型**，对象选得好：Leiden 当下因 GraphRAG 而热门，且已有维护工作缺理论——"热点算法 × 理论空白"。
2. **理论框架借力**：直接借用 Fan et al. 的 (relative) boundedness 给出"已有方法 unbounded / 本文 relatively bounded"的干净对比，让一个工程味较重的工作具有可陈述的理论贡献。
3. **工业背书与真实规模**：ByteDance 合作、4B 边内部数据集、部署声明、fraud-ring 实际业务（58.3M 顶点 / 26 天 / 每天约 0.5M 更新）与 GraphRAG token 成本节省，把"为什么要快"讲得很实。
4. **夸张但可信的加速比**（up to 10^5×），且质量通过两个维度（modularity + γ-density 比例）证明不降。
5. **可借鉴**：(a) 用 Lemma 刻画"何时某顶点会被影响"并配合"在实际参数下这些条件几乎不满足"的 Observation 来合理化剪枝；(b) 一张 design-rationale 图；(c) 贯穿全文的单一 running example；(d) 把应用研究放附录、正文只保留核心性能实验，以节省 12 页篇幅。
- **可追问的弱点（可作为后续工作切入点）**：质量无理论保证（Observation 3 是经验观察）；无并行版本；只处理无向图；没有消融（去掉 inc-refinement 用重算替换等）；AFF 由算法自身定义。
