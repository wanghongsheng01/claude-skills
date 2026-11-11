---
name: "icde-subject-areas"
description: "Choose the CMT 'Subject Areas' (one Primary, a few Secondary) for an IEEE ICDE research or EAB submission from the paper itself. Holds the exact ICDE 2027 CMT subject-area list (29 areas plus 'None Of Above', checked against the CMT form and the CFP topic list on 2026-11-11), selection rules taken from how ICDE assigns reviewers, and a scorer (scripts/suggest_areas.py) that reads the LaTeX sources or the PDF and ranks the areas with the evidence for each. Use whenever a paper is submitted to ICDE or its CMT form is filled (投 ICDE / ICDE 投稿 / CMT 表单 / Subject Areas / Primary Secondary 怎么选 / 选领域 / 选主题领域), also inside the submit-icde workflow."
---

# ICDE subject areas (CMT "Subject Areas*", Primary / Secondary)

The CMT form of the ICDE research track asks for exactly one **Primary** area and any number of **Secondary**
areas from a fixed list. ICDE matches reviewers to papers mainly through these areas (and the reviewers' bids),
so the choice decides who reads the paper. Use with `submit-icde` (whole submission) and `write-icde`.

## Language convention
The CMT form is reviewer-facing: area names are copied verbatim (English). Explanations to the author are in
Chinese (中文), delivered as a document.

## 1. The ICDE 2027 list (verbatim, CMT order)
Checked on 2026-11-11 against screenshots of the ICDE 2027 CMT form and the topic list of
https://icde2027.github.io/cf-research-papers.html (28 CFP topics; CMT adds "Data models, semantics, and query
languages" and "None Of Above"). [CHECK] for later editions: the list changes every year.

| # | Left column | # | Right column |
|---|---|---|---|
| 1 | AI and machine learning for data systems and vice versa | 17 | Explainability, fairness, bias, trust, authentication, and regulatory compliance |
| 2 | Benchmarking, performance modeling, tuning, and testing | 18 | Foundation models and LLMs for data engineering and vice versa |
| 3 | Cloud data management | 19 | Graph data |
| 4 | Data mining with a data-centric focus | 20 | Knowledge graphs for data engineering |
| 5 | Data models, semantics, and query languages | 21 | Multi-modal and heterogeneous data |
| 6 | Data preparation, cleaning, and integration | 22 | Multidimensional data, data warehousing, OLAP, and analytics |
| 7 | Data pricing and markets | 23 | Query processing and optimization |
| 8 | Data quality, curation, provenance, and workflows | 24 | Responsible and ethical data management |
| 9 | Data security and privacy | 25 | Storage, indexing, and physical database design |
| 10 | Data streams, complex event processing, and edge computing | 26 | Time-series, temporal, spatial, and spatio-temporal data |
| 11 | Data systems on modern hardware | 27 | Transaction management, concurrency control, and recovery |
| 12 | Data visualization and interactive data exploration | 28 | Uncertain, probabilistic, and approximate data |
| 13 | Distributed and parallel data management | 29 | Vector data |
| 14 | Distributed ledgers and blockchains | 30 | None Of Above (one box only: Primary; never use it when an area fits) |
| 15 | Domain-specific data engineering (scientific, medical, climate, urban, etc.) |  |  |
| 16 | Energy-efficient data engineering |  |  |

The form lists the areas alphabetically in two columns, each with a Primary and a Secondary box ("None Of Above" has a Primary box only).
`references/areas.md` gives, for each area, what it covers, the signal words the scorer uses, and typical
pairings.

## 2. Rules for choosing
1. **Primary = the community that should judge the main technical contribution**, not the application. Ask: "which
   reviewers would know the closest prior work in my related-work section?" A new index over authorization graphs is
   *Graph data* (or *Storage, indexing, …*), not *Data security and privacy*, if the contribution is the index.
2. **Primary should match the paper's own framing**: the area whose words appear in the title, the abstract and
   the contribution list. If the title says "graph", "vector", "stream", "LLM", the primary is usually that area.
3. **Secondary = 2-3 areas** (rarely 4): the application domain (e.g., security, data cleaning), the technique
   family (e.g., indexing, query processing, approximation), and the system aspect (e.g., distributed,
   transactions) — each only if a section of the paper actually contributes to it. More than four dilutes the
   reviewer match and looks unfocused.
4. **Do not pick an area the paper cannot defend**: a reviewer from that area will look for its standard baselines
   and benchmarks. If the paper has no transactional protocol, do not tick *Transaction management*.
5. **EAB papers**: add *Benchmarking, performance modeling, tuning, and testing* as a secondary (or primary when the
   benchmark itself is the contribution).
6. **LLM-for-data papers**: *Foundation models and LLMs for data engineering and vice versa* is primary only when
   the contribution is about using or serving LLMs; if the LLM is a black-box labeler and the contribution is a
   sampling/estimation method, primary is *Uncertain, probabilistic, and approximate data*, and the LLM area is
   secondary.
7. **Keep the CMT form and the paper consistent**: the scope statement and the keywords should use the same terms
   as the chosen areas.
8. **Never use "None Of Above"** when any area fits; it routes the paper to a generic pool.

## 3. Workflow
1. Run the scorer on the paper folder (LaTeX) or the PDF:
   `python3 scripts/suggest_areas.py <paper_dir_or_pdf> [--top 6] [--eab]`
   It weights title and abstract (x3), keywords/index terms (x3), section and paragraph headings (x2) and the body
   (x1, capped), and prints the ranked areas with the matched words.
2. Apply the rules of section 2 to the ranking: confirm the primary against the contribution list, keep 2-3
   secondaries that a section of the paper supports, drop areas that only match incidental words.
3. Write the answer for the author as a table: Primary (one), Secondary (ticked boxes), one line of reason each, in
   Chinese, and the verbatim English names to tick in CMT.
4. Update the CMT fields file of the submission (primary/secondary lines) so that the form, the scope statement and
   the keywords agree.

## 4. Worked example (AuthZ-Graph, "No Stale Allows", ICDE 2027 R2)
- Scorer: Graph data first; then Storage, indexing, and physical database design; Data security and privacy;
  Transaction management, concurrency control, and recovery (deferral/acknowledgment); Query processing.
- Choice: **Primary** Graph data (the index is a dynamic 2-hop reachability labeling; related work and baselines are
  reachability indexes). **Secondary** Data security and privacy (authorization, deny, revocation); Storage,
  indexing, and physical database design (index maintenance and size); Query processing and optimization (check
  latency, probe/scan choice). Transaction management was not ticked: the deferral rule is about acknowledging
  writes on a replica, but the paper has no transaction protocol or isolation claim.
