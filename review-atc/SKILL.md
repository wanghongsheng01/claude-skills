---
name: "review-atc"
description: "Simulated USENIX ATC (CCF-A / TH-CPL A) HotCRP Program Committee & Shepherd final review protocol. Tailored to ATC's emphasis on practicality, full end-to-end systems evaluation, zero Benchmarking Crimes (no omitted concurrency/sweep points), transparent real-OS-vs-harness implementation boundaries, lifecycle hygiene stress testing (RCU/epoch GC reclamation, SO_LINGER abrupt-disconnect FD/slot leak checks, live cross-channel fault isolation), cross-artifact pipeline order & probe-window closure, Decimal ROUND_HALF_UP parity, and strict 12.00-page zero-appendix 180 DPI visual gating. Use alongside write-atc and review-osdi."
---

# Simulated USENIX ATC Program Committee & Shepherd Review (`review-atc`)

Use after `write-atc` and before HotCRP submission to **USENIX ATC** (USENIX Annual Technical Conference).

## 1. Official Desk-Reject & HotCRP Compliance Gate (0 Tolerance)

- **Template & Strict 12.00-Page Cap**: Official `usenix-2020-09.sty` bundled flat at project root (for Overleaf portability), **strictly <= 12.00 pages main body** (visually verify at 180 DPI that zero body lines spill onto Page 13 and `References` starts cleanly at Page 13 top), **strictly 0 pages of Appendix**.
- **Double-Blind Anonymization**: Zero author names, affiliations, personal GitHub handles, internal hostnames/ports, or PDF `/Author` metadata leaks.
- **Native USENIX Style**: Concise practical systems prose—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes, hollow trailing QED boxes suppressed (`\renewcommand{\qedsymbol}{}`), `0%` un-upgraded arXiv citations where published versions exist.

## 2. Independent 3-Lens USENIX ATC PC Panel + Shepherd Meta-Review

USENIX ATC prioritizes **Practicality**, **End-to-End Systems Evaluation**, **Correctness & Soundness**, **Novelty**, and **Clarity**, gated by Conditional Accept + **Shepherding** sign-off:

1. **R1 — Systems Practicality, Isolation Architecture & Soundness Referee**:
   - Enforces **Real-OS-vs-Harness Boundary Transparency**: explicitly checks which components execute on real OS processes, real network/loopback sockets, real signals, and real OS memory/FD instrumentation vs. simulated upstream workloads—rejecting disguised mocks or unimplemented core modules punted to future work.
   - Audits **Lifecycle Hygiene Three-Pack** for lock-free / epoch / gateway / isolation systems:
     1. **Epoch/RCU GC Reclamation**: verify 100% retirement of old generations after slow concurrent readers finish;
     2. **Abrupt Client Disconnect Hygiene**: inject `>= 100` `SO_LINGER` forced TCP resets and assert `0` leaked tasks, `0` leaked concurrency slots, `0` OS `/dev/fd` growth, and `0` uncaught runtime exceptions (`ConnectionResetError` / `BrokenPipeError`);
     3. **Live Cross-Channel Fault Isolation**: run concurrent faulted vs. healthy channels confirming `100%` blocking & `0` upstream leakage on the faulted channel alongside `100%` uninterrupted throughput on healthy sibling channels.
   - Audits **Probe-Window & Pipeline-Order Closure**: tightens periodic health/drift propositions with exact detection intervals (`[0, T_h]`, distinguishing mutation arrival vs. probe completion) and verifies **identical stage ordering** across Figure 1, Section 3 prose, Algorithm 1 lines, and executable runtime code.
2. **R2 — End-to-End Evaluation, Anti-Benchmarking-Crime & Decimal-Reconciliation Referee**:
   - Enforces **Zero Omitted Sweep Points (Anti-Benchmarking-Crime Audit)**: cross-checks every parameter grid in `results/*.json`, `README.md`, and benchmark scripts against every table/plot—flagging any omitted concurrency level (e.g., dropping `C = 8` due to loopback scheduling jitter) as a **Blocking** Benchmarking Crime!
   - Performs **100% `Decimal(..., ROUND_HALF_UP)` Cross-Artifact Audit**: reconciles Abstract, prose, every table cell, AND **embedded figure callout annotations** against freshly run `results/*.json` (forbidding hardcoded stale latencies/percentages inside figure scripts and eliminating rounding-induced ratio paradoxes).
   - Audits **Honest Low-Load / Single-Tenant Crossover**: checks that the final evaluation subsection candidly quantifies fixed proxy/isolation hop overhead in trivial single-tenant static setups and pinpoints the exact multi-tenant/churn/scale crossover where the proposed design wins decisively.
3. **R3 — Outside-Area Systems Generalist, 180 DPI Visual & Wipe-First Artifact Referee**:
   - Inspects ALL rendered pages at **180 DPI PNG** to verify: zero 1–2 line body spill onto Page 13 (`page_13.png` starts cleanly at `References`), zero awkward wrapped narrow-column subsection headings, zero mixed parenthetical notes inside numeric table columns, `|\Delta p| \le 1` float proximity, and clean vector plots.
   - Runs **Wipe-First `/tmp` Cleanroom Verification**: deletes ALL pre-generated JSONs and PDFs inside `/tmp`, executes `bash run_all.sh` end-to-end (`exit 0`, zero uncaught exceptions), and verifies zero identity/path/secret leaks.
4. **Shepherd / PC Chair Meta-Review**:
   - Treats any Benchmarking Crime, uncaught runtime disconnect exception, missing lifecycle stress test, or stale table column as **Blocking** so the manuscript clears conditional-accept shepherding standards on initial submission.

## 3. Top-8 USENIX ATC Rejection Triggers (Symptom -> PC/Shepherd Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical ATC PC / Shepherd Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Benchmarking Crime: omitted sweep point** | "Your code & JSON test `C={1,4,8,16,32}`, yet Table 3 silently omits `C=8`!" | Report ALL sampled sweep points in full tables, explaining single-round scheduling jitter candidly via jitter-free CPU fast-path timings & high-concurrency scaling. |
| **T2** | **Hidden mock vs. real OS implementation boundary** | "Unclear which isolation parts run on real OS processes/sockets vs. mocked backends." | Add a dedicated *Implementation Scope & Boundary* paragraph clearly separating real OS mechanisms (processes, sockets, FDs, `ps`/cgroups) from controlled backend latency harnesses. |
| **T3** | **Unverified GC, FD leaks, or uncaught TCP resets** | "Does abrupt client disconnect leak slots/FDs, and do retired RCU epochs actually get collected?" | Harden runtime against `ConnectionResetError`/`BrokenPipeError` and run a real Lifecycle Hygiene stress suite (100 RCU swaps + slow readers, 100 `SO_LINGER` resets, live dual-channel fault isolation). |
| **T4** | **Stale embedded figure numbers & ratio paradoxes** | "Fig. 1 shows `0.21 µs` while Exp 1 JSON is `0.50 µs`; Table 4 ratio `76,950/2.638` disagrees with prose." | Dynamically load all figure annotations from `results/*.json`, enforce `Decimal(..., ROUND_HALF_UP)` across all tables/prose, and verify numerator/denominator ratio parity. |
| **T5** | **Ambiguous probe window & misaligned stage order** | "Fig. 1, Alg. 1, and code order Drift Guard vs. Quota Check differently; Prop. 1 blurs mutation vs. probe time." | Tighten Prop. 1 to `"arrives after probe k completes"` with explicit `[0, T_h]` window, and enforce 1-to-1 stage ordering across Figure 1, prose, pseudocode, and source code. |
| **T6** | **Microbenchmarks without end-to-end workloads** | "Isolated microbenchmarks don't prove end-to-end practical value." | Pair per-phase microbenchmarks with full-stack multi-tenant end-to-end throughput, P99/P99.9 latency, memory footprint, and practical baselines (process pools, sidecars, proxies). |
| **T7** | **Silent 2-line spill onto Page 13 (180 DPI)** | "Conclusion spills 2 lines onto Page 13 above References—violates 12-page limit." | Visually inspect `page_12.png` and `page_13.png` at 180 DPI confirming `0` body lines on Page 13, clean single-line subsection headings, and pure numeric table columns. |
| **T8** | **Cache-dependent artifact or non-USENIX formatting** | "Wiping pre-built JSONs breaks `run_all.sh`, or paper uses non-USENIX bold Takeaway stamps." | Pass wipe-first `/tmp` cleanroom rebuild (`exit 0`, zero exceptions), strip all `\textbf{Takeaway.}` stamps into native systems prose, and bundle `usenix-2020-09.sty` flat at zip root. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Full-Grid Concurrency Disclosure Check**: Diff the parameter grid inside `results/*.json` against every column/row of every evaluation table—never drop an inconvenient sweep point.
2. **`SO_LINGER` Abrupt-Reset & `/dev/fd` Leak Test**: 100 forced client disconnects routinely surface real uncaught `ConnectionResetError`/`BrokenPipeError` bugs and leaked semaphore slots in async gateways before reviewers ever run the artifact.
3. **RCU/Epoch Weak-Reference Reclamation Proof-by-Execution**: Pair slow in-flight readers with 100 rapid epoch swaps and check live generation count (`live_during <= 2`, `live_after == 1`, `100/100` retired) in code.
4. **Dynamic Figure-Callout Loading**: Ban hardcoded latency/percentage strings inside architecture-diagram Python scripts; read every embedded value straight from `results/*.json`.
5. **Four-Way Pipeline Order Alignment**: Check exact stage execution order across (a) Architecture Fig. 1, (b) Design Section prose, (c) Algorithm 1 pseudocode, and (d) runtime source code.
6. **Pure-Numeric Table Column Sweep**: Remove stray parenthetical text mixed into numeric table cells (e.g., keep clean `0.0` with unit in the header).
7. **Page-13 Top-Line Check at 180 DPI**: Confirm `References` begins cleanly at the very top of Page 13 (`12.00` body pages exact, `0` appendix) with `usenix-2020-09.sty` bundled flat beside `main.tex`.

## 5. Final Sign-Off Checklist
- [ ] `usenix-2020-09.sty` bundled flat, strictly `<= 12.00` body pages (`0` body lines on Page 13), **strictly `0` appendix**, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] Zero Benchmarking Crimes (all sweep points disclosed), explicit real-OS-vs-harness scope boundary, and honest single-tenant crossover regime.
- [ ] Lifecycle hygiene stress suite (GC reclamation + `SO_LINGER` FD/slot zero-leak + live cross-channel fault isolation) executed cleanly with `0` uncaught exceptions.
- [ ] `Decimal(..., ROUND_HALF_UP)` zero-drift reconciliation across prose, tables, and dynamically loaded figure annotations (`0` ratio paradoxes).
- [ ] 180 DPI visual proofread of every page passed (`0` Page-13 spill, `0` stretched headings, `0` hollow QED boxes, `0` non-USENIX `\textbf{Takeaway.}` stamps).
- [ ] Wipe-first `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
