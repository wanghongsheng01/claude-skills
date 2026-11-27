---
name: write-atc
description: "ACM SIGOPS / USENIX ATC (CCF-A / TH-CPL A) practical systems engineering, zero-downtime cloud/agent gateway isolation, per-tenant resource accounting, and operational evaluation craft distilled from accepted USENIX ATC 2023-2025 papers (TGW ATC '25, OSMOSIS, EdgeOS)."
---

# ACM SIGOPS / USENIX ATC Systems Craft (`write-atc`)

## 1. Official USENIX ATC 2027 Hard Guardrails
- **Format & Page Limit**: Official `usenix-2020-09.sty` (`\documentclass[letterpaper,twocolumn,10pt]{article}`), **strictly <= 12.0 pages main body**, unlimited References, **`0` appendix pages**.
- **Double-Blind & Clean Typography**: Suppress hollow trailing `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`); zero em-dashes (`<= 1.0/1K`), zero AI clichés (`expose`, `strictly`, `cleanly`, `furthermore`).

## 2. Five Signature Laws of Accepted USENIX ATC Papers

1. **Practical Operational Realism Over Heavy Theory**:
   - Follow *TGW (USENIX ATC '25)*: ATC reviewers prize deployable architectures with crisp wire-level latency breakdowns, **per-artifact memory footprint scaling (Bytes/Tool vs. process-per-tool sidecars)**, and **zero-drop rolling control-plane reload traces**.
2. **Native Systems Prose (No Mechanical `Takeaway.` Stamps)**:
   - Close evaluation subsections with concise natural systems synthesis sentences; keep every float within `|Δp| <= 1` of its first prose reference.
3. **Orthogonal Component Ablation & Noisy-Neighbor Tail Isolation**:
   - Include an explicit ablation table with a `\midrule` mean summary row isolating virtualized routing, epoch-pinned drain windows, schema-drift circuit breaking, and per-tenant token-bucket isolation under bursty floods.
4. **Honest Single-Tenant Static Crossover Regime**:
   - Quantify when a simple monolithic/direct-dispatch MCP server suffices (e.g., single-developer local setup with $N \le 5$ static tools and zero live control-plane rollouts, saving ~20–40 $\mu$s proxy hop) vs. multi-agent production gateways where `ToolIsolate` eliminates 14%–38% rollout drops and noisy-neighbor tail spikes.
5. **Claim-First Short Captions & Unified Precision**:
   - Open every table/figure caption with the quantitative finding (`<= 28` words for tables) and enforce uniform decimal precision per column.
