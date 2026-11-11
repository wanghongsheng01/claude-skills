# Second author's review of AuthZ-Graph (ICDE 2027 R2, 2026-11-11), lessons and worked case

The paper ("No Stale Allows", a dynamic 2-hop index FLIX for authorization graphs with conditions and deny edges) had
already been submitted (CMT ID 2034) when the second author, a data-visualization and database researcher, reviewed it
quickly. The comments came with screenshots of the dataset table and of the update-cost table. They are paraphrased in
substance below; the replacement PDF was prepared before the deadline.

| # | Comment (paraphrased) | Rule | What was done |
|---|---|---|---|
| A1 | "Trim the dataset statistics table: it does not show your method. Shorten its long caption." | S11, S01 | Judged, partly adopted. The table stays (reviewers expect sizes, and two columns, the user's closure and the frontier hubs it reaches, are the variables that explain every win and loss). The constant `Updates` column (10,000 in all rows but AMZN) was dropped and stated in the setup text; the caption now opens with what the table shows about the method: "Deep nesting gives users hundreds to thousands of subjects (Clos.), of which FLIX indexes only the 2–26% that are frontier hubs (Hubs)". 47 -> 30 words. |
| A2 | "Against LCR you seem to lose. Discuss why. Not everything has to be best; if it is all best it is not credible. Discuss strengths and weaknesses, with takeaways." | S07, S10 | A run-in paragraph "Why LCR wins on some graphs, and what it costs", built from a counter of the runs (below), plus a "Where FLIX wins and where it does not" paragraph and a takeaway per RQ. |
| A3 | "All table captions are too long; papers do not write captions this long." | S01, S02 | Every caption opens with the claim and has 19–30 words (before: 34–91). The bold/underline convention and the protocol (seeds, CI, prefixes, update counts) moved to the setup text once. |

## How the LCR paragraph was found (evidence first)
1. List where the baseline wins in the printed table: LCR updates were cheaper than FLIX on SYN-1M, SYN-10M, LJ-full,
   Orkut, Friendster, GO and GO^m; its index was the smallest on 13 of 17 graphs.
2. Read the per-method counters in the raw result files (`extra` column), not the paper: LCR logs `relabels`. On every
   graph where it won, at most 4 updates of the measured prefix reached any of its 64 landmarks (0 on the large shallow
   graphs), so an update only inserted the edge. Where it lost, 14 re-indexings in 1,000 updates already cost 345 µs per
   update (DBLP), and DEEP-16 needed 12.2 per update (88 ms).
3. The same mechanism explains the size win (64 landmarks instead of a label per group) and the price (checks at
   0.77–1.59x the BFS time: landmarks rarely decide a check, and a negative answer exhausts the search; 216 µs against
   5.25 µs for FLIX on the same prefix of DEEP-16).
4. Put the numbers into generator macros (`LCRBelowNames`, `LCRBelowRelabMax`, `LCRRelabDBLP`, ...), so the text cannot
   drift from the tables, and compare the same prefix for both methods.

Template: "<Baseline> is cheaper than <ours> (<range>x) on <graphs>, because there <counter> (<value>), so <what it
skips>, while <ours> <what it does>. Where <counter> is larger, <baseline> is far more expensive: <example with
number>. For the same reason <its other win>. Every <operation> pays for this: <mechanism>, so <metric> (<numbers,
same setting>)."

## Other baselines that win rows (each got one sentence with a mechanism)
- GrpClosure checks on SYN-10K and Orkut: most subjects a user reaches there are frontier hubs anyway (hub share in the
  dataset table), so the frontier shrinks no intersection.
- GrpClosure updates on 7 shallow graphs (0.08–0.60 µs): FLIX adds or removes a hub in all labels below a subject whose
  first or last frontier edge changes; every subject is already a hub of GrpClosure.
- C-FC on LJ-full and Friendster: it answers repeated checks from its cache when a check costs as little as a lookup.
- BFS on AMZN (and in the SV table on AMZN, YouTube): users reach under ten subjects, which BFS visits before FLIX has
  resolved the resource's ancestors.
- Lag acknowledges faster than FLIX-D in every row: it skips the flushes before restrictive writes, which is exactly
  what returns its false allows. The deferral table gained a Lag acknowledgment column so this is visible.

## Generator details that mattered
- A pair of methods has no underlined second: a count row must count only the marks that are printed (the first draft
  counted the loser of a pair as "second").
- An empty cell needs its reason in the caption from the run record ("--: killed at 85 GB", read from the OOM file).
- Results-table constant columns are findings (FLIX 0/0 in every row = always exact); the lint checks constant columns
  only in descriptive tables.

## Lint and gates
- Submitted version: 24 WARN (S01 x8, S02 x7, S03 x2, S05 x7), 8 notes (S04 x5, S01 x1, S11 x2: the near-constant
  Updates column and a dataset caption that never names the method).
- Replacement: 0 WARN, 0 notes; body still ends on page 12 (captions paid for the new analysis; two plot heights cut
  by 0.2 in; one sentence that had been added only to fill white space removed again).
- `icde-cmt-submission/prepare_cmt.py` reported 13 body pages because the AI section was titled "Declaration";
  fixed in the same round.
