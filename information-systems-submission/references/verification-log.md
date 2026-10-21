# Verification log

## 2026-10-21
Readable and used:
- shop.elsevier.com journal page (scope, article types, reproducibility emphasis).
- The 2016 reproducibility editorial and guidelines on cs.nyu.edu (Dennis Shasha, Editor-in-Chief).
- Elsevier-wide pages on LaTeX submission, highlights, graphical abstracts, artwork, generative AI, CRediT, declarations, research data and sharing.
- elsarticle v3.5 documentation (CTAN mirror).

Not readable:
- ScienceDirect Guide for Authors and journal insights pages: blocked for automated clients and the in-app browser ("There was a problem providing the content you requested", CPE00001).
- Elsevier open-access options page and Editorial Manager: blocked by robots rules.
- Crossref API: rate limited; dblp: bot protection.

Outdated, do not use as rules: https://cs.nyu.edu/~shasha/papers/authorinst.txt (old elsart class, email submission).

## How to update
1. Get the Guide for Authors from the user as PDF or pasted text.
2. For each [CHECK] item in SKILL.md, replace it with the guide's rule and mark it [GUIDE], adding the section name of the guide.
3. Add a dated entry here.

## 2026-10-21 (later the same day)
The user saved the ScienceDirect Guide for Authors from a normal browser as a single-page screenshot PDF (1920 x 29370 px). It was split into 13 tiles and read with OCR (tesseract), then checked by eye where OCR was unclear. All former [CHECK] items were resolved except the APC amount and the Editorial Manager URL:
- single anonymized review;
- highlights required at submission, 3–5 bullets, 85 characters, file name contains "highlights";
- abstract at most 250 words; 1–7 keywords;
- any consistent reference style at submission, numbered in order of appearance;
- research data Option C;
- editable source required ("upon submission or revision"); PDF is not a source file;
- figures as separate files named like Figure_1;
- AI declaration at the end, in a new section before the reference list;
- funding statement must give the sponsor's role.

## 2026-10-21 (evening): Claude in Chrome
At the user's request the Guide for Authors and the open-access page were opened in the user's own Chrome through the Claude in Chrome extension and read in full with get_page_text. The text matched the earlier OCR reading item by item. Newly confirmed:
- APC USD 3150 excluding taxes, all article types; licences CC BY, CC BY-NC, CC BY-NC-ND; subscription option free;
- 24-month self-archiving embargo for subscription articles;
- submission link https://submit.elsevier.com/INFOSYS;
- CiteScore 11.8 and Impact Factor 4.0 shown on the journal header.
No [CHECK] items remain. Future updates: use Claude in Chrome first when available.
