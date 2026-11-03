# 03 深读报告：ICDE 偏好方向的科学问题、研究方法、实验方法、写作方法与录用规律

## 0. 读了什么（诚实说明）
四个小组共精读 **21 篇 ICDE 2025–2027R1 录用论文**，其中 **17 篇读了全文**（arXiv/作者主页/作者 GitHub 版本），4 篇因 IEEE 闭源且无开放版本只读了摘要或元数据（CYANSQL、BOND、Tag-Filtered ANNS、"Beyond Majority Voting" 未找到），另用 3 篇同主题、有全文的 ICDE 论文作替补。每篇一份笔记（`A_*.md`…`D_*.md`，统一模板），每组一份综合（`*_synthesis.md`）。IEEE Xplore 的反爬验证没有绕过；若你有机构访问权，可补下载上述 4 篇放进 `pdfs/`。

| 组 | 方向（第 2 阶段排名） | 全文精读 |
|---|---|---|
| A | LLM for Data：成本/准确率权衡 | SPARQ'26、CARROT'26、CSV-Shapley'25、ZenDB'25（BOND'26 仅摘要） |
| B | LLM for Data：Text-to-SQL 选择与评测 | KaSLA'26、FusionSQL'26、SQLMorph'26(EAB)、CycleSQL'25、HEXGEN-FLOW'26 |
| C | 向量检索 + EAB | DDC'25、DCO-Benchmark'26(EAB)、XRAG'26(EAB)、RLESI'26(EAB)（Tag-Filtered'25 仅摘要） |
| D | 图算法 + 时间序列 | HIT-Leiden'27R1、DMI quasi-clique'27R1、CFCM'25、HBBMC MCE'25、TS-Fault'27R1(EAB) |

---

## 1. 科学问题的分类与本质

把 21 篇的问题定义还原成"输入—输出—约束—目标"后，ICDE 偏好的科学问题可归为 5 类：

| 类 | 本质（形式化骨架） | 代表 | 证明 gap 的典型证据 |
|---|---|---|---|
| **P1 昂贵算子的代价—质量优化** | 选一个决策变量（算子集合、chunk 序列、示例子集、查询计划、调度），在 **预算约束下最大化质量** 或 **质量约束下最小化代价** | SPARQ（min COST s.t. 充分性≥τ）、CARROT（max reranker 分 s.t. token≤B，NP-hard）、CSV（预算下选 ICL 示例）、ZenDB、KaSLA（背包） | Figure 1 失败例子 + "cheap vs accurate" 定位图 |
| **P2 已有结构的动态/大规模维护** | 静态算法成熟 → 在更新流下维护同一结果，复杂度以"受影响区域"表达 | HIT-Leiden、DMI quasi-clique | 重算代价随规模爆炸的图；"up to 10^4–10^5×" |
| **P3 消除已知瓶颈的复杂度改进** | 在既有 SOTA 上替换复杂度中的关键参数（m→n、δ→τ），并论证条件在真实数据上成立 | CFCM、HBBMC、DDC | 新上界定理 + 多达 27 个真实图 |
| **P4 选择/验证与评测** | 多候选中选正确者，或无标签时估计系统准确率 | CycleSQL、FusionSQL、HEXGEN-FLOW（调度） | pass@k 远高于 top-1 的预实验图 |
| **P5 评测范式本身有缺陷（EAB）** | 现有评测设置不真实 → 新基准 + 反直觉发现 | DCO-Benchmark、XRAG、RLESI、SQLMorph、TS-Fault | 汇总前人评测设定的表格，指出共同盲点 |

**本质规律**：被录取的论文都把一个"看起来是 ML/LLM 的问题"写成了一个**经典数据工程问题**——代价模型、查询计划、背包/调度、索引维护、抽样估计、溯源。CFP 明确把"纯 ML/DM"列为 out-of-scope，这一步是能否被视为 in-scope 的关键。

---

## 2. 解决方法的分类与"最关键的地方"

| 方法范式 | 关键一步做了什么 | 代表 |
|---|---|---|
| **M1 一条可利用的性质 + 基础版/增强版算法** | 找到一个 locality / boundedness / 单调性，使更新或剪枝只触及局部；"basic → enhanced"两版算法天然构成消融 | HIT-Leiden（relative boundedness）、DMI、HBBMC、CFCM |
| **M2 把 LLM 子问题映射到经典优化工具** | 背包、MCTS、bin-packing、Shapley + 多臂老虎机、溯源 + NLI | KaSLA、CARROT、BOND、CSV、CycleSQL |
| **M3 离线准备 + 在线轻量决策** | 离线训练路由器/建模板/打标签，在线只做便宜的选择，离线成本单列并论证可摊销 | SPARQ、CARROT、ZenDB |
| **M4 便宜代理 + 校验/回退** | 用 reranker 分、学习 verifier、子样本 F1 代替昂贵 LLM 质量；出错时回退 | SPARQ、ZenDB、CARROT |
| **M5 受控实验矩阵（EAB）** | 统一实现、统一硬件、改变一个因素（SIMD、OOD、维度、更新）观察排名翻转 | DCO-Benchmark、RLESI、TS-Fault |

**跨组最重要的观察（直接决定了我们的选题）**：
1. A、B 两组 10 篇 LLM-for-data 论文中，**没有一篇对"代理 → 真实质量"给出统计保证**（FusionSQL 写了 1−α 区间但未兑现）；
2. **没有一篇接受用户给定的精度目标或美元预算并保证满足**（A 组缺口 2）；
3. **没有一篇组合多个 LLM 厂商**（B 组缺口 2）；
4. 成本口径混乱：只有 ZenDB、CSV 报美元，没有一篇画完整的成本—质量 Pareto 前沿。

---

## 3. 实验方法的分类

| 论文类型 | 必备实验 | 常见配置 |
|---|---|---|
| LLM-for-data（A/B） | 主结果（质量+成本同表）、跨 LLM 骨干、消融、参数敏感性、泛化矩阵、case study、离线成本摊销 | 3–14 个数据集；9–14 个基线，必须含 ICDE/VLDB/SIGMOD 方法；4–5 个 RQ |
| 图算法（D） | 与"从头重算"的效率比、可扩展性（边数/更新批大小）、各优化的消融、内存 | C++ 单机；SNAP/KONECT 5–27 个图；硬件全披露；up to X× |
| 向量检索（C） | recall–QPS 曲线、构建时间/内存、不同 k 与数据集 | HNSW M=16/efC=500，IVF 4096；k=20/100 |
| EAB（C/D） | 统一实现、多因素控制、每节 Takeaway/Observation、推荐图（雷达图/决策树）、全部复现材料 | 8–21 个被测方法 |

**普遍弱点**（我们可以做得更好，作为差异化）：几乎没有显著性检验或多种子；XRAG、KaSLA 表中出现算术上不一致的数字仍被录取——ICDE 容忍这些，但它们是风险点，不是可模仿之处。

---

## 4. 写作方法的分类与规律

**标题**（1058 篇统计：中位 9 词，55% 含冒号，39% 是"缩写: 描述"）：
- `缩写: A <Cost-Efficient/Learned/Co-Designed> Framework for X`（2026 年 LLM 论文主流）；
- `Maintaining <结构> in Large Dynamic Graphs` / `at Billion Scale`（图维护模板）；
- `[Experiment, Analysis, and Benchmark] <对象>: <发现式短语>`（EAB）。

**摘要**（中位 203 词）：背景 1–2 句 → gap（2–4 个并列缺点）→ "We propose X" → 2–3 个组件 → 带 *up to / on average* 的数字 → 代码可用性。59% 用 "we propose"，34% 用 "extensive experiments"，17% 提到理论保证。

**引言**（5–7 段）：
1. P1 场景与重要性；2. P2–P3 现有方法与 gap（失败例子或预实验 = Figure 1）；3. 编号挑战 C1–C3；4. 方法概览，"To tackle C1, …"一一对应；5. 贡献列表 **3 条为主**（2026 年常在每条后标章节号）；6. 结果头条数字。段首加粗短语串逻辑；预先回应一个审稿人可能的质疑。

**章节顺序**：Intro → Preliminaries/Problem Definition → (Overview) → 方法 2–3 节 → Experiments（占 25–55%）→ Related Work（LLM 和理论型论文多放在实验后；问题驱动和 EAB 放在引言后）→ Conclusion → **AI-Generated Content Acknowledgment**（2026 年起 A/B/C/D 组读到的 2026–2027 论文几乎都有）。

**篇幅**：已出版论文中位 14 页（12 页正文 + 2 页参考文献）；参考文献 56–85 篇；图 5–24、表 2–10；证明放 GitHub 技术报告或 arXiv full version（ICDE 不允许附录）。

---

## 5. 录用规律（从 21 篇归纳，可操作）
1. **数据工程化框定**：把 LLM/ML 问题写成代价模型 + 约束优化 / 维护 / 抽样估计问题，并在 Related Work 中接续 ICDE/VLDB/SIGMOD 工作。
2. **一个清晰的关键洞见 + 一个可证明的性质**：一条性质（boundedness、单调性、方差分解）支撑整套方法，并以 Theorem/Lemma 形式给出。
3. **挑战—组件—实验一一对应**：3 个挑战 ↔ 3 个技术组件 ↔ 3 组实验（RQ）。
4. **Figure 1 证明 gap 真实存在**：真实失败例子或预实验，而不是概念图。
5. **报告真实成本**：美元 + token + 延迟，离线成本单列；有 Pareto 前沿更好。
6. **plug-in 定位 + 广覆盖实验**：方法可嵌入现有系统，用多数据集、多骨干弥补单点提升有限。
7. **复现材料**：代码与数据公开（评审时计入；EAB 强制）。
8. **趋势顺风**：LLM-for-data（15.7%）、向量检索（8.7%）、EAB（7%）在 2027R1 持续上升。

## 6. 由此确定的选题
综合缺口：**"用户给定精度目标 + 统计保证 + 多厂商 + 美元成本"** 四者在已读的 LLM-for-data 论文中无人同时做到；在更广的文献中（LOTUS、BARGAIN、SUPG-IT、CSV 语义过滤）保证型方法集中在**语义过滤**，**语义聚合**（COUNT/AVG/GROUP BY）缺少能同时选择多家模型、决定每个模型看多少元组、并给出置信区间的方法。这就是第 5 阶段 Ladder 论文的出发点（见 `05_paper/`）。
