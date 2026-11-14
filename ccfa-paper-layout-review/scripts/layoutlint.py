#!/usr/bin/env python3
"""layoutlint.py - page-layout lint for compiled two-column (ACM / IEEE) paper PDFs.

Detects, per page and per column:
  * blank regions (whitespace holes) inside the text block           -> rule L1 / L2
  * float-only pages and how much of them is actually filled         -> rule L3
  * stranded floats (placed before their first mention, or >1 page after) -> rule L4
  * unbalanced last page / near-empty last page                      -> rule L6
  * text outside the text block or crossing the column gutter        -> rule L7
  * section headings stranded at the bottom of a column, widow lines -> rule L8
  * (optional) LaTeX log: overfull boxes, float warnings              -> rule L7 / L9
  * (optional) source scan: \\vspace hacks, \\clearpage/\\newpage, [H]/[h!], \\FloatBarrier -> rule L5
and writes a page-annotated Markdown report, a JSON dump and PNG overlays
(red = hole, orange = float-only page slack, blue = float boxes, magenta = margin breach).

Usage:
  layoutlint.py PAPER.pdf OUTDIR [--log main.log] [--tex SRC_DIR] [--dpi 110]
                [--hole-pt 72] [--major-frac 0.15] [--blocker-frac 0.25] [--stats-only]

Read-only: the script never edits any source; it only reads the PDF / log / .tex files.
Thresholds are calibrated on published PVLDB / SIGMOD / ICDE papers (see references/LAYOUT_PRINCIPLES.md).
"""
import argparse, json, os, re, statistics, sys
from collections import Counter, defaultdict

try:
    import pymupdf as fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    sys.exit("needs PyMuPDF: pip install pymupdf")

CAP_RE = re.compile(r'^\s*(Figure|Fig\.|FIGURE|Table|TABLE|Algorithm|Listing)\s*([0-9]+|[IVXL]+)\s*[:.\-–—|]?')
REF_RE = re.compile(r'(Figures?|Figs?\.|Tables?|Tabs?\.|TABLES?|Algorithms?|Alg\.)\s*~?\s*([0-9]+|[IVXL]+)(?=[a-z]?\b)')
KIND = {'figure': 'Figure', 'fig.': 'Figure', 'figures': 'Figure', 'figs.': 'Figure', 'figs': 'Figure', 'fig': 'Figure',
        'table': 'Table', 'tables': 'Table', 'tab.': 'Table', 'tabs.': 'Table', 'algorithm': 'Algorithm',
        'algorithms': 'Algorithm', 'alg.': 'Algorithm', 'listing': 'Listing'}
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11,
         'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
REFSEC_RE = re.compile(r'^\s*(\d+\s+)?(R\s?EFERENCES|References|Bibliography)\s*$')
APPSEC_RE = re.compile(r'^\s*([A-Z0-9]+\.?\s+)?(A\s?PPENDIX|Appendix|APPENDICES|Appendices)\b')
HEAD_RE = re.compile(r'^\s*(\d+(\.\d+)*|[IVX]+\.|[A-H]\.)\s+[A-Z]')


CAPSTRICT_RE = re.compile(r'^\s*(Figure|Fig\.|FIGURE|Table|TABLE|Algorithm|Listing)\s*([0-9]+|[IVXL]+)\s*([:.|]|$)')


def is_caption(l):
    m = CAP_RE.match(l['text'])
    if not m:
        return None
    cs = CAPSTRICT_RE.match(l['text'])
    if not cs:
        return None
    if cs.group(3) == '.' and not (l['bold'] or l['text'].lstrip().startswith(('TABLE', 'Fig.', 'FIGURE'))):
        return None  # running text such as "... in Table 4. The shifted ..."
    return m


def kind_of(w):
    return KIND.get(w.lower().rstrip('~'), w)


def num_of(s):
    return int(s) if s.isdigit() else ROMAN.get(s, -1)


def union(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


# --------------------------------------------------------------------------- extraction
def extract(doc):
    pages = []
    for pno, page in enumerate(doc):
        W, H = page.rect.width, page.rect.height
        lines = []
        d = page.get_text('dict')
        for b in d['blocks']:
            if b.get('type') == 1:
                continue
            for l in b.get('lines', []):
                spans = [s for s in l['spans'] if s['text'].strip()]
                if not spans:
                    continue
                txt = ''.join(s['text'] for s in l['spans']).strip()
                x0 = min(s['bbox'][0] for s in spans); y0 = min(s['bbox'][1] for s in spans)
                x1 = max(s['bbox'][2] for s in spans); y1 = max(s['bbox'][3] for s in spans)
                if l.get('dir', (1, 0))[0] < 0.9:  # rotated text: treat as graphic
                    lines.append(dict(bbox=(x0, y0, x1, y1), text=txt, size=0, bold=False, rot=True))
                    continue
                sz = Counter()
                for s in spans:
                    sz[round(s['size'], 1)] += len(s['text'])
                size = sz.most_common(1)[0][0]
                bold = all((s['flags'] & 16) or 'Bold' in s['font'] or 'Bd' in s['font'] or '.B' in s['font'] for s in spans)
                lines.append(dict(bbox=(x0, y0, x1, y1), text=txt, size=size, bold=bold, rot=False))
        graphics = []
        for info in page.get_image_info():
            r = info['bbox']
            if r[2] - r[0] > 2 and r[3] - r[1] > 2:
                graphics.append(tuple(r))
        try:
            for dr in page.get_drawings():
                r = dr['rect']
                if r.width < 0.3 and r.height < 0.3:
                    continue
                if r.width > W * 0.95 and r.height > H * 0.95:
                    continue  # page background
                fill = dr.get('fill'); col = dr.get('color')
                if fill in [(1.0, 1.0, 1.0)] and not col:
                    continue  # white boxes do not fill space visually
                graphics.append((r.x0, r.y0, r.x1, r.y1))
        except Exception:
            pass
        pages.append(dict(no=pno + 1, W=W, H=H, lines=lines, graphics=merge_boxes(graphics, 6)))
    return pages


def merge_boxes(boxes, tol):
    boxes = [list(b) for b in boxes]
    changed = True
    while changed:
        changed = False
        out = []
        while boxes:
            a = boxes.pop()
            i = 0
            while i < len(boxes):
                b = boxes[i]
                if a[0] - tol <= b[2] and b[0] - tol <= a[2] and a[1] - tol <= b[3] and b[1] - tol <= a[3]:
                    a = [min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3])]
                    boxes.pop(i); changed = True
                else:
                    i += 1
            out.append(a)
        boxes = out
    return [tuple(b) for b in boxes]


# --------------------------------------------------------------------------- geometry
def geometry(pages):
    allsz = Counter()
    for p in pages:
        for l in p['lines']:
            if not l['rot']:
                allsz[l['size']] += len(l['text'])
    # infer body from long prose lines, not figure labels or reference glyphs
    prose_sz = Counter()
    for p in pages[:max(1, int(len(pages) * .7))]:
        for l in p['lines']:
            if not l['rot'] and len(l['text']) > 45 and 7.5 <= l['size'] <= 12:
                prose_sz[l['size']] += len(l['text'])
    body = (prose_sz or allsz).most_common(1)[0][0]
    bl = [(p, l) for p in pages for l in p['lines'] if abs(l['size'] - body) <= 0.35 and len(l['text']) > 25]
    if len(bl) < 50:
        sys.exit('layoutlint: cannot infer the text block (too little extractable body text; scanned or Type3-font PDF?)')
    W = statistics.median(p['W'] for p in pages); H = statistics.median(p['H'] for p in pages)
    x0s = sorted(l['bbox'][0] for _, l in bl); x1s = sorted(l['bbox'][2] for _, l in bl)
    left = [x for x in x0s if x < W / 2]; right = [x for x in x0s if x >= W / 2 - 5]
    two = len(right) > 0.2 * len(x0s)
    L = Counter(round(x) for x in left).most_common(1)[0][0]
    R1 = Counter(round(x) for x in x1s if x > W / 2).most_common(1)[0][0]
    if two:
        R0 = Counter(round(x) for x in right).most_common(1)[0][0]
        L1 = Counter(round(x) for x in x1s if x < W / 2 + 5).most_common(1)[0][0]
        cols = [(L, L1), (R0, R1)]
    else:
        cols = [(L, R1)]
    ys0 = sorted(l['bbox'][1] for _, l in bl); ys1 = sorted(l['bbox'][3] for _, l in bl)
    top = ys0[max(0, int(len(ys0) * 0.001))]
    bot = ys1[min(len(ys1) - 1, int(len(ys1) * 0.999))]
    # leading
    gaps = []
    for p in pages:
        cl = sorted([l for l in p['lines'] if abs(l['size'] - body) <= 0.35], key=lambda l: (round(l['bbox'][0] / 50), l['bbox'][1]))
        for a, b in zip(cl, cl[1:]):
            d = b['bbox'][1] - a['bbox'][1]
            if 5 < d < 20:
                gaps.append(d)
    lead = statistics.median(gaps) if gaps else body * 1.2
    return dict(W=W, H=H, body=body, cols=cols, two=two, top=top, bot=bot, lead=lead)


def col_of(b, g):
    """return list of column indexes the box occupies"""
    if not g['two']:
        return [0]
    (a0, a1), (b0, b1) = g['cols']
    gut = (a1 + b0) / 2
    if b[0] < gut - 8 and b[2] > gut + 8:
        return [0, 1]
    return [0] if (b[0] + b[2]) / 2 < gut else [1]


def is_header_footer(b, g):
    return b[3] < g['top'] - 1 or b[1] > g['bot'] + 1


# --------------------------------------------------------------------------- floats
def find_floats(p, g):
    lines = [l for l in p['lines'] if not is_header_footer(l['bbox'], g)]
    caps = []
    for i, l in enumerate(lines):
        m = is_caption(l)
        if m:
            caps.append((i, l, kind_of(m.group(1)), num_of(m.group(2))))
    floats = []
    elems = [('t', l['bbox'], l) for l in lines] + [('g', b, None) for b in p['graphics'] if not is_header_footer(b, g)]
    for i, l, kind, num in caps:
        cb = l['bbox']
        cols = col_of(cb, g)
        # caption block: following lines with small vertical gap and same column(s)
        cap_box = cb; words = len(l['text'].split())
        spanw = (g['cols'][cols[0]][1] - g['cols'][cols[0]][0]) if len(cols) == 1 else (g['cols'][-1][1] - g['cols'][0][0])
        prev = l
        # a caption paragraph: lines of the same size, same left edge, every line but the last nearly full width
        while (prev['bbox'][2] - prev['bbox'][0]) > 0.85 * spanw:
            nxt = [l2 for l2 in lines if col_of(l2['bbox'], g) == cols and 0 <= l2['bbox'][1] - prev['bbox'][3] < g['lead'] * 0.6
                   and abs(l2['size'] - l['size']) < 0.3 and abs(l2['bbox'][0] - cb[0]) < 3 and not CAP_RE.match(l2['text'])]
            if not nxt:
                break
            prev = min(nxt, key=lambda x: x['bbox'][1])
            cap_box = union(cap_box, prev['bbox']); words += len(prev['text'].split())
            if words > 600:
                break
        if len(cols) == 1:
            c0, c1 = g['cols'][cols[0]]
            span = (c0 - 4, c1 + 4)
        else:
            span = (g['cols'][0][0] - 4, g['cols'][-1][1] + 4)
        # grow region up and down while elements are close (float internal gaps are small)
        box = cap_box
        cand = [e for e in elems if e[1][0] >= span[0] - 2 and e[1][2] <= span[1] + 2 and e[1] != cb]
        colw = g['cols'][0][1] - g['cols'][0][0]
        body_like = lambda e: (e[0] == 't' and abs(e[2]['size'] - g['body']) <= 0.35 and (e[1][2] - e[1][0]) > 0.8 * colw
                               and len(e[2]['text']) > 40 and not CAP_RE.match(e[2]['text']))
        for direction in (-1, 1):
            grow = True; first_step = True
            while grow:
                grow = False
                tol = 18 if first_step else 11  # caption <-> body skip is larger than in-float gaps
                for e in cand:
                    b = e[1]
                    if direction < 0:
                        gap = box[1] - b[3]
                        ok = -2 < gap < tol and b[1] < box[1]
                    else:
                        gap = b[1] - box[3]
                        ok = -2 < gap < tol and b[3] > box[3]
                    if ok and not body_like(e):
                        box = union(box, b); grow = True; first_step = False
        has_graphic = any(e[0] == 'g' and e[1][1] >= box[1] - 1 and e[1][3] <= box[3] + 1 for e in cand)
        floats.append(dict(kind=kind, num=num, page=p['no'], cols=cols, bbox=box, cap=cap_box, cap_words=words,
                           full=len(cols) > 1, cap_text=l['text'][:80], graphic=has_graphic))
    # de-duplicate (same label twice e.g. "Table 3" repeated)
    seen = {}
    for f in floats:
        k = (f['kind'], f['num'])
        if k not in seen:
            seen[k] = f
    return list(seen.values())


def placement(f, g):
    b = f['bbox']; H = g['bot'] - g['top']
    if b[1] - g['top'] < 0.06 * H:
        return 'top'
    if g['bot'] - b[3] < 0.06 * H:
        return 'bottom'
    return 'here'


# --------------------------------------------------------------------------- analysis
def occupancy(p, g, floats):
    top, bot = int(g['top']), int(g['bot']) + 1
    occ = [[False] * (bot - top) for _ in g['cols']]
    boxes = [l['bbox'] for l in p['lines']] + list(p['graphics']) + [f['bbox'] for f in floats]
    for b in boxes:
        if is_header_footer(b, g):
            continue
        for c in col_of(b, g):
            for y in range(max(top, int(b[1])), min(bot, int(b[3]) + 1)):
                occ[c][y - top] = True
    return occ, top, bot


def runs(free, top):
    out = []; s = None
    for i, v in enumerate(free + [False]):
        if v and s is None:
            s = i
        elif not v and s is not None:
            out.append((top + s, top + i)); s = None
    return out


def analyse(pdf, hole_pt=72, major_frac=0.15, blocker_frac=0.25):
    doc = fitz.open(pdf)
    pages = extract(doc)
    g = geometry(pages)
    colH = g['bot'] - g['top']
    res = dict(pdf=os.path.abspath(pdf), geometry=g, pages=[], findings=[], floats=[])
    # reference section start
    ref_page = None; top_breaks = set()
    near_top = lambda l: l['bbox'][1] - g['top'] < 3 * g['lead']
    for p in pages:
        for l in p['lines']:
            if p['no'] == 1 and re.match(r'^\s*(ABSTRACT|Abstract)\s*$', l['text']):
                res.setdefault('abstract_y', l['bbox'][1])
            if REFSEC_RE.match(l['text']) and (l['bold'] or l['size'] >= g['body']):
                ref_page = ref_page or p['no']
                if near_top(l):
                    top_breaks.add(p['no'])
    res['ref_page'] = ref_page
    app_pages = set()
    for p in pages:
        for l in p['lines']:
            if APPSEC_RE.match(l['text']) and (l['bold'] or l['size'] >= g['body']) and len(l['text']) < 60 and near_top(l):
                app_pages.add(p['no'])
    breaks = app_pages | top_breaks  # sections that start at the top of a page (forced or natural break)
    res['section_breaks'] = sorted(breaks)
    # first mentions
    first = {}
    for p in pages:
        if ref_page and p['no'] > ref_page:
            break
        parts = []
        for l in p['lines']:
            capm = is_caption(l)
            parts.append(l['text'][capm.end():] if capm else l['text'])
        txt = re.sub(r'\s+', ' ', re.sub(r'([A-Za-z])-\n([a-z])', r'\1\2', '\n'.join(parts)))  # undo hyphenation
        for m in REF_RE.finditer(txt):
            first.setdefault((kind_of(m.group(1)), num_of(m.group(2))), p['no'])
        for m in re.finditer(r'(Figures|Figs\.|Tables|Tabs\.)\s*([0-9]+)\s*(?:and|,|–|-|to)\s*([0-9]+)', txt):
            for n in range(int(m.group(2)), int(m.group(3)) + 1):
                first.setdefault((kind_of(m.group(1)), n), p['no'])
    F = lambda **kw: res['findings'].append(kw)
    last = len(pages)
    for p in pages:
        fl = find_floats(p, g)
        for f in fl:
            f['placement'] = placement(f, g)
            f['first_ref_page'] = first.get((f['kind'], f['num']))
            res['floats'].append(f)
        occ, top, bot = occupancy(p, g, fl)
        body_lines = [l for l in p['lines'] if abs(l['size'] - g['body']) <= 0.35 and not is_header_footer(l['bbox'], g)
                      and not any(f['bbox'][1] - 1 <= l['bbox'][1] and l['bbox'][3] <= f['bbox'][3] + 1 for f in fl)]
        ncols = len(g['cols'])
        fill = [sum(o) / len(o) for o in occ]
        float_area = sum((f['bbox'][2] - f['bbox'][0]) * (f['bbox'][3] - f['bbox'][1]) for f in fl)
        body_area = (g['cols'][-1][1] - g['cols'][0][0]) * colH
        pinfo = dict(page=p['no'], fill=[round(x, 3) for x in fill], nfloats=len(fl), body_lines=len(body_lines),
                     float_frac=round(float_area / body_area, 3), prose_lines=0, holes=[], content_bottom=[])
        is_last = p['no'] == last
        in_refs = ref_page is not None and p['no'] >= ref_page
        prose_lines = [l for l in p['lines'] if len(l['text']) > 60 and not is_header_footer(l['bbox'], g)
                       and not is_caption(l) and abs(l['size'] - g['body']) < 0.8]
        float_only = len(prose_lines) < 4 and len(fl) > 0 and p['no'] > 1
        pinfo['float_only'] = float_only
        for c in range(ncols):
            fr = runs([not v for v in occ[c]], top)
            content = [i for i, v in enumerate(occ[c]) if v]
            cbot = top + content[-1] if content else top
            pinfo['content_bottom'].append(cbot)
            for (y0, y1) in fr:
                h = y1 - y0
                if h < hole_pt:
                    continue
                where = 'bottom' if y1 >= bot - 2 else ('top' if y0 <= top + 1 else 'middle')
                frac = h / colH
                pinfo['holes'].append(dict(col=c, y0=y0, y1=y1, h=h, frac=round(frac, 3), where=where))
                if is_last:
                    continue  # judged by the last-page rule
                if p['no'] == 1 and y1 <= res.get('abstract_y', g['top'] + 0.3 * colH) + 12:
                    continue  # unequal author blocks beside the full-width title block
                if float_only:
                    continue  # judged by the float-page rule
                sev = 'blocker' if frac >= blocker_frac else ('major' if frac >= major_frac else 'minor')
                pre_break = (p['no'] + 1) in breaks and where == 'bottom'
                if pre_break:  # hole right before References/Appendix that starts on the next page
                    sev = {'blocker': 'major', 'major': 'minor', 'minor': 'minor'}[sev]
                rule = 'L1' if where != 'top' else 'L2'
                F(rule=rule, page=p['no'], col=['left', 'right'][c] if ncols == 2 else 'single', severity=sev,
                  msg=f"blank region {h:.0f} pt high ({frac:.0%} of the column) at the {where} of the column, y={y0:.0f}-{y1:.0f}" +
                      (" [inside references]" if in_refs else '') + (" [page before References/Appendix]" if pre_break else ''), box=(g['cols'][c][0], y0, g['cols'][c][1], y1))
        if float_only:
            ff = sum(fill) / len(fill)  # vertical occupancy of the text block (robust to sub-figure gaps)
            if ff < 0.5:
                F(rule='L3', page=p['no'], col='page', severity='blocker' if ff < 0.35 else 'major',
                  msg=f"float-only page holds {len(fl)} float(s) filling only {ff:.0%} of the text block (published papers: float pages >= ~60% full, or none at all)",
                  box=(g['cols'][0][0], g['top'], g['cols'][-1][1], g['bot']))
            else:
                F(rule='L3', page=p['no'], col='page', severity='minor',
                  msg=f"float-only page ({len(fl)} floats, {ff:.0%} full); acceptable but most published papers interleave floats with text")
        # margins / gutter intrusions (one finding per page and side, worst case kept)
        worst = {}
        inside = lambda b, f: f['bbox'][0] - 2 <= b[0] and b[2] <= f['bbox'][2] + 2 and f['bbox'][1] - 2 <= b[1] and b[3] <= f['bbox'][3] + 2
        for l in p['lines']:
            b = l['bbox']
            if is_header_footer(b, g) or l['rot']:
                continue
            infull = any(f['full'] and inside(b, f) for f in fl)
            over_r = b[2] - g['cols'][-1][1]; over_l = g['cols'][0][0] - b[0]
            if over_r > 3.5 or over_l > 3.5:
                o = max(over_r, over_l)
                if o > worst.get('margin', (0,))[0]:
                    worst['margin'] = (o, dict(rule='L7', page=p['no'], col='margin', severity='major' if o > 6 else 'minor',
                                               msg=f"text extends {o:.1f} pt outside the text block: '{l['text'][:50]}'", box=b))
            elif ncols == 2 and not infull and col_of(b, g) == [0] and b[2] > g['cols'][0][1] + 3 and (
                    b[2] > g['cols'][1][0] - 1 or any(
                        col_of(o['bbox'], g) == [1] and len(o['text']) > 40 and abs(o['size'] - g['body']) <= 0.35
                        and o['bbox'][1] < b[3] and o['bbox'][3] > b[1] for o in p['lines'])):
                o = b[2] - g['cols'][0][1]
                if o > worst.get('gutter', (0,))[0]:
                    worst['gutter'] = (o, dict(rule='L7', page=p['no'], col='left', severity='major' if b[2] > g['cols'][1][0] - 2 else 'minor',
                                               msg=f"left-column content runs {o:.1f} pt into the gutter (overfull line or too-wide column float): '{l['text'][:50]}'", box=b))
        for _, f in worst.values():
            res['findings'].append(f)
        # stranded headings / widows
        for c in range(ncols):
            cl = sorted([l for l in p['lines'] if col_of(l['bbox'], g) == [c] and not is_header_footer(l['bbox'], g)],
                        key=lambda l: l['bbox'][1])
            if not cl:
                continue
            lastl = cl[-1]
            if HEAD_RE.match(lastl['text']) and lastl['bold'] and len(lastl['text']) < 70 and g['bot'] - lastl['bbox'][3] < 3 * g['lead'] and not is_last:
                F(rule='L8', page=p['no'], col=['left', 'right'][c] if ncols == 2 else 'single', severity='major',
                  msg=f"section heading stranded at the bottom of the column: '{lastl['text'][:50]}'", box=lastl['bbox'])
            firstl = cl[0]
            cw = g['cols'][c][1] - g['cols'][c][0]
            if (abs(firstl['size'] - g['body']) <= 0.35 and firstl['bbox'][1] - g['top'] < 3 and
                    (firstl['bbox'][2] - firstl['bbox'][0]) < 0.35 * cw and len(cl) > 1 and
                    cl[1]['bbox'][1] - firstl['bbox'][3] > g['lead'] * 0.6 and p['no'] > 1):
                F(rule='L8', page=p['no'], col=['left', 'right'][c] if ncols == 2 else 'single', severity='minor',
                  msg=f"possible widow (short last line of a paragraph at the top of the column): '{firstl['text'][:40]}'", box=firstl['bbox'])
        res['pages'].append(pinfo)
    # stranded floats
    for f in res['floats']:
        r = f['first_ref_page']
        if r is None:
            if f['kind'] in ('Figure', 'Table'):
                F(rule='L4', page=f['page'], col='float', severity='major',
                  msg=f"{f['kind']} {f['num']} is never referenced in the text before the references", box=f['bbox'])
            continue
        if f['page'] < r:
            F(rule='L4', page=f['page'], col='float', severity='minor' if r - f['page'] == 1 else 'major',
              msg=f"{f['kind']} {f['num']} appears on p{f['page']} before its first mention on p{r}", box=f['bbox'])
        elif f['page'] - r >= 2:
            F(rule='L4', page=f['page'], col='float', severity='major' if f['page'] - r >= 3 else 'minor',
              msg=f"{f['kind']} {f['num']} is placed {f['page'] - r} pages after its first mention (p{r})", box=f['bbox'])
    # last page
    lp = res['pages'][-1]
    if len(g['cols']) == 2:
        lb, rb = lp['content_bottom']
        used = max(lb, rb) - g['top']
        diff = abs(lb - rb) / colH
        res['last_page'] = dict(left_bottom=lb, right_bottom=rb, imbalance=round(diff, 3), used=round(used / colH, 3))
        if rb < g['top'] + 5 and used / colH < 0.5:
            pass
        elif diff > 0.25 and min(lb, rb) - g['top'] > 0.05 * colH:
            F(rule='L6', page=lp['page'], col='last', severity='major' if diff > 0.5 else 'minor',
              msg=f"last page columns unbalanced: left ends at y={lb:.0f}, right at y={rb:.0f} ({diff:.0%} of column)")
        if used / colH < 0.12 and len(res['pages']) > 2:
            F(rule='L6', page=lp['page'], col='last', severity='minor',
              msg=f"last page only {used / colH:.0%} used: a few lines spill over; tighten earlier text to save a page")
    return res


# --------------------------------------------------------------------------- log + source
def scan_log(path, res):
    if not path or not os.path.exists(path):
        return
    txt = open(path, errors='ignore').read()
    for m in re.finditer(r'Overfull \\hbox \(([\d.]+)pt too wide\) (?:in paragraph|detected) at lines? (\d+)', txt):
        pt = float(m.group(1))
        if pt > 1.0:
            res['findings'].append(dict(rule='L7', page=None, col='log', severity='major' if pt > 5 else 'minor',
                                        msg=f"Overfull \\hbox {pt:.1f} pt at source line {m.group(2)}"))
    for m in re.finditer(r'LaTeX Warning: (Float too large for page by ([\d.]+)pt[^\n]*|`h\' float specifier changed to `ht\'[^\n]*|Text page \d+ contains only floats[^\n]*)', txt):
        res['findings'].append(dict(rule='L9', page=None, col='log', severity='minor', msg='LaTeX: ' + m.group(1)[:120]))


SRC_PATTERNS = [
    (r'\\vspace\*?\{\s*-', 'L5', 'major', 'negative \\vspace (manual squeezing, forbidden by the venue templates)'),
    (r'\\vspace\*?\{\s*[0-9.]+\s*(cm|mm|in|pt|em|ex|baselineskip)', 'L5', 'info', 'positive \\vspace (fine inside a float; in running text it can open holes - check)'),
    (r'\\(clearpage|newpage|pagebreak)\b', 'L5', 'major', '\\clearpage/\\newpage in the body (forces a page end -> hole)'),
    (r'\\begin\{(figure|table)\*?\}\s*\[\s*H\s*\]', 'L5', 'major', '[H] placement (float cannot move -> holes)'),
    (r'\\begin\{(figure|table)\*?\}\s*\[\s*h!?\s*\]', 'L5', 'minor', '[h]/[h!] only placement (LaTeX changes it to [ht] or defers it)'),
    (r'\\FloatBarrier', 'L5', 'minor', '\\FloatBarrier (flushes floats; creates holes when used mid-section)'),
    (r'\\(setlength|addtolength)\{\\(abovecaptionskip|belowcaptionskip|textfloatsep|floatsep|intextsep|dbltextfloatsep|dblfloatsep|columnsep|textheight|textwidth|topmargin|oddsidemargin)\}', 'L5', 'major', 'changes template spacing / geometry'),
    (r'\\renewcommand\{\\(baselinestretch|arraystretch)\}\{0\.[0-8]', 'L5', 'major', 'shrinks line spacing'),
    (r'\\(small|footnotesize|scriptsize|tiny)\s*\\selectfont\s*$', 'L5', 'minor', 'font size switch'),
    (r'\\usepackage(\[[^]]*\])?\{(savetrees|geometry|titlesec|caption)\}', 'L5', 'major', 'package that changes template spacing'),
]


def scan_src(d, res):
    if not d or not os.path.isdir(d):
        return
    for root, _, files in os.walk(d):
        if '/.git' in root:
            continue
        for fn in files:
            if not fn.endswith('.tex'):
                continue
            pth = os.path.join(root, fn)
            for i, line in enumerate(open(pth, errors='ignore'), 1):
                code = line.split('%')[0] if not line.lstrip().startswith('%') else ''
                for pat, rule, sev, why in SRC_PATTERNS:
                    if re.search(pat, code):
                        res['findings'].append(dict(rule=rule, page=None, col='src', severity=sev,
                                                    msg=f"{os.path.relpath(pth, d)}:{i}: {why}: `{code.strip()[:80]}`"))


# --------------------------------------------------------------------------- output
COLORS = {'L1': (1, 0, 0), 'L2': (1, 0, 0), 'L3': (1, 0.55, 0), 'L4': (0, 0.4, 1), 'L6': (0.5, 0, 0.8), 'L7': (1, 0, 1), 'L8': (0, 0.6, 0)}


def overlays(pdf, res, out, dpi):
    doc = fitz.open(pdf)
    os.makedirs(os.path.join(out, 'overlays'), exist_ok=True)
    byp = defaultdict(list)
    for f in res['findings']:
        if f.get('page'):
            byp[f['page']].append(f)
    g = res['geometry']
    files = []
    for p in res['pages']:
        page = doc[p['page'] - 1]
        sh = page.new_shape()
        for f in res['floats']:
            if f['page'] == p['page']:
                sh.draw_rect(fitz.Rect(*f['bbox'])); sh.finish(color=(0, 0.3, 1), width=0.6, dashes='[2] 0')
        for h in p['holes']:
            c = g['cols'][h['col']]
            sh.draw_rect(fitz.Rect(c[0], h['y0'], c[1], h['y1']))
            sh.finish(color=(1, 0, 0), fill=(1, 0, 0), fill_opacity=0.18, width=1)
        for f in byp.get(p['page'], []):
            if f.get('box'):
                sh.draw_rect(fitz.Rect(*f['box'])); sh.finish(color=COLORS.get(f['rule'], (1, 0, 0)), width=1.6)
        sh.commit()
        y = 14
        for f in byp.get(p['page'], []):
            page.insert_text((6, y), f"{f['rule']} {f['severity']}: {f['msg'][:110]}", fontsize=6.5, color=(0.8, 0, 0)); y += 8
        if byp.get(p['page']) or p['holes']:
            fn = os.path.join(out, 'overlays', f"page-{p['page']:02d}.png")
            page.get_pixmap(dpi=dpi).save(fn); files.append(fn)
    return files


def report(res, out, files):
    g = res['geometry']
    sev = Counter(f['severity'] for f in res['findings'])
    L = [f"# layoutlint report: `{os.path.basename(res['pdf'])}`", '',
         f"- pages: {len(res['pages'])}; columns: {len(g['cols'])} {[(round(a), round(b)) for a, b in g['cols']]}; text block y={g['top']:.0f}-{g['bot']:.0f}; body {g['body']} pt; references start p{res['ref_page']}",
         f"- findings: blocker {sev['blocker']} / major {sev['major']} / minor {sev['minor']} (+{sev['info']} info leads)", '',
         '## Per-page fill', '', '| page | fill (per column) | floats | float-only | largest hole (pt, col, where) |', '|---|---|---|---|---|']
    for p in res['pages']:
        hh = max(p['holes'], key=lambda h: h['h'], default=None)
        hs = f"{hh['h']:.0f} ({hh['frac']:.0%}), {['L', 'R'][hh['col']] if len(g['cols']) == 2 else '-'}, {hh['where']}" if hh else ''
        L.append(f"| {p['page']} | {' / '.join(f'{x:.0%}' for x in p['fill'])} | {p['nfloats']} | {'yes' if p['float_only'] else ''} | {hs} |")
    L += ['', '## Floats', '', '| float | page | width | placement | first mention | caption words |', '|---|---|---|---|---|---|']
    for f in res['floats']:
        L.append(f"| {f['kind']} {f['num']} | {f['page']} | {'full' if f['full'] else 'column'} | {f['placement']} | {f['first_ref_page']} | {f['cap_words']} |")
    if 'last_page' in res:
        lp = res['last_page']
        L += ['', f"## Last page\n\nleft column ends y={lp['left_bottom']:.0f}, right y={lp['right_bottom']:.0f}; imbalance {lp['imbalance']:.0%}; used {lp['used']:.0%} of the column height"]
    L += ['', '## Findings', '', '| rule | page | column | severity | finding |', '|---|---|---|---|---|']
    order = {'blocker': 0, 'major': 1, 'minor': 2, 'info': 3}
    for f in sorted(res['findings'], key=lambda f: (order[f['severity']], f['page'] or 999)):
        L.append(f"| {f['rule']} | {f['page'] or '-'} | {f['col']} | {f['severity']} | {f['msg'].replace('|', '/')} |")
    if files:
        L += ['', '## Overlays', ''] + [f"- `{os.path.relpath(x, out)}`" for x in files]
    open(os.path.join(out, 'layoutlint.md'), 'w').write('\n'.join(L) + '\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf'); ap.add_argument('out')
    ap.add_argument('--log'); ap.add_argument('--tex')
    ap.add_argument('--dpi', type=int, default=110)
    ap.add_argument('--hole-pt', type=float, default=72)
    ap.add_argument('--major-frac', type=float, default=0.15)
    ap.add_argument('--blocker-frac', type=float, default=0.25)
    ap.add_argument('--stats-only', action='store_true', help='json only, no overlays (corpus calibration)')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    res = analyse(a.pdf, a.hole_pt, a.major_frac, a.blocker_frac)
    scan_log(a.log, res); scan_src(a.tex, res)
    files = [] if a.stats_only else overlays(a.pdf, res, a.out, a.dpi)
    json.dump(res, open(os.path.join(a.out, 'layoutlint.json'), 'w'), indent=1, default=str)
    report(res, a.out, files)
    sev = Counter(f['severity'] for f in res['findings'])
    print(f"{os.path.basename(a.pdf)}: blocker {sev['blocker']} major {sev['major']} minor {sev['minor']} -> {a.out}/layoutlint.md")


if __name__ == '__main__':
    main()
