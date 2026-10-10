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

def rev_en(key):
    t, q, n, by, d, k, _ = A[key]
    return (f'<figure class="rev-one"><blockquote>"{e(q)}"</blockquote>'
            f'<figcaption class="who">{stj(k)} {e(n)}, {e(by)} · Verificeret anmeldelse på '
            f'<a href="{ANM_URL}" target="_blank" rel="noopener" style="text-decoration:underline">Anmeld Håndværker</a></figcaption></figure>')

KORT_TXT = {
    "doere-og-vinduer": "Vinduer, hoveddøre, terrassedøre, foldedøre og franske altaner.",
    "terrasse": "Træterrasser, repos og trappetrin, gerne i ipé.",
    "gaardhaver": "Pergolaer, cykelskure, platforme, bænke og hegn til private og erhverv.",
    "nybyg": "Tilbygninger, gæstehuse, carporte, garager og nye huse.",
    "tag": "Nyt tag, tegltag, tagrenovering og efterisolering.",
    "renovering": "Vægge, gulve, lofter, facader og sommerhuse.",
}
OGSAA = ["carporte og garager", "udestuer og vinterhaver", "trapper", "spær", "skillevægge", "loftsbeklædning",
         "facadebeklædning", "foldedøre", "forsatsvinduer", "køkkener og garderobeskabe", "bygningsvedligeholdelse"]

def svc_grid():
    out = ['<div class="svc-grid">',
           f'<a class="svc svc-feature" href="hovedentreprise.html">{HEX}<h3>Hoved- og fagentreprise</h3>'
           '<p>Vi styrer hele byggeriet og koordinerer murer, elektriker, VVS og maler. Én kontrakt, én kontakt og ét ansvar fra start til aflevering.</p>'
           '<span class="svc-go">Sådan foregår det</span></a>']
    for s, n in YDELSER:
        if s in KORT_TXT:
            out.append(f'<a class="svc" href="{s}.html">{HEX}<h3>{e(n)}</h3><p>{KORT_TXT[s]}</p><span class="svc-go">Læs mere</span></a>')
    out.append("</div>")
    out.append(f'<p class="svc-more">Vi laver også {", ".join(OGSAA[:-1])} og {OGSAA[-1]}. Vi lejer desuden stillads og trailer ud. <a href="materieludlejning.html">Se materieludlejning</a></p>')
    return "\n".join(out)

TRUST = f"""<div class="container trust">
  <div><strong>Tømrermester</strong><span>og uddannet bygningskonstruktør</span></div>
  <div><strong>{ANM_SNIT} ud af 5</strong><span>{ANM_ANTAL} verificerede anmeldelser</span></div>
  <div><strong>Byggaranti</strong><span>Medlem af Dansk Håndværk</span></div>
  <div><strong>Hele {OMRAADE.split(" og ")[0]}</strong><span>og Hovedstadsområdet, fra base i Hundested</span></div>
</div>"""

SIGNATUR = """<div class="sign"><img src="images/signatur.png" alt="Sebastian Rosendals underskrift" width="172" height="176" loading="lazy">
  <div><strong>Sebastian Rosendal</strong><span>Indehaver, tømrermester og bygningskonstruktør</span></div></div>"""

# ---------------- FORSIDE ----------------
forside = f"""
<section class="hero">
  <div class="hero-text"><div class="hero-inner">
    <div class="hero-kicker">Tømrermester og bygningskonstruktør</div>
    <h1>Tømrer i Hundested for hele Nordsjælland og Hovedstadsområdet</h1>
    <p class="lead">Vi tager store som små opgaver for private og erhverv: døre og vinduer, terrasser, tag, nybyg og renovering. Et fast hold af tømrere, én kontakt og aftaler der bliver holdt.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a>
      <a class="btn btn-ghost" href="kontakt.html">Få et tilbud</a>
    </div>
    <div class="hero-proof"><strong>{ANM_SNIT}</strong><div>{STJ}<br>{ANM_ANTAL} anmeldelser på Anmeld Håndværker</div></div>
  </div></div>
  <div class="hero-img"><img src="images/bro-ipe.webp" srcset="images/bro-ipe-720.webp 720w, images/bro-ipe.webp 1081w" sizes="(max-width:820px) 100vw, 55vw"
    alt="Terrasse i ipé langs vandet med trappe op ad skrænten, bygget af Rosendal Tømrer" width="1081" height="804" fetchpriority="high"></div>
</section>

<section class="sec-mist">{TRUST}</section>

<section class="sec" id="om"><div class="container about">
  <div class="prose">
    <h2>Et tømrerfirma der tager hele opgaven</h2>
    <p>Rosendal Tømrer Entreprise blev stiftet i 2021 af Sebastian Rosendal, der er tømrermester og uddannet bygningskonstruktør. I dag er vi et fast hold af tømrere med base på Engdraget i Hundested, og vi dækker hele Nordsjælland og Hovedstadsområdet.</p>
    <p>Vi tager imod store som små opgaver, fra en enkelt ny terrassedør til tilbygninger og totalrenoveringer, hvor vi står for hele byggeriet og koordinerer de andre fag. Finder du ikke lige den opgave du står med her på siden, er du stadig meget velkommen til at ringe.</p>
    <p>Vi giver selvfølgelig byggaranti. Det er din tryghed for, at kvaliteten er i orden.</p>
    {SIGNATUR}
  </div>
  <ul class="principles">
    <li><strong>Én kontakt hele vejen</strong><span>Sebastian er altid til at få fat på, fra første besøg til aflevering.</span></li>
    <li><strong>Aftaler der holder</strong><span>Pris, tidsplan og omfang står i tilbuddet. Opstår der noget undervejs, hører du det før vi går videre.</span></li>
    <li><strong>Byggeteknisk overblik</strong><span>Som bygningskonstruktør kan Sebastian hjælpe med planlægning og tegninger, før der skal bygges.</span></li>
    <li><strong>Ryddet op hver dag</strong><span>Vi arbejder i dit hjem og opfører os derefter.</span></li>
  </ul>
</div></section>

<section class="sec sec-mist"><div class="container">
  <div class="sec-head"><h2>Det laver vi</h2><p>Fra små opgaver til hele byggerier, for private og erhverv. Vælg en ydelse og læs mere om hvordan vi griber den an.</p></div>
  {svc_grid()}
</div></section>

<section class="sec"><div class="container">
  <div class="rev-top">
    <div class="sec-head" style="margin:0"><h2>Det siger kunderne</h2><p>Udvalgte, verificerede anmeldelser fra Anmeld Håndværker.</p></div>
    <div class="rev-score"><span class="big">{ANM_SNIT}</span><span class="meta">{STJ}<br>ud af 5 baseret på {ANM_ANTAL} anmeldelser</span></div>
  </div>
  <div class="rev-grid">{rev_kort('brian')}{rev_kort('bitten')}{rev_kort('morten')}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Læs alle {ANM_ANTAL} anmeldelser her på Anmeldhåndværker.dk</a></div>
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
side("index", "Tømrer i Hundested · Nordsjælland og Hovedstaden",
     "Tømrermester og bygningskonstruktør i Hundested. Døre og vinduer, terrasser, tag, nybyg og renovering i Nordsjælland og København. 4,9 ud af 5.",
     forside, schemas=[schema_virksomhed()])

# ---------------- YDELSESSIDER ----------------
def sidebar(aktiv):
    li = "".join(f'<li><a href="{s}.html"{" class=\"active\"" if s == aktiv else ""}>{e(n)}</a></li>' for s, n in YDELSER)
    return (f'<aside class="side"><ul class="side-nav">{li}</ul>'
            f'<div class="side-cta"><h2>Kontakt os i dag</h2><p>Tømrerarbejde i Hundested. Vi dækker hele {OMRAADE}.</p>'
            f'<a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}{TLF}</a><a class="side-link" href="kontakt.html">Skriv til os</a></div></aside>')

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
    if d.get("billede"):
        src, alt = d["billede"]
        blokke.insert(1, f'<figure class="svc-fig"><img src="{src}" alt="{e(alt)}" loading="lazy"></figure>')
    gal = ""
    if d.get("galleri"):
        gal = '<div class="svc-gal">' + "".join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy" data-lb></figure>' for s, a in d["galleri"]) + "</div>"
    anm = rev_en(d["anm"]) if d["anm"] else ""
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in d["faq"])
    body = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Hjem</a> › {e(navn)}</div>
  <h1>{e(d['h1'])}</h1><p>{e(d['intro'])}</p>
  <div class="btn-row"><a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a><a class="btn btn-ghost" href="kontakt.html">Få et tilbud</a></div>
</div></section>
<section class="sec"><div class="container svc-layout">
  {sidebar(slug)}
  <div class="prose svc-main">{''.join(blokke)}{gal}{anm}
    <h2>Ofte stillede spørgsmål</h2><div class="faq">{faq}</div>
  </div>
</div></section>
{cta()}"""
    side(slug, d["title"], d["desc"], body, active=slug, schemas=[schema_virksomhed(), faq_schema(d["faq"])],
         extra_js=LB_JS if d.get("galleri") else "")

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

def case(key):
    t, q, n, by, d, k, typ = A[key]
    return (f'<article class="case"><div class="case-top"><div class="case-type">{e(typ)}</div><h3>{e(t)}</h3></div>'
            f'<div class="case-body"><div>{stj(k)}</div><blockquote>{e(q)}</blockquote>'
            f'<div class="who"><strong>{e(n)}</strong>, {e(by)} · {e(d)}</div></div></article>')

proj_html = ""
if LIVE:
    kort = "".join(f'<a class="ref-card" href="projekt-{p["slug"]}.html"><div class="ref-card-media"><img src="{p["billeder"][0][0]}" alt="{e(p["billeder"][0][1])}" loading="lazy"></div>'
                   f'<div class="ref-card-body"><h3>{e(p["titel"])}</h3><p>{e(p["by"])}</p></div></a>' for p in LIVE)
    proj_html = f'<section class="sec"><div class="container"><div class="sec-head"><h2>Projekter</h2></div><div class="refs-grid">{kort}</div></div></section>'

ref_body = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Hjem</a> › Referencer</div>
  <h1>Referencer og anmeldelser</h1>
  <p>Opgaver vi har løst i Nordsjælland og Hovedstadsområdet, fortalt med kundernes egne ord. Her er de {len(A)} nyeste af {ANM_ANTAL} anmeldelser på Anmeld Håndværker.</p>
</div></section>
{proj_html}
<section class="sec sec-mist"><div class="container">
  <div class="rev-top">
    <div class="sec-head" style="margin:0"><h2>{ANM_ANTAL} anmeldelser, {ANM_SNIT} i snit</h2><p>Kommunikation, aftaler, pris, tilfredshed og oprydning.</p></div>
  </div>
  <div class="refs-grid">{''.join(case(k) for k in A)}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Læs alle anmeldelser på Anmeld Håndværker</a><a href="{FB_ANM}" target="_blank" rel="noopener">Anmeldelser på Facebook</a></div>
</div></section>
{some()}
{cta()}"""
side("referencer", "Referencer og anmeldelser · Rosendal Tømrer",
     "38 verificerede anmeldelser med et snit på 4,9 ud af 5. Tag, vinduer, terrasser, tilbygning og renovering i Nordsjælland og Hovedstadsområdet.",
     ref_body, schemas=[schema_virksomhed()])



for p in LIVE:
    imgs = "".join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy" data-lb></figure>' for s, a in p["billeder"])
    side(f"projekt-{p['slug']}", f"{p['titel']} · Rosendal Tømrer", p.get("desc", p["titel"]),
         f'<section class="page-header"><div class="container"><div class="crumb"><a href="referencer.html">Referencer</a></div><h1>{e(p["titel"])}</h1><p>{e(p["by"])}</p></div></section>'
         f'<section class="sec"><div class="container"><div class="proj-gallery">{imgs}</div></div></section>{cta()}',
         active="referencer", extra_js=LB_JS)

# ---------------- JOB ----------------
FORM_ACTION = f"https://formspree.io/f/{FORMSPREE_ID}" if FORMSPREE_ID else "#"
FORM_JS = """<script>(function(){var f=document.getElementById('kf'),k=document.getElementById('kvit');
f.addEventListener('submit',function(ev){ev.preventDefault();var b=f.querySelector('button[type=submit]');b.disabled=true;b.textContent='Sender...';
function ok(){f.style.display='none';k.classList.add('vis');if(f.hasAttribute('data-lead')&&typeof gtag==='function'){gtag('event','generate_lead',{'currency':'DKK','value':%(v)s});}}
if(f.getAttribute('action')==='#'){ok();return;}
fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){if(r.ok){ok();}else{throw 0;}})
.catch(function(){b.disabled=false;b.textContent='Send henvendelse';alert('Formularen kunne ikke sendes. Ring på 50 70 05 05 eller skriv til info@rosendal-tomrer.dk.');});});})();</script>""" % {"v": "0"}

job = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Hjem</a> › Job</div>
  <h1>Er du vores nye tømrer?</h1>
  <p>Vi søger løbende tømrersvende til holdet. Også selvom der ikke ligger et opslag ude.</p>
</div></section>
<section class="sec"><div class="container contact-grid">
  <div class="prose">
    <img class="job-img" src="images/jobbil.webp" alt="Rosendal Tømrers firmabil ved værkstedet med en kasse i træ" width="587" height="585" loading="lazy">
    <h2>Hvem er vi?</h2>
    <p>Hos Rosendal Tømrer Entreprise er vi kvalitetsbevidste og stolte af vores faglige kunnen. Vi går på arbejde med glæde, fordi vi laver det vi brænder for, og vi lægger vægt på et kammeratligt og tæt sammenhold.</p>
    <p>Vi laver alle former for tømreropgaver, fordi vi kan lide at to dage ikke er ens: tag, døre og vinduer, terrasser, hegn, skure, gårdmiljøer, nybyg og renovering. Alt udføres ud fra kundens ønsker, så det er vigtigt at du er god til at tale med kunderne fra start til slut.</p>
    <h2>Fortæl os gerne</h2>
    <ul><li>Kort hvem du er</li><li>Din erfaring og tidligere arbejde</li><li>Hvorfor du elsker tømrerfaget</li><li>Hvorfor du er vores nye kollega</li></ul>
    <p>Du kan også bare ringe til Sebastian på <a href="tel:{TLF_RAW}">{TLF}</a>.</p>
  </div>
  <div>
    <form class="kf" id="kf" action="{FORM_ACTION}" method="POST">
      <h2>Søg job hos Danmarks fedeste tømrerfirma</h2>
      <p class="sub">Måske er det dig vi lige står og mangler? Send en besked, så vender vi tilbage til dig.</p>
      <input type="hidden" name="_subject" value="Jobansøgning via hjemmesiden">
      <div class="f-g"><label for="navn">Navn</label><input id="navn" name="Navn" required autocomplete="name"></div>
      <div class="f-row">
        <div class="f-g"><label for="mail">E-mail</label><input id="mail" name="_replyto" type="email" required autocomplete="email"></div>
        <div class="f-g"><label for="tlf">Telefon</label><input id="tlf" name="Telefon" type="tel" required autocomplete="tel"></div>
      </div>
      <div class="f-g"><label for="besk">Besked</label><textarea id="besk" name="Besked" required></textarea></div>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary" type="submit">Send ansøgning</button>
    </form>
    <div class="kvit" id="kvit" role="status"><h2>Tak for din ansøgning</h2><p>Vi har modtaget den og vender tilbage hurtigst muligt.</p></div>
  </div>
</div></section>
{cta("Spørgsmål om job?", "Ring til Sebastian og tag en uforpligtende snak.")}"""
side("job", "Job som tømrer i Nordsjælland · Rosendal Tømrer",
     "Vi søger løbende tømrersvende til holdet i Hundested. Send en ansøgning via formularen eller ring til Sebastian på 50 70 05 05.", job,
     extra_js=FORM_JS)

# ---------------- KONTAKT ----------------
valg = "".join(f"<option>{e(n)}</option>" for _, n in YDELSER) + "<option>Andet</option>"
kontakt = f"""
<section class="page-header"><div class="container">
  <div class="crumb"><a href="index.html">Hjem</a> › Kontakt</div>
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
    <form class="kf" id="kf" action="{FORM_ACTION}" method="POST" data-lead>
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

side("kontakt", "Kontakt Rosendal Tømrer · Ring 50 70 05 05",
     "Ring på 50 70 05 05 eller send en henvendelse. Vi vender tilbage inden for 24 timer på hverdage. Engdraget 11, 3390 Hundested.",
     kontakt, extra_js=FORM_JS, schemas=[schema_virksomhed()])

# ---------------- COOKIES ----------------
cookies = f"""
<section class="page-header"><div class="container"><div class="crumb"><a href="index.html">Hjem</a> › Cookiepolitik</div>
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

> Tømrerfirma i Hundested, stiftet 2021 af tømrermester og bygningskonstruktør Sebastian Norborg Rosendal. Fag- og hovedentrepriser for private og erhverv i Nordsjælland og Hovedstadsområdet: døre og vinduer, terrasser, gårdhaver og gårdmiljøer, nybyg, tag og renovering.

- Telefon: {TLF}
- E-mail: {MAIL}
- Adresse: {ADR}, {POST} {BY}
- CVR: {CVR}
- Anmeldelser: {ANM_SNIT} ud af 5 baseret på {ANM_ANTAL} verificerede anmeldelser ({ANM_URL})
- Åbningstid: {AABNING}
- Serviceområde: hele {OMRAADE}, med base i Hundested

## Ydelser
{ylist}

## Andet
- [Referencer]({DOMAIN}/referencer.html)
- [Kontakt]({DOMAIN}/kontakt.html)
""")
skriv(".nojekyll", "")
print("Bygget:", len(SIDER), "sider +404 +", len(GAMLE), "redirect-stubs")
