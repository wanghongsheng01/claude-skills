---
name: write-acl-arr
description: "ACL Rolling Review (ARR -> ACL / EMNLP / NAACL, CCF-A / TH-CPL A) paper craft, selective abstention & claim verification evaluation protocol, fine-grained error analysis, and native Limitations writing guide distilled from accepted ACL/EMNLP 2023-2025 papers (FActScore, MiniCheck, Claimify, STORYSUMM, Unanswerability in RAG)."
---

# ACL ARR (ACL / EMNLP) Paper Craft (`write-acl-arr`)

## 1. Official ACL ARR Hard Guardrails
- **Format & Page Limit**: `\documentclass[11pt]{article}` + `\usepackage[review]{acl}`, **strictly <= 8 pages main body**, followed immediately by a **mandatory unnumbered or numbered `Limitations` section** (does NOT count toward the 8-page body limit), optional `Ethical Considerations`, unlimited References, and unlimited Appendix.
- **Double-Blind**: Strict anonymization; suppress hollow trailing QED boxes (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`).

## 2. Five Native ACL Acceptance Laws (Form Follows Venue, Substance Absorbs Method)

1. **Native ACL Discourse (No Mechanical `Takeaway.` Stamps)**:
   - Accepted ACL/EMNLP papers close evaluation subsections with crisp, natural analytical prose sentences rather than repetitive `\textbf{Takeaway.}` labels. Keep every float within `|Δp| <= 1` of its first prose reference (introduce `Figure 1` in Section 1 on Pages 1–2, never wait until Page 4).
2. **Defeat Trivial Abstention via Selective Risk–Coverage (AURC) & Over-Abstention**:
   - In faithfulness, grounding, and abstention papers, a trivial verifier achieves `0%` hallucination by abstaining everywhere. Always report **Selective Utility / Answerable F1**, **Over-Abstention Rate (`OverAb %`)**, and **Area Under the Risk–Coverage Curve (AURC)** across threshold sweeps, paired with bootstrap 95% CIs and paired significance tests across `>= 5–6` neutral LLM families.
3. **Temporal / Structural Slice Decomposition & Operating Regimes**:
   - Follow *Claimify (ACL '25)* and *MiniCheck (EMNLP '24)*: stratify claims by semantic class and staleness horizon $\Delta t$, and explicitly analyze the **operating-regime crossover** (where lightweight static NLI verifiers suffice on timeless catalog attributes vs. where provenance-and-freshness verification becomes indispensable under finite TTL churn).
4. **Granular Error Taxonomy & Human Agreement ($\kappa$)**:
   - Include a quantitative multi-category error breakdown plus human-audit agreement (Cohen's $\kappa$ / exact match) on a stratified sample.
5. **Constructive Mandatory `Limitations` Section**:
   - ACL mandates a `Limitations` section: frame operational boundaries honestly and technically (e.g., clock-timestamp availability in upstream APIs, English/Chinese transactional scope, latency trade-off of live probe fallback) without self-negating the core verified contributions.
