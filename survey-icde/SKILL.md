---
name: "survey-icde"
description: "Survey which research directions, problems and methods IEEE ICDE (CCF A) has been accepting, built from all 1058 research-track papers of ICDE 2024, 2025, 2026 and 2027 Round 1 (official accepted lists, OpenAlex abstracts, LLM-assisted classification by area x problem type x method type). Use when choosing a topic for ICDE (ICDE 选题 / 方向调研 / 录用偏好), checking whether a direction is rising or declining, or repeating the survey for a new year. Includes the classified dataset and the scripts."
---

# Surveying ICDE's accepted directions (ICDE 方向调研)

Evidence: `references/icde_2024_2027r1_classified.csv` (one row per accepted research paper: year, title, area, problem, method, llm, dynamic, eab, doi) and `references/findings.md`. The labels come from an LLM (DeepSeek-chat, temperature 0) reading title and abstract (titles only for 2027 R1 and part of 2026); expect some per-paper noise, while shares and trends are stable. Counts are observations, not acceptance criteria.

Use with `read-icde` (deep reading of the chosen direction), `write-icde`, `submit-icde`.

## Language convention
Reports to the author in **Chinese (中文)**; paper text in English.

## Headline findings (shares of accepted research papers)
| Area | 2024 | 2025 | 2026 | 2027R1 | Trend |
|---|---|---|---|---|---|
| Graph algorithms (cohesive subgraphs, paths, matching, community) | 13.6% | 16.9% | 14.6% | 6.3% | largest, stable |
| Spatio-temporal / trajectories | 7.5 | 8.5 | 7.3 | 11.0 | stable-up |
| Time series and streams | 6.7 | 6.8 | 8.0 | 11.8 | up |
| Privacy / security / blockchain | 6.9 | 8.5 | 7.3 | 7.1 | stable |
| Indexing and storage | 7.2 | 8.1 | 7.7 | 4.7 | stable |
| **LLM for data** (Text-to-SQL, LLM data processing, RAG as data problem, LLM for DB tuning) | 1.3 | 4.4 | 9.6 | **15.7** | **fastest rising** |
| **Vector search** | 3.7 | 3.7 | 4.6 | **8.7** | rising |
| Graph learning (GNN) | 9.6 | 5.8 | 2.3 | 3.9 | declining |
| Recommendation / generic mining | 8.5 | 3.7 | 2.7 | 3.9 | declining |

Problem types: efficiency of a defined problem 33-40%, effectiveness 27-38%, system 13-22%, new problem 9-12%, benchmark/experimental 2% to 7% (EAB category from 2026). Method types: algorithm + index with complexity analysis stays first (33-43%); pure learned models fall (36% to 21-28%); LLM-centred methods rise (1.6% to 18%). About a quarter of papers target dynamic or streaming data. Published papers: median 14 pages (12 body + references); title median 9 words, 55% with a colon, 39% "ACRONYM: description"; abstract median 203 words.

## How to read the trend for topic choice
1. Rising + matches your resources wins: LLM-for-data needs only API budget; vector search and systems need hardware; graph algorithms need algorithmic depth and large graphs.
2. ICDE rejects pure ML/DM as out of scope. In rising LLM topics, accepted papers turn the LLM task into a data-engineering problem (cost model, plan, sampling, index, scheduling).
3. Declining areas (GNN, generic recommendation) need an explicit data-management angle to get in.

## Repeating the survey for a new year
1. Download the official accepted-paper pages (e.g. `https://icde20XX.github.io/accepted-papers.html`); the page format changes every year, so adapt `scripts/parse_accepted.py` (it contains parsers for the 2024, 2025 and 2026/2027 page formats) to emit `{year, session, title, authors}`.
2. `scripts/fetch_openalex.py`: abstracts from OpenAlex, source `S4210210321` (ICDE). The free tier has a small daily budget per IP; use `page=` pagination.
3. `scripts/match.py`: join by normalised title (fuzzy cutoff 0.9).
4. `scripts/classify.py`: LLM labels in batches of 15 with the fixed taxonomy inside the script. Set `LLM_KEYS_JSON` to a key file outside the repository; responses are cached.
5. Tabulate shares per year and write the report; keep the raw HTML for provenance.

Notes: dblp.org shows a bot check to scripts; do not try to bypass it. Session names on the 2024/2025 programme pages are a second, PC-made topic label and are worth keeping.

## Final checklist
- [ ] All years parsed; counts per year match the official lists.
- [ ] Abstract coverage reported; classification method stated as LLM-assisted.
- [ ] Shares, growth and per-area problem/method mix tabulated.
- [ ] Topic choice justified by trend + scope + own resources.
