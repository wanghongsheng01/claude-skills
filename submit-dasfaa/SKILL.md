---
name: "submit-dasfaa"
description: "Final submission, strict double-blind hygiene, Overleaf Git sync, and private GitHub workspace backup guide for DASFAA 2027 Research Track (Springer LNCS, 16 pages A4 including references, Abstract <= 200 words). Enforces the dual-repository security rule: neutral anonymous.4open.science link inside the double-blind PDF, and a dedicated PRIVATE GitHub backup repository per paper for full process archival. Use before uploading any DASFAA manuscript to CMT."
---

# Submitting to DASFAA 2027 (`submit-dasfaa`)

Official DASFAA 2027 rules snapshot in `references/official-rules.md` (verified **2026-11-25**). Official CFP pages always win if updated.

## 1. Strict Double-Blind vs. Private Backup Protocol (CRITICAL)
- **Inside the PDF & CMT Submission:**
  - Use **only** neutral anonymous artifact hosting (e.g., `https://anonymous.4open.science/r/<slug>`).
  - **NEVER** create a *public* GitHub repository under a personal account (e.g., `wanghongsheng01`) for a double-blind DASFAA submission prior to final acceptance notification (`2027-01-25`).
  - Strip PDF metadata (`\hypersetup{pdfauthor={}, pdftitle={}, pdfsubject={}, pdfkeywords={}}`).
- **Dedicated Private GitHub Backup Repository (Per Paper, Mandatory):**
  - Every DASFAA paper gets its own dedicated **PRIVATE** GitHub backup repository (`private: true`, e.g., `wanghongsheng01/<paper-slug>-dasfaa2027-workspace`) storing:
    - Overleaf LaTeX source snapshot (`overleaf_src/`)
    - Compiled final PDF + Overleaf upload zip
    - Full deep review, self-negation audit, simulated 3-reviewer report, revision closure table, and CMT checklist (`docs/`)
    - Gate verification logs (`audit_logs/`)
  - **NEVER** paste the private GitHub workspace URL into the manuscript PDF or CMT form.
  - **NEVER** commit API keys, credentials, or raw proprietary/PII customer data.

## 2. Final Pre-Upload Gate Sequence
1. Run `write-dasfaa/scripts/dasfaa_human_craft_audit.py <paper_dir> --pdf <final.pdf>` → **0 FAIL**.
2. Run `ccfa-visual-table-ref-mastery/scripts/latex_table_and_cite_lint.py` & `float_proximity_audit.py` → **0 FAIL**.
3. Run `ccfa-human-readable-math-and-proof/scripts/proof_and_math_audit.py` → **0 FAIL** (including `0` `□` QED boxes).
4. Visually inspect rendered PNGs of every modified/key page (and confirm no overflow, no clipped legends, no garbled glyphs, no widow tail on Page 16).
5. Push verified sources to the paper's **Overleaf Git repo**; verify clean re-compile matches local PDF page count (`≤ 16` pages) and content.
6. Commit & push complete submission package + process reports to the paper's dedicated **PRIVATE** GitHub backup repository (`git status` clean, verified on GitHub).
7. Verify CMT form parity: Title, Plain-Text Abstract (`≤ 200` words, exact match with PDF), Subject Areas, Author list & COI declarations, and uploaded PDF downloaded back from CMT.
