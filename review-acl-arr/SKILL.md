---
name: "review-acl-arr"
description: "Simulated ACL Rolling Review (ARR / ACL / EMNLP / NAACL) OpenReview Program Committee & Area Chair final review protocol. Tailored to ARR's decoupled Soundness (1-5) and Excitement (1-5) rubric, strict 8-page main body + unlimited uncounted Limitations & Ethical Considerations sections, Responsible NLP Research Checklist, multi-family leave-one-family-out judge agreement (Fleiss' kappa), exact paired McNemar & 10K paired bootstrap 95% CIs, transparent prompt-token & API-dollar accounting, Decimal ROUND_HALF_UP precision reconciliation, contamination hygiene, and 180 DPI ACL two-column visual checks. Use alongside write-acl-arr."
---

# Simulated ACL Rolling Review (ARR) PC & Area Chair Review (`review-acl-arr`)

Use after `write-acl-arr` and before OpenReview submission to **ACL Rolling Review (ARR)** for commitment to ACL, EMNLP, or NAACL.

## 1. Official Desk-Reject & ARR Format Gate (0 Tolerance)

- **Template & Strict 8-Page Cap**: Official `acl.sty` + `acl_natbib.bst` (bundled flat at project root for Overleaf), **strictly <= 8.0 pages main body** (long paper; `References` start cleanly after page 8).
- **Mandatory Dedicated Sections (Uncounted After Page 8)**:
  - **`Limitations` (Mandatory)**: Missing `Limitations` is a desk-reject / severe review penalty in ARR. Must address substantive methodological & empirical boundaries (trade-offs, theoretical assumptions/clock or distribution drift, domain/language scope, and API model snapshot reproducibility)—never empty boilerplate.
  - **`Ethical Considerations` (Recommended / Mandatory if applicable)**: Evaluated strictly against the **ACL Code of Ethics** and **Responsible NLP Research Checklist** (privacy, dual-use, PII/de-identification, bias, environmental/compute transparency).
- **Double-Blind Anonymization**: Zero author names, affiliations, personal GitHub links, identifying acknowledgements, or PDF `/Author` metadata leaks.
- **Native ACL Style**: Crisp natural-prose closing sentences per experiment subsection—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes.

## 2. Independent 3-Lens ARR Panel + Area Chair Meta-Review

ARR explicitly decouples **Soundness (1–5, objective scientific rigor)** from **Excitement (1–5, subjective interest & community impact)**. Main Conference requires BOTH strong Soundness (`>= 4.0`) and compelling Excitement; low Soundness sinks a paper regardless of excitement.

1. **R1 — NLP Methodology, Formal Soundness & Data Hygiene Referee**:
   - Verifies clean problem abstraction (`Problem -> Gap -> Mechanism -> Guarantee/Evidence`) and checks whether claims strictly match measured evidence.
   - Audits **Contamination Hygiene**: clearly separates proprietary/post-cutoff evaluation snapshots (zero pretraining contamination) from independent public stress benchmarks; rejects circular template overfitting.
   - Checks **Error Taxonomy & Qualitative Case Analysis**: demands concrete failure categories with real examples rather than aggregate scores alone.
2. **R2 — Statistical Rigor, Multi-Family Judges & Cost Transparency Referee**:
   - Enforces **Leave-One-Family-Out / Multi-Family Judge Agreement**: flags single-model LLM-as-a-judge or single-auditor validation as a Soundness vulnerability; requires `>= 3` independent model families on a stratified audit sample reporting exact verdict agreement and **Fleiss' $\kappa$** (or human Cohen's $\kappa$).
   - Enforces **Paired Statistical Testing**: demands exact two-sided **McNemar's test** `(b vs c, p-value)` for paired binary outcomes AND **10,000-resample paired bootstrap 95% CIs** for continuous/utility deltas (not raw mean differences).
   - Enforces **Prompt-Token & Dollar Cost Accounting**: when comparing against prompting/self-verification baselines, demands explicit average input/output token inflation (`+Tok`, `%`), API dollar cost at list prices, and CPU/wall-clock latency.
   - Runs **100% Claim-to-JSON Reconciliation** using explicit `Decimal(..., ROUND_HALF_UP)` to eliminate IEEE-754 half-to-even `.x5` `0.1 pp` drift across prose, figure labels, tables, and JSON outputs.
3. **R3 — Outside-Area NLP Generalist, Responsible Checklist & 180 DPI Typography Referee**:
   - Inspects every rendered page at **180 DPI PNG** for wrapped two-column equation numbers `(k)`, narrow-column whitespace rivers caused by long `\texttt{...}` model identifiers, squeezed architecture diagram sub-cards, legend overlaps, and float drift (`|\Delta p| > 1`).
   - Audits `figure_formula_consistency_audit.py` so mathematical notation in plotting scripts (`c_1,\dots,c_m`, `\kappa(c)`) matches `main.tex` character-for-character.
   - Audits the **Responsible NLP Research Checklist** and cleanroom `/tmp` artifact execution (`run_all.sh` exit 0, zero local paths or secrets).
4. **Area Chair Meta-Review**:
   - Anchors recommendation (Main Conference vs. Findings vs. Resubmit) squarely on agreed **Soundness** first, then **Excitement**; produces prioritized **Blocking / Major / Minor** surgical fixes before submission.

## 3. Top-8 ACL ARR Rejection Triggers (Symptom -> Reviewer Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical ARR Reviewer Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Single-model LLM judge / auditor bias** | "Using one LLM family to judge outputs risks self-preference and lowers Soundness to 2.5." | Run a stratified multi-family audit across `>= 3` independent model families (plus human audit where feasible) and report exact agreement + Fleiss' $\kappa$. |
| **T2** | **No paired significance tests on moderate $N$** | "Gains on ~150–300 paired items lack significance tests; improvements could be sampling noise." | Report exact paired discordant counts `(b vs c)`, two-sided McNemar $p$-values, and 10K paired bootstrap 95% CIs for utility/accuracy deltas. |
| **T3** | **Hidden prompt-token inflation & API costs** | "You claim cheaper verification than self-critique prompts, but omit token counts and dollar costs." | Measure and tabulate exact prompt/completion token overhead (`+Tok`, `%`), `$0.00` vs. API dollar cost, and millisecond latency in both main evaluation and Appendix tables. |
| **T4** | **IEEE-754 `.x5` `0.1 pp` drift across text/tables/figs** | "Table 3 prints `56.2` while Figure 4 prints `56.3`, and `Util = Cov - \gamma HCR` is off by 0.1." | Switch all table, figure, and assertion generators to `Decimal(..., ROUND_HALF_UP)` and verify 100.0% exact string parity against `results/*.json`. |
| **T5** | **Missing or superficial `Limitations` / Contamination note** | "Limitations is a generic two-line disclaimer; unclear whether public benchmarks leaked into pretraining." | Write a crisp 4-dimension `Limitations` section (trade-offs, assumption/drift boundaries, generalization scope, model snapshot reproducibility) + explicit `Contamination Hygiene` paragraph in Experimental Setup. |
| **T6** | **No qualitative Error Taxonomy** | "Paper reports aggregate scores without explaining *why* residual errors happen." | Add a compact error taxonomy table with percentages and 2–3 concrete illustrative cases showing exact residual failure modes. |
| **T7** | **Figure-vs-prose symbol drift** | "Figure 1 uses `c_i` and `\kappa(c_i)` whereas Section 3 defines `c_1,\dots,c_m` and `\kappa(c)`." | Gate every release with `figure_formula_consistency_audit.py` and re-render vector figures from unified notation constants. |
| **T8** | **Two-column ACL 180 DPI typography flaws** | "Equation tags wrap onto blank lines; `\texttt{Model-Name}` creates ugly whitespace rivers; exceeds 8 pages." | Pull wrapped `(k)` tags back inline via compact spacing/`&` shift, set model names in upright roman text instead of `\texttt{}`, adjust nested diagram card padding, and verify strict `<= 8.0` body pages at 180 DPI. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **`Decimal(..., ROUND_HALF_UP)` Four-Way Parity Sweep**: Audit prose, figure bar/point labels, LaTeX tables, and JSON files together after unifying rounding—eliminating every `.x5` `0.1 pp` discrepancy and closing derived-metric identities (`Util = Cov - \gamma \cdot \text{Err}`) exactly.
2. **3-Family Cross-Auditor Consensus Block**: Even when primary evaluation uses deterministic or hybrid scoring, backing up claim/classification extraction with a 3-family stratified consensus audit (`Fleiss' \kappa`) immediately upgrades ARR Soundness from 3.5 to 4.5+.
3. **Paired Discordant Counts `(b vs c)` Alongside Bootstrap CIs**: Showing exact `10 vs 0` or `97 vs 0` McNemar discordant pairs makes improvement robustness unmistakable in a 5-minute AC scan.
4. **Explicit `+Tok` Column in Baseline Comparisons**: Adding a single `+Tok` (and `$` cost) column exposes hidden 200%+ prompt inflation in self-verification baselines while spotlighting `0` extra tokens for deterministic/external guards.
5. **Upright Roman Model Names in Narrow ACL Columns**: Replacing `\texttt{Long-Model-Identifier}` with clean roman text (`Long-Model-Identifier`) eliminates justified-column whitespace rivers and subtle `Overfull \hbox` warnings.
6. **180 DPI Equation-Tag Inline Check**: Inspect every numbered equation (`Eq. (1)–(N)`) on rendered PNGs to ensure zero `(k)` tags wrap onto a trailing blank line in ACL's tight 3.0-inch column width.
7. **Self-Contained Overleaf Bundle + Cleanroom `/tmp` Verification**: Confirm `acl.sty` and `acl_natbib.bst` live flat beside `main.tex`, compile cleanly in `/tmp` (`<= 8.0` body pages), and run `bash run_all.sh` inside `/tmp` confirming `0` local paths, `0` secrets, and verbatim reproduction of all tables and figures.

## 5. Final Sign-Off Checklist
- [ ] `acl.sty` + `acl_natbib.bst`, strictly `<= 8.0` body pages, mandatory `Limitations` & `Ethical Considerations` present, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] 3-lens ARR review (Soundness & Excitement) + AC meta-review completed with all Blocking/Major items resolved at root cause.
- [ ] Multi-family audit (`Fleiss' \kappa`), paired McNemar & 10K bootstrap 95% CIs, and `+Tok` / API-cost accounting verified against `results/*.json`.
- [ ] `Decimal(..., ROUND_HALF_UP)` four-way parity (`prose == tables == figures == JSON`) verified with `0` discrepancies.
- [ ] 180 DPI visual proofread passed (`0` wrapped equation tags, `0` `\texttt{}` whitespace rivers, `0` diagram overlaps, `0` non-ACL `\textbf{Takeaway.}` stamps).
- [ ] Cleanroom `/tmp` run of `reviewer_repo/run_all.sh` passes (`exit 0`) with `0` identity/path/secret leaks.
