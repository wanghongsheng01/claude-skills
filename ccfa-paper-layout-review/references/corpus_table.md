# 校准语料逐篇实测（layoutlint.py --stats-only，2026-11-14）

PVLDB 论文代码 = vldb.org/pvldb/vol17|vol18/<code>.pdf；icde_<id> / arxiv_<id> = arxiv.org/abs/<id>（作者在 comments 注明录用）。

| paper | venue | pages | floats (body) | full-width share | float-only pages | max body hole (non-final page) | last-page imbalance | last-page used |
|---|---|---|---|---|---|---|---|---|
| arxiv_2602.12064 | SIGMOD 2026 (arXiv) | 15 | 17 | 29% | 0 | 0% | 2% | 44% |
| arxiv_2602.23289 | PACMMOD/SIGMOD (arXiv, acmsmall) | 27 | 19 | 0% | 0 | 0% | 0% | 0% |
| arxiv_2603.27775 | SIGMOD Companion 2026 (arXiv) | 14 | 10 | 20% | 0 | 0% | 1% | 13% |
| arxiv_2605.00676 | ICDE 2026 (arXiv, acmsmall) | 15 | 5 | 0% | 0 | 0% | 0% | 0% |
| arxiv_2610.05540 | PACMMOD (arXiv, acmsmall) | 27 | 4 | 0% | 1 | 0% | 0% | 0% |
| icde_2407.11025 | ICDE 2025 (arXiv, IEEEtran) | 14 | 16 | 38% | 0 | 0% | 50% | 49% |
| icde_2409.06148 | ICDE 2025 (arXiv, IEEEtran) | 17 | 24 | 17% | 1 | 32% | 95% | 100% |
| icde_2503.20394 | ICDE 2025 (arXiv, IEEEtran) | 14 | 21 | 38% | 0 | 0% | 0% | 43% |
| icde_2503.21426 | ICDE 2025 (arXiv, IEEEtran) | 14 | 12 | 25% | 1 | 0% | 20% | 20% |
| icde_2504.00328 | ICDE 2025 (arXiv, IEEEtran) | 14 | 18 | 6% | 0 | 0% | 89% | 100% |
| icde_2504.14282 | ICDE 2025 (arXiv, IEEEtran) | 14 | 16 | 31% | 0 | 0% | 15% | 99% |
| icde_2504.15742 | ICDE 2025 (arXiv, IEEEtran) | 14 | 8 | 25% | 0 | 0% | 1% | 20% |
| icde_2505.05738 | ICDE 2025 (arXiv, IEEEtran) | 16 | 17 | 18% | 0 | 100% | 1% | 54% |
| p1-arch | PVLDB 17/18 (proceedings PDF) | 13 | 19 | 26% | 0 | 0% | 2% | 80% |
| p1000-kaminsky | PVLDB 17/18 (proceedings PDF) | 13 | 12 | 17% | 0 | 0% | 1% | 43% |
| p108-yao | PVLDB 17/18 (proceedings PDF) | 9 | 9 | 11% | 0 | 0% | 2% | 96% |
| p1132-gao | PVLDB 17/18 (proceedings PDF) | 14 | 19 | 37% | 0 | 0% | 1% | 46% |
| p117-huang | PVLDB 17/18 (proceedings PDF) | 13 | 16 | 38% | 0 | 0% | 5% | 98% |
| p130-deeds | PVLDB 17/18 (proceedings PDF) | 14 | 17 | 18% | 0 | 0% | 1% | 16% |
| p14-hajidehi | PVLDB 17/18 (proceedings PDF) | 14 | 16 | 25% | 0 | 0% | 1% | 30% |
| p144-wu | PVLDB 17/18 (proceedings PDF) | 14 | 21 | 24% | 0 | 0% | 1% | 30% |
| p158-markakis | PVLDB 17/18 (proceedings PDF) | 15 | 14 | 0% | 0 | 0% | 0% | 100% |
| p173-ai | PVLDB 17/18 (proceedings PDF) | 14 | 20 | 5% | 0 | 0% | 0% | 38% |
| p187-liu | PVLDB 17/18 (proceedings PDF) | 13 | 17 | 18% | 0 | 0% | 1% | 88% |
| p200-chang | PVLDB 17/18 (proceedings PDF) | 13 | 19 | 5% | 0 | 0% | 0% | 92% |
| p213-tang | PVLDB 17/18 (proceedings PDF) | 13 | 14 | 79% | 0 | 0% | 4% | 99% |
| p226-miao | PVLDB 17/18 (proceedings PDF) | 13 | 18 | 17% | 0 | 0% | 2% | 98% |
| p239-cheng | PVLDB 17/18 (proceedings PDF) | 14 | 13 | 69% | 0 | 0% | 2% | 8% |
| p253-hu | PVLDB 17/18 (proceedings PDF) | 12 | 8 | 12% | 0 | 0% | 1% | 35% |
| p265-kieu | PVLDB 17/18 (proceedings PDF) | 14 | 20 | 25% | 0 | 0% | 0% | 27% |
| p279-lee | PVLDB 17/18 (proceedings PDF) | 14 | 24 | 4% | 0 | 0% | 3% | 36% |
| p28-moerkotte | PVLDB 17/18 (proceedings PDF) | 14 | 7 | 0% | 0 | 0% | 0% | 26% |
| p293-merkel | PVLDB 17/18 (proceedings PDF) | 15 | 16 | 31% | 0 | 0% | 0% | 6% |
| p3035-shankar | PVLDB 17/18 (proceedings PDF) | 14 | 10 | 40% | 0 | 0% | 0% | 20% |
| p308-xie | PVLDB 17/18 (proceedings PDF) | 14 | 12 | 25% | 0 | 0% | 0% | 21% |
| p3694-saxena | PVLDB 17/18 (proceedings PDF) | 13 | 21 | 19% | 0 | 0% | 1% | 73% |
| p3759-shi | PVLDB 17/18 (proceedings PDF) | 13 | 18 | 28% | 0 | 0% | 0% | 98% |
| p3869-chen | PVLDB 17/18 (proceedings PDF) | 14 | 16 | 19% | 0 | 0% | 0% | 77% |
| p3947-bu | PVLDB 17/18 (proceedings PDF) | 13 | 14 | 29% | 1 | 0% | 2% | 91% |
| p4144-schmidt | PVLDB 17/18 (proceedings PDF) | 14 | 19 | 11% | 0 | 0% | 1% | 40% |
| p4159-okolnychyi | PVLDB 17/18 (proceedings PDF) | 14 | 15 | 20% | 0 | 18% | 0% | 27% |
| p4173-shankar | PVLDB 17/18 (proceedings PDF) | 14 | 12 | 17% | 0 | 0% | 0% | 38% |
| p42-jiang | PVLDB 17/18 (proceedings PDF) | 11 | 17 | 12% | 0 | 0% | 1% | 5% |
| p4353-chen | PVLDB 17/18 (proceedings PDF) | 4 | 4 | 25% | 0 | 0% | 1% | 100% |
| p4817-karpathiotakis | PVLDB 17/18 (proceedings PDF) | 14 | 4 | 25% | 0 | 0% | 0% | 54% |
| p4860-xie | PVLDB 17/18 (proceedings PDF) | 14 | 13 | 23% | 0 | 0% | 0% | 88% |
| p4887-yang | PVLDB 17/18 (proceedings PDF) | 9 | 3 | 67% | 0 | 0% | 1% | 51% |
| p5126-bress | PVLDB 17/18 (proceedings PDF) | 13 | 30 | 3% | 0 | 0% | 0% | 96% |
| p5139-zhou | PVLDB 17/18 (proceedings PDF) | 14 | 6 | 33% | 0 | 0% | 1% | 24% |
| p5153-zhou | PVLDB 17/18 (proceedings PDF) | 13 | 5 | 0% | 0 | 0% | 1% | 92% |
| p5259-emani | PVLDB 17/18 (proceedings PDF) | 4 | 1 | 0% | 0 | 0% | 4% | 99% |
| p53-yuan | PVLDB 17/18 (proceedings PDF) | 13 | 19 | 26% | 0 | 0% | 0% | 92% |
| p66-yu | PVLDB 17/18 (proceedings PDF) | 14 | 21 | 0% | 0 | 0% | 1% | 54% |
| p80-zhou | PVLDB 17/18 (proceedings PDF) | 13 | 18 | 50% | 0 | 0% | 4% | 95% |
| p93-chen | PVLDB 17/18 (proceedings PDF) | 15 | 20 | 30% | 0 | 0% | 4% | 4% |
