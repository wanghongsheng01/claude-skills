# An Efficient and Effective Evaluator for Text2SQL Models on Unseen and Unlabeled Data (ICDE 2026, Regular)
- Source of full text: arXiv 2603.07841v2（2026-07-26）；IEEE DOI 10.1109/ICDE65706.2026.00182；FULL TEXT READ: yes
- Length: 正文约 12 页 + 参考文献约 1.5 页（PDF 共 14 页）；11 张图（Fig.1–11，Fig.10 含 a/b 两子图）；7 张表（Table I–VII）；75 条参考文献；约 16 个编号公式；0 个定理/引理
- 作者：Griffith University（Quoc Viet Hung Nguyen 组）+ Edith Cowan + UQ（Hongzhi Yin）；系统名 **FusionSQL**，代码 github.com/phkhanhtrinh23/FusionSQL

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：一个已训练好的 Text2SQL 模型要部署到新数据库/新 workload 上，但目标数据没有 gold SQL，无法算 EX，如何决定"能不能上线"。
- **本质问题**：**label-free、dataset-level 的性能估计（accuracy estimation under distribution shift）**。输入：冻结模型 f_ψ、其训练 workload、无标签目标 workload D'_T = {(q'_i, S', K')}；输出：数据集级准确率估计 M̂ ≈ M* = (1/n)Σ m(ŷ'_i, y*_i)（Eq.4）；约束：不改 ψ、不需 gold SQL、**不需可执行的已填充数据库**、低开销；目标：min E[(g_θ(Δ) − M*)²]（Eq.8）。本质是把"模型评测"转化为"从 train–test 分布偏移描述子 Δ 回归到准确率"的元学习回归问题（类似 CV 领域的 AutoEval / ATC / DoC，与 GNNEvaluator 思路同源）。
- **根因 / gap**：作者在 III-B 列 5 个挑战 ξ1–ξ5（无 GT、分布偏移、不能改模型、proxy 信号受幻觉影响不可靠、效率）。对现有方法的批评：(1) 传统评测要 gold SQL 和可执行库；(2) 置信度类估计器（ATC、DoC）来自图像分类、无 schema 感知；(3) PseAutoEval 需少量标签；(4) LLM-as-judge（BugJudge、ArenaCmp）逐样本调用、成本高。**证据**主要是论述 + Fig.1 概念图，**没有预实验** 证明 gap（motivation 偏"操作性需求"驱动）。
- **问题定义形式**：Section III "Problem Formulation" 很规范：A. Model（Eq.1–4）→ B. Challenges（ξ1–ξ5 编号）→ C. Objective（Eq.5–6 + 4 个性质：Accuracy、Uncertainty、Efficiency、Generality，每条标注对应哪个 ξ）。无 NP-hard 等复杂度结论。
- **重要缺口**：Objective 中承诺了 **校准的预测区间** P(M* ∈ [M̂−δ_α, M̂+δ_α]) ≥ 1−α，但全文 **没有任何方法或实验实现这一 coverage 保证**；表中的 "±95% CI" 只是 5 个随机种子的均值置信区间，不是对 M* 的覆盖保证。作者引用了 Prediction-Powered Inference [41]（Angelopoulos et al., Science 2023）却未作对比。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：冻结模型自身的 pooled 最后一层表示中，训练集与目标集的分布距离（全局漂移 + 尾部 + 形状）足以回归出目标集的执行准确率；用一个大规模合成语料制造大量"偏移–准确率"配对来训练这个回归器。
- **技术组件**：
  1. **FusionDataset**（IV-A）：从 TabLib + KaggleDBQA 收集表，GPT-5 过滤、聚类成库；用 OmniSQL + SQLForge + PARSQL + 算子改写合成 SQL（9.4M→8.1M 唯一，42 种算子、8 层嵌套、12 种方言）；每条 SQL 配多种风格问题并 **注入 distractor**。最终 3.37M 对 / 3.12M 唯一 SQL / 24,625 库（Table I 与 9 个现有 benchmark 对比）。解决"没有足够多样的偏移场景来训练评估器"。工程量大，属于数据贡献。
  2. **三种 shift descriptor**（核心新意）：SD_F（Fréchet 类：均值差 + 方差比，全局漂移）、SD_M（以源统计白化后的 Mahalanobis 距离均值/方差，尾部风险）、SD_SW（Sliced Wasserstein，分布形状），拼成 Δ。Table VII 用 PCA-4 维的具体例子说明欧氏均值差很小而三描述子能区分结构/语义变化。
  3. **回归器 g_θ**：3 层 MLP（256/128/64），MSE 训练；元集 n = 30K 个 (D_train, S_i)，|S_i| ≤ 10K。
  4. **Hybrid SWD**（IV-C）：top-k PCA 方向 + R 个随机方向（L≈24–34 vs 64），复杂度从 O(L[D(n+m)] + L(n+m)log(n+m)) 降为 O((n+m)Dk + L(n+m)log(n+m))（Eq.11–12）。工程优化。
  5. **FusionSQL-ML**：用 Reptile 元学习在 20 个 base model 上学初始化，对未见模型用 FusionDataset 子集（已知标签）做几步适配后再无标签估计目标集。
- **真正新的**：问题设定本身（label-free dataset-level Text2SQL 评测，作者声称首次）+ 三描述子组合；其余（MLP 回归、Reptile、随机 PCA）为现成组件组合。
- **理论保证**：无。只有 SWD 的复杂度表达式；Objective 中的覆盖率性质未被证明或验证。

## 3. 实验设计 (Experiments)
- **RQ 列表**（5 个）：RQ1 Data Coverage（FusionDataset 是否覆盖真实 workload）；RQ2 Data Efficiency（样本集/元集规模、预算）；RQ3 Evaluator Learning（估计准确性、跨数据集/跨模型泛化）；RQ4 Scalable Deployment（延迟/内存）；RQ5 Shift Modeling（描述子分析、非神经系统）。
- **数据集**：7 个评测 benchmark——Spider、WikiSQL、BIRD、SParC、CoSQL、SynSQL-2.5M、Spider 2.0；以 5 组 source→target 迁移组织：Spider→BIRD、WikiSQL→Spider、SParC→CoSQL（in-domain）、Spider→SynSQL-2.5M、WikiSQL→Spider 2.0。
- **被评估的 Text2SQL 模型**：主实验 5 个开源模型（Qwen2.5-72B-Instruct、Llama-3.1-70B-Instruct、DeepSeek-Coder-33B、XiYanSQL-QwenCoder-14B、CSC-SQL-7B），采用 CHESS 流水线微调；未见模型池 5 个（CodeLlama-34B、StarCoder2-15B、Mistral-7B、DeepSeek-Coder-6.7B、Phi-3-mini）；元训练池 20 个；另含 3 个非神经系统 ATHENA、ATHENA++、SQLizer。**全是开源/白盒模型**——方法依赖内部 embedding，**不适用于 GPT/Claude 等闭源 API 模型**，这一点论文未正面讨论。
- **基线**（7 个，含变体）：ATC-MC、ATC-NE（NeurIPS'21）、DoC τ=0.8/0.9（ICCV'21）、PseAutoEval（ICML'25）、BugJudge（KDD'25 NL2SQL-Bugs）、ArenaCmp（NeurIPS'23 MT-Bench 风格），两个 judge 基线都用 **GPT-5**；自身变体 FusionSQL-TL（10%/25% 标签微调）、FusionSQL-TI（TF-IDF）、FusionSQL-LLM。没有 ICDE/VLDB/SIGMOD 的评测类基线（因为作者声称问题是新的）。
- **指标**：被估计量 EM、EX；评估器指标 MAE（百分点），5 seeds 均值 ± 95% CI；另报 Pearson r（Fig.10a r = 0.53–0.70；Fig.10b 距离–EX 相关 r ≈ −0.889/−0.906）。
- **实验类型**：主结果（Table III：5 迁移 × 5 模型 × 9 方法，FusionSQL 平均 MAE 2.1–5.3 vs 最强基线 ArenaCmp 4.9–14.6）；跨模型泛化（Table IV，FusionSQL-ML MAE 5–7）；数据覆盖（Table I/II、Fig.3 t-SNE、Fig.4 16 维雷达图）；数据效率（Fig.5 样本集大小、Fig.6 元集大小 × 回归器）；校准（Fig.7）；延迟-精度权衡（Fig.8、Fig.9）；可扩展性（Fig.11、Table V：HSWD(8,16) 延迟 3.42s→1.27s、内存 8.9GB→3.2GB）；非神经系统（Table VI）；描述子个例分析（Table VII）。
- **成本报告**：**是本组中成本报告最"财务化"的一篇**——显式给出数据构造预算 B = 1000 USD 与成本约束（Eq.16，单样本生成/验证/执行成本 0.00012/0.00003/0.0004 USD，总计约 666.21 USD，最坏 985 USD）；评估延迟以分钟/秒报告；judge 基线的 API 成本只在脚注中指向 OpenAI 价格页，**没有给出 token 数**。
- **结果呈现**：主结果用大表（加粗最佳、下划线次佳）；其余大量用图。表述多为 "lowest MAE in most cases"、具体数值对比。
- **值得警惕**：Table III/IV/VI 中数字在模型间呈现高度规则的单调递增（如每列逐步 +0.4~0.6），CI 宽度也近乎模板化；FusionSQL-TL 加了标签反而更差的解释较牵强。这些是审稿时容易被质疑的点，但已被接收。

## 4. 写作结构 (Writing)
- **标题模式**："An Efficient and Effective <方法类型> for <对象> on <困难设定>"——用设定（Unseen and Unlabeled）作为卖点，而非方法名。
- **摘要逐句功能**：S1 背景（LLM 提升 Text2SQL）→ S2 部署挑战（无标签新数据集）→ S3 为什么常见（库演化、隐私、标注贵）→ S4 后果（无法批准发布/发现故障）→ S5 方案 FusionSQL（model-agnostic，无需标签）→ S6 机制一句话（分析自身输出模式刻画数据偏移）→ S7 用途（发布前检查、持续监控、质量下降检测）→ S8 结果（紧密跟踪真实准确率）+ 代码。摘要 **完全不出现数字和技术名词**，极度面向"应用价值"。
- **引言逐段功能**：P1 Text2SQL 技术演进史（神经解析器→LLM→模块化/候选选择/agent，引用 [1]–[28]，大量引 ICDE'25 论文如 AID-SQL、CycleSQL）；P2 运营缺口（上线前无标签）+ 基准多样化带来偏移 + 用斜体提出研究问题；P3 方案概述 + "to the best of our knowledge" 首创声明 + 产出"可靠性报告"；贡献列表 **5 条**（问题形式化 / 框架 / 数据集 / 实证 / 效率）。Figure 1 是"有标签评测 vs 无标签评测"对比的概念图，**不是数据驱动的 motivating example**。
- **章节顺序与篇幅**：I Intro（~1.3 页）→ **II Related Work（紧随引言，~0.5 页，分"Text2SQL 评测基准"与"label-free 性能估计"两类）** → III Problem Formulation（~0.8 页）→ IV FusionSQL Framework（~2 页）→ V Experiments（~6.5 页，占一半以上，按 RQ 组织为 A–D 小节）→ VI Conclusion & Future Work（很短）。无 Limitation 节。
- **写作技巧**：
  - 挑战用 ξ1–ξ5 编号，Objective 中每条性质回指对应 ξ，方法组件再回指——形成"挑战→性质→组件"的可追溯链条，审稿人易于对照。
  - 把"数据集构建"包装成一个独立贡献并单列 RQ1/RQ2，用 Table I 与 9 个 benchmark 对比规模，增加论文"分量"。
  - 用 distractor 的具体例子（TikTok 例句）说明数据集设计意图，生动。
  - 预算公式化（Eq.16）把"花了多少钱造数据"写成约束优化，显得严谨且回应可复现性。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **新问题设定 + 明确的工业动机**：上线前无标签评测是真实痛点（隐私、库演化），"首次形式化"在 ICDE 很有吸引力；可借鉴：从部署/运维视角为 LLM-for-data 定义新任务。
2. **规范的问题形式化**：Model / Challenges / Objective 三段式，目标函数与性质清楚，这是 ICDE 偏爱的写法。
3. **规模化实验**：7 个 benchmark、5+5+20 个模型、7 类基线、5 seeds + CI、延迟/内存/预算全报告，体量压人。
4. **数据资产贡献**：3.37M 样本的 FusionDataset 本身就是可复用资源。
5. **可借鉴的缺口**（新论文可攻击）：(a) 承诺的 1−α 覆盖保证未兑现——可用 conformal prediction / PPI 给出真正有统计保证的数据集级准确率区间；(b) 依赖白盒 embedding，无法评估闭源 API 模型或多 vendor 组合系统；(c) 只估计数据集级准确率，不支持 per-query 选择/拒答；(d) 未与 PPI 这种"少量标签 + 无偏"方法对比。
