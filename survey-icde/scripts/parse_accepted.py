import re, html, json, sys
def clean(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
out = []
# 2024: session tables
t = open('icde2024_github_io_papers_html.html').read()
for m in re.finditer(r'<th class="tblCellHead"[^>]*>(.*?)</th>(.*?)</table>', t, re.S):
    sess = clean(m.group(1))
    for li in re.finditer(r'<li><a[^>]*>(.*?)</a><br/><span[^>]*>(.*?)</span>', m.group(2), re.S):
        out.append({"year": 2024, "session": re.sub(r'\s*\[.*?\]', '', sess), "title": clean(li.group(1)), "authors": clean(li.group(2))})
# 2025: session headers "x.y: Name" then "ID | Title"
t = open('ieee-icde_org_2025_research-papers_.html').read()
lines = [clean(x) for x in re.split(r'</p>', t)]
sess = None
for i, l in enumerate(lines):
    if re.match(r'^\d+\.\d+\s*:\s*\S', l): sess = l.split(':', 1)[1].strip()
    m = re.match(r'^(\d+)\s*\|\s*(.+)$', l)
    if m and sess:
        out.append({"year": 2025, "session": sess, "title": m.group(2).strip(), "authors": lines[i+1] if i+1 < len(lines) else ""})
# 2026 / 2027R1: numbered list items; capture section headings h2/h3
for f, y in [('icde2026_github_io_accepted-papers_html.html', 2026), ('../../01_guidelines/raw/accepted-papers.html', 2027)]:
    t = open(f).read()
    pos = [(m.start(), clean(m.group(1))) for m in re.finditer(r'<h[1-4][^>]*>(.*?)</h[1-4]>', t, re.S)]
    for m in re.finditer(r'<li class="paper-item">(.*?)</li>', t, re.S):
        sec = [p for p in pos if p[0] < m.start()]
        ti = re.search(r'<div class="title">(.*?)</div>', m.group(1), re.S)
        au = re.findall(r'<span class="author-name">(.*?)</span>\s*<span class="affiliation">(.*?)</span>', m.group(1), re.S)
        out.append({"year": y, "session": sec[-1][1] if sec else "", "title": clean(ti.group(1)),
                    "authors": "; ".join(f"{clean(a)} {clean(b)}" for a, b in au)})
json.dump(out, open('../accepted_all.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter((o['year']) for o in out))
for y in [2024, 2025, 2026, 2027]: print(y, Counter(o['session'] for o in out if o['year'] == y).most_common(80))
