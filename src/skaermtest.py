import os, sys
from playwright.sync_api import sync_playwright
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','docs'))
SIDER=[f for f in sorted(os.listdir(R)) if f.endswith('.html')]
VP=[(1440,900),(390,844),(360,800)]
fejl=0
os.makedirs('/home/claude/shots',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in VP:
        ctx=b.new_context(viewport={'width':w,'height':h},device_scale_factor=1)
        for f in SIDER:
            pg=ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            pg.goto('file://'+R+'/'+f); pg.wait_for_timeout(250)
            sw=pg.evaluate('document.documentElement.scrollWidth')
            if sw>w: print(f'FEJL {f} @{w}: horisontal scroll ({sw}px)'); fejl+=1
            if errs: print(f'FEJL {f} @{w}: JS {errs}'); fejl+=1
            if f=='index.html':
                # CTA over folden (banner skjult saa vi maaler layoutet)
                pg.evaluate("document.getElementById('ckBanner').classList.remove('vis')")
                bot=pg.evaluate("document.querySelector('.hero .btn-primary').getBoundingClientRect().bottom")
                print(f'index @{w}x{h}: CTA bund {bot:.0f}px', 'OK' if bot<=h else 'UNDER FOLDEN')
                if bot>h: fejl+=1
                pg.screenshot(path=f'/home/claude/shots/index-{w}.png',full_page=(w==1440 or w==390))
            if f in('hovedentreprise.html','kontakt.html','referencer.html') and w in (1440,390):
                pg.evaluate("document.getElementById('ckBanner').classList.remove('vis')")
                pg.screenshot(path=f'/home/claude/shots/{f[:-5]}-{w}.png',full_page=True)
            pg.close()
        ctx.close()
    b.close()
print('fejl:',fejl); sys.exit(1 if fejl else 0)
