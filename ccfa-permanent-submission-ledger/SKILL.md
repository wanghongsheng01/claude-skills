---
name: ccfa-permanent-submission-ledger
description: "Master ledger of all permanent user-assistant paper-engineering rules, historical and current revision lessons, and mandatory automated pre-delivery quality gates across all CCF-A / top-venue submissions. Run `scripts/run_all_mandatory_gates.py` on EVERY version iteration before syncing Overleaf Git, dual GitHub repositories, or cloud storage."
---

# Permanent Submission Agreements & Mandatory Multi-Gate QA Ledger

This skill permanently codifies **every user requirement and corresponding engineering/writing solution** accumulated across our SIGMOD, PVLDB, ICDE, and journal submission campaigns so that **zero previously solved defects ever recur** on any manuscript iteration.

---

## 1. Complete Historical & Current Requirement-to-Solution Ledger

| # | User Requirement / Critique (Historical & Current) | Root Cause Identified | Permanent Engineering & Writing Solution | Enforcing Skill / Automated Script |
|---|---|---|---|---|
| **R1** | **Survey target venue & track innovation bar BEFORE starting/revising** (Research vs. EA&B vs. Industrial) | Different tracks judge novelty differently; applying Industrial style to PVLDB Research triggers "weak DB theory / too applied" rejects. | Run Track Novelty Calibration Matrix first; align problem abstraction, proof depth, and evaluation structure to the exact target track. | `ccfa-track-novelty-and-anti-stacking` (`anti_stacking_lint.py`) |
| **R2** | **Eliminate "scattered modules / gains from stacking many engineering components" smell** | Listing `"five operators... four guarantees"` in Abstract/Intro makes enterprise-inspired research look like an ad-hoc bag of filters. | Reverse-engineer `DBSP`/`SPADE`/`LOTUS`/`DocETL`: elevate into **one canonical DB problem** + **one unifying algebraic/optimization abstraction** (2 synergistic pillars), chained theoretical spine, and explicit **orthogonality vs. stacking** ablation analysis. | `ccfa-track-novelty-and-anti-stacking` (`anti_stacking_lint.py`) |
| **R3** | **Human-readable math in prose, theorems & proofs** (papers are read by living humans, not AI!) | Packing 12–16 inline formulas into narrow 3.3-inch two-column paragraphs or 19-line italic theorems exhausts reviewers. | Pre-define setup before `\begin{theorem}`; keep theorems $\le 9$ lines; put all `\sum`/`\frac`/multi-step chains into airy centered display blocks; cap inline math density in prose. | `ccfa-human-readable-math-and-proof` (`proof_and_math_audit.py`) |
| **R4** | **Mandatory check & fix for proof QED `□` formatting & typographical errors on EVERY version** | `acmart` default `txsya` `\openbox` floats above lowercase baseline like a tiny tofu box, and `<38%` short closing lines or tall inline `\sum` stretch leading and strand `□`. | Redefine `\qedsymbol` as an exact `0.50em` baseline-aligned geometric Halmos square; ban tall math in last 2 proof lines; enforce `42%–88%` closing line width via PyMuPDF check. | `ccfa-human-readable-math-and-proof` (`proof_and_math_audit.py`) |
| **R5** | **Mandatory check that ALL formulas & symbols in figures are correct and 100% consistent with prose** | Stale draft symbols (`\tau_0` vs. `\alpha, n_{\min}`), axis-vs-formula variable drift (`|T|` vs. `|T \setminus \mathcal{W}|`), and broken STIX `\setminus` glyphs. | AST-parse all figure scripts on every build; cross-check every math symbol, `(Thm. X)`, and `(Alg. Y)` against `main.tex`; ban STIX `\setminus` and raw ASCII `<=`. | `ccfa-human-readable-math-and-proof` (`figure_formula_consistency_audit.py`) |
| **R6** | **Zero crowding/overlap in figures & pure `booktabs` multi-tier tables** | Narrow vertical x-ticks collide (`DeepSeek V4` / `Qwen3.8`); vertical pipes `\|` break `\toprule`/`\midrule`. | Use shared-y-axis horizontal aligned matrices for multi-model plots; 300-DPI + PDF visual inspection; pure `booktabs` + `\cmidrule(lr){a-b}` with `0` vertical pipes. | `ccfa-visual-table-ref-mastery` (`latex_table_and_cite_lint.py`) |
| **R7** | **Float-to-prose proximity (`\|Δp\| ≤ 1`) & zero post-Related-Work float spills** | Late `figure*`/`table*` declarations in two-column LaTeX drift 2 pages later or spill onto Conclusion. | Place `figure*`/`table*` 1–1.5 columns earlier in `.tex` stream; audit exact PDF `(float_page - prose_page)` delta on every compile. | `ccfa-visual-table-ref-mastery` (`float_proximity_audit.py`) |
| **R8** | **Exhaustive 1-by-1 reference verification (`Published venue > arXiv`, pinpoint `\cite` $\le 4$ keys)** | Preprints cited after peer-reviewed publication (`TKDE`/`Nature`), truncated author lists, or 10-key undifferentiated citation dumps. | Run live Crossref + OpenAlex `ref_check.py` (`0 NOT_FOUND/SUSPECT/CHECK`); upgrade every published paper from `arXiv`; split citation brackets to $\le 4$ surgical keys. | `submission-integrity-check` (`ref_check.py`) + `latex_table_and_cite_lint.py` |
| **R9** | **Zero geopolitical model labels (`国外/国内`, `International/Domestic`) & zero opaque internal ports/codenames** | International venues are borderless; internal port numbers (`7207–7211`, `:4444`, `Redis v3`) mean nothing to reviewers. | Name models directly (`Claude-Opus-5.5`, `DeepSeek-V4-Pro`, `Qwen3.8-27B`); map all internal services to self-explanatory architectural roles. | `sigmod-human-writing-craft` (`ai_smell_audit.py`) |
| **R10** | **Permanent Data, LLM & Dual-Repo Delivery Hygiene** | Scattered scripts, secret-leak risk, or mixed sessions. | Enterprise data via `datahub-cli` (`~/.datahub/secrets.json`); LLMs via `llmhub` (`~/.llmhub/keys.env`); strict session isolation per paper; sync every version to **Overleaf Git + public `-artifact` repo + private `-workspace` repo + Feishu Drive** after `0`-secret scan; never click Submit on CMT. | `run_all_mandatory_gates.py` |

---

## 2. Single-Command Mandatory Gate Runner

Before delivering or pushing ANY version of ANY paper, execute:
```bash
python3 /Users/loctek/.gemini/antigravity/scratch/zju-ccfa-phd/repos/claude-skills/ccfa-permanent-submission-ledger/scripts/run_all_mandatory_gates.py \
  --paper-dir path/to/paper \
  --track pvldb-research \
  --fig-scripts path/to/fig_script.py
```
**Zero `FAIL`s allowed across all 7 automated gates.**

### Gate 8 — In-Paper Artifact Availability URL & Portable Reproducibility Repo Audit (Added Stage-3.2)
- **Trigger Lesson**: Even when a public GitHub `-artifact` repo exists, omitting its clickable URL inside `main.tex` prevents reviewers from finding the code, and hardcoded workstation paths (`/Users/...`) break reviewer execution.
- **Permanent Solution**:
  1. Every paper MUST include an explicit clickable `\url{https://github.com/...}` **Artifact Availability** statement in `main.tex` (e.g., in Experimental Setup and/or Conclusion) clearly stating open-sourced algorithms/benchmarks/traces/figure scripts alongside any enterprise privacy boundaries.
  2. Every script in the `-artifact` repo MUST resolve paths strictly relative to `Path(__file__).resolve().parents[1]`, ship with `requirements.txt` and one-click `reproduce_all.sh`, and pass clean-clone execution in `/tmp` with zero `/Users/...` paths and zero secrets (enforced by Gate 8 in `run_all_mandatory_gates.py --artifact-dir ...`).
