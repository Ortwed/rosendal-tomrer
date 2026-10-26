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

## Melby (projektcase: siddebænke i termofyr, 26-10-2026)
Bygget og testet, men står som status "pending". Christian skal afklare, før casen sættes live:
1. Må skolens navn (Melby Skole) bruges? Indtil da står der "en skole i Melby" i title, H1, tekster, alt-tekster og schema
2. Hører billede 04 (rund bænk i rødbrunt hårdttræ på stålstel, brosten, med en person) til projektet? Det er ikke med
3. Hvad omfattede "ny legeplads"? Ordet "legeplads" er ikke brugt på siden. Billede 03 viser en gynge i baggrunden, som vi ikke omtaler
4. Findes der en anmeldelse på Anmeld Håndværker? Indtil da er der intet afsnit om kundens anmeldelse
5. Billederne: på billede 02 er to personer i baggrunden og nummerpladen på varevognen sløret. På billede 03 er nummerpladen sløret. Christian bekræfter, at billederne må bruges
- Afventer Sebastian: omfang, mål, hvorfor termofyr blev valgt og hans erfaring med termofyr i skolemiljø (felterne står klar og vises først, når de er udfyldt)
- Fakta om termofyr er kun de kildebelagte: varmebehandlet uden kemikalier, mere dimensionsstabil end trykimprægneret, brun farve, UV-olie anbefales af producenter, ellers sølvgrå patina. Intet om holdbarhed i år, holdbarhedsklasse eller jordkontakt
- Casen er knyttet til ydelsen "Pergola, hegn og cykelskur" (bænke og gårdmiljøer) og linker til /terrasse/, de to andre cases og /omrader/
- Billederne er 720 og 1440 px webp som de andre cases, ikke 480/800/1200/1600 som i prompten
