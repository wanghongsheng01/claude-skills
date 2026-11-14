#!/usr/bin/env python3
"""corpus_stats.py OUTDIR: aggregate layoutlint --stats-only JSON of a corpus of published papers
(page fill, holes, float placement/width, caption length, float-to-mention distance, last page)."""
import json,glob,collections,statistics as st,re,os,sys
rows=[];agg=collections.defaultdict(list);C=collections.Counter()
for f in sorted(glob.glob(os.path.join(sys.argv[1] if len(sys.argv)>1 else 'corpus_out','*','layoutlint.json'))):
    r=json.load(open(f)); n=f.split('/')[1]; g=r['geometry']; colH=g['bot']-g['top']
    P=r['pages']; refp=r['ref_page'] or len(P)+1
    body=[p for p in P if p['page']<refp and p['page']!=len(P)]
    C['papers']+=1; C['pages']+=len(P)
    for p in body:
        mh=max([h['h'] for h in p['holes'] if h['where']!='top'] or [0]); agg['maxhole_frac'].append(mh/colH)
        agg['fill'].append(sum(p['fill'])/len(p['fill']))
        agg['floats_per_page'].append(p['nfloats'])
        if p.get('float_only'): C['float_only_pages']+=1; agg['float_page_fill'].append(sum(p['fill'])/len(p['fill']))
    holes=[(p['page'],h) for p in body for h in p['holes'] if h['where']!='top' and h['h']/colH>=0.10]
    if holes: C['papers_with_hole10']+=1; agg['hole_list'].append((n,[(pg,round(h['frac'],2),h['where']) for pg,h in holes]))
    fl=[x for x in r['floats'] if x['page']<refp]
    for x in fl:
        C['floats']+=1; C['float_'+x['kind']]+=1; C['place_'+x['placement']]+=1; C['full' if x['full'] else 'colw']+=1
        C[('full_' if x['full'] else 'col_')+x['kind']]+=1
        agg['capwords_'+x['kind']].append(x['cap_words'])
        if x['first_ref_page']:
            d=x['page']-x['first_ref_page']; agg['dist'].append(d)
    lp=r.get('last_page')
    if lp: agg['last_imb'].append(lp['imbalance']); agg['last_used'].append(lp['used'])
    sev=collections.Counter(x['severity'] for x in r['findings'] if x['rule'] in('L1','L2','L3'))
    rows.append((n,len(P),sev['blocker'],sev['major']))
q=lambda a,p: sorted(a)[min(len(a)-1,int(len(a)*p))]
out={}
out['counts']=dict(C)
for k in ['maxhole_frac','fill','floats_per_page','float_page_fill','last_imb','last_used','capwords_Figure','capwords_Table','dist']:
    a=agg[k]
    if a: out[k]=dict(n=len(a),median=round(st.median(a),3),p90=round(q(a,.9),3),p95=round(q(a,.95),3),p99=round(q(a,.99),3),max=round(max(a),3),min=round(min(a),3))
d=agg['dist']; out['dist_hist']=dict(collections.Counter(d))
out['hole_list']=agg['hole_list']
print(json.dumps(out,indent=1))
