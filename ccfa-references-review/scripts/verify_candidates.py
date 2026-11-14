#!/usr/bin/env python3
"""Verify candidate references before proposing them.
Input: a text file, one candidate per line:  title | first-author surname [| expected venue keyword]
Output: markdown table with status, DOI / URL, venue, year, pages, similarity. Only VERIFIED rows may be proposed."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reflint as R

def main():
    src = sys.argv[1]; cache = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser('~/.cache/reflint_cache.json')
    L = R.Lookup(cache, True); rows = []
    for line in open(src, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'): continue
        parts = [p.strip() for p in line.split('|')]
        title, author = parts[0], (parts[1] if len(parts) > 1 else None)
        exp = parts[2] if len(parts) > 2 else ''
        best = None
        for it in L.crossref_title(title, author):
            s = R.sim_cr(title, it)
            if s > 0.88 and (best is None or s > best[0]):
                best = (s, it)
        row = {'title': title, 'author': author, 'expect': exp, 'status': 'UNVERIFIED'}
        if best:
            it = best[1]
            row.update(status='VERIFIED', source='crossref', sim=round(best[0], 2), doi=it.get('DOI'),
                       venue=' '.join(it.get('container-title') or []) or (it.get('event') or {}).get('name', ''),
                       year=((it.get('published') or {}).get('date-parts') or [[None]])[0][0], pages=it.get('page', ''),
                       type=it.get('type'))
            if it.get('DOI', '').startswith('10.48550'): row['note'] = 'arXiv DOI only'
        else:
            s2 = L.s2(title=title)
            if s2 and R.sim(title, s2['title']) > 0.88:
                ext = s2.get('externalIds') or {}
                row.update(status='VERIFIED', source='semanticscholar', sim=round(R.sim(title, s2['title']), 2),
                           doi=ext.get('DOI'), dblp=ext.get('DBLP'), arxiv=ext.get('ArXiv'),
                           venue=(s2.get('venue') or ''), year=s2.get('year'))
        rows.append(row)
        L.save()
    print('| status | title | venue | year | DOI / id | pages | sim |')
    print('|---|---|---|---|---|---|---|')
    for r in rows:
        ident = r.get('doi') or (('DBLP ' + r['dblp']) if r.get('dblp') else '') or (('arXiv ' + r['arxiv']) if r.get('arxiv') else '')
        print(f"| {r['status']} | {r['title'][:90]} | {r.get('venue', '')[:60]} | {r.get('year', '')} | {ident} | {r.get('pages', '')} | {r.get('sim', '')} |")
    json.dump(rows, open(src + '.json', 'w'), indent=1, ensure_ascii=False)

if __name__ == '__main__':
    main()
