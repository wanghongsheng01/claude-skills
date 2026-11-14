---
name: ccfa-references-review
description: "Use when reviewing or fixing the reference list and in-text citations of a CCF-A database / NL2SQL paper (PVLDB, SIGMOD research or industrial, ICDE, ACL-family) before delivery (参考文献审查 / 引用太少 / 参考文献数量 / 引用规范 / reflint / 补参考文献 / 幻觉文献核查). Gives measured norms from 56 accepted 2024-26 papers by type (method median 51.5 refs, benchmark/EA&B 57, industrial 47; per-section citation counts; arXiv, recency, grouping, caption rules), 8 red lines (minimum count, cite every baseline/dataset/metric/tool at first use, every related-work claim cited, self-declared concurrent submissions in the bib, no unverified/hallucinated entries, published version over arXiv, no uncited entries, no notes in bib), style rules, and reflint.py, which checks a .tex+.bib against the norms and verifies every entry online (Crossref, arXiv, Semantic Scholar, DBLP). Reviewer and fixer must be different agents; candidate references must be verified before they are proposed."
---

# CCF-A references review

## When to use
- Before any paper is shown to the author or submitted, and after every revision round.
- When someone says the paper has too few references, too few citations, or a suspicious entry.
- When adding references: every candidate is verified with `scripts/verify_candidates.py` first.

## Norms (measured, median [P25, P75])
| | Method | Benchmark / EA&B | Industrial |
|---|---|---|---|
| Printed references | 51.5 [41, 64] | 57 [45.5, 75.5] | 47 [35.5, 60.5] |
| Citation brackets in text | 60 [50, 74] | 71 [52, 116] | 52 [29.5, 67.5] |
| Introduction | 12.5 [9, 16.5] | 16 [11.5, 22.5] | 11 [3, 17] |
| Related work | 16.5 [11.5, 25] | 12 [0, 26] | 15 [7.5, 22] |
| Experiments | 13 [7.75, 27.5] | 10 [3.5, 19.5] | 1 [0, 4.5] |
| Per related-work paragraph | 3.6 | 4.5 | 5 |
| Last 3 years | 57% | 42% | 32% |
| arXiv-only | 13% | 14% | 0% |
| Captions with a citation | 4/328 | 1/199 | 0/167 |

The full rules, with evidence and the sample, are in `references/REFERENCE_PRINCIPLES.md`. Read it before the first review.

## Red lines (any one = BLOCKER)
1. Printed references below the type P25 (method 41, benchmark 45, industrial 35). The target is the median. In PVLDB Vol. 20 and SIGMOD 2027 industrial, references do not count toward the 12 pages, so space is not a reason to stay short.
2. A baseline, dataset, benchmark, metric with prior art, or compared system appears without a citation at first mention. Models are cited by their technical report or model card, and tools by their paper or official documentation.
3. A related-work paragraph has no citation, or a claim about other work has no citation.
4. Concurrent or under-submission work by the same authors is mentioned but not in the bibliography. It must be marked "under submission" (PVLDB self-declaration policy).
5. An entry cannot be verified, or its metadata (title, venue, year, DOI) contradicts the publisher or DBLP record.
6. An arXiv entry is cited although a peer-reviewed version exists.
7. `\nocite{*}` or other uncited entries are printed, or a cited key is missing (shows as [?]).
8. Verification notes are left in `note` fields.

## Workflow (reviewer is not the fixer)
1. Pull the latest source. Clone read-only into a scratch folder; do not edit shared clones.
2. Run:
   ```
   python scripts/reflint.py --tex main.tex --type method|benchmark|industrial --online \
       --own "PaperName,OwnMetric1,OwnBaseline2" --cache ~/.cache/reflint.json --out report.md --json report.json
   ```
   It reports the count against the norm, per-section citation density, related-work paragraphs without citations, citations in captions, missing and uncited keys, well-known systems, models, benchmarks and tools without a citation at first use, and capitalised names never cited. It then checks every entry: DOI to Crossref, title to Crossref, arXiv, Semantic Scholar or DBLP, and URL status. It also finds arXiv entries with published versions and flags venue mismatches against the online record.
3. Read the introduction, related work, problem/metric definitions and experiment setup yourself. The script finds symptoms; you decide which claims need which citations.
4. For every needed addition, list candidates in a text file (`title | first-author surname`) and run `scripts/verify_candidates.py cands.txt`. Propose only rows marked VERIFIED, each with its DOI or DBLP/Anthology/OpenReview URL and a one-line reason.
5. Write `reviews/<paper>_refreview_rN.md` with a severity, a location, and a concrete fix for each finding. The fixer edits the .bib and adds `\cite` at the exact sentences, changes no numbers, recompiles, and checks that the references are [1..N] with no gaps, no [?], no uncited entries, and the body is still within the page limit. The reviewer then re-runs the review until there are 0 BLOCKER and 0 MAJOR findings.

## Notes and known limits of reflint
- Name detection is heuristic. Pass the paper's own system, variants and metrics with `--own`, and ignore generic acronyms.
- DBLP's API sits behind an anti-bot page from some networks. The script then falls back to Crossref and Semantic Scholar, which is rate-limited and retried with backoff. Results are cached.
- An "unverified" result means "not found automatically". Check it by hand; do not delete a real book or standard just because it has no DOI (for example, Abiteboul, Hull and Vianu, *Foundations of Databases*, 1995).
- NeurIPS, ICLR, ICML and CIDR have no DOIs. Cite the official proceedings or OpenReview URL.
- LLMs: any model used as a baseline, generator, judge or agent needs its technical report or vendor system/model card (the `Models` check). Models named only in an AI-use acknowledgement are exempt; the script skips those sections.
- Published-version detection misses papers whose title changed between arXiv and the venue (for example, a CIDR or PVLDB version renamed after review). For every remaining arXiv entry, search the title and the first author on DBLP or the venue site by hand.
- The year an index reports for a published version can be the arXiv year (for example, an ICLR 2026 paper indexed as 2025). Take the edition, year and pages from the venue page or DBLP.
- A citation at the end of a list sentence ("A, B, and C~\cite{a,b,c}") counts for every name in the list. A citation one or more sentences later does not: move it to the first mention.

## Files
- `references/REFERENCE_PRINCIPLES.md`: red lines, style rules, evidence, sample description.
- `scripts/reflint.py`: the linter (Python 3.9+, `requests`; optional `pymupdf` for `--pdf`).
- `scripts/verify_candidates.py`: verifies candidate references before they are proposed.
- `requirements.txt`
