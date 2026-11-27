---
name: "review-issta"
description: "Simulated ACM SIGSOFT ISSTA (CCF-A / TH-CPL A) Program Committee final review protocol grounded in the ACM SIGSOFT Empirical Standards, Open Science policy, and Artifact Evaluation criteria. Audits strict 4-axis Threats to Validity (Construct, Internal, External, Conclusion Validity with concrete mitigations), mandatory Data Availability section (smoke test, runtime, script-to-table/figure map), paired nonparametric significance (Wilcoxon + Vargha-Delaney A12 AND exact two-sided McNemar + Cliff's delta over binary fault vectors), LLM error taxonomy & fair thinking-budget disclosure, selective cost-ratio anti-overclaim checks, Decimal ROUND_HALF_UP parity, native framed 'Answer to RQk' boxes, and zero-cache /tmp cleanroom artifact reproduction. Use alongside write-issta."
---

# Simulated ACM SIGSOFT ISSTA Program Committee Review (`review-issta`)

Use after `write-issta` and before submission to **ACM SIGSOFT ISSTA** (International Symposium on Software Testing and Analysis).

## 1. Official Desk-Reject & Empirical Standards Gate (0 Tolerance)

- **Template & Page Cap**: Official ACM `acmart` (ISSTA / PACMSE cycle template, bundling `acmart.cls` and `ACM-Reference-Format.bst` flat for Overleaf), strictly within the cycle's body page cap (e.g., **<= 18.0 pages** excluding references for PACMSE/ISSTA cycles).
- **Mandatory Sections (ISSTA Open Science Policy)**:
  - **Four-Axis `Threats to Validity`**: Must explicitly cover ALL FOUR ACM SIGSOFT Empirical Standards axes—**Construct Validity**, **Internal Validity**, **External Validity**, AND **Conclusion Validity**—each paired with concrete experimental mitigations rather than generic checkbox boilerplate.
  - **`Data Availability` (Immediately Before References)**: Mandatory section linking the anonymous artifact mirror, stating the exact one-command **smoke test** (`bash run_all.sh`), single-core runtime (`~25s`), zero-API-key reproducibility, and explicit script-to-Table/Figure mapping.
- **Native ISSTA Style**: Clean framed **`Answer to RQ1..RQk`** summary boxes (verified verbatim against tables)—**zero** database-engineering `\textbf{Takeaway.}` stamps, double-blind clean, zero AI clichés, zero em-dashes.

## 2. Independent 3-Lens ISSTA PC Panel + PC Chair Meta-Review

1. **R1 — Program Analysis, Specification & Soundness Referee**:
   - Verifies formal semantics, soundness/completeness claims, and exact 1-to-1 correspondence between inference/generation rules and tool implementation.
   - Audits **Operating Regimes vs. Lightweight Static Linters**: checks whether simple AST/regex linters already handle syntactic rules faster and demands an honest counter-backed separation between syntactic/structural checks and cross-module semantic/stateful faults where dynamic/differential testing is indispensable.
2. **R2 — Empirical SE Methodology, Statistical Validity & Artifact Referee**:
   - Enforces **Dual Nonparametric Statistical Rigor**: on small multi-seed runs ($n=5$) where deterministic tools produce zero-variance ties, pairs multi-seed **Wilcoxon + Vargha–Delaney $\hat{A}_{12}$** with **exact two-sided McNemar's test + Cliff's $\delta$** over the full $N$-fault binary detection vector—including every LLM baseline and every ablation variant.
   - Audits **LLM Baseline Fairness & Error Taxonomy**: checks adaptive-thinking token budgets (preventing unfair truncation on reasoning models, with transparent `*` footnote markers) AND requires a **quantitative false-alarm taxonomy** stratified by fault/workflow complexity plus concrete false-negative case studies.
   - Enforces **Anti-Overclaim Cost-Ratio Precision**: if any lightweight/cheap baseline has a lower raw bill than the proposed tool (even with far lower recall), forbids blanket claims like `"X×–Y× lower cost than all baselines"`—must qualify precisely (e.g., `"than the top-two strongest LLMs"`) and state the cheap baseline's cost-recall trade-off honestly.
   - Runs **100% `Decimal(..., ROUND_HALF_UP)` Reconciliation** across Abstract, prose, every **`Answer to RQk` box**, tables, figures, and `results/*.json`.
3. **R3 — Outside-Area SE Generalist, 180 DPI Visual & Zero-Cache AEC Referee**:
   - Inspects every rendered page at **180 DPI PNG** for cross-figure notation/footnote consistency (e.g., `*` markers matching Table 4 across Fig. 2/3/5), readable axis fonts (`8–9 pt`), clean `Answer to RQk` box breaks, and `|\Delta p| \le 1` float proximity.
   - Runs **Zero-Cache Cleanroom `/tmp` Artifact Check**: deletes ALL pre-generated JSONs and figure PDFs inside an isolated `/tmp` copy, runs `bash run_all.sh`, and verifies `exit 0` with identical reproduced numbers and `0` host-path/identity/secret leaks.
4. **PC Chair Meta-Review**:
   - Evaluates against ACM SIGSOFT Empirical Standards (soundness, empirical validity, threats rigor, open science, practical usefulness) and issues Blocking/Major/Minor cures prior to submission.

## 3. Top-8 ISSTA Rejection Triggers (Symptom -> PC Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical ISSTA PC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **3-axis `Threats to Validity` (missing `Conclusion Validity`)** | "Threats omits Conclusion Validity and ignores small-seed ties and LLM stochasticity." | Include all four axes (`Construct`, `Internal`, `External`, `Conclusion Validity`) with explicit statistical & archiving mitigations. |
| **T2** | **Underpowered seed tests / missing LLM & ablation significance** | "Wilcoxon on $n=5$ zero-variance seeds is weak, and LLM/ablation gains lack $p$-values." | Report exact two-sided McNemar $p$-values and Cliff's $\delta$ over full $N$-fault binary vectors for ALL baselines, ALL LLMs, and ALL ablations. |
| **T3** | **Selective cost-ratio overclaim** | "Abstract claims `17.5×–225×` lower cost, yet Table 4 shows one small LLM costs less than your tool." | Qualify precisely (`"than the top-two LLMs"`) and explicitly report the cheaper model's exact bill alongside its recall collapse and FAR spike. |
| **T4** | **No qualitative/quantitative LLM error taxonomy** | "Only aggregate recall/FAR reported; why do LLMs fail so often?" | Stratify raw generated-test logs by fault category/complexity (single-table vs. multi-entity vs. multi-step rollback FAR) and walk through concrete FN cases. |
| **T5** | **Vague `Data Availability` / cache-only artifact** | "Artifact link lacks smoke test runtime or only echoes pre-saved JSONs." | State exact `bash run_all.sh` runtime, zero-API-key mode, and script-to-Table/Figure mapping in `Data Availability`, and verify zero-cache `/tmp` rebuild. |
| **T6** | **IEEE-754 `.x5` & `0.1×` ratio drift across boxes & figs** | "Fig. 2b prints `31.2%` vs. `31.3%` and §6.4 prints `5.6×` instead of `5.7×`." | Enforce `Decimal(..., ROUND_HALF_UP)` across every script, figure label, table cell, and `Answer to RQk` box from unrounded raw JSONs. |
| **T7** | **Unfairly truncated reasoning LLMs / missing `*` markers** | "Did adaptive-thinking models hit token limits? Why does Table 4 have `*` but Fig. 3a doesn't?" | Provision adequate thinking-token headroom, footnote it transparently, and verify `*` marker parity across every table and figure at 180 DPI. |
| **T8** | **Unclear boundary vs. simple static linters** | "Why not just run a fast static AST/regex linter?" | Quantify the exact syntactic vs. cross-module semantic operating regime using measured runtime and AST counters without self-negation. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Four-Axis Empirical Standards Check**: Verify `Construct`, `Internal`, `External`, and `Conclusion Validity` ALL exist as dedicated paragraphs with explicit mitigations.
2. **Full-Vector Exact McNemar + Cliff's $\delta$ Script**: Add a compact standalone script computing exact McNemar $p$-values and Cliff's $\delta$ over the $N$-fault binary outcome matrix for every baseline, LLM family, and ablation.
3. **Cost-Claim Boundary Audit**: Sort Table 4 by API cost ascending; if ANY baseline sits below the proposed tool's cost, tighten every cost-reduction claim in Abstract, Intro, and `Answer to RQk` boxes to specify the exact comparison group.
4. **Quantitative Fault-Category FAR Breakdown + Concrete FN IDs**: Extract per-category false-alarm rates from raw generated tests and cite 2–3 concrete false-negative fault IDs in prose.
5. **Actionable `Data Availability` Block**: Include exact smoke-test command, single-core execution time, zero-secret/zero-API-key guarantee, and 1-to-1 script → Table/Figure table.
6. **Footnote-Marker (`*`) Cross-Figure Audit at 180 DPI**: Check that every special-budget or model-variant marker (`*`, `†`) appears identically in all tables AND all figure legends/ticks.
7. **Wipe-Before-Run `/tmp` Cleanroom Test**: Delete all pre-built JSONs and `figures/` inside `/tmp` before running `bash run_all.sh` to guarantee genuine from-scratch reproducibility.

## 5. Final Sign-Off Checklist
- [ ] Official ACM `acmart`, strictly within body page limit, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`, `0%` un-upgraded arXiv citations.
- [ ] All 4 `Threats to Validity` axes (incl. `Conclusion Validity`) and actionable `Data Availability` section present.
- [ ] Dual nonparametric testing (Wilcoxon/$\hat{A}_{12}$ + exact McNemar/Cliff's $\delta$) and stratified error taxonomy verified against `results/*.json`.
- [ ] `Decimal(..., ROUND_HALF_UP)` parity across Abstract, prose, all `Answer to RQk` boxes, tables, and figures (`0` selective cost-claim overstatements).
- [ ] 180 DPI visual proofread passed (`0` missing `*` markers, `0` overlaps, `0` non-ISSTA `\textbf{Takeaway.}` stamps).
- [ ] Zero-cache `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
