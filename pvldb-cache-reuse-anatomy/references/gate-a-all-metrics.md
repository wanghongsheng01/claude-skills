# Gate A — all-metric dominance matrix

Question: does the proposed method beat **every** baseline on **every** metric the paper (or its artifact/DEV evidence) reports?

## Build the matrix

1. **Enumerate metrics** from every table, figure, macro file and DEV result: execution counts, hit rate, scanned rows/bytes,
   measured engine time, end-to-end latency (mean and p95/p99), throughput, memory/metadata bytes, startup/selection cost,
   lifecycle total, correctness counts, robustness grids, sensitivity sweeps, agent/real-trace replays.
2. **Enumerate baselines**: every safe control, every outside system, and every *own variant or portfolio member* the method
   could have chosen (a method that loses to its own simpler variant has an algorithmic defect).
3. **Per cell and in total.** Report W/T/L per cell plus totals and paired CIs where available.
4. **Classify each row:** PASS (wins every cell), PARTIAL (ties, no loss), FAIL (any loss), MISSING (metric not measured for
   all baselines), NOT EVALUATED (reported only for the method).

## Rules

- **Ties.** A tie is "not beaten" unless the paper proves it is at a floor no method can beat (offline optimum, distinct
  cold misses under the budget). Otherwise require a method change that wins the cell.
- **Modeled metrics** (e.g., an assumed fixed per-call overhead) never substitute for a measured metric; if the measured one
  loses, the row FAILs.
- **Count proxies vs cost.** Fewer executions with more expensive executions is a FAIL on engine time; check both.
- **Startup costs** excluded from suffix totals must be compared in a lifecycle total.
- **Correctness** rows (wrong answers, over-privileged answers) are safety constraints; ties at zero among safe methods are
  acceptable; any nonzero count for the method is blocking.
- **DEV vs TEST.** DEV results guide design; only frozen, pre-registered runs on unseen seeds count for the headline.

## Writing the requirement for a FAIL / PARTIAL / MISSING row

Each requirement names (a) the root cause from the paper's own mechanism, (b) the *algorithmic* change, (c) the acceptance
test (which grid, which baselines, which metric, per-cell and total), and (d) the protocol (pre-register on DEV, freeze by hash,
evaluate once). Rewording, narrowing the claim, dropping the metric, or moving it to an appendix does not close the row.
