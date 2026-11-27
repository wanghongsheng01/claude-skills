---
name: write-issta
description: "ACM SIGSOFT ISSTA (CCF-A / TH-CPL A) software testing & specification conformance paper craft, metamorphic/differential oracle evaluation, real-bug & mutation-score reporting, Vargha-Delaney A12 statistics, and Threats/Data-Availability standards distilled from accepted ISSTA 2024-2025 papers (QTRAN, ModelMeta, Metamorphic Coverage, Bugs in Pods)."
---

# ACM SIGSOFT ISSTA Paper Craft (`write-issta`)

## 1. Official ISSTA 2027 Hard Guardrails
- **Format & Page Limit**: `\documentclass[acmsmall,screen,review,anonymous]{acmart}`, **strictly <= 18 pages main body**, plus a **mandatory `Data Availability` section** immediately before References (excluded from the 18-page limit) and unlimited References.
- **Double-Blind & Clean Typography**: Strict double-anonymous review; suppress hollow trailing `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`); zero AI clichés, em-dashes `<= 1.2/1K`.

## 2. Five Signature Laws of Accepted ISSTA Papers

1. **Native ISSTA RQ Architecture & Concise `Answer to RQk` Callouts**:
   - Accepted ISSTA papers (*QTRAN ISSTA '25*, *ModelMeta ISSTA '25*, *Bugs in Pods ISSTA '24*) structure Evaluation into explicit `RQ1–RQ4` subsections and natively close each RQ with a compact framed **`Answer to RQk`** synthesis box summarizing the exact quantitative finding and mechanism.
2. **Real-World Unknown Bug Trophies + Mutation Testing + Zero-FP Audit**:
   - Software-testing PC members look first at **real defects uncovered in unmodified production/open-source codebases** (with root-cause category, severity, and confirmation/fix status), paired with controlled **mutation score (%)**, **false-positive rate (FPR %)**, and **per-specification runtime/token cost**.
3. **Cross-Project External Validity (Industrial + Open-Source Specifications)**:
   - Never evaluate on a single proprietary codebase alone: pair large-scale industrial KLoC repositories with **public open-source projects / specification benchmarks** so reviewers verify cross-repository generality.
4. **Non-Parametric Statistical Rigor (`Wilcoxon` + `Vargha–Delaney` $\hat{A}_{12}$)**:
   - Report multi-seed variance alongside paired Wilcoxon signed-rank $p$-values and **Vargha–Delaney $\hat{A}_{12}$ effect sizes**, plus an explicit **Operating Regimes** comparison explaining when lightweight syntactic AST/regex linters suffice (e.g., naming/import rules) vs. when semantic differential conformance testing is required (cross-module state/SQL invariants).
5. **Balanced `Threats to Validity` (`Internal / External / Construct`) & Mandatory `Data Availability`**:
   - Include a concise, non-self-negating `Threats to Validity` section where every threat is paired with the concrete experimental control that mitigates it, followed by Conclusion and `Data Availability` with an anonymized artifact URL.
