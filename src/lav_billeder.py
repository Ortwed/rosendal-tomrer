"""Genererer alle billedfiler fra uploads. Idempotent."""
from PIL import Image, ImageOps
import os, sys
U='/mnt/user-data/uploads'; O=os.path.join(os.path.dirname(__file__),'..','docs')
img=os.path.join(O,'images'); os.makedirs(img,exist_ok=True)
for f in ['logo_2.jpg','logo.png','firmabil_1.jpg']:
    if not os.path.exists(os.path.join(U,f)): sys.exit('MANGLER: '+f)

# Fuldt logo, beskaaret stramt
logo=Image.open(f'{U}/logo_2.jpg').convert('RGB')
g=ImageOps.invert(logo.convert('L')).point(lambda v:255 if v>40 else 0)
bbox=g.getbbox(); pad=12
logo=logo.crop((bbox[0]-pad,bbox[1]-pad,bbox[2]+pad,bbox[3]+pad))
h=150; lw=round(logo.width*h/logo.height)
logo.resize((lw,h),Image.LANCZOS).save(f'{img}/logo.webp',quality=90)
logo.resize((lw*2,h*2),Image.LANCZOS).save(f'{img}/logo.png',optimize=True)
# Hvid variant til moerk footer
L=logo.convert('L'); a=ImageOps.invert(L).point(lambda v:min(255,int(v*1.5)))
w=Image.new('RGBA',logo.size,(255,255,255,0)); w.putalpha(a)
w.resize((lw,h),Image.LANCZOS).save(f'{img}/logo-hvid.png',optimize=True)
print('logo',lw,h)

# Monogram -> favicon + apple-touch-icon
m=Image.open(f'{U}/logo.png').convert('RGB')
gm=ImageOps.invert(m.convert('L')).point(lambda v:255 if v>40 else 0); bb=gm.getbbox()
m=m.crop(bb); s=max(m.size); sq=Image.new('RGB',(s,s),'white'); sq.paste(m,((s-m.width)//2,(s-m.height)//2))
sq.resize((48,48),Image.LANCZOS).save(f'{O}/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
at=Image.new('RGB',(180,180),'white'); at.paste(sq.resize((150,150),Image.LANCZOS),(15,15)); at.save(f'{O}/apple-touch-icon.png')
sq.resize((96,96),Image.LANCZOS).save(f'{img}/monogram.png',optimize=True)

# Firmabil: hero + OG
v=Image.open(f'{U}/firmabil_1.jpg').convert('RGB')
v.resize((1440,1080),Image.LANCZOS).save(f'{img}/firmabil.webp',quality=80)
v.resize((900,675),Image.LANCZOS).save(f'{img}/firmabil-900.webp',quality=78)
# OG 1200x630 med bilen i fokus
W,H=v.size; ch=round(W*630/1200); top=min(H-ch, 470)
v.crop((0,top,W,top+ch)).resize((1200,630),Image.LANCZOS).save(f'{img}/og-forside.jpg',quality=84,optimize=True)
for f in sorted(os.listdir(img)): print(f, os.path.getsize(f'{img}/{f}')//1024,'KB')

# --- Billeder klippet ud af skaermbilleder af det gamle site (07-10-2026) ---
SK = {  # fil: (bredde det blev vist i, beskaering i visningskoordinater)
    'bro':     ('1791354855588_image.png', 2576, (190, 117, 1237, 896)),
    'sign':    ('1791354855588_image.png', 2576, (1368, 965, 1535, 1135)),
    'jobbil':  ('1791354908510_image.png', 2456, (344, 347, 931, 932)),
    'baenk-1': ('1791354882011_image.png', 2576, (1264, 1026, 1627, 1284)),
    'baenk-2': ('1791354882011_image.png', 2576, (1675, 1026, 2037, 1284)),
}
for navn, (f, vist, box) in SK.items():
    p = f'{U}/{f}'
    if not os.path.exists(p): sys.exit('MANGLER: ' + f)
    im = Image.open(p).convert('RGB'); s = im.width / vist
    im = im.crop(tuple(round(v * s) for v in box))
    if navn == 'sign':  # blæk -> transparent PNG
        L = im.convert('L'); a = ImageOps.invert(L).point(lambda v: 0 if v < 40 else min(255, v * 2))
        t = Image.new('RGBA', im.size, (22, 32, 43, 0)); t.putalpha(a); t.save(f'{img}/signatur.png', optimize=True)
    elif navn == 'bro':
        im.save(f'{img}/bro-ipe.webp', quality=80)
        im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS).save(f'{img}/bro-ipe-720.webp', quality=78)
        W, H = im.size; ch = round(W * 630 / 1200); top = (H - ch) // 2
        im.crop((0, top, W, top + ch)).resize((1200, 630), Image.LANCZOS).save(f'{img}/og-forside.jpg', quality=84, optimize=True)
    else:
        im.save(f'{img}/{navn}.webp', quality=80)
    print(navn, im.size)

with open(f'{img}/hex-hvid.svg', 'w') as fh:
    fh.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 340"><path fill="#fff" d="M150 0l150 85v170L150 340 0 255V85z"/></svg>\n')
