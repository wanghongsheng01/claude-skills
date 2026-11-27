---
name: "review-osdi"
description: "Simulated USENIX OSDI (CCF-A / TH-CPL A) Program Committee & Shepherd final review protocol. Tailored to strict double-blind HotCRP systems reviewing (<= 12 pages body, strictly 0 appendix pages, multi-round PC discussion + conditional accept/shepherding sign-off). Audits 'Small Mechanism, Strong Invariant' depth, clock-free safety vs. bounded-skew liveness separation, external-consensus/2PC impossibility arguments, crash-window superseded-version linearization, empirical safe GC watermarks, SIGKILL step-response timelines & P99.9 tail-latency CDFs, rounding-induced ratio paradoxes, and native OSDI prose. Use alongside write-osdi."
---

# Simulated USENIX OSDI Program Committee & Shepherd Review (`review-osdi`)

Use after `write-osdi` and before HotCRP submission to **USENIX OSDI** (Symposium on Operating Systems Design and Implementation).

## 1. Official Desk-Reject & HotCRP Compliance Gate (0 Tolerance)

- **Template & Hard Page Cap**: Official `usenix-2020-09.sty` (`\documentclass[letterpaper,twocolumn,10pt]{article}`), **strictly <= 12.0 pages main body** (sweet spot **11.5–12.0 pages**; References start on page 13).
- **Zero-Appendix Hard Rule**: **Strictly 0 pages of Appendix** — including an appendix is a classic OSDI desk-reject trigger. Every critical invariant, protocol step, and evaluation figure must live cleanly inside the 12-page body.
- **Double-Blind Anonymization**: Zero author names, affiliations, internal hostnames/ports, personal GitHub links, identifying acknowledgements, or PDF `/Author` metadata leaks.
- **Typography & Build Hygiene**: Zero TeX/Bib errors, zero `Overfull \hbox`, zero Type 3 fonts, hollow trailing QED boxes suppressed (`\renewcommand{\qedsymbol}{}`), `0` mechanical `\textbf{Takeaway.}` database-style stamps (OSDI uses crisp natural-prose evaluation closing sentences).

## 2. Independent 3-Lens OSDI PC Panel + Shepherd/Chair Meta-Review

Simulate OSDI's multi-round PC evaluation and conditional-accept shepherding bar using three independent systems referees:

1. **R1 — Distributed Consistency, Fault-Tolerance & Protocol Soundness Referee**:
   - Applies the **"Small Mechanism, Strong Invariant"** test: rejects "just an engineering exercise" lacking a clean, transferable systems abstraction.
   - Probes **Clock-Free Safety vs. Bounded-Skew Liveness**: verifies that safety (mutual exclusion, monotonic visibility, zero torn reads, zero double execution) relies purely on durable monotonic integer fencing/CAS transitions and NEVER on synchronized wall-clock time, while clock-drift bounds $\epsilon$ constrain liveness recovery bounds only.
   - Probes **"Why not Raft/etcd/ZooKeeper or 2PC?"**: demands both protocol-level impossibility (e.g., external SaaS orchestrators / REST stores / Git remotes lack `XA PREPARE`) AND the split-brain fencing gap of decoupled external lock services when the backing store itself does not validate monotonic fencing epochs.
   - Probes **Hidden Concurrency & Crash Races**: checks strict fencing inequality (`\tau > \tau_{\text{last}}`) across same-holder periodic renewal vs. new-cycle acquisition, crash-window upstream version evolution ($v_2 \to v_3$ linearization), and safe garbage-collection watermarks ($W_{\text{gc}}$) under active long-running readers.
2. **R2 — Systems Performance, Tail-Latency & Reproducibility Referee**:
   - Performs **100% Claim-to-JSON reconciliation** across every P50/P95/P99/P99.9 percentile, throughput number, recovery time, waste rate, and normalized overhead ratio.
   - Audits **Rounding-Induced Ratio Paradoxes**: ensures printed sub-millisecond baselines keep sufficient decimal precision (typically 2 decimals) so reviewers doing mental division on table columns never see a discrepancy against claimed speedups.
   - Verifies **OSDI's Two Signature Dynamic Visuals**: (a) physical-time `SIGKILL` crash-recovery step-response trace (showing leader crash, lease expiry, epoch takeover, zero duplicate commits, and unperturbed read-path throughput) and (b) high-contention empirical latency CDF (P50 to P99.9) collected on an isolated, contention-free machine.
   - Audits **Critical-Path Attribution & Crossover Honesty**: verifies per-phase microbenchmarks explicitly sum to the end-to-end normalized fraction (`< 0.1%`) and honestly quantifies the low-contention single-node/single-store regime where simpler locks suffice.
3. **R3 — Outside-Area Systems Generalist & 180 DPI Visual/Prose Referee**:
   - Inspects every compiled PDF page at **180 DPI PNG** for stretched wrapped two-column subsection headings, clipped legends, unreadable fonts (`< 8 pt`), float-to-prose drift (`|\Delta p| > 1`), and dense math walls.
   - Audits **native OSDI academic prose**: zero AI clichés, zero em-dashes, balanced concise cadence (~18–24 mean words/sentence), zero self-negation in Abstract/Conclusion, and cleanroom `/tmp` artifact execution reproducing all tables and figures verbatim.
4. **PC Chair / Shepherd Meta-Review**:
   - Synthesizes into **Blocking** (would cause rejection or block conditional-accept shepherding sign-off), **Major**, and **Minor** items. Any missing edge-case validation (such as crash-window version superseding or concurrent-reader GC safety) must be resolved via real targeted fault-injection experiments before submission—never brushed off as future work.

## 3. Top-8 OSDI Rejection Triggers (Symptom -> PC Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical OSDI PC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **"Just an engineering exercise"** | "Nice tool, but what generalizable systems principle or invariant does it teach?" | Center the architecture on one minimal composable mechanism (e.g., epoch-fenced immutable manifest publishing) with an explicit formal safety/liveness contract. |
| **T2** | **Unanswered "Why not etcd/Raft/2PC?"** | "Why didn't you just run Raft or 2PC across the stores?" | Dedicate a concise Rejected-Alternatives analysis proving (1) protocol impossibility (`XA PREPARE` absent in external REST/Git stores) and (2) decoupled lock-service split-brain gaps without store-side epoch fencing. |
| **T3** | **Wall-clock leakage into safety** | "Your lease uses TTLs; an NTP jump or VM pause will cause dual writers and data corruption." | Prove safety purely from durable monotonic integer CAS transitions (`clock-free safety`), isolating clock-skew assumptions strictly to recovery liveness (`(T_lease + T_tick)/(1 - \epsilon)`). |
| **T4** | **Unverified crash-window & GC edge cases** | "What if upstream mutates $v_2 \to v_3$ while the leader is dead, or GC deletes a snapshot mid-query?" | Run targeted fault-injection stress tests verifying (1) $0/N$ torn reads / dangling refs across superseded-version crashes and (2) $0\%$ reader failures under Safe-Watermark GC vs. $100\%$ under immediate deletion. |
| **T5** | **Synthetic-only or noisy-host evaluation** | "No failure timeline, no P99.9 tail CDF, and latency was measured on a busy shared server." | Add physical-time `SIGKILL` recovery trace + multi-stack contention CDF (P50–P99.9) executed on an isolated CPU benchmark without concurrent background builds. |
| **T6** | **Rounding-induced ratio paradox / JSON drift** | "Table shows `742.7` vs `1.0` yet claims `772x`, and prose P95 differs from JSON by 3 ms." | Unify sub-millisecond tables to 2 decimal places (`742.72 / 0.96 = 772.06x`) and run an automated Claim-to-JSON checker before final compilation. |
| **T7** | **Hidden overhead or missing crossover** | "Where do your microbenchmark numbers add up, and why wouldn't a simple DB lock beat you at $N=1$?" | Show exact additive phase sums normalized against end-to-end job runtime AND honestly report the $N=1$ single-store crossover where advisory locks have lower raw call latency. |
| **T8** | **Format / blind-review / non-OSDI style leaks** | "Includes appendix / exceeds 12 pages / uses database-style bold Takeaway stamps / wrapped heading stretches line." | Enforce `<= 12.0` body pages + `0` appendix, strip all non-OSDI `Takeaway.` stamps into crisp prose, audit double-blind metadata, and inspect 180 DPI PNGs of every page. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Sub-Millisecond Rounding Audit**: Check every table containing `< 2 ms` latencies; use 2 decimal places everywhere in that table so printed column ratios match claimed speedup factors to the second decimal.
2. **Strict-Inequality Fence vs. Heartbeat Renewal Separation**: Whenever write-ahead fencing requires strict monotonicity (`\tau > \tau_{\text{last}}`), verify the protocol explicitly distinguishes **cross-cycle lease acquisition** (advancing `\tau`) from **in-cycle heartbeat lease renewal** (extending TTL without self-fencing).
3. **Superseded-Version Crash-Window Stress Test**: Inject crashes mid-publication while advancing upstream source versions (`v_2 -> v_3`) and verify `0` torn reads, `0` dangling references, `0` duplicate commits, and `100%` convergence to the newest version.
4. **Empirical Safe-Watermark GC Verification**: Never leave snapshot garbage collection as a design-only claim—benchmark long-running concurrent readers against immediate deletion (`~100%` reader failures) vs. watermark retention (`0%` reader failures + measured GC latency).
5. **Additive Overhead Reconciliation**: Explicitly list the exact sum of critical-path phases (`Acquire + Stage + Commit + Pointer Flip`) and its exact percentage of end-to-end execution at both P50 and P99.
6. **Corpus-Count Consistency Across Evolution Windows**: Distinguish initial snapshot counts from evolved replay corpus counts consistently across Table 1, Motivation, and Evaluation so reviewers never suspect mismatched datasets.
7. **Two-Column Wrapped Subsection Heading Check (180 DPI)**: Shorten any narrow-column subsection title that wraps awkwardly and stretches inter-word spacing, and verify exact `12.00` body-page alignment with References starting cleanly at the top of page 13.

## 5. Final Sign-Off Checklist
- [ ] `usenix-2020-09.sty`, `<= 12.0` body pages, **strictly `0` appendix pages**, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] 3-lens OSDI PC review + Shepherd meta-review completed; all Blocking/Major items resolved at root cause (with targeted fault-injection/GC runs where needed).
- [ ] 100% Claim-to-JSON percentile and ratio reconciliation passed (no rounding-induced ratio paradoxes).
- [ ] Both signature OSDI visuals (`SIGKILL` timeline + P50–P99.9 CDF) and additive normalized critical-path overhead verified.
- [ ] 180 DPI visual proofread of every page completed (`0` stretched headings, `0` overlaps, `0` hollow QED boxes, `0` non-OSDI `Takeaway.` stamps).
- [ ] Cleanroom `/tmp` artifact execution (`bash run_all.sh`) passes (`exit 0`) with identical numbers and zero local-path/secret leaks.
