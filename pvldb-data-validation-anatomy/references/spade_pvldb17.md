# 范文拆解：SPADE 逐句账本（PVLDB 17(12), 2024）

> 对象：Shankar et al., "spade: Synthesizing Data Quality Assertions for Large Language Model Pipelines", PVLDB 17(12): 4173–4186, 2024, DOI 10.14778/3685800.3685835。
> 方法：pdftotext（默认 + `-layout` + 按左右栏裁切）逐栏重排；`pdftoppm -r 70` 渲染并目检 p1/p3/p4/p5/p6/p8/p9/p10 的版面。PDF 只作为数据读取。
> 版权约束：本文件不连续照抄原文超过约 12 个英文词；所有句子都是功能描述加中文转述；模板用 `<slot>` 占位。原文中的专有术语（prompt delta、FFR、subsumption 等）作为术语保留。
> 标签约定：S = 句子；P = 段落；【引】= 有引用支撑；【数】= 有数字；【例】= 用例子支撑；【前指】/【回指】= 指向后文或前文的章节、图表；【脚】= 脚注。

> 官方 PDF 的 URL、SHA256、字节数见 `provenance.md`。

## 0. 核验修正（2026-11-20，独立核验者对照官方 PDF）

几乎所有计数核验一致：摘要 188 词 / 8 句（逐句词数 21,16,19,16,30,27,28,31）；6 图 6 表；Def 3.1–3.3、0 定理、0 算法框、1 个编号公式；8 个脚注；4 条贡献分别指向 §2、§2.4、§3、§4；65 条文献全部被引；年份分箱、venue 分布、7 条自引、[50] 被用来卸载细节 4 次；各节引用密度（Intro+RW 占 79/90 个引用键 = 88%）；14% 与 21% 为 Table 4 均值的百分点差（所选比例 0.556→0.420，FFR 0.316→0.103）；F1 = 0.8135；ILP 最大运行时间 1.197 s；基线在 4/9 个 pipeline 违反 FFR（fashion、finance、lecturesum、negotiation）；§2.3 把 taxonomy 误写为 Fig 3。修正与补充如下：

| 项 | 原账本 | 核验值 |
|---|---|---|
| 参考文献篇幅 | 约 1.7 页 | 约 **1.35 页**（p14 只占两栏上部约 1/3） |
| 节起始（新增） | — | 摘要 p1L；§1 p1L；§2 p3L；§3 p6R 底部；§4 p9R 顶部；§5 p12L；§6 p12R；致谢 p12R；文献 p13L |
| 摘要中的数字（新增） | — | 4 个："nine"、14%、21%、2000 |
| §1 字数 | 约 1,450 | 约 1,530（去掉版权框、Fig 1、作者残片、脚注后） |
| 5 年内文献占比（新增） | — | 2019–2024 共 60/65 = **92.3%**；中位年份 2023 |
| 差距 <10% 的 3 个 pipeline（新增） | — | emails、negotiation、statsbot |
| 样例总数（新增） | — | 677 个（每 pipeline 均值 75.2） |
| 3.3.2 字数说明 | 约 360 | 含 73 词 Fig 6 图注；正文本身约 290 |


---

## 1. 元数据

| 项 | 值 |
|---|---|
| Venue | Proceedings of the VLDB Endowment (PVLDB) |
| Vol / Issue / Pages | Vol. 17, No. 12, pp. 4173–4186 |
| DOI | 10.14778/3685800.3685835 |
| Track | **未声明（unknown）**。首页、页脚、版权框、PVLDB Reference Format 都没有写 Research / Industry / EA&B / SDS 等字样；PDF 元数据的 Subject/Keywords 为空。唯一的版面线索是首页右上角的 ACM "Artifacts Available v1.1" 徽章 |
| 模板 | acmart（PDF Creator 字段为 acmart 2020/02/22 v1.70），双栏，letter 尺寸 |
| 总页数 | 14 |
| 正文页 | p1–p12（第 12 页右栏底部为 Acknowledgments），共 12 页 |
| 参考文献页 | p13 全页 + p14 两栏上部约 1/3（约 **1.35 页**，核验修正；原记约 1.7 页） |
| 作者/机构 | 10 位作者；UC Berkeley、HKUST、LangChain（2 位工业界作者）、Columbia |
| Artifact | 首页给出 GitHub 仓库；另外脚注给出 Streamlit app、taxonomy 标注 CSV、LangChain Hub 链接 |

### 1.1 各节字数（约数；按栏裁切后去掉代码行和短行估算，图注与表内文字只去掉一部分，所以偏高约 5–10%）

| 节 | 约字数 | 备注 |
|---|---|---|
| Abstract | 188（精确） | 8 句 |
| 1 Introduction | ~1,450 | 除去首页版权框/引用格式后的估计；含 4 条贡献 bullet |
| 2 Identifying Candidate Assertions（总） | ~2,500 | |
| 　2 引言段 | ~30 | |
| 　2.1 Prompt Deltas | ~280 | |
| 　2.2 Prompt Delta Analysis | ~700 | 不含 Table 1/2 表体 |
| 　2.3 From Taxonomy to Assertions | ~600 | 不含 Fig 3 中的代码 |
| 　2.4 Initial Deployment | ~900 | 不含代码清单与 Fig 4/5 |
| 3 Filtering Candidate Assertions（总） | ~2,650 | |
| 　3 引言段 | ~55 | |
| 　3.1 Definitions | ~450 | 含 Def 3.1/3.2 |
| 　3.2 Coverage Problem Formulation | ~460 | 含完整 ILP |
| 　3.3（3.3.1 之前） | ~430 | 含 Def 3.3 |
| 　3.3.1 ILP with Subsumption Constraints | ~500 | |
| 　3.3.2 Assessing Subsumption | ~360 | 含 Eq.(1) |
| 　3.3.3 Subsumption without Examples | ~450 | |
| 4 Evaluation（总） | ~1,800 | |
| 　4 引言段 | ~35 | |
| 　4.1 Pipeline and Dataset Descriptions | ~270 | |
| 　4.2 Method Comparison and Metrics | ~500 | 不含 Table 3/4 表体 |
| 　4.3 Results and Discussion | ~1,000 | 不含 4 段代码清单 |
| 5 Related Work | ~480 | |
| 6 Conclusion and Future Work | ~315 | |
| Acknowledgments | ~60 | |
| 正文合计 | 约 9,300–9,700 | |
| References | ~1,900 | |

结构比例：Intro 约占正文 15%；方法（§2+§3）约 55%；实验约 19%；RW 只有约 5%，并放在实验之后。

### 1.2 参考文献

- 总数：**65** 条，正文全部引用到（没有只列不引的条目）。
- 年份分布：

| 区间 | 条数 | 占比 |
|---|---|---|
| ≤2010 | 2（[6] 2008、[17] 2005） | 3% |
| 2011–2018 | 3（[22] 2017、[39] 2018、[46] 2018） | 5% |
| 2019–2022 | 23 | 35% |
| 2023–2024 | 37（其中 2024 只有自引技术报告 [50]） | 57% |

- 出处分布（按条目所列 venue 归类）：

| 类别 | 条数 | 条目 |
|---|---|---|
| DB 核心（SIGMOD/PVLDB/VLDBJ/SIGMOD Record/SIGMOD Companion） | 9 | [1][16][19][24][39][40][42][45][46] |
| DB 邻近（CIKM） | 1 | [47] |
| ML/AI/NLP 正式会议或期刊（MLSys/SysML、NeurIPS、ICLR、JAIR、NIPS workshop） | 8 | [4][5][18][22][25][29][57][59] |
| 数据挖掘（KDD） | 1 | [33] |
| HCI（CHI / CHI EA） | 3 | [60][61][63] |
| SE（ICSE） | 1 | [28] |
| 综述期刊（ACM CSUR） | 2 | [30][36] |
| OR/其他书章（INFORMS、Springer） | 2 | [6][17] |
| **arXiv 预印本** | **34** | 约 52% |
| GitHub 工具/博客 | 4 | [21][27][31][51] |

- 小结：DB 类 venue 只占约 15%（含 CIKM），arXiv 超过一半。这是 2024 年 LLM×DB 交叉论文的典型分布。DB 引用集中在两个位置：Intro 中"传统 ML 数据校验不适用"那一句，以及 RW 的最后一段。
- 自引：作者团队相关 7 条（[37][47][48][49][50][51][63]），其中 [50] 是本文 arXiv 技术报告，被用作卸载细节的去处（4 次）。
- 值得注意的细节：arXiv 技术报告 [50] 的标题是 "SPADE: Synthesizing Assertions for LLM Pipelines"，PVLDB 版本标题加了 **"Data Quality"**，这是一次明确面向 DB 社区的重新定位（见 §2 标题解剖）。

### 1.3 构件计数

| 构件 | 数量 | 说明 |
|---|---|---|
| Figures | 6 | Fig1 系统流程（teaser）；Fig2 taxonomy 树；Fig3 从 ΔP 到断言的生成流程（含代码）；Fig4 工具截图；Fig5 用途分布条形图；Fig6 subsumption DAG |
| Tables | 6 | T1 7 个 prompt 版本的 ΔP（跨栏）；T2 类别说明；T3 数据集（跨栏）；T4 主结果；T5 subsumption precision；T6 ILP 运行时间 |
| Definitions | 3 | Def 3.1 Coverage、Def 3.2 FFR、Def 3.3 Subsumption；另有 prompt delta 的段内定义（2.1）和 criterion 的"宽松定义"（2.3） |
| Theorems/Lemmas/Propositions | **0** | NP-hard（3.2）和 PTIME（3.3.3）都用正文论证给出，没有定理环境，也没有正式证明 |
| Algorithms（伪代码） | **0** | 3.3.3 用文字描述拓扑排序 |
| Examples（正式环境） | **0** | 用 run-in 粗体的 "Example LLM Pipeline" 段和多个段内例子（gratitude_v1–v3、JSON list f/g、conciseness 等）替代 |
| 显示的优化问题 | 5 | 3.2 抽象问题 + 完整 ILP；3.3.1 抽象问题 + 完整 ILP（改动处标蓝）；3.3.3 无样例 ILP |
| 带编号公式 | 1 | Eq.(1)，FFR 的上下界 |
| 代码清单（图外） | 4 块 / 9 个函数 | p6（2 个）、p11（3+3+1 个）；Fig 3 中另有 2 个函数 |
| Footnotes | 8 | 1 个解释命名的双关；7 个 URL（app、CSV、tweet、复现仓库、Hub 等） |
| Contributions bullets | 4 | 每条以 "(Section X)" 结尾 |

---

## 2. 标题解剖

`spade: Synthesizing Data Quality Assertions for Large Language Model Pipelines`（10 词）

| 成分 | 功能 | 可复用要点 |
|---|---|---|
| `spade`（小型大写，首页图里配了黑桃符号） | 系统名，品牌化 | 缩写全称在 Intro 才展开（System for Prompt Analysis and Delta-Based Evaluation），命名双关放在脚注 1，标题里不解释 |
| `:` | 系统名与描述分隔 | "<System>: <Gerund> <Object> for <Setting>" 是 PVLDB 系统论文最常见的形式 |
| `Synthesizing` | 动名词，说明系统做的动作 | 用"合成/生成"这类带 PL/DB 色彩的动词，不用 "Using LLMs to…" |
| `Data Quality Assertions` | 产物，用 DB 社区熟悉的概念命名 | 与 arXiv 版标题对比可见，"Data Quality" 是为 PVLDB 加上的。**把新问题挂到 DB 的老概念上**（data quality / assertions / constraints） |
| `for Large Language Model Pipelines` | 应用场景 | "pipeline" 一词把 LLM 调用重新框定为数据处理算子（Intro 第一段正是这样展开的） |

模板：`<system>: <Gerund-verb> <DB-familiar artifact> for <emerging workload>`

---

## 3. 摘要逐句（188 词，8 句）

| # | Move | 中文转述 | 模板 | 词数 |
|---|---|---|---|---|
| A1 | Context | LLM 越来越多地作为 pipeline 的一环，被反复用来处理或生成数据 | `<technology> is increasingly deployed as part of <workload> that repeatedly <operation>.` | 21 |
| A2 | Problem | 部署的主要障碍是 LLM 频繁且难以预测的错误 | `However, a key barrier to <deployment> is the frequent and unpredictable <failure type> of <technology>.` | 16 |
| A3 | Approach（问题重构） | 既然错误不可避免，就提出用"数据质量断言"来发现 LLM 可能出错的时刻 | `Accepting that <failures> are inevitable, we propose <DB concept> to detect when <technology> errs.` | 19 |
| A4 | Approach（系统登场） | 介绍 spade：自动合成断言、识别坏输出的方法 | `We present <system>, a method for automatically <verb-ing> <artifact> that <purpose>.` | 16 |
| A5 | Key-idea（观察） | 观察：开发者在原型期就会发现质量问题，并不断往 prompt 里加指令来修补 | `We observe that <users> already <implicit behavior> during <phase>, by <observable trace>.` | 30 |
| A6 | Technique | 因此 spade 分析 prompt 版本历史生成候选断言，再选出同时满足覆盖率与准确性要求的最小集合 | `<System> therefore mines <trace> to generate candidate <artifacts>, then selects a minimal subset satisfying <constraint1> and <constraint2>.` | 27 |
| A7 | Result-with-number | 在 9 个真实 pipeline 上，相比更简单的基线，断言数减少 14%，误报失败减少 21% | `Across <N> real-world <workloads>, <system> reduces <metric1> by <x%> and <metric2> by <y%> versus <baseline class>.` | 28 |
| A8 | Deployment / Impact | 已作为 LangSmith 的功能上线，为 2000+ 个跨行业 pipeline 生成过断言 | `<System> is deployed in <product> and has been used for <N>+ <units> across <scope>.` | 31 |

**摘要层面的观察**
1. 结构是 Context→Problem→Approach（重构）→System→Insight→Technique→Result→Deployment。没有单独的 Gap 句：A3 的"既然错误不可避免"同时承担了 gap（与其消除错误，不如检测错误）。
2. A5→A6 用 "therefore" 把"观察"和"技术"连成因果链：技术是从观察推出来的，不是凭空设计的。这是 insight-driven 写法的核心。
3. 两个数字（14%、21%）都绑定了比较对象（"simpler baselines"）。经核对 Table 4，二者都是 **9 个 pipeline 均值的百分点差**（选中比例 0.556→0.420；FFR 0.316→0.103），不是相对降幅（相对降幅分别约 25% 和 67%）。原文没有说明这一点。**写作教训：明确写 "percentage points" 还是 "relative"。**
4. 部署证据（A8）放在受控实验结果（A7）**之后**，两者各占一句，没有混写。
5. A7 中的 "efficiently" 没有对应的效率主张（实验只报告了 ILP 运行时间）。属于形容词溢出，不建议模仿。

---

## 4. 全文逐节、逐段、逐句

### 4.0 首页非正文元素
- **Fig 1 放在 p1 右栏顶部**：读者在 Intro 第一段旁就能看到系统全貌（开发者编辑 prompt→版本历史→①生成候选→②用带标签的输入输出过滤→要部署的断言）。图注 45 词，讲了两步流程。
- PVLDB Reference Format 和 Artifact Availability 框在左栏，Intro 从左栏下部开始。

---

### §1 INTRODUCTION（~1,450 词；10 个段落单元 + 4 条 bullet；Intro 内部用 run-in 粗体小标题把自己组织成"迷你论文"）

**I-P1 段落角色：Context，把 LLM 重新框定为数据处理算子（面向 DB 读者）**
- S1 `Context`：业界对用 LLM 处理、理解、生成数据热情高涨。【引 16（PVLDB 愿景论文）】 模板：`There is growing excitement around using <tech> for <data tasks> [<DB vision cite>].`
- S2 `Context/定义`：不需要大量标注数据，写一个自然语言 prompt 就能对一批数据项构建 LLM pipeline（斜体引入术语 *LLM pipeline*）。
- S3 `Context/例举`：可覆盖传统数据处理，如逐文档摘要、实体抽取、按元组补缺失值。【引 34】【例】 措辞上用"each tuple in a relation"，有意说 DB 的语言。
- S4 `Context/例举`：LLM 还支持生成型任务，如推荐理由、销售邮件、博客草稿。【例】
- S5 `Problem`：无论离线批处理还是在线逐条处理，规模化部署都面临 LLM 看似随机的数据质量错误：违背指令、格式错误、幻觉。【引 23；48, 63】 模板：`Deploying <workload> at scale—offline or online—is challenging due to <error class> [cite], e.g., <e1>, <e2>, <e3> [cite].`

**I-P2 段落角色：解法类别 → Gap → 挑战清单 → 与最接近的 DB 工作切割 → 研究问题**
- S1 `Approach-space`：发现错误的一条途径是数据质量断言。
- S2 `Prior work`：近期论文和 pipeline 工具已支持嵌入人工编写或人工挑选的断言。【引 26,41,54；21,27,31】
- S3 `Gap + 产业权威`：但"该加哪些断言"仍是开放问题，也是作者在 LangChain 观察到的大痛点。【无引用，用作者的工业身份背书】 模板：`However, determining <which X> remains open—and is a major pain point we observe at <org>.`
- S4 `Gap 证据`：开发者难以为自定义任务确定合适的断言集合。【引 38】
- S5 `Challenge list`：四个难点：预测所有失败模式；用多种规格方式写断言很耗时；断言需要精确（尤其涉及 LLM 调用时）；很多开发者缺乏编程经验。【引 26,63】
- S6 `Challenge 2`：断言无信息量或数量太多，会让开发者疲于监控（为后文的"最小集合"目标埋伏笔）。
- S7 `Gap vs DB 近邻`：传统 ML pipeline 的自动错误检测面向批量结构化记录，不适用于非结构化输出。【引 4,39,46,47（DB/MLSys）】 模板：`While <prior line> addresses <old setting> [cites], it assumes <property>, which does not hold for <new setting>.`
- S8 `Research question`：明确提出问题句：能否以最少的开发者投入为 LLM pipeline 找到数据质量断言？ 模板：`We therefore ask: can we <goal> with as little <cost> as possible?`

**I-P3 "Example LLM Pipeline." 段落角色：Running example（贯穿全文的电影推荐）**
- S1 `Example setup`：设想一个流媒体平台的 pipeline，为某用户生成某部电影的推荐理由段落。【例】
- S2 `Example 细节`：开发者写一个含 `{personal_info}`、`{movie_info}` 占位符的模板，对大量用户-电影对执行。
- S3 `Example 失败`：prompt 看似够用，测试时却出现：提到用户没看过的电影、提到敏感属性、输出太短。
- S4 `Observed behavior`：开发者通常往 prompt 里加指令来修补（例如不提种族）。
- S5 `Need`：LLM 仍可能不可预测地违背这些指令，所以部署时需要事后断言。 模板：`Yet <tech> may still violate <fixes> unpredictably, necessitating <post-hoc mechanism> at deployment.`

**I-P4 "Analyzing Prompt Version Histories." 段落角色：Insight 1（数据支撑）→ 实证研究 → 副产品**
- S1 `Key-idea 1`：第一个洞见是挖掘 prompt 版本历史来得到断言标准，因为开发者通过 prompt 的变化隐式编码了质量要求（斜体引入术语 *prompt deltas*）。 模板：`Our first insight is that <trace> encodes <requirements> implicitly, since <users> <behavior>.`
- S2 `Example 回扣`：例子中"至少 3 句""不提种族"等指令都可以对应一个候选断言。【例】
- S3 `Empirical study`：为了理解 delta 类型并验证其价值，作者分析了 19 个 LangChain 用户 pipeline 的版本历史。【数】
- S4 `Contribution 副产品`：由此构建 prompt delta taxonomy（Fig 2），并称其可能有独立的研究价值。【前指 Fig2】 模板：`From this analysis we derive <taxonomy> (Fig. X), which may be of independent interest to <community>.`

**I-P5 "Redundancy in Data Quality Assertions." 段落角色：Insight 2（从生成转向挑选）**
- S1 `Key-idea 2 / Problem+数`：第二个洞见：从 delta 用 LLM 生成候选会得到太多断言，几个 delta 就常超过 50 个。【数】
- S2 `Problem 细化`：许多冗余，另一些太模糊（如"简洁"）。【例】
- S3 `Challenge → motivates component`：即使工程师也很难去冗余，因为断言本身可能调用准确率不一的 LLM，所以需要自动过滤组件。
- S4 `Strawman → set-level 难点`：可以用少量标注估计每条断言的 FP/FN，但整体选出"既抓得多又少误报"的集合并不简单。 模板：`One could estimate <per-item metric> from <few labels>—but jointly choosing <set> that <obj1> while <obj2> is non-trivial.`

**I-P6 "spade: Our Data Quality Assertion Generation Framework." 段落角色：系统登场 + 目标的自然语言版**
- S1 `Approach`：基于以上洞见开发 spade（展开缩写，指向 Fig 1，脚注 1 是命名双关）。【回指 Fig1】【脚】
- S2 `Objective（prose）`：目标是选出重叠最小的布尔断言集合，最大化坏输出覆盖、最小化合取后的误报失败（括号内给出 false failure 的定义）。这句话就是 §3 形式化的自然语言预告。 模板：`<System>'s goal is to select <set> with minimal <redundancy>, maximizing <coverage> and minimizing <error> for <aggregation semantics>.`
- S3 `Architecture`：分为两个组件：候选生成与过滤。

**I-P7 "Component 1: Prompt Deltas for Candidate Assertion Generation." 段落角色：组件 1 技术 + 部署证据前置**
- S1 `Technique + contrast`：不直接让 LLM 针对整个 prompt 写断言（会漏掉部分内容），而是逐个 delta 生成，因为 delta 往往对应具体的失败模式。 模板：`Instead of directly <naive>, which <failure>, we <technique>, since <reason>.`
- S2 `Technique`：先用 taxonomy 自动分类 delta，再合成 Python 函数（可内含 LLM 调用）作为候选。
- S3 `Deployment+数（加粗）`：与 LangChain 合作公开发布了该组件，已被 2000+ 个 pipeline 使用，覆盖 10+ 行业。【引 51 博客】【数】 **这是全文唯一的正文加粗句**，把部署证据放在最显眼的位置。
- S4 `Forward-ref`：使用分析见 2.4 节。【前指】

**I-P8 "Component 2: Filtering Candidate Assertions with Limited Data." 段落角色：组件 2 的"朴素→不足→难度→可解"四连**
- S1 `Technique + contrast`：不需要人工挑选或微调单独的模型，只需少量通常已有的标注样例。【引 43,57】
- S2 `Naive`：可以估计每条断言的 FFR，并剔除超过阈值的（首次定义 FFR）。
- S3 `Why naive fails`：但选的是集合，集合的 FFR 仍可能超标，冗余也仍然存在。
- S4 `Hardness`：证明（文中用 "show"）在满足覆盖与 FFR 条件下选小子集是 NP-hard 的。
- S5 `Tractability`：但可以写成 ILP，在本文规模（数百到数千变量）下用求解器在合理时间内求解。 模板：`We show <problem> is NP-hard. That said, it can be cast as an ILP and solved in reasonable time at our scale (<size>).`

**I-P9（无小标题，接续组件 2）段落角色：低数据子问题 → 新概念**
- S1 `Sub-problem`：标注样例少时，可能覆盖不到所有失败模式，导致有价值的断言被丢掉。
- S2 `Running example`：例子中"少于 200 词"的正确断言，如果样本里没有违反者，就会被丢掉。【例】
- S3 `Alternative dismissed`：主动学习或弱监督可以补样本，但成本高，非程序员也难以使用。【引 6,40】
- S4 `Key-idea 3`：引入 assertion subsumption：一个断言不包含另一个的失败模式时，两者都保留。
- S5 `Summary`：于是 spade 在覆盖、准确、包含三类约束下选最小集合。

**I-P10 Contributions（引导句 + 4 条 bullet，每条以章节号收尾）**
- B1 `Contribution（经验/资源）`：把 prompt 版本历史识别为输出正确性的来源；基于 19 个 pipeline 建立断言标准的 taxonomy。（§2）【数】
- B2 `Contribution（系统+部署）`：提出 spade；公开发布候选生成组件并分析 2000+ 次部署。（§2.4）【数】【脚 app URL】
- B3 `Contribution（算法）`：给出满足覆盖和准确要求的最小集合选择方法；低数据场景下以 subsumption 作为新的覆盖代理。（§3）
- B4 `Contribution（评估+数）`：9 个真实 pipeline（8 个开源），每个约 75 个样例；优于不考虑断言间交互的基线，断言数 -14%、FFR -21%。（§4）
- 观察：B4 的基线被描述成 "do not consider interactions between assertions"，**用基线缺什么来定义基线**，同时也把本文的贡献点（集合层面的交互）说了出来。

---

### §2 IDENTIFYING CANDIDATE ASSERTIONS

**2-P0 段落角色：节首路标（2 句）**
- S1 `Goal`：第一个目标是生成候选断言集合。
- S2 `Roadmap`：先讲 delta 如何提示断言，再讲如何推导。 模板：`We first describe how <signal> informs <artifact>, then how to derive <artifact> from it.`

#### 2.1 Prompt Deltas

**2.1-P1 段落角色：形式化设定 + 运行例子落地**
- S1 `Setup/定义`：单步 LLM pipeline = 模板 P 用序列化的输入元组 t 填充后送入 LLM，得到响应（"tuple"一词仍是 DB 语言）。
- S2 `Setup`：开发者迭代时 P 会有多个版本。
- S3 `Notation`：令 P0 为空串，Pi 为第 i 版。
- S4 `Running example`：电影例子有 7 个版本，给出 P7 全文（长引文，斜体）。【例】

**2.1-P2 段落角色：核心概念定义**
- S1 `Definition（段内）`：ΔP_{i+1} 定义为 Pi 与 Pi+1 的 diff。
- S2 `Definition 细化`：ΔP 是句子集合，每句标为加（+）或删（−）。
- S3 `Forward-ref`：Table 1 给出例子的各版 ΔP。【前指 T1】
- S4 `Definition 细化`：加 = 新出现的句子；删 = 上一版有、这一版没有的句子。
- S5 `Edge case`：修改 = 删 + 加。
- S6 `Link to goal`：每个"加"都提示一条可能的断言标准（Table 1 最右列）。

#### 2.2 Prompt Delta Analysis

**2.2-P1 段落角色：实证研究的方法（数据来源 + 编码程序）**
- S1 `Motivation`：要了解开发者在意哪些断言，就看真实 pipeline。
- S2 `Data+数`：分析 19 个 LangChain 用户的 pipeline，每个有 3–11 个历史版本。【数】
- S3 `Diversity`：覆盖 5 个以上领域，从健身总结到统计学辅导机器人。【例】
- S4 `Offload`：细节见技术报告。【引 50】
- S5 `Method`：把 delta 分为不同类型，例如 inclusion、qualitative criteria。
- S6 `Rigor（HCI 方法）`：两位作者通过 open coding 和 axial coding 迭代 4 轮，得到 Fig 2 的 taxonomy。【数】【回指 Fig2】 模板：`Two authors iterated on the categories <k> times via open and axial coding, yielding <taxonomy> (Fig. X).`
- S7 `Artifact`：标注数据公开（脚注 3）。【脚】

**2.2-P2 段落角色：taxonomy 内容讲解（自顶向下）**
- S1 `Structure`：两个顶层类别：Structural 与 Content-Based。
- S2 `Number`：约 35% 为 Structural，65% 为 Content-Based。【数】
- S3 `Define class 1`：Structural 指不改变好响应标准的小重排，或对输出格式的规定（JSON/Markdown）。【例】
- S4 `Implication`：对应的断言检查输出是否符合指定结构。
- S5 `Define class 2`：Content-based 指任务含义的改变。
- S6 `Subtypes`：包括工作流步骤、包含或排除特定短语、定性指标。【例】
- S7 `Subtype 细化`：Data Integration 指向 prompt 加入新的上下文来源，例如新变量。【例】
- S8 `Pointer`：Table 1 对例子做了分类，Table 2 给每类示例。【回指 T1/T2】
- S9 `Impact（重复）`：taxonomy 对研究者和从业者都可能有用。

**2.2-P3 段落角色：从研究中提炼两条发现（为"可以自动化"背书）**
- S1 `Signpost`：建 taxonomy 得到两条关键发现。
- S2 `Finding 1`：不同 pipeline 的开发者迭代方式相似，很多节点可以用断言显式检查。
- S3 `Finding 2`：自动合成可行，因为不少 delta 能直接对应断言。
- S4 `Example`：例如大量 delta 是"包含/排除某短语"，对应检查是否出现该短语的断言。【例】 模板：`Overall, <study> reveals two findings. First, <regularity>. Second, <automation opportunity>, e.g., <instance>.`

**2.2-P4 段落角色：对管线中 LLM 子步骤的小型验证**
- S1 `Validation need`：要用 LLM 按 taxonomy 生成标准，先得验证 LLM 能否正确分类 delta。
- S2 `Result+数+日期`：对 19 个 pipeline 的全部 delta 人工标注真值，GPT-4（2023 年 10 月版）F1 = 0.8135。【数】 **给模型调用标注日期**，这是 LLM 论文的可复现性礼仪。
- S3 `Offload`：所用 prompt 见技术报告。【引 50】

#### 2.3 From Taxonomy to Assertions

**2.3-P1 段落角色：朴素方案 → 小实验否定 → 设计选择（附引用）**
- S1 `Recap`：分类后的 delta 常对应有意义的断言标准。
- S2 `Need`：接下来需要自动合成断言的方法。
- S3 `Naive`：自然的想法是让 LLM 按类别直接生成断言函数。
- S4 `Anecdotal negative+日期`：2024 年 1 月用 GPT-4 试过，发现漏掉了一些明显对应 taxonomy 类别的断言。（只是定性描述，没有给数字）
- S5 `Design choice+引`：因此采用两步 prompting，因为任务分解已被证明能提升 LLM 准确率。【引 20,59,61】 模板：`We therefore adopt <design>, as prior work shows <principle> improves <metric> [cites].`
- S6 `Steps`：第一步生成自然语言标准，第二步生成实现这些标准的 Python 函数。

**2.3-P2 段落角色：第一步细节 + 为什么逐 delta 分析**
- S1 `Technique`：对每个 ΔPi，让 LLM 尽可能多地提出标准，每条对齐一个 taxonomy 类别。（原文此处写 "from Figure 3"，但 taxonomy 在 Fig 2，**疑似交叉引用笔误**；Fig 3 在全文只出现这一次引用。）
- S2 `Loose definition`：标准被宽松地定义为作用于输出、求值为真或假的自然语言表达。【例：conciseness】
- S3 `Justification list`：逐 delta 而不是只看最终版的三个理由：开发者为省成本会删指令但仍期待同样行为【引 38】；prompt 有歧义；复杂 prompt 单看一版会漏。
- S4 `Conclusion`：所以逐 delta 分析能提高产出相关断言的可能性。

**2.3-P3 段落角色：第二步细节 + 输出对象命名**
- S1 `Technique`：汇总每个 delta 的标准后，再次 prompt LLM 生成 Python 函数。
- S2 `Capability`：函数可以调用外部库，或向 LLM 提二元问题。
- S3 `Design rule`：标准模糊时，允许生成多个函数分别实现。
- S4 `Example`：conciseness 可以对应三种函数：句数上限、词数上限、LLM 判断。【例】
- S5 `Output notation`：得到候选函数的多重集 F = {f1..fm}（为 §3 准备符号）。
- S6 `Offload`：两个 prompt 见技术报告。【引 50】

#### 2.4 Initial Deployment（**部署证据被隔离在方法章节里的独立小节**，标题用 "Initial"，自我降调）

**2.4-P1 段落角色：部署形态**
- S1 `Deployment+日期`：2023 年 11 月，作者通过 Streamlit 应用发布了候选生成的早期原型（脚注 4）。【脚】
- S2 `Usage flow`：开发者可以粘贴模板，或指向 LangChain Hub 上带提交历史的模板。
- S3 `UI`：应用会可视化识别出的类别并展示候选断言（Fig 4 截图）。【前指 Fig4】

**2.4-P2 "Tool Usage Insights and Feedback." 段落角色：使用量证据，每个数字都附口径或局限**
- S1 `Usage+数（口径）`：对自定义模板的运行超过 2000 次，并明确**排除了默认示例模板**。【数】 模板：`We observed over <N> runs on <custom inputs> (i.e., excluding <default>).`
- S2 `Diversity`：覆盖医疗、教育、烹饪、金融等领域。
- S3 `Figure+hedge`：Fig 5 是粗略分布；有些运行难以只归入一类（附例）。【回指 Fig5】
- S4 `Number+推断依据`：8% 是对话助手；从 prompt 中的公司名可以看出至少 4 家公司。【数】
- S5 `Engagement+数`：48 次运行点了下载按钮。【数】
- S6 `Measurement limitation`：用户也可能直接复制代码，作者没有统计复制事件。
- S7 `Hedged evidence`：没有人点踩，但作者明确说这不代表断言完美。 模板：`No user <negative signal>—which does not imply <perfection>.`
- S8 `Third-party evidence`：发现一位构建 PDF 问答工具的用户发布的自发好评（脚注 5）。【脚】
- S9 `Quote`：引用该用户的原话（保留原文拼写错误，显得真实）。
- S10 `Third-party evidence`：还发现一个独立的开源复现（脚注 6）。【脚】

**2.4-P3 "Observations about Assertion Criteria." 段落角色：部署中观察到的标准分布 + 失败案例 + 范围声明**
- S1 `Observation`：最常见的标准来自 inclusion 和 exclusion。
- S2 `Example`：购物助手要求包含客户提到的所有特征。【例】
- S3 `Example`：客服要求逐字引用上下文。【例】
- S4 `Failure observation`：聊天类任务常见"不要跑题"这类排除指令，GPT-4 难以为它生成标准。
- S5 `Failure detail`：为"避免无关内容"生成的函数没有调用 LLM。
- S6 `Failure detail`：而是做关键词匹配。
- S7 `Limitation+scope`：这说明当前 LLM 有局限，未来可能需要专门微调的模型；本文在现有 LLM 的能力范围内工作。 模板：`Such errors reflect limitations of current <models>, suggesting <future direction>; here we work within <present constraints>.`
- S8 `Offload`：详见技术报告。【引 50】

**2.4-P4 段落角色：部署后才出现的新模式（taxonomy 的扩展）**
- S1 `New pattern`：部署后发现开发者常希望在输出中隐藏工作流的某些部分。
- S2 `Map to taxonomy`：可以视为 exclusion 的特例。
- S3 `Example`：企业自动化 prompt 先要求写 SQL 查询某库。【例】
- S4 `Example`：另一条指令要求最终摘要里不能出现数据库名。
- S5 `Positive observation`：作者"惊喜地"发现系统准确识别并实现了这类排除。

**2.4-P5 "Observations about Assertions." 段落角色：为 §3 制造动机（模式 1：冗余）**
- S1 `Signpost`：版本多的 pipeline 有两种模式。
- S2 `Pattern 1`：prompt 工程会带来大量相似断言，部署时冗余难以管理。
- S3 `Example+数`：讲座摘要 pipeline（脚注 7）有 14 个版本，修改集中在同一段，导致断言重叠。【数】【脚】
- S4 `Evidence（代码）`：10 条断言都在检查"中心论点"，展示其中两条（代码清单）。【例】

**2.4-P6 段落角色：模式 2（不准确）→ 人工过滤不可行 → 引出 §3**
- S1 `Pattern 2`：很多断言不正确，会导致运行时错误或误报。
- S2 `Difficulty`：评估准确性难，尤其是调用 LLM 的断言，有经验的开发者也得看大量样例才能判断。
- S3 `Difficulty`：即使正确，与其他断言组合后的失败率和覆盖也难以推理。
- S4 `Number+前指`：几个版本就能产出 50+ 条断言（见 §4），人工对每个子集看失败率不现实。【数】【前指】
- S5 `Bridge`：因此采用自动过滤，见下一节。 模板：`Since <N>+ <artifacts> arise from <small input>, manually <task> is impractical; we therefore automate <step> (Section X).`

---

### §3 FILTERING CANDIDATE ASSERTIONS

**3-P0 段落角色：回顾 + 三重动机**
- S1 `Recap`：上一节显示候选冗余且有错，版本多时尤甚。【回指】
- S2 `Goal+triple motivation`：本节把候选集过滤成更小的集合，好处有三：提高效率、降低生产运行成本、减轻开发者认知负担。 模板：`Here we filter <set> to a smaller one, which improves <efficiency>, reduces <cost>, and lowers <human burden>.`

#### 3.1 Definitions

**3.1-P1 段落角色：基本对象与标签**
- S1 `Notation`：ei 表示 pipeline 在某输入上的一次端到端运行。
- S2 `Assumption`：本节假设 P 固定为开发者最终选定的版本。
- S3 `Label`：yi ∈ {0,1}，1 表示成功，0 表示失败。

**3.1-P2 段落角色：断言语义与目标的半形式化**
- S1 `Notation+延后`：E 是所有运行的集合，并不预先给定（马上处理）。
- S2 `Definition`：断言函数 f: E→{0,1}。
- S3 `Notation`：F′ 为 k 条断言的集合。
- S4 `Semantics`：ei 被 F′ 判为成功，当且仅当满足全部断言（合取语义）。
- S5 `Display`：ŷi 的分段式，行尾用 `//` 注释解释每一支（代码风格注释是本文公式的一个特色）。
- S6 `Objective（prose）`：从全部 m 条候选中选 F′，使大多数样例上 ŷ = y，且 F′ 尽可能小。
- S7 `Decomposition`：即最大化失败覆盖、最小化 FFR 和所选数量。
- Def 3.1 `Definition`：Coverage = 被 F′ 抓到的真实失败占全部真实失败的比例（公式加 `//` 注释）。
- Def 3.2 `Definition`：FFR = 真实成功中被 F′ 判为失败的比例。

**3.1-P3 段落角色：从理想定义退到可计算的样本版本**
- S1 `Symbol gloss`：解释 ŷi、yi、指示函数。
- S2 `Impracticality`：E 未知，所以 coverage 和 FFR 实际上无法计算。
- S3 `Assumption+前指`：先假设有带标签的子集 E′ ⊂ E，它可能不含所有失败类型，这个问题留到 3.3 处理。【前指】
- S4 `Notation`：之后用 E′ 上的版本代替，并省略下标。 模板：`In practice <ideal metric> is uncomputable since <universe> is unknown; we assume a labeled sample <E'> (which may miss <X>—addressed in §Y) and use <metric_{E'}>.`

#### 3.2 Coverage Problem Formulation

**3.2-P1 段落角色：抽象优化问题**
- S1 `Formal problem`：基于样本 E′ 选最小的 F′：min |F′|，约束 Coverage ≥ α、FFR ≤ τ（显示公式）。 模板：`Formally: minimize |<set>| subject to <metric1> ≥ α, <metric2> ≤ τ.`

**3.2-P2 段落角色：可行性说明 → 线性化 → 完整 ILP → 复杂度 → 规模论证**
- S1 `Caveat`：某些 α 下问题可能不可行。
- S2 `Example`：例如没有任何断言能抓住某个失败、而 α = 1。【例】
- S3 `Defer`：暂且忽略，留到 §4 讨论。【前指】
- S4 `Linearization`：引入 n×m 矩阵 M 记录每条断言在每个样例上的结果。
- S5 `Variables`：二元变量 xj（是否选中）和 wij（选中且判失败）。（注：此处正文写成 1 − Mij·xj，完整 ILP 中写成 (1 − Mij)·xj，后者才正确，3.3.1 的 ILP 又回到前一种写法。**符号前后不一致**，提醒我们自查。）
- S6 `Variable+constraint`：ui 表示失败样例是否被任一选中断言覆盖（不等式加 `//` 注释）。
- S7 `Constraint`：覆盖率约束。
- S8 `Variable`：zi 表示假失败。
- S9 `Constraint`：FFR 约束。
- S10 `Full ILP`：把最小化断言数写成完整 ILP（显示）。
- S11 `Naming`：解记为 spade_cov。
- S12 `Complexity`：τ = 0、α = 1 时可由 set cover 直接归约，"平凡地"是 NP-hard；又因为能写成 ILP，所以在 NP 中。**没有定理环境，一句话完成复杂度定位。** 模板：`Trivially, the problem is NP-hard for <special params> via a reduction from <classic problem>, and is in NP since <reason>.`
- S13 `Scale argument`：本文是几十条候选、少于 100 个样例，ILP 约数千变量。【数】
- S14 `Feasibility`：多数 ILP 求解器都能快速求解（原句缺动词，属于小语病）。

> **ILP 的动机链（全文统计）**：(i) Intro I-P8 先给朴素方案（逐条按阈值过滤）；(ii) 指出集合层面的 FFR 会累积，冗余也还在；(iii) 3.3.2 的 Eq.(1) 给出集合 FFR 的上下界（max ≤ FFR(S∪f) ≤ 和），从数学上说明逐条过滤为什么失效；(iv) 4.3 "FFR Tradeoffs" 用 fashion 和 lecturesummaries 的实测（每条都合格，合起来 FFR 达 88% 和 53%）在实验中坐实这一点。**动机→形式化→界→实证，四处呼应。**

#### 3.3 Subsumption Problem Formulation

**3.3-P1 段落角色：放宽假设 → 已考虑并否决的替代方案**
- S1 `Assumption recap`：前面假设开发者愿意提供全面的 E′。
- S2 `Failure of previous`：如果 E′ 不全，spade_cov 会漏掉只抓 E\E′ 中失败的断言（§4 有实证）。【前指】
- S3 `Alternative considered`：作者最初考虑过主动学习加弱监督。【引 6；40】
- S4 `Rejection reasons`：对前沿 LLM 来说成本高，而且要大量人工去平衡正负样本、保证 FFR 有意义。 模板：`We initially considered <alternative> [cite]; however, it is costly with <setting> and demands <manual effort>.`

**3.3-P2 段落角色：用真实例子直观引入新概念**
- S1 `Introduce concept`：为此引入 subsumption 概念。
- S2 `Real example`：代码评审 pipeline 中的 gratitude_v1/v2/v3，检查的感谢词逐级增多。【例（真实，非电影例子）】
- S3 `Conclusion`：v3 包含（subsumes）另外两个。

**3.3-P3 段落角色：目标与正式定义**
- S1 `Goal+assumption`：假设候选尽量覆盖失败模式，目标是选 F′ 使 F\F′ 都被 F′ 包含。
- S2 `Formal`：集合 S 包含 f，当且仅当 S 的合取蕴含 S∪{f} 的合取。
- Def 3.3 `Definition`：给出逐样例的量词形式，并附 "In other words"：f 抓不到 S 抓不到的新失败。 模板：`Definition. <S> ⟹ <f> iff <formal>. In other words, <plain-language consequence>.`

**3.3-P4 段落角色：第二个小例子，把概念连回 taxonomy**
- S1 `Example`：S 只有 f，f 解析 JSON 列表并检查至少 2 个元素。【例】
- S2 `Provenance`：f 可能来自 taxonomy 中计数类的 delta。
- S3 `Example`：g 只检查能否解析为 JSON 列表。
- S4 `Provenance`：g 可能来自 Response Format Instruction 类 delta。
- S5 `Conclusion`：g 失败则 f 必然失败，所以 S ⟹ g。

##### 3.3.1 ILP with Subsumption Constraints

**3.3.1-P1 段落角色：改写目标**
- S1 `Reformulate`：在原问题上加入 subsumption。
- S2 `Notation+objective`：G 为未被 F′ 包含的落选函数集合；目标 min |F′| + |G|，约束不变（显示）。

**3.3.1-P2 段落角色：引入 K 与 r**
- S1 `Variables`：引入矩阵 K 表示包含关系，Kij = 1 当且仅当 fi ⟹ fj。
- S2 `Forward-ref`：K 的构造见 3.3.2。【前指】
- S3 `Recall`：回顾 xj 的含义。
- S4 `Variable+display`：rj 表示 fj 是否被 F′ 包含（上下界约束）。

**3.3-P3（3.3.1 内）段落角色：逐条解释三个约束（教学式线性化）**
- S1 `Variable`：sj 表示 fj 既没被选中也没被包含；分三部分写。
- S2–S3 `Constraint 1 + gloss`：sj ≤ 1 − xj，并解释含义。
- S4–S5 `Constraint 2 + gloss`：sj ≤ 1 − rj，并解释 rj = 0 时 sj 可以为 1。
- S6–S7 `Constraint 3 + gloss`：sj ≥ 1 − xj − rj，确保只有两个条件都成立时 sj 才为 1。 模板：`<var> denotes <condition>. We break this into three parts. First, <c1>, indicating <meaning>. Second, <c2>, capturing <meaning>. Lastly, <c3>, which ensures <meaning>.`

**3.3.1-P4 段落角色：完整 ILP（改动处标蓝）→ 命名 → 为何保留覆盖约束**
- S1 `Full ILP`：目标是 Σxj + Σsj，完整 ILP 中相对 spade_cov 的改动**用蓝色高亮**。 可复用的版面技巧：第二个 ILP 只用颜色标出增量。
- S2 `Naming`：解记为 spade_sub。
- S3 `Design justification`：保留覆盖约束，因为单靠 subsumption 不反映失败的分布与重要性。
- S4 `Example`：如果某类失败在 E′ 中占关键比例，只看 subsumption 可能忽略它。
- S5 `Edge case`：α = 1 时，只优化 |F′| + |G| 不能保证覆盖全部失败。
- S6 `Forward-ref`：实践中 spade_sub 对 α 不如 spade_cov 敏感（§4）。【前指】

##### 3.3.2 Assessing Subsumption

**3.3.2-P1 段落角色：如何得到 K（工程实现）**
- S1 `Goal`：说明如何构造 K。
- S2 `Option`：纯 Python 函数可以用静态分析。
- S3 `Complication`：涉及 LLM 调用或混合时就复杂了。
- S4 `Choice`：因此 spade 用 GPT-4 识别成对的包含关系。
- S5 `Cost+数`：每个 pipeline 只需两次 LLM 调用：先把所有断言放进一个 prompt 列举关系，再转成可解析的列表。【数】 模板：`For any <unit>, only <k> LLM calls are needed: first <step1>, then <step2>.`

**3.3.2-P2 段落角色：提高精确率的三条剪枝启发式**
- S1 `Signpost`：为最大化精确率采用若干启发式。
- S2 `Heuristic 1（E′ 过滤）`：若某样例上 fi 通过而 fj 失败，则含 fi 的集合不包含 fj（显示）。
- S3 `Gloss`：换句话说，fj 抓到了 fi 没抓到的失败。
- S4 `Heuristic 2（FFR 界）`：利用 FFR 阈值跳过评估；给出 Eq.(1)：集合 FFR 介于各项最大值与各项之和之间。
- S5 `Consequence`：任一方单独的 FFR ≥ τ 时就不必评估。
- S6 `Heuristic 3（传递性）`：利用蕴含的传递性继续剪枝（跨页到 p9）。

**Fig 6（p9 左栏顶）**：subsumption DAG 示例，图注 73 词，自成一段完整解释（a 包含 b/c/d 的 gratitude 层级，e 是 LLM 检查、包含关键词检查 f）。

##### 3.3.3 Subsumption without Examples

**3.3.3-P1 段落角色：完备性补充（零样例情形）**
- S1 `Scope`：为完整起见，考虑完全没有样例 E′ 的情况。
- S2 `Consequence`：此时只能依靠 subsumption 关系。
- S3 `Formal`：给出去掉覆盖和 FFR 约束后的 ILP（显示）。

**3.3.3-P2 段落角色：复杂度反转 + 用 Fig 6 直观演示**
- S1 `Claim`：这个问题不再是 NP-hard。
- S2 `Figure`：看 Fig 6，边表示包含。【回指 Fig6】
- S3 `Edge semantics`：a→b 表示 b 抓到的失败是 a 的子集。
- S4 `Concrete`：a 检查一组感谢关键词，b 检查其中一部分。【例】
- S5 `Worked solution+数`：最小化时只选 a 和 e，其余都被包含，目标值为 2。
- S6 `Intuition`：直观过程：起初全不选，按序加入，同时把被新包含的函数的 s 置 0。

**3.3.3-P3 段落角色：一般化 → 算法 → 复杂度**
- S1 `Generalize`：包含关系一般构成 DAG。
- S2 `Edge case（括号）`：只有函数等价时才有环，这种平凡情形略去。
- S3 `Algorithm`：选所有入度为 0 的节点加入 F′。
- S4 `Correctness`：其余节点至少有一条入边，所以都被包含。
- S5 `Optimality gloss`：入度为 0 的节点也可以不选，但选了不会让目标变差，因为它不可能被其他节点包含。
- S6 `Algorithm summary`：所以只需对包含图做拓扑排序，取"顶部"节点。
- S7 `Complexity`：无样例时问题属于 PTIME。 模板：`More generally, <relation> forms a DAG; selecting all source nodes suffices, so the problem is in PTIME when <condition>.`

---

### §4 EVALUATION（只评估组件 2（过滤）；组件 1（生成）的证据来自 2.4 的部署观察和 2.2 的 F1 检验）

**4-P0 段落角色：路标 + artifact**
- S1 `Roadmap`：先讲 pipeline 和数据集，再讲方法、指标和结果。
- S2 `Artifact`：代码、数据集、LLM 响应都放在 GitHub。

#### 4.1 Pipeline and Dataset Descriptions

**4.1-P1 段落角色：工作负载来源与选取理由**
- S1 `Data+数`：9 个 pipeline：8 个来自 LangChain Hub（脚注 8），1 个是专有的。【数】【脚】
- S2 `Composition`：每个 pipeline 有一个模板和约 75 个带好坏标签的样例。【数】
- S3 `Provenance`：全部来自 LangChain 用户。
- S4 `Provenance（潜在风险）`：其中 6 个参与过 taxonomy 构建（2.2），各属不同领域。【回指】 **评估集与开发集有重叠，原文没有当作威胁讨论。**
- S5 `Provenance`：2 个来自 Streamlit 部署（2.4）。【回指】
- S6 `Selection rationale+deployment`：纳入专有的 fashion pipeline，因为它版本最多，且 spade 的断言已在生产中每天运行数万次。【数】 **部署证据出现在实验设置里，但只用来说明"为何选它"，不作为结果。**

**4.1-P2 段落角色：样例与标签怎么来（数据构造透明度）**
- S1 `Pointer`：Table 3 给出详情。【回指 T3】
- S2 `Labels`：fashion 的好坏样例由该初创公司的开发者提供。
- S3 `Construction`：其余 8 个用真实模板和历史（3–16 个版本），但输入输出样例由作者构造并标注，以便公开。（注：这 8 个中最多的是 14 个版本，16 属于 fashion，**数字有小出入**。）
- S4 `Source`：2 个 pipeline 的样例来自 Kaggle。
- S5 `Source`：其余 6 个用 ChatGPT Pro（GPT-4）合成，并经人工审核。
- S6 `Example`：例如让 ChatGPT 生成覆盖多种语言、应用类型和 diff 大小的 PR。【例】
- S7 `Number`：平均每个 pipeline 75 个样例。【数】
- S8 `Labeling`：在这些输入上运行 pipeline，再人工标注响应是否满足 prompt 指令。

#### 4.2 Method Comparison and Metrics

**4.2-P1 段落角色：实验约定与实现**
- S1 `Recap notation`：E′ 和标签。
- S2 `Notation`：τ 和 F（来自 §2 第一步）。【回指】
- S3 `Convention`：候选函数运行出错时记为失败。 **这是很容易漏写的实验约定，本文写明了。**
- S4 `Implementation`：Python + PuLP。
- S5 `Solver`：用 PuLP 默认的 CBC 求解器。【引 17】

**4.2-P2 段落角色：基线设计（先排除平凡基线，再定义真正的基线）**
- S1 `Trivial baseline dismissed+数`：最简单的做法是全选，但只要有一条断言全挂，就是 100% 覆盖、100% FFR。【数】
- S2 `Explanation`：失败来自运行错误或过于具体、从未匹配过真实输出的条件。
- S3 `Choice`：因此拿两个 spade 版本对比一个基线：逐条剔除单条 FFR 超过阈值的断言。
- S4 `Formal baseline`：基线 = {f ∈ F : FFR({f}) ≤ τ}。
- S5 `Methods`：spade_cov 对应 3.2 节的 ILP，spade_sub 对应 3.3.1 节的 ILP。【回指】 模板：`The simplest baseline—<trivial>—yields <degenerate result>; we instead compare against <reasonable baseline> that <rule>.`

**4.2-P3 段落角色：指标列表（编号列表，每项指回定义）**
- (1) 所选比例 |F′|/|F|；(2) 落选且未被包含的比例 |G|/|F|；(3) FFR（Def 3.2）；(4) E′ 上的覆盖（Def 3.1）。【回指 Def】

**4.2-P4 段落角色：子组件指标（只测 precision）的理由**
- S1 `Importance`：spade_sub 的效果取决于 subsumption 判定的质量。
- S2 `Metric choice`：没有真值，所以只测精确率（LLM 给出的包含对中正确的比例）。
- S3 `Declared non-measurement`：不评召回率，因为每个 pipeline 可能要标注数万对，不现实。【数】
- S4 `Justification`：精确率比召回更关键，只要识别出一部分包含关系，就能选出更少的断言。 模板：`We do not assess <metric> due to <impracticality>; moreover, <other metric> matters more because <reason>.`

#### 4.3 Results and Discussion

**4.3-P1 段落角色：先证明组件可用（precision、运行时间），再进入主结果**
- S1 `Signpost`：先讨论各组件是否实用。
- S2 `Result+数`：GPT-4 判定 subsumption 的平均精确率 0.82（Table 5），作者据此称"有效"。【数】【回指 T5】
- S3 `Result+数`：ILP 运行时间全都低于 1 秒，唯一例外是 fashion 上的 spade_sub，1.197 秒（Table 6）。【数】 **主动点出最大值。**
- S4 `Claim`：运行时间小，说明方法可行。
- S5 `Transition`：后文聚焦各方法选出的断言。

**4.3-P2 段落角色：主结果（固定参数 → 举一个 pipeline → 汇总胜负 → 头条数字）**
- S1 `Setting`：为简单起见，所有 pipeline 用相同阈值（α = 0.6，τ = 0.25）；结果见 Table 4。【数】【回指 T4】
- S2 `Walk-through`：以 codereviews 为例。
- S3 `Numbers`：基线选 20 条，spade_cov 选 2 条，spade_sub 选 15 条。【数】
- S4 `Explanation`：spade_sub 多选，是为了保证所有未被包含的函数都在集合里。
- S5 `Win count`：三者都满足覆盖约束，但基线在 9 个中有 4 个违反 FFR。【数】 模板：`All methods satisfy <c1>, but <baseline> violates <c2> in <k> of <N> <workloads>.`
- S6 `Headline`：spade_sub 比基线少选约 14% 的断言，FFR 低约 21%（原文用了 "significantly"，但没有统计检验）。【数】
- S7 `Number`：spade_cov 平均排除了约 44% 未被包含的函数。【数】
- S8 `Guidance`：选哪种实现主要取决于有多少标注数据。
- S9 `Transition`：接下来讨论取舍。

**4.3-P3 "Subsumption vs. E′ Coverage." 段落角色：两变体的互补关系与适用条件**
- S1 `Claim`：两者互补，E′ 越全面，spade_cov 越有用。
- S2 `Evidence+数`：本文的 E′ 不全面：spade_cov 落选的函数中平均 44% 未被包含，尽管它们满足 FFR。【回指 T4】
- S3 `Explanation+数`：这并不意外，平均每个任务只有约 34 个坏样例（按 Table 3 计算为 35.1，**有小出入**）。
- S4 `Applicability`：大型或成熟组织数据多，可用 spade_cov；数据稀缺时 spade_sub 更有利。
- S5 `Evidence（代码）`：展示 codereviews 中被 spade_cov 忽略、被 spade_sub 选中的 3 条断言。【例】

**4.3-P4 "Subsumption as a Means for Reducing Redundancy." 段落角色：机制解释（为什么 sub 能去冗余）**
- S1 `Observation`：候选冗余多时，基线与 spade_sub 选中的数量差距大。
- S2 `Example+数+代码`：codereviews 的 8 个版本里，开发者反复修改"简洁清晰"这条指令，产生 5 条做同一件事的断言（展示 3 条）。【例】

**4.3-P5 段落角色：赢的机制 + 主动承认的失败**
- S1 `Mechanism`：5 条都单独满足 FFR，基线会全选；只要 subsumption 判定正确，spade_sub 只选与 FFR 最兼容的那一条。
- S2 `Honest loss`：反过来，LLM 可能没有召回所有包含关系，spade_sub 仍会留下重复。
- S3 `Evidence`：例如 codereviews 中同时保留了 code_improvement 的 v1 和 v2。【例】 模板：`On the flip side, <component> may miss <relations>, so <method> may retain <defect>, e.g., <instance>.`

**4.3-P6 "α and τ Threshold Sensitivity." 段落角色：参数敏感性（定性，没有扫参）**
- S1 `Dependence`：ILP 能否求出可行解取决于 α 和 τ。
- S2 `Practical guidance`：如果不可行，开发者可以用二分法调整阈值。
- S3 `Result`：本文 9 个 pipeline 在选定阈值下都可行。【数】
- S4 `Sensitivity claim`：E′ 小，使 spade_cov 对 α 特别敏感。
- S5 `Number`：1 到 5 条断言就能覆盖 60% 的失败。【数】
- S6 `Example（代码）`：emails pipeline 中 spade_cov 只选了 1 条（"鼓励联系公司"的短语匹配）。【例】

**4.3-P7 段落角色：sensitivity 的结论**
- S1 `Conditional`：如果 E′ 穷尽且有代表性，spade_cov 可能就够了（以 emails 为例：多数失败确实是缺少联系鼓励）。
- S2 `Evidence`：但本文的 E′ 显然不穷尽，因为 spade_sub 总是多选。
- S3 `Mechanism`：spade_sub 对 α 不敏感，因为它按"能否覆盖新失败且不超 FFR"来选，即使覆盖约束不再紧。

**4.3-P8 "FFR Tradeoffs." 段落角色：预先回应审稿人的"复杂度值不值"质疑**
- S1 `Anticipated objection+数`：有 3 个 pipeline 上基线和 spade_sub 的所选比例差不到 10%，读者可能会问复杂度是否值得。 模板：`Given that <difference> is under <x> for <k> <workloads>, one may wonder whether <complexity> is worth it.`
- S2 `Answer`：spade_sub 通常更好，因为基线无法稳定满足 τ。
- S3 `Trend`：版本越多，断言越多，对基线越不利。
- S4 `Theory link`：集合 FFR 的最坏情况是各条 FFR 之和（Eq.(1)）。【回指 Eq1】
- S5 `Consequence`：独立断言很多时，总 FFR 很可能超过阈值。
- S6 `Evidence+数`：fashion 和 lecturesummaries 中，67 条和 32 条断言各自都合格，但基线的总 FFR 达 88% 和 53%。【数】
- S7 `Deployment scenario`：如果 spade 部署在能实时观察每次 LLM 调用的交互系统里（例如包在 API 外层），版本增多会让按总 FFR 过滤更加必要。
- S8 `Conclusion`：这说明需要更复杂的 cov/sub 方法。

---

### §5 RELATED WORK（~480 词，56 个引用键 / 51 个不同文献；4 个按主题组织的 run-in 段落；放在实验之后）

**5-P0**：S1 `Roadmap`：综述四个方向：prompt 工程、ML/LLM 评估、LLM 用于软件测试、ML pipeline 测试。

**5-P1 "Prompt Engineering."**
- S1 `Difficulty+引`：非技术和技术用户都觉得 prompt 工程难，措辞和顺序的小改动就会显著影响输出。【引 63；37,52；3,30；32】
- S2 `Drift`：API 背后的模型会变（prompt drift），输出可能在开发者不知情时改变。【引 9】
- S3 `Tools`：辅助 prompt 管理和实验的工具在涌现，有的甚至用 LLM 写 prompt。【引 2,11,60,61,65】
- S4 `Deployment challenges`：已部署的 prompt 带来新挑战。【引 38】
- S5 `Positioning（正交）`：本文不直接帮助写更好的 prompt，但可以通过发现错误间接帮助。 模板：`Our work does not directly <their goal>, but could indirectly support <users> by <our function>.`

**5-P2 "ML and LLM Evaluation."（最接近的工作在本段末尾）**
- S1 `Background`：评估和监控已部署的 ML 本来就难。【引 36,49】
- S2 `Escalation`：LLM 更难，因为输出是自由文本。【引 12】
- S3 `Contrast`：RAG 类任务有标准化指标，其他任务缺指标、缺标注。【引 29；13,43；8,38,62】
- S4 `Practice`：通常靠人工评估，近期研究表明 LLM 用评分卡也能自评。【引 18,38,58；7,26,64】
- S5 `Gap`：但评分卡难写，这促成了自动生成评估器的需求。【引 38】
- S6 `Closest work+gap`：近期研究和工业工具提出用断言抓 LLM 错误，但要用户自己挑选断言。【引 26,41,54；21,27,31】 模板：`Recent work [cites] and tools [cites] propose <mechanism>, while requiring the user to <manual step>.`（定位隐含在这里：本文自动完成这一步）

**5-P3 "LLMs for Software Testing."**
- S1 `Background`：LLM 被用来生成单元测试和测试用例。【引 28,44,53,55,56】
- S2 `Background`：有研究考察 prompting、幻觉、非确定性对代码和测试准确性的影响。【引 10,14,15,35】
- S3 `Positioning（互补）`：本文与之互补，用 LLM 为 LLM pipeline 生成代码形式的断言。

**5-P4 "Testing and Validation in ML Pipelines."（DB 引用集中在这里）**
- S1 `Background`：ML pipeline 在生产中难管理。
- S2 `DB lineage`：ML 测试文献多面向结构化数据，做数据质量校验或溯源。【引 5,22,46,47；33,45】
- S3 `Platforms`：平台提供实验追踪、防过拟合、数据分布调试。【引 1,42；19】
- S4 `Model assertions`：模型断言要么需要人工规格，要么需要大量数据训练"学习型断言"。【引 25；24】
- S5 `Positioning`：LLM pipeline 是新一类 ML pipeline，LLM 本身可以用很少的数据生成断言。
- S6 `Motivation for filtering`：近期研究指出开发者不愿运行上百条断言，这又一次为过滤提供了动机。【引 38】

> RW 的组织方式：按主题分四段；每段 2–6 句；**每段以一句"我们与之关系"收尾**（正交/补足 gap/互补/新类别+动机）。不设比较表。最接近的工作（[26][41][54] 及工具 [21][27][31]）在 Intro 和 RW 中各出现一次，措辞一致：它们需要人工提供或挑选断言。

**一句话定位（本文对最接近工作）**：已有 LLM pipeline 断言机制（EvalLM、NeMo Guardrails、DSPy Assertions 及 Guardrails/LangChain/LlamaIndex）只负责执行用户写好或挑好的断言，spade 则从 prompt 版本历史中**自动合成**候选断言，并**在集合层面最优地选出**满足覆盖和误报约束的最小子集；而 DB 社区的 ML 数据校验（Deequ、TFDV 等）面向批量结构化记录，无法直接用于非结构化的逐条 LLM 输出。

---

### §6 CONCLUSION AND FUTURE WORK（~315 词，2 段，无引用）

**6-P1 段落角色：按贡献顺序复述（9 句）**
- S1 `Problem+system`：本文提出自动生成断言以捕获 LLM pipeline 失败这一**新问题**，以及 spade。（"new problem" 在全文首次明确出现在结论里）
- S2 `Architecture`：两个组件：先合成，再过滤。
- S3 `Insight`：分析版本历史后发现 prompt delta 是需求的丰富来源。
- S4 `Taxonomy+deployment+数`：建立 taxonomy，并通过与 LangChain 集成和 2000+ 次运行展示其价值。
- S5 `Formulation`：把最优断言选择表达为 ILP。
- S6 `Subsumption`：提出 subsumption 处理数据稀缺。
- S7 `No-example case`：零样例时化为包含图上的拓扑排序。
- S8 `Evaluation`：在 9 个真实 pipeline 上评估。（结论中**没有重复 14%/21%**）
- S9 `Artifact`：代码和数据公开。

**6-P2 段落角色：未来工作（4 个方向，均从本文局限自然延伸）**
- S1 `Signpost`：仍有若干开放问题。
- S2 `FW1`：开发者希望自己权衡，而不只是给定 (α, τ)，因此需要人在回路的界面。
- S3 `FW2`：这样的界面也可以让开发者随手标注样例。
- S4 `FW3`：选择哪些样例来标注最有帮助是开放问题，类似主动学习（呼应 3.3 中被否决的替代方案）。
- S5 `FW4`：随着新失败模式出现，自动更新已部署的断言集合。

---

### 4.X 横切观察（Section 4 要求的专项）

**(a) Running example**
- 主例：电影推荐（合成例子）。出现在 Intro I-P3（引入）、I-P4（delta→断言）、I-P9（200 词断言被误删）、2.1（P7 全文）、Table 1（7 个版本的 ΔP 和类别）、Table 2（各类示例 delta 都用电影情境）、Fig 3（以 ΔP5 为例走完生成流程）。
- 副例：codereviews（真实 pipeline）。在 3.3 中以 gratitude 层级引入 subsumption；Fig 6 复用；4.3 中三次用于展示结果（选数对比、被 cov 忽略的断言、冗余的简洁性断言、重复的 v1/v2）。
- 设计要点：**方法部分用一个可控的玩具例子讲清楚，形式化和实验部分换成真实例子增加可信度**；电影例子不在 9 个评估 pipeline 中，避免了"例子即测试集"的嫌疑。

**(b) 问题形式化**
- 标签：yi ∈ {0,1}（1 = 成功）；断言 f: E→{0,1}；集合语义为合取（ŷi = 1 当且仅当全部断言通过）。
- 指标：Coverage（真实失败中被抓到的比例），FFR（真实成功中被误判为失败的比例）。先在全集 E 上定义，再明确退到样本 E′。
- 目标/约束：P_cov 为 min |F′|，约束 Cov ≥ α、FFR ≤ τ；P_sub 为 min |F′| + |G|，约束相同；P_0 为零样例时只保留 subsumption 约束。
- 层级：自然语言目标（Intro I-P6）→ 抽象优化问题（3.2 前半）→ 变量与约束逐个引入、每条附注释或解释 → 完整 ILP → 命名解（spade_cov/spade_sub）→ 复杂度一句话。
- 版面技巧：`//` 行尾注释写在公式里；第二个 ILP 只用蓝色标增量。

**(c) ILP 的动机与陈述** —— 见 3.2 后的"动机链"框：朴素逐条过滤 → 集合 FFR 累积和冗余 → NP-hard（set cover 归约）→ 实际规模小，ILP 可行 → Eq.(1) 的界 → 实测运行时间 ≤ 1.2 s，以及基线 FFR 达 88%/53% 的反例。

**(d) 部署/使用证据与受控评估的分离**
- 部署证据放在 **§2.4 "Initial Deployment"**（方法章节内的独立小节），只支撑组件 1（生成），用 "insights / observations" 措辞，每个数字都配口径（排除默认模板、没统计复制事件、没人点踩不等于完美）。
- 受控评估放在 **§4**，只评估组件 2（过滤），有固定的数据集、基线、阈值和指标表格。
- 两者的交界只有两处：4.1 说明 fashion pipeline 已在生产中每天运行数万次（作为选取理由）；4.3-P8 设想把 spade 包在 API 外层的交互部署（作为论证情景）。
- Abstract 和 Intro 都把部署数字放在受控结果之后或单列；Intro 中唯一的加粗句就是部署证据。
- 缺口（需要注意，不要模仿）：组件 1 **没有受控评估**（与"直接让 LLM 写断言"的对比只有 2.3 中一句定性描述），2.2 的 F1 = 0.8135 只验证了分类子步骤。

---

## 5. 图表清单

| ID | 页 | 内容 | 宽度 | 图注词数 | 图注是否给出结论 | 首次引用位置 vs 放置 |
|---|---|---|---|---|---|---|
| Fig 1 | p1 右栏顶 | 系统流程：开发者→prompt 版本→①生成候选→②用带标签 I/O 过滤→要部署的断言 | 单栏 | 45 | 部分：描述两步做了什么（"过滤冗余与不准确断言、同时保持覆盖"），属于功能型结论 | 首引 p2（I-P6）；**放置先于引用**（teaser） |
| Fig 2 | p3 左栏顶 | prompt delta taxonomy 树（2 个顶层、10 个叶类） | 单栏 | 8 | 否（只标来源"19 个 pipeline"） | 首引 p2（I-P4），放在下一页 |
| Table 1 | p4 顶 | 电影例子 7 个版本的 ΔP、类别、可能的断言标准 | **跨栏** | ~55 | 否（说明 +/− 记号与列含义） | 首引 p3（2.1），放在下一页 |
| Table 2 | p4 右栏 | 各类别的解释和示例 delta | 单栏 | 4 | 否 | 首引 p3（2.2-P2 末），放在下一页 |
| Fig 3 | p5 左栏顶 | 从 ΔP5 到标准 JSON，再到合成的 2 个 Python 函数 | 单栏 | 8 | 否 | 唯一一次引用在 p4（2.3-P2，且疑似把 Fig 2 误写为 Fig 3），放在下一页 |
| Fig 4 | p6 左栏顶 | Streamlit 工具截图 | 单栏 | 7 | 否 | 首引 p5（2.4-P1），放在下一页 |
| Fig 5 | p6 右栏顶 | 提交 prompt 的领域分布横向条形图（Health 20.8% 最高） | 单栏 | 14 | **是**（"覆盖多种领域"） | 首引 p5（2.4-P2），放在下一页 |
| Fig 6 | p9 左栏顶 | subsumption DAG（a→b,c,d；e→f） | 单栏 | 73 | 是（图注完整解释了每个节点和包含关系，可以脱离正文阅读） | 首引 p9（3.3.3-P2），同页 |
| Table 3 | p10 顶 | 9 个 pipeline 的好/坏样例数、版本数、任务、prompt 链接 | **跨栏** | ~50 | 部分（交代数据来源：startup / 合成 / Kaggle） | 首引 p9（4.1-P2），放在下一页 |
| Table 4 | p10 左栏 | 主结果：3 种方法 × 9 个 pipeline 的 FFR、Coverage、所选比例、未包含比例，✓/✗ 表示约束是否满足 | 单栏 | 74 | **是**（图注最后两句给结论：cov 选得最少；sub 在优化包含的同时选得最少） | 首引 p11（4.3-P2）；**放置先于引用** |
| Table 5 | p10 右栏（半栏，与 T6 并排） | 各 pipeline 的 subsumption 判定精确率（0.68–0.90） | 半栏 | ~10 | 否（但注明"两位作者核验"） | 首引 p11（4.3-P1），放在前一页 |
| Table 6 | p10 右栏（半栏） | 10 次试验的平均 ILP 运行时间 | 半栏 | ~22 | 否（注明基线没有 ILP） | 首引 p11，放在前一页 |

**模式**
- 6 图 6 表，其中只有 2 个跨栏元素（T1 例子表、T3 数据集表），都放在页顶。
- 图注长度两极分化：解释性图注长（Fig 1、Fig 6、T1、T3、T4 在 45–75 词），标签式图注极短（4–14 词）。**只有 T4、Fig 5、Fig 6 的图注带结论。**
- 结果表（T4/T5/T6）集中在一页（p10），讨论在 p11。读者翻一页就能对照。
- 没有任何折线图或柱状图形式的实验结果，全部实验结果都用表格呈现。唯一的统计图（Fig 5）属于部署证据。
- 代码清单承担了"定性证据"的角色（2.4 和 4.3 共 4 块），这是 LLM 系统论文特有的证据形式。

---

## 6. 实验设计

**6.1 RQ/主张（原文没有显式列出 RQ，以下按段落归纳）**
- C1（4.3-P1）组件可行：subsumption 判定够准（precision），ILP 够快（runtime）。
- C2（4.3-P2）主结果：spade_sub 和 spade_cov 在满足约束的前提下比基线选得更少、FFR 更低。
- C3（4.3-P3）cov 与 sub 互补；数据稀缺时 sub 能保留未被覆盖的断言。
- C4（4.3-P4/P5）subsumption 能去冗余（附失败案例）。
- C5（4.3-P6/P7）阈值敏感性：cov 对 α 敏感，sub 不敏感（定性）。
- C6（4.3-P8）为什么需要集合层面的 FFR：基线的总 FFR 会失控。
- 主张数与讨论段一一对应；**用加粗的 run-in 标题把讨论组织成"发现"**，而不是按 RQ 编号。

**6.2 数据集**
- 9 个 pipeline：8 个来自 LangChain Hub（公开）+ 1 个专有（fashion，生产中）。其中 6 个参与过 taxonomy 构建，2 个来自 Streamlit 部署。
- 每个约 75 个样例（好 19–60，坏 16–56；坏样例平均约 35）；版本数 3–16。
- 样例来源：fashion 由公司提供并标注；2 个取自 Kaggle；6 个由 GPT-4 合成后人工审核；标签由作者手工给出。
- 评估的是组件 2，所以候选集 F 由组件 1 生成（每个 pipeline 15–106 条候选）。

**6.3 基线**
- 数量：1 个真正的基线 + 1 个在正文中排除的平凡基线（全选，导致 100%/100%）。
- 选取理由：代表"不考虑断言间交互"的朴素做法（逐条 FFR 过滤），正好是 Intro I-P8 中先抛出、再否定的朴素方案。**基线 = Intro 里的稻草人，形成闭环。**
- 公平性：三种方法共用同一候选集 F、同一 E′、同一阈值；基线不含 ILP（T6 注明）。
- 缺失：没有和外部系统比较（EvalLM、DSPy Assertions 等需要人工挑选，不可直接对比，原文没有讨论这一点）；组件 1 没有对照基线；没有消融（例如去掉启发式剪枝）。

**6.4 指标**
- 主指标 4 个（所选比例、未包含比例、FFR、E′ 覆盖），各自指回定义；子组件指标 2 个（precision、runtime）。
- 明确声明不测 recall，并给出理由。

**6.5 胜/平/负的报告方式**
- 用 ✓/✗ 在表内标出约束满足情况；正文给出"基线在 4/9 违反 FFR"这样的计数。
- 平局：emails、statsbot、threads 三者 FFR 都是 0；sportroutine 基线与 cov 的 FFR 相同。正文只用"有 3 个 pipeline 差距 < 10%"一句集中回应。
- 负面结果：cov 的覆盖明显低于基线（0.6–0.94 vs ~1），原文把它表述为"互补"而不是"输"；sub 会留下重复（v1/v2），原文主动承认。
- 头条数字是均值的百分点差，但用 "%" 表达（见 §3 摘要观察 3）。

**6.6 统计处理**
- 只有运行时间取了 10 次平均；没有方差、置信区间或显著性检验；LLM 生成环节（候选、subsumption）只跑一次，非确定性没有讨论；"significantly lower FFR" 没有统计支撑。
- 阈值固定为 α = 0.6、τ = 0.25，没有扫参曲线；敏感性只做定性讨论。

**6.7 Threats / 局限的写法**
- 没有独立的 Threats to Validity 小节。局限分散在：2.4（复制事件没统计、没人点踩不等于完美、GPT-4 生成排除类断言的失败）、4.2（不测 recall）、4.3（重复断言、E′ 不全、阈值可能不可行）、6-P2（未来工作）。
- 未讨论的威胁（自审时可对照）：评估集与 taxonomy 开发集重叠（6/9）；合成样例和作者标注可能引入偏差；单一 LLM（GPT-4）；样本量小（约 75）。

---

## 7. 引用用法

**7.1 各节引用密度**

| 节 | 引用括号数 | 引用键数 | 约字数 | 键/千词 |
|---|---|---|---|---|
| Abstract | 0 | 0 | 188 | 0 |
| 1 Intro | 12 | 23 | ~1,450 | ~16 |
| 2（2.1–2.4） | 6 | 8（其中 [50] 出现 4 次） | ~2,500 | ~3 |
| 3 | 2 | 2 | ~2,650 | ~0.8 |
| 4 | 1 | 1（CBC 求解器） | ~1,800 | ~0.6 |
| 5 RW | 26 | 56（51 个不同文献） | ~480 | **~117** |
| 6 Conclusion | 0 | 0 | ~315 | 0 |

- 模式：引用高度集中在 Intro 和 RW（合计约 79 个键，占全部引用键约 87%）；方法和实验几乎不引用，靠自己的定义、例子和数据说话。
- 方法章节中的引用只承担三种功能：(i) 设计选择的依据（两步 prompting [20,59,61]）；(ii) 被否决的替代方案（主动学习 [6]、弱监督 [40]）；(iii) 细节卸载到技术报告 [50]。
- Intro 中的引用以"成组"为主（平均每个括号约 2 篇），多用在问题陈述和 gap 句上。

**7.2 RW 组织**：放在实验之后、结论之前；4 个主题段，各有 run-in 粗体标题；段内按"背景→难点→已有方案→与本文关系"推进；不设比较表；最接近的工作放在第二段末，DB 渊源放在最后一段。

**7.3 一句话定位**（同 §4 RW 末尾）：已有工作只"执行用户给定的断言"，spade "从 prompt 历史合成断言并做集合级最优挑选"；DB 的数据校验面向结构化批量数据，不能直接迁移。

---

## 8. 可复用规则（22 条，可检查）

| # | 规则 | 检查方法 | 证据位置 |
|---|---|---|---|
| R1 | 标题用 `<system>: <动名词> <DB 熟悉的产物> for <新负载>`，产物名挂靠 DB 老概念 | 标题中是否有 data quality/constraint/query/index 这类 DB 词 | 标题；对比 [50] 的 arXiv 标题，PVLDB 版加了 "Data Quality" |
| R2 | 摘要用 "observation→therefore→technique" 的因果链引出方法 | 摘要中是否有一句"我们观察到…"，紧接着一句"因此…" | A5→A6 |
| R3 | 摘要的每个数字都绑定比较对象，并说明是百分点还是相对值 | 搜索摘要里的 "%"，看后面是否跟着 "vs <baseline>" 和口径 | A7（本文绑定了比较对象，但没说明口径，是反例） |
| R4 | 部署/使用证据与受控评估在摘要中分句、在正文中分节 | 摘要中部署句是否独立；正文中是否有单独的 Deployment 小节 | A8；§2.4 vs §4 |
| R5 | Intro 第一段用 DB 语言重新框定新技术（tuple、relation、batch/online） | 第一段是否出现至少 2 个 DB 术语 | I-P1 S3、S5 |
| R6 | Intro 中有一个明确的研究问题句（疑问句） | 搜索 Intro 中的 "?" | I-P2 S8 |
| R7 | 用一句话与最接近的 DB 工作切割：它假设了 X，新场景不满足 X | Intro 中是否有 "While … [DB cites], … does not apply to …" | I-P2 S7 |
| R8 | Intro 用 run-in 粗体小标题组织成：例子→洞见 1→洞见 2→系统→组件 1→组件 2→贡献 | 数 Intro 中粗体或斜体的 run-in 标题（本文有 6 个） | I-P3 至 I-P8 |
| R9 | 每个洞见都来自数据（N 个真实 pipeline），并映射到一个系统组件 | 每个 insight 段是否带数字，是否被后文的某个组件"消费" | I-P4（19 个 pipeline→组件 1）、I-P5（>50 条断言→组件 2） |
| R10 | 每个设计选择都写成 "Instead of <naive>, which <fails>, we <technique>" | 方法段首句是否出现 instead of / rather than | I-P7 S1、I-P8 S1、2.3-P1 |
| R11 | 难度和可解性连写：先说 NP-hard（附归约来源），紧接着说"但在我们的规模下 ILP 可行"，并给出变量规模 | NP-hard 句之后两句内是否有规模数字 | I-P8 S4–S5；3.2 S12–S14 |
| R12 | 形式化分三层：自然语言目标（Intro）→抽象优化问题→完整 ILP；每引入一个变量就紧跟一句含义解释 | 检查每个新变量后面是否有解释句或 `//` 注释 | I-P6 S2；3.1；3.2；3.3.1-P3 |
| R13 | 第二个优化问题只标增量（颜色或标记），并单独一句解释为什么保留旧约束 | 第二个 ILP 是否高亮改动；是否有 "We maintain <c> because…" | 3.3.1-P4 S1、S3 |
| R14 | 先定义理想指标（全集），再明确退到样本版本，并前指后文如何补救样本不足 | 定义之后是否有 "in practice … uncomputable … we assume <sample> … (Section X)" | 3.1-P3 |
| R15 | 一个玩具例子贯穿方法部分（≥5 处复用），形式化和实验部分换成真实例子 | 统计 running example 的出现次数；看评估集是否不含该例子 | 电影例子 7 处；codereviews 用在 3.3 和 4.3 |
| R16 | LLM 调用要标注模型名和日期 | 搜索 "GPT-4" 后是否紧跟 "(as of <month year>)" | 2.2-P4、2.3-P1、2.4-P1 |
| R17 | 使用量数字附口径和测量盲区：排除了什么、没测什么、负面信号缺失不等于成功 | 部署段中每个数字后是否有 i.e./however/we did not measure | 2.4-P2 S1、S6、S7 |
| R18 | 实验约定写全：运行错误如何计、求解器及配置、阈值取值的理由 | 方法比较小节中是否有 error 处理、solver 名、"for simplicity we set" | 4.2-P1 S3–S5；4.3-P2 S1 |
| R19 | 基线 = Intro 中被否定的朴素方案；先排除平凡基线并说明它退化成什么 | 基线定义是否能在 Intro 中找到对应的朴素方案；有没有"simplest baseline yields…" | I-P8 S2–S3 ↔ 4.2-P2 |
| R20 | 不测的指标要声明并给理由，再说明为什么测到的那个指标更关键 | 搜索 "We do not assess" | 4.2-P4 S3–S4 |
| R21 | 先证明组件可行（准确率、运行时间，并点名最大值），再报主结果 | 结果小节第一段是否是 feasibility，是否点出最差值 | 4.3-P1 S2–S3 |
| R22 | 讨论用粗体发现型小标题，并包含一段主动回应"复杂度值不值" | 结果小节中是否有 "one may wonder…" 一类的段落 | 4.3-P8 S1 |
| R23 | 主动展示失败案例（代码或实例），说明机制而不是只给数字 | 结果讨论中是否至少有一个 "On the flip side" 并附具体实例 | 4.3-P5 S2–S3；2.4-P3 S4–S7 |
| R24 | RW 每段以一句"我们与之关系"收尾（正交/互补/补 gap），最接近的工作在 Intro 和 RW 中措辞一致 | 每段最后一句是否含 our work / complementary / while requiring | 5-P1 S5、5-P2 S6、5-P3 S3、5-P4 S5–S6 |
| R25 | 结论按贡献顺序复述，不重复头条百分比；未来工作从本文局限和被否决的方案自然延伸 | 结论中是否没有 % 数字；FW 是否呼应前文的局限 | 6-P1；6-P2 S4 呼应 3.3-P1 |

**反面清单（本文的瑕疵，写作时要自查）**
- 交叉引用笔误（2.3 写的 Fig 3 应为 Fig 2）；同一变量的两种写法（wij）；数字小出入（版本数 3–16 vs 3–11；坏样例 34 vs 35.1；"hundreds to thousands" vs "thousands" 变量）；"significantly" 没有统计检验；百分点和相对值口径不清；组件 1 没有受控评估；评估集与开发集重叠没有作为威胁讨论；3.2 末句缺动词。
