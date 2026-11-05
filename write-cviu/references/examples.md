# CVIU 写作范文与使用边界

核验：2026-11-05。以下是公开发表近邻论文的观察，不是期刊硬性要求或编辑给出的录用公式。出版社直接读取受阻时明确保留“搜索索引”；作者稿不能冒充期刊最终排版版本。这里只存引用与短分析，不附第三方全文或原图。

## 神经渲染与 Gaussian 控制

**Gaussian Splatting with NeRF-based color and opacity**，CVIU 251 (2025),104273，DOI 10.1016/j.cviu.2024.104273。

[正式页](https://www.sciencedirect.com/science/article/pii/S1077314224003540)；[作者稿 v5](https://arxiv.org/html/2312.13729v5)。本次正式页索引含摘要/章节摘录；作者稿正文可读。观察锚点：§3、Fig.1–2；§4 的实现/消融/时间；Table 6；§5。它展示了机制、局部结果和资源代价并列的组织方式。作者稿与正式版的表号可能不同；不要从范文继承公式正确性或夸张措辞。

## 机制应有独立评价

**NeRFtrinsic Four: An end-to-end trainable NeRF jointly optimizing diverse intrinsic and extrinsic camera parameters**，CVIU 249 (2024),104206，DOI 10.1016/j.cviu.2024.104206。

[正式页](https://www.sciencedirect.com/science/article/pii/S107731422400287X)；[作者稿 v4](https://arxiv.org/html/2303.09412v4)；[作者项目页](https://hannahhaensen.github.io/nerftrinsic_four/)。观察锚点：§4.2 的两类指标、§4.4 的对照条件、§4.6 的机制与困难条件分析、Fig.3、§5–6。公开稿较早；最终版对360°扩展的描述有变化，不得混用结论。

## 细节与分配问题的命名

**FSA-GS: Fine-Structure-Aware Gaussian Splatting for sparse-view novel view synthesis**，CVIU 271 (2026),104892，DOI 10.1016/j.cviu.2026.104892。

[正式页](https://www.sciencedirect.com/science/article/pii/S1077314226002596)；[章节摘录](https://www.sciencedirect.com/science/article/abs/pii/S1077314226002596)。仅读到官方索引的题名、摘要、引言/贡献及部分实验设置，未获得全文。可用它理解如何把细节分配问题写进题名与动机；不能从这些摘录推断消融是否完整、推荐固定章节数、声称已检查全部图片。

## 迁移时作独立判断

把范文的组织原则用于当前论文，而不是借来范文的技术结论。先确认任务、监督、比较预算和科学问题是否相同；不同任务的范文可启发表达，却未必是有效的直接实验基线。凡建议一个新指标或消融，应解释它排除何种替代解释。删去一个“不足”句前，判断它是重复修辞还是理解结果所需的条件；后者应压缩并准确表达，不能隐藏。
