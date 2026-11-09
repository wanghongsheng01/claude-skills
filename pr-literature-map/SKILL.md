---
name: pr-literature-map
description: Build an auditable publication landscape for Elsevier Pattern Recognition, separating scientific problems, application tasks and methods before choosing a research direction.
---

# Pattern Recognition publication landscape

Use this for venue learning or a literature landscape, before proposing new ideas. Target *Pattern Recognition*, ISSN 0031-3203, not *Pattern Recognition Letters* or similarly named proceedings.

For the observed 2026-11-09 landscape, read [the frozen corpus findings and limits](references/README.md). The bundle contains 3,846 public metadata rows, the title rules and provenance. Run `python3 references/audit_title_map.py` from this skill folder to replay its classification offline. A successful replay establishes consistency with the frozen rules, not semantic accuracy or acceptance preference.

## Corpus and time

Use DataHub's matching source module where configured; map sources with `datahub list`. Collect publisher-deposited DOI metadata and publisher records. Keep publication dates distinct from indexing/deposit dates. State the exact cutoff, timezone, window and treatment of online-first versus issue assignment. A month-only date does not prove availability on a particular day. Report incomplete years separately and test the effect of the ambiguous final month and a rolling window.

Keep DOI, title, venue/ISSN, year/volume, article type, date fields, provenance and exclusion reason. Exclude editorial boards, corrections and retractions from research-topic denominators, while retaining their audit rows. Missing volume or unavailable full text is a separate status. Never treat a preprint as a journal publication without a verified journal identity link.

A future issue date or missing volume does not establish that an article is unpublished. If the publisher confirms a Version of Record online by the cutoff, include it in a separate online-first cohort, record the exact online date, and deduplicate by DOI when combining cohorts. Publisher acceptance and a preprint upload are distinct from verified VoR publication. When online dates are absent, describe the result as an issue-date metadata cohort rather than all formally published articles available by the cutoff.

## Classify the problem before the method

Use three independent axes:

- **Task/domain:** recognition, segmentation, retrieval, clustering, anomaly detection, medical imaging, remote sensing, etc.
- **Scientific difficulty:** distribution shift, scarce/noisy supervision, incomplete or conflicting views, class imbalance, uncertainty, scalability, interpretability, etc.
- **Method:** contrastive learning, graph constraints, low-rank factorization, attention, diffusion, causal intervention, prototype learning, etc.

These are examples to adapt to the actual corpus, not a fixed list of claimed top topics. Keep unknown/ambiguous cases. A title may support a task label without supporting a scientific-problem label. Multi-label counts overlap and do not sum to 100%. Do not force one label by dictionary priority and then present the order as a discovery.

If using title rules, save the rules and matched spans. Call this coarse title-based tagging; audit a deterministic, stratified sample including unknowns and boundary terms. Report coverage and observed error, and avoid precision estimates unsupported by enough independent labels. Do not call this exhaustive manual reading.

## Interpretation and next reading

Rank only what the evidence measures. Published share is not acceptance probability: submissions and rejected papers are not observed. Large growth can reflect publishing volume, date indexing or a special issue. Compare yearly shares as well as counts and disclose the partial-year denominator.

For each frequently observed scientific problem, select contrasting full-text papers across years, methods and evidence designs. Include counterexamples and limitations, rather than only widely cited or open-access success cases. Keep a full-text retrieval log and explain selection bias. Route the resulting papers to `pr-evidence-reading`.

Deliver the corpus CSV/JSON, classification code/rules, exclusions, coverage and sensitivity tables, source list, a Chinese or requested-language synthesis, and a reading shortlist. If the evidence cannot support a ranking of scientific problems, deliver the bounded ranking it does support and the exact missing review work.
