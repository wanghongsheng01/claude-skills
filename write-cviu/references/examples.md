# CVIU 已发表样本与可迁移观察

原七篇核验日期：2026-11-07。2026-11-12 重新精读 VDGS v5、NeRFtrinsic Four v4 作者全文，以及 holistic triangulation 正式排版机构存档并检查实际图像，详见 [三篇逐节图表定位与迁移](exemplar-reading-20261112.md)。其余四篇本轮不新增全文已读的声明。全文阅读与正式出版元数据是不同证据。以下经验是本技能的研究判断，不是 CVIU 录用规则；不附第三方全文或原图。

## Gaussian 表示的控制位置

**Gaussian Splatting with NeRF-based color and opacity**，CVIU 251 (2025), 104273；DOI 10.1016/j.cviu.2024.104273。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314224003540)；[作者 v5 全文](https://arxiv.org/html/2312.13729v5)。

观察定位：作者稿 §3、Fig.2 解释新增网络控制什么；§4 的设计替代与时间表让质量和开销共同可判断；§5 先说明已支持的任务，再界定专门光反射任务的边界；正文时间表使实际成本可判断。迁移时明确自己的控制输入、输出和代价。作者稿早于正式版，表号和实验范围有变化；不能把“开销轻微”等措辞当作未经数字核对的模板。

## 结构主张配结构测量

**View consistency aware holistic triangulation for 3D human pose estimation**，CVIU 236 (2023), 103830；DOI 10.1016/j.cviu.2023.103830。[作者机构页](https://cvl.sjtu.edu.cn/getpaper/1100)；[正式排版机构存档](https://cvl.sjtu.edu.cn/Upload/Paper/View%20Consistency%20Aware%20Holistic%20Triangulation%20for%203D%20Human%20Pose%20Estimation.pdf)。

已读完整九页。§3 定义中间量与结构依赖；§4.2 同时评估位置和姿态合理性；Table 3 展示准确率与成本；§4.4 的对照分别对应设计选择，§4.5 集中讨论未见自由动作的姿态先验覆盖与相机数量变化的重训条件，明确关联 Table 4 的困难情形。迁移原则是测量中心主张本身。其多视角骨架指标不能未经重新定义就充当单目渲染指标；已发表表注也需独立校核。

## 最终图像分数与中间变量分开

**NeRFtrinsic Four: An end-to-end trainable NeRF jointly optimizing diverse intrinsic and extrinsic camera parameters**，CVIU 249 (2024), 104206；DOI 10.1016/j.cviu.2024.104206。[正式发表页](https://www.sciencedirect.com/science/article/pii/S107731422400287X)；[作者 v4 全文](https://arxiv.org/html/2303.09412v4)。

观察定位：作者稿 §4.2 区分图像质量与相机误差，§4.6 测试设计选择与输入减少，§5 讨论外观分数和结构错误可能并存。迁移时为几何、语义或校准主张设置直接证据。2023 作者稿与 2024 正式版的 360° 扩展及初始化条件不同，不能混写；正式版 §6 的可见内容说明 360° 集成仍需带噪初始位姿，并讨论位姿 MLP 初始化；不能沿用作者 v4 的“不适用于 360°”概括正式版。§4.6 的失败阈值实验说明边界可具体测试。也不照搬其特定重复实验的择优聚合方式。

## 近题定位：细节与 primitive 分配

**FSA-GS: Fine-Structure-Aware Gaussian Splatting for sparse-view novel view synthesis**，CVIU 271 (2026), 104892；DOI 10.1016/j.cviu.2026.104892。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314226002596)。

只读到出版社索引中的摘要、引言和部分章节。可观察其把细节问题对应到 primitive 分配与保留操作。适合借鉴题名、任务条件和问题—机制定位；不能据此断言全文消融、成本或图表规范。稀疏视角静态场景与动态人体并非同一比较协议。

## 近题定位：困难输入的具体化

**Towards robust 3D human reconstruction with uncertainty-aware low-rank adaptation**，CVIU 269 (2026), 104813；DOI 10.1016/j.cviu.2026.104813。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314226001803)。

只读到出版社摘要、Highlights 和引言。其问题定位从具体输入退化进入适配与融合机制。可迁移的是先定义“困难”再设计验证；不能由标题借来鲁棒性结论，也不能把单图人体形状恢复与视频人体渲染混为一项任务。

## 分析性研究的标题与问题

**Evaluating the effect of image quantity on Gaussian Splatting: A statistical perspective**，CVIU 263 (2026), 104575；DOI 10.1016/j.cviu.2025.104575。[出版社页](https://www.sciencedirect.com/science/article/pii/S107731422500298X)。

只读到官方索引元数据、Highlights 和摘要。题名直接说明被研究的变量和分析方式，摘要围绕相机数量、数据设计与重建响应。它说明该刊存在 Gaussian Splatting 分析性研究；不能据此断言期刊偏好负结果或保证控制研究获录。摘要所述饱和点属于其设置，不能迁移为其他数据集的通用阈值。未读全文，不能讨论其限制段落或统计检验细节。

## 动态长序列的限定性收益

**WinGS: Windowed Gaussian Splatting for long-sequence multi-view hand interaction reconstruction**，CVIU (November–December 2026), 104968；DOI 10.1016/j.cviu.2026.104968。[出版社预览](https://www.sciencedirect.com/science/article/abs/pii/S1077314226003358)。

只读到官方索引摘要、引言和章节片段。文章将长序列容量问题、窗口机制与对应数据连接，并把新增方法定位为可用基线；报告在指定数据上的提升，同时以 competitive 描述其他数据。实验预览将已经由先导实验回答的容量问题与后续正式比较分开。可借鉴范围明确的收益叙述与避免重复实验；尚未读取其完整限制章节，不能推断如何写限制或采纳了哪些审稿意见。

## 使用方式

先挑与当前研究问题相近的机制与评估做法，再判断是否需要新的实验。完整读取支持章节级分析，部分读取只支持已见片段；搜索索引可核实发表元数据，却不等于下载了正式全文。上述出版商直接 GET 返回 403 的访问记录应保留，不能由作者稿可读改写成出版社全文可读。

不要根据这七篇推断期刊偏好某一算法、固定篇幅、固定图数、某种配色或录用概率。比较不同论文时先统一版本、任务、监督和预算，再选择真正相关的引用。
