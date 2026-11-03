# Effective and General Distance Computation for Approximate Nearest Neighbor Search (ICDE 2025, Regular)
- Source of full text: arXiv 2404.16322v4 (17 Jan 2025, camera-ready 对应版本)；代码 github.com/mingyu-hkustgz/Res-Infer；部分证明与实验放在 technical report [31]。FULL TEXT READ: yes（正文 + 参考文献全部读完；technical report 未读）
- Length: arXiv 版 13 页（正文约 12 页 + 1 页参考文献，双栏 IEEE 格式）；10 个 figure（Fig.5 一张图含 28 个子图）；3 个 table（符号表、数据集表、近似精度表）；2 个 algorithm；40 篇参考文献（其中 [24] 与 [37] 是同一篇重复引用）；约 4 个编号公式；1 个 Theorem + 2 个 Lemma（Lemma 1 引自 ADSampling，Lemma 2 为本文），正文不给完整证明（推到 TR）
- 作者：HKUST(GZ) + Ant Group（Mingyu Yang, Wentao Li, ..., Wei Wang），典型"学术+工业落地"组合

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：加速 HNSW/IVF 等 AKNN 索引里的距离计算。
- **本质问题**：在 candidate generation + refinement 框架中，refinement 阶段对每个候选 p 只需回答一个**判定问题** "dis(p,q) > τ ?"（τ 为结果堆的最大距离），而不必算出精确距离。于是问题被还原为：
  - 输入：数据集 S ⊂ R^D、查询 q、当前阈值 τ、某种近似距离 dis′（投影或量化得到）；
  - 输出：对每个候选给出"剪枝 / 不剪枝"决策（必要时回退到精确距离）；
  - 约束：误剪枝率（把真近邻错剪）低，即 recall 损失可控；
  - 目标：最小化平均扫描维数 / 计算代价（等价于最大化 pruned rate）。
  这就是 Gao & Long (SIGMOD'23, ADSampling) 提出的 Distance Comparison Operation (DCO) 视角，本文在其上改进。
- **为什么现有方法不够（2 个根因）**：作者把 SOTA ADSampling 的缺陷归结为"过度依赖 random projection"，拆成两个 gap：
  1. **Effectiveness gap**：随机投影不是误差最小的正交投影，近似距离偏差大 → 需要更多增量维度才能做出判定；
  2. **Generality gap**：ADSampling 的误差界来自 JL lemma，只对随机投影成立，无法套到 PQ/OPQ 等量化距离上。
  证据：Fig.1（DEEP1M 上 PCA 与随机投影的估计误差分布对比，PCA 更集中）；Fig.2（DEEP/GLOVE 上经验误差分布与 3σ 界、ADSampling 实际使用的 10σ 界对比，显示 ADSampling 的界过于保守）。注意：gap 的证据放在方法章节里（§IV），而不是引言的 Figure 1 motivating example。
- **问题定义形式**：没有独立的 "Problem Definition" 环节和复杂度结论；§II-A 只用文字定义 KNN/AKNN（squared Euclidean），§III "Problem Analysis" 专门剖析 SOTA 的机制与局限——这是"改进某一 SOTA"类论文的典型写法：把 Problem Analysis 单列一节。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把 DCO 的"误差界"从依赖投影矩阵的理论常数改为依赖数据分布的量——用 PCA（最优正交投影）让残差方差最小化并以 Gaussian 分位数作界（DDC_res）；进一步把误差界当作可学习参数，把"是否剪枝"重述为以 (dis′, τ, 额外特征) 为输入的线性二分类问题（DDC_pca / DDC_opq），从而与近似距离来源解耦。
- **技术组件**：
  1. **Distance decomposition**（Eq.2）：旋转后 ‖x−q‖² = 可预计算项 C1 − 前 d 维内积 C2 + 残差内积误差项 ε=−2⟨q_r,x_r⟩，O(d) 得近似距离 → 解决 effectiveness gap 的分析基础；
  2. **PCA projection + Gaussian quantile bound**（Theorem 1 + Lemma 2 + Alg.1/2）：PCA 在所有正交投影中最小化残差方差；高斯假设下最小方差 ⇒ 最小分位数界；配合增量维度（Δd）的 Incremental-DDC_res → 解决 effectiveness gap。这是"真正的新东西"之一，但理论本身（PCA 方差最大化）是经典结论，新意在把它与 DCO 误差界连接。
  3. **Data-driven distance correction**（§V）：把 f(dis′) > τ ⇔ dis > τ 写成分类，用 logistic regression + SGD 学 m1、β；再对 β 二分搜索以满足训练集上 label-0（真近邻）的 target recall r=0.995 → 解决 generality gap，是本文最核心的新意。
  4. **工程扩展**：DDC_opq 额外用"点到其量化中心距离"作特征；OOD query 讨论（用约 100 个 OOD 查询重训）；PCA/OPQ 矩阵用采样训练使预处理与规模基本无关。
- **理论保证**：Theorem 1（PCA 最小化残差方差，在所有正交投影中最优）、Lemma 2（高斯假设下最小化方差即最小化分位数误差）。均为**在 Gaussian 假设下的最优性**，没有对端到端 recall 的保证；data-driven 部分完全无理论保证，只有经验 recall target。作者坦率承认 GLOVE 上高斯拟合有偏差，并说可由学习方法弥补。

## 3. 实验设计 (Experiments)
- **实验列表**（Exp-1..8，§VII）：Exp-1 时间-精度权衡主结果；Exp-2 target recall 敏感性；Exp-3 预处理时间与空间；Exp-4 与 FINGER 对比；Exp-5 可扩展性（SIFT100M 切成 20M–100M）；Exp-6 扫描维数比与 pruned rate 的机制分析；Exp-7 不接索引的纯近似精度（Recall@100, Table III）；Exp-8 Ant Group 人脸检索落地。
- **数据集**：8 个公开数据集（Table II）——MSONG(420d, ~992K)、GIST(960d, 1M)、DEEP(256d, 1M)、WORD2VEC(300d, 1M)、GLOVE(300d, 2.2M)、TINY5M(384d, 5M)、TINY80M(150d, 79M)、SIFT100M(128d, 100M)；外加 1 个 Ant Group 私有数据集（1M、512d 人脸）。规模 1M–100M。
- **基线**：原始 HNSW/IVF（精确距离）、HNSW++/IVF++（ADSampling，SIGMOD'23）、FINGER（WWW'23，仅 HNSW）。基线数量少（实质上 2 个 DCO 方法），但都是当时最新且含 SIGMOD 工作；共 11 个算法变体（2 个索引 × 5 种距离计算 + FINGER）。
- **指标**：recall@20 / recall@100、QPS（端到端）、扫描维数比、pruned rate、预处理时间/空间。
- **环境**：Intel Xeon Platinum 8352V 2.1GHz、512GB 内存、g++ 11.4 -O3，**刻意关闭 SIMD**（与 ADSampling 设置一致）——这一点后来被论文 3（DCO benchmark）点名批评为不贴近真实部署。HNSW M=16, efConstruction=500；IVF 4096 簇；训练 10,000 条训练查询、500,000 个负样本。
- **实验类型**：主结果 ✓、参数敏感性（target recall）✓、可扩展性 ✓、效率（时间/空间）✓、机制分析 ✓、工业 case study ✓；**没有严格意义的消融**（DDC_res/pca/opq 三个变体互相充当消融）。
- **结果呈现**：主结果全部用 recall-QPS 曲线图（Fig.5 共 28 子图）；只有 Table III 是表。提升表述："1.6 to 2.1 times" speedup over ADSampling（摘要与贡献）、"2x over HNSW, 1.45x over ADSampling on TINY80M"、"20% to 30% faster than FINGER"、Ant Group "reduces retrieval time by 35%, throughput +55.25%"。还给出一条可操作的 insight：数据方差偏斜（PCA 32 维保留 67%/82% 方差的 GIST/SIFT）时 PCA 类方法更优，方差均匀（WORD2VEC 36%、GLOVE 18%）时 OPQ 类更优。

## 4. 写作结构 (Writing)
- **标题模式**："Effective and General X for Y"——标题里的两个形容词直接对应两个 gap（effectiveness、generality），一一呼应贯穿全文。
- **摘要逐句功能**：S1 背景（AKNN 重要且难）→ S2 距离计算主导运行时间 → S3 现有方法用近似距离牺牲精度 → S4 SOTA ADSampling 的做法 → S5 ADSampling 在 effectiveness 与 generality 上受限、根因是依赖随机投影 → S6 方法（利用数据分布做正交投影 + 数据驱动校正、解耦）→ S7 实验（1.6–2.1×，精度更高）→ S8 工业落地（集成进 Ant Group 搜索引擎）。
- **引言逐段功能**：P1 KNN/AKNN 背景 → P2 四类 AKNN 算法 + 抽象出 candidate generation/refinement 框架 → P3 refinement 中距离计算占 80%/90% 时间（引用数字证明问题重要）→ P4 "The State-of-the-art" ADSampling 机制 → P5–P6 两个加粗小标题 "Effectiveness" / "Generality" 分别陈述 gap → P7 "Our Idea"：根因 + 以问句形式提出研究问题 → P8–P9 方案概述 → "Contributions" 4 条（每条带章节号：§III 分析 SOTA、§IV、§V、§VII）→ 引言内嵌 "Related Work" 段（ADSampling vs FINGER、learning-based ANNS）。**没有 Figure 1 motivating example**，Fig.1 出现在 §IV。
- **章节顺序与篇幅**：I Intro（~1.8 页，含 related work）→ II Preliminaries（~1 页）→ III Problem Analysis（~0.7 页）→ IV PCA 方法（~2.3 页）→ V 通用数据驱动方法（~1.5 页）→ VI 方法分析（复杂度/空间，~0.7 页）→ VII Experiments（~3.5 页）→ VIII Conclusion（极短）。Related Work 不单列，压缩进引言末尾两段——节省篇幅给实验。
- **好的写作技巧**：
  - 用 "Our Idea" 小标题 + 一个研究问句收束 gap，例如作者问能否开发既保留误差界又 "exploiting the properties of data points"（短引，<15 词）。
  - 每个方法组件都配一个 "Example"（Fig.3/Fig.4）与一个 "Remark"，并显式说明新方法如何退化为旧方法（m1=1, β=m·σ 时数据驱动版等价于 DDC_res），增强统一性。
  - 局限性主动暴露（OOD query 小节、GLOVE 高斯拟合偏差），把额外实验推到 TR 以节省篇幅。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **gap 定义极其清晰、可验证**：两个形容词（effective/general）= 两个 gap = 两个方法章节 = 标题，审稿人可以逐项核对。
2. **"插件式"贡献**：DCO 层的改进对 HNSW 与 IVF 同时有效，适用面广；且提供"选择指南"（方差偏斜度决定用 PCA 还是 OPQ）。
3. **理论 + 数据驱动结合**：最优性定理给方法正当性，学习方法给通用性；即使理论只在 Gaussian 假设下成立，配合 Fig.2 的经验验证也足够说服。
4. **规模与落地**：100M 规模可扩展性 + Ant Group 线上集成，契合 ICDE 对工程价值的偏好。
5. **可借鉴点**：针对一个强 SOTA（SIGMOD'23）做"根因分析 → 定向修复"的写法；Problem Analysis 单列一节；贡献列表带章节指针。**风险提示**：关闭 SIMD、基线少、无端到端理论保证——这些正是后续 EAB 论文（论文 3）攻击的点。
