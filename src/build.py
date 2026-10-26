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
# og tekst fra Sebastian. Saet status til 'live' og udfyld felterne som i traeterrasse-casen, saa bygges siden.
# Valgfrie felter: en linje i fakta eller en sektion i sek/sek_efter med vaerdien None vises ikke. Saa kan Sebastians
# svar (m², tidsforbrug, leverandoer, vedligehold osv.) skrives direkte ind, naar de kommer. udvidet = kundens laengere
# kommentar. Flere billeder, fx foer- og detaljebilleder, er bare flere linjer i billeder.
# Opfind aldrig tal: et tomt felt er bedre end et gaet.
PROJEKTER = [
    dict(slug="traeterrasse-trykimpraegneret-hundested", status="live", ydelse="terrasse", by="Hundested", aar="2025",
         titel="Træterrasse i trykimprægneret træ i Hundested",
         kort="Træterrasse i trykimprægneret træ",            # kortet paa projektoversigten
         tag="Trykimprægneret træ",                            # lille etiket paa kortet (valgfri, ligesom undertekst)
         link_tekst="træterrasse i Hundested",                # "Se et projekt: ..." fra ydelses- og omraadesider
         title="Træterrasse i trykimprægneret træ, Hundested | Rosendal",
         desc="Ny træterrasse i trykimprægneret træ i Hundested, bygget som 1:1-kopi af den gamle. Se projektet og kundens anmeldelse. Rosendal Tømrer.",
         svar="I 2025 byggede vi en ny træterrasse i trykimprægneret træ ved et hus i Hundested. Den nye terrasse blev lavet som en 1:1-kopi af den gamle, så mål og udtryk gik igen. En terrasse som denne kan vi også bygge til dit hus i Nordsjælland.",
         fakta=[("Opgave", "Ny træterrasse"), ("Materiale", "Trykimprægneret træ"), ("Sted", "Hundested"), ("År", "2025"),
                ("Størrelse", None), ("Tidsforbrug", None), ("Den gamle terrasse", None)],   # None = afventer Sebastian
         anmeldt=("4. juli 2025", "Anmeld Håndværker"), udvidet=None,
         anm_url=None, anm_opgave=None,   # Christian indsaetter ANM_RID_URL.format(rid=...) eller det link, han har
         billeder=[  # (fil uden endelse i /images/projekter/, alt, billedtekst eller None[, (bredde, hoejde)]).
                     # Det foerste er hovedbilledet. Maalene skal kun med, naar det store billede ikke er 1440 x 1080.
             ("traeterrasse-trykimpraegneret-hundested-1", "Ny træterrasse i trykimprægneret træ ved et hus med store glaspartier i Hundested.",
              "Ny træterrasse i trykimprægneret træ langs husets glaspartier, Hundested, 2025."),
             ("traeterrasse-trykimpraegneret-hundested-4", "Træterrassen i Hundested set langs husets glasdøre, med en ramme af brædder der skifter retning mod næste felt.", None),
             ("traeterrasse-trykimpraegneret-hundested-2", "Hele træterrassen i Hundested med brædder lagt i to retninger og en ramme af brædder mellem felterne.", None),
             ("traeterrasse-trykimpraegneret-hundested-3", "Detalje af ramme af brædder mellem to felter i en træterrasse i Hundested.", None),
         ],
         og_img="images/og-traeterrasse-trykimpraegneret-hundested.jpg",
         sek=[
             ("Opgaven: en ny terrasse, der ligner den gamle", ["Kunden i Hundested skulle have en ny træterrasse i trykimprægneret træ. Ønsket var, at den nye terrasse skulle være en 1:1-kopi af den gamle, så den passede til huset og til den måde, haven blev brugt på."]),
             ("Sådan blev den bygget", ["Vi byggede den nye terrasse i trykimprægneret træ og lavede den 1 til 1 som den gamle. Terrassen ligger langs husets lange række af glaspartier og døre. Brædderne er lagt i to retninger, med en ramme af brædder imellem felterne, og det giver terrassen et roligt, men levende udtryk. Kunden beskriver selv terrassen som stor."]),
         ],
         citat="En stor terrasse. Dygtige og behagelige håndværkere. Overholdt tidsplan og lavede flot arbejde.",
         karakterer="Kunden gav 5 ud af 5 på kommunikation, aftale, pris i forhold til tilbud, tilfredshed og oprydning.",
         sek_efter=[
             ("Trykimprægneret træ til terrasse", ('html', '<p>Trykimprægneret træ er et almindeligt valg til terrasser. Vi bygger terrasser i både trykimprægneret træ og hårdttræ som ipé. Er du i tvivl om, hvilket der passer til dit hus og din have, hjælper vi dig med at vælge. <a href="/terrasse/">Læs mere om terrasser</a>.</p>')),
             ("Skal du have en ny terrasse?", ('html', f'<p>Har du en gammel terrasse, der skal udskiftes, kan vi bygge en ny, der ligner den gamle, eller tegne en helt ny løsning sammen med dig. Vi tager opgaver i <a href="/tomrer-hundested/">Hundested</a> og resten af Nordsjælland. Ring på <a href="tel:{TLF_RAW}">{TLF}</a> eller <a href="/kontakt/" data-cta="projekt-tekst">skriv til os</a>, så aftaler vi en besigtigelse og giver dig et skriftligt tilbud.</p>')),
         ],
         faq=[
             ("Kan I bygge en ny terrasse, der er en kopi af den gamle?", "Ja. I dette projekt i Hundested blev den nye terrasse lavet 1 til 1 som den gamle."),
             ("Hvilket træ blev brugt?", "Trykimprægneret træ."),
             ("Bygger I terrasser uden for Hundested?", "Ja, vi bygger terrasser i hele Nordsjælland."),
             ("Hvad koster en ny terrasse?", "Prisen afhænger af størrelse, materiale og underlag. Efter en besigtigelse får du et skriftligt tilbud."),
             # Sidste saetning skal godkendes af Sebastian (FAKTATJEK.md)
             ("Overholder I tidsplanen?", "Kunden i Hundested skrev i sin anmeldelse, at vi overholdt tidsplanen. Vi aftaler tidsplanen med dig, før arbejdet går i gang."),
         ]),
    dict(slug="jatoba-terrasse-liseleje", status="live", ydelse="terrasse", by="Liseleje", aar="2025",
         titel="Jatoba terrasse med indbyggede trapper i Liseleje",
         kort="Jatoba terrasse med indbyggede trapper", tag="Jatoba",
         link_tekst="jatoba-terrasse i Liseleje",
         title="Jatoba terrasse med indbyggede trapper, Liseleje | Rosendal",
         desc="Ny terrasse i jatoba 21x145 mm på trækonstruktion med indbyggede trapper i Liseleje. Se projektet, fakta om jatoba og kundens anmeldelse.",
         svar="I 2025 byggede vi en ny terrasse i jatoba 21 × 145 mm på en trækonstruktion i Liseleje, med indbyggede trapper. Jatoba er et hårdt og tæt hårdttræ med rødbrun farve, som egner sig til terrasser. Vi bygger terrasser i hele Nordsjælland.",
         fakta=[("Opgave", "Ny terrasse med indbyggede trapper"), ("Træsort", "Jatoba"), ("Brædder", "21 × 145 mm"), ("Konstruktion", "Træ"),
                ("Sted", "Liseleje"), ("År", "2025"),
                ("Størrelse", None), ("Højde over terræn", None), ("Tidsforbrug", None), ("Leverandør", None)],   # afventer Sebastian
         anmeldt=("1. august 2025", "Anmeld Håndværker"), udvidet=None,
         anm_url=None, anm_opgave=None,   # Christian indsaetter ANM_RID_URL.format(rid=...) eller det link, han har
         billeder=[
             ("jatoba-terrasse-liseleje-1", "Ny terrasse i jatoba på trækonstruktion med indbyggede trapper ved et sort hus i Liseleje.",
              "Ny jatoba-terrasse med indbyggede trapper, Liseleje, 2025."),
             ("jatoba-terrasse-liseleje-2", "Jatoba-terrassen set på afstand, hele vejen rundt om et sort hus med fyrretræer og en birk i Liseleje.", None),
             ("jatoba-terrasse-liseleje-3", "Hjørnet af en hævet jatoba-terrasse under husets tagudhæng i Liseleje, med kanten klædt i samme træ.", None, (1125, 1500)),
         ],
         og_img="images/og-jatoba-terrasse-liseleje.jpg",
         sek=[
             ("Opgaven: en ny jatoba-terrasse med trapper", ["Kunden i Liseleje skulle have en ny terrasse i jatoba, opført på en trækonstruktion og med trapper bygget ind i terrassen."]),
             ("Sådan blev den bygget", ["Vi byggede terrassen på en trækonstruktion og lagde dækket i jatoba 21 × 145 mm. Terrassen ligger hævet over terrænet langs husets glaspartier, og kanten er klædt med brædder i samme træsort, så den fremstår som ét samlet træværk. Trapperne er bygget ind i terrassens kant, så de er en del af terrassens form og ikke en separat trappe, der står ved siden af."]),
             ("Sådan er trapperne bygget op", None),   # antal trin og placering, afventer Sebastian
             ("Hvad er jatoba?", ["Jatoba (Hymenaea courbaril) er et hårdttræ fra Mellem- og Sydamerika. Det kaldes også brasiliansk kirsebær. Kernetræet er laksrødt til orangebrunt og bliver med tiden mørkere, især når det rammes af sollys. Jatoba er meget hårdt og tæt, med en vægtfylde omkring 900 til 1.000 kg/m³, og regnes for holdbart og modstandsdygtigt over for naturlig nedbrydning, og det er derfor, det bruges til terrasser og trapper. Fordi træet er så hårdt, er det mere krævende at bearbejde end nåletræ. Som alt træ arbejder det med årstiderne."]),
             ("Jatoba eller trykimprægneret træ?", ('html', '<p>Trykimprægneret træ er et almindeligt og økonomisk valg til terrasser, mens hårdttræ som jatoba og ipé har en tættere struktur og en dybere farve. Du kan se et eksempel på en terrasse i trykimprægneret træ i vores projekt <a href="/projekter/traeterrasse-trykimpraegneret-hundested/">træterrasse i Hundested</a>. Er du i tvivl om, hvad der passer til dit hus og din have, hjælper vi dig med at vælge. Læs mere om <a href="/terrasse/">terrasser</a>.</p>')),
             ("Sebastians råd om vedligehold af jatoba", None),   # afventer Sebastian
         ],
         citat="God kommunikation, god pris, flot arbejde, meget tilfredse.",   # bindestregen foran "meget" i originalen er fjernet
         karakterer="Kunden gav 5 ud af 5 på kommunikation, aftale, pris i forhold til tilbud, tilfredshed og oprydning.",
         sek_efter=[
             ("Skal du have en ny terrasse?", ('html', f'<p>Vi bygger terrasser i jatoba, andre hårdttræsorter og trykimprægneret træ, med eller uden indbyggede trapper. Vi tager opgaver i Liseleje og resten af Nordsjælland. Ring på <a href="tel:{TLF_RAW}">{TLF}</a> eller <a href="/kontakt/" data-cta="projekt-tekst">skriv til os</a>, så aftaler vi en besigtigelse og giver dig et skriftligt tilbud.</p>')),
         ],
         faq=[
             ("Hvad er jatoba?", "Jatoba er et hårdt og tæt hårdttræ fra Mellem- og Sydamerika med rødbrun farve, som bliver mørkere med tiden. Det bruges blandt andet til terrasser og trapper."),
             ("Hvad er forskellen på jatoba og trykimprægneret træ?", "Jatoba er et hårdttræ, der er hårdere og tættere end trykimprægneret nåletræ. Trykimprægneret træ er et almindeligt og økonomisk valg til terrasser. Vi hjælper dig med at vælge ud fra hus, have og budget."),
             ("Skal en jatoba-terrasse olieres?", "Det er et valg. Ubehandlet udvikler jatoba en naturlig patina. Vil du bevare den varme røde farve, kan terrassen olieres. Vi rådgiver om, hvad der passer til din terrasse."),
             ("Kan I bygge trapper ind i terrassen?", "Ja. I dette projekt i Liseleje er trapperne bygget ind i terrassens kant."),
             ("Bygger I terrasser i Liseleje og omegn?", "Ja, vi bygger terrasser i Liseleje og i hele Nordsjælland."),
             ("Hvad koster en jatoba-terrasse?", "Prisen afhænger af størrelse, træsort, konstruktion og trapper. Efter en besigtigelse får du et skriftligt tilbud."),
         ]),
    # Case 3. Afklaret af Christian: skolens navn maa bruges, billederne er godkendt (personen paa 04 forbliver sloeret),
    # "legeplads" er traedaekkene rundt om traeerne, og den runde baenk er i termotrae. Ingen anmeldelse.
    dict(slug="siddebaenke-termofyr-melby-skole", status="live", ydelse="pergola-hegn-og-cykelskur", by="Melby", aar="2024",
         titel="Siddebænke i termofyr og nyt udeområde, Melby Skole",
         krumme="Siddebænke i termofyr, Melby Skole",
         kort="Siddebænke i termofyr, Melby Skole", undertekst="Nye bænke og udeområde, 2024", tag="Termofyr",
         link_tekst="siddebænke i termofyr på Melby Skole",
         title="Siddebænke i termofyr og udeområde, Melby Skole | Rosendal",
         desc="Nye siddebænke i termofyr og nyt udeområde på Melby Skole i 2024. Se projektet og fakta om termofyr fra Rosendal Tømrer i Nordsjælland.",
         svar="Vi har udført nye siddebænke i termofyr og et nyt udeområde ved Melby Skole i 2024. Bænkene er bygget ind i trædæk omkring skolegårdens store træer. Termofyr er varmebehandlet fyr uden kemikalier, og det er mere formstabilt end ubehandlet fyr.",
         fakta=[("Projekt", "Nye siddebænke i termofyr og nyt udeområde"), ("Sted", "Melby"), ("År", "2024"),
                ("Træ", "Termofyr (varmebehandlet fyr)"),
                ("Omfang", "Trædæk med siddebænke rundt om træerne og en rund bænk i termotræ på stålstel"), ("Størrelse", None)],   # None = afventer Sebastian
         anmeldt=None, citat=None, udvidet=None,   # der findes ingen anmeldelse til casen
         billeder=[
             ("melby-skole-termofyr-traedaek-omkring-trae-01", "Trædæk og siddebænke i termofyr omkring et stort træ i skolegård, Melby",
              "Trædæk med indbyggede bænke omkring skolegårdens træer"),
             ("melby-skole-termofyr-siddebaenke-skolegaard-02", "Nye siddebænke i termofyr i skolegård ved Melby Skole", "Siddebænke i termofyr i skolegården"),
             ("melby-skole-termofyr-traedaek-rosendal-varevogn-03", "Færdigt trædæk med termofyrbænke og Rosendal Tømrers varevogn i baggrunden, Melby",
              "Færdigt udeområde, Melby 2024"),
             # Christian: termotrae. Ikke "termofyr", da traesorten bag varmebehandlingen ikke er bekraeftet
             ("melby-skole-rund-baenk-staalstel-04", "Rund bænk i termotræ på stålstel på belægning ved Melby Skole", "Rund bænk i udeområdet", (1440, 1632)),
             ("melby-skole-termofyr-siddebaenke-traedaek-05", "Nyolieret termofyr på siddebænke og trædæk, orangebrun farve, skolegård i Melby", "Termofyr efter oliering"),
             ("melby-skole-termofyr-traedaek-og-siddebaenke-06", "Trædæk i flere niveauer med siddebænke i termofyr, Melby Skole", "Udeområdet set fra siden"),
         ],
         og_img="images/og-siddebaenke-termofyr-melby-skole.jpg",
         sek=[
             ("Om projektet", ["Vi har udført nye siddebænke i termofyr og et nyt udeområde ved Melby Skole i Melby i 2024. Den nye legeplads er bygget som trædæk i flere niveauer, og siddebænkene er bygget ind i dækket omkring de store træer i skolegården. Trædækket og de indbyggede bænke er udført i termofyr. Projektet omfatter også en rund bænk i termotræ, også kaldet thermotræ, på stålstel."]),
             ("Hvad er termofyr?", ["Termofyr, som også skrives thermofyr, er fyrretræ, der er varmebehandlet uden kemikalier. Varmebehandlingen gør træet mere dimensionsstabilt end almindeligt trykimprægneret træ, så det arbejder mindre, og den giver træet en mørk, brun farve. Producenter anbefaler UV-olie for at bevare farven udendørs. Uolieret går træet med tiden i en sølvgrå patina."]),
             ("Hvorfor termofyr til siddebænke?", ["Termofyr er ikke kemisk imprægneret, fordi træet alene er varmebehandlet. Samtidig giver varmebehandlingen træet en varm brun farve."]),
             ("Sebastians erfaring med termofyr", None),   # afventer Sebastian, kun med hans accept
         ],
         sek_efter=[
             ("Skal I have siddebænke eller trædæk?", ('html', f'<p>Vi bygger siddebænke, trædæk og terrasser i hele <a href="/omrader/">Nordsjælland</a>. Ring på <a href="tel:{TLF_RAW}">{TLF}</a> eller <a href="/kontakt/" data-cta="projekt-tekst">skriv til os</a>, så aftaler vi en besigtigelse og giver jer et skriftligt tilbud.</p>')),
         ],
         faq=[
             ("Hvad er termofyr (thermofyr)?", "Termofyr er varmebehandlet fyr uden kemikalier. Det er mere formstabilt og brunt i farven."),
             ("Skal termofyr vedligeholdes?", "Producenter anbefaler UV-olie for at bevare den brune farve. Uolieret bliver træet med tiden sølvgråt."),
             ("Hvor har I udført projektet?", "På Melby Skole i Melby i 2024."),
             ("Udfører I også terrasser og udeområder til private?", ('html', 'Ja, se vores terrasseprojekter i <a href="/projekter/traeterrasse-trykimpraegneret-hundested/">Hundested</a> og <a href="/projekter/jatoba-terrasse-liseleje/">Liseleje</a>, eller læs mere om <a href="/terrasse/">terrasser</a>.')),
             ("Kan I lave siddebænke og trædæk til offentlige institutioner?", "Ja, projektet ved Melby Skole er et eksempel."),
         ]),
    # Case 4. Afklaret af Christian: samme hus foer og efter, kunden er indforstaaet med billederne, og vinduer, doere,
    # indfatninger og tag blev ikke skiftet. Beklaedningens traesort kendes ikke: kun "traebeklaedning". Ingen anmeldelse.
    dict(slug="efterisolering-facadebeklaedning-sommerhus-melby", status="live", ydelse="renovering", by="Melby", aar="2023",
         titel="Efterisolering og ny facadebeklædning af sommerhus, Melby",
         krumme="Efterisolering og ny facade, Melby",
         kort="Efterisolering og ny facade, Melby", undertekst="Sommerhus, 2023", tag="Renovering",
         link_tekst="efterisolering og ny facade i Melby",
         title="Efterisolering og ny facade på sommerhus, Melby | Rosendal",
         desc="Efterisolering og ny facadebeklædning af sommerhus i Melby i 2023. Ny trækonstruktion uden på den eksisterende. Rosendal Tømrer, Nordsjælland.",
         svar="Vi har i 2023 efterisoleret et sommerhus i Melby og sat ny facadebeklædning op. Vi byggede en ny trækonstruktion uden på den eksisterende væg, isolerede i konstruktionen og afsluttede med ny beklædning. Huset fik dermed både et nyt udtryk og en bedre isoleret facade.",
         fakta=[("Projekt", "Efterisolering og ny facadebeklædning"), ("Bygning", "Sommerhus"), ("Sted", "Melby"), ("År", "2023"),
                ("Beklædning", None), ("Isolering", None), ("Areal", None), ("Tidsforbrug", None)],   # None = afventer Sebastian
         anmeldt=None, citat=None, udvidet=None,   # ingen anmeldelse, og der vises ingen fra andre projekter
         billeder=[   # hovedbilledet er efterbilledet 03. Foer/efter-afsnittet bruger numrene herunder
             ("sommerhus-efterisoleret-ny-facadebeklaedning-melby-03", "Efterisoleret sommerhus med ny lys facadebeklædning i træ, Melby", "Efter: ny facade, Melby 2023"),
             ("sommerhus-facade-foer-renovering-melby-01", "Rødmalet sommerhus med bræddeklædning før efterisolering og ny facade, Melby", "Før: den oprindelige facade"),
             ("sommerhus-gavl-foer-renovering-melby-02", "Gavl på rødmalet sommerhus før renovering af facaden, Melby", "Før: gavlen"),
             ("sommerhus-ny-facadebeklaedning-gavl-melby-04", "Gavl og langside på sommerhus med ny træbeklædning, Melby", "Efter: gavl og langside"),
             ("sommerhus-ny-facadebeklaedning-indgang-melby-05", "Indgangsside på sommerhus med ny facadebeklædning og hvid dør, Melby", "Efter: indgangssiden"),
         ],
         foer_efter=dict(kolonner=[("Før", [1, 2]), ("Efter", [3, 4])],
                         tekst="Før havde sommerhuset en rødmalet bræddeklædning. Efter har det fået ny, lys træbeklædning og ny facade hele vejen rundt."),
         og_img="images/og-efterisolering-facadebeklaedning-sommerhus-melby.jpg",
         sek=[
             ("Opgaven", ["I 2023 efterisolerede vi et sommerhus i Melby og satte ny facadebeklædning op. Før renoveringen havde huset en rødmalet bræddeklædning. Vi byggede en ny trækonstruktion uden på den eksisterende væg, efterisolerede i den nye konstruktion og afsluttede med ny træbeklædning."]),
             ("Sådan foregår udvendig efterisolering", ["Ved udvendig efterisolering bygges en ny konstruktion uden på den gamle væg. Hulrummet i den nye konstruktion isoleres, og facaden afsluttes med ny beklædning. Fordi arbejdet foregår udefra, kan rummene indenfor bevares uændrede, mens husets udseende ændrer sig."]),
             ("Sådan blev opgaven udført i detaljer", None),   # materiale, isolering, vindspaerre og ventilation, afventer Sebastian
         ],
         sek_efter=[
             ("Skal dit hus efterisoleres?", ('html', f'<p>Vi efterisolerer og renoverer huse og sommerhuse. Læs mere om <a href="/renovering/">renovering</a>, og se <a href="/omrader/">hvor vi kører</a>. Ring på <a href="tel:{TLF_RAW}">{TLF}</a> eller <a href="/kontakt/" data-cta="projekt-tekst">skriv til os</a>, så aftaler vi en besigtigelse og giver dig et skriftligt tilbud.</p>')),
         ],
         faq=[
             ("Hvad betyder det at efterisolere udvendigt?", "Der bygges en ny konstruktion uden på den eksisterende væg. Den isoleres, og facaden får ny beklædning."),
             ("Hvad er forskellen på at efterisolere ude og inde?", "Udvendig efterisolering ændrer husets udseende, mens rummene indenfor bevares uændrede. Ved indvendig efterisolering bevares facaden, og isoleringen bygges på indersiden af væggene."),
             ("Udfører I efterisolering og facadebeklædning af sommerhuse?", ('html', 'Ja, projektet i Melby i 2023 er et eksempel. <a href="/kontakt/" data-cta="projekt-faq">Kontakt os</a>, hvis du vil høre, hvad vi kan gøre ved dit hus.')),
             ("Hvor udfører I renoveringsopgaver?", ('html', f'Vores arbejdsområde går {ARBEJDSOMRAADE}. Se mere på siden om <a href="/omrader/">områder</a>.')),
         ]),
    # Case 5. Afklaret af Christian: kunden er indforstaaet med billederne, og anmeldelseslinket aabner den rigtige anmeldelse.
    # Tagsten og antal velux-vinduer kendes ikke. Producentens egen beskrivelse af Hardie Plank er ikke tjekket, saa der
    # staar kun "fibercement" og "begraense vedligeholdelsen", aldrig "vedligeholdelsesfri".
    # Adressen er kendt internt, men maa ikke staa nogen steder: hverken i tekst, filnavne, alt-tekster eller her.
    dict(slug="nyt-tegltag-hundested", status="live", ydelse="tag", by="Hundested", aar="2026",
         titel="Nyt tegltag med velux-vinduer og nye vindskeder, Hundested",
         krumme="Nyt tegltag, Hundested",
         kort="Nyt tegltag, Hundested", undertekst="Tag, velux og vindskeder, 2026", tag="Tag",
         link_tekst="nyt tegltag i Hundested",
         title="Nyt tegltag med velux og vindskeder, Hundested | Rosendal",
         desc="Nyt tegltag, nye velux-vinduer og vindskeder i Hardie Plank udført i Hundested i 2026. Se projektet fra Rosendal Tømrer.",
         svar="Vi har i 2026 lagt nyt tegltag på et hus i Hundested. Samtidig satte vi nye velux-vinduer i, monterede flere og skiftede vindskederne til Hardie Plank. Taget blev udført fra stillads, og huset fik et helt nyt udtryk.",
         fakta=[("Projekt", "Nyt tegltag"), ("Bygning", "Parcelhus"), ("Sted", "Hundested"), ("År", "2026"),
                ("Udført", "Nyt tegltag, nye velux-vinduer (og flere monteret), nye vindskeder i Hardie Plank"),
                ("Tagsten", None), ("Velux-vinduer", None), ("Areal", None), ("Tidsforbrug", None)],   # None = afventer Sebastian
         # Kundens tekst med tastefejlen "Rigtige" rettet til "Rigtig" (som i ANMELDELSER["kenneth"])
         citat="Vi har fået lagt et nyt tegltag. Alt er forløbet som vi havde håbet og forventet. Rigtig flinke og flittige håndværkere.",
         anmeldt=("oktober 2026", "Anmeld Håndværker"), anm_opgave="Udvendigt", udvidet=None,
         anm_url=ANM_RID_URL.format(rid=2145085),   # dekodet fra Facebooks delingslink, testet af Christian 26-10-2026
         karakterer="5,0 på Anmeld Håndværker.",
         billeder=[
             ("nyt-tegltag-med-velux-vinduer-hundested-01", "Nyt mørkt tegltag med nye velux-vinduer og nye vindskeder på hus i Hundested", "Efter: nyt tag, Hundested 2026"),
             ("tegltag-under-udskiftning-stillads-hundested-02", "Hus i Hundested med stillads og afdækning under udskiftning af tegltaget", "Under: stillads og afdækning"),
             ("gammelt-tegltag-foer-udskiftning-hundested-03", "Ældre tegltag med to velux-vinduer og tagstige før udskiftning, Hundested", "Før: det gamle tag"),
         ],
         # Der er kun ét efterbillede, saa hovedbilledet staar ogsaa sidst i raekken, med sin egen alt-tekst
         foer_efter=dict(h2="Før, under og efter", kolonner=[("Før", [2]), ("Under", [1]), ("Efter", [(0, "Det nye tegltag i Hundested set fra haven efter udskiftningen")])],
                         tekst="Før havde huset et ældre, mørkt tegltag med velux-vinduer og en tagstige. Under udskiftningen stod huset i stillads med afdækning. Efter har det fået et nyt, mørkt tegltag med flere velux-vinduer og nye vindskeder."),
         og_img="images/og-nyt-tegltag-hundested.jpg",
         sek=[
             ("Opgaven", ["I 2026 lagde vi nyt tegltag på et parcelhus i Hundested. Samtidig satte vi nye velux-vinduer i, monterede flere og skiftede vindskederne til Hardie Plank. Arbejdet blev udført fra stillads."]),
             ("Nye vindskeder i Hardie Plank", ["Hardie Plank er fibercement. Vi valgte fibercement til vindskederne for at begrænse vedligeholdelsen."]),
             ("Tagsten, velux-vinduer og undertag", None),   # afventer Sebastian
         ],
         sek_efter=[
             ("Skal dit tag skiftes?", ('html', f'<p>Læs mere om <a href="/tag/">nyt tag og tagrenovering</a> og om <a href="/tomrer-hundested/">tømrer i Hundested</a>. Ring på <a href="tel:{TLF_RAW}">{TLF}</a> eller <a href="/kontakt/" data-cta="projekt-tekst">skriv til os</a>, så aftaler vi en besigtigelse og giver dig et skriftligt tilbud.</p>')),
         ],
         faq=[
             ("Udfører I udskiftning af tegltag?", ('html', 'Ja, projektet i Hundested i 2026 er et eksempel. <a href="/kontakt/" data-cta="projekt-faq">Kontakt os</a>, hvis dit tag skal skiftes.')),
             ("Kan I også montere nye velux-vinduer i forbindelse med tagudskiftning?", "Ja, i dette projekt satte vi nye velux-vinduer i og monterede flere."),
             ("Hvad er Hardie Plank?", "Hardie Plank er planker af fibercement."),
             ("Hvor udfører I tagopgaver?", ('html', f'Vores arbejdsområde går {ARBEJDSOMRAADE}. Se mere på siden om <a href="/omrader/">områder</a>.')),
         ]),
    dict(slug="sommerhus-nyt-tag", titel="Sommerhusrenovering med nyt tag", by="Hundested", maaned="februar 2026", ydelse="renovering", anm="brian", status="pending", billeder=[]),
    dict(slug="tilbygning-gaestehus", titel="Tilbygning og gæstehus", by="Hundested", maaned="november 2025", ydelse="tilbygning", anm="rita", status="pending", billeder=[]),
    dict(slug="repos-trappe-ipe", titel="Repos-trappe i ipé", by="Veksø", maaned="juli 2026", ydelse="terrasse", anm="morten", status="pending", billeder=[]),
    dict(slug="vinduer-og-franske-altaner", titel="Nye vinduer og to franske altaner", by="Hundested", maaned="august 2026", ydelse="vinduer", anm="peter", status="pending", billeder=[]),
    dict(slug="facadebeklaedning-og-isolering", titel="Facadebeklædning og isolering", by="Ølsted", maaned="september 2025", ydelse="renovering", anm="hanne", status="pending", billeder=[]),
    dict(slug="doere-og-vinduer-vejby", titel="Nye døre og vinduer i Vejby", by="Vejby", maaned="april 2026", ydelse="doere", anm="anita", status="pending", billeder=[]),
]
LIVE = [p for p in PROJEKTER if p["status"] == "live"]
# "Vores projekter" er sit eget afsnit i Ydelser-menuen med oversigten /projekter/ og et underpunkt pr. case
# (Christian 23-10-2026, afloeser reglen om tidligst at vise oversigten ved 3 cases).
HUB = bool(LIVE)
S.STATE["projekter"] = [(p["slug"], p["link_tekst"][0].upper() + p["link_tekst"][1:]) for p in LIVE]   # korte navne i menuen
PROJ_KRUMME = "projekter"

def proj_billede(p, n=0, bredde="720"):
    return f'/images/projekter/{p["billeder"][n][0]}{"" if bredde == "1440" else "-720"}.webp'

def proj_links(ydelse=None, by=None):
    """'Se et projekt: ...' til ydelses- og omraadesiderne."""
    ps = [p for p in LIVE if (ydelse is None or p["ydelse"] == ydelse) and (by is None or p["by"] == by)]
    return "".join(f'<p><a href="/projekter/{p["slug"]}/" style="text-decoration:underline">Se et projekt: {e(p["link_tekst"])}</a></p>' for p in ps)

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
    "tag": "Nyt tag, tegltag, tagrenovering og efterisolering.",
    "vinduer": "Vinduer i træ og træ/alu, målt op, leveret og monteret.",
    "doere": "Hoveddøre, terrassedøre, foldedøre og franske altaner.",
    "terrasse": "Træterrasser, repos og trappetrin, gerne i ipé.",
    "renovering": "Vægge, gulve, lofter, isolering og facader, også i sommerhuse.",
    "nybyg": "Nye huse, gæstehuse, anneks, carporte og garager.",
    "pergola-hegn-og-cykelskur": "Pergolaer, hegn, cykelskure og bænke til private og erhverv.",
    "materieludlejning": "Lej stillads, betonblander, affugter, dumper, pælebor og værktøj i Hundested.",
}

def svc_grid():
    out = ['<div class="svc-grid">',
           f'<a class="svc svc-feature" href="{url("hovedentreprise")}">{HEX}<h3>Hovedentreprise</h3>'
           '<p>Vi styrer hele byggeriet og koordinerer murer, elektriker, VVS og maler. Én kontrakt, én kontakt og ét ansvar fra start til aflevering.</p>'
           '<span class="svc-go">Læs om hovedentreprise</span></a>']
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
    <h1>Godt håndværk og aftaler, du kan regne med</h1>
    <p class="lead">Tømrerfirma i Hundested. Vi hjælper private og erhverv i Nordsjælland med alt fra nye vinduer og træterrasser til renoveringer, tilbygninger og hele byggerier. Sebastian er din faste kontaktperson, og vi er et fast hold af tømrere.</p>
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
    <p>Vi tager os af både de mindre opgaver og de større byggeprojekter. Det kan være alt fra en ny terrassedør til en tilbygning eller en gennemgribende renovering, hvor vi også koordinerer de øvrige håndværkere. Små opgaver som fx dørskift samler vi og tager flere ad gangen.</p>
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
  <p>Vi kører fra værksted og kontor på Engdraget 11 i Hundested. Vores arbejdsområde går {ARBEJDSOMRAADE}, og opgaver længere væk tager vi også imod. Her er de områder, vi dækker.</p>
  {omr_chips()}
  <p><a href="/omrader/" style="text-decoration:underline">Se alle områder</a></p>
</div></section>
{some()}
{cta()}
"""
side("index", "Tømrer i Hundested og Nordsjælland | Rosendal Tømrer",
     "Tømrermester og bygningskonstruktør i Hundested. Tilbygning, tag, vinduer, terrasser og hovedentreprise i Nordsjælland. Ring 50 70 05 05.",
     forside, schemas=[schema_virksomhed()], extra_js=AH_BADGE_JS + "\n" + AH_SLIDER_JS + "\n" + AH_BADGE_HOEJDE_JS)

# ---------------- YDELSESSIDER ----------------
def sidebar(aktiv):
    li = "".join(f'<li><a href="{url(sl)}"{" class=\"active\"" if sl == aktiv else ""}>{e(n)}</a></li>' for sl, n in YDELSER)
    return (f'<aside class="side"><ul class="side-nav">{li}</ul>'
            f'<div class="side-cta"><h2>Kontakt os i dag</h2><p>Tømrerarbejde i Hundested. Vi dækker hele {OMRAADE}.</p>'
            f'<a class="btn btn-brass" href="tel:{TLF_RAW}">{ICON_TLF}{TLF}</a><a class="side-link" href="/kontakt/" data-cta="sidebar">Skriv til os</a></div></aside>')

def liste(items):
    return "<ul>" + "".join(f'<li><a href="{url(x[1])}">{e(x[0])}</a></li>' if isinstance(x, tuple) else f"<li>{e(x)}</li>" for x in items) + "</ul>"

OMR_VERB = {"hovedentreprise": "styrer byggerier", "tilbygning": "bygger til huse", "tag": "skifter tage",
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
    blokke.append(proj_links(ydelse=slug))
    blokke.append(rev_mini(d["anm"]))
    if slug in MATERIEL_LINKS:
        # Interne links til de maskiner, der passer til opgaven (og fra udlejningssiden tilbage hertil)
        kald = {"paelebor": "pælebor", "jordbor": "mobilt jordbor", "affugter": "affugter", "gipshejs": "gipshejs",
                "betonblander": "betonblander", "dumper": "dumper", "rullestillads": "rullestillads"}
        ml = [f'<a href="/materieludlejning/#{i}">{kald[i]}</a>' for i in MATERIEL_LINKS[slug]]
        blokke.append(f'<h2>Lav noget af det selv?</h2><p>Vil du selv tage fat, kan du leje {", ".join(ml[:-1])} og {ml[-1]} hos os i Hundested. '
                      'Ring for pris, eller læs mere under <a href="/materieludlejning/">materieludlejning</a>.</p>')
    blokke.append(f'<h2>Områder vi dækker</h2><p>Vi {OMR_VERB[slug]} i Hundested og resten af Nordsjælland. Arbejdsområdet går {ARBEJDSOMRAADE}, og opgaver længere væk tager vi også imod. '
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
# Alt indhold staar som tekst i HTML (ingen faner eller skjult indhold), saa soegemaskiner og AI kan citere maal og specs.
# Ingen priser og ingen offers i schema, foer Sebastian har krydstjekket dem med Stark (moedet 23-10-2026).
AFHENTNING = f"{ADR}, {POST} {BY}"

def maskine_kort(m):
    mid, _, navn, tekst, specs = m
    pris = '<p class="m-pris"><strong>Kontakt os for pris</strong></p>'
    return (f'<article class="maskine" id="{mid}"><img src="/images/materiel/{mid}.svg" alt="{e(navn)} til leje i Hundested" width="480" height="360" loading="lazy">'
            f'<div class="m-krop"><h3>{e(navn)}</h3><p>{e(tekst)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in specs)}</ul>{pris}'
            f'<a class="btn btn-brass" href="tel:{TLF_RAW}" data-cta="materiel-{mid}">{ICON_TLF}Ring og book {TLF}</a></div></article>')

def schema_materiel():
    elementer = []
    for i, (mid, _, navn, tekst, specs) in enumerate(MATERIEL):
        p = {"@type": "Product", "name": navn, "description": tekst + " " + ". ".join(specs) + ".",
             "image": f"{DOMAIN}/images/materiel/{mid}.svg", "url": f"{DOMAIN}/materieludlejning/#{mid}"}
        elementer.append({"@type": "ListItem", "position": i + 1, "item": p})
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "Materiel til leje hos " + NAVN, "itemListElement": elementer}

def schema_udlejning(navn, desc):
    # Udlejningsadressen er ogsaa virksomhedens adresse, men skrives ud her, saa afhentningsstedet staar i schema.
    s = schema_service(navn, desc, "materieludlejning")
    s["availableChannel"] = {"@type": "ServiceChannel", "name": "Afhentning",
                             "servicePhone": TLF_RAW,
                             "serviceLocation": {"@type": "Place", "name": "Afhentning af lejet materiel",
                                                 "address": {"@type": "PostalAddress", "streetAddress": ADR, "postalCode": POST,
                                                             "addressLocality": BY, "addressCountry": "DK"}}}
    return s

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
  <dl class="fakta"><dt>Afhentning</dt><dd>{AFHENTNING}, efter aftale</dd><dt>Pris</dt><dd>Kontakt os for pris: <a href="tel:{TLF_RAW}">{TLF}</a></dd>
    <dt>Åbningstid</dt><dd>{AABNING}</dd></dl>
  <nav class="m-hurtig" aria-label="Kategorier">{hurtig}</nav>
  {sektioner}
  <p class="m-note">Materiellet lejes pr. kalenderdag. Kontakt os for pris på {TLF}. Læs de fulde <a href="/lejebetingelser/">lejebetingelser</a>, før du lejer.</p>
  <h2>Sådan lejer du</h2>{trin}
  <h2>Skal vi hellere lave opgaven?</h2>
  <p>Vi er tømrere og bygger det, vi udlejer materiel til. Læs om {tilbage}.</p>
  <h2>Ofte stillede spørgsmål</h2><div class="faq">{faq}</div>
</div></section>
{cta("Skal du bruge noget af det?", f"Ring og hør, om det er ledigt. Vi dækker hele {OMRAADE}.")}"""
    side("materieludlejning", d["title"], d["desc"], body, active="materieludlejning",
         schemas=[schema_udlejning(navn, d["desc"]), faq_schema(d["faq"]), schema_materiel()],
         krummer=[(navn, None)])

materiel_side()

# ---------------- OM OS ----------------
fakta = [("Firmanavn", NAVN), ("CVR", CVR), ("Adresse", f"{ADR}, {POST} {BY} (værksted og kontor)"), ("Telefon", f'<a href="tel:{TLF_RAW}">{TLF}</a>'),
         ("E-mail", f'<a href="mailto:{MAIL}">{MAIL}</a>'), ("Åbningstid", AABNING), ("Stiftet", "2021 af Sebastian Rosendal"),
         ("Ansatte", str(ANSATTE)), ("Medlem af", "Dansk Håndværk"),
         ("Arbejdsområde", f"{ARBEJDSOMRAADE[0].upper()}{ARBEJDSOMRAADE[1:]}. Opgaver længere væk tager vi også imod"), ("Svartid", "Inden for 24 timer på hverdage"),
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
  <p>Sebastian blev uddannet tømrer i 2010 og bygningskonstruktør i 2018. I dag er han tømrermester, og i 2021 stiftede han Rosendal Tømrer Entreprise. Han er den, du taler med fra den første snak til det færdige resultat. Når der er brug for at tænke et projekt igennem, før det bygges, kommer begge uddannelser i spil.</p>
  {SIGNATUR}
  <h2>Rådgivning ud fra din opgave</h2>
  <div class="proj-citat"><blockquote>Jeg anbefaler ud fra den enkelte opgave: hvor den ligger, og hvilke forhold den skal stå i. Ligger en terrasse tæt på vandet, fraråder jeg blødt træ, fordi det holder dårligere der. Flere kunder vil også gerne væk fra trykimprægneret, og det tager vi med i snakken. Du skal føle dig godt rådgivet, før du vælger.</blockquote>
  <p>Sebastian Rosendal</p></div>
  <h2>Holdet</h2>
  <p>Vi er {ANSATTE} ansatte og et fast hold af tømrere. Kunderne omtaler vores svende som dygtige og venlige, og det er den måde, vi vil arbejde på. Du får besøg af folk, der kender opgaven, og som tager godt imod dine spørgsmål undervejs. Vi søger løbende tømrersvende, så er du interesseret i at blive en del af holdet, kan du læse mere under <a href="/job/">job</a>.</p>
  <h2>Sådan arbejder vi</h2>
  <p>Du har én fast kontaktperson. Du får et skriftligt tilbud, så du ved, hvad der er aftalt, og hvis der opstår noget uventet undervejs, tager vi dialogen med dig, inden vi går videre. Vi arbejder i dit hjem, og det tager vi alvorligt: Vi rydder op efter os og gør os umage for at gøre byggeperioden så overskuelig som muligt.</p>
  <p>Vi laver alt i Hundested og omegn, også reparationer og små opgaver. Små opgaver som fx dørskift samler vi og tager flere ad gangen.</p>
  <p>Mange af opgaverne involverer flere fag. Vi har faste samarbejdspartnere inden for murer, el, VVS, maler og kloak og kan tage hele projektet som <a href="/hovedentreprise/">hovedentreprise</a>, så du kun har én kontakt.</p>
  <h2>Medlem af Dansk Håndværk</h2>
  <p>Vi er medlem af Dansk Håndværk. For vores medarbejdere betyder medlemskabet overenskomst. For dig som kunde er det et garantistempel.</p>
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
  <p>Vi kører fra værksted og kontor på Engdraget 11 i Hundested. Arbejdsområdet går {ARBEJDSOMRAADE}.</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container narrow prose">
  <div class="svar"><strong>Kort svar</strong>Rosendal Tømrer Entreprise har base i Hundested. Vores arbejdsområde går {ARBEJDSOMRAADE}, med Frederiksværk, Hillerød, Helsinge, Gilleleje og sommerhusområderne langs Nordkysten imellem. Opgaver længere væk tager vi også imod. Ring på {TLF}, så finder vi ud af, hvordan vi kan hjælpe.</div>
  <h2>Her kører vi</h2>
  {omr_chips()}
  <p>Hundested har sin egen side, hvor du kan se opgaver fra byen: <a href="/tomrer-hundested/">tømrer i Hundested</a>.</p>
  {proj_links()}
  <h2>Hvor vi har løst opgaver</h2>
  <p>Kunderne fortæller selv, hvor og hvad vi har lavet. Vi har blandt andet løst opgaver i Hundested, Frederiksværk, Ølsted, Hillerød, Liseleje og Vejby: tag, vinduer og døre, terrasser, facade og renoveringer. Læs deres anmeldelser under <a href="/anmeldelser/">anmeldelser</a>.</p>
  <h2>Ligger din opgave længere væk?</h2>
  <p>Opgaver uden for arbejdsområdet tager vi også imod. Ring og fortæl, hvor opgaven ligger, og hvad den går ud på.</p>
  <h2>Det laver vi i hele området</h2>
  {liste([(n, sl) for sl, n in YDELSER])}
</div></section>
{cta()}"""
side("omrader", "Områder vi dækker i Nordsjælland | Rosendal Tømrer",
     "Rosendal Tømrer i Hundested tager tømrerarbejde fra Hundested til Frederikssund, Stenløse, Farum og Hørsholm. Ring 50 70 05 05.",
     omr, schemas=[schema_virksomhed()], krummer=[("Områder", None)])

hund_faq = [
    ("Har I værksted i Hundested?", f"Ja. Vi har værksted og kontor på {ADR}, {POST} {BY}."),
    ("Hvilke områder omkring Hundested kører I til?", f"Arbejdsområdet går {ARBEJDSOMRAADE}, blandt andet Frederiksværk, Ølsted, Lynæs, Hillerød, Helsinge, Gilleleje og sommerhusområderne langs Nordkysten. Opgaver længere væk tager vi også imod."),
    ("Tager I også små opgaver i Hundested?", "Ja. Vi laver alt i Hundested og omegn, også reparationer og små opgaver. Små opgaver som fx dørskift samler vi og tager flere ad gangen."),
    ("Hvordan får jeg et tilbud i Hundested?", f"Ring på {TLF} på hverdage mellem 07.00 og 16.00, eller send en henvendelse. Vi kommer ud og ser på opgaven og giver et fast skriftligt tilbud."),
    ("Hvor hurtigt svarer I?", "Vi vender tilbage inden for 24 timer på hverdage."),
    ("Kan jeg leje stillads i Hundested?", "Ja. Rullestillads, bukkestillads og andet materiel kan hentes på Engdraget 11 efter aftale. Kontakt os for pris."),
]
hund = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Områder", "omrader"), ("Tømrer i Hundested", None)])}
  <h1>Tømrer i Hundested</h1>
  <p>Rosendal Tømrer Entreprise har værksted og kontor på Engdraget 11 i Hundested. Vi tager tag, vinduer, døre, terrasser, tilbygninger og renoveringer i Hundested og omegn.</p>
  {hero_knapper()}
</div></section>
<section class="sec"><div class="container narrow prose">
  <div class="svar"><strong>Kort svar</strong>Rosendal Tømrer Entreprise er et tømrerfirma i Hundested, stiftet i 2021 af tømrermester og bygningskonstruktør Sebastian Rosendal. Vi har værksted og kontor på Engdraget 11 og tager tag, vinduer, døre, terrasser, tilbygninger og renoveringer. Ring på {TLF} på hverdage 07.00 til 16.00.</div>
  <h2>Vi har base i Hundested</h2>
  <p>Det er herfra, vi kører ud til opgaverne, og det er her, du kan hente stillads og værktøj, hvis du vil <a href="/materieludlejning/">leje materiel</a>. Du ringer til Sebastian og får en fast kontaktperson, der kender dit projekt fra første snak til aflevering.</p>
  <h2>Opgaver vi har løst i Hundested</h2>
  <p>Kunderne fortæller selv, hvordan det er gået. Her er et udpluk fra Hundested.</p>
  <div class="rev-mini">{rev_kort('kenneth')}{rev_kort('peter')}{rev_kort('brian')}</div>
  <p>Hundestedkunderne har blandt andet også fået en tilbygning og et gæstehus (november 2025), beklædning på vægge og loft samt altan i et sommerhus (august 2025), nyt tag og skillevæg (september 2025) og nyt tag (august 2025). <a href="/anmeldelser/">Læs flere anmeldelser</a>.</p>
  {proj_links(by="Hundested")}
  <h2>De mest relevante ydelser i Hundested</h2>
  {liste([("Tag: nyt tag og tagrenovering", "tag"), ("Vinduer: nye vinduer og vinduesudskiftning", "vinduer"), ("Tilbygning: mere plads til huset", "tilbygning"), ("Renovering af hus og sommerhus", "renovering"), ("Terrasse: træterrasser og trappetrin", "terrasse")])}
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

def proj_kort():
    return "".join(f'<a class="ref-card" href="/projekter/{p["slug"]}/"><div class="ref-card-media"><img src="{proj_billede(p)}" alt="{e(p["billeder"][0][1])}" width="720" height="540" loading="lazy"></div>'
                   f'<div class="ref-card-body">{f"""<span class="ref-tag">{e(p["tag"])}</span>""" if p.get("tag") else ""}<h3>{e(p["kort"])}</h3>'
                   f'<p>{e(p.get("undertekst") or p["by"] + " · " + p["aar"])}</p></div></a>' for p in LIVE)

ref_body = f"""
<section class="page-header"><div class="container">
  {crumb_html([("Anmeldelser", None)])}
  <h1>Anmeldelser fra vores kunder</h1>
  <p>Vi er stolte af at have {ANM_SNIT} i gennemsnit på Anmeld Håndværker. Her kan du læse, hvad vores kunder skriver om os.</p>
</div></section>
<section class="sec sec-mist"><div class="container">
  <div class="sec-head" style="margin:0"><h2>Anmeldelser fra Anmeld Håndværker</h2><p>Kommunikation, aftaler, pris, tilfredshed og oprydning. Listen opdateres automatisk.</p></div>
  <div class="ah-widget">{AH_LISTE_DIV}</div>
  <div class="rev-links"><a href="{ANM_URL}" target="_blank" rel="noopener">Læs alle anmeldelser på Anmeld Håndværker</a></div>
</div></section>
{some()}
{cta()}"""
side("anmeldelser", "Anmeldelser fra kunder | Rosendal Tømrer",
     "Læs anmeldelser fra vores kunder på Anmeld Håndværker. Tag, vinduer, terrasser, tilbygning og renovering i Hundested og Nordsjælland.",
     ref_body, schemas=[schema_virksomhed()], krummer=[("Anmeldelser", None)], extra_js=AH_LISTE_JS)

# ---------------- PROJEKTSIDER (kun naar status = live) ----------------
# Ingen Review- eller aggregateRating-markup: citatet er fra Anmeld Haandvaerker og vises kun som tekst.
# ---------------- ANMELDELSE PAA EN CASE ----------------
# Link til den enkelte anmeldelse: ANM_RID_URL i site_shared.py. Mangler id'et, linkes til profilen.

def anm_link(url):
    """Delingslinks fra Facebook (facebook.com/sharer/...?u=<url>) maa ikke bruges som href. Brug den dekodede u-parameter."""
    from urllib.parse import urlparse, parse_qs
    if url and "facebook.com/sharer" in url:
        return parse_qs(urlparse(url).query).get("u", [ANM_URL])[0]
    return url or ANM_URL

def anmeldelse_html(tekst, byline, dato, opgave, url):
    """Faelles anmeldelsesboks. Synlig tekst, ingen navne, ingen Review- eller aggregateRating-markup."""
    linje = " · ".join(e(x) for x in (byline, opgave, dato) if x)
    return (f'<div class="proj-citat"><blockquote>{e(tekst)}</blockquote>'
            f'<p>{linje}. <a href="{e(anm_link(url))}" target="_blank" rel="noopener noreferrer" data-cta="anmeldelse_link">Anmeldelse på Anmeld Håndværker</a></p></div>')

def schema_webside(p):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": p["titel"], "description": p["desc"],
            "url": f'{DOMAIN}/projekter/{p["slug"]}/', "inLanguage": "da-DK",
            "primaryImageOfPage": f'{DOMAIN}/images/projekter/{p["billeder"][0][0]}.webp',
            "isPartOf": {"@type": "WebSite", "url": DOMAIN + "/", "name": NAVN},
            "about": {"@id": DOMAIN + "/#virksomhed"}}

def projekt_side(p):
    krummer = [("Vores projekter", PROJ_KRUMME), (p.get("krumme") or p["titel"], None)]
    fakta = [(k, v) for k, v in p["fakta"] if v]
    if p.get("anmeldt"):   # cases uden anmeldelse udelader baade faktalinjen og afsnittet "Det siger kunden"
        fakta.append(("Anmeldt", f'{p["anmeldt"][0]} på <a href="{e(anm_link(p.get("anm_url")))}" target="_blank" rel="noopener noreferrer">{p["anmeldt"][1]}</a>'))
    fakta.append(("Udført af", NAVN))
    dl = "".join(f"<dt>{e(k)}</dt><dd>{v if '<a' in v else e(v)}</dd>" for k, v in fakta)

    def figur(i, cls="", alt=None):
        fil, alt0, tekst, *maal = p["billeder"][i]
        alt = alt or alt0
        b, h = maal[0] if maal else (1440, 1080)   # stort billede; et billede paa hoejkant faar sine egne maal
        img = (f'<img src="/images/projekter/{fil}.webp" srcset="/images/projekter/{fil}-720.webp 720w, /images/projekter/{fil}.webp {b}w" '
               f'sizes="{"(max-width:820px) 100vw, 780px" if cls else "(max-width:600px) 100vw, 390px"}" alt="{e(alt)}" width="{b}" height="{h}"'
               + (' fetchpriority="high"' if cls else ' loading="lazy"') + ' data-lb>')   # cls = hovedbilledet oeverst
        return f'<figure{cls}>{img}' + (f"<figcaption>{e(tekst)}</figcaption>" if tekst else "") + "</figure>"

    def sektioner(liste):
        ud = ""
        for h2, c in liste:
            if not c: continue          # tom sektion afventer Sebastian
            ud += f"<h2>{e(h2)}</h2>" + (c[1] if isinstance(c, tuple) else "".join(f"<p>{e(x)}</p>" for x in c))
        return ud

    # Valgfrit foer/efter-afsnit: kolonner = [(overskrift, [numre i billeder])]. De billeder vises ikke ogsaa i galleriet.
    # Et nummer kan vaere (nummer, anden alt-tekst), naar hovedbilledet ogsaa skal staa i raekken (alt-teksten skal vaere unik).
    fe = p.get("foer_efter")
    fe_html, brugt = "", set()
    if fe:
        nr = lambda x: x[0] if isinstance(x, tuple) else x
        brugt = {nr(x) for _, xs in fe["kolonner"] for x in xs}
        kol = "".join(f'<div><h3>{e(h)}</h3>{"".join(figur(nr(x), alt=x[1] if isinstance(x, tuple) else None) for x in xs)}</div>'
                      for h, xs in fe["kolonner"])
        fe_html = (f'<h2>{e(fe.get("h2", "Før og efter"))}</h2><p>{e(fe["tekst"])}</p>'
                   f'<div class="foer-efter" style="--kol:{len(fe["kolonner"])}">{kol}</div>')
    galleri = "".join(figur(i) for i in range(1, len(p["billeder"])) if i not in brugt)
    andre = "".join(f'<li><a href="/projekter/{q["slug"]}/">{e(q["kort"])}, {e(q["by"])}</a></li>' for q in LIVE if q is not p)
    andre = f"<h2>Andre projekter</h2><ul>{andre}</ul>" if andre else ""
    udvidet = f'<p>{e(p["udvidet"])}</p>' if p.get("udvidet") else ""
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{faq_html(a)}</p></details>" for q, a in p["faq"])
    kunde = ""
    if p.get("citat"):
        kunde = ("<h2>Det siger kunden</h2>"
                 + anmeldelse_html(p["citat"], f'Kunde i {p["by"]}', f'anmeldt {p["anmeldt"][0]}', p.get("anm_opgave"), p.get("anm_url"))
                 + f'{udvidet}<p>{e(p["karakterer"])}</p>')
    body = f"""
<section class="page-header"><div class="container">
  {crumb_html(krummer)}
  <h1>{e(p['titel'])}</h1><p>{e(p['by'])} · {e(p['aar'])}</p>
  {hero_knapper("projekt")}
</div></section>
<section class="sec"><div class="container narrow prose">
  <div class="svar"><strong>Kort svar</strong>{e(p['svar'])}</div>
  {figur(0, ' class="proj-hoved"')}
  <dl class="fakta">{dl}</dl>
  {sektioner(p['sek'])}
  {fe_html}
  {f'<div class="proj-gallery">{galleri}</div>' if galleri else ''}
  {kunde}
  {sektioner(p['sek_efter'])}
  {andre}
  <h2>Ofte stillede spørgsmål</h2><div class="faq">{faq}</div>
</div></section>
{cta()}"""
    side(f"projekter/{p['slug']}", p["title"], p["desc"], body, active=f"projekter/{p['slug']}", og_img=p["og_img"],
         schemas=[schema_webside(p), faq_schema(p["faq"])], extra_js=LB_JS, krummer=krummer)

for p in LIVE:
    projekt_side(p)
if HUB:
    side("projekter", "Vores projekter | Rosendal Tømrer", "Se udvalgte projekter fra Rosendal Tømrer i Hundested og Nordsjælland med billeder af det færdige resultat og fakta om opgaven.",
         f'<section class="page-header"><div class="container">{crumb_html([("Vores projekter", None)])}<h1>Vores projekter</h1>'
         f'<p>Udvalgte opgaver med billeder af det færdige resultat og fakta om opgaven.</p>{hero_knapper("projekter")}</div></section>'
         f'<section class="sec"><div class="container"><div class="refs-grid">{proj_kort()}</div></div></section>{cta()}',
         active="projekter", krummer=[("Vores projekter", None)])

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
  <p>Vi søger løbende tømrersvende til holdet, og vi tager altid imod ansøgninger.</p>
</div></section>
<section class="sec"><div class="container contact-grid">
  <div class="prose">
    <img class="job-img" src="/images/jobbil.webp" alt="Rosendal Tømrers firmabil ved værkstedet med en kasse i træ" width="587" height="585" loading="lazy">
    <h2>Hvem er vi?</h2>
    <p>Hos Rosendal Tømrer Entreprise er vi kvalitetsbevidste og stolte af vores faglige kunnen. Vi går på arbejde med glæde, fordi vi laver det vi brænder for, og vi lægger vægt på et kammeratligt og tæt sammenhold.</p>
    <p>Vi laver alle former for tømreropgaver, fordi vi kan lide at to dage ikke er ens: tag, døre og vinduer, terrasser, hegn, skure, gårdmiljøer, nybyg og renovering. Alt udføres ud fra kundens ønsker, så det er vigtigt at du er god til at tale med kunderne fra start til slut.</p>
    <h2>Send en åben ansøgning</h2>
    <p>Du behøver ikke vente på et opslag. Send en åben ansøgning via formularen, så tager vi en snak, når det passer.</p>
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
  <p>Vi laver alt i Hundested og omegn, også reparationer og små opgaver. Små opgaver som fx dørskift samler vi og tager flere ad gangen.</p>
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

# Afskrevet fra det gamle sites PDF (Rosendal-Materieludlejning-Betingelser.pdf). Kun stavning og tegnsaetning er rettet,
# bortset fra at beloeb og procentsatser er taget ud (moedet 23-10-2026), indtil Sebastian har krydstjekket priserne.
# Det er juridisk tekst, saa aendringer i indholdet skal komme fra Sebastian.
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
  <p>Har lejer beskadiget lejet materiel, forpligter lejer sig til at erstatte bortkommet eller beskadiget materiel. Ved tyveri, brand, hærværk m.v. forpligter lejer sig til at betale en selvrisiko, der beregnes af materiellets værdi og oplyses ved booking.</p>
  <h2>5. Uheld</h2>
  <p>Udgifter for lejer på grund af uheld er udlejer uvedkommende.</p>
  <h2>6. Forsikringsgebyr</h2>
  <p>Der tillægges et almindeligt forsikringsgebyr, der beregnes af den samlede pris og oplyses ved booking.</p>
  <h2>7. Ansvarsforsikring</h2>
  <p>Udlejer tegner ansvarsforsikring mod det erstatningsansvar, som udlejer ifølge dansk ret måtte ifalde for skader på personer eller ejendom (tingskader). Udlejer påtager sig intet ansvar og ingen risiko, hvorfor dette påhviler lejer. Såfremt udlejer bliver pålagt dette ansvar, er lejer forpligtet til at holde udlejer skadesløs for ethvert ansvar.</p>
  <h2>Annullering</h2>
  <p>Annullering af en ordre skal ske senest 7 dage før den aftalte booking. Ved annullering opkræves et gebyr, som oplyses ved booking.</p>
  <h2>Kontrol, rengøring og brændstof</h2>
  <p>I lejeperioden er udlejer forpligtet til at lave sikkerheds- og driftsmæssige kontroller af lejet materiel, herunder væskestand, batterier og løbende rengøring.</p>
  <p>Ved manglende rengøring opkræves et gebyr, som oplyses ved booking.</p>
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
HTML_GAMLE = {"hovedentreprise.html": "hovedentreprise", "doere-og-vinduer.html": "vinduer", "gaardhaver.html": "pergola-hegn-og-cykelskur",
              "materieludlejning.html": "materieludlejning", "referencer.html": "anmeldelser", "terrasse.html": "terrasse",
              "tag.html": "tag", "nybyg.html": "nybyg", "renovering.html": "renovering", "job.html": "job", "kontakt.html": "kontakt",
              "cookies.html": "cookies", "lejebetingelser.html": "lejebetingelser"}
# /materieludlejning/ var ogsaa WordPress-adressen og er nu siden selv. udlejning-af-stillads-og-trailer var kun paa testsiden.
WP_GAMLE = {"doere-vinduer": "vinduer", "gaardhaver": "pergola-hegn-og-cykelskur", "udlejning-af-stillads-og-trailer": "materieludlejning",
            # Moedet 23-10-2026: totalentreprise hedder nu hovedentreprise, og sommerhus er ikke en selvstaendig ydelse laengere
            "totalentreprise": "hovedentreprise", "sommerhus": "renovering"}

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

> Tømrerfirma i Hundested, stiftet 2021 af tømrermester Sebastian Norborg Rosendal, der blev uddannet tømrer i 2010 og bygningskonstruktør i 2018. Fag- og hovedentrepriser for private og erhverv i Nordsjælland: tilbygning, tag, vinduer og døre, terrasser, renovering af huse og sommerhuse samt nybyg. Reparationer og små opgaver tages også. Materieludlejning med afhentning på {ADR}, {POST} {BY}.

- Telefon: {TLF}
- E-mail: {MAIL}
- Adresse: {ADR}, {POST} {BY} (værksted og kontor)
- CVR: {CVR}
- Anmeldelser: {ANM_SNIT} ud af 5, {ANM_TEKST} anmeldelser på Anmeld Håndværker ({ANM_URL})
- Åbningstid: {AABNING}
- Ansatte: {ANSATTE}
- Medlem af Dansk Håndværk
- Serviceområde: {ARBEJDSOMRAADE}, med base på Engdraget 11 i Hundested. Opgaver længere væk tages også
- Materieludlejning: kontakt os for pris. Afhentning på {ADR}, {POST} {BY}

## Ydelser
{ylist}

## Andet
- [Om os]({DOMAIN}/om-os/)
- [Områder]({DOMAIN}/omrader/)
- [Tømrer i Hundested]({DOMAIN}/tomrer-hundested/)
- [Anmeldelser]({DOMAIN}/anmeldelser/)
- [Kontakt]({DOMAIN}/kontakt/)
""" + "".join(f"- [Projekt: {p['titel']}]({DOMAIN}/projekter/{p['slug']}/)\n" for p in LIVE))

if not LIVEBYG:
    skriv(".nojekyll", "")  # kun GitHub Pages bruger den
else:
    zipsti = shutil.make_archive(os.path.join(ROD, "rosendal-tomrer-live"), "zip", OUT)
    print(f"Live-zip: {os.path.abspath(zipsti)}")
print("Bygget:", len(SIDER), "indekserbare sider i", os.path.abspath(OUT))
