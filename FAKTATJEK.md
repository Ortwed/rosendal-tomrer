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

## Påstande der stadig skal bekræftes
- Tømrermester og uddannet bygningskonstruktør, og at han kan hjælpe med tegninger
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

## Go-live
- DEMO = False, FORMSPREE_ID og GA_ID i src/site_shared.py (verificer.py advarer, indtil de er sat)
- CNAME-fil i docs/ med rosendal-tomrer.dk
- Liste over gamle URL'er. Redirect-stubs findes for de 9 kendte
