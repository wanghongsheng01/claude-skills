---
name: "submit-kbs"
description: "Submission guide for the Elsevier journal Knowledge-Based Systems (KBS, ISSN 0950-7051). Use before preparing or submitting a manuscript to Knowledge-Based Systems (投稿 KBS / Knowledge-Based Systems)."
---

# Submit to Knowledge-Based Systems (投稿 KBS 指南)

Facts read from the official guide for authors on 2026-11-02 (ScienceDirect blocks the built-in browser; read it through Claude in Chrome). Portal steps below were recorded on the real submission of 2026-11-03.

## Rules
- Scope: AI, "knowledge-based and other artificial intelligence techniques-based systems". Leading topics include machine learning theory, methodology and algorithms, and intelligent decision support systems.
- Review: **single anonymized**. Authors stay on the manuscript; no anonymized version.
- Length: research papers "preferably no more than 20 double line spaced manuscript pages, including tables and figures". A soft limit; say so to the author if the paper is longer.
- Abstract at most 250 words; 1 to 7 keywords; highlights encouraged: 3 to 5 bullets of at most 85 characters each, as a separate editable file whose name contains "highlights".
- References: numbered in square brackets in order of appearance (elsarticle-num). Preprints may be cited.
- Source: editable files are required (.tex); a PDF is not a source file. The elsarticle template is encouraged.
- Funding sentence if none: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."
- Generative AI: a section titled "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process" with the statement "During the preparation of this work the author(s) used [TOOL] to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article."
- Data statement required at submission; preprints do not count as prior publication.

## elsarticle traps
- `\appendix` makes `\thesection` "Appendix A", so write `\ref{app:x}`, not `Appendix~\ref{app:x}`.
- Put the declarations before `\appendix`, or appendix floats may land after them.
- With `preprint,12pt` the text width is 390 pt (about 5.4 in).

## Portal (Elsevier "Submit your manuscript" service, recorded 2026-11-03)
The editorialmanager.com/knosys link leads to Elsevier's new submission service, not the old Editorial Manager screens. Seven steps:
1. Article type: Full Length Article.
2. Upload files. Required: Cover letter, Manuscript (a PDF when written in LaTeX; metadata is not extracted from it), Declaration of competing interests. Optional: Highlights, Supplementary material, Figure, Table, LaTeX source files (not needed until revision), co-submission to Data in Brief or MethodsX (extra charge; skip).
   - The page offers a "no competing interests" tick box in place of the declaration file. Tick it only if the manuscript's declaration says so for every author. If an author's employer appears in the declaration, untick it and upload the Word file from the declaration of interest tool.
   - In the tool: support for this work (step 1) records non-financial support such as provided compute or API access; outside support (step 2) records employment.
3. Title, abstract, keywords. The abstract box counts up to 250 words. The keyword box takes **at most 5**, separated by semicolons, even though the guide allows 7; drop the weakest one there and leave the manuscript unchanged.
4. Authors: first and last name, one institution per author (searched from a list), email, CRediT roles (match the manuscript's CRediT statement), corresponding-author tick.
5. Funding: Yes/No.
6. Additional information:
   - Research data: link, repository, original or reference data, and data set title. The link is printed verbatim in the article, so use a concept DOI that resolves to the latest version.
   - Free SSRN preprint: author's choice.
   - Subject area, chosen from DL, ML ("Other Machine Learning and computational intelligence"), CV, DS, LLM, APP and Emerging. Choose by the contribution, not the application.
7. Review and submit. The confirmation page shows no manuscript number; it arrives by email.
