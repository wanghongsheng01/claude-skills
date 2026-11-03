# Tag-Filtered Approximate Nearest Neighbor Search (ICDE 2025, Regular)
- Source of full text: **无公开全文**。已检索 arXiv API（标题、作者 Luo Jiarui + Deng Dong 组合）、arXiv 网页检索、OpenAlex、通用网页搜索，均无开放版本；IEEE DOI 10.1109/ICDE65448.2025.00272（需订阅，未访问）。实际阅读的材料：(1) OpenAlex 收录的摘要全文；(2) 作者 GitHub 仓库 github.com/SpaceIshtar/FilterGraph 的 README（README 自述为"my ICDE25 paper Tag-Filtered Approximate Nearest Neighbor Search"的代码，仓库内无论文 PDF）。
- **FULL TEXT READ: no**（只读了摘要 + 代码 README）。以下凡标【推断】的内容均为基于摘要/README 的推断，**不是论文原文内容**；页数、图表数、参考文献数无法统计。
- Length: 无法统计（未读全文）
- 作者（OpenAlex）：Jiarui Luo, Miao Qiao, Chaoji Zuo, Dong Deng（Rutgers / Auckland 一线；与 SeRF (SIGMOD'24, range-filtering ANNS) 作者群重叠）

## 1. 科学问题的本质 (Problem essence)
- **表面问题**（摘要）：对象带有 tag（如产地、颜色、类型），查询要求只在"携带查询 tag 的对象"中做 ANNS，作者称为 TFANNS。
- **本质问题**【推断，基于摘要的形式化】：输入为向量集合 S，每个对象 o 带 tag 集合 T(o)；查询 (q, T_q, k)；输出满足 tag 约束（摘要说"carry the query tags"，即 T_q ⊆ T(o) 或至少包含查询 tag，确切语义未读到）的近似 k 近邻；约束为索引内存；目标为在 recall ≥ 0.9 时最大化 QPS。核心张力是**索引内存 vs. 低/中频 tag 查询的召回率**。
- **为什么现有方法不够**（摘要明确给出的 gap）：
  1. SOTA Filtered-DiskANN（图索引）对**低到中频 tag** 的查询召回率低；
  2. 对这些 tag 做 pre-filtering（为子集单独建图/索引）能提高召回，但带来**大内存开销**。
  作者声称自己是第一个做 **tag-frequency-aware** 图索引的 TFANNS 工作——即"tag 频率"是 gap 的组织轴。
- **问题定义形式**：未读到原文，无法确认是否有复杂度结论。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**（摘要）：根据 tag 频率，在"全局一张图（省内存但低频 tag 召回差）"与"按 tag 预过滤建子图（召回高但内存大）"之间取折中，提出三种建图策略以平衡性能与内存。
- **技术组件**（来自 README 的命令行，能确认存在三种索引构建方式）：
  1. **Local Method**（`build_index`，参数含 graph_degree、num_of_entry_points、Lsize、ef_construction）【推断：按 tag 局部建图/多入口点】；
  2. **Global Method**（`build_index_v3`，参数含 degree_budget——即**度预算**）【推断：在全局度预算约束下为不同 tag 分配边，体现内存约束】；
  3. **Packing Strategy**（在 Local 基础上增加 pack_k 与 threshold_high 参数；搜索端使用 `index_sharing.h`）【推断：高频阈值以上的 tag 走共享图、低频 tag 打包/共享索引结构以节省内存】。
  - 数据格式：向量用 bin 文件，tag 以 CSR 稀疏矩阵存储，查询 tag 同样为稀疏矩阵——说明一个对象/查询可有多个 tag。
- **理论保证**：未读到，未知。

## 3. 实验设计 (Experiments)
- 摘要只给出一句结果："under ≥0.9 recall, our QPS is up to 13 times that of the best baseline"（"up to X×" 表述）。
- 基线：至少包含 Filtered-DiskANN 与 pre-filtering 类方法（摘要提及）；其余数据集、硬件、实验列表均**未读到**。

## 4. 写作结构 (Writing)
- **标题模式**：极简问题名式标题"Tag-Filtered ANNS"——直接命名一个新问题变体（与 SeRF 的"Range-Filtering ANNS"同一命名套路），暗示"定义新问题"型贡献。
- **摘要逐句功能**（摘要全文已读）：S1 ANNS 背景与重要性 → S2 对象带 tag、常见带 tag 约束的检索 → S3 命名问题 TFANNS → S4 SOTA Filtered-DiskANN 对低–中频 tag 召回低 → S5 pre-filtering 提高召回但内存大（形成 trade-off）→ S6 提出三种建图策略在性能与内存间折中，并声明"首个 tag-frequency-aware 图索引" → S7 实验：recall ≥ 0.9 时 QPS 最高为最佳基线 13 倍。摘要结构是典型的"背景 → 命名问题 → SOTA 缺陷（一句话、带具体条件）→ 朴素修补的副作用 → 我们的折中 → 首创性声明 → 一个数字"。
- 引言、章节结构、图表：**未读到**。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点【均为基于摘要的推断】
1. 问题有明确工业需求（向量数据库中的属性/标签过滤是普遍场景），且命名了一个清晰的问题变体。
2. gap 以"tag 频率"这一可量化的数据特征来刻画——低频 tag 的召回问题可以用一张"召回 vs tag 频率"的图直接展示（这是我们写类似论文时值得复用的 motivating 图思路，但不确定原文是否这样做）。
3. 把"内存 vs 召回"的 trade-off 显式化，并提供多种策略覆盖 trade-off 曲线，而非单一方法。
4. 结果数字大（13×）且设定了具体 recall 门槛（≥0.9），表述规范。
- **后续行动建议**：若需要全文，可通过机构 IEEE Xplore 访问或向作者索取；在获得全文前，本笔记不应作为写作结构/实验协议的依据。
