# Querying Templatized Document Collections with Large Language Models (ICDE 2025, Regular research paper；系统名 ZenDB)
- Source of full text: arXiv 2405.04674v1（2024-05-07，唯一版本，标题为 "Towards Accurate and Efficient Document Analytics with Large Language Models"，作者相同：Yiming Lin, Madelon Hulsebos, Ruiying Ma, Shreya Shankar, Sepanta Zeighami, Aditya G. Parameswaran, Eugene Wu；UC Berkeley/清华/哥大）。ICDE 版 DOI 10.1109/ICDE65448.2025.00183（pp. 2422–2435）。**注意**：arXiv 版是投稿前的 ACM 双栏排版预印本，不是 camera-ready；对比 OpenAlex 上 ICDE 版摘要，数字有小幅更新（ICDE 版 "up to 31× cost savings"、"81% in recall"；arXiv 版为 30× 与 80%），且 ICDE 版摘要更短、更聚焦"key insight is that documents… follow similar templates"。因此以下结构/数字以 arXiv v1 为准，可能与正式版略有出入。FULL TEXT READ: yes（arXiv v1 全文；PDF 存于 pdfs/A/ZenDB_2405.04674v1.pdf）。
- Length: 正文约 14 页（ACM 双栏排版，换成 IEEE 版约 13–14 页）+ 参考文献约 1.3 页；Figures 14 个（Fig.1–14）；Tables 7 个（Table 1–7）；references 63 篇（arXiv 版）；公式很少（编号公式 0 个，行内定义若干：选择度 s_o、goodness f_o = e_o × s_o、E(T)=|T|×e）；1 个 Theorem（Theorem 3.1，含完整归纳证明）；3 个 Algorithm（template_gen、tree_evaluate、tree_evaluate_multi_tuple）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：用 LLM 对一批 PDF 文档（市政议程报告、论文、违规通知）回答 ad-hoc 分析型查询（聚合、多过滤条件）。
- **本质问题**：**在非结构化文档上做"带 LLM 算子的 SQL 查询处理"，并以 LLM 调用的美元成本为主要代价的查询优化问题**；关键是找到一种"索引"来只把相关文本片段交给 LLM。
  - 输入：文档集合 D（带字体/位置等视觉格式信息的 PDF/Word）；用户定义的 DTable schema（表名 + 自然语言 DESCRIPTION，属性可惰性添加）；SQL 查询（非嵌套 SPJ + 聚合 + GROUP BY，join 仅限同一文档内 doc_id 等值连接）。
  - 输出：查询结果元组 + provenance（来源 text span）。
  - 约束 / 目标：在保证 precision/recall 的前提下最小化 LLM 调用成本（美元，或可替换为延迟）。论文没有写成单一的 argmin 公式，而是将其分解为传统 DB 子问题：索引构建（SHT）、数据模型、逻辑计划（谓词下推 + 按 e_o×s_o 的昂贵谓词排序、投影上拉、按 E(T) 贪心左深 join 序）、物理算子（基于 summary 的树搜索）。
- **为什么现有方法不够（3 个根因）**：
  1. Vanilla LLM 处理整篇长文档：不准（长上下文、复杂数据处理弱）且贵；
  2. RAG：按 embedding 相似度取固定粒度 chunk，**与文档的语义结构脱节**，找不全相关片段（例子：查 capital improvement 项目只取回红框一段，漏掉后续页面 20+ 个项目）；
  3. 现有 multi-modal DB / text-to-table ETL 对整篇文档调用 LLM，只适合小而简单的文档；XML/JSON 查询需要显式层级，而这里层级是隐式的。
  - 证据：Example 1.1 + Fig.1（市政议程报告及其语义层级）；Fig.2 一张"cheap vs accurate"二维示意图：在 GPT-4-32k 的样例查询上 ZenDB 比 LLM 和 RAG 分别高 25% 和 48% 准确率，成本只有 LLM 的 7%。
- **问题定义形式**：没有单一 "Problem Definition"。形式化集中在 Section 3.1 Preliminaries：Documents/Words/Phrases、Visual Pattern p(s)（7 维特征向量）、Candidate SHT（有序树 + 前序遍历单调）、text span、granularity、template（granularity→visual-pattern 集合的有序字典）、well-formattedness（兄弟节点视觉模式相同 + 同模式节点视觉前缀唯一）。复杂度方面只说"候选 SHT 指数多"，无 NP-hard 结论。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：同一集合中的文档往往由模板生成，模板的视觉格式（字体、大小、编号）暴露了隐式的语义层级；把它抽成 Semantic Hierarchical Tree（SHT）作为"语义索引"，查询时像人看目录一样沿树向下找最小相关片段，只把这片段交给 LLM。
- **技术组件**：
  1. **SHT 构建（单文档 oracle_gen）**：按视觉模式聚类 phrase → 每簇抽样 min(|C|,k) 条用 LLM 判断"是否 header"，过半否则剪掉 → 自顶向下按最小 phrase index 逐簇建树。**Theorem 3.1**：若真实 SHT well-formatted 且 LLM 能正确识别非 header，则 oracle_gen 输出真实 SHT。对 200+ 文档/16 个数据集/6 个领域的检验中 GPT-4 在 k=10 时 97% 文档正确，总花费 $0.37。
  2. **跨文档模板复用（template_gen, Algorithm 1）**：文档的视觉模式只要覆盖模板粒度的一个前缀即视为匹配，直接构建 SHT，**不调用 LLM**；不匹配才调用 oracle_gen 并登记新模板。→ LLM 成本只与"模板数"相关而非文档数。这是最有 DB 味道的"摊销"设计。
  3. **数据模型与 SQL 扩展**：DTable（CREATE TABLE … WITH DESCRIPTION；ALTER TABLE ADD attr WITH DESCRIPTION）、SHT Table、Table Catalog、Attribute Catalog；用户属性初值为 NULL，**按查询惰性填充**（lazy materialization）；隐藏系统属性 doc_id/text_span/node 用于 provenance。表/元组定位：在一个代表文档上用 table_oracle/tuple_oracle 自顶向下判定，其他同模板文档用两条规则（同粒度 + 名称相似度 > θ）无 LLM 填充。
  4. **查询引擎**：逻辑层沿用经典"昂贵谓词排序"（引用 Hellerstein 式工作 [32]），以 f_o = e_o × s_o 升序执行、e_o 在线自适应估计；投影上拉避免为被丢弃元组付 LLM 费；join 贪心左深序以 LLM 成本 E(T) 排序；nested loop join（因为 LLM 成本主导，join"实际上免费"）。物理层：每个 SHT 节点有 summary = 祖先+自身 header + NLTK 抽取式摘要 + 与表达式最相似的 top-1 句（动态部分），tree_evaluate（Algorithm 2）逐层用 search_oracle 筛候选节点，再用 evaluate_oracle / extract_oracle；多元组情况用 Algorithm 3 + multi_tuple_oracle。
  - 真正的新东西：SHT + 模板复用 + summary 树搜索；查询优化部分是把经典 DB 技术（谓词下推、昂贵谓词排序、投影上拉、惰性物化、provenance）"迁移"到 LLM 成本模型上——这是论文对 DB 审稿人的主要吸引力。
- **理论保证**：Theorem 3.1（正确性，有完整归纳证明，条件是 well-formatted + 完美 LLM oracle）。无成本最优性或近似保证；成本模型是启发式的。

## 3. 实验设计 (Experiments)
- **实验列表（Exp 1–5）**：Exp1 vs GPT-only；Exp2 vs RAG；Exp3 数据准备成本（3.1 SHT 构建、3.2 表填充、端到端成本摊销）；Exp4 summary 组成消融；Exp5 换用便宜 LLM（ZenDB-light, GPT-3.5-turbo）。没有显式 RQ 编号，用 "Experiment k" 小标题。
- **数据集（3 个，自建/合作方提供的真实集合）**：Scientific Publications（100 篇，平均 11.5 页、13,230 tokens，来自 UC Irvine 系统综述研究，20 个研究问题有人工标签）；Civic Agenda Reports（41 份，Malibu 市 2022–2024，平均 8.7 页、3,185 tokens，来自 Stanford Big Local News）；Notice of Violations（80 份，美国交通部 2023–2024，7.1 页、3,719 tokens）。
- **查询负载**：每个数据集 9 条 SQL，按谓词数 1/2/3 分为 QG1/QG2/QG3，各 3 条；随机选属性构造谓词 + 1 个投影属性 + doc_id，跨表时加 doc_id 等值 join；不含聚合（论证聚合在属性抽取后用关系算子执行，性能相同）。
- **基线（4 个）**：GPT_single（每个谓词/投影一次调用 + 整篇文档）、GPT_merge（所有谓词投影合并成一次调用）、RAG_seq（LlamaIndex 顺序 chunk，128 token，top-k=max(1, 5%×doc_size/128)）、RAG_tree（LlamaIndex 递归摘要树）。全部用 GPT-4-32k。**没有对比任何已发表的学术系统**（如 Evaporate、Lotus、Palimpzest 等），基线都是"策略"而非"系统"。
- **指标**：元组级 precision/recall；**成本 = 美元 + token 数（×1000）**，按"每查询每文档"平均；延迟（3 次平均）。表填充质量用 text span 的 FP/FN 定义（预测 span 包含真 span 记 FP，可接受；漏掉记 FN）。
- **实验类型**：主结果（Table 2 总表 + Table 3–5 按数据集×查询组的细分）；成本（Table 2–7 都有 $/tokens；Table 6 SHT 构建：Publication $0.05/6min；Table 7 表填充：GPT-3.5，$0.048/95.4k tokens，FN=0）；端到端摊销论证（预处理总成本 $0.1/$0.015/$0.015，跑一条查询就已比 GPT-only 便宜）；消融（Fig.11：no-ES、no-node-name、no-DS）；便宜模型（Fig.12、14：ZenDB-light precision −7%、recall −3%，成本 1/100；Fig.13：每 $1 可在单文档上跑 3.5k/3.7k/8k 条查询）。没有可扩展性实验（文档数最多 100）、没有参数敏感性实验（k、θ、summary 大小等）。
- **结果呈现**：主结果全部用表（precision、recall、$/tokens、latency 四组并列），消融与 light 版本用柱状图。表述："approximately 29×, 10×, and 4×" 成本节省，"up to 61% in precision and 80% in recall"（vs RAG），"up to a 4× reduction" 延迟，"at a marginally higher cost"（相对 RAG，坦诚说明比 RAG 贵一点）。

## 4. 写作结构 (Writing)
- **标题模式**：ICDE 版 `Querying <数据特征> Document Collections with Large Language Models`——标题直接点出"key insight 所依赖的数据特征（templatized）"，没有系统名；arXiv 版则是 "Towards Accurate and Efficient…"。值得学习：标题把"可利用的数据性质"放在最前。
- **摘要逐句功能（arXiv 版）**：S1 非结构化数据占 80%+ 且难以取值 → S2 现有文档管理不支持 ad-hoc 分析查询 → S3 LLM 直接用或 RAG 都不准，LLM 还贵 → S4 观察：同集合文档遵循相似模板，提出 ZenDB → S5 抽取语义层级 + 新查询引擎 → S6 用户用 SQL 施加 schema 并查询 → S7 结果：up to 30× 成本节省、精度不降，比 RAG precision +61%/recall +80%，成本略高。ICDE 版把 S4 改写为 "Our key insight is…"，更加突出单一洞见。
- **引言逐段功能**：P1 宏观动机（80% 非结构化、95% 企业视为问题）+ 设问 → P2 Example 1.1（真实合作方 Big Local News 的需求；LLM 与 RAG 都失败的具体例子）→ P3 "Leveraging Semantic Structure Helps"（加粗段首，Fig.2 给数字）→ P4 "Templatized Documents Provide Semantic Structure"（Fig.3 三种模板化文档示例）→ P5 "Leveraging Semantic Structure: Challenges"（三个挑战：结构未知且不严格、数据模型/查询接口不明确、LLM 成本高）→ P6 "Addressing Challenges in ZenDB"（逐一对应：SHT + well-formattedness 正确性；SQL 扩展 + 惰性属性；summary 树搜索）→ P7 "Other Related Work"（IR、半结构化 XQuery、text-to-table、multi-modal DB，各一句并说明区别）→ P8 5 条 bullet 贡献。每段都以加粗短语开头，形成"动机→洞见→挑战→解法"的清晰链条。Figure 1 是 motivating example（文档 + 语义结构 + SHT + NL/SQL 查询四合一）。
- **章节顺序与篇幅**：1 Intro（~2.3 页）→ 2 User Workflow（~0.8 页，Fig.4 三步流程）→ 3 SHT（~2.5 页，含定理证明）→ 4 Data Model & Query Language（~1.5 页）→ 5 Table Population（~1 页）→ 6 Query Engine（~2.3 页）→ 7 Evaluation（~3 页）→ 8 Related Work（~0.8 页，6 类：Text-to-Table、RAG、Multi-Modal DB、NL Interfaces、LLMs meet DM、Structured Extraction）→ 9 Conclusion（含 future work：无模板/噪声模板、更多 SQL）。Related Work 放在末尾，引言中有一个简短版本。
- **写作技巧**：
  - 引言用加粗段首词组串起逻辑（Helps → Provide → Challenges → Addressing），读者扫段首即可掌握全文。
  - 用 "User Workflow" 一节代替抽象的 system overview，以用户/DBA 视角讲三步流程，降低阅读门槛。
  - 用"像人看目录找章节"的类比解释树搜索；用 DB 术语（predicate pushdown、projection pull-up、provenance、lazy）包装 LLM 操作，凸显 DB 贡献。
  - 坦诚定义语义选择："按完全填充 DTable 后执行 SQL" 的语义，承认 LLM 不一致问题 out of scope。
  - 示例短引：作者把树搜索比作 "how a person might use a table of contents"。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **单一、清晰、可被数据验证的洞见**："模板化文档 → 隐式层级结构 → 语义索引"，这是一个数据特性驱动的洞见，而非模型技巧，非常符合 DB 社区口味。
2. **把 LLM 查询处理放进经典 DB 框架**：数据模型、DDL 扩展、惰性物化、昂贵谓词排序、join 序、provenance，几乎每一项都能对应到 DB 教科书概念，审稿人容易评价其"DB 贡献"。
3. **成本以美元报告 + 摊销论证**：离线索引成本（$0.1 级别）与在线查询成本分开，并证明一条查询即可回本；ZenDB-light 的"每 $1 可执行查询数"图非常直观。
4. **真实应用场景与合作方**（Stanford Big Local News 记者需求），提升 practical impact 的可信度。
5. **有正确性定理**（虽然条件较强），使"结构抽取"不只是启发式。
- **可借鉴**：用 "Experiment k" 而非 RQ 也可以；预处理成本单独成表；"cheap vs accurate"二维定位图（Fig.2）作为引言第二张图。
- **潜在弱点（供我们攻击）**：(a) 每个数据集仅 9 条查询、最多 100 篇文档，规模小、无可扩展性实验；(b) 基线只有自定义策略，没有对比同期 LLM-powered 查询系统；(c) 依赖视觉格式与模板，非模板/扫描件/噪声模板未处理（作者自列 future work）；(d) 成本模型是启发式（e_o 在线估计），无预算约束下的最优计划；(e) 属性值与谓词结果可能不一致的问题被明确排除；(f) join 仅限文档内；(g) 没有参数敏感性（k、θ、summary 大小）。
