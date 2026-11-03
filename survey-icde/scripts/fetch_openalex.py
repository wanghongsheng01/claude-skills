import json, time, urllib.request, urllib.parse, re
def get(url):
    for i in range(4):
        try: return json.load(urllib.request.urlopen(url, timeout=60))
        except Exception as e: time.sleep(2 + 2*i)
    return None
works = []
for y in [2024, 2025, 2026]:
    cursor = 1
    while cursor:
        u = ("https://api.openalex.org/works?filter=primary_location.source.id:S4210210321,publication_year:%d&per-page=200&page=%s"
             "&select=id,doi,display_name,publication_year,abstract_inverted_index,cited_by_count,biblio&mailto=research@example.org") % (y, cursor)
        d = get(u)
        if not d: break
        works += d['results']; cursor += 1
        if not d['results']: break
    print(y, len([w for w in works if w['publication_year'] == y]))
def ab(inv):
    if not inv: return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps); return " ".join(w for _, w in pos)
for w in works: w['abstract'] = ab(w.pop('abstract_inverted_index'))
json.dump(works, open('openalex_icde.json', 'w'), ensure_ascii=False)
