---
name: pr-submission-package
description: 在研究证据与作者事实已具备时准备或核查 Pattern Recognition 的可编辑稿件、Highlights、cover letter、声明和附件，并区分本地完成、系统proof与正式提交。
---

# Pattern Recognition 投稿材料

先确认用户请求的是打包、修订还是投稿系统操作。复用已确认作者事实，不从机构访问、邮箱或旧稿推断本稿作者资格。明确主稿/代码/数据版本；未做真实实验时只准备结构与事实需求，不能生成带虚构发现的投稿稿。

刷新[官方Guide](https://www.sciencedirect.com/journal/pattern-recognition/publish/guide-for-authors)。2026-11-09个人浏览器实读确认：单栏、LaTeX双倍或Word1.5行距、20–35页（综述40）、摘要≤250词、关键词1–7、数字引文、Highlights必需。指南对附录计页内部矛盾，记录正文/总页数并尽量总计≤35；不要假定豁免。可配合pr-venue-gate，未安装时直接核查官方页。

准备并逐项对应：

- 可编辑主稿、完整引用库、正式PDF和依赖；Guide链接的[CAS模板](https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip)按当前实链复核。保留原模板通知，兼容修改单独记载。
- 可编辑表、独立图文件和图注；图表源与核实结果相连，不在打包时改变数据或比较范围。
- 独立可编辑Highlights，3–5条且每条≤85字符含空格；每条与正文贡献/真实发现一致。
- Cover letter说明重要性和适配，并回答：五篇代表当前SOTA的文章及是否比较、可用公共数据集及本文采用情况、通常验证指标及本文选择；未采用时据实解释。
- 利益冲突工具生成的Word声明、真实资金和资助者角色、CRediT、数据可用性、适用的AI声明，以及作者确认的姓名/单位/通讯信息。不能把本地模拟声明称工具导出。
- 必要补充材料，随稿并逐项正文引用，给清楚说明；文件会原样出版，需独立检查。数据Option C允许无法共享时解释原因，私人备份不等于公开存储。

Graphical abstract是鼓励项；需要时按当前Guide与AI政策制作，不能用一般生成式工具制作。研究方法中的模型调用、代码辅助与数据分析应有Methods披露，写作辅助另有稿末AI声明；不得以生成式修图改变实验输出。

在干净目录重建源包，检查缺依赖、绝对路径、参考文献和字体；逐页读最终PDF，核对公式、表头、字号、图例、页数及作者信息。打包后重新比较正文、摘要、Highlights、cover letter与补充的数字及范围。向实际Editorial Manager上传时再遵守其当前源文件规则并核对系统proof，不根据本地编译推断平台兼容。

分别报告：**科学证据就绪 / 本地文件就绪 / 系统proof已检查 / 已提交且有回执**。Guide实链为[PR Editorial Manager](https://www.editorialmanager.com/PR/default.aspx)，公开入口可访问不证明登录或提交成功。只有用户授权范围包含相应系统动作且最终作者批准事实齐备时执行；技能本身不扩大权限。

迁移依据：[cviu-submission固定快照](https://github.com/wanghongsheng01/claude-skills/blob/4ba3b7356807a54e8858406ca3bc24a303c7910d/cviu-submission/SKILL.md)，只迁移版本、重建与多状态核查方法；CVIU引用格式和无显式页数上限不适用于PR。
