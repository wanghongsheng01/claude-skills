---
name: "review-icde-industrial"
description: "Simulated IEEE ICDE Industry & Applications Track program-committee final review protocol. Tailored to the single-blind industrial track (practitioner + applied-academic PC, 12-page hard cap with zero appendix, mandatory AI-Generated Content Acknowledgement, no revision round in ICDE 2027). Audits production deployment credibility, formal-in-industrial soundness (including out-of-band state/schema drift vs. version-fenced caches), strongest-safe same-catalog baselines, standalone public-benchmark validity, amortization crossover q*, 180 DPI visual typography, and S01-S11 results presentation. Use alongside review-icde, write-icde-industrial, and paper-presubmission-review."
---

# Simulated IEEE ICDE Industry & Applications Track PC Review (`review-icde-industrial`)

Use after `write-icde-industrial` and before final submission to the **IEEE ICDE Industry & Applications Track** (complements `review-icde`, which targets the Research and EAB tracks).

## 1. Official Desk-Reject & Track Compliance Gate (0 Tolerance)

- **Template & Page Cap**: `\documentclass[conference]{IEEEtran}`, **strictly <= 12 pages** including references (verify against the exact cycle's Industry CFP), **strictly 0 pages of Appendix** (no appendix allowed; all proofs/algorithms supporting claims must live concisely inline).
- **Single-Blind & Authorship**: Single-blind review; verify `>= 1` non-academic industry co-author and realistic industrial affiliation context without turning the paper into a product brochure.
- **Mandatory Sections & Portal Limits**:
  - Unnumbered **AI-Generated Content Acknowledgement** immediately before References (required by IEEE ICDE 2027).
  - Plain-text CMT Abstract strictly **<= 2,000 characters** (sweet spot **180–220 words**), stripped of LaTeX macros, zero self-negating disclaimers.
  - Artifact URL must be a **neutral, non-tracking public mirror** (never a personal webpage with analytics/tracking), with cleanroom runnable scripts matching every reported table number.
  - Zero hollow trailing QED `□` boxes in narrow IEEEtran columns (`\renewcommand{\IEEEQED}{}`), zero `Overfull \hbox`, zero Type 3 fonts.

## 2. Independent 3-Lens Industrial PC Panel + Senior PC Meta-Review

Never review with author bias. Assemble three distinct lenses from the actual ICDE Industry PC composition (cloud/data-platform architects from Meta/Databricks/AWS/Google/IBM + applied DB researchers):

1. **R1 — Industrial Systems Architect & Formal Soundness Referee**:
   - Tests whether the paper delivers a **genuine architectural/algorithmic contribution** rather than a marketing overview or ad-hoc glue script.
   - Scrutinizes every formal definition, algorithm, and inline `IEEEproof` for **edge cases and out-of-band state mutations** (e.g., direct warehouse DDL `ALTER TABLE` bypassing a control-plane revision counter, clock skew, partial failures, multi-tenant isolation boundaries).
   - Audits **production rollout realism**: shadow-audit / dual-run migration path, operational failure modes, and transferable **Lessons Learned**.
2. **R2 — Empirical Methodology, Baselines & Reproducibility Referee**:
   - Performs **100% Claim-to-JSON reconciliation**: every number, speedup, percentage, latency, and sample size in Abstract, Intro, RQs, captions, and Operating Regimes must match raw `results/*.json` and tables to identical decimal precision.
   - Audits **baseline fairness**: demands the **strongest safe same-catalog baselines** (not just broken legacy scripts or unfiltered scans), exact cold-vs-warm path accounting, and the **amortization break-even crossover $q^*$** (queries per policy/metadata update).
   - Enforces the **Public-Data Sufficiency Rule**: verifies that headline claims stand **independently on public benchmarks** (e.g., TPC-DS / TPC-H) even if proprietary production traces were removed.
   - Enforces **Results Presentation S01–S11**: bold best, underline second-best (ties share marks), Best/2nd or standing summary per RQ, unified decimals per metric, single unit per column header, claim-first captions (`<= 30` words for tables), ICDE-native `\textbf{Takeaway.}` per RQ, and honest **Operating Regimes** analysis (`phenomenon -> run-counter mechanism -> crossover boundary -> safety fallback`).
3. **R3 — Outside-Area Generalist, 180 DPI Visual & Anti-Self-Negation Referee**:
   - Runs a **10-minute two-pass scan** (Title -> Abstract -> Fig. 1 -> Section openings -> Tables) to verify immediate mechanism clarity and SOTA standing.
   - Inspects **every page rendered at 180 DPI PNG** (not just `pdflatex` logs!) for wrapped equation numbers, stretched pseudocode lines, crowded `\tabcolsep` headers, legend overlaps, font mismatches against 8–9 pt body Times, and float-to-prose drift (`|\Delta p| <= 1`).
   - Runs **anti-AI-smell & anti-self-negation audit**: zero AI clichés, zero em-dashes, balanced sentence cadence (`<= 26` mean words), positive safety vocabulary (avoid repeating `"fail"` / `"Fail-Closed"` as positive headers), zero self-inflicted objections (`"A natural objection is..."`), and zero repeated caveats in Abstract/Conclusion.
4. **Senior PC Meta-Review**:
   - Because ICDE 2027 has **one rebuttal and NO revision round**, any gap requiring a new experiment, proof repair, or missing baseline is **Blocking (fatal post-submission)** and MUST be fixed before submission rather than patched with prose caveats.

## 3. Top-8 ICDE Industry Track Rejection Triggers (Symptom -> PC Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical PC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Marketing brochure / thin tech depth** | "Reads like a product blog; no formal model or generalizable design principle." | Add crisp `Preliminaries & Problem Formulation` + 2–3 named theorems with concise inline constructive proofs + reusable architectural abstraction. |
| **T2** | **Toy / synthetic-only evaluation** | "No real operational workload, no deployment constraints, belongs in Research track (and weak there)." | Pair real production workload characterization, rollout/shadow-audit path, and concrete Lessons Learned with scalable public benchmarks. |
| **T3** | **Out-of-band state bypass in version-fenced caches** | "Your hot cache keys only on control-plane revision $\tau$; what if a DBA runs `ALTER TABLE` directly on the warehouse?" | Upgrade cache keys and theorems to composite version pairs $\tau = (\tau_{\mathrm{pol}}, \tau_{\mathrm{sch}})$ binding physical schema fingerprints, and benchmark the updated key in code. |
| **T4** | **Strawman / unsafe-only baselines** | "Comparing only against unfiltered SQL or legacy scripts hides the real cost vs. safe alternatives." | Benchmark strongest *safe* same-catalog baselines (per-app materialized views, dynamic uncached policy join, DB-native RLS) and derive break-even $q^*$. |
| **T5** | **Conclusions hinge solely on private enterprise data** | "Reviewers cannot verify your main claims because the enterprise dataset is non-public." | Explicitly break out standalone public-benchmark metrics (e.g., TPC-DS leakage, compliance, speedup) in Setup and RQs showing every headline claim holds on public data alone. |
| **T6** | **Cross-section number / precision drift** | "Table IV reports `2,629.5x` and `22.0x` while Fig. 3 caption says `2,629x` and `22x`." | Run an automated regex reconciliation script across Abstract, prose, tables, captions, and JSON outputs; unify decimal precision per metric everywhere. |
| **T7** | **Self-negating framing or unexplained losses** | "Authors concede overhead in Abstract/Conclusion" OR "All-best claims look non-credible." | Keep every losing cell visible in tables; state mechanism once via real counters in the measuring RQ; add a dedicated `Operating Regimes: Where X Wins and Where It Falls Behind` paragraph; zero concessions in Abstract/Conclusion. |
| **T8** | **Hidden visual defects in clean LaTeX builds** | "Equation numbers wrap onto blank lines and Table IV columns collide." | Always render every page to 180 DPI PNG and visually inspect; fix equation overflow via `\resizebox{0.91\columnwidth}{!}{...}` / `\quad`, tighten long pseudocode constants with `\footnotesize\ttfamily`, and keep `\tabcolsep >= 3.5pt` using clean abbreviated headers. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

Before declaring an ICDE Industry manuscript camera-ready-grade for submission, explicitly run these 7 surgical checks that routinely slip past first-pass linters:

1. **Composite Revision Key Closure**: Verify every version-fenced cache theorem, algorithm line, and benchmark script keys on BOTH control-plane policy version AND underlying physical schema/catalog fingerprint (`\tau = (\tau_{\mathrm{pol}}, \tau_{\mathrm{sch}})`), confirming zero latency regression on the hot path.
2. **180 DPI Equation-Number & Pseudocode Line Audit**: Even with `0 Overfull \hbox`, inspect rendered PNGs of every `cases` equation, multi-term display equation, and `algorithmic` block for silently wrapped `(k)` equation tags or stretched word spacing from long monospace error identifiers.
3. **Cross-Artifact Precision Reconciliation**: Grep all derived ratios (`x`), percentages (`%`), and micro/millisecond latencies across `main.tex` (Abstract, RQs, captions, Operating Regimes, Conclusion) and assert exact string-precision agreement with `results/*.json`.
4. **Standalone Public-Benchmark Proof Block**: Confirm the experimental setup and key RQs explicitly quote standalone public-benchmark outcomes (separated from proprietary enterprise telemetry) so reviewers immediately see public reproducibility.
5. **Header Breathing Room in Wide Multi-Panel Tables**: Reject `\tabcolsep < 3.0pt` in 7–9 column full-width tables; replace verbose column titles with crisp unambiguous abbreviations and maintain `\tabcolsep` at `3.5–4.5pt`.
6. **Sentence Cadence Polishing**: Check mean sentence length and split 38–58 word compound sentences down to a crisp `22–26` word mean while keeping `0.00/1K` AI clichés and `0.00/1K` em-dashes and holding the exact 12-page budget.
7. **Neutral Artifact Statement & Stripped-Macro CMT Abstract Check**: Verify the supplemental link is described as a neutral, non-tracking public mirror, strip LaTeX macros to verify plain-text abstract length `<= 2,000` characters, and verify cleanroom execution in `/tmp` reproduces every table and figure verbatim.

## 5. Final Sign-Off Checklist
- [ ] `<= 12` pages total (0 appendix), `0` TeX/Bib errors, `0` Overfull `\hbox`, AI-Generated Content Acknowledgement present, stripped abstract `<= 2,000` chars.
- [ ] 3-lens PC review + Senior PC meta-review completed with real Blocking/Major findings fixed at the root cause (not just patched with caveats).
- [ ] 100% Claim-to-JSON number & decimal-precision reconciliation verified.
- [ ] 180 DPI visual inspection completed on all modified and float-bearing pages.
- [ ] Cleanroom `/tmp` run of artifact `run_all.sh` passes (`exit 0`) with zero hardcoded local paths or secrets.
- [ ] `master_8gate_audit.py`, `icde_structure_check.py`, `results_lint.py`, `proof_and_math_audit.py`, `figure_formula_consistency_audit.py`, `latex_table_and_cite_lint.py`, `float_proximity_audit.py`, and `ai_smell_audit.py` all pass (`0 FAIL / 0 WARN`).
