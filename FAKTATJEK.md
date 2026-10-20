# Faktatjek med Sebastian før go-live

Opdateret 07-10-2026 efter gennemgang af det gamle site (skærmbilleder) og Anmeld Håndværker.

## Bekræftet via hans eget site eller Anmeld Håndværker
- Åbningstid mandag-fredag 07.00-17.00
- Dækker hele Nordsjælland og Hovedstadsområdet
- Byggaranti
- Søger løbende tømrersvende (jobside med formular)
- Gårdhaver = gårdmiljøer: hegn, skure, pergolaer, cykeloverdækninger, platforme. Private og erhverv
- 38 anmeldelser, snit 4,9, Elite. 6 ansatte (5/2026). 20 nyeste vises på referencesiden
- Ekstra ydelser fra Anmeld Håndværker: carporte, garager, udestuer, vinterhaver, trapper, spær, skillevægge, loftsbeklædning, facader, foldedøre, forsatsvinduer, køkkener, garderobeskabe

## Påstande bekræftet af Sebastian 13-10-2026 (står også på Anmeld Håndværker)
- Tømrermester og uddannet bygningskonstruktør (tegninger leverer han ikke, det er fjernet fra sitet 12-10-2026)
- Medlem af Dansk Håndværk (vises sammen med byggaranti)
- Svartid "inden for 24 timer på hverdage"
- Faste samarbejdspartnere: murer, el, VVS, maler, kloak
- Belægning "i samarbejde med en lokal anlægsgartner" (terrasse og gårdhaver)
- Asbest i ældre eternittage (tag-siden)
- Materieludlejning: hvad udlejes, levering, opstilling
- Må vi bruge hans underskrift på forsiden? (klippet fra det gamle site)
- Er det ok at vise anmeldelserne med fornavn og by?

## Billeder
- Ipé-broen, de runde bænke, jobbilen og underskriften er klippet ud af skærmbilleder. Bænkene er kun 360 px brede. Bed om originalerne
- Hent ALDRIG billeder direkte fra det inficerede WordPress-site. Bed Sebastian sende dem fra telefonen
- Projektsider er bygget, men skjult (status 'pending'), indtil der er færdigbilleder
- Billeder af Sebastian og holdet i gang med rigtige opgaver til de fire punkter på forsiden (ingen stockbilleder)

## Efter go-live
- Nye FAQ-spørgsmål (Nybyg har kun ét tilbage, Hovedentreprise to), projektsider og undersider
- Anmeld Håndværker-widget på Referencer og forsiden. Koden ligger i Sebastians firmalogin
- Formularer via PHP på Simply i stedet for Formspree (data bliver i DK). Kræver egen spambeskyttelse, og Jakob skal bekræfte PHP mail() samt SPF/DKIM. Formspree slås fra, når det er testet mod info@

## Go-live (13-10-2026, Simply.com)
- Sitet ligger på Simply.com. ortwed.github.io er testside med noindex (docs/). Live bygges med `python3 src/build.py --live`, som laver live/ og rosendal-tomrer-live.zip til upload
- DEMO = False. GA_ID er ikke sat (ingen Google Analytics)
- Formspree: formularen mbgdzaov på Sebastians konto, sender til info@, låst til rosendal-tomrer.dk
- .htaccess: HTTPS uden www, 301 for de 9 gamle URL'er, 410 på wp-stier

## Efter go-live, oprydning
- Slet Christians gamle Formspree-formular (mrpekpzr), når en test fra rosendal-tomrer.dk er kommet frem
- Google Search Console sat op 20-10-2026. Google Virksomhedsprofil overtaget, website-feltet peger på https://rosendal-tomrer.dk/ med UTM (utm_source=google, utm_medium=organic, utm_campaign=gbp)
- Indsend sitemap.xml igen i Search Console, når den nye sitestruktur er uploadet til Simply
- Når den nye struktur er live: ret GBP's booking/kontaktlink til https://rosendal-tomrer.dk/kontakt/ (ikke kontakt.html), og anmod om indeksering af de nye adresser (/tag/, /terrasse/ osv.)
- Status på GBP og Search Console: se GBP-GSC-STATUS.md (20-10-2026). Search Console viser ingen sikkerhedsproblemer
- Slet grenen udkast-materieludlejning på GitHub (identisk med main)
