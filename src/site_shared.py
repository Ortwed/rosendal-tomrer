"""Faelles skabelon for rosendal-tomrer.dk. Alt HTML bygges herfra."""
import json, os, html

DOMAIN = "https://rosendal-tomrer.dk"
NAVN = "Rosendal Tømrer Entreprise ApS"
KORT = "Rosendal Tømrer"
TLF = "50 70 05 05"
TLF_RAW = "+4550700505"
MAIL = "info@rosendal-tomrer.dk"
ADR = "Engdraget 11"
POST = "3390"
BY = "Hundested"
CVR = "42228672"
FB = "https://www.facebook.com/profile.php?id=100068776222589"
FB_ANM = "https://www.facebook.com/profile.php?id=100068776222589&sk=reviews"
IG = "https://www.instagram.com/rosendaltomrerentrepriseaps/"
ANM_URL = "https://www.anmeld-haandvaerker.dk/tomrer/rosendal-tomrer-entreprise-aps"
ANM_ANTAL = 37
ANM_SNIT = "4,9"
GA_ID = None          # fx "G-XXXXXXX". None = ingen gtag.js (demo)
FORMSPREE_ID = None   # fx "mabcdxyz". None = demo-tilstand, intet sendes
COOKIE = "rosendal_samtykke"
DEMO = True          # True = noindex paa alle sider (demo paa GitHub Pages). Saet False ved go-live

YDELSER = [  # (slug, navigationsnavn)
    ("hovedentreprise", "Hoved- og fagentreprise"),
    ("nybyg", "Nybyg og tilbygning"),
    ("tag", "Tag"),
    ("doere-og-vinduer", "Døre og vinduer"),
    ("terrasse", "Terrasser"),
    ("gaardhaver", "Gårdhaver og udestuer"),
    ("renovering", "Renovering"),
    ("materieludlejning", "Materieludlejning"),
]

def e(s):
    return html.escape(s, quote=True)

CSS = r"""
:root{
  --navy:#0E2A44; --blue:#1D3D73; --blue-mid:#2C5294; --brass:#B87F35; --brass-dk:#94641F;
  --sand:#F7F4EE; --mist:#EEF1F5; --line:#DFE3E9; --ink:#16202B; --muted:#55606D; --white:#fff;
  --head:'Archivo',system-ui,sans-serif; --body:'Manrope',system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
:root{padding-top:env(safe-area-inset-top,0px)}
html{scroll-behavior:smooth;scroll-padding-top:90px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
body{font-family:var(--body);color:var(--ink);background:var(--white);line-height:1.65;font-size:1.02rem;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
:focus-visible{outline:3px solid var(--brass);outline-offset:3px}
h1,h2,h3,h4{font-family:var(--head);font-stretch:92%;font-weight:700;line-height:1.15;letter-spacing:-.015em;color:var(--navy)}
.container{max-width:1200px;margin:0 auto;padding:0 1.5rem}
.narrow{max-width:780px}

/* HEADER */
header{background:var(--white);position:sticky;top:0;z-index:100;border-bottom:1px solid var(--line)}
.header-inner{max-width:1200px;margin:0 auto;padding:.9rem 1.5rem;display:flex;align-items:center;gap:1.6rem}
.logo img{height:52px;width:auto}
nav{margin-left:auto}
nav ul{display:flex;gap:1.8rem;list-style:none;align-items:center}
nav a{font-size:.95rem;font-weight:600;padding:.3rem 0;position:relative}
nav a:hover,nav a.active{color:var(--blue)}
nav a.active::after{content:'';position:absolute;left:0;right:0;bottom:-3px;height:2px;background:var(--brass)}
.nav-dd{position:relative;padding-bottom:1rem;margin-bottom:-1rem}
.nav-dd>button{font:inherit;font-size:.95rem;font-weight:600;background:none;border:0;cursor:pointer;color:inherit;padding:.3rem 0}
.nav-dd>button.active{color:var(--blue)}
.nav-sub{display:none;position:absolute;top:100%;left:-1rem;background:#fff;min-width:250px;padding:.5rem 0;border:1px solid var(--line);border-top:3px solid var(--blue);box-shadow:0 12px 28px rgba(14,42,68,.12)}
.nav-dd:hover .nav-sub,.nav-dd:focus-within .nav-sub{display:block}
.nav-sub a{display:block;padding:.6rem 1.2rem;font-size:.92rem;white-space:nowrap}
.nav-sub a:hover,.nav-sub a.active{background:var(--mist)}
.nav-sub a.active::after{display:none}
.social{display:flex;gap:.5rem}
.social a{width:34px;height:34px;display:grid;place-items:center;border:1px solid var(--line);border-radius:50%;color:var(--blue)}
.social a:hover{background:var(--blue);color:#fff;border-color:var(--blue)}
.social svg{width:16px;height:16px;fill:currentColor}
.hdr-tlf{display:inline-flex;align-items:center;gap:.5rem;background:var(--blue);color:#fff;font-family:var(--head);font-weight:700;padding:.65rem 1.1rem;border-radius:3px;white-space:nowrap}
.hdr-tlf:hover{background:var(--navy)}
.hdr-tlf svg{width:16px;height:16px;fill:currentColor}
.menu-toggle{display:none;background:none;border:0;font-size:1.7rem;cursor:pointer;color:var(--navy);padding:.2rem .4rem}

/* KNAPPER */
.btn{display:inline-flex;align-items:center;gap:.55rem;font-family:var(--head);font-weight:700;font-size:1rem;padding:.95rem 1.6rem;border-radius:3px;border:2px solid var(--blue);transition:background .2s,color .2s}
.btn svg{width:18px;height:18px;fill:currentColor}
.btn-primary{background:var(--blue);color:#fff}
.btn-primary:hover{background:var(--navy);border-color:var(--navy)}
.btn-ghost{background:transparent;color:var(--blue)}
.btn-ghost:hover{background:var(--blue);color:#fff}
.btn-brass{background:var(--brass);border-color:var(--brass);color:#fff}
.btn-brass:hover{background:var(--brass-dk);border-color:var(--brass-dk)}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem}

/* HERO (forside) */
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.08fr);min-height:600px;background:var(--white)}
.hero-text{display:flex;align-items:center;padding:4rem 3rem 4rem max(1.5rem,calc((100vw - 1200px)/2 + 1.5rem))}
.hero-inner{max-width:560px}
.hero-kicker{display:flex;align-items:center;gap:.7rem;font-weight:700;color:var(--brass-dk);margin-bottom:1.2rem;font-size:.98rem}
.hero-kicker::before{content:'';width:3px;height:1.4em;background:var(--brass)}
.hero h1{font-size:clamp(2rem,3.5vw,3.05rem);margin-bottom:1.2rem;font-stretch:88%}
.hero p.lead{font-size:1.12rem;color:var(--muted);margin-bottom:2rem;max-width:34em}
.hero-proof{display:flex;align-items:center;gap:.8rem;margin-top:2rem;padding-top:1.4rem;border-top:1px solid var(--line);font-size:.92rem;color:var(--muted)}
.hero-proof strong{font-family:var(--head);font-size:1.5rem;color:var(--navy)}
.stars{color:var(--brass);letter-spacing:.1em;font-size:1rem}
.hero-img{position:relative;overflow:hidden;background:var(--navy)}
.hero-img img{width:100%;height:100%;object-fit:cover;object-position:68% 60%;clip-path:polygon(14% 0,100% 0,100% 100%,0 100%)}
.hero-img::before{content:'';position:absolute;inset:0;background:var(--brass);clip-path:polygon(12.6% 0,14% 0,0 100%,-1.4% 100%);z-index:1}

/* SIDEHOVED (undersider) */
.page-header{background:var(--navy);color:#fff;padding:4.2rem 0 3.6rem;position:relative;overflow:hidden}
.page-header::after{content:'';position:absolute;right:-60px;top:-40px;width:340px;height:390px;background:url(images/hex-hvid.svg) no-repeat center/contain;opacity:.07}
.page-header .crumb{font-size:.9rem;color:rgba(255,255,255,.7);margin-bottom:.9rem}
.page-header .crumb a{text-decoration:underline;text-underline-offset:3px}
.page-header h1{color:#fff;font-size:clamp(2rem,4vw,3rem);margin-bottom:1rem;max-width:20ch}
.page-header p{max-width:620px;color:rgba(255,255,255,.86);font-size:1.1rem}
.page-header .btn-row{margin-top:1.8rem}
.page-header .btn-ghost{color:#fff;border-color:rgba(255,255,255,.6)}
.page-header .btn-ghost:hover{background:#fff;color:var(--navy)}

/* SEKTIONER */
.sec{padding:5rem 0}
.sec-mist{background:var(--mist)}
.sec-sand{background:var(--sand)}
.sec-head{margin-bottom:2.6rem;max-width:680px}
.sec-head h2{font-size:clamp(1.7rem,3vw,2.4rem);margin-bottom:.7rem}
.sec-head p{color:var(--muted);font-size:1.06rem}
.prose h2{font-size:clamp(1.5rem,2.6vw,2rem);margin:2.6rem 0 .9rem}
.prose h2:first-child{margin-top:0}
.prose h3{font-size:1.2rem;margin:1.8rem 0 .6rem}
.prose p{margin-bottom:1.05rem;color:#2C3742}
.prose ul{margin:0 0 1.2rem 1.2rem}
.prose li{margin-bottom:.45rem}
.prose li::marker{color:var(--brass)}
.prose strong{color:var(--navy)}

/* OM-OS (forside) */
.about{display:grid;grid-template-columns:1.1fr .9fr;gap:4rem;align-items:start}
.principles{list-style:none;border-left:3px solid var(--blue);padding-left:1.6rem}
.principles li{margin-bottom:1.6rem}
.principles strong{display:block;font-family:var(--head);font-size:1.12rem;color:var(--navy);margin-bottom:.2rem}
.principles span{color:var(--muted)}

/* YDELSESKORT */
.svc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}
.svc{background:#fff;padding:1.8rem 1.5rem 1.6rem;display:flex;flex-direction:column;min-height:230px;transition:background .2s}
.svc:hover{background:var(--navy)}
.svc:hover h3,.svc:hover p,.svc:hover .svc-go{color:#fff}
.svc .hex{width:30px;height:34px;margin-bottom:1.2rem;fill:var(--blue)}
.svc:hover .hex{fill:var(--brass)}
.svc h3{font-size:1.18rem;margin-bottom:.5rem}
.svc p{font-size:.93rem;color:var(--muted);margin-bottom:1rem}
.svc-go{margin-top:auto;font-weight:700;font-size:.9rem;color:var(--blue)}
.svc-feature{grid-column:span 2;background:var(--blue)}
.svc-feature h3,.svc-feature p,.svc-feature .svc-go{color:#fff}
.svc-feature p{color:rgba(255,255,255,.85);font-size:1rem;max-width:36em}
.svc-feature .hex{fill:var(--brass)}

/* ANMELDELSER */
.rev-top{display:flex;justify-content:space-between;align-items:end;gap:2rem;flex-wrap:wrap;margin-bottom:2.4rem}
.rev-score{display:flex;align-items:center;gap:1rem}
.rev-score .big{font-family:var(--head);font-size:3.4rem;font-weight:800;color:var(--navy);line-height:1}
.rev-score .meta{font-size:.92rem;color:var(--muted)}
.rev-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.rev{background:#fff;padding:1.7rem;border-top:3px solid var(--brass);display:flex;flex-direction:column}
.rev h3{font-size:1.05rem;margin:.5rem 0 .6rem}
.rev blockquote{color:#2C3742;font-size:.96rem;margin-bottom:1.2rem}
.rev .who{margin-top:auto;font-size:.88rem;color:var(--muted)}
.rev .who strong{color:var(--navy)}
.rev-links{margin-top:2rem;display:flex;gap:1.4rem;flex-wrap:wrap;font-weight:700;color:var(--blue)}
.rev-links a{text-decoration:underline;text-underline-offset:4px}
.rev-one{background:var(--white);border-left:3px solid var(--brass);padding:1.6rem 1.8rem;margin:2.4rem 0 0}
.rev-one blockquote{font-family:var(--head);font-stretch:92%;font-size:1.25rem;line-height:1.4;color:var(--navy);margin-bottom:.8rem}
.rev-one .who{font-size:.9rem;color:var(--muted)}

/* PROCES (er en reel raekkefoelge) */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;counter-reset:s;list-style:none}
.steps li{counter-increment:s;border-top:2px solid var(--blue);padding-top:1.2rem}
.steps li::before{content:counter(s);font-family:var(--head);font-weight:800;font-size:1.6rem;color:var(--brass);display:block;margin-bottom:.4rem}
.steps strong{display:block;font-family:var(--head);color:var(--navy);font-size:1.1rem;margin-bottom:.3rem}
.steps span{color:var(--muted);font-size:.95rem}

/* GARANTI-BAAND */
.trust{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;padding-top:2.2rem;padding-bottom:2.2rem}
.trust div{border-left:3px solid var(--brass);padding-left:1rem}
.trust strong{display:block;font-family:var(--head);color:var(--navy);font-size:1.02rem}
.trust span{font-size:.9rem;color:var(--muted)}

/* SPLIT MED BILLEDE */
.split{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:center}
.split img{width:100%;height:auto;border-radius:2px}

/* FAQ */
.faq details{border-bottom:1px solid var(--line)}
.faq details:first-of-type{border-top:1px solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:1.2rem 2.5rem 1.2rem 0;font-family:var(--head);font-weight:700;font-size:1.08rem;color:var(--navy);position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:'+';position:absolute;right:.3rem;top:1rem;font-size:1.5rem;color:var(--brass);font-weight:400}
.faq details[open] summary::after{content:'–'}
.faq details p{padding:0 0 1.3rem;color:#2C3742;max-width:68ch}

/* REFERENCER */
.refs-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.case{background:#fff;border:1px solid var(--line);display:flex;flex-direction:column}
.case-top{background:var(--navy);color:#fff;padding:1.3rem 1.5rem 1.2rem;position:relative;overflow:hidden}
.case-top::after{content:'';position:absolute;right:-18px;bottom:-26px;width:90px;height:104px;background:url(images/hex-hvid.svg) no-repeat center/contain;opacity:.12}
.case-type{font-size:.85rem;color:rgba(255,255,255,.72);margin-bottom:.3rem}
.case-top h3{color:#fff;font-size:1.2rem}
.case-body{padding:1.4rem 1.5rem 1.6rem;display:flex;flex-direction:column;flex:1}
.case-body blockquote{color:#2C3742;font-size:.96rem;margin-bottom:1rem}
.case-body .who{margin-top:auto;font-size:.88rem;color:var(--muted)}
.case-body .who strong{color:var(--navy)}
.ref-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line)}
.ref-card-media{aspect-ratio:4/3;overflow:hidden;background:var(--mist)}
.ref-card-media img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.ref-card:hover .ref-card-media img{transform:scale(1.04)}
.ref-card-body{padding:1.3rem 1.4rem 1.5rem}
.ref-card-body h3{font-size:1.15rem;margin-bottom:.4rem}
.ref-card-body p{font-size:.93rem;color:var(--muted)}

/* PROJEKTSIDE */
.proj-gallery{columns:3;column-gap:1rem}
.proj-gallery figure{break-inside:avoid;margin:0 0 1rem}
.proj-gallery img{width:100%;height:auto;cursor:zoom-in}
.lb{position:fixed;inset:0;background:rgba(9,22,36,.95);display:none;align-items:center;justify-content:center;z-index:999;padding:2rem}
.lb.open{display:flex}
.lb img{max-width:100%;max-height:86vh}
.lb button{position:absolute;background:none;border:0;color:#fff;font-size:2.4rem;cursor:pointer;padding:.5rem 1rem}
.lb-close{top:.6rem;right:.8rem}.lb-prev{left:.4rem;top:50%;transform:translateY(-50%)}.lb-next{right:.4rem;top:50%;transform:translateY(-50%)}

/* KONTAKT */
.contact-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:3.5rem;align-items:start}
.c-item{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid var(--line)}
.c-item:first-of-type{border-top:1px solid var(--line)}
.c-label{font-size:.85rem;color:var(--muted)}
.c-value{font-family:var(--head);font-weight:700;color:var(--navy);font-size:1.08rem}
.c-value a{text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--brass)}
.c-big{font-size:1.6rem}
.map-wrap{margin-top:1.6rem;aspect-ratio:4/3;background:var(--mist);border:1px solid var(--line)}
.map-wrap iframe{width:100%;height:100%;border:0}
.map-consent{width:100%;height:100%;background:none;border:0;cursor:pointer;font:inherit;color:var(--muted);padding:1.5rem;display:flex;flex-direction:column;justify-content:center;gap:.4rem}
.map-consent strong{font-family:var(--head);color:var(--blue);font-size:1.05rem}
form.kf{background:var(--mist);padding:2.2rem;border-top:4px solid var(--blue)}
.kf h2{font-size:1.5rem;margin-bottom:.4rem}
.kf .sub{color:var(--muted);margin-bottom:1.6rem;font-size:.95rem}
.f-row{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.f-g{margin-bottom:1rem}
.f-g label{display:block;font-weight:700;font-size:.9rem;margin-bottom:.35rem;color:var(--navy)}
.f-g label span{font-weight:500;color:var(--muted)}
.f-g input,.f-g select,.f-g textarea{width:100%;font:inherit;font-size:1rem;padding:.8rem .9rem;border:1px solid #C9D0D9;background:#fff;border-radius:2px;color:var(--ink)}
.f-g textarea{min-height:140px;resize:vertical}
.f-g input:focus,.f-g select:focus,.f-g textarea:focus{outline:2px solid var(--blue);outline-offset:0;border-color:var(--blue)}
.f-note{font-size:.9rem;color:var(--muted);margin:.4rem 0 1.4rem;padding-left:.9rem;border-left:3px solid var(--brass)}
.kf .btn{border:0;cursor:pointer;width:100%;justify-content:center}
.hp{position:absolute;left:-9999px}
.kvit{display:none;background:#fff;border-left:4px solid var(--brass);padding:1.6rem}
.kvit h2{margin-bottom:.5rem}
.kvit.vis{display:block}

/* CTA */
.cta{background:var(--blue);color:#fff;padding:4.2rem 0}
.cta-inner{display:flex;justify-content:space-between;align-items:center;gap:2rem;flex-wrap:wrap}
.cta h2{color:#fff;font-size:clamp(1.6rem,3vw,2.3rem);margin-bottom:.5rem}
.cta p{color:rgba(255,255,255,.85);max-width:40em}
.cta .btn-ghost{color:#fff;border-color:rgba(255,255,255,.65)}
.cta .btn-ghost:hover{background:#fff;color:var(--blue)}

/* SOME */
.some{padding:2.6rem 0;text-align:center;border-bottom:1px solid var(--line)}
.some p{color:var(--muted);margin-bottom:.8rem}
.some .social{justify-content:center}
.some .social a{width:auto;border-radius:3px;padding:.55rem 1rem;gap:.5rem;display:inline-flex;font-weight:700;font-size:.92rem}

/* FOOTER */
footer{background:var(--navy);color:rgba(255,255,255,.78);padding:4rem 0 2rem;font-size:.94rem}
.f-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:3rem;margin-bottom:2.6rem}
footer img.flogo{height:58px;width:auto;margin-bottom:1.2rem}
footer h3{color:#fff;font-size:1rem;margin-bottom:1rem}
footer ul{list-style:none}
footer li{margin-bottom:.45rem}
footer a:hover{color:#fff;text-decoration:underline}
.f-bottom{border-top:1px solid rgba(255,255,255,.14);padding-top:1.6rem;font-size:.85rem;color:rgba(255,255,255,.6)}
.ck-footerlink{background:none;border:0;font:inherit;color:inherit;cursor:pointer;text-decoration:underline;text-underline-offset:2px}

/* COOKIEBANNER */
.ck-banner{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#fff;border-top:3px solid var(--blue);box-shadow:0 -6px 24px rgba(14,42,68,.14);padding:1.3rem 1.5rem calc(1.3rem + env(safe-area-inset-bottom,0px));display:none}
.ck-banner.vis{display:block}
.ck-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr auto;gap:1.5rem;align-items:center}
.ck-banner h2{font-size:1.05rem;margin-bottom:.3rem}
.ck-banner p{font-size:.88rem;color:var(--muted);max-width:64ch}
.ck-banner p a{color:var(--blue);font-weight:700;text-decoration:underline}
.ck-knapper{display:flex;gap:.7rem}
.ck-knapper button{font:inherit;font-weight:700;font-size:.92rem;padding:.85rem 1.4rem;border-radius:3px;cursor:pointer;border:2px solid var(--blue);min-width:150px}
.ck-afvis{background:#fff;color:var(--blue)}
.ck-accept{background:var(--blue);color:#fff}

/* MOBIL */
@media (max-width:1080px){
  .header-inner{gap:.8rem}
  nav{position:absolute;top:100%;left:0;right:0;background:#fff;border-bottom:1px solid var(--line);display:none;max-height:calc(100vh - 80px);overflow:auto}
  nav.open{display:block}
  nav ul{flex-direction:column;align-items:stretch;gap:0;padding:.5rem 0}
  nav li>a,.nav-dd>button{display:block;padding:.85rem 1.5rem;width:100%;text-align:left}
  nav a.active::after{display:none}
  .nav-dd{padding:0;margin:0}
  .nav-sub{display:block;position:static;border:0;box-shadow:none;padding:0 0 .4rem;min-width:0}
  .nav-sub a{padding:.55rem 2.4rem}
  .social{display:none}
  .hdr-tlf{margin-left:auto}
  .menu-toggle{display:block}
  .svc-grid{grid-template-columns:repeat(2,1fr)}
  .steps,.trust{grid-template-columns:repeat(2,1fr)}
  .rev-grid,.refs-grid{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:820px){
  .hero{grid-template-columns:minmax(0,1fr);min-height:0}
  .hero-text{padding:2rem 1.5rem 2.2rem;order:1}
  .hero-img{order:0;height:200px}
  .hero-img img{clip-path:none;object-position:72% 64%}
  .hero-img::before{display:none}
  .hero h1{font-size:2rem;margin-bottom:.8rem}
  .hero p.lead{font-size:1rem;margin-bottom:1.3rem}
  .hero-kicker{margin-bottom:.7rem;font-size:.9rem}
  .hero-proof{margin-top:1.4rem}
  .about,.split,.contact-grid{grid-template-columns:1fr;gap:2.4rem}
  .f-grid{grid-template-columns:1fr;gap:2rem}
  .proj-gallery{columns:2}
}
@media (max-width:600px){
  .logo img{height:40px}
  .hdr-tlf{padding:.55rem .8rem;font-size:.92rem}
  .sec{padding:3.4rem 0}
  .svc-grid,.rev-grid,.refs-grid,.steps,.trust{grid-template-columns:1fr}
  .svc-feature{grid-column:auto}
  .svc{min-height:0}
  .f-row{grid-template-columns:1fr}
  form.kf{padding:1.5rem}
  .page-header{padding:3rem 0 2.6rem}
  .btn{padding:.85rem 1.2rem}
  .ck-inner{grid-template-columns:1fr;gap:1rem}
  .ck-knapper button{flex:1;min-width:0}
  .proj-gallery{columns:1}
  .hero h1{font-size:1.8rem}
}
@media (max-width:600px){h1,h2,h3{overflow-wrap:break-word}}
.svc-more{margin-top:1.4rem;color:var(--muted)}
.svc-more a{color:var(--blue);font-weight:700;text-decoration:underline;text-underline-offset:3px}
"""

ICON_TLF = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.8c0-.9.3-1.5 1.6-1.5h1.7V3.4c-.3 0-1.3-.1-2.5-.1-2.4 0-4.1 1.5-4.1 4.2v2.3H7.5V13h2.7v8z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3A4.7 4.7 0 1 0 16.7 12 4.7 4.7 0 0 0 12 7.3zm0 7.8a3.1 3.1 0 1 1 3.1-3.1 3.1 3.1 0 0 1-3.1 3.1zm6-8a1.1 1.1 0 1 1-1.1-1.1A1.1 1.1 0 0 1 18 7.1zM21.9 8.2a5.5 5.5 0 0 0-1.5-3.9 5.5 5.5 0 0 0-3.9-1.5C15 2.7 9 2.7 7.5 2.8a5.5 5.5 0 0 0-3.9 1.5 5.5 5.5 0 0 0-1.5 3.9C2 9.7 2 14.3 2.1 15.8a5.5 5.5 0 0 0 1.5 3.9 5.5 5.5 0 0 0 3.9 1.5c1.5.1 7.5.1 9 0a5.5 5.5 0 0 0 3.9-1.5 5.5 5.5 0 0 0 1.5-3.9c.1-1.5.1-6.1 0-7.6zm-2 9.2a3.1 3.1 0 0 1-1.8 1.8c-1.2.5-4.1.4-5.4.4s-4.2.1-5.4-.4a3.1 3.1 0 0 1-1.8-1.8c-.5-1.2-.4-4.1-.4-5.4s-.1-4.2.4-5.4a3.1 3.1 0 0 1 1.8-1.8C8.5 4.3 11.4 4.4 12.7 4.4s4.2-.1 5.4.4a3.1 3.1 0 0 1 1.8 1.8c.5 1.2.4 4.1.4 5.4s.1 4.2-.4 5.4z"/></svg>'
HEX = '<svg class="hex" viewBox="0 0 30 34" aria-hidden="true"><path d="M15 0l15 8.5v17L15 34 0 25.5v-17z"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800'
         '&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">')

def schema_virksomhed():
    return {
        "@context": "https://schema.org", "@type": "GeneralContractor",
        "@id": DOMAIN + "/#virksomhed", "name": NAVN, "alternateName": KORT,
        "url": DOMAIN + "/", "logo": DOMAIN + "/images/logo.png",
        "image": DOMAIN + "/images/og-forside.jpg",
        "telephone": TLF_RAW, "email": MAIL, "vatID": "DK" + CVR, "taxID": CVR,
        "foundingDate": "2021-03", "founder": {"@type": "Person", "name": "Sebastian Norborg Rosendal",
                                               "jobTitle": "Tømrermester og bygningskonstruktør"},
        "address": {"@type": "PostalAddress", "streetAddress": ADR, "postalCode": POST,
                    "addressLocality": BY, "addressRegion": "Hovedstaden", "addressCountry": "DK"},
        "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in
                       ["Nordsjælland", "Halsnæs", "Hundested", "Frederiksværk", "Frederikssund",
                        "Hillerød", "Helsinge", "Gribskov"]],
        "knowsAbout": ["Hovedentreprise", "Fagentreprise", "Nybyg", "Tilbygning", "Tagarbejde",
                       "Døre og vinduer", "Terrasser", "Carporte", "Renovering"],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "bestRating": "5",
                            "reviewCount": str(ANM_ANTAL)},
        "sameAs": [FB, IG, ANM_URL],
    }

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def analytics_head():
    if not GA_ID:
        return ""
    return f"""<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{'ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied','analytics_storage':'denied','functionality_storage':'granted','security_storage':'granted','wait_for_update':500}});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',true);
(function(){{var m=document.cookie.match(/(?:^|; ){COOKIE}=([^;]*)/);if(m&&decodeURIComponent(m[1])==='alle'){{gtag('consent','update',{{'ad_storage':'granted','ad_user_data':'granted','ad_personalization':'granted','analytics_storage':'granted'}});}}}})();
gtag('js',new Date());gtag('config','{GA_ID}',{{'anonymize_ip':true}});
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>"""

def nav(active):
    ys = [s for s, _ in YDELSER]
    sub = "".join(f'<a href="{s}.html"{" class=\"active\"" if s == active else ""}>{e(n)}</a>' for s, n in YDELSER)
    def a(href, txt, key):
        return f'<li><a href="{href}"{" class=\"active\"" if key == active else ""}>{txt}</a></li>'
    return f"""<header>
  <div class="header-inner">
    <a href="index.html" class="logo"><img src="images/logo.webp" alt="{e(NAVN)}" width="437" height="150"></a>
    <nav id="mainnav" aria-label="Hovedmenu">
      <ul>
        {a('index.html', 'Forside', 'index')}
        <li class="nav-dd"><button type="button"{' class="active"' if active in ys else ''} aria-haspopup="true">Ydelser ▾</button><div class="nav-sub">{sub}</div></li>
        {a('referencer.html', 'Referencer', 'referencer')}
        {a('index.html#om', 'Om os', 'om')}
        {a('job.html', 'Job', 'job')}
        {a('kontakt.html', 'Kontakt', 'kontakt')}
      </ul>
    </nav>
    <div class="social">
      <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ICON_FB}</a>
      <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON_IG}</a>
    </div>
    <a class="hdr-tlf" href="tel:{TLF_RAW}">{ICON_TLF}<span>{TLF}</span></a>
    <button class="menu-toggle" type="button" aria-label="Åbn menu" aria-controls="mainnav" aria-expanded="false"
      onclick="var n=document.getElementById('mainnav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">☰</button>
  </div>
</header>"""

def cta(h="Har I et projekt vi skal se på?",
        p="Ring og fortæl kort om opgaven, eller send en beskrivelse og gerne et par billeder. Vi vender tilbage inden for 24 timer på hverdage."):
    return f"""<section class="cta"><div class="container cta-inner">
  <div><h2>{h}</h2><p>{p}</p></div>
  <div class="btn-row"><a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}Ring {TLF}</a><a class="btn btn-ghost" href="kontakt.html">Skriv til os</a></div>
</div></section>"""

def some():
    return f"""<section class="some"><div class="container">
  <p>Vi viser løbende vores opgaver på Facebook og Instagram.</p>
  <div class="social"><a href="{FB}" target="_blank" rel="noopener">{ICON_FB}Facebook</a><a href="{IG}" target="_blank" rel="noopener">{ICON_IG}Instagram</a></div>
</div></section>"""

def footer():
    ylinks = "".join(f'<li><a href="{s}.html">{e(n)}</a></li>' for s, n in YDELSER)
    return f"""<footer><div class="container">
  <div class="f-grid">
    <div>
      <img class="flogo" src="images/logo-hvid.png" alt="{e(NAVN)}" width="437" height="150">
      <p>Tømrermester og bygningskonstruktør. Fag- og hovedentrepriser for private og erhverv i Nordsjælland.</p>
      <p style="margin-top:1rem">{ADR}, {POST} {BY}<br><a href="tel:{TLF_RAW}">Tlf. {TLF}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
    </div>
    <div><h3>Ydelser</h3><ul>{ylinks}</ul></div>
    <div><h3>Virksomheden</h3><ul>
      <li><a href="referencer.html">Referencer</a></li><li><a href="index.html#om">Om os</a></li>
      <li><a href="job.html">Job</a></li><li><a href="kontakt.html">Kontakt</a></li>
      <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
    </ul></div>
  </div>
  <div class="f-bottom">© 2026 {e(NAVN)} · CVR {CVR}<br>
    <a href="cookies.html">Cookiepolitik</a> · <button type="button" class="ck-footerlink" onclick="return ckAabn()">Skift cookieindstillinger</button></div>
</div></footer>"""

COOKIE_HTML = """<div class="ck-banner" id="ckBanner" role="dialog" aria-labelledby="ckTitel" aria-describedby="ckBesk">
  <div class="ck-inner">
    <div><h2 id="ckTitel">Cookies på rosendal-tomrer.dk</h2>
      <p id="ckBesk">Vi bruger cookies til at se hvordan siden bliver brugt og til at måle effekten af vores annoncering. Kortet fra Google Maps på kontaktsiden sætter også cookies. Vælger du "Kun nødvendige", sættes ingen af delene, og siden virker præcis som før. <a href="cookies.html">Læs mere om cookies</a>.</p></div>
    <div class="ck-knapper"><button type="button" class="ck-afvis" onclick="ckSvar('noedvendige')">Kun nødvendige</button><button type="button" class="ck-accept" onclick="ckSvar('alle')">Accepter alle</button></div>
  </div>
</div>"""

COOKIE_JS = """<script>
(function(){
  var N='%(c)s',b=document.getElementById('ckBanner');
  function laes(){var m=document.cookie.match(new RegExp('(?:^|; )'+N+'=([^;]*)'));return m?decodeURIComponent(m[1]):null;}
  function skriv(v){document.cookie=N+'='+encodeURIComponent(v)+'; expires='+new Date(Date.now()+365*864e5).toUTCString()+'; path=/; SameSite=Lax';}
  function slet(){document.cookie=N+'=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; SameSite=Lax';}
  function g(v){if(typeof gtag!=='function')return;var s=v==='alle'?'granted':'denied';gtag('consent','update',{'ad_storage':s,'ad_user_data':s,'ad_personalization':s,'analytics_storage':s});}
  window.ckKort=function(){var w=document.getElementById('mapWrap');if(!w||w.querySelector('iframe'))return;
    w.innerHTML='<iframe src="https://maps.google.com/maps?q=Engdraget%%2011%%2C%%203390%%20Hundested&z=14&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" title="Kort: Engdraget 11, 3390 Hundested"></iframe>';};
  window.ckSvar=function(v){skriv(v);g(v);if(b)b.classList.remove('vis');if(v==='alle')ckKort();};
  window.ckAccepterKort=function(){ckSvar('alle');};
  window.ckAabn=function(){slet();if(b)b.classList.add('vis');return false;};
  var v=laes();if(v===null){if(b)b.classList.add('vis');}else if(v==='alle'){ckKort();}
})();
document.addEventListener('click',function(ev){var a=ev.target.closest?ev.target.closest('a[href^="tel:"]'):null;
  if(a&&typeof gtag==='function'){gtag('event','kontakt_opkald',{'nummer':a.getAttribute('href').slice(4)});}},true);
</script>""" % {"c": COOKIE}

def build_page(slug, title, desc, body, active=None, schemas=(), og_img="images/og-forside.jpg",
               noindex=False, extra_js=""):
    if len(title) > 60: raise ValueError(f"{slug}: title {len(title)} tegn")
    if len(desc) > 158: raise ValueError(f"{slug}: description {len(desc)} tegn")
    path = "" if slug == "index" else f"{slug}.html"
    url = f"{DOMAIN}/{path}"
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex, follow">\n' if (noindex or DEMO) else ""
    canon = "" if noindex else f'<link rel="canonical" href="{url}">\n'
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{analytics_head()}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}{canon}<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#1D3D73">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(NAVN)}">
<meta property="og:locale" content="da_DK">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{DOMAIN}/{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<style>{CSS}</style>
{ld}
</head>
<body>
{nav(active or slug)}
<main>
{body}
</main>
{footer()}
{COOKIE_HTML}
{COOKIE_JS}
{extra_js}
</body>
</html>
"""
