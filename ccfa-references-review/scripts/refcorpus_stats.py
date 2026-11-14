#!/usr/bin/env python3
"""Measure reference/citation practice in published-paper PDFs (numeric [n] styles + ACL author-year)."""
import re, sys, json, os, statistics as st
CIT = re.compile(r'\[(\d{1,3}(?:\s*[,–\-]\s*\d{1,3})*)\]')
TOPV = re.compile(r'(?i)SIGMOD|PVLDB|Proc\.? ?VLDB|VLDB|ICDE|Manag\.? ?Data|PACMMOD|\bACL\b|EMNLP|NAACL|COLING|NeurIPS|Neural Information|ICML|ICLR|Learning Representations|KDD|CIDR|OSDI|SOSP|NSDI|EuroSys|TODS|Trans\.|Transactions|Journal|AAAI|WWW|Web Conference|SIGIR|IJCAI|CIKM|WSDM|EDBT|PODS|ICDT|DaMoN|HILDA|aiDM|Proceedings|Conference|Symposium|Workshop')
ARX = re.compile(r'(?i)arxiv|corr\b|preprint')
WEB = re.compile(r'(?i)https?://|\[n\.d\.\]|accessed|github')
def expand(g):
    out=[]
    for part in re.split(r'\s*,\s*', g):
        m=re.match(r'(\d+)\s*[–\-]\s*(\d+)$',part)
        if m:
            a,b=int(m.group(1)),int(m.group(2))
            if 0<b-a<40: out+=list(range(a,b+1))
        elif part.strip().isdigit(): out.append(int(part))
    return out
def find_refs(lines):
    hs=[i for i,l in enumerate(lines) if re.match(r'^\s*(REFERENCES|References|R EFERENCES|Bibliography)\s*$',l)]
    cands=hs[-3:] if hs else []
    if not cands:
        st_=[i for i,l in enumerate(lines) if re.match(r'\s*\[1\]\s',l)]
        cands=st_[-1:]
    best=None
    for s in cands:
        entries={}; cur=None
        for j in range(s+1,len(lines)):
            m=re.match(r'\s*\[(\d{1,3})\]\s*(.*)',lines[j])
            if m:
                cur=int(m.group(1)); entries.setdefault(cur,''); entries[cur]+=' '+m.group(2); continue
            if re.match(r'^\s*(APPENDIX|Appendix|A\s+[A-Z][A-Z ]{4,})\s*$',lines[j]) and len(entries)>5: break
            if cur is not None: entries[cur]+=' '+lines[j].strip()
        if entries:
            mx=max(entries); cover=len([k for k in range(1,mx+1) if k in entries])/mx
            if cover>0.8 and (best is None or len(entries)>len(best[1])): best=(s,entries)
    return best
def heading_kind(h):
    u=re.sub(r'[^A-Z]','',h.upper())
    if 'INTRODUCTION' in u: return 'intro'
    if 'RELATED' in u or 'LITERATURE' in u or 'PRIOR WORK' in u: return 'related'
    if re.search(r'EXPERIMENT|EVALUATION|EMPIRICAL|RESULTS|BENCHMARKING RESULTS|ANALYSIS OF', u): return 'exp'
    if re.search(r'CONCLUSION|ACKNOWLEDG|LIMITATION|DISCUSSION|LESSONS|FUTURE', u): return 'other'
    if re.search(r'BACKGROUND|PRELIMINAR|PROBLEM|MOTIVATION', u): return 'prelim'
    return 'method'
HEAD = re.compile(r'^\s*(?:(\d{1,2})\.?|([IVX]{1,5})\.)\s+([A-Z][A-Za-z0-9 ,:&\-/]{2,60})\s*$')
KNOWN = re.compile(r'(?i)^(introduction|related work|background|preliminar|method|approach|methodology|experiment|evaluation|results|analysis|conclusion|limitations|discussion|problem|overview|system|framework|benchmark|dataset)')
def sections(body):
    secs=[]; cur='front'; buf=[]
    for l in body:
        m=HEAD.match(l)
        if m:
            h=m.group(3); words=h.split()
            ok = (m.group(2) is not None) or (sum(c.isupper() for c in h if c.isalpha())>=0.8*sum(c.isalpha() for c in h) and len(words)<=10) or (KNOWN.match(h) and len(words)<=6)
            if ok:
                secs.append((cur,buf)); cur=heading_kind(m.group(3)); buf=[]; continue
        buf.append(l)
    secs.append((cur,buf)); return secs
def pubyear(fn):
    m=re.search(r'arxiv_(\d\d)',fn)
    if m: return 2000+int(m.group(1))
    m=re.search(r'acl_(\d{4})',fn)
    if m: return int(m.group(1))
    return None
def analyze(path, pyear=None, kind=None):
    txt=open(path,errors='ignore').read()
    txt=re.sub(r'(?m)^(\d{1,2}|[IVX]{1,5}\.)\n([A-Z][^\n]{2,60})$', r'\1 \2', txt)
    lines=txt.split('\n')
    if not re.search(r'(?m)^\s*\[1\]\s', txt): return analyze_ay(txt, path, pyear, kind)
    r=find_refs(lines)
    res={'file':os.path.basename(path),'type':kind}
    if not r: return analyze_ay(txt, path, pyear, kind)
    s,ent=r
    body=lines[:s]
    # drop trailing REFERENCES heading
    N=len(ent); res['n_refs']=N
    yrs=[]; arx=0; top=0; web=0; doi=0; pages=0
    for k,e in ent.items():
        ys=[int(y) for y in re.findall(r'(?<!\d)(19[5-9]\d|20[0-2]\d)(?!\d)',e)]
        if ys: yrs.append(max(ys) if max(ys)<=2026 else min(ys))
        isweb=bool(WEB.search(e)) and not TOPV.search(e)
        isarx=bool(ARX.search(e)) and not re.search(r'(?i)In Proceedings|Proc\. ACM|PVLDB|Proc\. VLDB',e)
        if isweb: web+=1
        elif isarx: arx+=1
        elif TOPV.search(e): top+=1
        if re.search(r'(?i)doi|10\.\d{4,}/',e): doi+=1
        if re.search(r'\d+\s*[–\-]\s*\d+|pages|pp\.',e.replace(str(ys[-1]) if ys else 'xx','')): pages+=1
    py=pyear or (max(yrs) if yrs else 2025)
    res.update(pubyear=py, recent3=round(sum(1 for y in yrs if y>=py-2)/max(1,len(yrs)),2),
               old10=round(sum(1 for y in yrs if y<=py-10)/max(1,len(yrs)),2),
               peer=round(top/N,2), arxiv=round(arx/N,2), web=round(web/N,2), doi=round(doi/N,2), pages=round(pages/N,2))
    secs=sections(body)
    per={}; groups=0; singles=0; cited=set(); paras_rel=[]
    for kname,buf in secs:
        t='\n'.join(buf)
        c=[expand(g) for g in CIT.findall(t)]
        c=[x for x in c if x and max(x)<=N]
        per.setdefault(kname,[0,0])
        per[kname][0]+=len(c); per[kname][1]+=sum(len(x) for x in c)
        for x in c:
            cited.update(x)
            if len(x)>1: groups+=1
            else: singles+=1
        if kname=='related':
            for p in re.split(r'\n\s*\n',t):
                if len(p)>300: paras_rel.append(len(CIT.findall(p)))
    res['cites_by_section']={k:v[0] for k,v in per.items()}
    res['refs_by_section']={k:v[1] for k,v in per.items()}
    res['grouped_share']=round(groups/max(1,groups+singles),2)
    res['cite_instances']=groups+singles
    res['uncited_refs']=N-len(cited & set(range(1,N+1)))
    res['related_paras']=len(paras_rel); res['cites_per_related_para']=round(per.get('related',[0])[0]/len(paras_rel),1) if paras_rel else None
    caps=re.findall(r'(?m)^\s*((?:Figure|Fig\.|Table|TABLE)\s+[\dIVX]+[:.].{0,400}?)(?:\n\s*\n)', '\n'.join(body), flags=re.S)
    res['captions']=len(caps); res['captions_with_cite']=sum(1 for c in caps if CIT.search(c))
    return res
AYC = re.compile(r'\(([^()]*?\b(?:19|20)\d\d[a-z]?)\)')
AYN = re.compile(r'[A-Z][A-Za-z\-]+(?: et al\.| and [A-Z][A-Za-z\-]+)? \((?:19|20)\d\d[a-z]?\)')
def analyze_ay(txt, path, pyear, kind):
    lines=txt.split('\n')
    hs=[i for i,l in enumerate(lines) if re.match(r'^\s*References\s*$',l)]
    res={'file':os.path.basename(path),'type':kind,'style':'author-year'}
    if not hs: res['error']='no refs'; return res
    s=hs[-1]; rest='\n'.join(lines[s+1:])
    m=re.search(r'(?m)^\s*(A\s+[A-Z][a-z]+|Appendix)',rest)
    if m: rest=rest[:m.start()]
    blocks=[b.replace('\n',' ').strip() for b in re.split(r'\n\s*\n',rest) if re.search(r'(19|20)\d\d',b) and len(b)>40]
    # a block may hold several entries; split on '. YEAR.' boundaries heuristically
    ents=[]
    for b in blocks:
        parts=re.split(r'(?<=[\.\)])\s+(?=[A-Z][a-zA-Z\-]+(?:,| and)[^.]{0,200}?\.\s(?:19|20)\d\d[a-z]?\.)',b)
        ents+=[p for p in parts if len(p)>30]
    N=len(ents); res['n_refs']=N
    yrs=[]; arx=top=web=0
    for e in ents:
        ys=[int(y) for y in re.findall(r'(?<!\d)(19[5-9]\d|20[0-2]\d)(?!\d)',e)]
        if ys: yrs.append(ys[0])
        if WEB.search(e) and not TOPV.search(e): web+=1
        elif ARX.search(e) and not re.search(r'(?i)Proceedings',e): arx+=1
        elif TOPV.search(e): top+=1
    py=pyear or 2025
    res.update(pubyear=py, recent3=round(sum(1 for y in yrs if y>=py-2)/max(1,len(yrs)),2), old10=round(sum(1 for y in yrs if y<=py-10)/max(1,len(yrs)),2),
        peer=round(top/max(1,N),2), arxiv=round(arx/max(1,N),2), web=round(web/max(1,N),2))
    body=lines[:s]; secs=sections(body); per={}; g=sgl=0; paras=[]
    for kname,buf in secs:
        t=' '.join(buf)
        inst=[]
        for c in AYC.findall(t):
            n=len(re.findall(r'(?:19|20)\d\d',c))
            if re.search(r'[A-Z][a-z]',c): inst.append(n)
        inst+= [1]*len(AYN.findall(t))
        per[kname]=per.get(kname,0)+len(inst)
        g+=sum(1 for n in inst if n>1); sgl+=sum(1 for n in inst if n==1)
        if kname=='related':
            for p in re.split(r'\n\s*\n','\n'.join(buf)):
                if len(p)>300: paras.append(len(AYC.findall(p))+len(AYN.findall(p)))
    res['cites_by_section']=per; res['grouped_share']=round(g/max(1,g+sgl),2); res['cite_instances']=g+sgl
    res['related_paras']=len(paras); res['cites_per_related_para']=round(per.get('related',0)/len(paras),1) if paras else None
    return res
if __name__=='__main__':
    print(json.dumps(analyze(sys.argv[1]),ensure_ascii=False))
