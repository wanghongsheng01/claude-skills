# BOND: A Co-Designed Framework for LLM-Powered Analytics Over Relational Data (ICDE 2026, Regular research paper)
- Source of full text: **未获得全文**。检索记录：arXiv API/网站按标题、关键词（tile quantization、prefix sharing、radix tree、bin-packing）和作者（Lixiang Chen、Chengcheng Yang、Zhicheng Pan 等）检索均无匹配；GitHub 仓库/代码搜索无匹配；Unpaywall 显示 is_oa=false；Semantic Scholar 显示 openAccessPdf=CLOSED；IEEE Xplore 页面返回反爬验证（未尝试绕过）；按要求未访问 dblp。IEEE DOI 10.1109/ICDE65706.2026.00145（proceedings pp. 1914–1926，共 13 页）。作者：Lixiang Chen, Qin Zheng, Zhicheng Pan, Chengcheng Yang, Rong Zhang, Xuan Zhou（据 OpenAlex/S2 元数据；从作者过往工作如 AQETuner、ByteCard 推测为华东师大团队，未经全文确认）。
- **FULL TEXT READ: no** —— 仅读了 Semantic Scholar 提供的官方摘要（约 10 句）。以下凡是摘要中没有的内容都标为【推测】或【未知】，不能当作论文事实引用。
- Length: 13 页（来自 proceedings 页码）；figures/tables/references/equations/theorems 数量【未知】（OpenAlex 仅匹配到 24 条参考文献，这不是全文参考文献总数）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**（摘要可见）：数据库中通过 SQL 调用 LLM（LLM UDF / semantic operator）做分析，带来很大的计算开销，因为通用 LLM 推理引擎并非为关系型工作负载设计。
- **本质问题（基于摘要的还原）**：**批量 LLM 推理的执行优化 / 调度问题**——在"整批数据事先已知"这一数据库特有前提下，联合优化 (a) 推理引擎内的批组织和 (b) 关系数据的布局，以最小化查询执行时间。
  - 输入：一个对关系表逐行调用 LLM 的 SQL 查询（整批行与 prompt 模板事先可知）；GPU 集群。
  - 输出：数据重组后的执行顺序 + 推理批次划分 + 分布式调度计划。
  - 目标：最小化查询执行时间（摘要报告最多降低 71.8%）。
  - 约束：GPU 硬件特性（tile 大小）、【推测】显存/KV cache 容量。
  - 摘要明确提到的两个子问题形式：批创建被建模为 **bin-packing 问题**；数据布局通过一个 **tree-based framework** 搜索最大化前缀共享与 cache locality 的排列。是否有 NP-hard 证明【未知】（bin-packing 本身是 NP-hard，论文很可能借此论证，但未读到）。
- **为什么现有方法不够（摘要给出的 gap）**：
  1. 现有优化技术面向**不可预测的在线请求流**设计（如 serving 系统），没有利用数据库操作中"整批数据可预知"的先验；
  2. 现有方法把 LLM 引擎当作**黑盒**，只在数据侧或只在引擎侧优化，缺少协同设计（co-design）。
  - 证据形式（预实验、Figure 1）【未知】。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea（摘要可见）**：数据库里的 LLM 调用是"离线批"而非"在线流"，因此可以同时改造推理引擎和数据组织，让两边围绕"前缀共享 + GPU 友好的批形状"协同优化。
- **技术组件（摘要可见）**：
  1. **Batch-efficient LLM inference engine**：用 radix tree 索引到来的 prompt 以识别共享前缀；把批创建建模成 bin-packing，使计算分组与 GPU 硬件特性对齐，从而缓解 **tile-quantization 效应**（矩阵维度不是 tile 整数倍导致的算力浪费）。→ 对应 gap 2（引擎侧白盒化）。
  2. **Prefix-oriented data re-organizer**：在推理前重排关系数据（行序/列序【推测】），用树形框架寻找最大化前缀共享与 cache 局部性的布局。→ 对应 gap 1（利用批先验）。与 MLSys 2025 "Optimizing LLM Queries in Relational Data Analytics Workloads"（行/字段重排以提高 KV cache 复用）思路相近，BOND 是否将其作为基线【未知】。
  3. **Bubble-free task scheduler**：在分布式环境下连接上述两组件，保证 GPU 持续利用（无空泡）。→ 系统工程。
  - 真正的新东西（判断）：把 tile-quantization 这一 GPU kernel 层效应引入"LLM-in-DB"批构造，并与数据重排协同——这是"跨层 co-design"的卖点；radix-tree 前缀共享本身来自 SGLang/RadixAttention 一类工作【推测】。
- **理论保证**：【未知】。

## 3. 实验设计 (Experiments)
- 摘要只给出一个数字："query execution time 最多降低 71.8%"。数据集、基线、指标、是否报告 token/美元、消融与可扩展性实验均【未知】。
- 【推测，需全文核实】可能的基线类别：直接调用 vLLM/SGLang 的 LLM-UDF 执行、带前缀缓存的 serving 系统、MLSys'25 的数据重排方法；可能的指标：端到端查询时间、GPU 利用率、吞吐、prefix hit rate。

## 4. 写作结构 (Writing)
- **标题模式**：`缩写: A Co-Designed Framework for <应用> Over <数据类型>`——强调 "co-designed"，即"跨层协同"作为核心贡献类型。
- **摘要逐句功能（已读）**：S1 背景：SQL 集成 LLM 让分析流程优雅 → S2 问题：带来显著计算开销，因为常规推理未针对关系负载优化 → S3 gap：现有优化面向在线流、把 LLM 引擎当黑盒，没有利用整批数据先验 → S4 提出 BOND，两侧（引擎 + 数据组织）的 batch-aware 协同优化 → S5 "两个主组件" 引导句 → S6–S7 组件一：radix tree 前缀索引 + bin-packing 批构造，缓解 tile quantization → S8 组件二：前缀导向的数据重组，树形框架找最佳布局 → S9 两组件由 bubble-free 调度器连接 → S10 结果：最多降低 71.8% 执行时间。结构是标准的"背景—问题—gap—方法（组件逐一）—结果"，且"First/Second/Finally"清晰编号。
- 引言、章节、Related Work、图表【未知】。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点（基于摘要的有限判断）
1. **切中 DB 系统社区的核心问题**：LLM-in-SQL 的执行效率是 2024–2026 热点（LOTUS、Palimpzest、MLSys'25 数据重排等），BOND 给出"系统层"答案。
2. **明确的 DB 特有洞见**："整批已知"是数据库区别于在线 serving 的关键前提，这种"利用 DB 场景先验去优化 ML 系统"的叙事很容易被 ICDE 认可。
3. **跨层 co-design**：同时动推理引擎（GPU tile 层）与数据层（行/列布局），贡献面宽。
4. **经典组合优化建模**：bin-packing、树搜索布局，便于给出形式化与复杂度。
- **对我们的启示（不依赖全文）**：成本维度可以是"GPU 时间/执行时间"而不只是 API 美元；"在线 vs 批"的区分是一个可复用的 gap 构造方式。
- **局限（只能就摘要判断）**：摘要只报告执行时间，未提准确率是否完全不受影响（数据重排可能改变 prompt 顺序/上下文，从而影响 LLM 输出——这是一个可能的攻击点，需要全文核实作者是否讨论）；未提美元成本或 API 场景（方法似乎面向自托管 GPU）。
- **建议**：若作者有 IEEE Xplore 机构访问权限，请手动下载全文放入 pdfs/A/ 后再补全本笔记。
