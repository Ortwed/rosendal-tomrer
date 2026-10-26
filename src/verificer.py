"""Tjekker sitet foer levering. Exit 1 ved fejl.

  python3 src/verificer.py          tjekker testsiden i docs/
  python3 src/verificer.py --live   tjekker live/ (bygget med build.py --live)
"""
import os, re, sys, json, itertools
sys.path.insert(0, os.path.dirname(__file__))
from site_shared import YDELSER, GA_ID, FORMSPREE_ID, DEMO, LIVEBYG, DOMAIN, url, OMRAADE

R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "live" if LIVEBYG else "docs"))
fejl, adv = [], []
YSLUGS = [s for s, _ in YDELSER]
NOINDEX = ("404", "tak", "cookies", "lejebetingelser")   # bevidst noindex, ogsaa paa live

def laes(p): return open(os.path.join(R, p), encoding="utf-8").read()

def tekst(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S)
    return re.sub(r"<[^>]+>", " ", h)

# Alle HTML-filer. Redirect-stubs ("Siden er flyttet") er ikke rigtige sider og tjekkes for sig.
alle = []
for rod, _, filer in os.walk(R):
    for f in filer:
        if f.endswith(".html"):
            alle.append(os.path.relpath(os.path.join(rod, f), R))
stubs = [p for p in alle if "Siden er flyttet" in laes(p)]
sider = sorted(p for p in alle if p not in stubs)
def slug_af(p):
    if p == "index.html": return "index"
    if p == "404.html": return "404"
    return p[:-len("/index.html")]
linket = set()
titler = {}

for f in sider:
    h = laes(f)
    sl = slug_af(f)
    t = lambda m: fejl.append(f"{f}: {m}")
    noindex = sl in NOINDEX
    if len(re.findall(r"<h1[\s>]", h)) != 1: t("ikke præcis ét H1")
    m = re.search(r"<title>(.*?)</title>", h)
    if not m or len(m.group(1)) > 60: t("title mangler eller > 60")
    else: titler.setdefault(m.group(1), []).append(f)
    m = re.search(r'name="description" content="(.*?)"', h)
    if not m or len(m.group(1)) > 158: t("description mangler eller > 158")
    if sl != "404" and not noindex and 'rel="canonical"' not in h: t("canonical mangler")
    if sl not in ("404",) and not noindex:
        c = re.search(r'rel="canonical" href="([^"]+)"', h)
        if c and c.group(1) != DOMAIN + url(sl): t(f"canonical er forkert: {c.group(1)}")
    if '<html lang="da">' not in h: t("lang mangler")
    if 'href="tel:+4550700505"' not in h: t("tel-link mangler")
    for img in re.findall(r"<img[^>]*>", h):
        if not re.search(r'alt="[^"]+"', img) and 'alt=""' not in img: t(f"alt mangler: {img[:60]}")
        for src in re.findall(r'\ssrc="([^"]+)"', img):
            if src.startswith("http"): continue
            base = R if src.startswith("/") else os.path.join(R, os.path.dirname(f))
            if not os.path.exists(os.path.normpath(os.path.join(base, src.lstrip("/") if src.startswith("/") else src.split("?")[0]))): t(f"billede findes ikke: {src}")
        for ss in re.findall(r'srcset="([^"]+)"', img):
            for s in [x.strip().split(" ")[0] for x in ss.split(",")]:
                if not os.path.exists(os.path.normpath(os.path.join(R, os.path.dirname(f), s))): t(f"srcset findes ikke: {s}")
    alts = [a for a in re.findall(r'<img[^>]*\salt="([^"]+)"', h)]
    for a in {a for a in alts if alts.count(a) > 1}: t(f"samme alt-tekst flere gange: {a[:50]}")
    typer = []
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            j = json.loads(ld); typer.append(j.get("@type"))
            if "aggregateRating" in ld or '"Review"' in ld: t("AggregateRating/Review i schema (skal ikke bruges paa virksomheden selv)")
        except Exception: t("ugyldig JSON-LD")
    if sl not in ("index", "404", "tak", "cookies", "lejebetingelser") and "BreadcrumbList" not in typer: t("BreadcrumbList mangler")
    if sl in YSLUGS:
        if "Service" not in typer: t("Service-schema mangler")
        if "FAQPage" not in typer: t("FAQPage mangler")
    if sl == "index" and "GeneralContractor" not in typer: t("virksomhedsschema mangler paa forsiden")
    for href in re.findall(r'href="([^"]*)"', h):
        if href.startswith(("http", "tel:", "mailto:", "#")): continue
        rent = href.split("#")[0].split("?")[0]
        if sl == "404" or rent.startswith("/"):
            p = rent.lstrip("/")
        else:
            p = os.path.normpath(os.path.join(os.path.dirname(f), rent))
        if p in ("", "."): p = "index.html"
        if os.path.isdir(os.path.join(R, p)): p = os.path.join(p, "index.html")
        p = os.path.normpath(p)
        if sl != "404": linket.add(p)
        if not os.path.exists(os.path.join(R, p)): t(f"død intern link: {href}")
    brod = tekst(h)
    if re.search(r" — ", brod): t("spaced em-dash i tekst")
    if "/wp-content" in h: t("hotlink til gammel WordPress")
    for ord_, msg in ([("27010474", "forveksling med S. Rosendal ApS (CVR)"), ("S. Rosendal", "omtale af S. Rosendal ApS"),
                      ("[UDFYLD", "pladsholder paa side"), ("[VERIFIC", "pladsholder paa side"),
                      ("Jægerspris", "udenfor scope"), ("Skibby", "udenfor scope"), ("Slangerup", "udenfor scope"),
                      ("38 anmeldelser", "forkert anmeldelsestal"), ("38 verificerede", "forkert anmeldelsestal"), ("39 anmeldelser", "fast anmeldelsestal")]
                     # Hovedstadsomraadet var udenfor scope i auditten, men er med igen (20-10-2026), saa
                     # site og Google-profil siger det samme. Fejl kun hvis OMRAADE ikke laengere naevner det.
                     + ([] if "Hovedstadsområdet" in OMRAADE else [("Hovedstadsområdet", "udenfor scope (audit)")])):
        if ord_ in h: t(f"{msg}: '{ord_}'")
    if "København" in brod: adv.append(f"{f}: nævner København (udenfor aftalt scope)")
    # Moedet 23-10-2026: ordet hedder hovedentreprise, sommerhus er ingen selvstaendig ydelse, ingen udlejningspriser
    if re.search(r"totalent[er]+pr", h, re.I): t("'totalentreprise' paa siden (hedder nu hovedentreprise)")
    if 'href="/sommerhus/"' in h or re.search(r'href="(\.\./)*sommerhus/"', h): t("link til den gamle sommerhus-side")
    if "6.000" in brod: t("beløbet 6.000 kr. må ikke stå på sitet")
    if "spjæld" in brod.lower(): t("ordet 'spjæld' må ikke stå på sitet")
    if re.search(r"ingen ledige|ikke ledige", brod, re.I): t("tekst om at der ikke er ledige stillinger")
    if sl in ("materieludlejning", "lejebetingelser") and re.search(r"\d[\d.]*\s*(kr\.|%)", brod): t("pris eller procentsats paa udlejningsside")

for tt, fs in titler.items():
    if len(fs) > 1: fejl.append(f"samme title paa flere sider: {tt} ({', '.join(fs)})")

indekserbare = [s for s in sider if slug_af(s) not in NOINDEX]
for p in indekserbare:
    if p != "index.html" and p not in linket: fejl.append(f"forældreløs side (ingen interne links): {p}")

# Sitemap: alle indekserbare sider, ingen noindex-sider
sm = laes("sitemap.xml")
smurls = set(re.findall(r"<loc>(.*?)</loc>", sm))
for p in indekserbare:
    if DOMAIN + url(slug_af(p)) not in smurls:
        fejl.append(f"mangler i sitemap: {p}")
for p in sider:
    if slug_af(p) in NOINDEX and DOMAIN + url(slug_af(p)) in smurls: fejl.append(f"noindex-side staar i sitemap: {p}")
if "<lastmod>" not in sm: fejl.append("sitemap mangler lastmod")
for u in smurls:
    p = u.replace(DOMAIN, "").strip("/")
    if not os.path.exists(os.path.join(R, p, "index.html") if p else os.path.join(R, "index.html")): fejl.append(f"sitemap peger paa side der ikke findes: {u}")

# Redirects: hver gammel URL har en stub, og .htaccess har en 301-regel
ht = laes(".htaccess")
if re.search(r"RewriteRule \^index\\\.html", ht): fejl.append(".htaccess: regel for index.html giver endeloes loekke")
GAMLE_HTML = ["hovedentreprise", "doere-og-vinduer", "gaardhaver", "materieludlejning", "referencer", "terrasse", "tag", "nybyg", "renovering", "job", "kontakt", "cookies", "lejebetingelser"]
for g in GAMLE_HTML:
    if f"{g}.html" not in stubs: fejl.append(f"redirect-stub mangler: {g}.html")
    if f"^{g}\\.html$" not in ht: fejl.append(f".htaccess mangler 301 for {g}.html")
for g in ["doere-vinduer", "gaardhaver", "udlejning-af-stillads-og-trailer", "totalentreprise", "sommerhus"]:
    if f"{g}/index.html" not in stubs: fejl.append(f"redirect-stub mangler: {g}/")
    if f"^{g}/?$" not in ht: fejl.append(f".htaccess mangler 301 for /{g}/")
for st in stubs:
    m = re.search(r'rel="canonical" href="([^"]+)"', laes(st))
    if not m: fejl.append(f"stub uden canonical: {st}"); continue
    ny = m.group(1).replace(DOMAIN, "").strip("/")
    if not os.path.exists(os.path.join(R, ny, "index.html")): fejl.append(f"stub peger paa side der ikke findes: {st} -> {ny}")
if "HTTP_HOST" not in ht or "https://rosendal-tomrer.dk/$1" not in ht: fejl.append(".htaccess mangler https/www-regel")

# Ydelsessider: kort svar 40-60 ord, ordantal, ordoverlap
def hoved(s):
    h = laes(f"{s}/index.html")
    h = h.split("<main>")[1].split('<section class="cta">')[0]
    h = re.sub(r"<aside.*?</aside>", " ", h, flags=re.S)
    h = re.sub(r'<div class="crumb">.*?</div>|<div class="btn-row">.*?</div>', " ", h, flags=re.S)
    h = re.sub(r'<section class="sec-mist"><div class="container trust">.*?</section>', " ", h, flags=re.S)
    return h
O = {}
for s in YSLUGS:
    h = hoved(s)
    m = re.search(r'<div class="svar"><strong>[^<]*</strong>(.*?)</div>', h, re.S)
    n = len(tekst(m.group(1)).split()) if m else 0
    if not m: fejl.append(f"{s}: kort svar-boks mangler")
    elif not 38 <= n <= 62: adv.append(f"{s}: kort svar er {n} ord (maal 40-60)")
    ord_antal = len(tekst(h).split())
    if ord_antal < 450: adv.append(f"{s}: kun {ord_antal} ord broedtekst")
    O[s] = set(re.findall(r"[a-zæøå]{4,}", tekst(h).lower()))
maks = 0
for a, b in itertools.combinations(O, 2):
    ov = len(O[a] & O[b]) / len(O[a] | O[b])   # Jaccard
    maks = max(maks, ov)
    if ov > 0.30: adv.append(f"ordoverlap {a}/{b}: {ov:.0%}")
    if "--ord" in sys.argv and ov > 0.30: print(f"  delte ord {a}/{b}:", " ".join(sorted(O[a] & O[b])))

if DEMO: adv.append("testside: noindex paa alle sider (live bygges med --live)")
if not GA_ID: adv.append("GA_ID ikke sat (ingen Google Analytics endnu)")
if not FORMSPREE_ID: adv.append("FORMSPREE_ID ikke sat: formularen sender ikke")
if LIVEBYG:
    for s in sider:
        if 'content="noindex' in laes(s) and slug_af(s) not in NOINDEX: fejl.append(f"live-side med noindex: {s}")
for f in ["robots.txt", "sitemap.xml", "llms.txt", "favicon.ico", "apple-touch-icon.png", ".htaccess", "images/og-forside.jpg"] + ([] if LIVEBYG else [".nojekyll"]):
    if not os.path.exists(os.path.join(R, f)): fejl.append(f"mangler: {f}")

print(f"{len(sider)} HTML-sider + {len(stubs)} redirect-stubs. Største ordoverlap mellem ydelsessider: {maks:.0%}")
for x in fejl: print("FEJL ", x)
for x in adv: print("ADV  ", x)
print(f"{len(fejl)} fejl, {len(adv)} advarsler")
sys.exit(1 if fejl else 0)
