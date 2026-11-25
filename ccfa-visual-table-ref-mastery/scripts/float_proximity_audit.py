#!/usr/bin/env python3
"""Audit Float-to-Prose Proximity and Late-Section Spill in a compiled CCF-A PDF.

Checks for every Figure N, Table N, and Algorithm N:
  1. Caption page `p_cap` (where 'Figure N:' / 'Table N:' / 'Algorithm N' is rendered).
  2. First prose discussion page `p_prose` (excluding abstract / Section 1 intro / Section 6 roadmap).
  3. Delta `dp = p_cap - p_prose`:
       - PASS (Ideal): dp == 0 (same page!)
       - ACCEPTABLE:   abs(dp) == 1 (adjacent page across column break)
       - FAIL:         abs(dp) >= 2 (stranded far from discussion!)
  4. Late-section spill: flags FAIL if an experimental float lands on a page after Related Work starts
     while its prose was earlier.
"""
import re, sys
import fitz


def audit_pdf(pdf_path: str) -> int:
    doc = fitz.open(pdf_path)
    pages_txt = [pg.get_text() for pg in doc]

    # Locate section start pages (1-indexed)
    rel_work_page = None
    concl_page = None
    body_start_for_exp = 2  # skip page 1-2 intro bullet mentions when matching Section 3+ floats
    for idx, t in enumerate(pages_txt, 1):
        if rel_work_page is None and re.search(r"(?m)^\s*(?:\d+\s+)?(?:RELATED WORK|Related Work)\s*$", t):
            rel_work_page = idx
        if concl_page is None and re.search(r"(?m)^\s*(?:\d+\s+)?(?:CONCLUSION|Conclusion)\s*$", t):
            concl_page = idx

    floats = []
    for kind in ("Figure", "Table", "Algorithm"):
        cap_pat = re.compile(rf"(?m)^\s*{kind}\s+(\d+)\s*(?:[:.]|\s+[A-Z])")
        seen_nums = {}
        for pno, t in enumerate(pages_txt, 1):
            for m in cap_pat.finditer(t):
                num = int(m.group(1))
                # Distinguish caption line from inline 'Figure 1 shows...'
                line = t[m.start():t.find("\n", m.start())] if "\n" in t[m.start():] else t[m.start():]
                if kind in ("Figure", "Table") and not re.match(rf"^\s*{kind}\s+{num}\s*:", line):
                    continue
                if kind == "Algorithm" and re.search(r"\b(formalizes|lines?|executes|enforces|halts|is)\b", line):
                    continue
                if num not in seen_nums:
                    seen_nums[num] = pno

        for num in sorted(seen_nums):
            p_cap = seen_nums[num]
            ref_pat = re.compile(rf"\b{kind}s?\s+(?:\d+[–-]{num}\b|{num}\b)(?!\s*:)")
            mention_pages = []
            for pno, t in enumerate(pages_txt, 1):
                # Remove the caption line itself before searching mentions
                t_clean = re.sub(rf"(?m)^\s*{kind}\s+{num}\s*:.*$", "", t)
                if kind == "Algorithm":
                    t_clean = re.sub(rf"(?m)^\s*Algorithm\s+{num}\s+[A-Z].*$", "", t_clean)
                if ref_pat.search(t_clean):
                    mention_pages.append(pno)
            # Filter out Page 1-2 intro forward pointers if there is a main-section mention on page >= 3
            non_intro = [p for p in mention_pages if p >= 3] or mention_pages
            # Pick the mention closest to the actual analysis section (first non-intro mention)
            p_prose = non_intro[0] if non_intro else p_cap
            floats.append((kind, num, p_prose, p_cap, mention_pages))

    print(f"=== Float-to-Prose Proximity Audit: {pdf_path} (Pages={len(doc)}, RelWork=p.{rel_work_page}, Concl=p.{concl_page}) ===")
    fails = 0
    for kind, num, p_prose, p_cap, all_m in floats:
        dp = p_cap - p_prose
        spilled = rel_work_page is not None and p_cap > rel_work_page and p_prose <= rel_work_page
        status = "PASS (same page)" if dp == 0 else ("OK (adj page)" if abs(dp) == 1 and not spilled else "FAIL")
        if status == "FAIL":
            fails += 1
        extra = " [SPILLED PAST RELATED WORK!]" if spilled else ""
        print(f"  {kind:9s} {num:2d} | prose=p.{p_prose:2d} | float=p.{p_cap:2d} | delta={dp:+2d} | mentions={all_m} -> {status}{extra}")
    print(f"Summary: {len(floats)} floats audited, {fails} FAIL(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(audit_pdf(sys.argv[1]))
