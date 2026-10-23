# Source and public-review verification

## Citation ledger

For every existing or proposed reference, record:

| Field | Why it matters |
|---|---|
| Local citation key | Joins manuscript mentions to the record |
| Exact title, author group, year, venue, volume/article/page, DOI | Detects invented or mixed bibliographic records |
| Primary source URL and date checked | Publisher, author repository, PubMed, Crossref or official proceedings |
| Identity check outcome | DOI/title/author/year agree; unresolved differences remain flagged |
| Supporting section or passage location | A real paper can still be mis-cited |
| Neighboring manuscript claim and intended role | Background, method, dataset, comparison, mechanism or recommendation |
| Actual citation location | Prevents adding a long uncited bibliography |
| Verification level | Full supporting passage read; abstract-only support; metadata-only; unresolved |

A metadata service can establish identity. It cannot establish that a paper supports a mechanism, a performance comparison, or a particular implementation. Read the necessary primary passage. Cite the original method/data source where relevant; do not copy a reference from a review without checking it. Verify online-first versus issue year when they differ, and retain the source's article number rather than inventing a page range.

Reference expansion follows uncovered claims, not a quota. Add only sources used in the argument. The publication sample in `bib-publication-sample.md` is descriptive and deliberately small; its reference count and page range are not submission thresholds.

## Finding public historical peer review

Search the exact article title and DOI with terms for reviewer report, author response and peer-review history. Check the publisher landing page and supplements; the authors' institutional repositories and linked preprints; then relevant public review indexes. Record query, date, destination, access outcome and whether the document is actually linked to the target manuscript.

Distinguish:

- **Historical reviewer report:** a public document verifiably belonging to that paper's editorial process.
- **Author response:** a public reply linked to those reports.
- **Preprint comments or post-publication discussion:** useful context, but not necessarily journal refereeing.
- **Acknowledged draft reader:** not evidence of formal reviewer identity.
- **Simulated review:** the present analyst's judgment; label it as such.

The 2026-10-23 bbac343 investigation found no verifiable contemporaneous reviewer report or author response within the searched public scope. The journal article dates show receipt, revision and acceptance; they do not reveal reviewer demands. A bioRxiv DOI exists, but that content endpoint returned 403 in the browser search investigation. Other papers that cite bbac343 and publish their own reports are not its review history. “Not located” is not proof that no report exists.

Sources checked include [OUP article/history](https://academic.oup.com/bib/article/23/5/bbac343/6672903), [JCU archive](https://researchonline.jcu.edu.au/75949/), [UAB publication record](https://portalrecerca.uab.cat/en/publications/benchmarks-in-antimicrobial-peptide-prediction-are-biased-due-to-/), [author team page](https://biogenies.info/subsite/team/mb.html) and [bioRxiv monthly archive](https://connect.biorxiv.org/archive/index.php?dt=2022-05). Some CLI reads failed while browser/search reads succeeded; do not relabel a failed channel as a successful one.

## Offline LaTeX closure is a separate layer

The bundled checker addresses direct citation-key coverage for explicit `\bibitem` manuscripts. It does not fetch the internet, expand arbitrary TeX, execute code, infer a DOI, or assess citation relevance. `\nocite` is reported but does not count as a scientific citation. Supported literal examples and comments do not count; citation-generating command/environment definitions require a TeX-expansion audit. A missing input, recognized unsupported dynamic bibliography, or multiple `thebibliography` environments in one manuscript prevents a pass. Custom macros beyond the documented supported forms still require a normal compile and manual/expanded-output check.
