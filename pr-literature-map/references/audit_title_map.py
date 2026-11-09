#!/usr/bin/env python3
"""Audit the bundled public title map offline using only the Python standard library.

Run: python3 audit_title_map.py
Outputs JSON to stdout; never reads credentials, accesses the network, or edits files.
"""
from pathlib import Path
import collections,csv,hashlib,json,re
ROOT=Path(__file__).resolve().parent
with (ROOT/'pr_issue_date_title_map_20261109.csv').open(encoding='utf-8') as f:
 rows=list(csv.DictReader(f))
tax=json.loads((ROOT/'title_signal_taxonomy_20261109.json').read_text())
reference=json.loads((ROOT/'title_map_summary_20261109.json').read_text())
manifest=json.loads((ROOT/'sources_and_status_20261109.json').read_text())
for r in manifest['artifacts']:
 assert hashlib.sha256((ROOT/r['name']).read_bytes()).hexdigest()==r['sha256'], 'Bundled artifact hash mismatch: '+r['name']
assert len({r['doi'] for r in rows})==len(rows),'Duplicate DOI in bundled map'
for r in rows:
 for axis,cats in tax.items():
  matches={key:sorted({m.group(0).lower() for m in re.finditer(v['regex'],r['title'],re.I)}) for key,v in cats.items()}
  matches={k:v for k,v in matches.items() if v}
  assert ';'.join(matches)==r[axis+'_tags'],'Tag drift: '+r['doi']+' '+axis
  assert matches==json.loads(r[axis+'_evidence']),'Matched-span drift: '+r['doi']+' '+axis
 assert (r['core']=='True')==(r['period']=='main' and not r['excluded_reason']),'Core flag mismatch'
 if r['title'].lower().startswith(('removed:','withdrawn:')):
  assert r['excluded_reason']=='nonresearch_publication','Withdrawal/removal must be excluded'
core=[r for r in rows if r['core']=='True'];counts=collections.Counter(r['year'] for r in core)
expected=reference['cohorts']['main_issue_core']
assert len(core)==expected['n'];assert dict(counts)==expected['years']
axes={}
for axis in tax:
 c=collections.Counter(k for r in core for k in r[axis+'_tags'].split(';') if k)
 for z in expected['axes'][axis]['categories']:assert c[z['tag']]==z['n']
 axes[axis]={'matched_rows':sum(bool(r[axis+'_tags']) for r in core),'unknown_rows':sum(not r[axis+'_tags'] for r in core),'counts':dict(c)}
print(json.dumps({'status':'PASS_OFFLINE_REPLAY','records':len(rows),'core':len(core),'years':dict(counts),'axes':axes,'scope':'Replays title rules and core membership only; not a scientific-problem accuracy or acceptance-preference validation'},ensure_ascii=False,indent=2))
