---
name: "submit-ml"
description: "Submission guide for the Springer journal Machine Learning (MLJ, ISSN 0885-6125). Use before submitting or transferring a manuscript to Machine Learning (投稿 Machine Learning / 改投 MLJ): Contribution Information Sheet, sn-jnl port, reference rules, figure rules, declarations and LLM disclosure."
---

# Submit to Machine Learning (投稿 Machine Learning 指南)

Facts read from the official guide and journal home page on 2026-11-02. Portal steps are not yet recorded; add them after a real submission.

## Desk risk
- The home page reports a median of 5 days from submission to first decision. Treat the information sheet and the first two pages as the main risk.
- Scope: research on learning problems, methods, applications and research methodology. Papers must state contributions clearly, support them with verifiable evidence, describe the learning component with its assumptions, and place the contribution in the machine learning literature.

## Mandatory: Contribution Information Sheet (1-2 pages)
Incomplete or uninformative sheets are returned without review. Reviewers expect the same answers in the introduction.
1. Main claim and why it matters to the machine learning literature. "We are the first to do X" is not acceptable without the importance of X.
2. Evidence, stated precisely with results and their implications.
3. The most closely related papers by other authors and how the paper relates to them.
4. Earlier publication of parts of the paper, and the significant contribution beyond it.

## Manuscript
- Springer Nature LaTeX template recommended: `\documentclass[pdflatex,sn-basic]{sn-jnl}`. Text width is 31pc (372 pt). In this class `\scriptsize` is 9 pt and `\footnotesize` is 7 pt, so use `\footnotesize` for dense tables.
- Upload source files and PDF. **No subfolders** for figures or bibliography. Editable source is required at every submission and revision.
- Title page information: authors, affiliations with country, corresponding author's e-mail, ORCID if available. Acknowledgments in a separate section on the title page.
- Abstract 150-250 words with no undefined abbreviations or unspecified references; 4-6 keywords; at most three heading levels.
- The guide states no anonymization requirement and requires authors on the title page, so review appears not to be double-blind. Confirm in the portal.
- No submission or publication fee. Open access is optional and is offered after acceptance.

## References
- Author-year citations. The reference list holds only works that are **published or accepted**; mention unpublished work in the text. Check every preprint for a published version before submitting.
- Cite data used, with DOI where available.

## Figures
- Lettering about 2-3 mm (8-12 pt), Helvetica or Arial, consistent size. Lines at least 0.3 pt. Fonts embedded.
- Name files `Fig1`, and so on. Figures go inside the text. Captions start with "Fig." (the class adds this). Size to the column width.
- Use patterns as well as colors, with lettering contrast of at least 4.5:1.

## Declarations (before the references)
- Under "Statements and Declarations": Funding, Competing interests, Data and code availability, Authors' contributions, and ethics if applicable. Missing declarations return the paper as incomplete.
- Employment by an interested company counts, including multiple affiliations, and so does support such as equipment. Do not use the sample sentence "did not receive support from any organization" if any organization helped.
- LLM use goes in the Methods. Only AI-assisted copy editing is exempt.

## Before submitting
- Check the public code repository for an earlier manuscript and state it in question 4 of the sheet.
- Compile once with pdflatex (Overleaf: New Project, Upload Project) and read every page. Check `tab:` widths at 372 pt.
- Reviewers may be suggested. Give independent people with institutional e-mail addresses.
- The journal also runs calls such as the ECML PKDD journal track; read the call for its schedule and conference obligations first.
