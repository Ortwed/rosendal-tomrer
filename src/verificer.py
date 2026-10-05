"""Tjekker sitet før levering. Exit 1 ved fejl."""
import os, re, sys, json, itertools
sys.path.insert(0, os.path.dirname(__file__))
from site_shared import YDELSER, GA_ID, FORMSPREE_ID

R = os.path.join(os.path.dirname(__file__), "..", "docs")
fejl, adv = [], []
sider = sorted(f for f in os.listdir(R) if f.endswith(".html"))
linket = set()

def tekst(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
    return re.sub(r"<[^>]+>", " ", h)

for f in sider:
    h = open(os.path.join(R, f), encoding="utf-8").read()
    t = lambda m: fejl.append(f"{f}: {m}")
    if len(re.findall(r"<h1[\s>]", h)) != 1: t("ikke præcis ét H1")
    m = re.search(r"<title>(.*?)</title>", h)
    if not m or len(m.group(1)) > 60: t("title mangler eller > 60")
    m = re.search(r'name="description" content="(.*?)"', h)
    if not m or len(m.group(1)) > 158: t("description mangler eller > 158")
    if f != "404.html" and 'rel="canonical"' not in h: t("canonical mangler")
    if '<html lang="da">' not in h: t("lang mangler")
    if 'href="tel:+4550700505"' not in h: t("tel-link mangler")
    for img in re.findall(r"<img[^>]*>", h):
        if not re.search(r'alt="[^"]+"', img) and 'alt=""' not in img: t(f"alt mangler: {img[:60]}")
        for src in re.findall(r'src="([^"]+)"', img):
            if not src.startswith("http") and not os.path.exists(os.path.join(R, src.lstrip("/"))): t(f"billede findes ikke: {src}")
        for src in re.findall(r'srcset="([^"]+)"', img):
            for s in [x.strip().split(" ")[0] for x in src.split(",")]:
                if not os.path.exists(os.path.join(R, s)): t(f"srcset findes ikke: {s}")
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(ld)
        except Exception: t("ugyldig JSON-LD")
    for href in re.findall(r'href="([^"#?]+)', h):
        if href.startswith(("http", "tel:", "mailto:")): continue
        p = href.lstrip("/") or "index.html"
        linket.add(p)
        if not os.path.exists(os.path.join(R, p)): t(f"død intern link: {href}")
    if re.search(r" — ", tekst(h)): t("spaced em-dash i tekst")
    if re.search(r"rosendal-tomrer\.dk/wp-content", h): t("hotlink til gammel WordPress")

for s, _ in YDELSER:
    h = open(os.path.join(R, s + ".html"), encoding="utf-8").read()
    if '"FAQPage"' not in h: fejl.append(f"{s}: FAQPage mangler")

for f in sider:
    if f not in linket and f not in ("404.html",): fejl.append(f"forældreløs side: {f}")

# Ordoverlap mellem ydelsessider (kun brødtekst i <main>, uden faelles CTA)
def ord(s):
    h = open(os.path.join(R, s + ".html"), encoding="utf-8").read()
    h = h.split("<main>")[1].split('Andre ydelser')[0]
    h = re.sub(r'<div class="crumb">.*?</div>|<div class="btn-row">.*?</div>', ' ', h, flags=re.S)
    return set(w for w in re.findall(r"[a-zæøå]{4,}", tekst(h).lower()))
O = {s: ord(s) for s, _ in YDELSER}
maks = 0
for a, b in itertools.combinations(O, 2):
    ov = len(O[a] & O[b]) / len(O[a] | O[b])  # Jaccard
    maks = max(maks, ov)
    if ov > 0.30: adv.append(f"ordoverlap {a}/{b}: {ov:.0%}")

if not GA_ID: adv.append("GA_ID ikke sat (demo)")
if not FORMSPREE_ID: adv.append("FORMSPREE_ID ikke sat: formularen sender ikke (demo)")
for f in ["robots.txt", "sitemap.xml", "llms.txt", "favicon.ico", "apple-touch-icon.png", ".nojekyll", "images/og-forside.jpg"]:
    if not os.path.exists(os.path.join(R, f)): fejl.append(f"mangler: {f}")

print(f"{len(sider)} HTML-sider. Største ordoverlap mellem ydelsessider: {maks:.0%}")
for x in fejl: print("FEJL ", x)
for x in adv: print("ADV  ", x)
print(f"{len(fejl)} fejl, {len(adv)} advarsler")
sys.exit(1 if fejl else 0)
