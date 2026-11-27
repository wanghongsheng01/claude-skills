---
name: write-usenix-security
description: "USENIX Security (CCF-A / TH-CPL A) security paper architecture, formal threat modeling, non-interference proofs, adaptive multi-turn red-teaming, and mandatory Ethics & Open Science compliance distilled from accepted USENIX Security & NDSS 2024-2026 papers (IsolateGPT/SecGPT, privilege-separated LLM gateways)."
---

# USENIX Security Paper Craft (`write-usenix-security`)

## 1. Official USENIX Security 2027 Hard Guardrails
- **Format & Page Limit**: Official `usenix-2020-09.sty`, **strictly <= 13.0 pages main body**, followed by **mandatory `Ethics Considerations` and `Open Science` sections** + References + optional concise Appendix (**total PDF <= 20 pages**).
- **Double-Blind & Anti-Stacking**: Zero semicolons laundry-lists in Abstract (`<= 2` semicolons); suppress hollow trailing `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`); zero em-dash chains, zero AI clichés, zero mechanical `Takeaway.` stamps.

## 2. Five Signature Laws of Accepted USENIX Security Papers

1. **Crisp Threat Model & Explicit Positioning Against Hub-and-Spoke Sandboxes (*IsolateGPT / SecGPT*)**:
   - Clearly define trusted computing base (TCB), attacker capabilities (header spoofing, prompt injection, multi-query predicate probing, stale token replay), and explicitly explain why **application-level spoke sandboxing (*IsolateGPT / SecGPT*)** does NOT prevent cross-application confused-deputy escalation, column-union over-broadening, or implicit-predicate side channels inside a shared SSO data gateway.
2. **Formal Non-Interference Guarantee + Property Fuzzing**:
   - Pair formal non-interference / fail-closed theorems with 10,000-state randomized policy fuzzing (`0` violations).
3. **Adaptive Multi-Turn Red-Teaming Curve (Attack Budget $k = 1 \to 10$)**:
   - Security reviewers reject static-only probe evaluations: evaluate **adaptive multi-turn adversaries** across `>= 5–6` foundation-model families over increasing query/turn budgets $k$, measuring both **Attack Success Rate (ASR %)** and **Benign False-Rejection Rate (FRR %)**.
4. **Honest Operating-Regime Crossover (When Database RBAC Views Suffice)**:
   - Quantify the single-application, fixed-SQL dashboard regime where static database RBAC views already prevent cross-app escalation at zero gateway overhead, versus multi-application dynamic LLM query synthesis where static views either explode combinatorially or leak implicit predicates.
5. **Mandatory `Ethics Considerations` & `Open Science` Excellence**:
   - Detail stakeholder harm minimization (zero testing against live customer PII, responsible internal vulnerability remediation) and provide a complete self-contained anonymized artifact (`run_all.sh`) reproducing every probe, fuzz trial, and figure.
