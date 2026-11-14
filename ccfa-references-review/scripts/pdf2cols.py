import pymupdf, sys
def extract(pdf):
    doc=pymupdf.open(pdf); out=[]
    for pg in doc:
        W=pg.rect.width
        bl=[b for b in pg.get_text('blocks') if b[6]==0]
        full=[b for b in bl if b[0]<W*0.4 and b[2]>W*0.6]
        def key(b):
            col = 0 if b[0]<W*0.45 else 1
            if b in full: col=0
            return (col,b[1])
        for b in sorted(bl,key=key):
            out.append(b[4].rstrip()); out.append('')
    return '\n'.join(out)
if __name__=='__main__':
    open(sys.argv[2],'w').write(extract(sys.argv[1]))
