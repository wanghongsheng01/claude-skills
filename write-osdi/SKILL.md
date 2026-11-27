---
name: write-osdi
description: "USENIX OSDI (CCF-A / TH-CPL A) systems paper architecture, crash-consistency evaluation, failure-recovery timeline & tail-latency CDF craft, and reviewer-defense playbook distilled from accepted OSDI 2020-2025 papers (Delos OSDI '20, Blockaid OSDI '22, ExoFlow OSDI '23, Chardonnay OSDI '23, Beaver OSDI '24, Kamino OSDI '25, F2FSJ OSDI '25)."
---

# USENIX OSDI Systems Paper Craft (`write-osdi`)

## 1. Official USENIX OSDI Hard Guardrails
- **Format & Page Limit**: Official `usenix-2020-09.sty` (`\documentclass[letterpaper,twocolumn,10pt]{article}`), **strictly <= 12 pages main body** (aim for **11.4–12.0 pages**), unlimited References, **strictly ZERO Appendix (`0` appendix pages — desk-reject redline)**.
- **Double-Blind**: Strict double-anonymous review on HotCRP; zero author names, affiliations, internal hostnames/ports, or personal GitHub URLs. Suppress hollow trailing QED boxes (`\AtBeginDocument{\renewcommand{\qedsymbol}{}\renewcommand{\qed}{}}`).

## 2. Six Signature Laws of Accepted OSDI Papers

1. **"Small Mechanism, Strong Invariant" + Explicit Rejected Alternatives**:
   - OSDI reviewers prize minimal, composable mechanisms that uphold a rock-solid safety invariant without heavyweight distributed machinery. In Section 2, explicitly answer the obvious systems-PC question: **"Why not deploy external Raft/etcd/ZooKeeper or run distributed 2PC?"** Quantify both protocol impossibility (external SaaS orchestrators and Git remotes lack `XA PREPARE`) and split-brain fencing gaps when an external lock service is decoupled from the relational control-plane state machine.
2. **Separate Clock-Free Safety from Bounded-Skew Liveness**:
   - Any lease or epoch protocol at OSDI MUST explicitly prove in its protocol specification and safety theorem that **safety (mutual exclusion, monotonic snapshot visibility, zero false deletion) relies strictly on monotonic integer `fencing_epoch` CAS transitions in the shared store and NEVER on synchronized wall-clock time**, while wall-clock bounds affect **recovery liveness only**. Also specify **garbage-collection (GC) safety watermarks** (e.g., retaining pinned blobs/snapshots until active reader leases advance).
3. **Signature Visual #1 — Real-Time Crash-Recovery Step-Response Timeline**:
   - Follow *ExoFlow (OSDI '23)* and *Delos (OSDI '20)*: include a physical-time ($t$ in seconds) step-response trace where a live leader/sync worker suffers `SIGKILL` mid-flight at $t = t_{\text{kill}}$, showing lease expiry, fencing-epoch takeover, idempotent manifest replay, zero duplicate execution, and unperturbed read-path throughput (`0` reader errors).
4. **Signature Visual #2 — Multi-Stack Contention Tail-Latency CDF (P50 to P99.9)**:
   - Follow *Chardonnay (OSDI '23)* and *Kamino (OSDI '25)*: pair throughput scaling curves with an empirical **latency CDF** (P50, P95, P99, P99.9) on an isolated CPU benchmark so reviewers see how lease fencing + jittered backoff eliminates retry-storm tail spikes.
5. **Normalized Critical-Path Overhead & Two-Minute Scannable Tables**:
   - Report per-phase microbenchmark latency (`Acquire`, `Stage`, `Publish`, `Renew`) AND normalize it as a fraction of end-to-end workflow execution (`< 0.1%`). Keep every float within `|Δp| <= 1` of its first prose reference; open every table/figure caption with the quantitative takeaway claim (`<= 30` words for tables); unify decimal precision; close every evaluation subsection with a crisp **Takeaway**.
6. **Honest Crossover Regime (When Simpler Locks Suffice)**:
   - Explicitly state and quantify the low-contention boundary: for a single environment stack ($N = 1$) mutating one relational store without external Git/orchestrator mirroring, session-scoped DB advisory locks incur slightly lower per-call latency by skipping manifest persistence; once $N \ge 2$ stacks share a control plane or mirror across heterogeneous stores, `ChronoLease` eliminates 36%+ contention waste and torn visibility at sub-millisecond read overhead.
