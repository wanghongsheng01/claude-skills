---
name: write-icml
description: "ICML 2027 (CCF-A / TH-CPL A) machine learning paper architecture, theorem-proof readability, empirical rigor, anti-AI-smell, and submission craft distilled from official ICML 2027 CFP and ICML 2024-2026 Oral/Spotlight papers."
---

# write-icml — ICML 2027 Human-Craft & Theoretical-Empirical Rigor Guide

## 1. Official ICML 2027 Hard Constraints (Verified 2026-11-26)
- **Deadlines**: Portal opens Jan 8, 2027; Mandatory Abstract Jan 14, 2027 (AoE); Full Paper Jan 22, 2027 (AoE).
- **Format**: Official ICML two-column LaTeX style (`icml2027.sty`, 10pt Times, US Letter, 2-column), **strictly <= 8 body pages** (excluding Broader Impact Statement, References, and unlimited Appendix; exceeding 8 body pages is automatic desk reject).
- **Review Policy**: Strictly **double-blind** on OpenReview. Zero author names, affiliations, personal GitHub handles, acknowledgments, or local `/Users/...` paths.
- **Required Closing Statement**: Concise **Impact Statement** placed immediately after Conclusion (does not count toward the 8-page body limit).

## 2. ICML Reviewer Mental Model & Acceptance Bar
1. **First-Principle Mathematical Core**: ICML reviewers reject "engineering pipelines with 5 heuristics." Every design component must follow from one clean statistical/learning-theoretic principle (e.g., finite-sample risk control, minimax regret, shift-calibrated abstention).
2. **Theory-Experiment Tight Coupling**: Every theorem must predict an observable empirical regime (e.g., coverage/risk gap vs. shift magnitude $\Delta$, sample complexity $O(1/\sqrt{n})$ vs. empirical error bands) — zero ornamental math.
3. **Multi-Domain + Public Benchmark Validation**: Pair real-world domain benchmarks (anonymized/sanitized multi-domain enterprise traces) with standard public ML distribution-shift benchmarks; report multi-seed means ± 95% CI, paired significance tests, strong tuned baselines (Standard Split Conformal, Weighted/Tibshirani Covariate-Shift CP, Angelopoulos CRC, Temperature/Platt Selective Risk), and sensitivity/ablation sweeps.
4. **Human-Readable Math & Prose**:
   - Zero inline set-builders `\{ ... : ... \}` in prose; promote complex expressions to centered `equation`/`align` blocks.
   - Main body (<= 8 pages) presents clear theorem statements, intuitive Proof Sketches, and key identities; full proofs live in well-spaced Appendix sections (short 3–6 line paragraphs + displayed steps).
   - Zero AI clichés (`delve`, `tapestry`, `incisive`, `principled decomposition`, `orthogonal`, `crucially`, `notably`, `seamless`, `comprehensive`, `dramatically`, `sweet spot`).
   - Zero geopolitical model labels (`domestic`/`international`).
   - Pure `booktabs` tables (`0` vertical rules `|`), Okabe-Ito colorblind-safe vector figures, float proximity `|Δp| <= 1`, zero hollow QED `□` artifacts in narrow columns.
