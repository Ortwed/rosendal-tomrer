"""Alt tekstindhold. Udkast: skal faktatjekkes med Sebastian (se FAKTATJEK.md)."""

# Verificerede anmeldelser fra anmeld-haandvaerker.dk (side 1-2 hentet 07-10-2026, 21 af 38).
# (titel, tekst, fornavn, by, maaned, karakter, opgavetype). Teksten er kun rettet for tastefejl.
ANMELDELSER = {
    "kenneth": ("Nyt tegltag", "Alt er forløbet som vi havde håbet og forventet. Rigtig flinke og flittige håndværkere.", "Kenneth", "Hundested", "oktober 2026", "5,0", "Tag"),
    "ulla": ("Nyt tag hos min mor. Ny carport hos mig selv.",
             "Nem at få kontakt til. Meget imødekommende og problemløsning helt i top. Møder mig der hvor jeg er og tager godt imod mine spørgsmål. Kan varmt anbefale firmaet, de svende jeg har haft kontakt med, også helt i top.",
             "Ulla", "Hundested", "oktober 2026", "5,0", "Tag · Carport"),
    "peter": ("Nye vinduer og to franske altaner", "Super flot udført.", "Peter", "Hundested", "august 2026", "5,0", "Døre og vinduer"),
    "morten": ("Repos-trappe i ipé",
               "Vi fik bygget et fem meter langt repos-trin i ipé fra foldedør ned til eksisterende stenterrasse. Tilbud, udførsel, oprydning og fakturering kørte helt som aftalt, og resultatet er super flot. Vi havde god sparring med svendene mens de byggede. Vil klart bruge igen.",
               "Morten", "Veksø", "juli 2026", "5,0", "Terrasse"),
    "anne": ("Vinduer og terrasse", "Alle aftaler overholdt og rigtig flot arbejde.", "Anne", "Hundested", "juni 2026", "5,0", "Døre og vinduer · Terrasse"),
    "anita": ("Nye døre og vinduer",
              "To tømrere satte et badeværelsesvindue, et køkkenvindue og to yderdøre i. Begge meget venlige og serviceminded. Alle aftaler med firmaet er overholdt til punkt og prikke, og vi er MEGET glade for resultatet.",
              "Anita", "Vejby", "april 2026", "5,0", "Døre og vinduer"),
    "brian": ("Renovering af sommerhus med nyt tag",
              "Nye vægge og gulv med isolering og nyt tag. Det har været en fornøjelse hele vejen igennem. Sebastian er altid til at få fat på, og hans ansatte er både dygtige og søde. Alle aftaler er overholdt, derfor fuld plade herfra.",
              "Brian", "Hundested", "februar 2026", "5,0", "Renovering · Fag- og hovedentreprise"),
    "elisabeth": ("Dør, paneler og terrassedør", "Montering af dør og paneler og reparation af terrassedør.", "Elisabeth", "Hundested", "februar 2026", "4,8", "Indvendigt"),
    "erik": ("Nye bærende stolper ved indgangen",
             "Meget fin oplevelse fra første dialog med firmaet og indtil arbejdet var færdigt. Pænt arbejde og rigtig fin oprydning.",
             "Erik", "Hundested", "januar 2026", "5,0", "Renovering"),
    "rita": ("Tilbygning og gæstehus",
             "Tømrerfirma med fokus på virkelig godt håndværk. Overholder aftaler og informerer fint, hvis der er problemer. Konstruktiv i løsning af misforståelser. Et firma jeg har været 100 % tryg ved.",
             "Rita", "Hundested", "november 2025", "5,0", "Nybyg · Fag- og hovedentreprise"),
    "nila": ("Vindue", "God kommunikation, levering til tiden og hurtigt arbejde. Alt er fint.", "Nila", "Hillerød", "oktober 2025", "4,2", "Døre og vinduer"),
    "richo": ("Gulv der trak sig fra hinanden om vinteren", "Opgaven blev løst på aftalt tidspunkt, kan ikke sætte en finger på noget. Kan varmt anbefale Rosendal Tømrer Entreprise!", "Richo", "Hundested", "oktober 2025", "5,0", "Renovering"),
    "erikms": ("Ny terrassedør",
               "Firmaet sendte efter aftale en mand ud til opmåling. Efter en god korrespondance om pris og udførelse blev døren bestilt hjem. Da den var leveret fra fabrikken, gik håndværkerne straks i gang, og samme dag var opgaven udført til tilfredshed.",
               "Erik", "Hundested", "oktober 2025", "4,9", "Døre og vinduer"),
    "hanne": ("Ny facadebeklædning og isolering", "Godt og behageligt samarbejde med Sebastian og et rigtig flot stykke arbejde. Vi kan på det varmeste anbefale Rosendal Tømrer Entreprise ApS.", "Hanne", "Ølsted", "september 2025", "5,0", "Renovering"),
    "marie": ("Ny hoveddør og fugning af vindue", "Mine bedste anbefalinger af Rosendal Tømrer. Arbejdet er udført meget tilfredsstillende af venlige og kompetente fagfolk.", "Marie", "Hundested", "september 2025", "5,0", "Døre og vinduer"),
    "mie": ("Nyt tag, skillevæg og mere", "Fantastisk tømrervirksomhed! Pålidelige, venlige og super dygtige. Alt blev lavet til tiden og i høj kvalitet. KÆMPE ROS og mine varmeste anbefalinger!", "Mie", "Hundested", "september 2025", "5,0", "Tag · Renovering"),
    "bitten": ("Beklædning på vægge og loft samt altan",
               "Kæmpe fornøjelse at have Rosendal til at stå for mit sommerhusprojekt. Alle aftaler blev overholdt, og resultatet er blevet super flot. Dejligt med en håndværker, der både holder aftaler og svarer, når man skriver eller ringer.",
               "Bitten", "Hundested", "august 2025", "5,0", "Renovering"),
    "bodil": ("Nyt tag", "Effektive og behagelige håndværkere. Jeg vil gerne bruge dem en anden gang.", "Bodil", "Hundested", "august 2025", "5,0", "Tag"),
    "ullas": ("Reparation af vinduesrammer", "Afklaring af problem, udbedring og god kommunikation.", "Ulla", "Frederiksværk", "august 2025", "5,0", "Døre og vinduer"),
    "kira": ("Terrasse", "God kommunikation, god pris, flot arbejde. Meget tilfredse.", "Kira", "Liseleje", "august 2025", "5,0", "Terrasse"),
}

# Ydelsessider. Felter pr. side:
#   title, desc, h1, intro   meta og sidehoved
#   svar                     kort svar-boks (40-60 ord), skrevet saa den kan citeres direkte
#   ind / ind_h              "hvad indgaar" (punkter; (tekst, slug) giver et link)
#   sek                      [(h2, [afsnit] | ('ul', [..]) | ('html', '<p>..</p>'))]
#   trin                     4 trin: (titel, tekst)
#   pris_intro / pris        hvad paavirker prisen. INGEN tal, indtil Sebastian leverer dem
#   anm                      noegler i ANMELDELSER (vises som kort)
#   faq                      [(spoergsmaal, svar)]
# Alt er udkast, indtil Sebastian har godkendt det (se FAKTATJEK.md, afsnit "Nye paastande").
TRIN_STD = [("Første snak", "Du ringer eller skriver og fortæller kort om opgaven."),
            ("Besigtigelse", "Vi kommer ud, ser på forholdene og taler løsninger igennem."),
            ("Fast tilbud", "Du får et skriftligt tilbud med pris, omfang og tidsplan."),
            ("Udførelse og aflevering", "Vi udfører arbejdet, holder dig orienteret og afleverer ryddet op.")]

YDELSER = {
"hovedentreprise": dict(
    title="Hovedentreprise i Nordsjælland | Rosendal Tømrer",
    desc="Hovedentreprise i Nordsjælland. Tømrermester i Hundested koordinerer murer, el, VVS og maler. Én kontrakt, én kontakt. Ring 50 70 05 05.",
    h1="Hovedentreprise: én kontrakt og én kontakt",
    intro="Én kontrakt, én kontakt og ét ansvar. Vi styrer byggeriet og koordinerer de andre fag, så du ikke selv skal være byggeleder.",
    svar='Hovedentreprise betyder, at du har én aftalepart: Rosendal Tømrer Entreprise i Hundested. Vi koordinerer murer, el, VVS, maler og kloak, holder tidsplanen og afleverer et færdigt byggeri i Nordsjælland. Du kender prisen, før byggeriet går i gang, fordi alle fag samles i ét skriftligt tilbud.',
    ind=["Ét samlet, skriftligt tilbud", "Koordinering af murer, el, VVS, maler og kloak", "Tidsplan, som du får sammen med tilbuddet",
         "Tømrerarbejdet udført af vores eget hold", "Løbende dialog med dig som bygherre", "Oprydning undervejs og ved aflevering"],
    sek=[
        ("Forskellen på fagentreprise og hovedentreprise", [
            "Entrepriseform handler om, hvem du har en aftale med, og hvem der hæfter for helheden. Her er forskellen, som vi forklarer den, når en kunde spørger.",
            "Fagentreprise. Du har en kontrakt med hver håndværker. Vi udfører tømrerarbejdet, og du eller din rådgiver sørger for, at murer, el, VVS og maler kommer ind på det rigtige tidspunkt.",
            "Hovedentreprise. Du har én kontrakt med os om hele byggeriet. Vi hyrer og koordinerer de øvrige fag og er din eneste kontakt. Tegninger og beregninger laver vi ikke selv. Dem står din arkitekt eller ingeniør for, og vi bygger efter dem.",
        ]),
        ("Hvem er aftalepart, og hvem hæfter?", [
            "Ved hovedentreprise har du kontrakten med os, også når arbejdet udføres af vores samarbejdspartnere. Går noget skævt mellem to fag, er det vores opgave at få det rettet, ikke din.",
            "Det er den største forskel i hverdagen: du skal ikke selv være byggeleder ved siden af dit arbejde.",
        ]),
        ("Sådan koordinerer vi murer, el, VVS, maler og kloak", [
            "Vi har faste samarbejdspartnere inden for murer, el, VVS, maler og kloak i Nordsjælland. Vi indhenter tilbuddene, lægger tidsplanen og sørger for, at fagene kommer ind i den rækkefølge, byggeriet kræver. Du får ét samlet tilbud.",
            "Det kræver, at byggeriet er tænkt igennem, før det første fag går i gang. Det er her, Sebastians baggrund som både tømrer og bygningskonstruktør kommer til nytte: Han kender konstruktionen indefra og er med i planlægningen tidligt.",
        ]),
        ("Typiske projekter", ('ul', [
            "Tilbygning, anneks og gæstehus",
            "Nyt hus på egen grund",
            "Renovering af hele huset eller sommerhuset",
            "Nyt tag med nye vinduer i samme projekt",
            "Renovering, hvor flere fag skal passe sammen",
        ])),
        ("Foretrækker du at styre selv?", [
            "Har du selv styr på de andre fag, eller vil du stå for koordineringen, laver vi også tømrerarbejdet som ren fagentreprise. Vi siger ærligt, hvad vi tror passer bedst til dit projekt.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller om projektet, og vi afklarer, om det skal være fagentreprise eller hovedentreprise."),
          ("Besigtigelse", "Vi besøger grunden eller huset og gennemgår tegninger, hvis du har dem."),
          ("Fast tilbud", "Du får ét skriftligt tilbud, der samler alle fagene, med omfang og tidsplan."),
          ("Udførelse og aflevering", "Vi koordinerer byggepladsen, holder dig orienteret og afleverer ryddet op.")],
    pris_intro='Vi giver ikke et overslag uden at have set opgaven. Disse forhold vejer tungest:',
    pris=["Byggeriets størrelse og hvor mange fag, der skal koordineres", "Om projektet allerede er tegnet af en arkitekt eller en ingeniør",
          "Valg af materialer, vinduer, tag og facade", "Grundens beliggenhed og adgangsforholdene"],
    faq=[
        ("Hvad er forskellen på fagentreprise og hovedentreprise?", "I en fagentreprise har du en kontrakt med hver håndværker og står selv for koordineringen. I en hovedentreprise har du én kontrakt med os, og vi koordinerer de øvrige fag. Hvilken form der passer til dit projekt, afklarer vi ved første besigtigelse."),
        ("Hvad koster koordineringen?", "Der er et tillæg for koordineringen, men til gengæld slipper du for spildtid mellem fagene og for selv at bære risikoen, når de skal passe sammen. Vi lægger tallene frem, så du kan vurdere det."),
        ("Hvem søger byggetilladelse?", "Ansøgningen går til kommunen, og reglerne afhænger af byggeriets art og størrelse. Vi gennemgår med dig, hvad dit projekt kræver, og hvem der tager sig af hvad, inden vi giver tilbud."),
        ("Kan vi bo i huset under byggeriet?", "Ofte ja. Vi planlægger rækkefølgen, så der er mindst muligt rod og støv i de rum, I bruger, og så der først åbnes ind til det eksisterende hus, når nybygningen er lukket og tæt."),
        ("Hvordan afleveres projektet?", "Vi rydder op og gennemgår byggeriet sammen med dig. Hvis der opstår noget uventet undervejs eller ved afleveringen, tager vi dialogen med dig, inden vi forlader pladsen."),
        ("Hvilke håndværkere samarbejder I med?", "Vi har faste samarbejdspartnere inden for murer, el, VVS, maler og kloak i Nordsjælland. Du får ét samlet tilbud."),
    ],
    anm=['brian']),

"tilbygning": dict(
    title="Tilbygning i Nordsjælland | Rosendal Tømrer",
    desc="Tilbygning, anneks og gæstehus i Nordsjælland. Tømrermester og bygningskonstruktør fra Hundested bygger til hus og sommerhus. Ring 50 70 05 05.",
    h1="Tilbygning, anneks og gæstehus",
    intro="Mere plads uden at flytte. Vi bygger tilbygninger til huse og sommerhuse i Nordsjælland, fra første snak til afleveret byggeri.",
    svar='En tilbygning giver dig mere plads uden at flytte. Vi bygger udvidelser af stuen, ekstra værelser, anneks og førstesal på huse og sommerhuse i Nordsjælland. Sebastian Rosendal, tømrermester og uddannet bygningskonstruktør, er din faste kontakt. Når vi har set huset og grunden, får du en fast pris i et skriftligt tilbud.',
    ind=["Gennemgang af huset, grunden og dine ønsker", "Tømrerarbejdet i tilbygningen: gulv, vægge, tagkonstruktion, vinduer og døre",
         "Tilslutning til det eksisterende hus", "Hjælp til at koordinere de øvrige fag, hvis du ønsker det",
         "Tidsplan og løbende dialog undervejs", "Oprydning og aflevering"],
    sek=[
        ("En tilbygning skal se ud, som om den altid har hørt til", [
            "Det handler om taghældning, vinduesplacering, materialer og om, hvordan det nye rum hænger sammen med resten af boligen. Her har vi gavn af, at Sebastian både er tømrermester og uddannet bygningskonstruktør.",
            "Vi starter med at se på huset og høre, hvad pladsen skal bruges til. Derefter taler vi løsning og udtryk igennem, og når det er på plads, får du et fast tilbud med tidsplan.",
        ]),
        ("Fire typiske tilbygninger", ('ul', [
            "Udvidelse af stuen eller køkken-alrummet, så huset får plads til hele familien",
            "Ekstra værelse eller gæsteværelse",
            "Anneks, der hænger sammen med huset",
            "Førstesal ovenpå en eksisterende bygning",
        ])),
        ("Tilbygning eller gæstehus?", [
            "En tilbygning giver mere sammenhængende plads i hverdagen, fordi det nye rum er en del af huset. Et fritliggende gæstehus kan til gengæld være enklere at bygge, fordi det ikke skal kobles på det eksisterende hus. Vi gennemgår fordele og ulemper ved din grund og dit hus, før du beslutter dig.",
        ]),
        ('Byggetilladelse', [
            "En tilbygning til en bolig skal som udgangspunkt have tilladelse fra kommunen. Reglerne afhænger af størrelse, placering og lokalplan, og det er kommunen, der afgør sagen. Vi taler det igennem med dig, inden vi giver tilbud, så du ved, hvad der skal søges, og af hvem.",
        ]),
        ("Hele projektet eller kun tømrerarbejdet", [
            ('html', '<p>Du kan nøjes med tømrerarbejdet, eller du kan få hele byggeriet som hovedentreprise med én kontakt. Læs mere under <a href="/hovedentreprise/">hovedentreprise</a>. Skal der bygges et helt nyt hus eller et fritliggende anneks, finder du det under <a href="/nybyg/">nybyg</a>.</p>'),
        ][0]),
    ],
    trin=[("Første snak", "Du fortæller, hvad du vil bruge pladsen til, og omtrent hvad du har af budget."),
          ("Besigtigelse", "Vi gennemgår huset og grunden og taler plan og udtryk igennem."),
          ("Fast tilbud", "Du får det hele på skrift: pris, omfang og tidsplan for tilbygningen."),
          ("Udførelse og aflevering", "Vi bygger tilbygningen lukket og tæt, før der åbnes ind til huset, og afleverer ryddet op.")],
    pris_intro='Prisen på en tilbygning afhænger af opgaven. Her er det, der betyder mest:',
    pris=["Tilbygningens størrelse", "Om der bygges på en eksisterende konstruktion eller fra grunden", "Valg af vinduer, døre og facade",
          "Installationer som el og VVS", "Adgangen til byggepladsen"],
    faq=[
        ("Hvor lang tid tager en tilbygning?", "Det afhænger af størrelse og hvor mange fag der er involveret. Du får altid en tidsplan sammen med tilbuddet, så du ved, hvad du kan regne med."),
        ("Kan vi bo i huset, mens I bygger til?", "Det kan I som regel. Vi bygger tilbygningen færdig udefra, så den er lukket og tæt, før væggen mod jeres hus bliver åbnet."),
        ("Skal jeg have byggetilladelse?", "Som udgangspunkt skal en tilbygning til en bolig have tilladelse fra kommunen. Reglerne afhænger af størrelse, placering og lokalplan, og kommunen afgør sagen. Vi gennemgår det med dig, før vi giver tilbud."),
        ("Kan I bygge til et sommerhus?", "Ja. Vi bygger til både helårshuse og sommerhuse. Hvilke regler der gælder for dit sommerhus, afhænger af området, så det afklarer vi ved besigtigelsen."),
        ("Kan I tage hele projektet, også el og VVS?", "Ja, hvis du vælger hovedentreprise. Så koordinerer vi murer, el, VVS og maler, og du har én kontakt. Du kan også nøjes med tømrerarbejdet."),
        ("Kan tilbygningen blive i samme stil som huset?", "Det er målet. Taghældning, vinduer og materialer skal passe til huset, så tilbygningen ser ud, som om den altid har været der."),
    ],
    anm=['rita']),

"tag": dict(
    title="Nyt tag og tagrenovering i Nordsjælland | Rosendal",
    desc="Nyt tag, tegltag og tagrenovering i Nordsjælland. Tømrermester i Hundested tager hele tagprojektet med stillads og efterisolering. Ring 50 70 05 05.",
    h1="Nyt tag og tagrenovering",
    intro="Et tag skal holde i mange år. Vi skifter, renoverer og efterisolerer tage på huse og sommerhuse i Nordsjælland.",
    svar='Vi skifter og renoverer tage på huse og sommerhuse i Nordsjælland, også tegltage. Vi tager hele tagprojektet: nedtagning, undertag, lægter, nyt tag, inddækninger og efterisolering, og vi har selv stillads. Prisen kender du, når vi har gennemgået taget og spærene og sendt dig et skriftligt tilbud.',
    ind=["Gennemgang af tag og spær, før du får tilbud", "Nedtagning af det gamle tag", "Undertag og lægter", "Nyt tag på hus og sommerhus, også tegltag",
         "Inddækninger, ventilation og tagudhæng", "Ovenlysvinduer og kviste", "Efterisolering, når taget alligevel er åbent", "Stillads og oprydning"],
    sek=[
        ("Hele tagprojektet", [
            "Et nyt tag er mere end nye plader eller sten. Undertag, lægter, inddækninger og ventilation skal spille sammen, ellers får man problemer med fugt længe før selve tagbelægningen er slidt op.",
            "Vi gennemgår taget og spærene, inden vi giver tilbud, så du ved, om der er skjulte skader, der skal udbedres samtidig.",
        ]),
        ("Efterisolering ved tagskifte", [
            "Et tagskifte er et godt tidspunkt at efterisolere på, fordi taget alligevel er åbent. Vi taler isoleringen igennem med dig, så den passer til husets konstruktion og til, hvad du vil bruge huset til.",
        ]),
        ("Stillads og sikkerhed", [
            "Vi har selv stillads og trailer, så stilladset er en del af tilbuddet. Det giver sikre arbejdsforhold og betyder, at vi ikke skal vente på en udlejer for at holde tidsplanen.",
        ]),
        ("Gamle eternittage", [
            "Ældre eternittage kan indeholde asbest, og så skal nedtagningen håndteres efter særlige regler. Vi får det afklaret, før arbejdet går i gang, så både du og vores folk er trygge.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller om taget og hvad du har set: fugtpletter, løse sten eller et tag, der er ved at være slidt."),
          ("Besigtigelse", "Vi går taget og spærene igennem og siger ærligt, om det kan repareres, eller om det er tid til et nyt."),
          ("Fast tilbud", "Du får et skriftligt tilbud med pris, omfang og tidsplan, inklusive stillads."),
          ("Udførelse og aflevering", "Vi åbner kun så meget af taget ad gangen, som vi kan nå at lukke igen, og afleverer ryddet op.")],
    pris_intro='Du får en fast pris, når vi har været oppe og se på taget. De største poster er:',
    pris=["Tagets størrelse og form", "Hvilken tagbelægning du vælger", "Om spær, lægter eller undertag skal udbedres", "Ovenlysvinduer, kviste og efterisolering",
          "Om taget er et gammelt eternittag"],
    faq=[
        ("Hvornår skal mit tag skiftes?", "Typiske tegn er knækkede eller porøse plader, fugtpletter på loftet og et undertag, der er gået i stykker. Vi kommer gerne ud og giver en ærlig vurdering af, om det kan repareres, eller om det er tid til et nyt."),
        ("Kan I efterisolere samtidig med, at taget skiftes?", "Ja, og det er det bedste tidspunkt at gøre det på, fordi taget alligevel er åbent."),
        ("Hvad sker der, hvis det regner undervejs?", "Vi åbner kun så meget af taget ad gangen, som vi kan nå at lukke igen, og dækker af, når det er nødvendigt."),
        ("Leverer I også stillads?", "Ja. Vi har selv stillads og trailer, så det er med i tilbuddet."),
        ("Kan I skifte tag og vinduer i samme projekt?", "Ja. Står stilladset oppe, giver det god mening at skifte vinduer og tag i samme forløb. Vi kan også tage det som hovedentreprise."),
        ("Hvor lang tid tager et tagskifte?", "Det afhænger af tagets størrelse og form. Du får en tidsplan sammen med tilbuddet."),
    ],
    galleri=[("/images/tag-roedt-gult-hus.webp", "Nyt rødt tag på et gult hus med overdækket terrasse"),
             ("/images/tag-stillads-banner.webp", "Stillads med Rosendal-banner og firmabiler under udskiftning af et tag"),
             ("/images/tag-sort-kviste.webp", "Nyt sort tag med kviste på et murstenshus"),
             ("/images/tag-sort-fra-stillads.webp", "Nyt sort tag set fra stilladset")],
    anm=['kenneth', 'mie', 'bodil']),

"vinduer": dict(
    title="Nye vinduer og vinduesudskiftning | Rosendal Tømrer",
    desc="Nye vinduer i træ og træ/alu i Nordsjælland. Opmåling, levering og korrekt montering af tømrere fra Hundested. Ring 50 70 05 05 for et tilbud.",
    h1="Nye vinduer",
    intro="Nye vinduer giver et lunere hus og et pænere udtryk. Vi står for opmåling, levering og montering.",
    svar='Vi skifter og monterer vinduer i træ og træ/alu på huse og sommerhuse i Nordsjælland. Vi måler op, bestiller og leverer vinduerne og monterer dem med tætte fuger og færdige lysninger, så du kun har ét sted at henvende dig. Efter opmålingen får du en fast pris i et skriftligt tilbud.',
    ind=["Opmåling og rådgivning om valg af vinduer", "Bestilling og levering af vinduerne", "Fjernelse af de gamle vinduer", "Montering med tætte fuger ude og inde",
         "Lysninger og indvendig afslutning", "Oprydning efter opgaven"],
    sek=[
        ("Monteringen er det vigtigste", [
            "Et godt vindue kan blive et dårligt vindue, hvis det sættes forkert i. Fugerne skal være tætte både inde og ude, og vinduet skal sidde rigtigt i muren, så der ikke opstår kuldebroer og fugt.",
            "Vi tager os af det hele: opmåling, valg af produkt, montering, lysninger og fuger, så du står med et færdigt resultat.",
        ]),
        ("Træ eller træ/alu?", [
            "Træ/alu-vinduer kræver mindre vedligehold udvendigt, mens rene trævinduer ofte passer bedst til ældre huse. Vi hjælper dig med at vælge ud fra hus, beliggenhed og budget.",
        ]),
        ("Reparation, forsatsvinduer og ovenlys", [
            "Ikke alle vinduer skal skiftes. Er rammen kun slidt i overfladen, kan en reparation være nok. Er træet blødt, skal der nyt til. Vi ser på vinduet og siger det ærligt, også når svaret er, at du ikke har brug for et nyt.",
            "Vi monterer også ovenlysvinduer og forsatsvinduer og udbedrer vinduesrammer og fuger. Reparationer og små opgaver tager vi i hele Hundested og omegn, og dem samler vi gerne, så flere tages ad gangen.",
        ]),
        ("Vinduer og døre i samme opgave", [
            ('html', '<p>Mange skifter vinduer og yderdøre samtidig, så huset får ét samlet udtryk. Se mere under <a href="/doere/">døre, terrassedøre og foldedøre</a>. Vinduer sammen med nyt tag kan tages i samme forløb, se <a href="/tag/">tag</a>.</p>'),
        ][0]),
    ],
    trin=[("Første snak", "Du fortæller, hvilke vinduer det drejer sig om, og hvorfor de skal skiftes."),
          ("Opmåling", "Vi kommer ud, måler op og taler træ eller træ/alu igennem med dig."),
          ("Fast tilbud", "Du får ét tilbud på vinduer, montering og afslutning."),
          ("Bestilling, montering og aflevering", "Vinduerne bestilles hjem. Når de er leveret, monterer vi dem og afleverer ryddet op.")],
    pris_intro='Prisen fastlægges efter opmålingen. Det er især disse ting, der flytter den:',
    pris=["Antal vinduer og deres størrelse", "Træ eller træ/alu", "Specialmål eller særlige udførelser", "Hvor meget lysninger og afslutning skal udbedres", "Om højtsiddende vinduer kræver stillads"],
    faq=[
        ("Hvor lang tid tager det at skifte et vindue?", "Et almindeligt vindue skiftes typisk på få timer, og hullet i facaden er kun åbent kort tid. Ved større opgaver planlægger vi rækkefølgen, så huset ikke står åbent natten over."),
        ("Hvad med lysninger og indvendig afslutning?", "Det er med i opgaven. Du skal ikke have en maler eller anden håndværker ind bagefter for at gøre det færdigt, medmindre du ønsker det."),
        ("Leverer I selv vinduerne?", "Ja. Vi bestiller vinduerne hjem og leverer dem, så du har én at henvende dig til, hvis der senere er noget med produktet."),
        ("Kan man nøjes med at reparere et vindue?", "Nogle gange. Er rammen kun slidt i overfladen, kan en reparation være nok. Er træet blødt, skal der nyt til. Vi ser på det og siger det, som det er."),
        ("Hvilke vinduer passer til et ældre hus?", "Rene trævinduer passer ofte bedst til ældre huse. Vi ser på huset og siger, hvad vi tror giver det pæneste og mest holdbare resultat."),
        ("Kan I skifte vinduer og tag samtidig?", "Ja. Står stilladset oppe, giver det god mening at tage begge dele i samme forløb."),
    ],
    anm=['anita', 'ullas']),

"doere": dict(
    title="Nye døre, terrassedøre og foldedøre | Rosendal Tømrer",
    desc="Hoveddøre, terrassedøre, foldedøre og franske altaner i Nordsjælland. Opmåling, levering og montering ved tømrere i Hundested. Ring 50 70 05 05.",
    h1="Døre, terrassedøre og foldedøre",
    intro="Ny dør, nyt udtryk. Vi måler op, bestiller og monterer hoveddøre, terrassedøre, foldedøre og franske altaner.",
    svar='Vi leverer og monterer hoveddøre, yderdøre, terrassedøre, foldedøre og franske altaner i Nordsjælland. Efter opmåling bestiller vi døren hjem, og når den er leveret, monterer vi den med tætte fuger og afslutter indvendigt. Du får et skriftligt tilbud med en fast pris, før døren bestilles.',
    ind=["Opmåling", "Bestilling og levering af døren", "Montering af hoveddør, terrassedør eller foldedør", "Fugning og tætning", "Paneler, lister og indvendig afslutning", "Oprydning"],
    sek=[
        ("Hoveddør og yderdør", [
            "En hoveddør er det første, man ser, og den skal samtidig holde vejr og vind ude. Montering og fugning afgør, om døren sidder tæt i mange år. Vi tager både selve døren og tilpasningen af åbningen.",
        ]),
        ("Terrassedør og foldedør", [
            "En terrassedør eller en foldedør binder stue og terrasse sammen. Vi bygger også det, der kommer uden for døren, så overgangen bliver pæn: Vi har fx bygget et fem meter langt repos-trin i ipé fra en foldedør ned til en eksisterende stenterrasse.",
        ]),
        ("Fransk altan", [
            "En fransk altan giver lys og luft i en stue eller et soveværelse uden at tage plads udenfor. Hullet i muren skal som regel gøres større, og det klarer vi som en del af opgaven.",
        ]),
        ("Indvendige døre og paneler", [
            "Vi monterer også indvendige døre, paneler og lister og reparerer eksisterende døre, fx en terrassedør, der ikke lukker, som den skal.",
            "Vi laver alt i Hundested og omegn, også de små opgaver. Et enkelt dørskift samler vi gerne med andre små opgaver og tager flere ad gangen.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller, hvilken dør det drejer sig om, og hvad du ønsker dig."),
          ("Opmåling", "Vi kommer ud og måler åbningen op og taler dørtype og udtryk igennem."),
          ("Fast tilbud", "Du får et skriftligt tilbud, og døren bestilles hjem."),
          ("Montering og aflevering", "Når døren er leveret, monterer vi den, fuger og afslutter og afleverer ryddet op.")],
    pris_intro='Døren og åbningen afgør prisen. Her er de vigtigste faktorer:',
    pris=["Dørtype: hoveddør, terrassedør, foldedør eller fransk altan", "Dørens størrelse og eventuelle specialmål", "Om åbningen i muren skal laves om", "Udvendig og indvendig afslutning"],
    faq=[
        ("Hvor lang tid tager det at skifte en dør?", "Det afhænger af døren og åbningen. Du får en tidsplan sammen med tilbuddet."),
        ("Kan I lave en fransk altan i et eksisterende hus?", "Ja. Hullet i muren skal som regel gøres større, og det klarer vi som en del af opgaven."),
        ("Kan I sætte en foldedør i, hvor der er en terrassedør i dag?", "Ofte kan det lade sig gøre, men åbningen skal som regel laves om. Vi ser på konstruktionen, så vi kan sige, hvad der er muligt."),
        ("Leverer I selv dørene?", "Ja. Vi bestiller døren hjem og leverer den, og du har én kontakt fra bestilling til montering."),
        ("Hvad med afslutningen omkring døren?", "Fuger, lister og paneler omkring døren er en del af opgaven, så den står færdig, når vi er væk."),
        ("Kan I også reparere en dør?", "Ja. Vi har blandt andet repareret en terrassedør og monteret paneler ved en dør."),
        ("Tager I også et enkelt dørskift?", "Ja. Små opgaver som et dørskift samler vi og tager flere ad gangen, så ring og fortæl, hvad du har brug for."),
    ],
    anm=['erikms', 'marie']),

"terrasse": dict(
    title="Træterrasse og trappetrin i Nordsjælland | Rosendal",
    desc="Træterrasser, repos og trappetrin i ipé og andre træsorter. Vi bygger terrassen med en stabil underkonstruktion, så den holder. Ring 50 70 05 05.",
    h1="Terrasser i træ",
    intro="En terrasse er hverdagens udestue. Vi bygger træterrasser, repos og trappetrin i Nordsjælland.",
    svar='Vi bygger træterrasser, repos og trappetrin i hårdttræ som ipé og jatoba og i nåletræ i Nordsjælland. Vi starter med underkonstruktionen, så terrassen ligger plant og tørt i mange år. Belægning omkring terrassen laver vi i samarbejde med en lokal anlægsgartner. Når vi har set stedet, får du en fast pris i et skriftligt tilbud.',
    ind=["Besigtigelse og rådgivning om træsort", "Fundament og underkonstruktion", "Terrasse, repos eller trappetrin i det valgte træ",
         "Siddetrin, bænke og plantekasser efter ønske", "Oprydning efter opgaven"],
    sek=[
        ("Det der ikke ses, betyder mest", [
            "En træterrasse står eller falder med underkonstruktionen. Afstand mellem strøer, luft under brædderne og afvanding afgør, om terrassen ligger plant og tørt om ti år.",
            "Derfor starter vi altid med fundamentet og konstruktionen, før vi taler om brædder og overflade.",
        ]),
        ("Det bygger vi", ('ul', [
            "Træterrasser i hårdttræ som ipé og jatoba og i trykimprægneret træ",
            "Repos og trappetrin fra dør til have",
            "Hævede terrasser på skrå grunde",
            "Terrasser med indbygget bænk eller plantekasse",
        ])),
        ("Valg af træ", [
            "Hårdttræ som ipé og jatoba er tungt, tæt og holdbart, men koster mere. Trykimprægneret træ er billigere og fint til mange opgaver. Vi gennemgår forskellen på holdbarhed, udseende og vedligehold, så du kan vælge med åbne øjne.",
        ]),
        ("Sebastian: Sådan rådgiver jeg om træ", [
            "Jeg anbefaler ud fra den enkelte opgave: hvor terrassen ligger, og hvilke forhold den skal stå i. Ligger den tæt på vandet, fraråder jeg blødt træ, fordi det holder dårligere der. Flere kunder vil også gerne væk fra trykimprægneret, og det tager vi med i snakken. Du skal føle dig godt rådgivet, før du vælger.",
        ]),
        ("Terrasse og altan til sommerhuset", [
            "Mange sommerhuse får en ny terrasse eller en altan, ofte som en del af en større renovering. Vi bygger begge dele og kan tage dem i samme forløb som tag, vinduer eller facade.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller, hvor terrassen skal ligge, og hvordan den skal bruges."),
          ("Besigtigelse", "Vi ser på grunden, målene og niveauforskellene og taler træsort igennem."),
          ("Fast tilbud", "Du får ét tilbud på fundament, træ og trin."),
          ("Bygning og aflevering", "Vi bygger fra fundamentet og op og afleverer ryddet op.")],
    pris_intro='Terrassens pris afgøres af størrelse og materiale. Det spiller ind:',
    pris=["Terrassens størrelse", "Træsort: hårdttræ eller nåletræ", "Niveauforskelle og antal trin", "Underlag og adgang til arbejdsstedet", "Ekstra som bænk eller plantekasse"],
    faq=[
        ("Hvilket træ holder længst?", "Tætte hårdttræsorter som ipé holder typisk længst og kræver mindst vedligehold. Vi rådgiver ud fra, hvordan terrassen skal bruges, og hvor meget sol og fugt den får."),
        ("Kan I bygge videre på en eksisterende stenterrasse?", "Ja. Vi har fx bygget et fem meter langt repos-trin i ipé fra en foldedør ned til en eksisterende stenterrasse."),
        ("Skal terrassen behandles?", "Det afhænger af træsorten og det udtryk, du ønsker. Lader man træet stå ubehandlet, bliver det sølvgråt med tiden."),
        ("Laver I også belægning omkring terrassen?", "Belægning og haveanlæg laver vi i samarbejde med en lokal anlægsgartner, så du kan få det hele i ét projekt."),
        ("Kan terrassen bygges på en skrå grund?", "Ja. Vi bygger også hævede terrasser og trappetrin, hvor terrænet falder."),
    ],
    billede=("/images/bro-ipe.webp", "Lang terrasse i ipé langs kysten med trappe op ad skrænten, bygget af Rosendal Tømrer"),
    galleri=[("/images/terrasse-haardttrae-trin.webp", "Terrasse i hårdttræ med indbyggede trin ved et sort træhus"),
             ("/images/terrasse-haardttrae-hus.webp", "Nylagt terrasse i hårdttræ ved et hus med have"),
             ("/images/terrasse-trykimp-langs-hus.webp", "Terrasse i trykimprægneret træ langs et hus med store vinduespartier"),
             ("/images/terrasse-trykimp-hjoerne.webp", "Terrasse i trykimprægneret træ, der knækker rundt om hjørnet af huset")],
    anm=['morten']),

"renovering": dict(
    title="Renovering af hus og sommerhus | Rosendal Tømrer",
    desc="Renovering af hus og sommerhus i Nordsjælland: vægge, gulve, isolering, lofter og indvendigt tømrerarbejde. Én kontakt hele vejen. Ring 50 70 05 05.",
    h1="Renovering",
    intro="Fra et enkelt rum til hele huset. Vi renoverer boliger og sommerhuse i Nordsjælland, både indvendigt og udvendigt.",
    svar='Vi renoverer huse og sommerhuse i Nordsjælland, fra et enkelt rum til hele huset: vægge, gulve, lofter, isolering, facader og indvendigt tømrerarbejde. Åbner vi noget uventet, siger vi det med det samme og aftaler prisen med dig, før vi fortsætter. Efter besigtigelsen får du en skriftlig pris.',
    ind=["Nye vægge, gulve, lofter og skillevægge", "Efterisolering af vægge, gulv og loft", "Indvendig beklædning, døre, paneler og lister",
         "Facadebeklædning og udskiftning af bærende stolper og rådne konstruktioner", "Oprydning undervejs og ved aflevering"],
    sek=[
        ("Renovering kræver overblik", [
            "Når man åbner op i et ældre hus, finder man ofte noget, man ikke havde regnet med. Vi siger det med det samme, forklarer mulighederne og aftaler prisen med dig, før vi går videre.",
            "Mange renoveringer involverer flere fag. Vi kan tage hele opgaven som hovedentreprise, så du kun har én kontakt.",
        ]),
        ("Reparationer og små opgaver", [
            "Vi laver alt i Hundested og omegn, også reparationer og de små opgaver: en dør, der skal skiftes, et par paneler eller en rådden stolpe. Små opgaver som fx dørskift samler vi og tager flere ad gangen, så du ikke skal vente længe, og så turen giver mening for begge parter. Store opgaver kan vi tage som hovedentreprise.",
        ]),
        ("Renovering af sommerhuse", ('html',
            '<p>Mange af vores opgaver ligger i sommerhusområderne omkring Hundested og på Nordkysten. Et sommerhus har ofte brug for flere ting på én gang: nyt tag, efterisolering, nye vægge og gulve, nye vinduer og facadebeklædning. Det kan give god mening at tage dem samlet, fordi stilladset står der alligevel, og fordi arbejdet kan planlægges, så huset kun er åbent, når det er nødvendigt.</p>'
            '<p>Skal sommerhuset også have en terrasse eller en altan, bygger vi den i samme forløb. Se <a href="/terrasse/">terrasse</a>, <a href="/tag/">nyt tag</a> og <a href="/vinduer/">vinduer</a>.</p>')),
    ],
    trin=[("Første snak", "Du fortæller, hvad der skal renoveres, og hvad du ønsker dig af resultatet."),
          ("Besigtigelse", "Vi gennemgår rummene eller huset og forklarer mulighederne."),
          ("Fast tilbud", "Du får det aftalte på skrift, med pris og omfang."),
          ("Udførelse og aflevering", "Vi stopper op og viser dig, hvis vi finder noget uventet, og afleverer ryddet op.")],
    pris_intro='Prisen afhænger af, hvor meget der skal laves, og hvad vi finder undervejs. Det spiller ind:',
    pris=["Hvor mange rum eller dele af huset, der renoveres", "Husets alder og stand", "Valg af materialer og finish", "Om flere fag skal koordineres"],
    faq=[
        ("Hvad sker der, hvis I åbner noget uventet?", "Vi stopper arbejdet, viser dig det, vi har fundet, og aftaler løsning og pris, før noget fortsætter."),
        ("Kan vi bo i huset under renoveringen?", "Ofte ja. Vi planlægger arbejdet, så der er mindst muligt rod og støv i de rum, I bruger."),
        ("Rydder I op efter jer?", "Ja. Oprydning er en del af opgaven, både undervejs og når vi afleverer."),
        ("Laver I små opgaver også?", "Ja. Vi laver alt i Hundested og omegn, også reparationer og små opgaver. Små opgaver som fx dørskift samler vi og tager flere ad gangen. Ring og fortæl, hvad det drejer sig om."),
        ("Renoverer I også sommerhuse?", "Ja. Vi renoverer sommerhuse med nyt tag, efterisolering, vægge, gulve, vinduer og facade, og vi kan bygge terrasse eller altan i samme forløb."),
        ("Kan I tage hele renoveringen?", "Ja. Vi kan tage hele opgaven som hovedentreprise og koordinere de øvrige fag, så du har én kontakt."),
    ],
    anm=['erik', 'bitten']),

"nybyg": dict(
    title="Nybyg i Nordsjælland | Rosendal Tømrer",
    desc="Nye huse, gæstehuse, anneks, carporte og garager i Nordsjælland. Tømrermester og bygningskonstruktør fra Hundested. Ring 50 70 05 05 for et tilbud.",
    h1="Nybyg: huse, gæstehuse og anneks",
    intro="Fritliggende byggeri på din grund. Vi bygger nye huse, gæstehuse, anneks, carporte og garager i Nordsjælland.",
    svar='Vi bygger nye huse, fritliggende gæstehuse, anneks, carporte og garager i Nordsjælland, ofte som hovedentreprise med én kontakt. Sebastian Rosendal er tømrermester og uddannet bygningskonstruktør. Du kan også få en carport eller garage i samme projekt. Efter besigtigelse af grunden får du et skriftligt tilbud med fast pris.',
    ind=["Gennemgang af grund og ønsker", "Tømrerarbejdet: konstruktion, tag, vinduer og døre", "Koordinering af murer, el, VVS, maler og kloak i hovedentreprise",
         "Tidsplan og løbende dialog", "Oprydning og aflevering"],
    sek=[
        ("Gæstehus eller anneks på egen grund", [
            "Et fritliggende anneks eller gæstehus bygges ude på grunden og kan bruges til gæster, kontor eller hobby. Vi taler med dig om, hvad bygningen skal kunne, og hvor den skal ligge, før vi går videre.",
        ]),
        ("Carport og garage", [
            "Carporte og garager bygger vi som selvstændige opgaver eller sammen med andet tømrerarbejde.",
        ]),
        ("Nyt hus i hovedentreprise", [
            ('html', '<p>Ved et nyt hus skal mange fag passe sammen. Som hovedentreprise har du én kontrakt og én kontakt, og vi koordinerer murer, el, VVS, maler og kloak. Læs mere under <a href="/hovedentreprise/">hovedentreprise</a>. Vil du udvide et eksisterende hus i stedet, se <a href="/tilbygning/">tilbygning</a>.</p>'),
        ][0]),
        ("Tegninger og byggetilladelse", [
            "Tegninger og beregninger laver vi ikke selv. Dem står din arkitekt eller ingeniør for, og vi bygger efter dem. Kommunen skal give tilladelse til et nyt hus, og vi gennemgår med dig, hvad der skal være klar, før første spade sættes i jorden.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller, hvad du vil bygge, og hvor."),
          ("Besigtigelse", "Vi ser på grunden og gennemgår tegninger, hvis de findes."),
          ("Fast tilbud", "Du får et tilbud med pris, omfang og tidsplan for hele byggeriet."),
          ("Byggeri og aflevering", "Vi bygger, koordinerer fagene og afleverer ryddet op.")],
    pris_intro='Prisen afhænger af, hvad der skal bygges, og hvor. Det spiller ind:',
    pris=["Bygningens type og størrelse", "Om der er tegninger og byggetilladelse på plads", "Valg af materialer til tag, facade og vinduer", "Hvor mange fag der skal koordineres", "Grundens beliggenhed og adgang"],
    faq=[
        ("Hvor lang tid tager det at bygge nyt?", "Det afhænger af størrelse og hvor mange fag der er involveret. Du får altid en tidsplan sammen med tilbuddet."),
        ("Laver I også tegninger?", "Nej, tegninger og beregninger laver vi ikke selv. Vi arbejder sammen med din arkitekt eller ingeniør og bygger efter tegningerne."),
        ("Kan I bygge anneks eller gæstehus på en sommerhusgrund?", "Det afhænger af lokalplanen og reglerne for området. Det afklarer vi sammen med dig ved besigtigelsen, inden vi giver tilbud."),
        ("Bygger I carporte og garager?", "Ja, både som selvstændige opgaver og sammen med andet tømrerarbejde."),
        ("Hvilke fag er med i en hovedentreprise?", "Vi koordinerer faste samarbejdspartnere inden for murer, el, VVS, maler og kloak og laver selv tømrerarbejdet. Du får ét samlet tilbud."),
    ],
    anm=['ulla']),

"pergola-hegn-og-cykelskur": dict(
    title="Pergola, hegn og cykelskur i træ | Rosendal Tømrer",
    desc="Pergolaer, hegn, cykeloverdækninger, skure og bænke i træ til private, boligforeninger og erhverv i Nordsjælland. Tømrere i Hundested. Ring 50 70 05 05.",
    h1="Pergola, hegn og cykelskur i træ",
    intro="Fra et enkelt skur til et helt gårdmiljø. Vi bygger i træ til private, boligforeninger og erhverv.",
    svar='Vi bygger pergolaer, hegn, skure, cykeloverdækninger, platforme og bænke i træ til private, boligforeninger og erhverv i Nordsjælland. Mange opgaver er gårdmiljøer, hvor flere skal bruge det samme sted hver dag. Prisen står i et skriftligt tilbud, som du får, når vi har set stedet.',
    ind=["Pergolaer og overdækninger", "Cykeloverdækninger og affaldsskure", "Platforme, bænke og siddemiljøer, også runde bænke omkring træer",
         "Hegn, plankeværk og læskærme", "Skure og redskabsrum"],
    sek=[
        ("Uderum der bliver brugt", [
            "En god gårdhave er et sted, folk faktisk opholder sig. Det kræver læ, steder at sidde og plads til cykler og affald, så resten af gården kan bruges til noget bedre.",
            "Vi bygger alt fra mindre hegn og skure til større pergolaer, cykeloverdækninger og platforme. Mange af opgaverne er for boligforeninger og erhverv, hvor flere skal kunne bruge det samme sted.",
        ]),
        ("Det har vi bygget", ('ul', [
            "Pergola, cykelstativer og skure i et gårdmiljø mellem etageboliger",
            "Runde bænke af træ omkring træer ved en erhvervsejendom",
            "Rund bænk med lameller i træ",
        ])),
        ("Vedligehold og holdbarhed", [
            "Træ i det fri skal tåle vejr og slid, og hvor meget vedligehold det kræver, afhænger af træsort og placering. Vi gennemgår valgene med dig, så du ved, hvad stedet kommer til at kræve over tid.",
        ]),
        ("Private og erhverv", [
            "Til private handler det ofte om læ og et rart sted at sidde. Til boligforeninger og erhverv er holdbarhed og vedligehold vigtigst, fordi mange bruger det hver dag. Vi tager en indledende snak om behov og forventninger, før vi giver tilbud.",
        ]),
    ],
    trin=[("Første snak", "Du fortæller, hvad pladsen skal bruges til, og hvem der bruger den."),
          ("Besigtigelse", "Vi ser på stedet og taler behov og forventninger igennem."),
          ("Fast tilbud", "Du får et tilbud på det, der skal bygges."),
          ("Bygning og aflevering", "Vi bygger og afleverer ryddet op.")],
    pris_intro='Prisen afhænger af, hvad der skal bygges, og hvor meget stedet skal kunne holde til. Det spiller ind:',
    pris=["Hvad der skal bygges, og hvor meget", "Valg af træ og overfladebehandling", "Hvor mange der skal bruge stedet, og dermed hvor robust det skal være", "Adgangen til stedet"],
    faq=[
        ("Laver I gårdhaver for boligforeninger?", "Ja. Vi bygger gårdmiljøer for både private, boligforeninger og erhverv, fra en enkelt cykeloverdækning til hele gården."),
        ("Kan I bygge en bænk rundt om et træ?", "Ja. Runde bænke og siddemiljøer bygges på mål, så de passer til træet og pladsen."),
        ("Hvem laver belægningen omkring?", "Den klarer en lokal anlægsgartner, vi samarbejder med, så du får hele gården ét sted fra."),
        ("Skal der byggetilladelse til et skur eller en pergola?", "Det afhænger af størrelse og placering, og kommunen afgør det. Vi gennemgår det med dig ved besigtigelsen."),
    ],
    billede=("/images/gaard-pergola-cykelskur.webp", "Gårdmiljø i træ med pergola, cykelstativer og skure mellem etageboliger"),
    galleri=[("/images/baenk-1.webp", "Rund træbænk omkring et træ i et gårdmiljø ved en erhvervsejendom"),
             ("/images/baenk-2.webp", "Rund bænk i træ med lameller, bygget af Rosendal Tømrer")],
    anm=[]),

}


# ---------------- MATERIELUDLEJNING ----------------
# Kilde: Sebastians Word-dokument "Rosendal Materiel Udlejning" (12 maskiner). Ingen andre kilder til maskiner
# eller priser. Tastefejl rettet (DDK, 230C, 1,26 n, Jordbordet). Udeladt indtil afklaret med Sebastian:
# stilladsklasse paa bukkestillads, affugterens rumstoerrelse og effekt. Se FAKTATJEK.md.
# Hver maskine: (id/anker, kategori, navn, tekst, specifikationer).
# Ingen priser paa sitet (moedet 23-10-2026): Sebastian krydstjekker priser og maskiner med Stark foerst.
# Priserne staar i hans Word-dokument, ikke her, saa de ikke ved et uheld kommer med i en build.
# id bruges som anker nu og som /materieludlejning/<id>/, hvis en maskine senere faar sin egen side.
MATERIEL_KATEGORIER = [
    ("el", "El-værktøj til leje i Hundested", "Til skæring og slibning, når du bygger eller renoverer indendørs."),
    ("bygning", "Bygningsmateriel til leje i Hundested", "Stillads, løft, varme og affugtning til byggepladsen og renoveringen."),
    ("jord", "Jord og anlæg til leje i Hundested", "Til haven, hegnet og byggeprojektet, når der skal bores huller eller flyttes jord."),
]
MATERIEL = [
    ("bordsav", "el", "Dewalt kompakt bordsav",
     "Bordsav med aluminiumsbord og kraftig 1850 W motor. Ideel til alle skæreopgaver.",
     ["Klinge Ø210 mm", "Maks. skæredybde 65 mm ved 90° og 45 mm ved 45°", "230 V"]),
    ("girafsliber", "el", "Festool girafsliber",
     "Let og enkel langhalssliber, der giver en bedre arbejdsstilling, med udtag til støvsuger.",
     ["Leveres uden slibenet og sandpapir"]),
    ("rullestillads", "bygning", "Jumbo rullestillads",
     "Til arbejde i højden. Stilladset er nemt at transportere og samle, og det kører på hjul.",
     ["Aluminium"]),
    ("bukkestillads", "bygning", "Jumbo bukkestillads",
     "Til mange slags opgaver. Bukkene kan justeres i højden fra 110 til 190 cm.",
     ["Vægt 20 kg", "Varmgalvaniseret"]),
    ("varmeblaeser", "bygning", "Varmeblæser 2 kW",
     "Hurtig og stabil varme til garage, byggepladsvogn og lignende, med enkel styring.",
     ["Effekt 2 kW", "Kraftig blæser"]),
    ("transportvogn", "bygning", "Ravendo transportvogn TW 2000",
     "Trækvogn med bremse til transport af materialer.",
     ["Længde 200 cm, bredde 100 cm, højde 47 cm", "Lastkapacitet 1.200 kg", "Egenvægt 88 kg", "Gummihjul på stålfælg"]),
    ("gipshejs", "bygning", "Raptor gipshejs",
     "Manuel hejs til montering af gipsplader op til 3,2 m. Leveres i 3 dele.",
     ["Samlet vægt 25 kg", "5 gummihjul, hvoraf ét kan låses"]),
    ("affugter", "bygning", "Master affugter DH 752",
     "Til mindre lokaler ved vandskader. Afrimer hurtigt og automatisk, og tanken har overløbssikring.",
     ["Tank 5,7 L", "Mulighed for afløbsslange", "230 V", "Vægt 30 kg"]),
    ("betonblander", "bygning", "Betonblander 120 L",
     "Til blanding af beton, cement og mørtel. Nem at håndtere og med sikkerhedsafbryder.",
     ["550 W motor, 230 V 50 Hz", "H 1,04 m, B 69 cm, D 1,26 m"]),
    ("dumper", "jord", "Scheppach dumper DP3000",
     "Kraftig dumper med 4-takts motor til alle slags underlag: byggeplads, skovbrug, landbrug og byggeprojekter.",
     ["Mål 133 × 81 × 103,8 cm", "Lad 91,2 × 65 × 56 cm", "Maks. belastning 300 kg", "3 gear og 1 bakgear"]),
    ("paelebor", "jord", "Pælebor",
     "Benzindrevet 2-takts pælebor. Ideelt til hegn i haven.",
     ["Tre bor: 100, 150 og 200 mm", "Olie og benzin 1:40", "Vægt med bor 11 til 12,5 kg"]),
    ("jordbor", "jord", "Mobilt jordbor",
     "Jordbor, der kan spændes på en kuglekobling, fx på en ATV eller havetraktor.",
     ["Bor på 127, 152, 203, 254 og 305 mm", "Motor 9 hk", "Vægt 168 kg"]),
]
MATERIEL_SIDE = dict(
    title="Materieludlejning i Hundested | Rosendal Tømrer",
    desc="Lej bordsav, stillads, betonblander, affugter, dumper og pælebor hos Rosendal Tømrer. Afhentning på Engdraget 11, 3390 Hundested. Ring for pris.",
    h1="Materieludlejning til private og erhverv i Hundested",
    intro="Lej det materiel, vi selv arbejder med, til dit eget projekt. Du henter det på Engdraget 11 i Hundested, så ring og hør, om det er ledigt.",
    svar="Hos Rosendal Tømrer i Hundested kan du leje bordsav, girafsliber, rullestillads, bukkestillads, varmeblæser, transportvogn, "
         "gipshejs, affugter, betonblander, dumper, pælebor og mobilt jordbor. Materiellet lejes pr. kalenderdag og afhentes på "
         "Engdraget 11 i Hundested. Ring på 50 70 05 05 for at høre, om det er ledigt, og book.",
    trin=[("Ring og fortæl, hvad du skal bruge", "Vi tjekker, om materiellet er ledigt, og hjælper dig med at vælge det rigtige."),
          ("Hent det i Hundested", "Du henter materiellet på Engdraget 11 efter aftale. Skal det leveres, så kontakt os for pris."),
          ("Aflever igen", "Materiellet afleveres til den aftalte tid og i samme stand, som du fik det.")],
    faq=[
        ("Hvor længe kan jeg leje?", "Materiellet lejes pr. kalenderdag, og en dag regnes som 8 timers brug. Bruger du det mere end 8 timer, tæller det som en ekstra dag. Ring og aftal, hvor mange dage du skal bruge det."),
        ("Hvad koster det at leje?", "Kontakt os for pris. Ring på 50 70 05 05, så får du prisen og hører samtidig, om materiellet er ledigt."),
        ("Kan jeg afbestille?", "Ja. Afbestilling skal ske senest 7 dage før den aftalte booking. Der opkræves et gebyr, som du får oplyst, når du booker."),
        ("Skal jeg selv sørge for brændstof?", "Ja. Benzindrevne maskiner, fx pæleboret, udlejes uden brændstof, og du skal selv påfylde korrekte væsker efter anvisningerne."),
        ("Hvad skal jeg bruge til hegn i haven?", "Til hullerne til hegnsstolperne kan du leje pæleboret med bor på 100, 150 og 200 mm. Det mobile jordbor kan spændes på fx en ATV eller havetraktor og har bor op til 305 mm. Skal der flyttes jord, kan dumperen tage op til 300 kg."),
        ("Hvad bruger jeg ved en vandskade?", "Affugteren Master DH 752 er til mindre lokaler. Den afrimer automatisk, har overløbssikring på tanken og kan tilsluttes en afløbsslange. Ring og fortæl om rummet, så hører du, om den passer til opgaven."),
        ("Kan I hjælpe med at vælge stillads?", "Ja. Vi er tømrere og bruger selv stilladserne, så ring og fortæl om opgaven. Så hjælper vi dig med at vælge mellem rullestillads og bukkestillads."),
        ("Lejer I ud til private?", "Ja. Vi lejer ud til både private og erhverv."),
        ("Hvor henter jeg materiellet?", "På Engdraget 11, 3390 Hundested, efter aftale. Skal det leveres, så kontakt os for pris."),
    ],
)
# Ydelsessider der linker til bestemte maskiner (og omvendt fra udlejningssiden)
MATERIEL_LINKS = {
    "terrasse": ["paelebor", "jordbor"], "pergola-hegn-og-cykelskur": ["paelebor", "jordbor"],
    "renovering": ["affugter", "gipshejs"],
    "tilbygning": ["betonblander", "dumper", "rullestillads"], "nybyg": ["betonblander", "dumper", "rullestillads"],
}


# ---------------- GUIDE: TRAE TIL TERRASSE ----------------
# Teksten er Christians udkast ud fra Sebastians svar. Sebastian har bedt om at laese den, foer den bruges.
# Indtil GODKENDT_AF_SEBASTIAN = True: siden findes kun paa testsiden (noindex), uden byline, uden links fra andre sider,
# og den er hverken i sitemap eller llms.txt. I live-builden bygges den slet ikke.
# Opfind intet: ingen haardhed, densitet, certificering, priser, herkomst, forbud eller "brun impraegneret".
GODKENDT_AF_SEBASTIAN = False
GUIDE_TRAE_TERRASSE = dict(
    title="Træ til terrasse: trykimprægneret, jatoba, ipé | Rosendal",
    desc="Guide til træ til terrasse: trykimprægneret, jatoba og ipé. Vedligehold, levetid og underkonstruktion, skrevet ud fra vores erfaring som tømrere.",
    h1="Træ til terrasse: trykimprægneret, jatoba eller ipé",
    byline="Skrevet af Rosendal Tømrer på baggrund af Sebastian Rosendals erfaring. Sebastian er uddannet tømrer (2010) og bygningskonstruktør (2018).",
    intro="Her forklarer vi, hvilket træ vi bygger terrasser i, hvad der afgør valget, og hvad der skal være i orden under brædderne. Det bygger på vores egen erfaring som tømrere. Guiden erstatter ikke et tilbud, for det rigtige valg afhænger af huset og placeringen.",
    svar="Vi bygger terrasser i trykimprægneret træ, jatoba og ipé. Trykimprægneret er den økonomiske løsning og males efter cirka et år. Jatoba og ipé er hårdttræ, som kan blive gråt eller olieres en gang om året. Placering og vejrpåvirkning vejer tungest, og underkonstruktionen afgør levetiden.",
    tabel=dict(hoved=["Træsort", "Fordele", "Ulemper", "Vedligehold"], raekker=[
        ["Trykimprægneret", "God holdbarhed til pengene", "Skal males", "Maling efter cirka et år"],
        ["Jatoba", "Hårdttræ", "", "Lad den blive grå, eller behandl en gang om året"],
        ["Ipé", "Hårdttræ", "Høj pris", "Lad den blive grå, eller behandl en gang om året"]]),
    sek=[
        ("Hvad afgør, hvilket træ vi anbefaler?", ["Placering og vejrpåvirkning vejer tungest. Terrasser tæt på vand er hårdere belastet end terrasser længere inde i landet. Derudover handler det om kundens økonomi. Vi fravælger ikke nogen træsorter, men finder den løsning, der passer til netop den kunde og det hus."]),
        ("Underkonstruktionen afgør meget", ('html', '<p>Det er ikke kun træet i overfladen, der bestemmer, hvor længe en terrasse holder. Tre ting er vigtige for os:</p>'
            '<ul><li>Ordentlig dimensionering af underkonstruktionen.</li><li>Strøtape ovenpå strøerne, som forlænger levetiden.</li>'
            '<li>Korrekt mellemrum mellem brædderne, så træet kan arbejde, når det udsættes for fugt.</li></ul>')),
        ("Vedligehold", ["Trykimprægneret træ behandles med maling. Hårdttræ kan stå uden behandling og blive gråt, og det tåler det godt, fordi det er hårdttræ. Vil man bevare træets farve, anbefaler vi olie en gang om året."]),
        ("Hvor længe holder en terrasse?", ["Efter vores erfaring holder en terrasse i trykimprægneret træ typisk 15 til 20 år, og en terrasse i hårdttræ 25 til 50 år eller mere. Tallene er et skøn ud fra vores erfaring og ikke en garanti. Levetiden afhænger af, hvordan underkonstruktionen er udført."]),
        ("Hvorfor vælger nogle kunder trykimprægneret fra?", ["Nogle kunder fortæller os, at de gerne vil væk fra behandlingsformen, fordi trykimprægnering tidligere var kraftigere og giftigere. Andre vælger trykimprægneret, fordi det giver god holdbarhed til prisen. Begge dele er et fornuftigt udgangspunkt for en snak om, hvad der passer til jer."]),
        ("Året rundt", ["Vi bygger på samme måde hele året. Men fyrretræ kan have et højt fugtindhold, når det lægges, og det skal man tage højde for."]),
    ],
    faq=[
        ("Hvilket træ skal jeg vælge til min terrasse?", "Det afhænger af placering, vejrpåvirkning og økonomi. Terrasser tæt på vand er hårdere belastet. Vi finder den løsning, der passer til netop jeres hus og budget."),
        ("Hvor længe holder en terrasse?", "Efter vores erfaring typisk 15 til 20 år i trykimprægneret træ og 25 til 50 år eller mere i hårdttræ, afhængigt af underkonstruktionen. Det er et skøn og ikke en garanti."),
        ("Skal en terrasse i hårdttræ behandles?", "Nej, den kan stå ubehandlet og blive grå. Vil man bevare farven, anbefaler vi olie en gang om året."),
        ("Skal trykimprægneret træ males?", "Ja, vi anbefaler maling efter cirka et år."),
        ("Hvad gør en terrasse mere holdbar?", "En ordentligt dimensioneret underkonstruktion, strøtape ovenpå strøerne og korrekt mellemrum mellem brædderne."),
        ("Hvad koster en terrasse?", "Det afhænger af træsort og størrelse. Ipé er den dyreste af de tre. Kontakt os, så giver vi et tilbud."),
        # Udkastet siger "Mest i Nordsjaelland. Vi tager ogsaa opgaver i hovedstadsomraadet ...". Efter moedet 23-10-2026 bruger
        # sitet arbejdsomraadet i stedet for Hovedstadsomraadet, saa svaret foelger det. Sebastian afgoer det ved godkendelsen.
        ("Hvor bygger I terrasser?", "Mest i Nordsjælland. Vores arbejdsområde går fra Hundested til Frederikssund, Stenløse, Farum og Hørsholm, og opgaver længere væk tager vi også imod, når projektet passer til os."),
    ],
)
