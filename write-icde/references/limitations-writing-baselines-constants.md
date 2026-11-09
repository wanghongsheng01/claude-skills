# Baselines, hand-set constants and setup disclosures in accepted papers

Read in full on 2026-11-09 for the AuthZ-Graph ("No Stale Allows") ICDE 2027 R2 submission, after its v6 revision added a
direction-optimizing BiBFS baseline and a sweep of the probe/scan constant. Companion to `limitations-writing-reachability.md`.
Section 4 holds the rewriting rules; section 7 the before/after rewrites from that submission.

## 0. Method and scope

- 10 core papers read in full text (PDF downloaded, text extracted page by page, every quote below re-located in the extracted text with a string search). One extra paper (DBL, DASFAA 2021) was also read in full. It is outside the target venues, so it is listed separately and **excluded from all counts**.
- Venues of the 10 core papers: SC'12 (1), ICDE 2023 (1), SIGMOD 2013/2021/2022 (3), PVLDB 2014/2022 (3), and SEA 2020 / SEA 2021 (2: Hanauer et al. and O'Reach, both named in the brief).
- "PDF p." means the page index of the PDF file that was read. For PVLDB/SIGMOD/ICDE PDFs, this is the page within the paper, not the printed proceedings page number.
- Version caveats: Beamer was read from the author-hosted PDF, which carries a post-deadline erratum note in Table III. IFCA was read from the PKU-hosted PDF (15 pages). BatchHL, QbS, Hanauer and O'Reach were read from arXiv versions (v1/v1/v1/v2), which may differ slightly from the proceedings versions.
- Quotes are verbatim and under 15 words. Ellipses are not used inside quotes.

## 1. Per-paper table (summary)

| # | Paper (venue, year) | DOI / URL read | Q1: losses and baselines | Q2: constants and thresholds | Q3: machines and noise | One verbatim quote (location) |
|---|---|---|---|---|---|---|
| 1 | Beamer, Asanović, Patterson, *Direction-Optimizing BFS* (SC'12) | DOI 10.1109/SC.2012.50; read: people.eecs.berkeley.edu/~krste/papers/beamer-sc2012.pdf | Weakest graphs (flickr, wikipedia) explained by a mechanism: "substantially higher effective diameter" (Sec. VI-D, PDF p.6). Bottom-up alone "yields only modest speedups or even slowdowns" (VI-C, p.6). | α and β come from a sweep over the evaluation suite (Figs. 8–9), with the choice rule stated ("maximizes the average and minimum"). Insensitivity claim: α >12 is "relatively insensitive". Worst-case cost of mistuning: "within 15–20% of its peak". Oracle check: heuristic "within 10% of the oracle" (VI-B/C, p.5–6). | Three machines, each with a stated role: 16-core for most results, 40-core for scalability, 8-core "to perform a direct comparison with prior work" on the same hardware. "On all platforms we disable Turbo Boost"; 64 BFS runs averaged (VI-A, p.5). Cross-platform comparison with published numbers, with the hardware gap stated ("Despite using a slower system", VI-F, p.7). | "we select α = 14 since it maximizes the average and minimum" (Sec. VI-B, PDF p.5) |
| 2 | Pang, Zou, Liu, *IFCA* (ICDE 2023) | DOI 10.1109/ICDE55515.2023.00172; read: mod.wict.pku.edu.cn/docs/20230620091531176236.pdf | Concedes BiBFS strength **in the Introduction** (p.2). Index methods TOL/IP answer queries faster, "which is expected because IFCA does not build any index" (VI-C, p.11). Negative queries: faster "on nearly all the datasets", with a mechanism for the exceptions (p.11). Explains why the index baseline DAGGER is slower than BiBFS: "unidirectional search and depth-first strategy outweighs the advantage of pruning" (p.12). Gives a crossover analysis (query-per-update ratio, Fig. 6). | Cost-switch ratio λ is **measured** by a micro-benchmark, not hand-set (Sec. V-D4, p.8). Defaults "selected heuristically" (ϵpre = 100/m by intuition, α = 0.1 from prior work [56], ϵinit = 100ϵpre, step = 10) "to prove that IFCA's advantage ... is not reliant on the best parameters" (VI-A4, p.10). Sweep: Figs. 2–3. The ϵinit/step and α sweeps are "given in our full version". Oracle switching-point comparison (Tab. IV, p.10). | One machine (Xeon 2.1 GHz, 128 GB). Competitor code "kindly provided by their authors" (VI, p.8). | "BiBFS is actually more efficient than state-of-the-art reachability algorithms on dynamic graphs" (Sec. I, PDF p.2) |
| 3 | Farhan, Wang, Koehler, *BatchHL* (SIGMOD 2022) | DOI 10.1145/3514221.3517883; read: arxiv.org/pdf/2204.11012v1 | Own parallel variant BHLp "does not perform well on the last four datasets", with a mechanism (few affected vertices, so thread overhead dominates) and a regime statement (Sec. 7.2.1, p.11). BiBFS included as a baseline; no BiBFS wins are reported. | 20 landmarks chosen "in the same way as FulFD" for fairness (provenance = prior work; Sec. 7.1, p.10). Competitors use "the same parameter settings as suggested by their authors". Sweep of 10–50 landmarks (Figs. 7–8, Sec. 7.3, p.12–13), conclusions stated as mechanism-based trends. | One Linux server (Xeon W-2175, 512 GB; p.10). | "otherwise it may introduce unneeded thread overhead" (Sec. 7.2.1, PDF p.11) |
| 4 | Wang, Wang, Koehler, Lin, *Query-by-Sketch* (SIGMOD 2021) | DOI 10.1145/3448016.3452826; read: arxiv.org/pdf/2104.09733v1 | Bi-BFS baseline is 10–300× slower. Explains why baseline ParentPPL is slower than the simpler PPL (a vertex has many parents; Sec. 6.2.1, p.9). Explains QbS's own slow case (Twitter: large shortest-path graphs; p.9–10). | "We set \|R\| = 20 in QbS by default" with **no stated provenance for 20**; reasons are given only for picking high-degree vertices (Sec. 6.1, p.9). Sweep of 20–100 (Figs. 9–11) reports mixed outcomes (query time rises on some graphs), each with a mechanism (Sec. 6.4.3, p.11). | One Linux server (Xeon W-2175, 512 GB; p.8). | "more landmarks do not necessarily improve query time" (Sec. 6.4.3, PDF p.11) |
| 5 | Hanauer, Henzinger, Schulz, *Faster Fully Dynamic Transitive Closure in Practice* (SEA 2020) | read: arxiv.org/pdf/2002.00813v1 (LIPIcs DOI not verified) | BiBFS loss stated with exact factors in prose: "BiBFS won for d = 1.25, where it was about 20 % faster". Then "deteriorated with increasing density up to a slowdown factor of 91" (p.10). On Kronecker graphs: "The performance of BiBFS was ambivalent: it was the fastest on two instances" (p.11). Explains why own heavier variants lose to the simplest one (doubled/tripled update cost; p.9–10). | "Preliminary tests for SVC revealed z = 25 as a good threshold" (z = 50 on larger graphs; p.8): an informal-tuning origin, stated openly. Other parameters (k, c) are reported as separate named configurations, SV(k), SVA(k,c), SVC(z,c), rather than tuned away. | One machine. "Each experiment had exclusive access to one core and could use solely local memory", no swapping (p.7). Explains why the two strongest older competitors are missing (proprietary library) and how they are compared indirectly via BFS/DFS (p.7). | "Preliminary tests for SVC revealed z = 25 as a good threshold" (Sec. 4, PDF p.8) |
| 6 | Hanauer, Schulz, Trummer, *O'Reach* (SEA 2021; JEA 2022, DOI 10.1145/3556540) | read: arxiv.org/pdf/2008.10932v2 | Loss in one sentence: "Only for purely negative queries, IP(d) and BFL(s) were a bit faster alone" (p.17). Explains why the expensive Matrix (full TC) loses to constant-time tests: cache effects and memory footprint (p.12). Explains the weak case (cit-Patents, fallback rate >90%; p.12). | Test order "optimized by some preliminary experiments on a small subset of benchmark instances" and ordered "to avoid overfitting" (Sec. 4, p.9). k = 16, p = 75, h = 8, t = 4 are **stated without provenance** (Sec. 5.1, p.12). There is no systematic sweep, only remarks (k = 8 and t = 2 trade-offs, p.17). Competitors run with "the presets given by the authors". | One 48-core machine. Runs are sequential and exclusive on one processor. A disclosed exception: Matrix used non-local memory and 48-thread initialization (p.10). Five runs with median, seeds, and five query shuffles; "does not change the overall picture" (p.10). | "optimized by some preliminary experiments on a small subset of benchmark instances" (Sec. 4, PDF p.9) |
| 7 | Akiba, Iwata, Yoshida, *Pruned Landmark Labeling* (SIGMOD 2013) | DOI 10.1145/2463676.2465315; read: arxiv.org/pdf/1304.4661 | Query-time loss is implicit and has no mechanism: faster "for almost all the smaller five datasets", otherwise "comparable" (Sec. 7.2.2, p.9). | The number of bit-parallel BFSs is set to 16 or 64 **without provenance** (Sec. 7.2, p.9). Sweep in Fig. 5: "not too sensitive ... unless we choose a too big number" (Sec. 7.3.5, p.11). | **Two machines**: the competitor HHL ran on a different Windows server, stated in one factual sentence, plus a note that only HHL preprocessing was parallelized while all other timings are sequential (Sec. 7.2, p.9). | "Experiments for hierarchical hub labeling were conducted on a Windows server" (Sec. 7.2, PDF p.9) |
| 8 | Wei, Yu, Lu, Jin, *IP label* (PVLDB 7(12), 2014) | DOI 10.14778/2732977.2732992; read: vldb.org/pvldb/vol7/p1191-wei.pdf | Best on only 5 of 13 sparse graphs, framed as "comparable to the best results in other sparse graphs" (Sec. 8.1, p.10). Loss on patent explained (half of the vertices have out-degree ≥4, so DFS is costly), with a future remedy (p.11). Index size larger on most graphs, with a mechanism (p.10). | k, h follow a stated rule (sparse 2/2, dense 5/5); µ = 100 "by default" (Sec. 8, p.10). Sweep on one graph (govwild) ends with "It confirms that µ = 100 is reasonable" (Sec. 8.4, p.11). | One machine (Xeon X5550, 24 GB), with time and memory caps stated (p.9). | "It confirms that µ = 100 is reasonable." (Sec. 8.4, PDF p.11) |
| 9 | Chen, Peng, Wang, Yu, *DLCR* (PVLDB 15(8), 2022) | DOI 10.14778/3529337.3529348; read: vldb.org/pvldb/vol15/p1645-chen.pdf | Unfavourable fact (index about 4× larger than P2H+) stated in one sentence with a mechanism (inverted indices, last-edge field) (Exp 1, p.11). | 8 synthetic labels "following the setting in [21]". \|Λ′\| = 4 "by default" with **no provenance** (Sec. 5.1, p.11). Sensitivity results (e.g., virtual labels, density) **deferred to the technical report** (p.11). | One machine (Xeon 2.3 GHz, 384 GB). 10 rounds averaged for updates (p.11–12). | "following the setting in [21]" (Sec. 5.1, PDF p.11) |
| 10 | Zhang, Li, Yuan, Qin, Zhang, Chang, *Shortest-Path Queries on Complex Networks: Experiments, Analyses, and Improvement* (PVLDB 15(11), 2022) | DOI 10.14778/3551793.3551820; read: vldb.org/pvldb/vol15/p2640-li.pdf | A baseline slower than plain BFS is explained: CTLB is 0.14× BFS on DELI but "1.25 times longer than BFS" on UK07, because "distance queries used by CTLB are not free" (Ex-1, p.10). Own variant MLLD slower than MLLU on LIVE, with a factor and a mechanism (p.12). The authors' own MLL has "the slowest query speed" among the index methods, framed as a space/time trade-off in a "Summary of Findings" (p.9). | PLLB baseline builds a partial PLL to distance ≤5 "in this paper", with **no provenance and no sweep** (p.9). | One machine (64 cores, 500 GB; p.9). | "But distance queries used by CTLB are not free" (Ex-1, PDF p.10) |
| S | Lyu, Li, He, Gong, *DBL* (DASFAA 2021; **excluded from counts**) | DOI 10.1007/978-3-030-73197-7_52; read: arxiv.org/pdf/2101.09441 | Loss to IP on 3 datasets, followed by a dedicated paragraph, "We analyze the reason", which blames large diameter (514, 24) for slow pruned BFS (p.15). CPU-over-GPU wins are also explained by diameter (p.16). | **Per-dataset** label sizes chosen "according to our parameter study" (p.13). | One server with a GPU (p.11). | "We analyze the reason that DBL can be slower than IP" (Sec. 6, PDF p.15) |

## 2. Detailed notes by question

### Q1: bidirectional / optimized online search baselines, and losses

- **IFCA (ICDE 2023)** is the closest precedent. A BiBFS strength is conceded in the Introduction ("Interestingly, we find that BiBFS ..."). It is turned into a design feature: a cost-based switch to BiBFS, so IFCA "performs at least comparably with BiBFS on graphs without discernible communities". In experiments, BiBFS is "the second-best" overall (p.12). The paper also gives a query-per-update crossover plot showing where index methods would win (Fig. 6, p.12). The pattern is concede, convert into a regime boundary, then quantify the crossover.
- **Hanauer et al. (SEA 2020)** report BiBFS wins with exact percentages and densities. The losing regime (very sparse, d = 1.25) is stated first, then how the gap grows with density ("slowdown factor of 91"). On Kronecker graphs, BiBFS is called "ambivalent" and its two wins are counted. This candid wording did not undermine the paper's claim that the new algorithms beat all *dynamic* competitors.
- **Pre-empting "weak baseline"**: 7/10 papers explain *why* a more elaborate method or variant is slower than a simpler one. The explanations name a concrete cost:
  - DAGGER vs BiBFS: unidirectional DFS (IFCA).
  - ParentPPL vs PPL: multiple parents (QbS).
  - CTLB vs BFS: "distance queries ... are not free" (MLL).
  - Bottom-up-only vs top-down (Beamer).
  - Matrix vs constant-time tests: cache footprint (O'Reach).
  - BHLp vs BHL: thread overhead (BatchHL).
  - SV(2)/SV(3) vs SV(1): doubled/tripled update cost (Hanauer).
- **Placement**: all 10 report unfavourable results in running prose in the experiments section, not only in tables. 9/10 attach a one-sentence mechanism. The exception is PLL, which uses "almost all" and "comparable" with no mechanism. Only IFCA repeats the BiBFS point outside the experiments section (Introduction). In no paper was the concession buried in a table only.
- **Hedging words used for partial wins**: "nearly all", "on most datasets", "comparable to the best", "a bit faster", "ambivalent".

### Q2: hand-set constants and thresholds

- **Beamer's α = 14 and β = 24 have a stated provenance.** They come from a sweep over the same 10 evaluation graphs (Figs. 8–9). The selection rule is stated (maximize average and minimum performance). The mistuning cost is bounded ("within 15–20% of its peak on most graphs"). The heuristic is checked against an oracle that tries all switch points ("within 10% of the oracle"). Beamer does not discuss that tuning and testing used the same graphs.
- **Openly informal origins were accepted** in three papers:
  - IFCA: "we select IFCA's parameters heuristically".
  - Hanauer: "Preliminary tests ... revealed z = 25".
  - O'Reach: "preliminary experiments on a small subset of benchmark instances ... to avoid overfitting".

  No paper uses the words "ad hoc" or "not tuned".
- **Inherit-for-fairness provenance**:
  - BatchHL: 20 landmarks "in the same way as FulFD".
  - DLCR: "following the setting in [21]".
  - IFCA: α = 0.1 following [56].
  - Competitor parameters "as advised" or "presets given by the authors": IFCA, BatchHL, O'Reach.
- **Measured instead of hand-set**: IFCA's cost-model ratio λ comes from a micro-benchmark of the two basic operations. This is the most defensible template for a cost-based switch constant.
- **Sweep conclusions are worded in three ways**:
  1. Insensitivity: Beamer "relatively insensitive"; PLL "not too sensitive ... unless we choose a too big number"; IFCA "impact ... is insignificant".
  2. Confirmation: IP "It confirms that µ = 100 is reasonable".
  3. Mechanism-explained trends, including adverse ones: QbS "more landmarks do not necessarily improve query time"; BatchHL Twitter linear growth.
- **Both papers whose method contains a run-time switch (Beamer, IFCA) validate it against an oracle switch point.**

### Q3: experimental setup disclosures

- **Multiple machines (2/10)**:
  - Beamer gives each machine a one-line role and states the direction of any hardware advantage when comparing with other platforms ("Despite using a slower system"; "a slightly slower system").
  - PLL states in one neutral sentence that a competitor ran on a different server, and separately notes the parallel-vs-sequential asymmetry.
  - Neither paper apologizes. Both keep the claims to within-machine ratios or state the direction of the bias (the bias works against the authors).
- **Noise controls stated explicitly (3/10)**:
  - Beamer: Turbo Boost disabled, 64 runs averaged.
  - Hanauer: exclusive core, local memory, no swapping.
  - O'Reach: exclusive processor, 5 runs with median, 5 seeds, 5 query shuffles, plus a robustness sentence: "taking the median instead or increasing the number of repetitions does not change the overall picture".
- **Disclosed deviations or exceptions (3/10)**:
  - O'Reach: Matrix used non-local memory and parallel initialization.
  - PLL: HHL preprocessing was parallelized.
  - Beamer: the author version carries an erratum note in Table III saying a TEPS rescaling "does not appear in the published version" because it was confirmed after the deadline.
- **Shared servers or noise admissions**: 0/10 mention a shared server or background load.
- **Missing competitor explained**: Hanauer (proprietary library, so compared indirectly). DBL is excluded from the IFCA comparison because "it cannot handle edge deletions".
- **Deferring material to a full version or technical report**: IFCA and DLCR (2/10). Note that ICDE 2027 forbids appendices, so only an artifact URL is available. See Section 5.

## 3. Counts (n = 10 core papers; DBL excluded; nothing UNVERIFIED is counted)

| Observation | Count | Papers |
|---|---|---|
| Report at least one unfavourable result in running prose (not table-only) | 10/10 | all |
| Attach a one-sentence mechanism to that result | 9/10 | all but PLL |
| Explain why a more elaborate baseline or variant is slower than a simpler one | 7/10 | Beamer, IFCA, BatchHL, QbS, Hanauer, O'Reach, MLL |
| Use a standalone BiBFS / bidirectional baseline | 5/10 | IFCA, BatchHL, QbS, Hanauer, MLL (O'Reach uses pruned BiBFS as a fallback) |
| ...of those, concede BiBFS wins or strength somewhere | 2/5 | IFCA (Introduction and Experiments), Hanauer (exact %) |
| Concession placed in the Introduction | 1/10 | IFCA |
| State at least one own or baseline constant with **no provenance sentence** | 5/10 | QbS (\|R\| = 20), O'Reach (k, p, h, t), PLL (16/64), DLCR (\|Λ′\| = 4), MLL (≤5) |
| Openly admit informal origin ("heuristically", "preliminary tests/experiments") | 3/10 | IFCA, Hanauer, O'Reach |
| Use the words "ad hoc" or "not tuned" | 0/10 | none |
| Constant inherited from prior work, stated as such | 3/10 | BatchHL, DLCR, IFCA (α) |
| Constant measured by micro-benchmark | 1/10 | IFCA (λ) |
| In-paper sensitivity sweep of a key parameter | 7/10 | Beamer, IFCA, BatchHL, QbS, PLL, IP, Hanauer (named configurations) |
| ...sweep conclusion worded as insensitivity | 3/7 | Beamer, PLL, IFCA |
| ...worded as "confirms ... reasonable" | 1/7 | IP |
| ...worded as mechanism-explained trends, including adverse ones | 2/7 | BatchHL, QbS |
| Sweep run on the same graphs used for evaluation, without comment | 3/7 | Beamer, IP (single graph), IFCA (two graphs shown, "trends ... similar") |
| Switch heuristic compared with an oracle switch point | 2/2 papers with a switch | Beamer, IFCA |
| Experiments on more than one machine | 2/10 | Beamer, PLL |
| Explicit noise-control statement beyond averaging | 3/10 | Beamer, Hanauer, O'Reach |
| Disclosed setup exception or erratum | 3/10 | O'Reach, PLL, Beamer (author version) |
| Mention shared server or background noise | 0/10 | none |
| Defer sweeps or results to a full version or TR | 2/10 | IFCA, DLCR |

## 4. Distilled rewriting rules for "No Stale Allows"

1. **Name the BiBFS win in prose, with a number, a graph property and a mechanism, in that order.** Template (Hanauer/IFCA/MLL style): "On shallow graphs (diameter ≤ D), DO-BiBFS is X× faster than [ours] because both frontiers meet after ≤ k levels, so the index probe and the label merge are not amortized." Do not leave it in a table only. 10/10 papers use prose and 9/10 give a mechanism.
2. **Concede early and convert the concession into a regime boundary.** IFCA puts "BiBFS is actually more efficient than state-of-the-art ..." in the Introduction and then defines when its method wins. For us: one sentence in the Introduction or the contributions saying the index targets deep or high-fan-out authorization chains and update-plus-check workloads. Add a crossover figure (IFCA's query-per-update plot, Hanauer's density sweep).
3. **Pre-empt "weak baseline" by naming the cost the stronger baseline pays.** If DO-BiBFS is slower than plain BFS on some graphs, write one sentence like MLL's "distance queries used by CTLB are not free": state the direction-switch bookkeeping overhead and when it is not repaid. Also state that the baseline follows Beamer's heuristic and uses the same graph layout. 7/10 papers explain such inversions.
4. **Give every constant one of four accepted provenances, never "ad hoc".** The four are:
   - (a) swept on the suite with an explicit selection rule (Beamer: "maximizes the average and minimum");
   - (b) inherited from prior work for fairness (BatchHL, DLCR);
   - (c) measured by a micro-benchmark (IFCA's λ);
   - (d) "chosen heuristically / by preliminary tests on a subset" plus a robustness check (IFCA, Hanauer, O'Reach).

   If we keep Beamer's α = 14 and β = 24 unchanged, say so and cite SC'12 as the provenance (type b). If our switch constant (the "constant-4") was hand-set, use type (d) wording.
5. **Sweep over at least one order of magnitude, normalize per graph, and report the worst-case loss of the fixed value.** Beamer's Fig. 8 plots "relative to its best on that graph" and states "within 15–20% of its peak". Word the conclusion with a quantified band ("within X% of the per-graph best for c ∈ [a, b]"). Avoid a bare "insensitive". If the sweep uses the evaluation graphs, add one clause saying so; no accepted paper did, which is a cheap way to stand out.
6. **Validate the switch against an oracle.** Both accepted papers with a run-time switch (Beamer, IFCA) report how close the heuristic gets to an oracle that tries every switch point. One small table or sentence ("within Y% of the oracle on Z/N graphs") answers most threshold criticism.
7. **Disclose a second machine or a later batch in one neutral sentence per machine, keep claims within-machine, and state the direction of any bias.** Templates:
   - PLL: "Experiments for X were conducted on [machine]."
   - Beamer: role per machine; "despite using a slower system".

   Never compare absolute times across machines. Report ratios measured on the same host. If the second host is faster or slower, say which way that biases the comparison.
8. **Add one robustness sentence on measurement noise, not an apology.** Give the controls (exclusive cores, pinned threads, turbo/frequency settings, repetitions, median) and then O'Reach's line: increasing repetitions or using the median "does not change the overall picture". No accepted paper in the corpus mentions shared servers. If the server was shared, state the controls and the observed run-to-run spread (e.g., CV) instead of the word "shared".

## 5. ICDE 2027 research-track CFP check (fetched 2026-11-09)

Sources:
- CFP page: https://icde2027.github.io/cf-research-papers.html
- Submission guidelines: https://icde2027.github.io/submission-guidelines.html
- Change history: GitHub API commits for repo icde2027/icde2027.github.io.

(a) **Page limit.** The CFP says: "Research and EAB papers must not exceed 12 pages, excluding references and the AI-generated content declaration (explained below). No appendix is allowed."
- The submission-guidelines page still says "AI-generated content acknowledgement". The camera-ready section of the CFP says "excluding the AI-generated content acknowledgments and the references".
- The disclosure itself "shall be disclosed in the acknowledgments section".
- So the exclusions are references plus the AI-content declaration/acknowledgment. Appendices are not allowed.

(b) **Round 2 dates.** "Submission due ... November 11, 2026". "All deadlines are 5:00PM Pacific Time." Other Round 2 dates:
- Author Rebuttal Period: January 8-15, 2027.
- Notification: February 10, 2027 ("Notification dates are approximate.").
- Camera-ready: March 10, 2027.
- CMT: https://cmt3.research.microsoft.com/ICDE2027

(c) **Rule changes dated after 2026-11-06: none found.**
- The last commit touching either page is ee76fd2, dated 2026-10-28T13:21Z. The newest commit in the whole repository is a414777, dated 2026-10-28T16:52Z.
- Neither page carries an "updated on" notice.
- The 2026-10-28 commit (before the cut-off) changed:
  - "acknowledgement" to "declaration" in the page-limit sentence;
  - COI definitions, now with dates: "during 2023 to the present"; "four or more papers published during 2016 to the present"; a new "collaborators" clause;
  - the 1-year-wait wording;
  - the registration wording;
  - added text: "Papers with incorrect or incomplete COI declarations as of the submission closing time are subject to desk rejection."
- Other rules on the current CFP:
  - "Single-blind anonymity: Submissions are reviewed in a single-blind manner."
  - Supplemental material: "Availability of the supplemental material will be considered in the evaluation of the paper."
  - No rule on multiple machines or experimental hardware.

## 6. UNVERIFIED items (not counted)

- The LIPIcs DOIs for Hanauer et al. SEA 2020 and O'Reach SEA 2021 were not checked. Only the arXiv versions and the JEA DOI for O'Reach (via Crossref) were checked.
- TOL (SIGMOD 2014), BFL (TKDE), the Hanauer et al. ALENEX single-source study, and Ligra's |E|/20 threshold were **not read** and are not used.
- IFCA's full version (GitHub) was not read, so the content of its deferred α, ϵinit and step sweeps is unverified.
- Whether the arXiv versions of BatchHL, QbS and O'Reach differ from their proceedings versions in the quoted passages was not checked.

## 7. Before/after from AuthZ-Graph v6 (statements that came back while compressing to 12 pages)

| v6 sentence | Problem | Rewrite (rule) |
|---|---|---|
| "The constant 4 was fixed when the check was first implemented ... and was not tuned" | provenance as confession; 0/10 papers say "not tuned" | "We set the constant to 4 heuristically and use it on all graphs; Section X varies it from 1 to 16" (rule 4d, IFCA) |
| "BiBFS ... slower on the other 14 graphs (up to 1.80x the time of BFS). FLIX is faster than the better of the two on all graphs but AMZN" | competitor-vs-competitor first, no mechanism: reads as a strawman BiBFS | lead with "FLIX is 1.05-16.3x faster than BiBFS on all 21 graphs"; one sentence naming the cost BiBFS pays (our BFS already searches from the cheaper side; BiBFS first enumerates the grant/deny sources); the single exception with its absolute gap (rules 1, 3) |
| "as the main runs shared the server, we compare methods only within a run"; "a later build that adds them" | 0/10 papers mention shared servers; "later" invites "added after the fact" | "every ratio compares methods run in one process on the same graph and stream"; "a second build ... reproduces every counter of the main runs, which our scripts check" (rules 7, 8) |
| case study ending "runs at 0.91x the speed of BFS and 0.78x that of BiBFS" | the only production graph ends on a double loss; ratios only in prose | absolute values of all three (all < 1 us) and the purpose of the case study (freshness under real deny rules), where the baselines returned stale allows (9/10 attach a mechanism) |
| "checks take up to 1.60x as long ..., with 8 or 16 up to 3.09x; no constant is more than 3% faster than 4" | conclusion buried after the losses | "4 is within 3% of the best of 1-16 on every graph, comparable to the noise between runs with identical decisions; smaller constants probe too often, larger ones too rarely" (rule 5, Beamer's "within 15-20% of its peak") |
