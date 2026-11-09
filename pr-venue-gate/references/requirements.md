# 官方要求快照与证据边界

核查日2026-11-09；[canonical PR Guide](https://www.sciencedirect.com/journal/pattern-recognition/publish/guide-for-authors)。该日CLI真实GET403，个人Chrome只读可见正文；以下基于后者，未进入投稿系统。提交前刷新。

| 项目 | 核查结果 | 指南位置 |
|---|---|---|
| 范围 | 原创模式识别理论/方法/应用，扎根相关文献；非模式识别主体的常规应用应投别处 | Aims and scope |
| 审稿 | Single anonymized；初筛后通常至少两名评审 | Peer review |
| 版式 | 单栏；LaTeX双倍/Word1.5倍行距；两端对齐、有页码 | Journal specific information: Writing and formatting |
| 页数 | 20–35；综述至40；附录计页存在矛盾 | 同上、Submission checklist → Page Limit |
| 字体版心 | Times New Roman；正文及表10pt、脚注/图注8pt；上右下左4.3/4.8/4.3/4.8cm | Journal specific information |
| 标题/作者页 | 标题14pt，建议10–15词且简洁；作者信息8pt，真实完整单位和通讯信息 | 同上、Title page |
| 摘要/关键词 | 摘要≤250词，独立可读；英文关键词1–7 | Abstract、Keywords |
| Highlights | 必需，3–5条×每条≤85字符含空格；独立可编辑文件 | Highlights |
| Graphical abstract | 鼓励；独立文件，宽≥1328px、长边水平、13cm宽可读 | Graphical abstract |
| 源 | 可编辑doc/docx/tex；PDF不是源；Guide链接CAS模板 | File format、LaTeX |
| 表图 | 表可编辑无竖线/底色；图按出现引用、独立文件与图注；矢量嵌字体，照片≥300dpi、位图线图≥1000dpi | Tables、Figures, images, and other artwork |
| 引文 | 方括号数字按出现次序；请求35–55条，相关近期多来源；避免堆引及过多非评审预印本 | References |
| 数据 | Option C：存储并引用/链接，不能共享须说明原因；投稿给可用性声明 | Research data、Data statement |
| 声明 | 利益冲突工具生成Word文件；资金与资助角色、CRediT、适用AI披露；作者须批准具体版本 | Ethics and policies、Article structure |
| 附件 | 随稿、正文引用并给说明；原样出版不代排版 | Supplementary material |
| Cover letter | 必需；说明重要性与范围，回答五篇SOTA文章、公共数据集、验证度量三组问题及未使用理由 | Submission checklist → Cover Letter |

规则冲突：通用File format许可LaTeX双栏，而专属段禁止，采用单栏。专属页数句和checklist把appendices列为包含项，另句又说不计；记录正文及总页数，不能凭一句获得豁免。通用段双倍行距与Word专属1.5不同，采用专属值。表格10pt与段末“脚注字号或略小”不一致，采用明确10pt。

结论要讨论优势、弱点、领域用途、未来工作，与摘要不同。节编号采用1.1等；摘要不编号。无需机械限定段数或贡献条数。参考文献必须真实，正式版可用则替代预印本。

[Elsevier AI政策](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals)：论文准备辅助须披露；研究方法/代码/分析中的AI在Methods描述；解释图可以在人工核查、图注及总体声明披露下使用；数据图必须来自真实数据和可复现方法；原始实验/观测图像不可用生成式工具伪造或改造；一般生成式工具不用于graphical abstract。勿沿用旧版笼统禁图说法。

[Option C原文](https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines)允许对不能共享作原因说明，不等于必须无条件公开全部数据。私人Git备份、审稿附件与公开仓库是不同访问状态。

Guide实链：[CAS ZIP](https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip)、[PR Editorial Manager](https://www.editorialmanager.com/PR/default.aspx)。本快照只验证链接，未执行模板、登录或上传。
