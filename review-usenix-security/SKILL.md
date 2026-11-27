---
name: "review-usenix-security"
description: "Simulated USENIX Security Symposium (CCF-A / TH-CPL A) HotCRP Program Committee, Ethics Review, Open Science & Shepherd final review protocol. Tailored to USENIX Security's strict 13-page body limit + mandatory canonical 'Ethical Considerations' (Menlo Report four-principle stakeholder & responsible-disclosure analysis) and 'Compliance with the Open Science Policy' appendices before References, white-box lexical-shadowing / parser-evasion red-teaming (e.g., nested WITH CTE shadowing base tables), cryptographic verification-cache & atomic kid-revocation code-to-claim audits, multi-turn adaptive attack budgets (k=1..16), complex benign-workload FPR stress testing, standalone public-benchmark breakouts, Decimal ROUND_HALF_UP parity, and wipe-first /tmp cleanroom reproduction. Use alongside write-usenix-security."
---

# Simulated USENIX Security PC, Ethics & Open Science Review (`review-usenix-security`)

Use after `write-usenix-security` and before HotCRP submission to the **USENIX Security Symposium**.

## 1. Official Desk-Reject, Ethics & Open Science Gate (0 Tolerance)

- **Template & Strict 13-Page Cap**: Official `usenix-2020-09.sty` bundled flat at project root (for Overleaf portability), **strictly <= 13.0 pages main body** (excluding the two mandatory pre-Reference appendices and References; total PDF cleanly compact, typically `<= 20` pages).
- **Two Mandatory Canonical Pre-Reference Sections (EXACT USENIX Security Titles!)**:
  1. **`Ethical Considerations`** (immediately before References; NEVER shorten to `"Ethics Considerations"`): Explicitly structured around the **Menlo Report four principles** (Respect for Persons, Beneficence, Justice, Respect for Law and Public Interest), enumerating distinct stakeholder groups, concrete harm-minimization controls, de-identification safeguards, and responsible vulnerability disclosure status. Weak or missing ethics sections can trigger standalone rejection.
  2. **`Compliance with the Open Science Policy`** (immediately before References; NEVER shorten to `"Open Science"`): Links the neutral anonymous artifact mirror, lists exact reproducible components (code, scripts, datasets, benchmarks), and—if proprietary production logs or PII cannot be released—explicitly justifies the privacy exception while demonstrating full independent verification via public benchmarks and synthetic workloads.
- **Double-Blind & Native USENIX Style**: Zero author names, affiliations, personal GitHub handles, internal hostnames/ports, or PDF `/Author` metadata leaks; crisp natural systems-security prose (**zero** `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes, hollow QED boxes suppressed).

## 2. Independent 3-Lens USENIX Security PC + Ethics/Open-Science Panel

USENIX Security retired multi-cycle open-ended Major Revisions in favor of Accept / short-term **Shepherding** / Reject—so every security hole, ethics gap, or code-to-claim mismatch must be eliminated *before* submission:

1. **R1 — Adversarial Security, Threat Model & White-Box Bypass Referee**:
   - **White-Box Parser & Lexical-Shadowing Red-Team**: actively crafts white-box bypasses against the actual implementation code—specifically testing nested lexical shadowing (e.g., nested `WITH <base_table> AS (...)` tricking a flat CTE-name extractor into skipping authorization rewrites on the outer physical base table!), schema-qualified names, mixed casing, quoted identifiers, inline comments, and correlated subqueries. Any real bypass caught MUST be patched in code, added to Algorithm 1 (`\mathcal{C} \cap \mathcal{R} = \emptyset`), and proved in Theorem 1.
   - **Cryptographic Code-to-Claim Parity Audit**: verifies every security-critical optimization claimed in prose (e.g., short-lived `(kid, token)` signature caches with atomic key revocation `revoke_kid()`) actually exists in the implementation and is covered by a deterministic revocation-replay unit test!
   - **Threat Model Realism**: verifies clear TCB boundaries, realistic adversary capabilities, explicit out-of-scope vectors (e.g., side channels/kernel compromise), and tight alignment between threat model and formal invariants.
2. **R2 — Adaptive Evaluation, Complex Benign FPR & Public External Validity Referee**:
   - **Multi-Turn Adaptive Adversary Budgets**: rejects static single-shot attack evaluations; checks cumulative Attack Success Rate (ASR) across increasing interactive turn budgets (e.g., $k = 1 \to 16$) where an adaptive adversary switches attack classes mid-session, compared head-to-head against client-isolation / proxy baselines.
   - **Complex Benign-Workload FPR Stress Suite**: demands explicit False Positive Rate (FPR / FDR) testing on complex realistic benign queries/inputs (multi-CTE, `LEFT JOIN`, `CASE WHEN`, `COALESCE`, `EXISTS`/`IN`, window functions) alongside honest **Operating-Regime Crossover** analysis (when lightweight native views/ACLs suffice vs. when compiled gateway enforcement is indispensable).
   - **Standalone Public-Benchmark Breakout**: ensures public-benchmark ASR and FPR (e.g., TPC-DS / public suites) are reported explicitly on their own—never hidden solely inside combined totals with private/synthetic traces.
   - **100% `Decimal(..., ROUND_HALF_UP)` Reconciliation**: verifies every ASR, FPR, latency, and revocation count across Abstract, prose, tables, captions, and `results/*.json` (`0` drift).
3. **R3 — Ethics/Open-Science Compliance, 180 DPI Visual & Wipe-First Artifact Referee**:
   - Audits both mandatory canonical appendices (`Ethical Considerations` + `Compliance with the Open Science Policy`) against USENIX Security's official checklists.
   - Inspects every rendered page at **180 DPI PNG** for wrapped equation tags `(k)`, overfull Algorithm lines, figure-vs-prose symbol drift (`figure_formula_consistency_audit.py`), and `|\Delta p| \le 1` float proximity.
   - Runs **Wipe-First `/tmp` Cleanroom Execution**: deletes ALL pre-generated `results/*.json` and `figures/*.pdf` inside `/tmp`, executes `bash run_all.sh`, and verifies `exit 0` with identical reproduced ASR/FPR/revocation checks and `0` identity/path/secret leaks.
4. **Shepherd / PC Chair Meta-Review**:
   - Treats any reproducible white-box bypass, missing revocation implementation, non-canonical Ethics/Open Science title, or missing standalone public-track breakout as **Blocking**.

## 3. Top-8 USENIX Security Rejection Triggers (Symptom -> PC/Ethics Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical USENIX Security Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **White-box parser / lexical-shadowing bypass** | "A nested `WITH base_table AS (...)` subquery fools your flat CTE set and leaks unauthorized rows!" | Enforce strict namespace disjointness (`\mathcal{C} \cap \mathcal{R} = \emptyset`) and unconditional schema-qualified base-table rewriting in code, Algorithm 1, and Theorem 1; add a 20-probe white-box evasion suite. |
| **T2** | **Crypto cache / revocation code-to-claim mismatch** | "Section 3.1 claims `(kid, token)` caching with atomic `kid` revocation, but your code only caches `token`." | Implement real composite `(kid, token)` cache keys + atomic `revoke_kid(kid)` eviction and verify immediate `DENY_UNKNOWN_KID` on replay in automated tests. |
| **T3** | **Non-canonical or thin Ethics / Open Science sections** | "Wrong section titles; lacks Menlo Report stakeholder analysis and omits why raw production logs aren't shared." | Use exact titles `Ethical Considerations` (Menlo Report 4 principles + stakeholders + disclosure) and `Compliance with the Open Science Policy` (artifact manifest + justified PII exception + public verification path) before References. |
| **T4** | **Static one-shot attacks without adaptive budgets** | "What if an adaptive adversary probes across $k=16$ turns switching vectors?" | Evaluate cumulative ASR over multi-turn adaptive budgets ($k=1 \to 16$) against strong isolation baselines. |
| **T5** | **Unmeasured FPR on complex benign workloads** | "Your strict grammar/AST rejections probably break real complex SQL with CTEs, outer joins, and window functions." | Run a dedicated complex-benign stress suite (`>= 30` multi-CTE/join/window queries) proving `0.0%` FPR and align `FPR/FDR` terminology throughout. |
| **T6** | **Public-benchmark security numbers hidden in combined totals** | "External reviewers cannot tell whether claims hold on public TPC-DS without trusting private telemetry." | Explicitly report standalone public-track ASR and FPR in the main evaluation section alongside combined totals. |
| **T7** | **Overclaiming universal dominance over native ACLs** | "On small static single-app schemas, native DB views/RLS are simpler—why hide that?" | Include an honest counter-backed Operating Regimes crossover quantifying when native views suffice vs. multi-app dynamic sharing. |
| **T8** | **13-page / Overfull / AI-tic / cache-only artifact slips** | "Eq. (2) wraps, Algorithm 1 overflows column, or wiping JSONs breaks `run_all.sh`." | Inspect 180 DPI PNGs (`\small` / line splits for `0 Overfull`), verify `0.00/1K` AI-tics & `0` `\textbf{Takeaway.}` stamps, bundle `usenix-2020-09.sty` flat, and pass wipe-first `/tmp` `bash run_all.sh`. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Attack Your Own Parser Like a White-Box CTF Player**: Spend 15 minutes trying to break your own AST rewriter / policy engine using nested lexical shadowing, mixed casing, schema qualifiers, quoting, and correlated subqueries—catching a real 0-day bypass pre-submission saves the entire paper.
2. **Grep Every Claimed Crypto/Revocation Primitive Against Actual Source Code**: Confirm composite cache keys (`(kid, token)`), constant-time checks, TTL expirations, and atomic `revoke_kid()` calls are literally implemented and unit-tested.
3. **Exact Canonical Title Check**: Verify verbatim headings `\section*{Ethical Considerations}` and `\section*{Compliance with the Open Science Policy}` immediately preceding `\bibliographystyle` / `\bibliography`.
4. **Standalone Public-Track Breakout Verification**: Ensure the reader sees exact public-dataset `ASR` and `FPR` numbers right in Section 5 without opening JSON files.
5. **Complex Benign Regression Suite (`>= 30` Queries)**: Always pair every white-box hardening patch with a complex benign regression suite (`LEFT JOIN`, `CASE WHEN`, `COALESCE`, `EXISTS`, `IN`, nested CTEs, window functions) to prove zero collateral damage (`0.0%` FPR).
6. **Post-Edit AI-Tic Re-Scan**: Surgical security edits frequently sneak in hype words like `"unconditionally"` or `"fundamentally"`—always re-run `ai_smell_audit.py` (`0.00/1K`) *after* the final prose polish.
7. **Wipe-First `/tmp` Full-Suite Cleanroom Run**: Delete all pre-built `results/exp*.json` and `figures/*.pdf` inside `/tmp`, run `bash run_all.sh`, and assert every experiment (including white-box evasion, revocation replay, and benign FPR) recomputes and passes `exit 0` with `0` identity/secret leaks.

## 5. Final Sign-Off Checklist
- [ ] `usenix-2020-09.sty` bundled flat, strictly `<= 13.0` body pages, exact canonical `Ethical Considerations` & `Compliance with the Open Science Policy` before References, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] White-box parser/lexical-shadowing red-team passed (`0.0%` ASR) with invariants synced across code, Algorithm 1, and Theorem 1.
- [ ] Cryptographic cache & atomic `kid` revocation code-to-claim parity verified by live replay tests.
- [ ] Multi-turn adaptive budget ($k=1..16$), complex benign FPR (`0.0%`), standalone public-benchmark metrics, and honest operating regimes verified against `results/*.json` (`Decimal(..., ROUND_HALF_UP)` `0` drift).
- [ ] 180 DPI visual proofread passed (`0` wrapped equation tags, `0` algorithm overflows, `0` hollow QED boxes, `0` non-USENIX `\textbf{Takeaway.}` stamps, `0.00/1K` AI-tics).
- [ ] Wipe-first `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
