# Reviewer lens: what accepted ICDE papers did well and which weaknesses were tolerated

> Survivor evidence: built from accepted papers only, so it cannot show why papers were rejected.

Extracted from the 'why accepted' sections of 21 reading notes (read-icde/references/notes). Chinese original.


## BOND: A Co-Designed Framework for LLM-Powered Analytics Over Relational Data (ICDE 2026, Regular research paper)
1. **切中 DB 系统社区的核心问题**：LLM-in-SQL 的执行效率是 2024–2026 热点（LOTUS、Palimpzest、MLSys'25 数据重排等），BOND 给出"系统层"答案。
2. **明确的 DB 特有洞见**："整批已知"是数据库区别于在线 serving 的关键前提，这种"利用 DB 场景先验去优化 ML 系统"的叙事很容易被 ICDE 认可。
3. **跨层 co-design**：同时动推理引擎（GPU tile 层）与数据层（行/列布局），贡献面宽。
4. **经典组合优化建模**：bin-packing、树搜索布局，便于给出形式化与复杂度。
- **对我们的启示（不依赖全文）**：成本维度可以是"GPU 时间/执行时间"而不只是 API 美元；"在线 vs 批"的区分是一个可复用的 gap 构造方式。
- **局限（只能就摘要判断）**：摘要只报告执行时间，未提准确率是否完全不受影响（数据重排可能改变 prompt 顺序/上下文，从而影响 LLM 输出——这是一个可能的攻击点，需要全文核实作者是否讨论）；未提美元成本或 API 场景（方法似乎面向自托管 GPU）。
- **建议**：若作者有 IEEE Xplore 机构访问权限，请手动下载全文放入 pdfs/A/ 后再补全本笔记。

## CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG (ICDE 2026, Regular research paper)
1. **把 LLM 应用问题还原成经典 DB 风格的组合优化**：有形式化定义、预算约束、NP-hard 证明、复杂度分析——审稿人熟悉的"问题-难度-算法"叙事。
2. **成本是一等公民**：token 预算写进目标（Eq.2 的 λ·cost/B 项），并用 Table IV 单独拆分离线索引与在线 token 成本，正面击中 graph-based RAG 的离线成本痛点（GraphRAG 2.3M tokens）。
3. **实验面广且直接对应论点**：每个 Challenge 都有专门实验（顺序敏感性 Fig.10、预算非单调 Table V、领域差异 Fig.5/Fig.11），并提供上界变体 CARROT_upper 与多种搜索策略消融（Beam/Bandit/Agent-Only），回答"为什么一定要 MCTS"。
4. **代理目标被验证**：用 reranker-质量相关性（r=0.83）为"用 reranker 分代替 LLM 质量"辩护，堵住最大漏洞。
5. **可借鉴**：(a) 用一个小例子同时展示所有 gap 的 Figure 1；(b) 自建 upper-bound 变体；(c) 延迟分解脚注；(d) 一次性训练成本 Remark 预先回应"训练开销"质疑。
- **潜在弱点（供我们攻击）**：只有 NP-hard，无近似保证；reranker 作为 benefit 是代理，最终 LLM 质量与代理之间的 gap 未被建模；固定 chunk size 假设；评测指标仍是 ROUGE/BLEU 等词面指标；没有报告美元成本；"30%" 主要相对 rank-based 基线。

## Tailoring the Shapley Value for In-context Example Selection towards Data Wrangling (ICDE 2025, Regular research paper；方法名 CSV / MCSV / ACSV / BCSV)
1. **把"prompt 工程"问题变成一个有公理化基础的数据估值问题**：Shapley value 是 DB 社区熟悉的工具（data valuation、data debugging、SIGMOD Record 综述），"约束化 + 唯一性定理"给出了漂亮的理论包装。
2. **成本/预算是问题定义的一部分**：Problem 1/2 都显式带预算 B；样本分配的优化目标直接把 token 成本放进约束（Eq.10–12），这是"把 LLM 任务变成预算约束下的估计/优化问题"的典型范式。
3. **理论保证密集**：7 个 Proposition（无偏、误差界、错误概率），在 LLM-for-data 论文中少见，提升了"非纯经验"的学术分量。
4. **实验覆盖面广**：14 个数据集、6 类任务、13 个基线（含专用 SOTA）、方差、统计检验、跨 LLM——对"general applicability"论点支撑充分。
5. **可借鉴**：(a) 用 "anytime algorithm + 误差随预算单调下降" 的论证回避"到底花多少钱"的质疑；(b) 统一的 $10/数据集 预算设置便于公平比较；(c) critical difference 图展示多数据集排名。
- **潜在弱点（供我们攻击）**：(a) CSV 的 top-k 与最优 k-子集（Problem 1）之间无保证，且忽略示例间交互（冗余/互补）和顺序；(b) 示例选择是"每个数据集一次性"的静态选择，不是 per-query 自适应；(c) U 仅在 200 条样本上估计，估计噪声与 LLM 随机性未建模进误差界；(d) 预算只计 token/调用，未考虑选择阶段与推理阶段成本的联合优化（选择成本能否被推理阶段摊销）；(e) 只用 gpt-3.5 为主，较新的长上下文模型下 k 的约束可能变化；(f) 证明全在 TR，可复核性弱。

## SPARQ: A Cost-Efficient Framework for Offline Table Question Answering via Adaptive Routing (ICDE 2026, Regular research paper)
1. **场景切口新且贴合 DB 关切**：把"离线/本地部署 + 隐私 + 零 API 成本"作为一等目标，而不是又一个追求在线 GPT 精度的方法；"消费级 GPU 上超过 GPT 系方法"是很强的卖点（4B 模型 WikiTQ 77.03 > H-STAR GPT-4o-mini 74.93）。
2. **扎实的 empirical-study-first 叙事**：Section III 的 5 条发现让方法设计显得"必然"，审稿人容易认同。
3. **成本被写进训练信号与优化目标**：reward = acc × 成本惩罚 × 长度惩罚；Eq.1 是"min 成本 s.t. 充分性 ≥ τ"的约束优化形式——把 LLM 任务写成了 DB 风格的 cost-based optimization（类似查询优化器选计划）。
4. **系统层工程完整**：CPU-GPU 调度、动态 batching、full version + 代码 + 数据，满足 artifact 期待；5 个数据集含两个"企业脏数据"基准（TableBench、NIAT）提升实用性说服力。
5. **可借鉴**：双轨公平比较（引用原文结果 + 统一后端重跑）；分层分析（按表大小）；"reasoning cliff"曲线；"router 过度剪枝"的分布图（Fig.5）。
- **潜在弱点（供我们攻击）**：无理论保证（router 次优性、verifier 误判率与最终准确率的关系均未分析）；COST 定义为运行时间但训练用的是离线枚举测得的成本，未考虑负载/硬件变化；算子可并行但未利用；verifier 阈值 τ 全局固定；没有美元/能耗成本模型；多表、多跳、表间 join 场景未覆盖。

## Querying Templatized Document Collections with Large Language Models (ICDE 2025, Regular research paper；系统名 ZenDB)
1. **单一、清晰、可被数据验证的洞见**："模板化文档 → 隐式层级结构 → 语义索引"，这是一个数据特性驱动的洞见，而非模型技巧，非常符合 DB 社区口味。
2. **把 LLM 查询处理放进经典 DB 框架**：数据模型、DDL 扩展、惰性物化、昂贵谓词排序、join 序、provenance，几乎每一项都能对应到 DB 教科书概念，审稿人容易评价其"DB 贡献"。
3. **成本以美元报告 + 摊销论证**：离线索引成本（$0.1 级别）与在线查询成本分开，并证明一条查询即可回本；ZenDB-light 的"每 $1 可执行查询数"图非常直观。
4. **真实应用场景与合作方**（Stanford Big Local News 记者需求），提升 practical impact 的可信度。
5. **有正确性定理**（虽然条件较强），使"结构抽取"不只是启发式。
- **可借鉴**：用 "Experiment k" 而非 RQ 也可以；预处理成本单独成表；"cheap vs accurate"二维定位图（Fig.2）作为引言第二张图。
- **潜在弱点（供我们攻击）**：(a) 每个数据集仅 9 条查询、最多 100 篇文档，规模小、无可扩展性实验；(b) 基线只有自定义策略，没有对比同期 LLM-powered 查询系统；(c) 依赖视觉格式与模板，非模板/扫描件/噪声模板未处理（作者自列 future work）；(d) 成本模型是启发式（e_o 在线估计），无预算约束下的最优计划；(e) 属性值与谓词结果可能不一致的问题被明确排除；(f) join 仅限文档内；(g) 没有参数敏感性（k、θ、summary 大小）。

## CYANSQL: Unlock the Power of NL2SQL via Clustering-based Test-Time Scaling (ICDE 2026, Regular)
- 无法基于原文判断。仅从元数据看：(1) 16 页、70 篇参考文献，体量为完整 ICDE regular 论文；(2) 产学合作（复旦 + 腾讯云），通常意味着有工业场景/系统部署叙事；(3) 该组前作 PURPLE（ICDE'24）与 CycleSQL（ICDE'25）连续三年在 ICDE 发表 NL2SQL 工作，说明该组熟悉 ICDE 审稿偏好（DB 技术 + LLM）。
- **建议**：若作者可通过机构订阅从 IEEE Xplore 下载 PDF，放到 `/Users/loctek/Desktop/ICDE2027/03_deep_reading/pdfs/B/` 后可补读本篇。由于它是本组与"多候选选择"最直接相关的一篇（与本项目研究方向最接近），**强烈建议补读**，重点核查：聚类依据（执行结果 / SQL 结构 / embedding）、簇内与簇间如何选择、是否组合多个 LLM、是否报告 token 成本、是否有选择正确率的统计保证。
- 本组中用于补位、已全文精读的替代论文见：`B_cyclesql_substitute.md`（同组 ICDE'25，候选验证）与 `B_hexgenflow_substitute.md`（ICDE'26，Text-to-SQL 多 LLM 调用的推理调度与成本）。

## Grounding Natural Language to SQL Translation with Data-Based Self-Explanations（CycleSQL）(ICDE 2025, Regular)
1. **用经典 DB 技术（provenance、query inversion、图同构）解决 LLM 时代的问题**：给 NL2SQL 验证提供了一个"DB 原生"的信号，是 ICDE 审稿人最认可的差异化点。可借鉴：在 LLM 候选选择中引入数据库执行层面的证据（溯源、反例、差分执行），而非仅靠 LLM 自评。
2. **plug-and-play + 广覆盖**：7 个模型（含 Seq2seq 和 LLM）全部提升，弥补了单点提升幅度不大的弱点。
3. **Fig.1 的 pass@k vs top-1 预实验** 非常有说服力地证明"候选里有正确答案，问题在选择"——这是候选选择类论文的标准开场，新论文可直接借鉴这种 motivation 证据形式。
4. **完整的消融与错误分析**（替换反馈方式、替换验证器、Oracle）回应了"为何不用 LLM 直接判"的质疑（Table III：LLM 验证器仅 +0.7 EX）。
5. 可攻击的缺口：(a) 无 BIRD/Spider 2.0 等更难基准；(b) 首过策略对验证器的误判非常敏感，且不利用候选之间的一致性信息；(c) 验证器需要在目标 benchmark 训练集上训练（30K 样本），跨域迁移有限；(d) 空结果查询无法溯源；(e) 无统计保证（如控制错误接受率的阈值选择）、无多模型候选融合、无成本分析。

## An Efficient and Effective Evaluator for Text2SQL Models on Unseen and Unlabeled Data (ICDE 2026, Regular)
1. **新问题设定 + 明确的工业动机**：上线前无标签评测是真实痛点（隐私、库演化），"首次形式化"在 ICDE 很有吸引力；可借鉴：从部署/运维视角为 LLM-for-data 定义新任务。
2. **规范的问题形式化**：Model / Challenges / Objective 三段式，目标函数与性质清楚，这是 ICDE 偏爱的写法。
3. **规模化实验**：7 个 benchmark、5+5+20 个模型、7 类基线、5 seeds + CI、延迟/内存/预算全报告，体量压人。
4. **数据资产贡献**：3.37M 样本的 FusionDataset 本身就是可复用资源。
5. **可借鉴的缺口**（新论文可攻击）：(a) 承诺的 1−α 覆盖保证未兑现——可用 conformal prediction / PPI 给出真正有统计保证的数据集级准确率区间；(b) 依赖白盒 embedding，无法评估闭源 API 模型或多 vendor 组合系统；(c) 只估计数据集级准确率，不支持 per-query 选择/拒答；(d) 未与 PPI 这种"少量标签 + 无偏"方法对比。

## HEXGEN-FLOW: Optimizing LLM Inference Request Scheduling for Agentic Text-to-SQL (ICDE 2026, Regular)
1. **抓住 LLM-for-data 的"系统侧"空白**：大家都在提准确率，它研究 agentic Text-to-SQL 的服务效率，问题新且工业相关（异构 GPU、多租户、SLO）。
2. **形式化 + 启发式 + 系统实现** 的完整链条，并给出 NP-hard 论断为启发式辩护——ICDE 系统论文的标准套路。
3. **实验矩阵大**：3 种硬件 × 6 条 trace × 多负载 × 5 基线 + 消融 + 案例 + 开销，且有误差棒。
4. 可借鉴的缺口：(a) 把候选数、修正轮数视为 **外生固定**，没有与"选择算法"联合优化——例如自适应决定生成多少候选、何时提前停止（early stopping）以同时满足 SLO 与准确率；(b) 只用单一开源模型（Llama-3.1-70B / Qwen3-30B），不涉及 **多 vendor API 混合**（商用 API 的速率限制、价格差异）；(c) 不报 token/$ 成本；(d) 准确率–延迟的 trade-off 完全未讨论。这些正好是"成本感知的多 LLM 候选生成与选择"类论文可以切入的点。

## Knapsack Optimization-based Schema Linking for LLM-based Text-to-SQL Generation (ICDE 2026, Regular)
1. **把 LLM 任务"数据库化/优化化"**：用经典组合优化（0-1 knapsack + DP）重新表述一个 NLP 子问题，符合 ICDE 审稿人对"形式化+算法"的偏好；可借鉴：为 LLM 流水线中的选择/过滤步骤找一个经典优化模型（背包、集合覆盖、子模最大化）。
2. **"新指标 → 新现象 → 新方法" 的叙事链**：先证明旧指标失效，再用新指标暴露 seesaw，最后方法直接针对 seesaw；逻辑闭环强。
3. **plug-in 定位 + 大量基线**：替换 7 个 SOTA 系统的 linking 模块均有提升，覆盖闭源（GPT-4、DeepSeek-V3）与开源（CodeS、StarCoder2）backbone，说服力来自广度而非单点 SOTA。
4. **小模型胜大模型 + 延迟几乎不增**：1.6B 打分器 + 推理时间对比，契合 ICDE 对效率/实用性的关注。
5. 可借鉴的反面教训：缺理论保证、DP 离散化细节缺失、Table V 数字不一致、无方差/显著性、无 token/$ 成本——新论文可在这些点上做得更严谨以形成差异化。

## SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation (ICDE 2026, Experiment-Analysis-Benchmark)
1. **EAB 轨道契合**：不追 SOTA，而是提供可复现的评测框架 + 新发现（join 与命名是主要失败模式），开源工具，符合 ICDE Experiment-Analysis-Benchmark 的评价标准。
2. **数据库视角的问题建模**：schema graph、JQG、图同构去重、传递性冗余检测、多重集结果关系匹配——都是 DB 社区熟悉的概念，区别于 NLP 社区的 benchmark 论文。
3. **因果隔离实验**（Table VI 固定上下文换回原 NL）显示了实验设计的严谨性，审稿人通常欣赏。
4. **指标设计有诊断价值**：过预测/欠预测分解直观，并给出 15 种变异算子的系统验证。
5. 可借鉴的缺口：(a) 只用 BIRD dev、3 个旧系统、单一 GPT-4o；(b) 扩展集仅 58 条，NL 改写有 12.1% 意图漂移，缺乏自动意图一致性验证；(c) 声称低成本却没报告成本；(d) EXP/EXR 只用于离线诊断，未用于 **在线候选选择/重排序**（在无 GT 时无法计算）——这是一个可以连接"多候选 SQL 选择"的切入点：例如用候选间的 EXP/EXR 相似度做软投票/聚类。

## Distance Comparison Operations Are Not Silver Bullets in Vector Similarity Search: A Benchmark Study on Their Merits and Limits (ICDE 2026, EAB)
1. **"fundamentally new" insight 来自否定已有共识**：先前 4 篇论文都报告 DCO 有 2–4× 加速；本文证明在默认开 SIMD 的真实条件下，大部分场景收益缩小甚至变负，并且排名会翻转（DDC_opq 在 SIFT 上从最差变最好）。这是 EAB 最被认可的新意类型：**揭示先前评测协议的系统性偏差**。
2. **gap 可视化做得极好**：Table I 一张表让审稿人立刻相信"之前没人这样测过"。
3. **双面结论**：不只是"打假"，还找到被忽视的优点（建索引/插入加速），并给出可操作的选择指南（Fig.14）与 4 条未来方向，避免成为纯负面论文。
4. **可复现性**：从零统一重实现 + 开源代码与数据 + 附录详细实现细节（数据布局、语言、kernel 组织）+ 参数研究说明默认参数的影响。
5. **可借鉴点**：做 EAB 时 (a) 先把先前工作的评测协议列成表找"系统性盲区"；(b) 引入被忽视的强简单基线；(c) 加入一个现实但被忽视的维度（硬件、OOD、超高维、更新）；(d) Takeaway 框 + 推荐决策图。不足：未做多线程/批量并行查询、未覆盖磁盘索引与量化索引（RaBitQ 等）的交互——这些是后续可攻的 gap。

## Effective and General Distance Computation for Approximate Nearest Neighbor Search (ICDE 2025, Regular)
1. **gap 定义极其清晰、可验证**：两个形容词（effective/general）= 两个 gap = 两个方法章节 = 标题，审稿人可以逐项核对。
2. **"插件式"贡献**：DCO 层的改进对 HNSW 与 IVF 同时有效，适用面广；且提供"选择指南"（方差偏斜度决定用 PCA 还是 OPQ）。
3. **理论 + 数据驱动结合**：最优性定理给方法正当性，学习方法给通用性；即使理论只在 Gaussian 假设下成立，配合 Fig.2 的经验验证也足够说服。
4. **规模与落地**：100M 规模可扩展性 + Ant Group 线上集成，契合 ICDE 对工程价值的偏好。
5. **可借鉴点**：针对一个强 SOTA（SIGMOD'23）做"根因分析 → 定向修复"的写法；Problem Analysis 单列一节；贡献列表带章节指针。**风险提示**：关闭 SIMD、基线少、无端到端理论保证——这些正是后续 EAB 论文（论文 3）攻击的点。

## [替代论文] Benchmarking RL-Enhanced Spatial Indices Against Traditional, Advanced, and Learned Counterparts (ICDE 2026, EAB)
1. **"fundamentally new" 的来源**：(a) 首次把 RLESI 放到**磁盘**、**调过参**、与**三类强基线**同台的条件下；(b) 揭示"只看调好参后的查询时间"会掩盖巨大的训练/调参成本（>30 小时/索引/数据集）、尾延迟尖峰与插入代价；(c) 给出采样训练导致局部性失真的机制性解释。结论是否定性的但不是简单否定：承认 RLESI 的"架构兼容性"价值。
2. **方法选择的原则透明**：每一范式选一个 SOTA RLESI，并配齐其 traditional/advanced/learned 对应物，形成可比的 3×4 矩阵；排除理由（无开源）写明。这是"如何选择比较方法"的范本。
3. **可复现性**：开源（带 icde26 分支）、基于成熟库 libspatialindex、统一节点/页面参数、给出每个索引的插入策略取舍、调参配置表与调参代价。
4. **findings 组织**：22 条 Observation 在引言即按 7 组预告，在 VI 节用雷达图收束，再给出"挑战—局限—机会"三段式，最后附一个小改进（BM-tree-Impr）证明洞见可行动。
5. **可借鉴点**：做 learned/AI-for-DB 类 EAB 时，必须报告"全成本"（训练 + 调参 + 建索引 + 尾延迟 + 更新），并把调参当作实验变量而不是固定前提。**不足**：只有 2D 点数据、单机 HDD（无 SSD/内存对比）、调参只用网格搜索且搜索空间小、缺统计显著性——这些正是后续 EAB 可补的 gap。

## Tag-Filtered Approximate Nearest Neighbor Search (ICDE 2025, Regular)
1. 问题有明确工业需求（向量数据库中的属性/标签过滤是普遍场景），且命名了一个清晰的问题变体。
2. gap 以"tag 频率"这一可量化的数据特征来刻画——低频 tag 的召回问题可以用一张"召回 vs tag 频率"的图直接展示（这是我们写类似论文时值得复用的 motivating 图思路，但不确定原文是否这样做）。
3. 把"内存 vs 召回"的 trade-off 显式化，并提供多种策略覆盖 trade-off 曲线，而非单一方法。
4. 结果数字大（13×）且设定了具体 recall 门槛（≥0.9），表述规范。
- **后续行动建议**：若需要全文，可通过机构 IEEE Xplore 访问或向作者索取；在获得全文前，本笔记不应作为写作结构/实验协议的依据。

## XRAG: eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation (ICDE 2026, EAB)
1. **话题热度 + 资产价值**：RAG 是 2025–2026 最热方向，一个开源、带 Web UI、统一数据集、统一指标（7+10+23 个）的工具本身就有社区价值——EAB 轨道认可"benchmark 资产"。
2. **公平比较的控制变量设计**：固定 retriever/generator/seed/temperature/prompt/chunking，Table III 显式列出固定与差异模块；检索标签用文档 ID 统一。
3. **若干反直觉 lesson**：检索得到的 top-3 上下文常优于人工标注的 golden context（小模型下）；选对模型类型比单纯加大参数更重要（DeepSeek R1 推理模型在 RAG 中幻觉高）；context 数量增加收益有限，精度更关键；iterative orchestrator 适合多跳。
4. **成本维度**：延迟与 token 消耗表让 lesson 可落到"推荐 reranker"这样的工程建议。
5. **可借鉴点**：(a) 特征勾选表做 gap 证据；(b) 统一数据格式与 ID 级标签；(c) 加粗 lesson 句。**反面教材**：摘要无数字、无 findings 汇总、表格一致性问题、样本量小——我们的 EAB 投稿应在这些点上做得更严谨（统计检验、置信区间、完整测试集或说明采样方差）。

## Fast Maximization of Current Flow Group Closeness Centrality (ICDE 2025, Regular) —【替代论文 #2】
1. **理论密度高**：2 个定理 + 十余个引理，复杂度与近似比完整，属于 ICDE 图算法中"理论型"代表；同时有扎实的工程（72 线程、27 个图、百万级）。
2. **清晰的单点突破叙事**：SOTA 的瓶颈（Laplacian solver，复杂度依赖 m）→ 我们的方法（依赖 n）→ 实验在稠密图上加速最明显，理论与实验形成闭环。
3. **把物理/谱图论工具（电网络、生成森林、Schur complement）迁移到数据管理问题**，并在引言里主动链接"data management community"使用电阻距离的工作。
4. **可借鉴**：(a) 在 Preliminaries 中专设 "State-of-the-art Method + Performance Discussion" 小节；(b) 两阶段方法（basic 版 + enhanced 版）——基础版证明可行，增强版提速，二者对比天然构成消融；(c) 每节开头的推导路线图。
- **可追问的弱点**：近线性复杂度依赖对真实图的经验假设（d_max^{2τ+2}）；只有静态版本——**动态图上的 group CFCC 维护**是显而易见的后续题（与本组 ICDE 2027 的"maintenance"论文题型一致）；基线跨语言；k 固定为 20，未测试大 k；无 case study。

## Scalable Algorithm for Dynamic Quasi-clique Detection (ICDE 2027 round 1, Regular)
1. **"首个动态版本"叙事**：把一个有成熟静态 SOTA（Pang et al.）的 NP-hard 问题搬到动态设定，问题新、门槛低、易于理解。
2. **速度差距巨大**（10^2–10^4×）且质量有可信的"合法性"保证（精确密度验证）；更新时延中位数微秒级（Table VIII/IX）。
3. **实验非常全面**：9 个数据集 × 5 种动态生成方式 × 7 组附加实验，弥补了理论较薄的短板；明确的 ablation（B）与修复成功率统计（Table X）回应了"为何需要候选列表/局部修复"的潜在质疑。
4. **团队背景**：CUHK-SZ 稠密子图方向的连续工作（[1][2] 是同组的 densest subgraph 工作），领域积累可信。
5. **可借鉴**：(a) "静态 SOTA 的局部步骤 + 可更新 sketch + 候选池 + 周期性重建"是一个可迁移到其他 NP-hard 结构（k-plex、δ-clique、defective clique）的通用配方——作者自己在结论中也指出这些扩展方向；(b) 每个算法后紧跟 "Time Complexity." 段。
- **可追问的弱点**：无近似保证、无质量随时间漂移的理论界；数据规模偏小（≤22M 边），与标题 "Scalable" 不完全匹配；基线是"每次从头重跑"，缺少更强的增量基线（作者自建的 NSF 部分起此作用）；DMQCP NP-hard 的论证过于简单；同期 arXiv 上已出现另一篇 "Detecting Large Quasi-cliques on Dynamic Networks"（2606.05809），说明该方向竞争很快。

## Maximal Clique Enumeration with Hybrid Branching and Early Termination (ICDE 2025, Regular) —【自选论文 #5】
1. **在经典问题上改进最坏复杂度**：MCE 自 1973 年 BK 以来被反复研究，能给出新的（条件性）更优界本身就是强贡献；并用 223 个真实图统计条件成立率，弥补"条件性"的弱点。
2. **两个正交贡献**（hybrid 框架 + early termination），且 ET 可插入任何 BB 框架——提高了"通用性"得分。
3. **系统的消融**：Table III–VI 分别隔离框架、VBBMC 实现、切换深度、t、边序五个设计维度，每个设计选择都有表格支持。
4. **与前作差异的显式论证**，降低"增量过小"风险。
5. **可借鉴**：(a) 数据集表中列出理论参数（δ, τ, ρ）；(b) 在 Remarks 中把复杂度比较的条件转化为可验证的图统计；(c) "已有框架 → 新框架 A → 混合框架 B" 的递进叙事；(d) 在附录中补证已有算法的复杂度，形成完整的复杂度对比表（Table VII）。
- **可追问的弱点（gap 来源）**：只有单线程静态算法（并行与动态均未涉及，而相关工作列出了 16 篇并行 MCE）；hybrid 切换深度 d 只做了经验选择（d=1），无自适应理论；t 只到 3（4-plex 的补图最大度 3，不再是路径/环，需要新技巧）；附录图例误写为 "HBBkC++"，说明附录打磨不足；加速倍数有限（≤4.38×）。

## Maintaining Leiden Communities in Large Dynamic Graphs (ICDE 2027 round 1, Regular)
1. **"静态经典算法 + 动态维护"的稳定题型**，对象选得好：Leiden 当下因 GraphRAG 而热门，且已有维护工作缺理论——"热点算法 × 理论空白"。
2. **理论框架借力**：直接借用 Fan et al. 的 (relative) boundedness 给出"已有方法 unbounded / 本文 relatively bounded"的干净对比，让一个工程味较重的工作具有可陈述的理论贡献。
3. **工业背书与真实规模**：ByteDance 合作、4B 边内部数据集、部署声明、fraud-ring 实际业务（58.3M 顶点 / 26 天 / 每天约 0.5M 更新）与 GraphRAG token 成本节省，把"为什么要快"讲得很实。
4. **夸张但可信的加速比**（up to 10^5×），且质量通过两个维度（modularity + γ-density 比例）证明不降。
5. **可借鉴**：(a) 用 Lemma 刻画"何时某顶点会被影响"并配合"在实际参数下这些条件几乎不满足"的 Observation 来合理化剪枝；(b) 一张 design-rationale 图；(c) 贯穿全文的单一 running example；(d) 把应用研究放附录、正文只保留核心性能实验，以节省 12 页篇幅。
- **可追问的弱点（可作为后续工作切入点）**：质量无理论保证（Observation 3 是经验观察）；无并行版本；只处理无向图；没有消融（去掉 inc-refinement 用重算替换等）；AFF 由算法自身定义。

## TS-Fault: Benchmarking Time Series Forecasters Against Structural Faults (ICDE 2027 round 1, EAB — Experiment, Analysis & Benchmark)
1. **反直觉、可一句话传播的发现**：clean 精度与鲁棒性负相关；基础模型"最准也最脆"——EAB 赛道最看重"改变社区认知"的结论。
2. **把 ML 问题包装成数据工程问题**："Treating TSF robustness as a data-quality problem"，并在引言首段引用时序数据库系统，贴合 ICDE 的数据管理定位。
3. **形式化框架 + 系统化分类**（Def.1/2、风险度量、四条性质、2×2 taxonomy、难度分解表），让一个 benchmark 显得有理论骨架。
4. **规模与可复现性**：21 模型、120 配置、代码/实例/检查点全部开源。
5. **可借鉴**：(a) 定位表 + 四象限图；(b) RQ 先答后证；(c) Discussion 中主动列出 threats 与反 Goodhart 机制。
- **可追问的弱点（gap 来源）**：
  - Mode III/IV 下连 Naive 的误差都从 1.24 涨到 129（ratio ~106），说明注入幅度极大；而 LSTM/GRU 的 ratio≈1.0 且难度斜率≈1.0——这更像是"对输入不敏感"（10 epoch 训练下可能接近预测均值），而非真正的鲁棒。**鲁棒性指标没有区分 "robust" 与 "insensitive"**，也没有讨论在 regime 真实切换时"跟随输入"本来就是正确行为（目标被固定为干净未来）。
  - 每个配置只有 20 对窗口，无方差/置信区间、无随机种子、无硬件与运行开销。
  - 6 个数据集中 4 个是 ETT，领域仅能源/负荷/气候；组合故障与 held-out Θ 只提出未执行。
  - 只评测不修复：没有给出任何提升鲁棒性的方法（例如故障检测 + 修复的数据清洗前处理），这正是数据工程方向可接的后续工作。