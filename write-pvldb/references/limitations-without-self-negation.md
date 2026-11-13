# Limitations without self-negation — evidence pointer

This file does **not** reproduce official PDF body text (copyright). It points at the corpora already read, and restates counts and rules.

## Corpora (full-text reads)

1. Ten accepted algorithm papers (ICDE 2025–2027 R1, TKDE 2022, VLDB Journal 2019, PVLDB 14(5) 2021 HCM, PVLDB 18(3) 2024/25 AADS, SIGMOD 2023 Star). Notes: `write-icde/references/limitations-writing.md`. Official PVLDB PDFs at vldb.org (HCM p757; AADS p623).
2. Sixteen accepted EAB papers (ICDE 2024–2027 R1 and PVLDB EA&B), including DCO, RLESI, XRAG, TS-Fault, SQLMorph, HCT-QA, CITBench, RDL-Bench, Text2VectorSQL, and PVLDB neighbours such as SemBench and Dawn of NL2SQL. Notes: `write-icde/references/limitations-writing-eab.md` and `experiment-analysis-writing/references/pvldb-sample-2023-2026.md`.
3. Caching / view-reuse / access-control and AQP papers: `write-icde/references/limitations-writing-caching-access.md`, `limitations-writing-aqp.md`.

## Counts used in write-pvldb §7

- Abstract states a loss of the authors' own method: 0/10 (algorithm). Benchmark limits in the abstract: 0/9 EAB.
- Conclusion lists own losses or own-benchmark limits: 0/10 and 0/9.
- Dedicated “where we fail” about the authors' method: 0/10.
- “limitation(s)” about the authors' own benchmark: 0/9.
- Typical treatment of one negative result: 1–4 sentences, once, next to the number; fact → mechanism → regime → bound.
- Labelled Threats about the benchmark: 1/9, ≈110 words (TS-Fault).
- Inter-annotator agreement reported: 0/4 in EAB Part B; 0/4 apologise for not collecting it.
- Vocabulary never used about the authors' own method/benchmark: “does not help”, “fails”, “the advantage vanishes”, “bug”, “rerun”, “mistake”, “unfortunately”, “we report rather than paper over”.

## Integrity boundary

Rules change wording, placement and frequency only. Measured numbers, losing cells, and facts a reviewer needs to judge validity stay.

Checked: 2026-11-12 PT. If a new official paper is added to the corpus, update the counts; do not invent quotations.
