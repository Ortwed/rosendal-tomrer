"""Bygger hele sitet. Idempotent: kan koeres igen og igen.

  python3 src/build.py          testsiden til ../docs (noindex, vises paa ortwed.github.io/rosendal-tomrer/)
  python3 src/build.py --live   live-versionen til ../live og ../rosendal-tomrer-live.zip (til Simply)

Sider ligger som /<slug>/index.html (pæne URL'er). Al HTML skrives med rodstier (/tag/, /images/x.webp);
build_page goer dem relative, saa samme HTML virker paa begge adresser.
"""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
import site_shared as S
from site_shared import *
from indhold import ANMELDELSER as A, YDELSER as Y, MATERIEL, MATERIEL_KATEGORIER, MATERIEL_SIDE, MATERIEL_LINKS

ROD = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROD, "live" if LIVEBYG else "docs")
BEHOLD = {"images", "favicon.ico", "apple-touch-icon.png", ".git"}
if LIVEBYG:
    shutil.rmtree(OUT, ignore_errors=True)       # live-mappen bygges forfra, saa der aldrig ligger gamle filer med
    shutil.copytree(os.path.join(ROD, "docs", "images"), os.path.join(OUT, "images"))
    for f in ("favicon.ico", "apple-touch-icon.png"):
        shutil.copy(os.path.join(ROD, "docs", f), OUT)
else:
    for f in os.listdir(OUT):                    # ryd gamle genererede filer (fx de gamle .html-sider)
        if f in BEHOLD: continue
        p = os.path.join(OUT, f)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
SIDER = []

def skriv(navn, txt):
    p = os.path.join(OUT, navn)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)

def side(slug, *a, **k):
    skriv("index.html" if slug == "index" else f"{slug}/index.html", build_page(slug, *a, **k))
    if not k.get("noindex"):
        SIDER.append(slug)

# ---------------- PROJEKTER ----------------
# status 'pending' = skjult (ingen side, intet menupunkt, ikke i sitemap) indtil der er faerdigbilleder
# og tekst fra Sebastian. Saet status til 'live' og udfyld billeder, tekst og citat, saa bygges siden.
PROJEKTER = [
    dict(slug="sommerhus-nyt-tag", titel="Sommerhusrenovering med nyt tag", by="Hundested", maaned="februar 2026", ydelse="sommerhus", anm="brian", status="pending", billeder=[]),
    dict(slug="tilbygning-gaestehus", titel="Tilbygning og gæstehus", by="Hundested", maaned="november 2025", ydelse="tilbygning", anm="rita", status="pending", billeder=[]),
    dict(slug="repos-trappe-ipe", titel="Repos-trappe i ipé", by="Veksø", maaned="juli 2026", ydelse="terrasse", anm="morten", status="pending", billeder=[]),
    dict(slug="nyt-tegltag", titel="Nyt tegltag", by="Hundested", maaned="oktober 2026", ydelse="tag", anm="kenneth", status="pending", billeder=[]),
    dict(slug="vinduer-og-franske-altaner", titel="Nye vinduer og to franske altaner", by="Hundested", maaned="august 2026", ydelse="vinduer", anm="peter", status="pending", billeder=[]),
    dict(slug="facadebeklaedning-og-isolering", titel="Facadebeklædning og isolering", by="Ølsted", maaned="september 2025", ydelse="renovering", anm="hanne", status="pending", billeder=[]),
    dict(slug="terrasse-liseleje", titel="Terrasse i Liseleje", by="Liseleje", maaned="august 2025", ydelse="terrasse", anm="kira", status="pending", billeder=[]),
    dict(slug="doere-og-vinduer-vejby", titel="Nye døre og vinduer i Vejby", by="Vejby", maaned="april 2026", ydelse="doere", anm="anita", status="pending", billeder=[]),
]
LIVE = [p for p in PROJEKTER if p["status"] == "live"]
S.STATE["projekter"] = bool(LIVE)

# ---------------- FAELLES BYGGEKLODSER ----------------
LB_JS = """<div class="lb" id="lb" role="dialog" aria-label="Billedvisning"><button class="lb-close" aria-label="Luk">×</button><button class="lb-prev" aria-label="Forrige">‹</button><img alt=""><button class="lb-next" aria-label="Næste">›</button></div>
<script>(function(){var L=document.getElementById('lb'),I=L.querySelector('img'),B=[].slice.call(document.querySelectorAll('[data-lb]')),i=0;
function v(n){i=(n+B.length)%B.length;I.src=B[i].src;I.alt=B[i].alt;L.classList.add('open');}
B.forEach(function(b,n){b.addEventListener('click',function(){v(n);});});
L.querySelector('.lb-close').onclick=function(){L.classList.remove('open');};L.querySelector('.lb-prev').onclick=function(){v(i-1);};L.querySelector('.lb-next').onclick=function(){v(i+1);};
document.addEventListener('keydown',function(ev){if(!L.classList.contains('open'))return;if(ev.key==='Escape')L.classList.remove('open');if(ev.key==='ArrowLeft')v(i-1);if(ev.key==='ArrowRight')v(i+1);});})();</script>"""

def stj(k):
    return '<span class="stars" aria-hidden="true">★★★★★</span>' if k == "5,0" else f'<span class="stars" aria-hidden="true">★★★★☆</span> <strong>{k}</strong>'

STJ = stj("5,0")

def rev_kort(key, cls="rev"):
    t, q, n, by, d, k, _ = A[key]
    return (f'<article class="{cls}">{stj(k)}<h3>{e(t)}</h3><blockquote>{e(q)}</blockquote>'
            f'<div class="who"><strong>{e(n)}</strong>, {e(by)} · {e(d)}</div></article>')

def rev_mini(keys):
    if not keys: return ""
    return (f'<h2>Det siger kunderne</h2><div class="rev-mini">{"".join(rev_kort(k) for k in keys)}</div>'
            f'<p><a href="/anmeldelser/">Alle anmeldelser</a></p>')

def omr_chips():
    li = "".join(f'<li><a href="{url(sl)}">{e(n)}</a></li>' if sl else f"<li><span>{e(n)}</span></li>" for sl, n in OMRAADER)
    return f'<ul class="chips">{li}</ul>'

KORT_TXT = {
    "tilbygning": "Mere plads til stuen, et ekstra værelse, et anneks eller en førstesal.",
    "sommerhus": "Nyt tag, isolering, vinduer, terrasse og altan til sommerhuse.",
    "tag": "Nyt tag, tegltag, tagrenovering og efterisolering.",
    "vinduer": "Vinduer i træ og træ/alu, målt op, leveret og monteret.",
    "doere": "Hoveddøre, terrassedøre, foldedøre og franske altaner.",
    "terrasse": "Træterrasser, repos og trappetrin, gerne i ipé.",
    "renovering": "Vægge, gulve, lofter, isolering og facader.",
    "nybyg": "Nye huse, gæstehuse, anneks, carporte og garager.",
    "pergola-hegn-og-cykelskur": "Pergolaer, hegn, cykelskure og bænke til private og erhverv.",
    "materieludlejning": "Lej stillads, betonblander, affugter, dumper, pælebor og værktøj i Hundested.",
}

def svc_grid():
    out = ['<div class="svc-grid">',
           f'<a class="svc svc-feature" href="{url("totalentreprise")}">{HEX}<h3>Totalentreprise og hovedentreprise</h3>'
           '<p>Vi styrer hele byggeriet og koordinerer murer, elektriker, VVS og maler. Én kontrakt, én kontakt og ét ansvar fra start til aflevering.</p>'
           '<span class="svc-go">Læs om entrepriseformerne</span></a>']
    for sl, n in YDELSER:
        if sl in KORT_TXT:
            out.append(f'<a class="svc" href="{url(sl)}">{HEX}<h3>{e(n)}</h3><p>{KORT_TXT[sl]}</p><span class="svc-go">Læs mere</span></a>')
    out.append("</div>")
    out.append(f'<p class="svc-more">Vi laver også carporte og garager, udestuer og vinterhaver, skillevægge, loftsbeklædning, facadebeklædning, køkkener og garderobeskabe samt bygningsvedligeholdelse. Ring og hør, hvad vi kan gøre for dig: <a href="tel:{TLF_RAW}">{TLF}</a>.</p>')
    return "\n".join(out)

TRUST = f"""<div class="container trust">
  <div><strong>Tømrermester</strong><span>og uddannet bygningskonstruktør</span></div>
  <div><strong>Skriftligt tilbud</strong><span>så du kender pris og omfang, før vi går i gang</span></div>
  <div><strong>Fast hold af tømrere</strong><span>og én fast kontaktperson hele vejen</span></div>
  <div><strong>Hele {OMRAADE}</strong><span>fra værksted og kontor i Hundested</span></div>
</div>"""

TRUST_LILLE = f"""<section class="sec-mist"><div class="container trust">
  <div><strong>Tømrermester</strong><span>og uddannet bygningskonstruktør</span></div>
  <div><strong>Skriftligt tilbud</strong><span>så du kender pris og omfang, før vi går i gang</span></div>
  <div><strong>Svar inden for 24 timer</strong><span>på hverdage</span></div>
  <div><strong>Fast hold af tømrere</strong><span>og én fast kontaktperson hele vejen</span></div>
</div></section>"""

SIGNATUR = """<div class="sign"><img src="/images/signatur.png" alt="Sebastian Rosendals underskrift" width="172" height="176" loading="lazy">
  <div><strong>Sebastian Rosendal</strong><span>Indehaver, tømrermester og bygningskonstruktør</span></div></div>"""

def hero_knapper(tag="hero"):
    return (f'<div class="btn-row"><a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a>'
            f'<a class="btn btn-ghost" href="/kontakt/" data-cta="{tag}">Få et tilbud</a></div>')

# ---------------- FORSIDE ----------------
forside = f"""
<section class="hero">
  <div class="hero-text"><div class="hero-inner">
    <div class="hero-kicker">Rosendal Tømrer Entreprise · siden 2021</div>
    <h1>Tømrermester i Hundested: tilbygning, tag, vinduer og totalentreprise i Nordsjælland</h1>
    <p class="lead">Vi hjælper private og erhverv med alt fra nye vinduer og træterrasser til renoveringer, tilbygninger og hele byggerier. Sebastian er din faste kontaktperson, og vi er et fast hold af tømrere.</p>
    <div class="cta-block">
      <div class="btn-row">
        <a class="btn btn-primary" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a>
        <a class="btn btn-ghost" href="/kontakt/" data-cta="hero">Få et tilbud</a>
      </div>
      <div class="hero-badges">
        <div class="ah-badge">{AH_BADGE_DIV}</div>
        <img class="dh-logo" src="/images/garanti-dansk-haandvaerk.webp" alt="Garanti, Dansk Håndværk: Rosendal Tømrer er medlem og giver byggegaranti" width="190" height="190">
      </div>
    </div>
  </div></div>
  <div class="hero-img"><img src="/images/terrasse-trapper.webp" srcset="/images/terrasse-trapper-720.webp 720w, /images/terrasse-trapper.webp 1500w" sizes="(max-width:820px) 100vw, 55vw"
    alt="Terrasse i hårdttræ med siddetrapper, trappe op ad skrænten og hegn af lodrette lister, bygget af Rosendal Tømrer" width="1500" height="1125" fetchpriority="high"></div>
</section>

<section class="sec-mist">{TRUST}</section>

<section class="sec" id="om"><div class="container about">
  <div class="prose">
    <h2>Et tømrerfirma, der tager hele opgaven</h2>
    <p>Rosendal Tømrer Entreprise blev stiftet i 2021 af Sebastian Rosendal, der er tømrermester og uddannet bygningskonstruktør. I dag er vi et fast hold af tømrere med værksted og kontor på Engdraget i Hundested. Herfra hjælper vi private og erhverv med tømreropgaver i hele {OMRAADE}.</p>
    <p>Vi tager os af både de mindre opgaver og de større byggeprojekter. Det kan være alt fra en ny terrassedør til en tilbygning eller en gennemgribende renovering, hvor vi også koordinerer de øvrige håndværkere.</p>
    <p>For os handler godt håndværk ikke kun om det færdige resultat. Det handler også om, at du ved, hvad der skal ske, at vi holder vores aftaler, og at der bliver taget hånd om tingene undervejs. Læs mere <a href="/om-os/" style="text-decoration:underline">om os</a>.</p>
    {SIGNATUR}
  </div>
  <ul class="principles">
    <li><strong>Du har én fast kontaktperson</strong><span>Du taler med Sebastian fra den første snak til det færdige resultat. Du ved, hvem du skal kontakte, og hvem der har overblikket over dit projekt.</span></li>
    <li><strong>Vi holder, hvad vi aftaler</strong><span>Du får et skriftligt tilbud, så du ved, hvad der er aftalt. Hvis der opstår noget uventet undervejs, tager vi dialogen med dig, inden vi går videre.</span></li>
    <li><strong>Vi tænker projektet igennem</strong><span>Med erfaring som tømrermester og uddannet bygningskonstruktør har Sebastian blik for både detaljerne og helheden. Det giver et godt grundlag for at finde løsninger, der fungerer i praksis.</span></li>
    <li><strong>Vi behandler dit hjem ordentligt</strong><span>Vi arbejder i dit hjem, og det tager vi alvorligt. Vi rydder op efter os og gør os umage for at gøre byggeperioden så overskuelig som muligt.</span></li>
  </ul>
</div></section>

<section class="sec sec-mist"><div class="container">
  <div class="sec-head"><h2>Det laver vi</h2><p>Fra små opgaver til hele byggerier, for private og erhverv. Vælg en ydelse og læs mere om, hvordan vi griber den an.</p></div>
  {svc_grid()}
</div></section>

<section class="sec"><div class="container">
  <div class="sec-head"><h2>Det siger vores kunder</h2><p>Anmeldelser fra Anmeld Håndværker. De opdateres automatisk, når der kommer nye.</p></div>
  <div class="ah-widget">{AH_SLIDER_DIV}</div>
  <p class="ah-mere"><a href="/anmeldelser/">Se alle anmeldelser →</a></p>
</div></section>

<section class="sec sec-sand"><div class="container">
  <div class="sec-head"><h2>Sådan foregår et projekt</h2><p>Samme fire trin, uanset om det er et vindue eller en tilbygning.</p></div>
  <ol class="steps">
    <li><strong>Første snak</strong><span>Du ringer eller skriver og fortæller kort om opgaven.</span></li>
    <li><strong>Besigtigelse</strong><span>Vi kommer ud, ser på forholdene og taler løsninger igennem.</span></li>
    <li><strong>Fast tilbud</strong><span>Du får et skriftligt tilbud med pris, omfang og tidsplan.</span></li>
    <li><strong>Udførelse og aflevering</strong><span>Vi bygger, holder dig orienteret undervejs og afleverer ryddet op.</span></li>
  </ol>
</div></section>

<section class="sec"><div class="container narrow prose">
  <h2>Hvor kører vi?</h2>
  <p>Vi kører fra værksted og kontor på Engdraget 11 i Hundested og tager opgaver i hele Nordsjælland. Her er de områder, vi dækker.</p>
  {omr_chips()}
  <p><a href="/omrader/" style="text-decoration:underline">Se alle områder</a></p>
</div></section>
{some()}
{cta()}
"""
side("index", "Tømrer i Hundested og Nordsjælland | Rosendal Tømrer",
     "Tømrermester og bygningskonstruktør i Hundested. Tilbygning, tag, vinduer, terrasser og totalentreprise i Nordsjælland. Ring 50 70 05 05.",
     forside, schemas=[schema_virksomhed()], extra_js=AH_BADGE_JS + "\n" + AH_SLIDER_JS + "\n" + AH_BADGE_HOEJDE_JS)

# ---------------- YDELSESSIDER ----------------
def sidebar(aktiv):
    li = "".join(f'<li><a href="{url(sl)}"{" class=\"active\"" if sl == aktiv else ""}>{e(n)}</a></li>' for sl, n in YDELSER)
    return (f'<aside class="side"><ul class="side-nav">{li}</ul>'
            f'<div class="side-cta"><h2>Kontakt os i dag</h2><p>Tømrerarbejde i Hundested. Vi dækker hele {OMRAADE}.</p>'
            f'<a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}{TLF}</a><a class="side-link" href="/kontakt/" data-cta="sidebar">Skriv til os</a></div></aside>')

def liste(items):
    return "<ul>" + "".join(f'<li><a href="{url(x[1])}">{e(x[0])}</a></li>' if isinstance(x, tuple) else f"<li>{e(x)}</li>" for x in items) + "</ul>"

OMR_VERB = {"totalentreprise": "styrer byggerier", "tilbygning": "bygger til huse", "sommerhus": "renoverer sommerhuse", "tag": "skifter tage",
            "vinduer": "skifter vinduer", "doere": "monterer døre", "terrasse": "bygger terrasser", "renovering": "renoverer boliger",
            "nybyg": "bygger nyt", "pergola-hegn-og-cykelskur": "bygger pergolaer og hegn"}

def ydelse(slug):
    d = Y[slug]
    navn = dict(YDELSER)[slug]
    blokke = [f'<div class="svar"><strong>Kort svar</strong>{e(d["svar"])}</div>']
    if d.get("billede"):
        src, alt = d["billede"]
        blokke.append(f'<figure class="svc-fig"><img src="{src}" alt="{e(alt)}" loading="lazy"></figure>')
    if d.get("ind"):
        blokke.append(f'<h2>{e(d.get("ind_h", "Det indgår i opgaven"))}</h2>{liste(d["ind"])}')
    for h2, c in d["sek"]:
        if isinstance(c, tuple):
            body = liste(c[1]) if c[0] == "ul" else c[1]
        else:
            body = "".join(f"<p>{e(x)}</p>" for x in c)
        blokke.append(f"<h2>{e(h2)}</h2>{body}")
    if d.get("kategorier"):
        # Illustrationerne er tegninger, ikke fotos af Sebastians materiel, saa alt-teksten er kun kategorien.
        kort = "".join(f'<div class="mat-kort"><img src="{src}" alt="Illustration: {e(n)}" width="960" height="720" loading="lazy">'
                       f'<h3>{e(n)}</h3><p>{e(t)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in ting)}</ul></div>'
                       for n, src, t, ting in d["kategorier"])
        blokke.append(f'<h2>Det kan du leje</h2><div class="mat-grid">{kort}</div>')
    if d.get("efter_html"):
        blokke.append(d["efter_html"])
    blokke.append("<h2>Sådan foregår det</h2><ol class=\"trin\">" + "".join(f"<li><strong>{e(t)}</strong>{e(x)}</li>" for t, x in d["trin"]) + "</ol>")
    blokke.append(f'<h2>Hvad påvirker prisen?</h2><p>{e(d["pris_intro"])}</p>{liste(d["pris"])}')
    if d.get("galleri"):
        blokke.append('<div class="svc-gal">' + "".join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy" data-lb></figure>' for s, a in d["galleri"]) + "</div>")
    blokke.append(rev_mini(d["anm"]))
    if slug in MATERIEL_LINKS:
        # Interne links til de maskiner, der passer til opgaven (og fra udlejningssiden tilbage hertil)
        kald = {"paelebor": "pælebor", "jordbor": "mobilt jordbor", "affugter": "affugter", "gipshejs": "gipshejs",
                "betonblander": "betonblander", "dumper": "dumper", "rullestillads": "rullestillads"}
        ml = [f'<a href="/materieludlejning/#{i}">{kald[i]}</a>' for i in MATERIEL_LINKS[slug]]
        blokke.append(f'<h2>Lav noget af det selv?</h2><p>Vil du selv tage fat, kan du leje {", ".join(ml[:-1])} og {ml[-1]} hos os i Hundested. '
                      'Se priser pr. dag under <a href="/materieludlejning/">materieludlejning</a>.</p>')
    blokke.append(f'<h2>Områder vi dækker</h2><p>Vi {OMR_VERB[slug]} i Hundested og resten af Nordsjælland. '
                  'Læs om <a href="/tomrer-hundested/">tømrer i Hundested</a>, eller se <a href="/omrader/">alle områder</a>.</p>')
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    body = f"""
<section class="page-header"><div class="container">
  {crumb_html([(navn, None)])}
  <h1>{e(d['h1'])}</h1><p>{e(d['intro'])}</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container svc-layout">
  {sidebar(slug)}
  <div class="prose svc-main">{''.join(blokke)}
    <h2>Ofte stillede spørgsmål</h2><div class="faq">{faq}</div>
  </div>
</div></section>
{TRUST_LILLE}
{cta()}"""
    side(slug, d["title"], d["desc"], body, active=slug,
         schemas=[schema_service(navn, d["desc"], slug), faq_schema(d["faq"])],
         extra_js=LB_JS if d.get("galleri") else "", krummer=[(navn, None)])

for sl, _ in YDELSER:
    if sl in Y:          # materieludlejning har sin egen skabelon herunder
        ydelse(sl)

# ---------------- MATERIELUDLEJNING ----------------
# Alt indhold staar som tekst i HTML (ingen faner eller skjult indhold), saa soegemaskiner og AI kan citere priser og maal.
def kr(n):
    return f"{n:,}".replace(",", ".") + " kr."

def maskine_kort(m):
    mid, _, navn, tekst, specs, inkl, ekskl = m
    pris = (f'<p class="m-pris"><strong>{kr(inkl)}</strong> pr. dag inkl. moms<span>{kr(ekskl)} ekskl. moms</span></p>'
            if inkl else '<p class="m-pris"><strong>Kontakt for pris</strong></p>')
    return (f'<article class="maskine" id="{mid}"><img src="/images/materiel/{mid}.svg" alt="{e(navn)} til leje i Hundested" width="480" height="360" loading="lazy">'
            f'<div class="m-krop"><h3>{e(navn)}</h3><p>{e(tekst)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in specs)}</ul>{pris}'
            f'<a class="btn btn-brass" href="tel:{TLF_RAW}" data-cta="materiel-{mid}">{ICON_TLF}Ring og book {TLF}</a></div></article>')

def schema_materiel():
    elementer = []
    for i, (mid, _, navn, tekst, specs, inkl, _ekskl) in enumerate(MATERIEL):
        p = {"@type": "Product", "name": navn, "description": tekst + " " + ". ".join(specs) + ".",
             "image": f"{DOMAIN}/images/materiel/{mid}.svg", "url": f"{DOMAIN}/materieludlejning/#{mid}"}
        if inkl:   # "Kontakt for pris" faar ingen offers
            p["offers"] = {"@type": "Offer", "price": str(inkl), "priceCurrency": "DKK", "url": f"{DOMAIN}/materieludlejning/#{mid}",
                           "seller": {"@id": DOMAIN + "/#virksomhed"},
                           "priceSpecification": {"@type": "UnitPriceSpecification", "price": inkl, "priceCurrency": "DKK",
                                                  "unitCode": "DAY", "valueAddedTaxIncluded": True}}
        elementer.append({"@type": "ListItem", "position": i + 1, "item": p})
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "Materiel til leje hos " + NAVN, "itemListElement": elementer}

def materiel_side():
    d = MATERIEL_SIDE
    navn = "Materieludlejning"
    hurtig = "".join(f'<a href="#{k}">{e(h.replace(" til leje i Hundested", ""))}</a>' for k, h, _ in MATERIEL_KATEGORIER)
    sektioner = "".join(
        f'<section class="m-kat" id="{k}"><h2>{e(h)}</h2><p>{e(intro)}</p><div class="m-grid">'
        + "".join(maskine_kort(m) for m in MATERIEL if m[1] == k) + "</div></section>"
        for k, h, intro in MATERIEL_KATEGORIER)
    trin = "<ol class=\"trin\">" + "".join(f"<li><strong>{e(t)}</strong>{e(x)}</li>" for t, x in d["trin"]) + "</ol>"
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    ydl = {"terrasse": "Terrasse", "pergola-hegn-og-cykelskur": "Pergola, hegn og cykelskur", "renovering": "Renovering",
           "tilbygning": "Tilbygning", "nybyg": "Nybyg"}
    tilbage = ", ".join(f'<a href="{url(k)}">{e(v.lower())}</a>' for k, v in list(ydl.items())[:-1]) + f' og <a href="{url("nybyg")}">nybyg</a>'
    body = f"""
<section class="page-header"><div class="container">
  {crumb_html([(navn, None)])}
  <h1>{e(d['h1'])}</h1><p>{e(d['intro'])}</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container prose m-side">
  <div class="svar"><strong>Kort svar</strong>{e(d["svar"])}</div>
  <nav class="m-hurtig" aria-label="Kategorier">{hurtig}</nav>
  {sektioner}
  <p class="m-note">Alle priser er pr. kalenderdag. Oven i den samlede pris kommer et forsikringsgebyr på 7 %. Læs de fulde <a href="/lejebetingelser/">lejebetingelser</a>, før du lejer.</p>
  <h2>Sådan lejer du</h2>{trin}
  <h2>Skal vi hellere lave opgaven?</h2>
  <p>Vi er tømrere og bygger det, vi udlejer materiel til. Læs om {tilbage}.</p>
  <h2>Ofte stillede spørgsmål</h2><div class="faq">{faq}</div>
</div></section>
{cta("Skal du bruge noget af det?", f"Ring og hør, om det er ledigt. Vi dækker hele {OMRAADE}.")}"""
    side("materieludlejning", d["title"], d["desc"], body, active="materieludlejning",
         schemas=[schema_service(navn, d["desc"], "materieludlejning"), faq_schema(d["faq"]), schema_materiel()],
         krummer=[(navn, None)])

materiel_side()

# ---------------- OM OS ----------------
fakta = [("Firmanavn", NAVN), ("CVR", CVR), ("Adresse", f"{ADR}, {POST} {BY} (værksted og kontor)"), ("Telefon", f'<a href="tel:{TLF_RAW}">{TLF}</a>'),
         ("E-mail", f'<a href="mailto:{MAIL}">{MAIL}</a>'), ("Åbningstid", AABNING), ("Stiftet", "2021 af Sebastian Rosendal"),
         ("Dækningsområde", f"Hundested og {OMRAADE}"), ("Svartid", "Inden for 24 timer på hverdage"),
         ("Anmeldelser", f'{ANM_SNIT} ud af 5 på <a href="{ANM_URL}" target="_blank" rel="noopener">Anmeld Håndværker</a> ({ANM_TEKST} anmeldelser)')]
fakta_html = "".join(f"<dt>{e(k)}</dt><dd>{v if '<a' in v else e(v)}</dd>" for k, v in fakta)
omos = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Om os", None)])}
  <h1>Tømrermester og bygningskonstruktør i Hundested</h1>
  <p>Rosendal Tømrer Entreprise ApS blev stiftet i 2021 af Sebastian Rosendal og har værksted og kontor på Engdraget i Hundested.</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container narrow prose">
  <h2>Sebastian Rosendal</h2>
  <p>Sebastian er tømrermester og uddannet bygningskonstruktør. Han stiftede firmaet i 2021 og er den, du taler med fra den første snak til det færdige resultat. Når der er brug for at tænke et projekt igennem, før det bygges, kommer begge uddannelser i spil.</p>
  {SIGNATUR}
  <h2>Holdet</h2>
  <p>Vi er et fast hold af tømrere. Kunderne omtaler vores svende som dygtige og venlige, og det er den måde, vi vil arbejde på. Du får besøg af folk, der kender opgaven, og som tager godt imod dine spørgsmål undervejs. Vi søger løbende tømrersvende, så er du interesseret i at blive en del af holdet, kan du læse mere under <a href="/job/">job</a>.</p>
  <h2>Sådan arbejder vi</h2>
  <p>Du har én fast kontaktperson. Du får et skriftligt tilbud, så du ved, hvad der er aftalt, og hvis der opstår noget uventet undervejs, tager vi dialogen med dig, inden vi går videre. Vi arbejder i dit hjem, og det tager vi alvorligt: Vi rydder op efter os og gør os umage for at gøre byggeperioden så overskuelig som muligt.</p>
  <p>Mange af opgaverne involverer flere fag. Vi har faste samarbejdspartnere inden for murer, el, VVS, maler og kloak og kan tage hele projektet som <a href="/totalentreprise/">hovedentreprise</a>, så du kun har én kontakt.</p>
  <h2>Fakta om virksomheden</h2>
  <dl class="fakta">{fakta_html}</dl>
  <p>Se også hvad kunderne siger under <a href="/anmeldelser/">anmeldelser</a>, eller <a href="/omrader/">se hvilke områder vi dækker</a>.</p>
</div></section>
{cta()}"""
side("om-os", "Om Rosendal Tømrer | Tømrermester i Hundested",
     "Rosendal Tømrer Entreprise ApS i Hundested: tømrermester og bygningskonstruktør Sebastian Rosendal og et fast hold af tømrere. Ring 50 70 05 05.",
     omos, schemas=[schema_virksomhed()], krummer=[("Om os", None)])

# ---------------- OMRAADER OG HUNDESTED ----------------
omr = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Områder", None)])}
  <h1>Områder vi dækker i Nordsjælland</h1>
  <p>Vi kører fra værksted og kontor på Engdraget 11 i Hundested og tager tømrerarbejde i hele Nordsjælland.</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container narrow prose">
  <div class="svar"><strong>Kort svar</strong>Rosendal Tømrer Entreprise har base i Hundested og tager opgaver i Hundested, Frederiksværk, Hillerød, Helsinge, Gilleleje og sommerhusområderne langs Nordkysten. Ring på {TLF}, så finder vi ud af, om vi kan tage din opgave.</div>
  <h2>Her kører vi</h2>
  {omr_chips()}
  <p>Hundested har sin egen side, hvor du kan se opgaver fra byen: <a href="/tomrer-hundested/">tømrer i Hundested</a>.</p>
  <h2>Hvor vi har løst opgaver</h2>
  <p>Kunderne fortæller selv, hvor og hvad vi har lavet. Vi har blandt andet løst opgaver i Hundested, Frederiksværk, Ølsted, Hillerød, Liseleje og Vejby: tag, vinduer og døre, terrasser, facade og renoveringer. Læs deres anmeldelser under <a href="/anmeldelser/">anmeldelser</a>.</p>
  <h2>Ligger din opgave et andet sted?</h2>
  <p>Ring og fortæl, hvor opgaven ligger, og hvad den går ud på. Så hører du, om vi kan tage den.</p>
  <h2>Det laver vi i hele området</h2>
  {liste([(n, sl) for sl, n in YDELSER])}
</div></section>
{cta()}"""
side("omrader", "Områder vi dækker i Nordsjælland | Rosendal Tømrer",
     "Rosendal Tømrer i Hundested tager tømrerarbejde i Hundested, Frederiksværk, Hillerød, Helsinge, Gilleleje og på Nordkysten. Ring 50 70 05 05.",
     omr, schemas=[schema_virksomhed()], krummer=[("Områder", None)])

hund_faq = [
    ("Har I værksted i Hundested?", f"Ja. Vi har værksted og kontor på {ADR}, {POST} {BY}."),
    ("Hvilke områder omkring Hundested kører I til?", "Vi tager opgaver i hele Nordsjælland, blandt andet Frederiksværk, Ølsted, Lynæs, Hillerød, Helsinge, Gilleleje og sommerhusområderne langs Nordkysten."),
    ("Hvordan får jeg et tilbud i Hundested?", f"Ring på {TLF} på hverdage mellem 07.00 og 17.00, eller send en henvendelse. Vi kommer ud og ser på opgaven og giver et fast skriftligt tilbud."),
    ("Hvor hurtigt svarer I?", "Vi vender tilbage inden for 24 timer på hverdage."),
    ("Kan jeg leje stillads eller trailer i Hundested?", "Ja. Rullestillads, trailer og andet materiel kan hentes på Engdraget 11 efter aftale, og levering kan aftales."),
]
hund = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Områder", "omrader"), ("Tømrer i Hundested", None)])}
  <h1>Tømrer i Hundested</h1>
  <p>Rosendal Tømrer Entreprise har værksted og kontor på Engdraget 11 i Hundested. Vi tager tag, vinduer, døre, terrasser, tilbygninger og renoveringer i Hundested og omegn.</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container narrow prose">
  <div class="svar"><strong>Kort svar</strong>Rosendal Tømrer Entreprise er et tømrerfirma i Hundested, stiftet i 2021 af tømrermester og bygningskonstruktør Sebastian Rosendal. Vi har værksted og kontor på Engdraget 11 og tager tag, vinduer, døre, terrasser, tilbygninger og renoveringer. Ring på {TLF} på hverdage 07.00 til 17.00.</div>
  <h2>Vi har base i Hundested</h2>
  <p>Det er herfra, vi kører ud til opgaverne, og det er her, du kan hente rullestillads, trailer og værktøj, hvis du vil leje. Du ringer til Sebastian og får en fast kontaktperson, der kender dit projekt fra første snak til aflevering.</p>
  <h2>Opgaver vi har løst i Hundested</h2>
  <p>Kunderne fortæller selv, hvordan det er gået. Her er et udpluk fra Hundested.</p>
  <div class="rev-mini">{rev_kort('kenneth')}{rev_kort('peter')}{rev_kort('brian')}</div>
  <p>Hundestedkunderne har blandt andet også fået en tilbygning og et gæstehus (november 2025), beklædning på vægge og loft samt altan i et sommerhus (august 2025), nyt tag og skillevæg (september 2025) og nyt tag (august 2025). <a href="/anmeldelser/">Læs flere anmeldelser</a>.</p>
  <h2>De mest relevante ydelser i Hundested</h2>
  {liste([("Tag: nyt tag og tagrenovering", "tag"), ("Vinduer: nye vinduer og vinduesudskiftning", "vinduer"), ("Tilbygning: mere plads til huset", "tilbygning"), ("Sommerhus: renovering og nyt tag", "sommerhus")])}
  <h2>Sådan kommer vi i gang</h2>
  <p>Ring på <a href="tel:{TLF_RAW}">{TLF}</a>, eller send en henvendelse via <a href="/kontakt/" data-cta="omrade">kontaktsiden</a>. Vi kommer ud og ser på opgaven, og du får et fast skriftligt tilbud. Vi svarer inden for 24 timer på hverdage.</p>
  <p>Vi kører også til resten af Nordsjælland. Se <a href="/omrader/">alle områder</a>.</p>
  <h2>Ofte stillede spørgsmål</h2>
  <div class="faq">{''.join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in hund_faq)}</div>
</div></section>
{cta()}"""
side("tomrer-hundested", "Tømrer i Hundested | Rosendal Tømrer",
     "Tømrer i Hundested: tag, vinduer, døre, terrasser, tilbygning og renovering. Tømrermester med værksted på Engdraget 11. Ring 50 70 05 05.",
     hund, active="tomrer-hundested", schemas=[faq_schema(hund_faq)],
     krummer=[("Områder", "omrader"), ("Tømrer i Hundested", None)])

# ---------------- ANMELDELSER ----------------
def case(key):
    t, q, n, by, d, k, typ = A[key]
    return (f'<article class="case"><div class="case-top"><div class="case-type">{e(typ)}</div><h3>{e(t)}</h3></div>'
            f'<div class="case-body"><div>{stj(k)}</div><blockquote>{e(q)}</blockquote>'
            f'<div class="who"><strong>{e(n)}</strong>, {e(by)} · {e(d)}</div></div></article>')

proj_html = ""
if LIVE:
    kort = "".join(f'<a class="ref-card" href="/projekter/{p["slug"]}/"><div class="ref-card-media"><img src="{p["billeder"][0][0]}" alt="{e(p["billeder"][0][1])}" loading="lazy"></div>'
                   f'<div class="ref-card-body"><h3>{e(p["titel"])}</h3><p>{e(p["by"])} · {e(p["maaned"])}</p></div></a>' for p in LIVE)
    proj_html = f'<section class="sec"><div class="container"><div class="sec-head"><h2>Projekter</h2></div><div class="refs-grid">{kort}</div></div></section>'

ref_body = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Anmeldelser", None)])}
  <h1>Anmeldelser fra vores kunder</h1>
  <p>Vi er stolte af at have {ANM_SNIT} i gennemsnit på Anmeld Håndværker. Her kan du læse, hvad vores kunder skriver om os.</p>
</div></section>
{proj_html}
<section class="sec sec-mist"><div class="container">
  <div class="sec-head" style="margin:0"><h2>Anmeldelser fra Anmeld Håndværker</h2><p>Kommunikation, aftaler, pris, tilfredshed og oprydning. Listen opdateres automatisk.</p></div>
  <div class="ah-widget">{AH_LISTE_DIV}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Læs alle anmeldelser på Anmeld Håndværker</a><a href="{FB_ANM}" target="_blank" rel="noopener">Anmeldelser på Facebook</a></div>
</div></section>
{some()}
{cta()}"""
side("anmeldelser", "Anmeldelser fra kunder | Rosendal Tømrer",
     "Læs anmeldelser fra vores kunder på Anmeld Håndværker. Tag, vinduer, terrasser, tilbygning og renovering i Hundested og Nordsjælland.",
     ref_body, schemas=[schema_virksomhed()], krummer=[("Anmeldelser", None)], extra_js=AH_LISTE_JS)

# ---------------- PROJEKTSIDER (kun naar status = live) ----------------
def projekt_side(p):
    ydl = dict(YDELSER)[p["ydelse"]]
    imgs = "".join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy" data-lb></figure>' for s, a in p["billeder"])
    body = (f'<section class="page-header"><div class="container">{crumb_html([("Projekter", "projekter"), (p["titel"], None)])}'
            f'<h1>{e(p["titel"])}</h1><p>{e(p["by"])} · {e(p["maaned"])}</p></div></section>'
            f'<section class="sec"><div class="container"><div class="proj-gallery">{imgs}</div></div></section>'
            f'<section class="sec sec-mist"><div class="container narrow prose">{rev_mini([p["anm"]])}'
            f'<p>Læs mere om <a href="{url(p["ydelse"])}">{e(ydl.lower())}</a> eller <a href="/tomrer-hundested/">tømrer i Hundested</a>.</p></div></section>{cta()}')
    side(f"projekter/{p['slug']}", f"{p['titel']} | Rosendal Tømrer", f"{p['titel']} i {p['by']}, {p['maaned']}. Udført af Rosendal Tømrer. Ring 50 70 05 05.",
         body, active="projekter", extra_js=LB_JS, krummer=[("Projekter", "projekter"), (p["titel"], None)])

if LIVE:
    kort = "".join(f'<a class="ref-card" href="/projekter/{p["slug"]}/"><div class="ref-card-media"><img src="{p["billeder"][0][0]}" alt="{e(p["billeder"][0][1])}" loading="lazy"></div>'
                   f'<div class="ref-card-body"><h3>{e(p["titel"])}</h3><p>{e(p["by"])} · {e(p["maaned"])}</p></div></a>' for p in LIVE)
    side("projekter", "Projekter | Rosendal Tømrer", "Se udvalgte projekter fra Rosendal Tømrer i Hundested og Nordsjælland: tag, vinduer, terrasser, tilbygning og renovering.",
         f'<section class="page-header"><div class="container">{crumb_html([("Projekter", None)])}<h1>Projekter</h1><p>Udvalgte opgaver, vist med billeder af det færdige resultat.</p></div></section>'
         f'<section class="sec"><div class="container"><div class="refs-grid">{kort}</div></div></section>{cta()}', krummer=[("Projekter", None)])
    for p in LIVE:
        projekt_side(p)

# ---------------- FORMULARER ----------------
# Ingen honeypot (_gotcha): Formspree's eget spamfilter (Formshield) er nok, og et skjult
# felt kan blive udfyldt af Chromes autoudfyld, saa en rigtig henvendelse forsvinder.
# NB: Formshield lagde testbeskeder som "asdasd" i Spam. Test altid med rigtige saetninger.
# Efter afsendelse sendes besoegende til /tak/ (egen side, noindex), hvor maalingen sker.
FORM_ACTION = f"https://formspree.io/f/{FORMSPREE_ID}" if FORMSPREE_ID else "#"
FORM_JS = """<script>(function(){var f=document.getElementById('kf');
f.addEventListener('submit',function(ev){ev.preventDefault();var b=f.querySelector('button[type=submit]'),t=b.textContent;b.disabled=true;b.textContent='Sender...';
if(f.getAttribute('action')==='#'){b.disabled=false;b.textContent=t;alert('Formularen er ikke koblet til endnu (demo). Ring på 50 70 05 05.');return;}
fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){if(r.ok){window.location.href=f.getAttribute('data-tak');}else{throw 0;}})
.catch(function(){b.disabled=false;b.textContent=t;alert('Formularen kunne ikke sendes. Ring på 50 70 05 05 eller skriv til info@rosendal-tomrer.dk.');});});})();</script>"""

job = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Job", None)])}
  <h1>Er du vores nye tømrer?</h1>
  <p>Vi søger løbende tømrersvende til holdet. Også selvom der ikke ligger et opslag ude.</p>
</div></section>
<section class="sec"><div class="container contact-grid">
  <div class="prose">
    <img class="job-img" src="/images/jobbil.webp" alt="Rosendal Tømrers firmabil ved værkstedet med en kasse i træ" width="587" height="585" loading="lazy">
    <h2>Hvem er vi?</h2>
    <p>Hos Rosendal Tømrer Entreprise er vi kvalitetsbevidste og stolte af vores faglige kunnen. Vi går på arbejde med glæde, fordi vi laver det vi brænder for, og vi lægger vægt på et kammeratligt og tæt sammenhold.</p>
    <p>Vi laver alle former for tømreropgaver, fordi vi kan lide at to dage ikke er ens: tag, døre og vinduer, terrasser, hegn, skure, gårdmiljøer, nybyg og renovering. Alt udføres ud fra kundens ønsker, så det er vigtigt at du er god til at tale med kunderne fra start til slut.</p>
    <h2>Fortæl os gerne</h2>
    <ul><li>Kort hvem du er</li><li>Din erfaring og tidligere arbejde</li><li>Hvorfor du elsker tømrerfaget</li><li>Hvorfor du er vores nye kollega</li></ul>
    <p>Du kan også bare ringe til Sebastian på <a href="tel:{TLF_RAW}">{TLF}</a>.</p>
  </div>
  <div>
    <form class="kf" id="kf" action="{FORM_ACTION}" method="POST" data-tak="/tak/?f=job">
      <h2>Søg job hos Danmarks fedeste tømrerfirma</h2>
      <p class="sub">Måske er det dig vi lige står og mangler? Send en besked, så vender vi tilbage til dig.</p>
      <input type="hidden" name="Formular" value="Jobansøgning">
      <input type="hidden" name="_subject" value="Jobansøgning via hjemmesiden">
      <div class="f-g"><label for="navn">Navn</label><input id="navn" name="Navn" required autocomplete="name"></div>
      <div class="f-row">
        <div class="f-g"><label for="mail">E-mail</label><input id="mail" name="_replyto" type="email" required autocomplete="email"></div>
        <div class="f-g"><label for="tlf">Telefon</label><input id="tlf" name="Telefon" type="tel" required autocomplete="tel"></div>
      </div>
      <div class="f-g"><label for="besk">Besked</label><textarea id="besk" name="Besked" required></textarea></div>
      <button class="btn btn-primary" type="submit">Send ansøgning</button>
    </form>
  </div>
</div></section>
{cta("Spørgsmål om job?", "Ring til Sebastian og tag en uforpligtende snak.")}"""
side("job", "Job som tømrer i Nordsjælland | Rosendal Tømrer",
     "Vi søger løbende tømrersvende til holdet i Hundested. Send en ansøgning via formularen eller ring til Sebastian på 50 70 05 05.", job,
     extra_js=FORM_JS, krummer=[("Job", None)])

valg = "".join(f"<option>{e(n)}</option>" for _, n in YDELSER) + "<option>Andet</option>"
kontakt = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Kontakt", None)])}
  <h1>Få et uforpligtende tilbud</h1>
  <p>Fortæl kort om opgaven, så vender vi tilbage inden for 24 timer på hverdage. Den hurtigste vej er telefonen.</p>
</div></section>
<section class="sec"><div class="container contact-grid">
  <div>
    <div class="c-item"><div><div class="c-label">Telefon</div><div class="c-value c-big"><a href="tel:{TLF_RAW}">{TLF}</a></div></div></div>
    <div class="c-item"><div><div class="c-label">Åbningstid</div><div class="c-value">{AABNING}</div></div></div>
    <div class="c-item"><div><div class="c-label">E-mail</div><div class="c-value"><a href="mailto:{MAIL}">{MAIL}</a></div></div></div>
    <div class="c-item"><div><div class="c-label">Adresse</div><div class="c-value">{ADR}, {POST} {BY}</div></div></div>
    <div class="c-item"><div><div class="c-label">CVR</div><div class="c-value">{CVR}</div></div></div>
    <div class="map-wrap" id="mapWrap"><button type="button" class="map-consent" onclick="ckAccepterKort()">
      <strong>Vis kort</strong><span>Kortet hentes fra Google Maps, som sætter cookies. Klikker du her, accepterer du det, og kortet vises med det samme.</span></button></div>
  </div>
  <div>
    <form class="kf" id="kf" action="{FORM_ACTION}" method="POST" data-tak="/tak/">
      <input type="hidden" name="Formular" value="Kontakt">
      <input type="hidden" name="_subject" value="Henvendelse via hjemmesiden">
      <h2>Send en henvendelse</h2>
      <p class="sub">Jo mere du fortæller, jo bedre kan vi give et retvisende tilbud.</p>
      <div class="f-row">
        <div class="f-g"><label for="navn">Navn</label><input id="navn" name="Navn" required autocomplete="name"></div>
        <div class="f-g"><label for="tlf">Telefon</label><input id="tlf" name="Telefon" type="tel" required autocomplete="tel"></div>
      </div>
      <div class="f-g"><label for="mail">E-mail</label><input id="mail" name="_replyto" type="email" required autocomplete="email"></div>
      <div class="f-row">
        <div class="f-g"><label for="type">Type opgave <span>(valgfrit)</span></label><select id="type" name="Type opgave"><option value="">Vælg</option>{valg}</select></div>
        <div class="f-g"><label for="adr">By eller postnummer <span>(valgfrit)</span></label><input id="adr" name="By eller postnummer"></div>
      </div>
      <div class="f-g"><label for="besk">Beskriv opgaven</label><textarea id="besk" name="Beskrivelse" required></textarea></div>
      <p class="f-note">Har du billeder af opgaven? Send dem gerne til <a href="mailto:{MAIL}">{MAIL}</a>, efter du har sendt formularen.</p>
      <button class="btn btn-primary" type="submit">Send henvendelse</button>
    </form>
  </div>
</div></section>"""
side("kontakt", "Kontakt Rosendal Tømrer | Ring 50 70 05 05",
     "Ring på 50 70 05 05 eller send en henvendelse. Vi vender tilbage inden for 24 timer på hverdage. Engdraget 11, 3390 Hundested.",
     kontakt, extra_js=FORM_JS, schemas=[schema_virksomhed()], krummer=[("Kontakt", None)])

TAK_JS = """<script>(function(){var job=/[?&]f=job/.test(location.search);
if(typeof gtag==='function'){gtag('event','form_submit',{'formular':job?'job':'kontakt'});
if(!job){gtag('event','generate_lead',{'currency':'DKK','value':0});}}})();</script>"""
tak = f"""
<section class="sec tak"><div class="container narrow">
  <h1>Tak for din henvendelse</h1>
  <p class="lead" style="color:var(--muted);font-size:1.12rem;margin-top:.8rem">Vi har modtaget den og vender tilbage inden for 24 timer på hverdage. Haster det, så ring på <a href="tel:{TLF_RAW}" style="text-decoration:underline">{TLF}</a>.</p>
  <div class="btn-row"><a class="btn btn-primary" href="/">Til forsiden</a><a class="btn btn-ghost" href="/anmeldelser/">Læs, hvad kunderne siger</a></div>
</div></section>"""
side("tak", "Tak for din henvendelse | Rosendal Tømrer", "Tak for din henvendelse. Vi vender tilbage inden for 24 timer på hverdage.",
     tak, noindex=True, extra_js=TAK_JS)

cookies = f"""
<section class="page-header"><div class="container">{crumb_html([("Cookiepolitik", None)])}
<h1>Cookiepolitik</h1><p>Her kan du se hvilke cookies vi bruger, og hvordan du ændrer dit valg.</p></div></section>
<section class="sec"><div class="container narrow prose">
  <h2>Hvad er cookies?</h2><p>En cookie er en lille tekstfil, som gemmes i din browser. Vi sætter kun cookies, der ikke er nødvendige, hvis du har sagt ja.</p>
  <h2>Nødvendige cookies</h2><p><strong>{COOKIE}</strong> gemmer dit valg i cookiebanneret i 12 måneder. Den er nødvendig for at vi kan huske dit svar.</p>
  <h2>Statistik og marketing</h2><p>Hvis du accepterer, bruger vi Google Analytics til at se, hvordan siden bliver brugt. Afviser du, sendes der kun anonyme signaler uden cookies.</p>
  <h2>Anmeldelser fra Anmeld Håndværker</h2><p>På forsiden og på siden med anmeldelser vises anmeldelser med en widget fra Anmeld Håndværker. Den hentes fra deres server, når siden åbnes.</p>
  <h2>Google Maps</h2><p>Kortet på kontaktsiden hentes fra Google og sætter cookies. Det vises derfor først, når du har accepteret.</p>
  <h2>Skift dit valg</h2><p>Du kan altid ændre eller trække dit samtykke tilbage via linket "Skift cookieindstillinger" nederst på alle sider.</p>
  <h2>Ansvarlig</h2><p>{e(NAVN)}, {ADR}, {POST} {BY}. CVR {CVR}. <a href="mailto:{MAIL}">{MAIL}</a></p>
</div></section>"""
side("cookies", "Cookiepolitik | Rosendal Tømrer",
     "Sådan bruger rosendal-tomrer.dk cookies, og hvordan du ændrer eller trækker dit samtykke tilbage.", cookies, noindex=True)

# Afskrevet fra det gamle sites PDF (Rosendal-Materieludlejning-Betingelser.pdf). Indholdet er bevaret, kun stavning
# og tegnsaetning er rettet. Det er juridisk tekst, saa aendringer i indholdet skal komme fra Sebastian.
lb = f"""
<section class="page-header"><div class="container">{crumb_html([("Materieludlejning", "materieludlejning"), ("Lejebetingelser", None)])}
<h1>Lejebetingelser for materieludlejning</h1><p>Gælder for al leje af materiel hos {e(NAVN)}.</p></div></section>
<section class="sec"><div class="container narrow prose">
  <h2>1. Lejeperiode</h2>
  <p>Al udlejning af materiel sker pr. kalenderdag, og én kalenderdag tælles som 8 timer. Bruges det lejede materiel mere end 8 timer, afregnes der én ekstra kalenderdag.</p>
  <p>Lejet materiel må kun benyttes til arbejde på de lejede dage.</p>
  <h2>2. Brug og ansvar</h2>
  <p>Lejet materiel må kun benyttes af lejeren eller af andre, der står skrevet i kontrakten. Udlejer er ikke ansvarlig for personskader eller andet i forbindelse med brugen. Ligeledes er udlejer ikke erstatningsansvarlig for tab som følge af arbejdsafbrydelser, funktionssvigt, driftstab, avancetab eller andet tab.</p>
  <h2>3. Fremleje og tilbagelevering</h2>
  <p>Lejer må ikke fremleje eller handle med lejet materiel. Alt lejet materiel skal tilbageleveres på udlejers plads til den aftalte tid og i samme stand. Lejer erklærer sig indforstået med, at udlejer ved lejers svigtende tilbagelevering kan komme i besiddelse af materiellet ved en fogedforretning på lejers regning.</p>
  <h2>4. Skader, tyveri og selvrisiko</h2>
  <p>Har lejer beskadiget lejet materiel, forpligter lejer sig til at erstatte bortkommet eller beskadiget materiel. Ved tyveri, brand, hærværk m.v. forpligter lejer sig til en selvrisiko på 35 % af materiellets værdi. Selvrisikoen er oplyst ekskl. moms.</p>
  <h2>5. Uheld</h2>
  <p>Udgifter for lejer på grund af uheld er udlejer uvedkommende.</p>
  <h2>6. Forsikringsgebyr</h2>
  <p>Der tillægges et almindeligt forsikringsgebyr på 7 % af den samlede pris.</p>
  <h2>7. Ansvarsforsikring</h2>
  <p>Udlejer tegner ansvarsforsikring mod det erstatningsansvar, som udlejer ifølge dansk ret måtte ifalde for skader på personer eller ejendom (tingskader). Udlejer påtager sig intet ansvar og ingen risiko, hvorfor dette påhviler lejer. Såfremt udlejer bliver pålagt dette ansvar, er lejer forpligtet til at holde udlejer skadesløs for ethvert ansvar.</p>
  <h2>Annullering</h2>
  <p>Annullering af en ordre skal ske senest 7 dage før den aftalte booking. Ved annullering opkræves et gebyr på 220 kr. ekskl. moms (275 kr. inkl. moms).</p>
  <h2>Kontrol, rengøring og brændstof</h2>
  <p>I lejeperioden er udlejer forpligtet til at lave sikkerheds- og driftsmæssige kontroller af lejet materiel, herunder væskestand, batterier og løbende rengøring.</p>
  <p>Ved manglende rengøring opkræves et gebyr på 400 kr. ekskl. moms (500 kr. inkl. moms).</p>
  <p>Alle benzindrevne maskiner udleveres uden brændstof, og det er lejers ansvar at påfylde korrekte væsker i henhold til anvisningerne.</p>
  <h2>Ansvar og erstatning</h2>
  <p>Lejer påtager sig alt ansvar og al risiko ved lejet materiel, herunder skader på personer, ting eller materiel, uanset om skaderne sker som følge af forkerte oplysninger.</p>
  <p>Lejer er ikke berettiget til at kræve erstatning for tab opstået i forbindelse med brug af materiellet.</p>
  <h2>Levering og afhentning</h2>
  <p>Ved levering eller afhentning af lejet materiel: kontakt os for pris.</p>
  <h2>Udlejer</h2>
  <p>{e(NAVN)}, {ADR}, {POST} {BY}. CVR {CVR}. Telefon <a href="tel:{TLF_RAW}">{TLF}</a>, <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</div></section>"""
side("lejebetingelser", "Lejebetingelser for materieludlejning | Rosendal",
     "Betingelser for leje af materiel hos Rosendal Tømrer Entreprise ApS: lejeperiode, selvrisiko, forsikringsgebyr, annullering og rengøring.", lb, noindex=True)

# ---------------- 404 ----------------
f404 = f"""<section class="page-header"><div class="container"><h1>Siden findes ikke</h1>
<p>Adressen er måske ændret, da vi fik ny hjemmeside. Gå til forsiden, eller ring, hvis du leder efter noget bestemt.</p>
<div class="btn-row"><a class="btn btn-brass" href="/">Til forsiden</a><a class="btn btn-ghost" href="tel:{TLF_RAW}">Ring {TLF}</a></div></div></section>
<section class="sec"><div class="container">{svc_grid()}</div></section>"""
skriv("404.html", build_page("404", "Siden findes ikke | Rosendal Tømrer", "Siden findes ikke. Gå til forsiden eller ring på 50 70 05 05.", f404, noindex=True))

# ---------------- REDIRECTS (gamle URL'er -> nye) ----------------
# Gamle sider laa som <navn>.html. De oprindelige WordPress-adresser var /<slug>/ og er enten nye sider
# (terrasse, tag, nybyg, renovering, job, kontakt) eller omdirigeres her. Rigtige 301'ere kommer fra .htaccess paa
# Simply. Stubbene er reserve (meta refresh + canonical), hvis .htaccess ikke kan bruges, og de virker paa testsiden.
HTML_GAMLE = {"hovedentreprise.html": "totalentreprise", "doere-og-vinduer.html": "vinduer", "gaardhaver.html": "pergola-hegn-og-cykelskur",
              "materieludlejning.html": "materieludlejning", "referencer.html": "anmeldelser", "terrasse.html": "terrasse",
              "tag.html": "tag", "nybyg.html": "nybyg", "renovering.html": "renovering", "job.html": "job", "kontakt.html": "kontakt",
              "cookies.html": "cookies", "lejebetingelser.html": "lejebetingelser"}
# /materieludlejning/ var ogsaa WordPress-adressen og er nu siden selv. udlejning-af-stillads-og-trailer var kun paa testsiden.
WP_GAMLE = {"doere-vinduer": "vinduer", "gaardhaver": "pergola-hegn-og-cykelskur", "udlejning-af-stillads-og-trailer": "materieludlejning"}

def stub(fil, ny, dybde):
    rel = "../" * dybde + ny + "/"
    skriv(fil, f"""<!DOCTYPE html><html lang="da"><head><meta charset="UTF-8">
<title>Siden er flyttet</title><link rel="canonical" href="{DOMAIN}{url(ny)}"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={rel}"></head><body><p>Siden er flyttet til <a href="{rel}">{DOMAIN}{url(ny)}</a>.</p></body></html>
""")
for g, n in HTML_GAMLE.items(): stub(g, n, 0)
for g, n in WP_GAMLE.items(): stub(f"{g}/index.html", n, 1)

# ---------------- .HTACCESS (Simply.com, Apache) ----------------
# Gamle URL'er foerst og med fuld adresse, saa de kun bruger ét hop. Derefter 410 paa WordPress-stierne (Google dropper
# spam-siderne fra infektionen hurtigere) og til sidst HTTPS uden www.
# Maa IKKE indeholde en regel for index.html: DirectoryIndex rammer den internt og giver en endeloes loekke.
vaert = DOMAIN.split("//")[1]
htaccess = f"""Options -Indexes -MultiViews
DirectoryIndex index.html
ErrorDocument 404 /404.html
ErrorDocument 410 /404.html

RewriteEngine On
# Gamle .html-adresser og WordPress-adresser til de nye sider (301)
""" + "".join(f"RewriteRule ^{g.replace('.', chr(92) + '.')}$ {DOMAIN}{url(n)} [R=301,L]\n" for g, n in HTML_GAMLE.items()) \
    + "".join(f"RewriteRule ^{g}/?$ {DOMAIN}{url(n)} [R=301,L]\n" for g, n in WP_GAMLE.items()) + f"""
# WordPress-rester findes ikke laengere (410)
RewriteRule ^(wp-admin|wp-content|wp-includes|wp-json)(/.*)?$ - [G,L]
RewriteRule ^(wp-login\\.php|xmlrpc\\.php|wp-config\\.php)$ - [G,L]

# HTTPS og uden www
RewriteCond %{{HTTPS}} off [OR]
RewriteCond %{{HTTP_HOST}} ^www\\. [NC]
RewriteRule ^(.*)$ https://{vaert}/$1 [R=301,L]

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 month"
  ExpiresByType image/png "access plus 1 month"
  ExpiresByType image/jpeg "access plus 1 month"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
"""
skriv(".htaccess", htaccess)

# ---------------- ROBOTS, SITEMAP, LLMS ----------------
bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Google-Extended", "ClaudeBot", "Claude-SearchBot", "Applebot-Extended"]
skriv("robots.txt", "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {DOMAIN}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{DOMAIN}{url(s)}</loc><lastmod>{SIDST_OPDATERET}</lastmod></url>\n" for s in SIDER)
skriv("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
ylist = "\n".join(f"- [{n}]({DOMAIN}{url(sl)})" for sl, n in YDELSER)
skriv("llms.txt", f"""# {NAVN}

> Tømrerfirma i Hundested, stiftet 2021 af tømrermester og bygningskonstruktør Sebastian Norborg Rosendal. Fag-, hoved- og totalentrepriser for private og erhverv i Nordsjælland: tilbygning, tag, vinduer og døre, terrasser, sommerhuse, renovering og nybyg.

- Telefon: {TLF}
- E-mail: {MAIL}
- Adresse: {ADR}, {POST} {BY} (værksted og kontor)
- CVR: {CVR}
- Anmeldelser: {ANM_SNIT} ud af 5, {ANM_TEKST} anmeldelser på Anmeld Håndværker ({ANM_URL})
- Åbningstid: {AABNING}
- Serviceområde: Hundested og resten af Nordsjælland, med base på Engdraget 11 i Hundested

## Ydelser
{ylist}

## Andet
- [Om os]({DOMAIN}/om-os/)
- [Områder]({DOMAIN}/omrader/)
- [Tømrer i Hundested]({DOMAIN}/tomrer-hundested/)
- [Anmeldelser]({DOMAIN}/anmeldelser/)
- [Kontakt]({DOMAIN}/kontakt/)
""")

if not LIVEBYG:
    skriv(".nojekyll", "")  # kun GitHub Pages bruger den
else:
    zipsti = shutil.make_archive(os.path.join(ROD, "rosendal-tomrer-live"), "zip", OUT)
    print(f"Live-zip: {os.path.abspath(zipsti)}")
print("Bygget:", len(SIDER), "indekserbare sider i", os.path.abspath(OUT))
