#!/usr/bin/env python3
"""montage: stack PNG crops vertically with filename labels. Usage: montage.py out.png a.png b.png ..."""
import sys,glob,os
from PIL import Image, ImageDraw
out=sys.argv[1]; files=sys.argv[2:]
ims=[Image.open(f) for f in files]
W=max(i.width for i in ims); H=sum(i.height+30 for i in ims)
S=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(S); y=0
for f,i in zip(files,ims):
    d.text((5,y+5),os.path.basename(f),fill='red'); y+=30; S.paste(i,(0,y)); y+=i.height
S.save(out); print(out,S.size)
