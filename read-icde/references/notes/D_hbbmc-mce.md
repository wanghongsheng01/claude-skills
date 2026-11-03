# Maximal Clique Enumeration with Hybrid Branching and Early Termination (ICDE 2025, Regular) —【自选论文 #5】
- **选择理由**：在 ICDE 2025/2026 官方录用列表中的约 20 篇 cohesive-subgraph（core/clique/truss/plex）论文里，逐一检索 arXiv，确认有开放全文且 arXiv 注释写明 "Accepted by ICDE'25" 的有两篇（本文；"Finding Near-Optimal Maximum Set of Disjoint k-Cliques…"）。选本文是因为它最能代表 ICDE 图算法论文的"硬核"模板：经典 NP-hard 枚举问题 + branch-and-bound + **改进最坏情况时间复杂度**的定理 + 剪枝/提前终止 + SNAP/NetworkRepository 数据集 + 一张张运行时间表格。同时它是静态算法，可以和本组三篇"动态维护"论文形成对照（"静态 SOTA → 动态维护"中的那个"静态 SOTA"长什么样）。
- Source of full text: arXiv 2412.08218v1（2024-12-11，cs.DB；Kaixin Wang [BJUT], Kaiqiang Yu, Cheng Long [NTU]）；FULL TEXT READ: yes（正文 12 页 + 附录 A–D + 参考文献全部读过）
- Length: 全文 17 页（arXiv 完整版）= 正文约 12 页（p1–p12）+ 附录约 3.5 页（A：已有 VBBMC 算法复杂度及两个补证；B：Theorem 2 的完整证明；C：2-plex/3-plex 例子；D：合成数据实验）+ 参考文献约 1.5 页；Figures 5 个（正文仅 Fig.1，附录 Fig.2–5）；Tables 7 个（正文 I–VI 全是数据集/运行时间表，附录 VII 复杂度汇总）；References 66 条；编号 Equations 8 个；Theorem 6 个（正文 1–4，附录 5–6）；Lemma 2 个（附录 B）；Definition 1 个；Problem 1 个；Algorithm 10 个（正文 8 个，附录 2 个复现已有算法）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：枚举图中所有极大团（MCE）。
- **本质问题**：在最坏情况输出规模为 3^{n/3}（Moon–Moser 图）的枚举问题中，**用图的稀疏性参数刻画并降低搜索树规模**。已有最优界 O(nδ·3^{δ/3})（δ=degeneracy，BK_Degen）。本文的问题是：能否用比 δ 更小的参数（truss 相关数 τ < δ）给出更好的上界，并在实践中更快。
  - 输入：无向简单图 G；输出：全部极大团；无近似、无参数。
- **作者给出的 gap**：(1) 所有 SOTA 都用 *vertex-oriented* Bron–Kerbosch 分支，近年的改进（BK_Rcd、BK_Fac、图归约 [15]）只在实践层面加速，没有改进理论界（作者在附录 A 甚至自己补证了 BK_Rcd 为 O(nδ·2^δ)、BK_Fac 为 O(nδ·3.14^{δ/3})，说明它们理论上还更差）；(2) *edge-oriented* 分支（来自同组 k-clique listing 的 EBBkC [19]）能把子问题规模压到 τ，但若直接用于 MCE 会产生 O(m·2^τ) 个分支。gap 的证据是 **复杂度对比** 而非实验图——典型的理论驱动型论文。
- **问题定义形式**：Definition 1（clique）+ Problem 1（MCE），以及一句 hardness 评论（极大团数可达 3^{n/3}）。整个 Preliminaries 不到半页。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：**只在根分支用 edge-oriented 分支（按 truss-based 边序，子图规模 ≤ τ），之后全部切换为带 pivot 的 vertex-oriented 分支**——兼得"小子问题"与"pivot 剪枝"，得到 O(δm + τm·3^{τ/3})；再对稠密候选子图（clique / 2-plex / 3-plex 且排斥集为空）用其 *补图只含孤立点、简单路径、简单环* 的拓扑性质直接构造全部极大团，跳过分支。
- **技术组件**：
  1. **EBBMC（edge-oriented BK branching，Eq.2–3，Alg.2–3）**：把边分支推广到 MCE 需要两处新设计——维护排斥图 g_X 以保证极大性检查与不重复；额外处理候选图中度为 0 的顶点（Eq.3，否则奇数规模的极大团会漏掉）。Theorem 1：O(δm + τm·2^τ)。
  2. **HBBMC（hybrid，Alg.4）**：根用 EBBMC、其余用 VBBMC + 经典 pivot（选在 g_C 中邻居最多的顶点）。Theorem 2：时间 O(δm + τm·3^{τ/3})、空间 O(m+n)。证明（附录 B）靠两个引理：Tomita 等的递推 F(n) ≤ max_k{k·F(n−k)} + O(n²) ⇒ O(3^{n/3})（Lemma 1），以及"三角形数 ≤ mτ"（Lemma 2）。**Remarks 给出何时更优的条件 δ ≥ max{3, τ + 3 ln ρ / ln 3}（ρ=m/n），并在 139 + 84 个真实图上统计：111/139、72/84 满足**——这是把"条件性理论改进"落地为"多数真实图成立"的标准论证。
  3. **Early termination（Alg.5–8，Theorem 3–4）**：2-plex 时把顶点分成 F/L/R 三个团，2^{|L|} 个极大团可直接按位枚举；3-plex 时补图最大度 ≤ 2，分解为路径/环，用 Enum_from_Path / Enum_from_Cycle 组合输出。两者时间 O(|E(g_C)| + ω(g_C)·c(g_C))，即"近乎输出最优"。检测条件可与 pivot 选择同时完成，每分支只多 O(|V(g_C)|)。该技术对 VBBMC/EBBMC/HBBMC 都适用且不改变最坏复杂度。
- **"真正的新东西" vs. 工程组合**：hybrid 分支 + 新复杂度界是理论核心；early termination 是新颖的组合观察；graph reduction（GR, [15]）是直接复用的工程组件。作者专门用一整段 "Differences between HBBMC and EBBkC [19]" 从递归树深度/宽度、正确性所需结构、"hybrid" 含义三方面与自己的前作划清界限——**主动回应"增量太小/自我重复"的审稿风险**，值得学习。
- **理论保证**：完整（6 个定理含正确性与复杂度；附录给出全部证明），但 HBBMC 的优越性是 *条件性* 的。

## 3. 实验设计 (Experiments)
- **实验目标**：(1) 与基线对比（Table II）；(2) 消融：HBBMC++ vs HBBMC+（无 ET）vs RDegen（Table III 前 3 列）；(3) hybrid 中 VBBMC 实现的选择（Ref++/Rcd++/Fac++，Table III 后 3 列）；(4) 切换深度 d∈{1,2,3}（Table IV，含递归调用次数）；(5) ET 参数 t∈{0,1,2,3}（Table V，含可提前终止分支比例）；(6) 边序的作用（truss vs degeneracy vs min-degree，Table VI）；附录 D：合成 ER/BA 图可扩展性（n 从 100K 到 10M，ρ 从 5 到 40，各 10 个随机图取均值，Fig.5）。
- **数据集**：16 个真实图（Network Repository），从 nasasrb（55K/1.3M）到 orkut（3.0M/106M）、socfba（3.1M/23.7M），表中同时列出 δ、τ、ρ——**把理论中出现的参数直接列进数据集表**，方便读者对照 Theorem 2 的条件。
- **基线（4 个）**：RRef、RDegen、RRcd、RFac（均来自 [15]，即 BK_Ref/BK_Degen/BK_Rcd/BK_Fac + 图归约 GR），都是最新 SOTA 的统一实现。
- **硬件**：Linux，2.10GHz Intel CPU，128GB 内存；C++；单线程；代码开源（GitHub wangkaixin219/HBBMC）。运行时间包含排序生成与递归枚举。
- **结果呈现**：**全部用表**（正文 6 张表，几乎无图）；提升表述："up to 4.38x faster than the state-of-the-art"、WE 4.0×、DB 2.94×；消融用贡献比例表述："on OR, the hybrid framework and early-termination technique contribute 41.7% and 58.3%"；合成数据 "average speedups of 1.84x and 1.94x"。加速倍数相对 10^3–10^5× 的维护类论文很"朴素"，但因为是改进了几十年的经典问题，几倍加速 + 理论改进已足够。

## 4. 写作结构 (Writing)
- **标题模式**："<经典问题> with <技术1> and <技术2>"——直接把两个技术贡献写进标题。
- **摘要逐句功能**：S1 问题重要性 → S2 已有方法共性（vertex-oriented BK 分支）→ S3 我们提出 HBBMC（hybrid 定义）→ S4 效果（更有效剪枝 + 在多数真实图成立的条件下复杂度更优）→ S5 第二个技术 early termination → S6 其通用性 → S7 实验。
- **引言逐段功能**：P1 定义 + 应用（社区检测、蛋白质功能预测、文档聚类、图像、电商频繁项）→ P2 BB 框架与 BK 分支的详细描述（三元组 (S, g_C, g_X)）→ P3 两个已有改进方向（pivot 剪枝；用 degeneracy 序缩小子问题），SOTA 复杂度 O(nδ·3^{δ/3})，以及"近期工作只在实践中改进" → P4 观察：k-clique listing 中的 edge-oriented 分支能把规模界到 τ<δ → P5 迁移到 MCE + 问题（O(m·2^τ)）+ hybrid 方案 + 新复杂度 + 成立条件 → P6 early termination 的直觉（clique / t-plex 的补图拓扑）→ 贡献 **3 条 bullet**（每条带 Section 编号）+ 章节安排。**引言没有图**，但用文字把整个算法讲完了——引言篇幅约 2 页。
- **章节顺序与篇幅**：I Intro（~2 页）→ II Problem & Preliminaries（~0.5 页）→ III Branch-and-bound Algorithms（~3.5 页：已有 VBBMC → 新 EBBMC → HBBMC，"先讲旧框架再讲新框架"的递进式结构）→ IV Early Termination（~2.3 页）→ V Experiments（~3 页）→ **VI Related Work（~0.8 页，放在实验后）**：BB 类 vs reverse-search 类（polynomial delay 但实践慢）、并行 MCE、其他图类型/对偶问题 → VII Conclusion。
- **伪代码风格**：每个框架一个 Algorithm，递归过程以 "Procedure XXX_Rec(S, g_C, g_X)" 命名；后续算法以"lines 6–7 of Algorithm 2"互相引用，减少重复。
- **running example**：正文没有贯穿全文的例子，只有 Fig.1 的局部示意；具体小例子被放到附录 C（2-plex、3-plex 各一个）。这一做法节省正文篇幅，但降低了可读性。
- **一句短引用**：作者强调 HBBMC 是 "the first algorithm that integrates the edge-oriented branching strategy and the vertex-oriented branching strategy"——"first" 定位语句。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **在经典问题上改进最坏复杂度**：MCE 自 1973 年 BK 以来被反复研究，能给出新的（条件性）更优界本身就是强贡献；并用 223 个真实图统计条件成立率，弥补"条件性"的弱点。
2. **两个正交贡献**（hybrid 框架 + early termination），且 ET 可插入任何 BB 框架——提高了"通用性"得分。
3. **系统的消融**：Table III–VI 分别隔离框架、VBBMC 实现、切换深度、t、边序五个设计维度，每个设计选择都有表格支持。
4. **与前作差异的显式论证**，降低"增量过小"风险。
5. **可借鉴**：(a) 数据集表中列出理论参数（δ, τ, ρ）；(b) 在 Remarks 中把复杂度比较的条件转化为可验证的图统计；(c) "已有框架 → 新框架 A → 混合框架 B" 的递进叙事；(d) 在附录中补证已有算法的复杂度，形成完整的复杂度对比表（Table VII）。
- **可追问的弱点（gap 来源）**：只有单线程静态算法（并行与动态均未涉及，而相关工作列出了 16 篇并行 MCE）；hybrid 切换深度 d 只做了经验选择（d=1），无自适应理论；t 只到 3（4-plex 的补图最大度 3，不再是路径/环，需要新技巧）；附录图例误写为 "HBBkC++"，说明附录打磨不足；加速倍数有限（≤4.38×）。
