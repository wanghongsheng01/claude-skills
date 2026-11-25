---
name: "submit-pods"
description: "Final submission, EasyChair registration, strict double-anonymous hygiene, and private backup protocol for ACM PODS 2027 (PACMMOD, acmsmall, <=15 body pages excluding references and unlimited appendix). Enforces zero public author-linked repository URLs inside the review PDF, dual-submission conflict check, and Overleaf/private GitHub archival."
---

# Submitting to ACM PODS 2027 (`submit-pods`)

## Official PODS 2027 Cycle 2 Schedule (All 11:59 PM AoE)
- **Abstract Submission**: December 3, 2026 (2026-12-04 19:59 CST)
- **Full Paper Submission**: December 10, 2026 (2026-12-11 19:59 CST)
- **Rebuttal**: January 26–29, 2027
- **Initial Notification**: February 8, 2027
- **Revision Deadline**: February 22, 2027
- **Final Notification**: March 1, 2027
- **Submission Portal**: `https://easychair.org/conferences/?conf=pods2027`

## Mandatory Pre-Submission Gates
1. **ACM Non-Concurrent Submission Check**: Confirm no substantially overlapping manuscript is concurrently under review at any journal (e.g., DMKD) or conference.
2. **Strict Double-Anonymous Check**: Run `write-pods/scripts/pods_human_craft_audit.py paper/main.tex --pdf paper/main.pdf` → **`0 FAIL`**. Ensure zero personal GitHub links, zero author/institution strings, and empty PDF `/Author` metadata.
3. **15-Page Body Limit**: Confirm References begin on or before Page 16 (main body ≤ 15.0 pages) under `\documentclass[acmsmall,review,anonymous]{acmart}` with zero margin/font hacks.
4. **Reference Integrity**: Run `submission-integrity-check/scripts/ref_check.py` → `0 NOT_FOUND`, `0 SUSPECT`, published venues preferred over preprints.
5. **Visual & Math Proofcheck**: Run `proof_and_math_audit.py`, `figure_formula_consistency_audit.py`, `float_proximity_audit.py`, and `latex_table_and_cite_lint.py` → `0 FAIL`, plus visual inspection of rendered page PNGs.
6. **Private Workspace Backup**: Archive LaTeX sources, compiled PDF, Overleaf zip, experiment scripts, and review reports in a dedicated **PRIVATE** GitHub repository (never linked from the anonymous PDF).
