# Observed Information Systems papers (data quality, cleaning, ER, experimental studies)

Collected 2026-10-21. All DOIs carry the Information Systems prefix 10.1016/j.is. Full texts were read from arXiv or author-hosted copies because ScienceDirect blocks automated access; "metadata only" means the title, venue and abstract were seen but not the body.

| ID | Paper | Vol / year | Text used | DOI |
|---|---|---|---|---|
| A | Mohammed, Budach, Feuerpfeil, Ihde, Nathansen, Noack, Patzlaff, Naumann, Harmouch. The effects of data quality on machine learning performance on tabular data | 132 / 2025, 102549 | arXiv 2207.14529v6 (about 70%) | 10.1016/j.is.2025.102549 |
| B | Papadakis et al. Three-dimensional entity resolution with JedAI | 93 / 2020 | authors' PDF, full | 10.1016/j.is.2020.101565 |
| C | Mandilaras, Papadakis et al. Reproducible experiments on three-dimensional entity resolution with JedAI | 102 / 2021, 101830 | authors' PDF | 10.1016/j.is.2021.101830 |
| D | Huang, Milani, Chiang. Privacy-aware data cleaning-as-a-service | 94 / 2020 | arXiv 2008.00368 | 10.1016/j.is.2020.101608 |
| E | Simonini et al. Scaling entity resolution: a loosely schema-aware approach | 83 / 2019 | postprint | 10.1016/j.is.2019.03.006 |
| F | Data Lakehouse: A survey and experimental study | 127 / 2024 | metadata only | 10.1016/j.is.2024.102460 |
| G | CrossER: A robust and adaptable generalized entity resolution framework | 135 / 2025 | metadata only | 10.1016/j.is.2025.102609 |
| H | Astappiev et al. SMBench: No-code benchmarking of learning-based entity matching | 139 / 2026 | metadata only | 10.1016/j.is.2026.102711 |
| I | Giovanelli et al. Reproducible experiments for generating pre-processing pipelines for AutoETL | 120 / 2024 | metadata only | 10.1016/j.is.2023.102314 |
| J | TREATS: Fairness-aware entity resolution over streaming data | 129 / 2025 | metadata only | 10.1016/j.is.2024.102506 |

Related editorial: Chirigati, Capone, Rampin, Freire, Shasha. A collaborative approach to computational reproducibility. Inf. Syst. 59 (2016) 95–97, doi:10.1016/j.is.2016.03.002 (check author order against the journal).

## Observations
**Titles.** 6–12 words. Study papers (A, F) name the object and the finding without a coined name; system papers put the system name first with a colon (G, H, J, E-style). Subtitles after a colon are common (F, G, H, J).

**Abstracts.** 7–11 sentences. A: context, problem, example, requirement, aim with counts ("six data quality dimensions", "19 algorithms"), design ("three scenarios"), outline; no result decimals. D and E: no numbers. B: about 260 words with an inline list and artifact URLs. C (reproducibility paper): about 165 words.

**Introductions.** A: ten paragraphs ending in a run-in "Contributions." label with four bullets and an outline. E: eleven paragraphs with a worked example and five noun-phrase contribution bullets ("an approach to ...", "the evaluation of our approach on seven real-world datasets"). D: four numbered contributions starting "We extend / We re-define / We evaluate". B: three bullets after "In summary, this work makes the following contributions:".

**Sections.** A: Data quality and AI, Related work, Data quality dimensions and pollution (one subsection per dimension), ML tasks, Experimental setup (hardware, implementation, datasets, parameters), Results (one subsection per task), discussion, conclusion. D: preliminaries ... Experiments (setup, then one subsection per question) ... Related work, Conclusions. The journal's reproducibility guidelines prescribe Introduction, Software, Reproducibility protocol, datasets and experiments, Extending, optional Discussion, Conclusions, with hardware, running times, verified and failed environments and known limitations.

**Results paragraphs** open with an action or a figure: "We compare SafeClean to PrivateClean ..." (D), "Figure 11 shows ..." (E), "Looking into Table 4(b), we observe that ..." (B); they close with "Overall, we can conclude that ..." (B). Bold run-in labels ("Completeness.", "Scalability analysis.") are used in A and B.

**Limitations.** No separate section in A, B, D or E. A states scope in the introduction ("we limit our experiments to ..."); D states each limitation where it applies; future work is a short list in the conclusions. None stacks caveats.

**Captions.** Mostly noun phrases of 5–20 words ("F1-scores of the classification algorithms for completeness.", "Framework overview."). Longer captions only define abbreviations. Table captions above tables.

**References.** Numbered brackets, often with names ("Foroni et al. [21]"). B has 86 references, dominated by PVLDB/VLDB, SIGMOD, ICDE, EDBT, TKDE and KDD; C has 27. Footnotes carry URLs and side remarks (22 in E, 14 in C, 2 in A).

**Register (body text).**
| Paper | Mean sentence length | >35 words | ( per 100 w | ; per 100 w | hedges per 100 w |
|---|---|---|---|---|---|
| B (measured, full) | 25.4 | 17% | 1.45 | 0.10 | 0.10 |
| A intro (estimate) | ~24 | ~15% | ~1.0 | ~0.44 | low |
| D intro (estimate) | ~30 | ~29% | ~0.6 | ~0.1 | low |
| E intro (estimate) | ~20 | ~7% | ~1.7 | ~0.5 | low |
| C body (estimate) | ~20 | ~4% | ~1.0 | ~0.2 | low |

**Vocabulary.** System papers (B, E) use some promotional words ("seamlessly", "leverage", "novel"); the empirical study (A) is plain. No em dashes appear in the five full texts. Established field vocabulary is used; new terms are defined once in a preliminaries section.

## Case study: what changed when a DKE-desk-rejected audit paper was rewritten for IS (2026-10)
Original register: mean sentence 15.7 words, 1% over 35 words, 0.90 semicolons and 1.71 negations per 100 words, about 40 uses of private nouns such as "authority", "obligation" and "contract", internal codes (P19, v5, v7, version-3) and a "Recent DKE studies" paragraph. The rewrite merged short sentences, moved related work forward and anchored it in PVLDB/SIGMOD/ICDE evaluation studies, stated each caveat once, removed codes and journal traces, and kept every number and table.
