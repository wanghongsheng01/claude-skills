# CYANSQL: Unlock the Power of NL2SQL via Clustering-based Test-Time Scaling (ICDE 2026, Regular)
- Source of full text: **无公开全文**。IEEE DOI 10.1109/ICDE65706.2026.00084（IEEE Xplore document 11629462，ICDE 2026 论文集 pp.1057–1072）。arXiv API（`ti:CYANSQL`、`all:CyanSQL`、`abs:"clustering-based test-time scaling"` 等检索，后续被限流 HTTP 429）、OpenAlex（记录存在但 `is_oa: false`、`oa_status: closed`、无 abstract）、Crossref（无 abstract）、Web 搜索（无 arXiv / GitHub / 作者主页 PDF）均未找到开放版本。Semantic Scholar API 返回 429。IEEE Xplore 页面自动抓取被环境的反爬保护拦截，未尝试绕过。
- **FULL TEXT READ: no**——本笔记只包含书目元数据与一条二手来源（腾讯云相关人员的 LinkedIn 帖子摘要，经 Web 搜索结果转述）。**以下任何关于方法/实验的内容都不是来自论文原文，不可作为引用依据。**
- Length（来自 Crossref / OpenAlex 元数据）：页码 1057–1072，即 **16 页**（含参考文献）；Crossref 记录 **70 条参考文献**；图/表/公式数量 **未知**。
- 作者（OpenAlex）：Haoyu Qin, Tonghui Ren, Zhenying He, X. Sean Wang, Jiashu Xing, Yanghuan Ye, Shifei Huang, Jinbao Li。前 4 位属复旦大学（Zhenying He / X. Sean Wang 组，与 ICDE'24 PURPLE、ICDE'25 CycleSQL 同组），后 4 位推测为腾讯云（据二手来源称为"腾讯云与复旦大学合作"）。

## 1. 科学问题的本质 (Problem essence)
- **仅能从标题与二手来源推断**：标题表明属于 **NL2SQL 的 test-time scaling**（推理时采样多个候选 SQL 再选择），关键词 "Clustering-based" 表明选择/组织候选的方式是 **聚类**。二手来源称该方法针对多表 JOIN、嵌套过滤等复杂查询，按 SQL 的逻辑结构组织候选（"cluster-aware"）。
- 推测（**未经原文证实**）：可能是把候选 SQL 按执行结果或结构等价聚类，以聚类层面的信息替代简单的多数投票（self-consistency）。具体的问题形式化、gap 证据、是否有 NP-hard 结论均 **未知**。

## 2. 方法的最关键之处 (Key insight)
- **未知**（未读全文）。不对组件、理论保证做任何陈述。

## 3. 实验设计 (Experiments)
- 二手来源（厂商宣传，**未核实**）称在 BIRD 上取得 **73.47% EX** 和 **87.22% "Recall"**（推测为候选集中包含正确 SQL 的比例，即 pass@k 类指标，含义未经原文确认）。
- 数据集、基线、LLM backbone、成本报告、是否融合多个 LLM vendor、是否有统计保证：**全部未知**。

## 4. 写作结构 (Writing)
- **标题模式**（唯一可分析的部分）："<系统名>: Unlock the Power of <任务> via <技术>-based <范式>"——"Unlock the Power of" 是营销式开头，"Clustering-based Test-Time Scaling" 同时点出技术手段（聚类）和流行范式（TTS）。系统名 CYAN 疑为 C(lustering)… 的缩写，具体含义未知。
- 摘要、引言、章节结构：**未知**。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
- 无法基于原文判断。仅从元数据看：(1) 16 页、70 篇参考文献，体量为完整 ICDE regular 论文；(2) 产学合作（复旦 + 腾讯云），通常意味着有工业场景/系统部署叙事；(3) 该组前作 PURPLE（ICDE'24）与 CycleSQL（ICDE'25）连续三年在 ICDE 发表 NL2SQL 工作，说明该组熟悉 ICDE 审稿偏好（DB 技术 + LLM）。
- **建议**：若作者可通过机构订阅从 IEEE Xplore 下载 PDF，放到 `/Users/loctek/Desktop/ICDE2027/03_deep_reading/pdfs/B/` 后可补读本篇。由于它是本组与"多候选选择"最直接相关的一篇（与本项目研究方向最接近），**强烈建议补读**，重点核查：聚类依据（执行结果 / SQL 结构 / embedding）、簇内与簇间如何选择、是否组合多个 LLM、是否报告 token 成本、是否有选择正确率的统计保证。
- 本组中用于补位、已全文精读的替代论文见：`B_cyclesql_substitute.md`（同组 ICDE'25，候选验证）与 `B_hexgenflow_substitute.md`（ICDE'26，Text-to-SQL 多 LLM 调用的推理调度与成本）。
