# BigLake: architecture, governance and operational evidence

## Source and reading scope
- SIGMOD 2024 formal publication, DOI: https://doi.org/10.1145/3626246.3653388
- Publication-version course mirror: https://www.cs.cmu.edu/~15721-f24/papers/BigLake.pdf
- Checked 2026-11-18: publication-text and section/figure-structure reading; not sentence-level rhetorical annotation or an independent reproduction. The PDF is a mirror, not an original publisher endpoint; the DOI identifies the publication.
- Observed: 13 pages, 10 figures, 3 SQL listings and 39 references; no standalone experimental section. These are not quotas.

## Observed structure and evidence
Sections 1–2 introduce needs, contributions and architecture; 3 covers table authorization, governance and acceleration; 4 unstructured data and inference; 5 cross-cloud operations; 6 production use cases; 7 concludes.

A TPC-DS comparison uses 10 TB, 2,000 slots and sequential query execution, with approximately fourfold reduction in aggregate runtime. The plotted comparison is a query subset, not proof of a uniform gain across every query. The paper also notes a 2 GB model-size limit and immature early operational tooling.

## Interpretation and proposed transfer
Evidence can accompany architecture and concrete use cases rather than occupy a mandatory chapter. For a candidate industrial system, link each design claim to a performance, governance or operations observation. Preserve workload size, resources, execution protocol and plotted-subset boundaries. Separate supported model/data limits from general capability claims. The chapter arrangement is a useful example, not a reason to omit systematic evaluation.
