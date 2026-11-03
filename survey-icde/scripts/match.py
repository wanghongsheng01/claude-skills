import json, re, difflib
acc = json.load(open('accepted_all.json')); oa = json.load(open('openalex_icde.json'))
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower().replace('[experiment, analysis, and benchmark]', ''))
idx = {norm(w['display_name']): w for w in oa}
keys = list(idx)
hit = 0
for a in acc:
    a['eab'] = 'experiment, analysis' in a['title'].lower()
    k = norm(a['title']); w = idx.get(k)
    if not w and a['year'] < 2027:
        c = difflib.get_close_matches(k, keys, n=1, cutoff=0.9); w = idx[c[0]] if c else None
    if w:
        hit += 1; a.update(doi=w['doi'], abstract=w['abstract'], cites=w['cited_by_count'], pages=w.get('biblio'))
json.dump(acc, open('accepted_all.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(hit, Counter((a['year'], bool(a.get('abstract'))) for a in acc))
print('EAB', Counter(a['year'] for a in acc if a['eab']))
