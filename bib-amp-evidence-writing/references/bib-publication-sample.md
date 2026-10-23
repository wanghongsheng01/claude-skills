# BiB同方向文章篇幅与参考文献调查

核查日期：2026-10-23。按评价研究、生成方法、MIC与实验研究选取6篇；另将1篇综合调查兼benchmark单列，不用其较长参考文献表抬高本稿目标。

参考文献数量指文章末尾编号条目数，不是被其他论文引用次数；所有编号从官方HTML逐条解析，并检查1至N连续。页数独立标注证据等级，不根据HTML字数或搜索摘要猜测。


| 文章 | 年份/研究类型 | 参考文献条目 | 发表篇幅 | 页数核查依据 |
|---|---|---:|---:|---|
| [Benchmarks in antimicrobial peptide prediction are biased due to the selection of negative data](https://academic.oup.com/bib/article/23/5/bbac343/6672903) | 2022；评价研究 | 59 | 12 | 直接读取JCU发表版本PDF，12物理页；Europe PMC JATS page-count=12复核 |
| [Do deep learning models make a difference in the identification of antimicrobial peptides?](https://academic.oup.com/bib/article/23/3/bbac094/6563422) | 2022；评价研究 | 99 | 16 | CICESE作者机构记录报告16页，未获得可本地解析的PDF；不称为PDF实计 |
| [Designing antimicrobial peptides using deep learning and molecular dynamic simulations](https://academic.oup.com/bib/article/24/2/bbad058/7066348) | 2023；生成与湿实验研究 | 65 | 未核实 | 官方PDF本轮403；检索索引显示1–13但不将其当作已核实PDF页数，留待核验 |
| [Diff-AMP: tailored designed antimicrobial peptide framework with all-in-one generation, identification, prediction and optimization](https://academic.oup.com/bib/article/25/2/bbae078/7620508) | 2024；生成方法研究 | 70 | 13 | publisher-deposited JATS counts/page-count=13；未本地解析PDF |
| [TG-CDDPM: text-guided antimicrobial peptides generation based on conditional denoising diffusion probabilistic model](https://academic.oup.com/bib/article/26/1/bbae644/7922577) | 2025；生成方法研究 | 53 | 11 | 直接读取Birmingham发表版本PDF：12物理页减1机构封面=11正式页；JATS复核11 |
| [AI-guided discovery and optimization of antimicrobial peptides through species-aware language model](https://academic.oup.com/bib/article/26/4/bbaf343/8205772) | 2025；MIC预测及湿实验研究 | 52 | 15 | publisher-deposited JATS counts/page-count=15；未本地解析PDF |
| [Comprehensive assessment of machine learning-based methods for predicting antimicrobial peptides](https://academic.oup.com/bib/article/22/5/bbab083/6189771) | 2021；综合调查 + 独立benchmark（单列） | 122 | 22 | 作者Monash机构元数据明确 Number of pages=22 / 1–22；未本地解析PDF |

六篇原始研究/评价研究为52–99条，中位数62条。不能据此推定“BiB必须60篇”。bbab083为122条、22页，其综述范围显著更广，应单列。可核实页数的原始研究为11–16页；它们是出版社最终排版，其他稿件可能是不同投稿排版，不能按页数等同评判研究完整性。

参考文献扩充可优先补足实际使用的方法原始出处（序列比对、VAE、扩散、LSTM、JS和MMD），再补直接回答相邻问题的AMP评价、定量MIC与实验研究。每条新增文献都必须绑定具体句子，不将所有候选集中堆到引言末尾。

限制：bbad058本轮官方PDF读取返回403，未将索引中1–13页作为已完成PDF核查。其65条参考文献由完整官方HTML独立核实。其余页数中两篇实际读取PDF、两篇用publisher-deposited JATS页数字段、两篇用作者机构明确页数元数据；未冒充全部为PDF实计。


本表为有目的选择的七篇相关论文，不是期刊总体的随机样本。用它发现论证覆盖可能缺失的类别，不设置目标引用数量。所有新增引用仍应通过逐条身份、内容支持和正文实际引用核验。
