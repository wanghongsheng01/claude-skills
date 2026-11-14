# CCF-A 数据库论文 图 / 图注 / 表 / 版式 原则与红线（FIGURE_PRINCIPLES v1）

更新：2026-11-14（太平洋时间）。用途：作图人、审图人、改图人共用的清单。审图人和改图人必须是两个不同的 agent，循环到审图人挑不出 blocker/major 为止，之后才交给作者。

## 0. 学习样本（26 篇，2024–2026 已录用的 SIGMOD / PVLDB / ICDE 论文）

全部从官方 PVLDB 页面或已录用论文的 arXiv 版下载，存放在 `_figure_craft/refs/`。每篇前 14 页都按 70 dpi 渲染成缩略总览（`renders/sheets/`），26 篇的图注和表题全部抽成文本（`caps/`），下表 [ ] 内的 12 张图另按 100 dpi 逐页细看（`renders/zoom/`）。

| 代号 | 论文 | 会议/轨道 | 重点看了什么 |
|---|---|---|---|
| Bu24 | Bu et al., *Adaptive and Robust Query Execution for Lakehouses at Scale* (Databricks) | PVLDB 17, p3947（工业） | [Fig.1 架构图] 线型图例，3 句图注 |
| Yang25 | Yang et al., *Unlocking the Power of CI/CD for Data Pipelines in Distributed Data Warehouses* (Google) | PVLDB 18, p4887（工业） | [Fig.1 组件图] 网格对齐、等大方框 |
| Okol24 | Okolnychyi et al., *Petabyte-Scale Row-Level Operations in Data Lakehouses* (Apple) | PVLDB 17, p4159（工业） | [Fig.9/10] 图例在轴外上方，轴标题带单位和刻度类型 |
| Karp25 | Karpathiotakis et al., *Scribe: How Meta transports zettabytes per day* | PVLDB 18, p4817（工业） | [Fig.1] 区域容器 + 颜色编码（反例：字太小） |
| Schm25 | Schmidt et al., *SQLStorm* | PVLDB 18, p4144 | [Fig.7/8] 共享图例放在轴外，单位写成 [ms]，图注结论先行 |
| Xie25 | Xie et al., *SiriusBI* (Tencent) | PVLDB 18, p4860（工业） | [Fig.2 工作流] 分区着色（反例：字太小） |
| Yadav26 | Yadav et al., *Enzyme: Incremental View Maintenance for Data Engineering* (Databricks) | SIGMOD Companion '26（工业），arXiv 2603.27775 | [Fig.8] 图注写明对数轴（反例：x 刻度标签旋转拥挤，y 轴标题过小） |
| Liu26 | Liu et al., *Workload-Aware Incremental Reclustering in Cloud Data Warehouses* | PACMMOD 4(3) (SIGMOD 2026)，arXiv 2602.23289 | [Fig.9 工作流，Fig.10 结果] 多面板共用一个图例放在顶部；"Fig. N. 短标题. 解释" 的图注 |
| Zhou26 | Zhou et al., *SALUS: Automated Auditing of NL-to-SQL Benchmarks* | PACMMOD (SIGMOD 2027)，arXiv 2610.05540 | [Fig.2 流水线] 左→右，直角折线，用括号给阶段分组 |
| Nezha26 | *Nezha: A Key-Value Separated Distributed Store with Optimized Raft* | ICDE 2026，arXiv 2603.09122 | [Fig.3 架构图] 图中 ①–⑥ 步骤编号与正文对应；[Fig.4–6] 反例：图例画在柱子上方的数据区里 |
| Saxena24 | *Why TPC Is Not Enough: An Analysis of the Amazon Redshift Fleet* | PVLDB 17, p3694（工业） | 缩略总览 + 图注 |
| Shi24 | *Practical Insights into Large-Scale Spark Workloads at ByteDance* | PVLDB 17, p3759（工业） | 缩略总览 + 图注 |
| Chen24a | *UniView* | PVLDB 17, p4353（demo） | 架构图 |
| Chen24b | *TDSQL: Tencent Distributed Database System* | PVLDB 17, p3869（工业） | 缩略总览 + 图注 |
| Zhou25a | *AnalyticDB-PG* (Alibaba) | PVLDB 18, p5139（工业） | 缩略总览 + 图注 |
| Zhou25b | *Streaming View* (Alibaba) | PVLDB 18, p5153（工业） | 缩略总览 + 图注 |
| Bress25 | *Workload Insights From the Snowflake Data Cloud* | PVLDB 18, p5126（工业） | 分布图、表 |
| Emani25 | *Horizon: Robust Checks for SQL Migration Using LLMs* | PVLDB 18, p5259 | 系统总览图 |
| Shankar25 | *DocETL* | PVLDB 18, p3035 | 缩略总览 |
| Shankar24 | *SPADE* | PVLDB 17, p4173 | 图注、表 |
| Gao24 | *Text-to-SQL Empowered by LLMs: A Benchmark Evaluation* | PVLDB 17, p1132 | 结果图 |
| Kaminsky25 | *Incremental Detection of Denial Constraint Violations* | PVLDB 18, p1000 | 结果图 |
| RBAC27 | *Benchmarking Text-to-SQL under Role-Based Access Control* | SIGMOD 2027，arXiv 2607.22115 | 表、图注 |
| DIVER26 | *DIVER: A Robust Text-to-SQL System* | SIGMOD 2026，arXiv 2602.12064 | 工作流图、表 |
| Fusion26 | *An Efficient and Effective Evaluator for Text2SQL Models* | ICDE 2026，arXiv 2603.07841 | 框架图、图注 |
| LivingDB26 | *Living Databases* | ICDE 2026，arXiv 2605.00676 | 图注 |

图注统计（从 26 篇抽取的 83 条 Figure 图注，按正则估计）：约 54% 不止一句，第一句是短标题，后面接解释或结论；约 24% 只有 ≤8 个词的标题（这类多见于纯系统描述图，在结果图上算弱点）。

**重要观察**：已发表论文也会犯错，例如 Bu24 的曲线穿过虚线容器、Yadav26 的刻度标签旋转拥挤、Nezha26 的图例压在柱子上、Karp25 和 Xie25 的字太小。审稿人能容忍，不等于我们可以犯。本清单里的红线取自 作者的明确要求加上最好的样本，比平均发表水平更严。

---

## 1. 硬红线 R1–R16（任何一条不过，图都不能交付；违反算 blocker）

| 编号 | 红线 | 来源 / 正例 |
|---|---|---|
| **R1** | **箭头和连线不得穿过任何方框、节点或文字**（包括图注、标签、图例）。连线只能在框与框之间的空白通道里走。 | 作者对某在投工业稿流水线图的批评（2026-11-14：线穿过框）；正例 Yang25 Fig.1、Zhou26 Fig.2、Liu26 Fig.9：没有一根线穿框 |
| **R2** | **线不得压在文字上**：边标签（yes/no、数据名）不能被别的线划过；标签要放在线旁的空白处，必要时加白底（`fill=white, inner sep=1pt`）。 | 正例 Liu26 Fig.9（"synced"、"Yes" 都在线旁空白处）；Zhou26 Fig.2 |
| **R3** | **图例不得覆盖数据**（曲线、柱子、散点、误差线）。图例优先放在轴外上方（多面板共用一个），其次放在经确认的空白区域。 | 作者对某在投稿 CDF 图和条形图的批评（图例压曲线、压柱顶）；正例 Schm25 Fig.7、Liu26 Fig.10、Okol24 Fig.9（全部放在轴外上方）；反例 Nezha26 Fig.4–6 |
| **R4** | **轴标题、刻度标签、图例、面板标题都不得被裁切，也不得越出图框或互相重叠**（`bbox_inches='tight'`，并在最终 PDF 中逐图核对）。 | 作者对某在投稿条形图 y 轴标题被裁的批评 |
| **R5** | **文字和文字不得重叠**：页眉和会议名、图中标签之间、图注和图、相邻面板的刻度（如 "80" 紧贴下一面板的 "0"）、表格和正文都不能重叠。 | 作者对某在投稿页眉与会议名重叠的批评 |
| **R6** | **印刷尺寸下图中最小字号 ≥ 6 pt**（ACM 正文 9 pt，图内文字建议 7–8 pt）。matplotlib 要按最终宽度出图（单栏 3.33 in，双栏 7 in），不要先画大图再缩小。 | 正例 Schm25、Liu26（图字约 7 pt）；反例 Karp25 Fig.1、Xie25 Fig.2 |
| **R7** | **不得有越界或溢出**：图、表、公式不能伸进页边距或另一栏；log 中 Overfull \hbox 大于 1 pt 的必须处理。 | ACM/PVLDB 模板要求；pvldb-paper-craft 版式检查 |
| **R8** | **成稿里不得留占位符、TODO、"pending"、"TBD"、[??]、未定义引用**。 | 投稿底线 |
| **R9** | **每根轴都要有标题，量纲要有单位**（`time (s)`、`rows (%)`、`Runtime [ms]`）；对数轴要在轴标题或图注里写明。 | Okol24 "Write Time (seconds, log scale)"；Yadav26 图注 "Note that the y-axis is log scale"；Schm25 "Runtime [ms]" |
| **R10** | **图中信息不能只靠颜色区分**：红/绿不能当唯一区分；同时用线型、标记或填充纹理，灰度打印后仍能分辨。 | Liu26 Fig.10 用实心和斜线纹理区分 query 和 recluster；Okol24 Fig.10 用纹理区分 eager 和 lazy |
| **R11** | **多面板图里，刻度不同的面板必须各自有 y 轴标题，或在面板标题里写明**；不能让读者误以为几个面板共用刻度。 | Schm25 Fig.8 每个面板各有标注 |
| **R12** | **数据标签（柱顶数字等）不得与柱子、误差线、轴线或其他标签重叠**。 | Liu26 Fig.10：柱顶倍数不碰柱子也不碰相邻标签 |
| **R13** | **方框里的文字不得断词**（"met-ric"、"speci-fied"），也不得溢出方框。框宽要按最长的词设定，或手动 `\\` 换行。 | 正例 Yang25、Zhou26、Liu26：所有框内文字都完整 |
| **R14** | **箭头必须有明确的起点和终点**：箭头尖端接在框边中点或均匀分布的锚点上，不能落在框角，不能与别的出边或入边重叠；箭头尖要在印刷尺寸下看得清。 | 正例 Yang25 Fig.1、Liu26 Fig.9 |
| **R15** | **流程图不得有悬空节点**：每个节点都要有入边或出边，或者在图注里说明它是终点或输出。 | 正例 Zhou26 Fig.2 |
| **R16** | **图、表的数字必须与正文和表格逐一一致**（审图时抽查 3 个以上数字）。 | 投稿底线（"数字永不改，结果不隐藏"） |

## 2. 风格规则 S1–S29（违反算 major 或 minor）

### 2a. 架构图 / 流水线图
| 编号 | 规则 | 来源 |
|---|---|---|
| S1 | 单一主流向：左→右，或上→下。需要换行时用"蛇形"布局，并让回流线在最外侧的独立通道里走。 | Zhou26 Fig.2（左→右）、Liu26 Fig.9、Yang25 Fig.1 |
| S2 | 节点放在网格上：同一层的框顶端对齐、等高；同类框等宽，框间距一致。 | Yang25 Fig.1、Zhou26 Fig.2 |
| S3 | 连线用直线或直角折线（TikZ `-|`、`|-`），不用随手画的曲线；交叉越少越好，非交叉不可时用跨线桥或改变布局。 | Zhou26 Fig.2；反例 Bu24 Fig.1 的曲线穿过虚线容器 |
| S4 | 线型和颜色各有固定含义，并在图内放小图例或在图注里说明（如"实线：数据流；虚线：控制/元数据"）。 | Bu24 Fig.1 底部的线型图例；Liu26 Fig.9 用虚线表示元数据 |
| S5 | 步骤编号用 ①②③ 或 (1)(2)，正文按编号逐步引用。 | Nezha26 Fig.3 与正文 Step ①–⑥ |
| S6 | 用分组框或括号表示阶段或子系统，分组框的边不能与内部节点的边重合或相交。 | Zhou26 Fig.2 的括号；Karp25 的区域容器 |
| S7 | 颜色最多 3–4 种，只用来强调"我们的组件"或类别；颜色用色盲友好调色板（Okabe-Ito/ColorBrewer），不用红绿对。 | Zhou26（橙色表示方法组件）；Liu26 用蓝色系 |
| S8 | 图字体与正文同族或接近（ACM：Libertine/Biolinum；PVLDB 同理），所有图的字体一致。 | Schm25、Liu26 图文字体统一 |

### 2b. 结果图（plot）
| 编号 | 规则 | 来源 |
|---|---|---|
| S9 | 多面板图共用一个图例，放在所有面板上方的轴外。 | Liu26 Fig.10、Schm25 Fig.7 |
| S10 | 刻度标签不拥挤：类别多时改用横向条形图，或缩写后在图注里解释；不要用 45° 旋转去硬塞（Yadav26 Fig.8 的反例）。 | Yadav26 反例；Bress25 用横向分布图 |
| S11 | 同一篇论文里，同一方法在所有图中用同一颜色、同一标记、同一线型；"我们的方法"用最醒目的颜色并放在图例最后或最前。 | Liu26（WAIR 一律深蓝）、Schm25 |
| S12 | 网格线浅（灰、细），对数轴不要把每条次网格线都画出来。 | Schm25、Okol24 |
| S13 | 数据跨越多个数量级时用对数轴，并标明（见 R9）。 | Yadav26、Schm25 |
| S14 | 重叠的标记要错开、调透明度或换空心标记，保证每个点都能看见。 | 审图经验（反例：某在投稿点图中三角压住方块） |
| S15 | 图的宽高比按栏宽设计，图里不留大片空白，也不压缩到字挤在一起。 | Liu26、Okol24 |

### 2c. 表格
| 编号 | 规则 | 来源 |
|---|---|---|
| S16 | 用 booktabs（`\toprule \midrule \bottomrule`），**不用竖线**，横线尽量少。 | 样本渲染页中所见的表格（如 Yang25 表1–2、Bu24 表1、Bress25）均为三线表 |
| S17 | 数字列右对齐或按小数点对齐（`siunitx S` 列），小数位一致；文字列左对齐，长文字列用 `>{\raggedright\arraybackslash}p{}`，不要两端对齐导致字间距被拉开。 | 样本渲染页中的数值表 |
| S18 | 主结果表中每列最佳加粗，次佳加下划线（我们的 SOTA 规则），并在表题里写明"越高越好/越低越好"。 | DIVER26 表 3（标出前三）；我们的 SOTA 门禁规则 |
| S19 | 表字号 ≥ 7 pt；不要用 `\resizebox` 把宽表缩到很小，应该拆表、缩写列名或改用双栏 `table*`。 | 投稿底线；R6 |
| S20 | 表题在表上方，图注在图下方（ACM/IEEE 惯例）。 | 全部样本 |

### 2d. 图注 / 表题
| 编号 | 规则 | 来源 |
|---|---|---|
| S21 | 图注能脱离正文单独读懂：第一句给出结论（我们的方法怎样），后面说明设置、数据集、编码（颜色、线型、虚线的含义）和"越高越好"。 | Schm25 Fig.7（"Scaling on SQLStorm is more challenging."）；Liu26 Fig.10；Bu24 Fig.1 |
| S22 | 图注里定义图中出现的每个缩写和符号。 | Liu26 Fig.17（"FK: …"） |
| S23 | 图注不要太长（一般 ≤4 行）；细节写进正文。 | 样本中位数约 2–3 行 |
| S24 | 图、表都要在正文里先被引用、再出现，尽量放在首次引用的那一页或下一页的顶部（`[t]`）。 | 版式惯例 |

### 2e. 页面版式（作者追加）
| 编号 | 规则 |
|---|---|
| S25 | 页眉短标题（`\shorttitle` 或 `\renewcommand\shorttitle`）不得与会议名重叠；逐页检查页眉。 |
| S26 | 证明结束的方框（QED）跟在最后一行行尾（`\qedhere`），不单独占一行。 |
| S27 | 不出现孤行、寡行，也不出现被浮动体挤出的大片空白；章节标题不留在页底。 |
| S28 | Underfull/Overfull 警告逐条处理；代码清单不能伸出栏宽。 |
| S29 | 审图和交付都必须用 pdfTeX（Overleaf 默认）编译的 PDF。XeTeX/tectonic 的字体、断行和 overfull 都与 pdfTeX 不同：实测：某稿表格在 XeTeX 下伸进右栏、压住相邻表格（overfull 46 pt），另一稿表中的 ✓ 缺字，而 pdfTeX 版都没有问题。只有拿不到 pdfTeX 版时才用 XeTeX，并在审稿意见里注明。 |

## 3. 严重度定义
- **blocker**：违反任何 R 条，或者读者会读错数据或流程。必须改。
- **major**：违反 S 条，并且明显影响专业观感或可读性（字太小、配色不安全、表格竖线、断词）。本轮必须改。
- **minor**：观感上的打磨。能改就改。

## 4. 审图流程（审图人用）
1. `git pull` 后编译，或者取最新的 Overleaf PDF。
2. 运行 `scripts/figlint.py <pdf> <outdir> --log <log>`：按 200 dpi 渲染、自动裁出每个图和表、检测文字叠字、越界文字、过小文字和 overfull 警告。
3. **逐张打开裁图，放大到 300–400 dpi 看局部**。重点看：线穿框、线压字、图例压数据、标签被裁、刻度挤、断词、字太小、颜色只靠红绿区分。
4. 每个问题写清：规则编号、位置（图号、面板、元素）、严重度、可以照着做的修改指令（例如"把 (2)→(3) 的箭头改为从 (2).south 出发，沿框下方 4 mm 的通道直角走到 (3).south"）。
5. 改图人改完后，审图人重新运行第 1–4 步。只有 0 blocker 和 0 major 才能交付。
