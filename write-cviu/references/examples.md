# CVIU 已发表样本与可迁移观察

核验日期：2026-11-06。五篇均核实正式发表；实际阅读范围分别是一个正式排版机构存档、两个作者稿全文和两个出版社索引摘录。全文阅读与正式出版元数据是不同证据。以下经验是本技能的研究判断，不是 CVIU 录用规则；不附第三方全文或原图。

## Gaussian 表示的控制位置

**Gaussian Splatting with NeRF-based color and opacity**，CVIU 251 (2025), 104273；DOI 10.1016/j.cviu.2024.104273。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314224003540)；[作者 v5 全文](https://arxiv.org/html/2312.13729v5)。

观察定位：作者稿 §3、Fig.2 解释新增网络控制什么；§4 的设计替代与时间表让质量和开销共同可判断；§5 集中说明范围。迁移时明确自己的控制输入、输出和代价。作者稿早于正式版，表号和实验范围有变化；不能把“开销轻微”等措辞当作未经数字核对的模板。

## 结构主张配结构测量

**View consistency aware holistic triangulation for 3D human pose estimation**，CVIU 236 (2023), 103830；DOI 10.1016/j.cviu.2023.103830。[作者机构页](https://cvl.sjtu.edu.cn/getpaper/1100)；[正式排版机构存档](https://cvl.sjtu.edu.cn/Upload/Paper/View%20Consistency%20Aware%20Holistic%20Triangulation%20for%203D%20Human%20Pose%20Estimation.pdf)。

已读完整九页。§3 定义中间量与结构依赖；§4.2 同时评估位置和姿态合理性；Table 3 展示准确率与成本；§4.4 的对照分别对应设计选择，§4.5 集中写条件限制。迁移原则是测量中心主张本身。其多视角骨架指标不能未经重新定义就充当单目渲染指标；已发表表注也需独立校核。

## 最终图像分数与中间变量分开

**NeRFtrinsic Four: An end-to-end trainable NeRF jointly optimizing diverse intrinsic and extrinsic camera parameters**，CVIU 249 (2024), 104206；DOI 10.1016/j.cviu.2024.104206。[正式发表页](https://www.sciencedirect.com/science/article/pii/S107731422400287X)；[作者 v4 全文](https://arxiv.org/html/2303.09412v4)。

观察定位：作者稿 §4.2 区分图像质量与相机误差，§4.6 测试设计选择与输入减少，§5 讨论外观分数和结构错误可能并存。迁移时为几何、语义或校准主张设置直接证据。2023 作者稿与 2024 正式版的 360° 扩展及初始化条件不同，不能混写；也不照搬其特定重复实验的择优聚合方式。

## 近题定位：细节与 primitive 分配

**FSA-GS: Fine-Structure-Aware Gaussian Splatting for sparse-view novel view synthesis**，CVIU 271 (2026), 104892；DOI 10.1016/j.cviu.2026.104892。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314226002596)。

只读到出版社索引中的摘要、引言和部分章节。可观察其把细节问题对应到 primitive 分配与保留操作。适合借鉴题名、任务条件和问题—机制定位；不能据此断言全文消融、成本或图表规范。稀疏视角静态场景与动态人体并非同一比较协议。

## 近题定位：困难输入的具体化

**Towards robust 3D human reconstruction with uncertainty-aware low-rank adaptation**，CVIU 269 (2026), 104813；DOI 10.1016/j.cviu.2026.104813。[正式发表页](https://www.sciencedirect.com/science/article/pii/S1077314226001803)。

只读到出版社摘要、Highlights 和引言。其问题定位从具体输入退化进入适配与融合机制。可迁移的是先定义“困难”再设计验证；不能由标题借来鲁棒性结论，也不能把单图人体形状恢复与视频人体渲染混为一项任务。

## 使用方式

先挑与当前研究问题相近的机制与评估做法，再判断是否需要新的实验。完整读取支持章节级分析，部分读取只支持已见片段；搜索索引可核实发表元数据，却不等于下载了正式全文。上述出版商直接 GET 返回 403 的访问记录应保留，不能由作者稿可读改写成出版社全文可读。

不要根据这五篇推断期刊偏好某一算法、固定篇幅、固定图数、某种配色或录用概率。比较不同论文时先统一版本、任务、监督和预算，再选择真正相关的引用。
