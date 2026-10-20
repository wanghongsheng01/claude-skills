"""Register statistics of LaTeX papers: sentence length, share above 35 words, parentheses and semicolons per 100 words.
Usage: python3 style_stats.py DIR [DIR ...]   (each DIR holds the .tex sources of one paper)
"""
import re,sys,glob
def clean(s):
    s=re.sub(r'(?<!\\)%.*','',s)
    s=re.sub(r'\\begin\{(equation|align|table|figure|algorithm)\*?\}.*?\\end\{\1\*?\}','',s,flags=re.S)
    s=re.sub(r'\$[^$]*\$','X',s)
    s=re.sub(r'\\(cite[pt]?|ref|eqref|label)\{[^}]*\}','R',s)
    return s
for d in sys.argv[1:]:
    txt=''.join(open(f,errors='ignore').read() for f in glob.glob(d+'/**/*.tex',recursive=True) if 'check' not in f and 'numbers' not in f and '/tables/' not in f)
    t=clean(txt)
    m=re.search(r'\\section\{Intro.*?(?=\\section)',t,re.S)
    body=t
    sents=[x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z\\])',re.sub(r'\s+',' ',body)) if len(x.split())>3]
    L=[len(x.split()) for x in sents]
    par=body.count('(');semi=body.count(';');words=len(body.split())
    print(f"{d:14s} sents={len(L)} meanlen={sum(L)/len(L):.1f} >35w={sum(l>35 for l in L)/len(L):.0%} paren/100w={100*par/words:.2f} semi/100w={100*semi/words:.2f}")
