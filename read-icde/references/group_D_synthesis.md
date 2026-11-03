# D 组综合：图算法（ICDE 最大主题）+ 时间序列 — 共性模式与研究空白

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

## 1. 问题框架（Problem framing）的共性

观察到三种可复用的叙事模板：

**模板 A：静态算法已成熟 → 动态 / 大规模维护**（#1 HIT-Leiden、#3 DMI，以及未读的 ego-betweenness 论文，其标题也是这种结构）
- 固定句式："X 在 Y 场景中被广泛使用 → 真实图是动态的 → 从头重算代价大 → 已有维护工作要么不存在（DMI：'there is no prior work'），要么缺乏理论、对大图低效（HIT-Leiden：只有一篇 [14]）"。
- 题目结构固定："Maintaining <经典算法/度量> in/at <Large Dynamic / Billion Scale>"、"Scalable Algorithm for Dynamic <问题>"。
- 问题定义非常短：一个 Problem（"给定 G、旧结果、ΔG，返回新结果"），不重新证明 hardness，而是继承静态问题的 hardness（DMI 一句话："MQCP NP-hard，因此 DMQCP 也 NP-hard"）。
- 理论贡献重心从 hardness 转向 **更新代价的刻画**：HIT-Leiden 用 Fan et al. 的 (relative) boundedness，证明已有算法 unbounded（Theorem 1），自己 relatively bounded；DMI 按单次更新给 Õ(d_max²) / Õ(d_max)。
- 动机证据：工业规模数字（HIT-Leiden：ByteDance 10^8 顶点、4×10^9 边、要求 10^5 条更新在分钟级完成）比 motivating figure 更有说服力。

**模板 B：静态 SOTA 有明确瓶颈 → 新技术打破瓶颈**（#2 CFCM、#5 HBBMC）
- 先在 Preliminaries 中详细复述 SOTA（CFCM 有专门的 "State-of-the-art Method + Performance Discussion" 小节；HBBMC 先讲 VBBMC 再讲 EBBMC），把瓶颈落到一个复杂度项上（CFCM：Õ(kε⁻³m) 依赖 m；HBBMC：O(nδ·3^{δ/3}) 依赖 δ）。
- 贡献即"把复杂度中的 m 换成 n"或"把 δ 换成 τ<δ"，并配一个"在真实图上成立"的条件论证（HBBMC：δ ≥ τ + 3lnρ/ln3 在 111/139 个图上成立；CFCM：scale-free 图上 d_max(S∪T) 很小）。

**模板 C：评测范式有缺陷 → 新基准 → 反直觉发现**（#4 TS-Fault，EAB）
- 批判"单一干净数据误差排名"→ 把问题重新定位为 *数据质量* 问题（对 ICDE 定位至关重要）→ 形式化框架 + 分类法 → 大规模评测 → 3–5 条可一句话传播的发现。
- 用两张"定位表"（基准代际演进、鲁棒性研究四象限）证明空白象限存在。

## 2. 方法结构（theory → algorithm → optimization）

| 论文 | 理论层 | 核心算法层 | 优化/工程层 |
|---|---|---|---|
| HIT-Leiden | boundedness 分析（Thm 1）；Lemma 1–4 刻画"哪些顶点可能被影响"；Observation 2–3 + Assumption 1 论证可忽略的情形 | inc-movement / inc-refinement / inc-aggregation 三阶段，在每层 supergraph 复用 | 复用 SIGMOD'24 的 constant-time 动态连通性索引；def-update 延迟同步 |
| DMI | 复用 MinHash 复杂度（Lemma 1–2）；局部修复的充分条件（Lemma 3） | 增量 γ-degree 剪枝 + 候选列表 + 删除时 1/2 点修复 | 周期性重建（Batch）；两种 sketch 变体 |
| CFCM | 森林计数 ↔ 电流（Lemma 3.1–3.3）；JL、Bernstein、谱稀疏化；Thm 3.11 / 4.7 近似比 | ForestCFCM（基础版）→ SchurCFCM（增强版） | 自适应采样提前停止；72 线程并行；|T*| 的选取启发式 |
| HBBMC | Thm 1–2 新复杂度界；Thm 3–4 近乎输出最优的提前终止 | EBBMC → HBBMC（根边分支 + 其余点分支） | 图归约 GR（复用）；四个辅助集合加速集合交 |
| TS-Fault | Def.1–2、风险度量 WC/AVG、场景参数四性质 | 窗口重要性分数 + 四种 fault 算子 + 难度映射 | 可组合算子、held-out Θ（未执行） |

共性：
1. **"key insight"几乎都是一个"局部性 / 有界性"性质**：HIT-Leiden——更新只影响 N²(AFF)，子社区 γ-connectivity 可用连通分量近似；DMI——更新只影响端点邻域的 containment/γ-degree；HBBMC——truss 边序把每个子问题限制在 τ 个顶点；CFCM——以高度数节点为辅助根后随机游走很快被吸收。写论文时应当能用一句话说出"哪个界/哪个局部性让算法成立"。
2. **"basic 版 → enhanced 版"双算法结构**很常见（CFCM 的 Forest/Schur，HBBMC 的 EBBMC/HBBMC，DMI 的 bf/bt 两种 sketch），两版之间的对比天然构成消融。
3. **复杂度陈述方式**：每个算法后一段 "Time Complexity."（DMI、HIT-Leiden）或一个 Theorem（HBBMC、CFCM）；动态论文按"单次更新"或"受影响区域"陈述，静态论文按图参数（δ, τ, d_max, 直径）陈述；"for real-world graphs" 这样的限定语被广泛接受（CFCM 的 Õ(n)、DMI 的 near-linear）。
4. **质量保证是动态论文的普遍短板**：HIT-Leiden 和 DMI 都没有质量/近似界，都用"modularity 差异 < 0.01"、"density ∈ [0.91, 1.00]"一类经验结论代替——审稿人接受，但这是可以超越的地方。

## 3. 实验协议的共性

- **数据来源**：SNAP、KONECT、Network Repository 是标准来源；动态论文的"更新流"都是作者自造的：HIT-Leiden——按时间戳排序，前 80% 建初始图，滑动窗口 b∈{10..10^5}、r=9 批；无时间戳的 it-2004 随机打乱；DMI——rand / inc / del / temp / tinc 五种生成方式，最多 10^5 次操作。**没有公认的动态图基准**。
- **基线**：动态论文的必有基线是"每次从头重跑静态算法"（ST-Leiden、FastNBSim/NBSim/NuQClq 每次更新重跑），外加少量已有增量方法或自建的朴素增量变体（DMI 的 NSF）。基线数量都只有 3–4 个——**问题新颖时基线少是可以接受的**。
- **指标**：效率 = 总运行时间（log 轴）；质量 = 问题自身的目标函数（modularity、密度/大小、CFCC）+ 结构性质（HIT-Leiden 的 γ-density 比例）；DMI 额外报告更新时延中位数/最大值与内存峰值。
- **实验类型的"标配清单"**：主结果 → 参数敏感性（batch size、γ、k、ε、t 等）→ 可扩展性（操作数 Q、n、ρ）→ 组件时间分解或消融 → 内存 →（可选）长期稳定性 / case study。HIT-Leiden 把 Graph-RAG 与 fraud-ring 两个应用放在附录，正文只放核心性能实验。
- **硬件**：图算法论文都是单台大内存 Xeon 服务器、C++、多数单线程（CFCM 用 72 线程）；EAB 论文（TS-Fault）反而没有报告硬件——这是 EAB 稿件容易被挑的点。
- **结果呈现与措辞**：维护类论文强调数量级（"up to five / four orders of magnitude"），静态经典问题强调倍数（"up to 4.38×"、"up to 370×"），EAB 强调统计量（Spearman ρ、p 值、失败计数）。"up to"几乎出现在每一篇摘要中。

## 4. 写作结构的共性

- **章节顺序**：Intro → (Related Work) → Preliminaries/Problem → [Theory] → Algorithm(s) → Experiments → (Related Work) → Conclusion。Related Work 的位置与论文类型相关：问题驱动/动态论文（HIT-Leiden、DMI）和 EAB（TS-Fault）放在第 II 节，用来定位问题空白；理论/算法驱动论文（CFCM、HBBMC）放在实验之后，因为引言和 Preliminaries 已经交代了 SOTA。
- **引言**：一般 5–7 段，结构为 应用背景 → 经典模型/SOTA → gap（可能不止一个，常附工业或理论证据）→ 方法概览 → 贡献（3–4 条 bullet，常带 Section 编号）→ 章节安排。理论型论文引言中没有 Figure 1；HIT-Leiden 在引言放了 3 张流程/示例图。
- **定义与引理的位置**：所有定义集中在 Preliminaries，记号表（Table I）几乎是标配（HIT-Leiden、CFCM）；Lemma 紧挨使用它的算法；证明要么放附录 / full version（HIT-Leiden 用 GitHub 托管 full version 并在正文引用 [53]），要么省略（DMI 的 Lemma 3 "omitted due to space"）。
- **伪代码风格**：algorithm2e 风格，Input/Output 明确，正文逐行引用（"lines 2–7"）；递归过程以 Procedure XXX_Rec 命名；复杂算法拆成多个子过程，彼此用"lines x–y of Algorithm k"引用以节省篇幅。
- **值得学习的单点技巧**：HIT-Leiden 的"design rationale"图（Fig.7，画出 Assumption/Lemma/Observation → 算法组件的依赖关系）与贯穿全文的 running example；CFCM 每节开头的"本节推导路线图"；HBBMC 的数据集表直接列出理论参数 δ、τ、ρ，以及"与自己前作的差异"专段；TS-Fault 的"RQ 先答后证"（每个 RQ 第一句就是答案）与 Threats to Validity。
- **新规范**：DMI 包含 "AI-Generated Content Acknowledgment"（声明 ChatGPT/Gemini 只用于润色与实验代码辅助）——ICDE 2027 投稿应准备同类声明。

## 5. 具体研究空白（gaps）

1. **动态社区/稠密子图维护缺少质量保证**（HIT-Leiden Sec.IV-B Observation 3 与 Sec.V-D；DMI Sec.IV-E）。两篇都只证明代价（relative boundedness / 每次更新 Õ(d_max)），质量只靠经验（>99% 子社区仍满足 γ-density；密度 ≥0.91）。可做方向：带 *可证明的 modularity 或 quasi-clique 规模漂移界* 的维护算法，或带误差监控的"按需局部重算"。

2. **"何时重建"缺少理论——重建调度问题**（DMI Alg.3–4 每 Batch=5000 次操作固定重建，Fig.6 与 Table VIII/IX 显示重建占总时间 8%–89%；HIT-Leiden 附录 B Fig.22 第 276 批出现尖峰）。把"重建时机"形式化为在线决策问题（基于质量漂移估计或摊还代价的自适应触发），对两类维护算法都适用。

3. **动态图算法缺少统一基准（模板 C 对图领域的空白）**（HIT-Leiden Sec.VI-A 的滑动窗口协议 vs. DMI Sec.VI-A 的 rand/inc/del/temp 生成方式，彼此不可比；DMI 的最大图只有 22M 边）。可以仿照 TS-Fault 做一个 EAB：标准化的更新流生成器（时序、突发、对抗、删除密集）、时延分布、长期质量漂移和内存指标，并系统比较已有的 Louvain/Leiden/k-core/clique 维护算法。

4. **静态 SOTA 的动态化仍有大量空位**：
   - CFCM（Sec.VII 只讨论边选择扩展）只有静态版本——*动态图上的 group CFCC 维护*（森林样本能否在边更新后局部修复？）完全空白；
   - HBBMC 是单线程静态（Sec.VI 列出了 16 篇并行 MCE，但没有把 hybrid 分支与 early termination 用于并行或动态）——*hybrid 分支的动态 MCE / 并行 MCE*；
   - DMI 结论中点名的 k-plex、δ-clique、defective clique 的动态版本。
   这是模板 A 的"现成选题池"；但要注意 arXiv 上同期已有另一篇动态 quasi-clique 论文（2606.05809），说明热点方向竞争很快。

5. **"near-linear" 依赖经验假设、缺少参数化分析**（CFCM Lemma 3.7/4.6 中 d_max^{2τ+2} 对直径 τ 是指数的，只靠 scale-free 假设压下；HBBMC Remarks 的条件 δ ≥ τ + 3lnρ/ln3 只在 80% 左右的真实图成立）。可做：给出更紧的、可在线验证的参数化界，或在不满足条件的图上自适应选择框架（HBBMC Table IV 的切换深度 d 目前只是经验选择 d=1）。

6. **十亿级规模仍是稀缺的卖点**：本组只有 HIT-Leiden 用到 4B 边（且是不公开的 ByteDance 数据）；DMI ≤22M、CFCM/HBBMC ≤106M。未读的 ego-betweenness 论文标题即是"at Billion Scale"，说明审稿人看重这一点。可做：在公开的十亿级图（如 LAW 的 it-2004、uk-2007、twitter 等）上给出 I/O 或内存受限的维护算法。

7. **TS-Fault 的鲁棒性指标混淆了"鲁棒"与"对输入不敏感"**（Sec.V-D 定义 r = AVG/L；Table V/VIII 中 LSTM/GRU 的 r≈1.0、难度斜率≈1.0，但它们干净 MSE 只是中游，且 Naive 在 Mode III/IV 下误差从 1.24 涨到 129）。同时目标被固定为干净未来（Eq.1），在真实 regime 切换时"跟随输入"可能才是正确行为。可做：区分"应当忽略的故障"和"应当跟随的变化"的评测协议，或补充敏感度/信息利用度指标。

8. **只评测不修复：面向预测的故障检测与数据修复是数据工程空白**（TS-Fault Sec.VII-D 与结论只给出诊断；组合故障 Eq.19 与 held-out Θ 都留作未来工作；每个配置只有 20 对窗口、无方差、无硬件，6 个数据集中 4 个是 ETT）。可做：针对 mechanism-level 故障（Mode III/IV）的"检测 → 修复 → 预测"管线，在 TS-Fault 上量化修复带来的鲁棒性提升，并扩展到交通、金融、临床领域——这正好把 ML 鲁棒性问题落到 ICDE 的数据质量主线上。

## 6. 对 ICDE 2027 投稿的直接建议（基于本组观察）
- 如果走图算法：优先模板 A（"静态 SOTA → 动态 / 十亿级维护"），在理论上借用已有框架（relative boundedness、参数化复杂度），并争取 **一个有质量保证的结果**，以区别于 HIT-Leiden/DMI 只给代价界的做法。
- 必备元素：一句话 key insight（局部性/有界性）、Problem 定义 + 复杂度定理、"basic → enhanced"双算法、对比"每次从头重跑"的基线、batch size/参数/可扩展性/组件分解/内存实验、"up to X×"措辞、公开代码，以及（如篇幅不够）托管在 GitHub/arXiv 的 full version。
- 如果走 EAB：学习 TS-Fault 的"定位表 + RQ 先答后证 + Threats to Validity"，但要补上硬件、开销、方差，并避开它在指标设计上的漏洞。
