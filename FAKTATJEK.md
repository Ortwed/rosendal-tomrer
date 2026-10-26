# Faktatjek med Sebastian før go-live

Opdateret 07-10-2026 efter gennemgang af det gamle site (skærmbilleder) og Anmeld Håndværker.

## Bekræftet via hans eget site eller Anmeld Håndværker
- Åbningstid mandag-fredag 07.00-16.00 (rettet efter mødet 23-10-2026, var 07.00-17.00)
- Arbejdsområde fra Hundested til Frederikssund, Stenløse, Farum og Hørsholm (mødet 23-10-2026). Hovedstadsområdet er taget ud af sitet
- Byggaranti
- Søger løbende tømrersvende (jobside med formular)
- Gårdhaver = gårdmiljøer: hegn, skure, pergolaer, cykeloverdækninger, platforme. Private og erhverv
- 38 anmeldelser, snit 4,9, Elite. 7 ansatte (mødet 23-10-2026, var 6 i 5/2026). 20 nyeste vises på referencesiden
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
- GBP's booking/kontaktlink er sat 20-10-2026 til https://rosendal-tomrer.dk/kontakt.html?utm_source=google&utm_medium=organic&utm_campaign=gbp-kontakt
- Når den nye struktur er live: ret GBP's booking/kontaktlink til https://rosendal-tomrer.dk/kontakt/ (samme UTM), og anmod om indeksering af de nye adresser (/tag/, /terrasse/ osv.)
- GA4 (G-Y07ZQXFQWY) er live på Simply siden 20-10-2026 på den nuværende version (gren live-ga4, bygget fra 5fc7680). Testet: realtid virker. Nøglehændelser markeres i GA4, når der er data: kontakt_opkald, email_click, generate_lead. Mangler i GA4: dataopbevaring 14 mdr., Google-signaler fra, knyt til Search Console. main (ny struktur) har også GA4 og afløser live-ga4, når den uploades
- Status på GBP og Search Console: se GBP-GSC-STATUS.md (20-10-2026). Search Console viser ingen sikkerhedsproblemer
- Slet grenen udkast-materieludlejning på GitHub (identisk med main)

## Materieludlejning (siden /materieludlejning/, 21-10-2026)
Bygget ud fra Sebastians Word-dokument "Rosendal Materiel Udlejning" (12 maskiner). Afklar med Sebastian:
- Bukkestillads: hvad betyder "Stilladsklasse 4 300 Kr/m2"? Udeladt indtil videre
- Affugter DH 752: "rumstørrelse 701 m3" og "900 W" strider mod producentens data. Udeladt indtil videre
- Girafsliber: præcist modelnavn (står kun som "Festool girafsliber")
- Gælder lejebetingelserne og forsikringsgebyret på 7 % stadig? Den nye PDF er ordret den samme som den gamle
- Levering: lejebetingelserne siger "kontakt for pris". Er det stadig sådan?
- Trailer: udlejes den stadig? Den står ikke i Word-dokumentet og er derfor fjernet fra siden
- Geografi: siden følger OMRAADE, som nu er Nordsjælland
- Illustrationerne er tegninger (src/lav_materiel_svg.py), ikke fotos af Sebastians materiel

## Anmeld Håndværker-widgets (22-10-2026)
- Elite-badge (type 3) i toppen af forsiden, slider (type 2) i "Det siger vores kunder" og liste (type 6) på /anmeldelser/. Koderne er indsat uændret, scriptet ligger nederst på siden
- Tjek på testsiden: vises de tre widgets, og kommer de det rigtige sted? Hvis en widget dukker op nederst på siden i stedet, bruger scriptet document.write og skal stå lige efter sin div
- Tjek om widgets sætter cookies (DevTools → Application → Cookies, domæne anmeld-haandvaerker.dk). Gør de, skal de først indlæses efter samtykke
- Virker widgetsene ikke på ortwed.github.io, kan Anmeld Håndværker have låst dem til rosendal-tomrer.dk. Så testes de først live
- Faktalinjerne har ikke længere faste anmeldelsestal eller "Byggaranti". Elite-badget og Garanti-logoet fra Dansk Håndværk står under Ring- og tilbudsknappen på forsiden
- Garanti-logoet må kun bruges som medlem af Dansk Håndværk. Medlemskabet er bekræftet af Sebastian, men dokumentation mangler stadig
- De korte kundecitater på ydelsessiderne er stadig vores egne


## Mødet med Sebastian 23-10-2026
- Totalentreprise hedder nu hovedentreprise. /totalentreprise/ sender 301 til /hovedentreprise/
- Sommerhus er ikke længere en selvstændig ydelse. /sommerhus/ sender 301 til /renovering/, og sommerhuse er nævnt på renovering og terrasse
- Materieludlejning: alle priser, gebyrer og procentsatser er taget af udlejningssiden, lejebetingelserne og schema ("Kontakt os for pris"). Priserne står kun i Sebastians Word-dokument. Lejebetingelserne siger nu "oplyses ved booking" om selvrisiko, forsikringsgebyr, annullering og rengøring. Det er juridisk tekst, så Sebastian skal godkende formuleringen
- Afventer Sebastians krydstjek med Stark: priser, maskiner og specs. Affugterens rumstørrelse er fjernet ("til mindre lokaler"). Bukkestilladsets stilladsklasse og girafsliberens modelnavn er stadig uafklaret. Ingen billeder eller specs fra Stark, og ingen af Sebastians produktbilleder
- 7 ansatte: tæller Sebastian med i de 7? Sitet skriver "Vi er 7 ansatte"
- Uddannet tømrer 2010 og bygningskonstruktør 2018 står som hans personlige uddannelse (Om os, schema, llms.txt). Firmaet er stiftet 2021
- Hans faglige holdning om træ til terrasser står på Om os og terrasse-siden i hans stemme. Ingen konkrete træarter endnu (kommer som separat content)
- Dansk Håndværk: "overenskomst for medarbejderne og et garantistempel for kunderne" står på Om os. Beløbet nævnes ikke nogen steder
- Google-profilen skal sige det samme som sitet: åbningstid 07.00-16.00 og arbejdsområdet (ikke Hovedstadsområdet)

## Projektcase: træterrasse i Hundested (23-10-2026)
- Siden /projekter/traeterrasse-trykimpraegneret-hundested/ er live på testsiden. Casen linkes fra terrasse, Hundested og Områder
- FAQ "Overholder I tidsplanen?": sætningen "Vi aftaler tidsplanen med dig, før arbejdet går i gang." skal godkendes af Sebastian
- Linket til anmeldelsen går til Rosendals profil på Anmeld Håndværker, ikke til selve anmeldelsen. Skift til et direkte link, hvis Anmeld Håndværker har et
- Kunden er ikke nævnt ved navn ("Kunden fra Hundested"), og der er ingen Review-markup
- Billederne er omdøbt og konverteret fra de tre fotos, Christian sendte. Det fjerde foto (terrassen set langs husets glasdøre) er med som billede 4 i galleriet

## Projektcase: jatoba-terrasse i Liseleje (23-10-2026)
- Live på testsiden. Billederne er Christians tre fotos (23-10-2026), omdøbt til jatoba-terrasse-liseleje-1..3. Hovedbilledet er terrassen langs glaspartierne med trapperne i kanten. Billede 3 står på højkant
- Casene linker til hinanden under "Andre projekter"
- Terrasse-siden nævner nu jatoba ved siden af ipé og trykimprægneret træ (kort svar, "Det bygger vi" og "Valg af træ"). Skal godkendes af Sebastian
- Afventer Sebastian, felterne står klar i skabelonen og vises først, når de er udfyldt: størrelse i m², højde over terræn, tidsforbrug eller måned, leverandør (evt. FSC), trappernes opbygning (antal trin, placering), hans råd om vedligehold og olie, før- og detaljebilleder
- Fakta om jatoba (art, oprindelse, farve, vægtfylde 900 til 1.000 kg/m³) er fra generelle træreferencer. Ingen Janka-tal
- Anmeldelsen (1. august 2025) nævner ikke jatoba. Linket går til profilen på Anmeld Håndværker. Bindestregen foran "meget" i citatet er fjernet

## Vores projekter og anmeldelser (23-10-2026)
- Materieludlejning har sin egen dropdown i topmenuen efter "Vores projekter": Alt materiel, El-værktøj, Bygningsmateriel, Jord og anlæg og Lejebetingelser. Den står ikke længere under Ydelser
- "Vores projekter" har sin egen dropdown i topmenuen efter Kontakt, med "Alle projekter" (/projekter/) og en linje pr. case. Reglen om at vente til 3 cases er droppet
- /anmeldelser/ viser kun widgetten fra Anmeld Håndværker og linket til profilen. Projektkortene og linket til anmeldelser på Facebook er fjernet derfra

## Melby (projektcase: siddebænke i termofyr, live på testsiden 26-10-2026)
Afklaret af Christian: skolens navn må bruges, billederne er godkendt, "legeplads" er trædækkene med bænke rundt om træerne, og der er ingen anmeldelse.
Til Sebastian:
1. Er den runde bænk på billede 04 i termotræ? Christian siger ja, men den ser rødbrun ud. Er det termofyr eller en anden varmebehandlet træsort?
2. Omfang, mål, hvorfor termofyr blev valgt og hans erfaring med termofyr i skolemiljø (felterne står klar og vises først, når de er udfyldt)
- Personen på billede 04 er sløret, og fotografens fod er skåret væk. På billede 02 er to personer og en nummerplade sløret, på 03 en nummerplade
- "Thermofyr" og "thermotræ" nævnes én gang hver som søgevariant
- Casen hører under ydelsen "Pergola, hegn og cykelskur" (bænke og gårdmiljøer)
- Billederne er 720 og 1440 px webp som de andre cases, ikke 480/800/1200/1600 som i prompterne

## Renovering Melby (projektcase: efterisolering og ny facade, live på testsiden 26-10-2026)
Afklaret af Christian: samme hus før og efter, kunden er indforstået med billederne, og vinduer, døre, indfatninger og tag blev ikke skiftet. Ingen anmeldelse.
Til Sebastian:
1. Hvilken træsort og profil er den nye beklædning? Siden siger kun "træbeklædning"
2. Isolering, vindspærre og ventilation, hvorfor udvendigt, areal og tid (felterne står klar)
- FAQ om vinduer og dørpartier er udeladt
- Hovedbilledet (efter, 03) står øverst. Før/efter-afsnittet viser 01 og 02 som før og 04 og 05 som efter

## Tegltag Hundested (projektcase: nyt tegltag, live på testsiden 26-10-2026)
Afklaret af Christian: kunden er indforstået med billederne, og linket med rid=2145085 åbner den rigtige anmeldelse.
Til Sebastian:
1. Tagsten (type, farve) og antal velux-vinduer før og efter. Vinduerne er ikke talt i teksten, kun i alt-teksten til førbilledet ("to velux-vinduer"), som prompten angav
2. Hardie Plank: producentens egen beskrivelse er ikke tjekket. Siden siger kun "fibercement" og "for at begrænse vedligeholdelsen", aldrig "vedligeholdelsesfri"
3. Undertag, lægter, tid og areal, og hvorfor Hardie Plank (felterne står klar)
- Anmeldelsens "Rigtige flinke" er rettet til "Rigtig flinke" som tastefejl
- Postkasse og husnummer på billede 03 var sløret på forhånd. Navneskiltet på hoveddøren på billede 01 er sløret for en sikkerheds skyld
- Der er kun ét efterbillede, så hovedbilledet står også sidst i rækken "Før, under og efter" med sin egen alt-tekst

## Anmeldelseslinks på cases (26-10-2026)
- anmeldelse_html i build.py: citatet som tekst, byline "Kunde i <by>", target="_blank" rel="noopener noreferrer". Ingen Review-markup, ingen navne, aldrig "verificeret kunde"
- Som udgangspunkt linker alle cases til profilen (ANM_URL) med teksten "Se vores profil og anmeldelser på Anmeld Håndværker" og cta_click "anmeldelse_profil" (case 1 og 2)
- Case 5 (tegltag) linker direkte til anmeldelsen med rid=2145085, fordi Christian har testet, at linket åbner Kenneths anmeldelse. Teksten er så "Anmeldelse på Anmeld Håndværker" og cta_click "anmeldelse_link". Den nye prompt (del B) siger profil på alle cases, men den er skrevet, før linket blev testet. Sig til, hvis case 5 også skal linke til profilen
- Nye direkte links: sæt anm_rid på casen i build.py, når linket er testet. Ingen delingslinks fra Facebook

## Guide træ til terrasse (26-10-2026)
Siden /guide/trae-til-terrasse/ er bygget ud fra Christians udkast med Sebastians svar. Flaget GODKENDT_AF_SEBASTIAN i indhold.py er False:
- Testsiden viser guiden med noindex, uden byline og uden links fra andre sider. Den er hverken i sitemap eller llms.txt
- Live-builden bygger den slet ikke. verificer.py fejler, hvis den alligevel kommer med, eller hvis en side linker til den før godkendelsen
- Når Sebastian har godkendt teksten: sæt GODKENDT_AF_SEBASTIAN = True. Så kommer byline (med Sebastian som author i schema), sitemap, llms.txt og links fra /terrasse/ og case 1, 2 og 3 automatisk
Til Sebastian:
1. Godkend hele teksten, også levetiderne (15 til 20 år og 25 til 50 år eller mere), som står som hans skøn og ikke en garanti
2. FAQ "Hvor bygger I terrasser?": udkastet nævner "hovedstadsområdet". Efter mødet 23-10-2026 bruger sitet arbejdsområdet (fra Hundested til Frederikssund, Stenløse, Farum og Hørsholm), så svaret følger det. Han afgør, hvad der skal stå
3. Guiden siger "Vi fravælger ikke nogen træsorter". Om os og terrassesiden siger, at han fraråder blødt træ tæt på vandet. Passer de to sammen for ham?
4. Senere, kun med hans ja: hvad han mener med "brun imprægneret", eksempler (Vedbæk, jatoba, kyst), kilde til et eventuelt kommunalt forbud, fakta om ipé, "hvad ville jeg vælge derhjemme" og citater med hans navn
- Ingen billeder endnu. Der er plads til et hero-billede (kommentar i build.py). Ingen lagerfotos

## Fælles anmeldelseskomponent, oprindelig (26-10-2026, erstattet af afsnittet ovenfor)
- anmeldelse_html i build.py: citatet som tekst, byline "Kunde i <by>", linket "Anmeldelse på Anmeld Håndværker" med target="_blank" rel="noopener noreferrer" og cta_click (anmeldelse_link). Ingen Review-markup
- Link til den enkelte anmeldelse: ANM_RID_URL i site_shared.py (profilen med ?rid=<id>). Delingslinks fra Facebook omsættes til den dekodede u-parameter
- Case 1 og 2 linker stadig til profilen. Christian indsætter deres rid i anm_url
