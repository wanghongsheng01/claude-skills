# bbac343: paragraph, experiment and figure functions

Original analysis of Sidorczuk et al., Briefings in Bioinformatics 23(5), bbac343 (2022), DOI [10.1093/bib/bbac343](https://doi.org/10.1093/bib/bbac343). Main text and three figures/two tables were read; figure/table layouts were checked in the [author institutional published-version PDF](https://researchonline.jcu.edu.au/75949/1/75949.pdf), pages 3, 5, 6, 8 and 9, on 2026-10-23. This file contains analysis, not article text or images.

## Central lesson

The paper holds the positive dataset fixed and crosses architecture, negative sampling and evaluation conditions. Results answer whether bias appears, how factors change performance, and how repeats affect stability. It is an evaluation study rather than a new wet-lab study. Learn that controlled question-to-answer structure; do not copy broad claims condemning all previous benchmarks. The observed 12 pages and 59 references are not journal minima.

## All 37 scientific prose paragraphs

IDs are locally assigned by section/order. The scientific-prose count excludes captions, references and endmatter; duplicated HTML table layouts are counted once.

| ID / section | Paragraph function | Argument order | Sentence function |
|---|---|---|---|
| ABS-01 / Abstract | 将完整研究压缩为问题、控制设计、主发现和可用解决方案。 | 对象背景→研究需要→具体问题→设计规模→方向性发现→影响→工具交付。 | 先以一般现在时说明领域背景，随后用作者主动语态说明操作，再用结果主语表达发现。 |
| INT-01 / Introduction | 建立AMP生物学对象及性质与功能之间的联系。 | 存在范围→生物学功能→序列性质→结构及作用→机制的例外。 | 从定义句进入机制解释，用转折约束简单概括。 |
| INT-02 / Introduction | 说明AMP作为治疗候选的吸引力。 | 耐药性相对优势→作用方式差异→可能原因。 | 短段只承担一个理由，因果解释跟随判断。 |
| INT-03 / Introduction | 把社会需求连接到计算方法增长。 | 耐药负担→候选需求→计算工具增长。 | 由宏观动机转到本文所属技术问题。 |
| INT-04 / Introduction | 为跨学科读者建立最小技术词汇。 | 浅层到深层方法→标注数据→正负类别→特征提取→特征选择。 | 抽象术语立即配实际方法，避免连续堆砌名词。 |
| INT-05 / Introduction | 展示表面充分的数据资源仍有对象范围问题。 | 正类数据库丰富→成熟肽与前体差别→长度筛选后果。 | 先承认已有资源，再定位其适用边界。 |
| INT-06 / Introduction | 将核心缺口锁定在负类，而非继续扩散背景。 | 前一问题可解决→关键缺口→其他领域也存在。 | 承上启下并提升问题的一般性。 |
| INT-07 / Introduction | 梳理可选方案并定义后文比较单位。 | 三类处理路线→既有实践→筛选规则→术语和缩写。 | 先分类，再解释本文研究对象及命名；引用承担方法来历。 |
| INT-08 / Introduction | 提出可回答的问题，并预告受控研究设计。 | 研究目的→既有比较遗漏→跨采样问题→架构与模型实例定义→因子组合及重复→贡献。 | 目的句后立即说明为何现有证据不能回答，再给设计而非口号。 |
| DAT-01 / Methods / Data sets | 把正类构建写成可重复的操作。 | 数据源版本→纳入条件→去除条件→去冗余阈值及理由→数量→先划分后采样。 | 顺序动词和数量构成方法链，说明关键顺序的科学作用。 |
| DAT-02 / Methods / Data sets | 固定负类母体的来源与版本。 | 母体数据库→审核状态→数量→发行版本。 | 极短一段提供必要来源，不夹杂研究过程。 |
| DAT-03 / Methods / Data sets | 解释方法入选、重复和统一处理。 | 候选方法池→入选数量与依据→五次重复→兼容性改动→泄漏控制→补充位置。 | 给出改动的目的和定位，不在正文复述全部实现细节。 |
| DAT-04 / Methods / Data sets | 说明负样本规则如何可能形成混杂。 | 共同筛选逻辑→位置规则→替代分类任务风险→不同过滤比例。 | 把操作与其统计后果相连，机制解释有具体规则支持。 |
| DAT-05 / Methods / Data sets | 展示各采样法的类别平衡差异。 | 平衡组→轻微不平衡组→显著不平衡组→反向例外。 | 按共同性质归组，避免逐方法重复介绍。 |
| DAT-06 / Methods / Data sets | 展示长度分布这一潜在快捷线索。 | 精确匹配组→近似匹配组→短序列组→长序列组→图表定位。 | 从方法规则导出样本分布，并把大量数值交给图。 |
| DAT-07 / Methods / Data sets | 补足样本单位的本质区别。 | 匹配长度的方法用片段→其余用完整序列。 | 短对比句消除相同名词背后的不同单位。 |
| DAT-08 / Methods / Data sets | 说明去冗余操作与阈值。 | 避免过度代表→算法版本→适用方法数量→主要阈值→表定位。 | 目的与动作配对，关键数字紧跟。 |
| DAT-09 / Methods / Data sets | 说明正负集合交叠的检查必要性。 | 部分方法执行检查→两类可能交叠来源。 | 先陈述实际行为，再解释为何需要。 |
| DAT-10 / Methods / Data sets | 为后续分析概括输入分布。 | 正负差异→负类间差异→同法重复相似→补充图定位。 | 过渡段用有限结论把方法连接到结果。 |
| ARC-01 / Methods / Model architectures | 界定对照范围与任务。 | 候选池→可复现入选标准→二分类任务→排除MIC/多类→保留多阶段方法中的适用部分。 | 明确研究问题后再选对照，排除理由由任务决定。 |
| ARC-02 / Methods / Model architectures | 说明表示提取的共同流程和类型差异。 | 序列编码→人工描述符→学习表示→混合例外。 | 共性在前，差异和例外在后。 |
| ARC-03 / Methods / Model architectures | 按表示复杂度组织实现差异。 | 组成特征→顺序/理化特征→全序列性质→相似度/片段→学习嵌入。 | 按概念递进而非按开发时间流水叙述。 |
| ARC-04 / Methods / Model architectures | 如实交代统一重实现与原模型的差别。 | 原方法有特征选择→实际执行部分→沿用已选特征→不执行步骤及依据。 | 差别写为明确、有限、可定位的操作选择。 |
| ARC-05 / Methods / Model architectures | 将完整实现细节导向补充。 | 可复用代码数量→重新实现数量→补充表。 | 用一句完成来源和细节分工。 |
| R1-01 / Results / Sampling effect | 用主分析直接回答核心问题。 | 评价操作→图位置→总体规律→效果量差异→例外→统计检验。 | 结果先给主方向再给大小与例外，统计证据附在比较之后。 |
| R1-02 / Results / Sampling effect | 用连续变量分析解释主现象。 | 主要归纳→组成差异相关→长度差异相关。 | 从现象转到可测的解释变量，报告方向、强度和检验。 |
| R2-01 / Results / Component importance | 比较多个因素的重要性。 | 三个分组箱线→组间/组内离散比→数值→成对检验→校正后比例。 | 先可视化再量化，避免只有图的印象。 |
| R2-02 / Results / Component importance | 解释模型差异及优胜方法特点。 | 主要因素→高表现方法组成→异常方法及可能原因→最佳者性能与稳定性→生物学解释文献。 | 区分观察事实与可能解释，引用为解释提供外部根据。 |
| R2-03 / Results / Component importance | 解释训练集方法的分组趋势。 | 排序现象→几种方法分布相近→回接相关结果→解释优势来源。 | 使用前文结果构成证据链，减少重复背景。 |
| R2-04 / Results / Component importance | 处理方向反转这一重要反例。 | 训练时表现弱的方法作基准反而强→长度差异→具体中位数→相关支持。 | 主动提出反常结果，再解释，不把反例埋在补充。 |
| R3-01 / Results / Replicate repeatability | 把平均性能与稳定性分开检验。 | 重复设计→输入相似但输出有差异→不稳定者数值→反例模式→可能原因→外部一致证据。 | 先确认重复单位，然后报告波动，最后提出解释。 |
| R3-02 / Results / Replicate repeatability | 突出同时准确和稳定的方法。 | 稳定且高表现组→SD数值→算法类别。 | 简短段落提炼可供选择的性质。 |
| R3-03 / Results / Replicate repeatability | 让分层结果回到总体规律。 | 再次出现主趋势→指出不明显的架构→图定位。 | 以例外限定结论而非无限外推。 |
| DIS-01 / Discussion and conclusions | 将发现放回领域惯例并解释意义。 | 领域做法→本文识别的偏差→主图证据→对排名可信度的含义。 | 讨论从研究答案起步，避免重新介绍方法。 |
| DIS-02 / Discussion and conclusions | 给出可执行的解决方案。 | 工具目的→公共/隐藏标签分工→上传与比较→私有验证。 | 用用户可执行步骤把问题研究转成实践价值。 |
| DIS-03 / Discussion and conclusions | 把具体发现联系到可重复研究标准。 | 广泛问题→术语定义→公开标准→可用比例→与本文方法表现联系。 | 先引用明确标准，再报告本研究可观察的符合情况。 |
| DIS-04 / Discussion and conclusions | 以贡献和行动建议结束全文。 | 实践后果→本文贡献→规模→建议及资源。 | 结尾给读者下一步，而不是再次罗列内部障碍。 |

## Main figures and tables

### F1 — PDF page 6

Question: 常见比较为何产生混杂，以及本文怎样控制它。

Observed design: 上方三条彩色训练路径汇入同一基准；下方统一正类先划分，再交叉负类采样与架构，训练和基准用蓝/红背景区分。矩形/椭圆/六边形区分数据/采样/模型。

Transferable feature: 图示直接连接问题与实验，不只是给软件模块画框；同一对象跨面板保持角色一致。

Caution: 下部交叉箭头和长图注较密；不必复制形状数量。示意仅画3类，实际12×11×5在正文定义。

### F2 — PDF page 8

Question: 同源采样优势是否存在、哪一因素解释较多变化。

Observed design: A以同法AUC和异法AUC作成对散点，等值线让方向一眼可见；B/C/D为横向箱线，分别按架构、训练采样和测试采样分组，共用AUC语义。

Transferable feature: 配对对照和分布展示组合，均值结论与变异范围互补；点旁标签减少来回查图例。

Caution: 不少标签小、颜色近似，B/C/D轴起点并非完全一致，图注有措辞可改善；学习功能不照搬所有视觉细节。

### F3 — PDF page 9

Question: 每个训练×测试组合的均值与重复波动。

Observed design: 3×4排列12幅热图，行列顺序统一；每格颜色编码平均AUC，黑点大小编码SD；黑框标出同法对角线，全图共用色标和点径图例。

Transferable feature: 展示完整交叉组合而非只挑最好；一套坐标同时让读者看均值、稳定性和同法效应。

Caution: 双编码对小尺寸阅读要求高；多个模型相似配色需清楚刻度；不能把点径误写成样本量。

### T1 — PDF page 3

Purpose: 将11种负类采样操作化为可比较变量。

Observed design: 整页横向、少横线、无竖网格，列为采样法、排除关键词、长度、去冗余、额外筛选、平衡性、来源。

Transferable feature: 一行一个研究对象，一列一个会影响结论的设计选择，来源逐行可追溯。

### T2 — PDF page 5

Purpose: 将12个架构的特征与学习器差异摆在同一框架。

Observed design: 整页横向，按深度/非深度分组；列架构、年份、特征规模、提取、选择、算法、引文。长文本自动换行。

Transferable feature: 把方法说明与文献来历结合，正文可聚焦差异为何重要。

## Applying the experiment-writing lesson

State the question, common conditions, changed factors, experimental unit and measurement before interpreting the outcome. A complete comparison can be more informative than one favorable score. The exemplar's five sampling repeats measure variation across those sampled datasets; do not automatically relabel them as training-seed replication. Describe what was actually repeated in any new paper.

For generative AMP work, reconstruction, generation, property prediction and measured activity form distinct questions. A shared strain or dataset name does not itself create a fair performance comparison. A case study can motivate an evaluation choice without being a baseline.

Use low-order distribution metrics for the properties they measure. Residue composition and dipeptide frequencies cannot establish full sequence-distribution equivalence. Separate sampling variability within one trained model from variability across independent training runs; do not derive a fictitious across-seed CI from within-run samples.

For wet experiments, state the tested peptide panel, strain identifiers, concentration units, endpoint definition and biological/technical replication. Procurement details may be irrelevant to the main paper. Eligibility and denominators still follow the research question. A resolved or unresolved difference affecting a scientific interpretation cannot disappear merely because another presentation looks stronger.

The exemplar has no new wet laboratory experiment. It supports experiment organization, not specific assay protocols. Do not infer culture conditions or synthesis provenance from it.

## Endmatter and references

Three Key Points map to study scope, principal problem and remedy. Acknowledgments, funding and availability are separate from the scientific argument. The 13 author biographies belong to the published layout and should not inflate scientific word counts. The acknowledgment of draft readers is not proof of formal referee identity. The 59 references perform different roles—biology, data, methods, adjacent-domain problems and reproducibility—not a quota to reproduce.
