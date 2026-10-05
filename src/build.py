"""Bygger hele sitet til ../docs. Idempotent: kan koeres igen og igen."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from site_shared import *
from indhold import ANMELDELSER as A, YDELSER as Y

OUT = os.path.join(os.path.dirname(__file__), "..", "docs")
SIDER = []

def skriv(navn, txt):
    p = os.path.join(OUT, navn)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)

def side(slug, *a, **k):
    skriv(f"{slug}.html", build_page(slug, *a, **k))
    if not k.get("noindex"):
        SIDER.append(slug)

STJ = '<span class="stars" aria-hidden="true">★★★★★</span>'

def rev_kort(key, cls="rev"):
    t, q, n, by, d = A[key]
    return (f'<article class="{cls}">{STJ}<h3>{e(t)}</h3><blockquote>{e(q)}</blockquote>'
            f'<div class="who"><strong>{e(n)}</strong>, {e(by)} · {e(d)}</div></article>')

def rev_en(key):
    t, q, n, by, d = A[key]
    return (f'<figure class="rev-one"><blockquote>"{e(q)}"</blockquote>'
            f'<figcaption class="who">{STJ} {e(n)}, {e(by)} · Verificeret anmeldelse på '
            f'<a href="{ANM_URL}" target="_blank" rel="noopener" style="text-decoration:underline">Anmeld Håndværker</a></figcaption></figure>')

KORT_TXT = {
    "nybyg": "Tilbygninger, gæstehuse, carporte og nye huse.",
    "tag": "Nyt tag, tagrenovering og efterisolering.",
    "doere-og-vinduer": "Vinduer, yderdøre, foldedøre og franske altaner.",
    "terrasse": "Træterrasser, repos og trappetrin.",
    "gaardhaver": "Overdækkede gårdhaver, udestuer og pergolaer.",
    "renovering": "Indvendig og udvendig renovering af hus og sommerhus.",
    "materieludlejning": "Lej stillads og trailer, når vi ikke selv bruger det.",
}

def svc_grid():
    out = ['<div class="svc-grid">',
           f'<a class="svc svc-feature" href="hovedentreprise.html">{HEX}<h3>Hoved- og fagentreprise</h3>'
           '<p>Vi styrer hele byggeriet og koordinerer murer, elektriker, VVS og maler. Én kontrakt, én kontakt og ét ansvar fra start til aflevering.</p>'
           '<span class="svc-go">Sådan foregår det</span></a>']
    for s, n in YDELSER[1:]:
        if s == "materieludlejning": continue
        out.append(f'<a class="svc" href="{s}.html">{HEX}<h3>{e(n)}</h3><p>{KORT_TXT[s]}</p><span class="svc-go">Læs mere</span></a>')
    out.append("</div>")
    out.append('<p class="svc-more">Vi lejer også stillads og trailer ud. <a href="materieludlejning.html">Se materieludlejning</a></p>')
    return "\n".join(out)

TRUST = f"""<div class="container trust">
  <div><strong>Tømrermester</strong><span>og uddannet bygningskonstruktør</span></div>
  <div><strong>{ANM_SNIT} ud af 5</strong><span>{ANM_ANTAL} verificerede anmeldelser</span></div>
  <div><strong>Dansk Håndværk</strong><span>Medlem med garantiordning</span></div>
  <div><strong>Eget materiel</strong><span>Stillads, trailer og værksted i Hundested</span></div>
</div>"""

# ---------------- FORSIDE ----------------
forside = f"""
<section class="hero">
  <div class="hero-text"><div class="hero-inner">
    <div class="hero-kicker">Tømrermester og bygningskonstruktør</div>
    <h1>Tømrer og hovedentreprenør i Nordsjælland</h1>
    <p class="lead">Vi bygger til, bygger nyt og renoverer for private og erhverv. Et fast hold af tømrere, én kontakt og aftaler der bliver holdt.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a>
      <a class="btn btn-ghost" href="kontakt.html">Få et tilbud</a>
    </div>
    <div class="hero-proof"><strong>{ANM_SNIT}</strong><div>{STJ}<br>{ANM_ANTAL} anmeldelser på Anmeld Håndværker</div></div>
  </div></div>
  <div class="hero-img"><img src="images/firmabil.webp" srcset="images/firmabil-900.webp 900w, images/firmabil.webp 1440w" sizes="(max-width:820px) 100vw, 55vw"
    alt="Rosendal Tømrers firmabil med trailer, stillads og lægter klar til en opgave i Nordsjælland" width="1440" height="1080" fetchpriority="high"></div>
</section>

<section class="sec-mist">{TRUST}</section>

<section class="sec" id="om"><div class="container about">
  <div class="prose">
    <h2>Et tømrerfirma der tager hele opgaven</h2>
    <p>Rosendal Tømrer Entreprise blev stiftet i 2021 af Sebastian Norborg Rosendal, der er tømrermester og uddannet bygningskonstruktør. I dag er vi et fast hold af tømrere med base på Engdraget i Hundested.</p>
    <p>Vi laver alt fra en enkelt ny terrassedør til tilbygninger og totalrenoveringer, hvor vi står for hele byggeriet og koordinerer de andre fag. Det er den samme tilgang uanset størrelsen: vi giver en ærlig vurdering, et klart tilbud, og så gør vi det vi har aftalt.</p>
    <p>Det kan du læse i vores anmeldelser, hvor kunderne går igen på de samme ting: aftaler der holder, svende der er til at snakke med, og pænt ryddet op når vi går.</p>
  </div>
  <ul class="principles">
    <li><strong>Én kontakt hele vejen</strong><span>Sebastian er altid til at få fat på, fra første besøg til aflevering.</span></li>
    <li><strong>Aftaler der holder</strong><span>Pris, tidsplan og omfang står i tilbuddet. Opstår der noget undervejs, hører du det før vi går videre.</span></li>
    <li><strong>Byggeteknisk overblik</strong><span>Som bygningskonstruktør kan Sebastian hjælpe med planlægning og tegninger, før der skal bygges.</span></li>
    <li><strong>Ryddet op hver dag</strong><span>Vi arbejder i dit hjem og opfører os derefter.</span></li>
  </ul>
</div></section>

<section class="sec sec-mist"><div class="container">
  <div class="sec-head"><h2>Det laver vi</h2><p>Fra små opgaver til hele byggerier. Vælg en ydelse og læs mere om hvordan vi griber den an.</p></div>
  {svc_grid()}
</div></section>

<section class="sec"><div class="container">
  <div class="rev-top">
    <div class="sec-head" style="margin:0"><h2>Det siger kunderne</h2><p>Udvalgte, verificerede anmeldelser fra Anmeld Håndværker.</p></div>
    <div class="rev-score"><span class="big">{ANM_SNIT}</span><span class="meta">{STJ}<br>ud af 5 baseret på {ANM_ANTAL} anmeldelser</span></div>
  </div>
  <div class="rev-grid">{rev_kort('brian')}{rev_kort('rita')}{rev_kort('morten')}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Se alle {ANM_ANTAL} anmeldelser</a><a href="referencer.html">Se udvalgte opgaver</a></div>
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
{some()}
{cta()}
"""
side("index", "Tømrer og hovedentreprenør i Nordsjælland · Rosendal",
     "Tømrermester og bygningskonstruktør i Hundested. Nybyg, tilbygning, tag, vinduer, terrasser og renovering. 4,9 ud af 5 på 37 anmeldelser.",
     forside, schemas=[schema_virksomhed()])

# ---------------- YDELSESSIDER ----------------
def ydelse(slug):
    d = Y[slug]
    navn = dict(YDELSER)[slug]
    blokke = []
    for h2, indhold in d["sek"]:
        if isinstance(indhold, tuple):
            body = "<ul>" + "".join(f"<li>{e(x)}</li>" for x in indhold[1]) + "</ul>"
        else:
            body = "".join(f"<p>{e(x)}</p>" for x in indhold)
        blokke.append(f"<h2>{e(h2)}</h2>{body}")
    anm = rev_en(d["anm"]) if d["anm"] else ""
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    andre = "".join(f'<li><a href="{s}.html">{e(n)}</a></li>' for s, n in YDELSER if s != slug)
    body = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Forside</a> / Ydelser / {e(navn)}</div>
  <h1>{e(d['h1'])}</h1><p>{e(d['intro'])}</p>
  <div class="btn-row"><a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a><a class="btn btn-ghost" href="kontakt.html">Få et tilbud</a></div>
</div></section>
<section class="sec"><div class="container narrow prose">{''.join(blokke)}{anm}</div></section>
<section class="sec sec-mist"><div class="container narrow">
  <div class="sec-head"><h2>Ofte stillede spørgsmål</h2></div>
  <div class="faq">{faq}</div>
</div></section>
<section class="sec" style="padding:3rem 0"><div class="container narrow prose">
  <h2 style="font-size:1.3rem">Andre ydelser</h2><ul>{andre}</ul>
</div></section>
{cta()}"""
    side(slug, d["title"], d["desc"], body, active=slug, schemas=[schema_virksomhed(), faq_schema(d["faq"])])

for s, _ in YDELSER:
    ydelse(s)

# ---------------- REFERENCER ----------------
# Projekter med billeder. status 'pending' = skjult indtil der er faerdigbilleder.
PROJEKTER = [
    dict(slug="tilbygning-gaestehus", titel="Tilbygning og gæstehus", by="Hundested", status="pending", billeder=[]),
    dict(slug="sommerhus-nyt-tag", titel="Sommerhus med nyt tag", by="Hundested", status="pending", billeder=[]),
    dict(slug="repos-ipe", titel="Repos-trappe i ipé", by="Veksø", status="pending", billeder=[]),
]
LIVE = [p for p in PROJEKTER if p["status"] == "live"]

CASES = [("rita", "Tilbygning · Hovedentreprise"), ("brian", "Renovering · Tag"),
         ("morten", "Terrasse"), ("ulla", "Tag · Carport"), ("peter", "Vinduer · Franske altaner"),
         ("anita", "Døre og vinduer"), ("erik", "Renovering"), ("anne", "Vinduer · Terrasse"), ("nila", "Vinduer")]

KARAKTER = {"nila": "4,2", "elisabeth": "4,8"}  # alle andre: 5,0

def case(key, typ):
    t, q, n, by, d = A[key]
    k = KARAKTER.get(key)
    st = f'<span class="stars" aria-hidden="true">★★★★☆</span> <strong>{k}</strong>' if k else STJ
    return (f'<article class="case"><div class="case-top"><div class="case-type">{e(typ)}</div><h3>{e(t)}</h3></div>'
            f'<div class="case-body"><div>{st}</div><blockquote>{e(q)}</blockquote>'
            f'<div class="who"><strong>{e(n)}</strong>, {e(by)} · {e(d)}</div></div></article>')

proj_html = ""
if LIVE:
    kort = "".join(f'<a class="ref-card" href="projekt-{p["slug"]}.html"><div class="ref-card-media"><img src="{p["billeder"][0][0]}" alt="{e(p["billeder"][0][1])}" loading="lazy"></div>'
                   f'<div class="ref-card-body"><h3>{e(p["titel"])}</h3><p>{e(p["by"])}</p></div></a>' for p in LIVE)
    proj_html = f'<section class="sec"><div class="container"><div class="sec-head"><h2>Projekter</h2></div><div class="refs-grid">{kort}</div></div></section>'

ref_body = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Forside</a> / Referencer</div>
  <h1>Udvalgte opgaver</h1>
  <p>Et udsnit af de opgaver vi har løst for kunder i Nordsjælland, fortalt med kundernes egne ord. Alle anmeldelser er verificerede på Anmeld Håndværker.</p>
</div></section>
{proj_html}
<section class="sec sec-mist"><div class="container">
  <div class="rev-top">
    <div class="sec-head" style="margin:0"><h2>{ANM_ANTAL} anmeldelser, {ANM_SNIT} i snit</h2><p>Kommunikation, aftaler, pris, tilfredshed og oprydning.</p></div>
  </div>
  <div class="refs-grid">{''.join(case(k, t) for k, t in CASES)}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Læs alle anmeldelser på Anmeld Håndværker</a><a href="{FB_ANM}" target="_blank" rel="noopener">Anmeldelser på Facebook</a></div>
</div></section>
{some()}
{cta()}"""
side("referencer", "Referencer og anmeldelser · Rosendal Tømrer",
     "Udvalgte opgaver og 37 verificerede anmeldelser med et snit på 4,9 ud af 5. Tilbygning, tag, vinduer, terrasser og renovering i Nordsjælland.",
     ref_body, schemas=[schema_virksomhed()])

LB_JS = """<div class="lb" id="lb" role="dialog" aria-label="Billedvisning"><button class="lb-close" aria-label="Luk">×</button><button class="lb-prev" aria-label="Forrige">‹</button><img alt=""><button class="lb-next" aria-label="Næste">›</button></div>
<script>(function(){var L=document.getElementById('lb'),I=L.querySelector('img'),B=[].slice.call(document.querySelectorAll('[data-lb]')),i=0;
function v(n){i=(n+B.length)%B.length;I.src=B[i].src;I.alt=B[i].alt;L.classList.add('open');}
B.forEach(function(b,n){b.addEventListener('click',function(){v(n);});});
L.querySelector('.lb-close').onclick=function(){L.classList.remove('open');};L.querySelector('.lb-prev').onclick=function(){v(i-1);};L.querySelector('.lb-next').onclick=function(){v(i+1);};
document.addEventListener('keydown',function(ev){if(!L.classList.contains('open'))return;if(ev.key==='Escape')L.classList.remove('open');if(ev.key==='ArrowLeft')v(i-1);if(ev.key==='ArrowRight')v(i+1);});})();</script>"""

for p in LIVE:
    imgs = "".join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy" data-lb></figure>' for s, a in p["billeder"])
    side(f"projekt-{p['slug']}", f"{p['titel']} · Rosendal Tømrer", p.get("desc", p["titel"]),
         f'<section class="page-header"><div class="container"><div class="crumb"><a href="referencer.html">Referencer</a></div><h1>{e(p["titel"])}</h1><p>{e(p["by"])}</p></div></section>'
         f'<section class="sec"><div class="container"><div class="proj-gallery">{imgs}</div></div></section>{cta()}',
         active="referencer", extra_js=LB_JS)

# ---------------- JOB ----------------
job = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Forside</a> / Job</div>
  <h1>Bliv en del af holdet</h1>
  <p>Vi er altid interesserede i at høre fra dygtige tømrere og lærlinge i Nordsjælland, også selvom vi ikke har et opslag ude.</p>
</div></section>
<section class="sec"><div class="container narrow prose">
  <h2>Hvem leder vi efter?</h2>
  <p>Vi leder efter faglærte tømrere og lærlinge, der er stolte af deres arbejde og gode til at tale med kunderne. Vores opgaver spænder fra vinduer og terrasser til tilbygninger og hele renoveringer, så hverdagen er afvekslende.</p>
  <h2>Hvad får du hos os?</h2>
  <ul>
    <li>Et fast hold og en mester der er til at få fat på</li>
    <li>Varierede opgaver, primært i Halsnæs og Nordsjælland</li>
    <li>Ordentligt værktøj, materiel og værksted i Hundested</li>
  </ul>
  <h2>Sådan søger du</h2>
  <p>Ring til Sebastian på <a href="tel:{TLF_RAW}">{TLF}</a> eller send et par linjer om dig selv til <a href="mailto:{MAIL}">{MAIL}</a>. Et langt CV er ikke nødvendigt.</p>
</div></section>
{cta("Spørgsmål om job?", "Ring til Sebastian og tag en uforpligtende snak.")}"""
side("job", "Job som tømrer i Nordsjælland · Rosendal Tømrer",
     "Er du tømrer eller lærling i Nordsjælland? Vi hører gerne fra dig, også selvom vi ikke har et opslag ude. Ring eller skriv til Sebastian.", job)

# ---------------- KONTAKT ----------------
valg = "".join(f"<option>{e(n)}</option>" for _, n in YDELSER) + "<option>Andet</option>"
action = f"https://formspree.io/f/{FORMSPREE_ID}" if FORMSPREE_ID else "#"
kontakt = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Forside</a> / Kontakt</div>
  <h1>Få et uforpligtende tilbud</h1>
  <p>Fortæl kort om opgaven, så vender vi tilbage inden for 24 timer på hverdage. Den hurtigste vej er telefonen.</p>
</div></section>
<section class="sec"><div class="container contact-grid">
  <div>
    <div class="c-item"><div><div class="c-label">Telefon</div><div class="c-value c-big"><a href="tel:{TLF_RAW}">{TLF}</a></div></div></div>
    <div class="c-item"><div><div class="c-label">E-mail</div><div class="c-value"><a href="mailto:{MAIL}">{MAIL}</a></div></div></div>
    <div class="c-item"><div><div class="c-label">Adresse</div><div class="c-value">{ADR}, {POST} {BY}</div></div></div>
    <div class="c-item"><div><div class="c-label">CVR</div><div class="c-value">{CVR}</div></div></div>
    <div class="map-wrap" id="mapWrap"><button type="button" class="map-consent" onclick="ckAccepterKort()">
      <strong>Vis kort</strong><span>Kortet hentes fra Google Maps, som sætter cookies. Klikker du her, accepterer du det, og kortet vises med det samme.</span></button></div>
  </div>
  <div>
    <form class="kf" id="kf" action="{action}" method="POST">
      <h2>Send en henvendelse</h2>
      <p class="sub">Jo mere du fortæller, jo bedre kan vi give et retvisende tilbud.</p>
      <div class="f-row">
        <div class="f-g"><label for="navn">Navn</label><input id="navn" name="Navn" required autocomplete="name"></div>
        <div class="f-g"><label for="tlf">Telefon</label><input id="tlf" name="Telefon" type="tel" required autocomplete="tel"></div>
      </div>
      <div class="f-g"><label for="mail">E-mail</label><input id="mail" name="_replyto" type="email" required autocomplete="email"></div>
      <div class="f-row">
        <div class="f-g"><label for="type">Type opgave <span>(valgfrit)</span></label><select id="type" name="Type opgave"><option value="">Vælg</option>{valg}</select></div>
        <div class="f-g"><label for="adr">Adresse på opgaven <span>(valgfrit)</span></label><input id="adr" name="Adresse" autocomplete="street-address"></div>
      </div>
      <div class="f-g"><label for="besk">Beskriv opgaven</label><textarea id="besk" name="Beskrivelse" required></textarea></div>
      <p class="f-note">Har du billeder af opgaven? Send dem gerne til <a href="mailto:{MAIL}">{MAIL}</a> efter du har sendt formularen.</p>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary" type="submit">Send henvendelse</button>
    </form>
    <div class="kvit" id="kvit" role="status"><h2>Tak for din henvendelse</h2><p>Vi har modtaget den og vender tilbage inden for 24 timer på hverdage. Haster det, så ring på <a href="tel:{TLF_RAW}">{TLF}</a>.</p></div>
  </div>
</div></section>"""
FORM_JS = """<script>(function(){var f=document.getElementById('kf'),k=document.getElementById('kvit');
f.addEventListener('submit',function(ev){ev.preventDefault();var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent='Sender...';
function ok(){f.style.display='none';k.classList.add('vis');if(typeof gtag==='function'){gtag('event','generate_lead',{'currency':'DKK','value':%(v)s});}}
if(f.getAttribute('action')==='#'){ok();return;}
fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){if(r.ok){ok();}else{throw 0;}})
.catch(function(){b.disabled=false;b.textContent='Send henvendelse';alert('Formularen kunne ikke sendes. Ring på 50 70 05 05 eller skriv til info@rosendal-tomrer.dk.');});});})();</script>""" % {"v": "0"}
side("kontakt", "Kontakt Rosendal Tømrer · Ring 50 70 05 05",
     "Ring på 50 70 05 05 eller send en henvendelse. Vi vender tilbage inden for 24 timer på hverdage. Engdraget 11, 3390 Hundested.",
     kontakt, extra_js=FORM_JS, schemas=[schema_virksomhed()])

# ---------------- COOKIES ----------------
cookies = f"""
<section class="page-header"><div class="container"><div class="crumb"><a href="index.html">Forside</a> / Cookiepolitik</div>
<h1>Cookiepolitik</h1><p>Her kan du se hvilke cookies vi bruger, og hvordan du ændrer dit valg.</p></div></section>
<section class="sec"><div class="container narrow prose">
  <h2>Hvad er cookies?</h2><p>En cookie er en lille tekstfil, som gemmes i din browser. Vi sætter kun cookies, der ikke er nødvendige, hvis du har sagt ja.</p>
  <h2>Nødvendige cookies</h2><p><strong>{COOKIE}</strong> gemmer dit valg i cookiebanneret i 12 måneder. Den er nødvendig for at vi kan huske dit svar.</p>
  <h2>Statistik og marketing</h2><p>Hvis du accepterer, bruger vi Google Analytics til at se hvordan siden bliver brugt, og Google Ads til at måle effekten af vores annoncering. Afviser du, sendes der kun anonyme signaler uden cookies.</p>
  <h2>Google Maps</h2><p>Kortet på kontaktsiden hentes fra Google og sætter cookies. Det vises derfor først, når du har accepteret.</p>
  <h2>Skift dit valg</h2><p>Du kan altid ændre eller trække dit samtykke tilbage via linket "Skift cookieindstillinger" nederst på alle sider.</p>
  <h2>Ansvarlig</h2><p>{e(NAVN)}, {ADR}, {POST} {BY}. CVR {CVR}. <a href="mailto:{MAIL}">{MAIL}</a></p>
</div></section>"""
side("cookies", "Cookiepolitik · Rosendal Tømrer",
     "Sådan bruger rosendal-tomrer.dk cookies, og hvordan du ændrer eller trækker dit samtykke tilbage.", cookies)

# ---------------- 404 ----------------
f404 = f"""<section class="page-header"><div class="container"><h1>Siden findes ikke</h1>
<p>Adressen er måske ændret, da vi fik ny hjemmeside. Gå til forsiden, eller ring hvis du leder efter noget bestemt.</p>
<div class="btn-row"><a class="btn btn-brass" href="index.html">Til forsiden</a><a class="btn btn-ghost" href="tel:{TLF_RAW}">Ring {TLF}</a></div></div></section>
<section class="sec"><div class="container">{svc_grid()}</div></section>"""
skriv("404.html", build_page("404", "Siden findes ikke · Rosendal Tømrer",
      "Siden findes ikke. Gå til forsiden eller ring på 50 70 05 05.", f404, noindex=True)
      .replace('href="', 'href="/').replace('href="/http', 'href="http').replace('href="/tel:', 'href="tel:')
      .replace('href="/mailto:', 'href="mailto:').replace('href="/#', 'href="#')
      .replace('src="images/', 'src="/images/').replace('url(images/', 'url(/images/'))

# ---------------- REDIRECT-STUBS for gamle WordPress-URL'er ----------------
GAMLE = {"doere-vinduer": "doere-og-vinduer.html", "terrasse": "terrasse.html", "gaardhaver": "gaardhaver.html",
         "nybyg": "nybyg.html", "tag": "tag.html", "renovering": "renovering.html",
         "materieludlejning": "materieludlejning.html", "job": "job.html", "kontakt": "kontakt.html"}
for gammel, ny in GAMLE.items():
    skriv(f"{gammel}/index.html", f"""<!DOCTYPE html><html lang="da"><head><meta charset="UTF-8">
<title>Siden er flyttet</title><link rel="canonical" href="{DOMAIN}/{ny}"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=../{ny}"></head><body><p>Siden er flyttet til <a href="../{ny}">{ny}</a>.</p></body></html>
""")

# ---------------- ROBOTS, SITEMAP, LLMS ----------------
bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Google-Extended", "ClaudeBot", "Claude-SearchBot", "Applebot-Extended"]
skriv("robots.txt", "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {DOMAIN}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{DOMAIN}/{'' if s == 'index' else s + '.html'}</loc></url>\n" for s in SIDER)
skriv("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
ylist = "\n".join(f"- [{n}]({DOMAIN}/{s}.html)" for s, n in YDELSER)
skriv("llms.txt", f"""# {NAVN}

> Tømrerfirma i Hundested, stiftet 2021 af tømrermester og bygningskonstruktør Sebastian Norborg Rosendal. Fag- og hovedentrepriser for private og erhverv i Nordsjælland: nybyg, tilbygning, tag, døre og vinduer, terrasser, gårdhaver og renovering.

- Telefon: {TLF}
- E-mail: {MAIL}
- Adresse: {ADR}, {POST} {BY}
- CVR: {CVR}
- Anmeldelser: {ANM_SNIT} ud af 5 baseret på {ANM_ANTAL} verificerede anmeldelser ({ANM_URL})
- Serviceområde: Nordsjælland, især Halsnæs, Frederiksværk, Frederikssund, Hillerød og Gribskov

## Ydelser
{ylist}

## Andet
- [Referencer]({DOMAIN}/referencer.html)
- [Kontakt]({DOMAIN}/kontakt.html)
""")
skriv(".nojekyll", "")
print("Bygget:", len(SIDER), "sider +404 +", len(GAMLE), "redirect-stubs")
