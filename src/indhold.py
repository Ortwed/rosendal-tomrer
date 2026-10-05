"""Alt tekstindhold. Udkast: skal faktatjekkes med Sebastian (se FAKTATJEK.md)."""

# Verificerede anmeldelser fra anmeld-haandvaerker.dk (hentet 04-10-2026). Fornavn + by.
ANMELDELSER = {
    "ulla": ("Nyt tag hos min mor. Ny carport hos mig selv.",
             "Nem at få kontakt til. Meget imødekommende og problemløsning helt i top. Kan varmt anbefale firmaet, de svende jeg har haft kontakt med, også helt i top.",
             "Ulla", "Hundested", "oktober 2026"),
    "peter": ("Nye vinduer og to franske altaner", "Super flot udført.", "Peter", "Hundested", "august 2026"),
    "morten": ("Repos-trappe i ipé",
               "Vi fik bygget et fem meter langt repos-trin i ipé fra foldedør ned til eksisterende stenterrasse. Tilbud, udførsel, oprydning og fakturering kørte helt som aftalt, og resultatet er super flot.",
               "Morten", "Veksø", "juli 2026"),
    "anne": ("Vinduer og terrasse", "Alle aftaler overholdt og rigtig flot arbejde.", "Anne", "Hundested", "juni 2026"),
    "anita": ("Nye døre og vinduer",
              "To tømrere satte et badeværelsesvindue, et køkkenvindue og to yderdøre i. Begge meget venlige og serviceminded. Alle aftaler er overholdt til punkt og prikke.",
              "Anita", "Vejby", "april 2026"),
    "elisabeth": ("Dør, paneler og terrassedør", "Montering af dør, paneler og reparation af terrassedør.", "Elisabeth", "Hundested", "februar 2026"),
    "erik": ("Nye bærende stolper ved indgangen",
             "Meget fin oplevelse fra første dialog med firmaet og indtil arbejdet var færdigt. Pænt arbejde og rigtig fin oprydning.",
             "Erik", "Hundested", "januar 2026"),
    "brian": ("Renovering af sommerhus med nyt tag",
              "Nye vægge og gulv med isolering og nyt tag. Sebastian er altid til at få fat på, og hans ansatte er både dygtige og søde. Alle aftaler er overholdt, derfor fuld plade herfra.",
              "Brian", "Hundested", "februar 2026"),
    "rita": ("Tilbygning og gæstehus",
             "Tømrerfirma med fokus på virkelig godt håndværk. Overholder aftaler og informerer fint, hvis der er problemer. Et firma jeg har været 100 % tryg ved.",
             "Rita", "Hundested", "november 2025"),
    "nila": ("Vindue", "God kommunikation, levering til tiden og hurtigt arbejde.", "Nila", "Hillerød", "oktober 2025"),
}

# Ydelsessider. Hver: title, desc, h1, intro, sektioner [(h2, [afsnit...] eller ('ul', [...]))], faq, anmeldelse
YDELSER = {
"hovedentreprise": dict(
    title="Hovedentreprise og fagentreprise i Nordsjælland",
    desc="Vi tager hovedentreprisen på nybyg, tilbygning og renovering og koordinerer murer, elektriker og VVS. Én kontrakt og én kontakt. Tømrermester i Hundested.",
    h1="Hoved- og fagentreprise",
    intro="Én kontrakt, én kontakt og ét ansvar. Vi styrer hele byggeriet og koordinerer de andre fag, så du ikke skal.",
    sek=[
        ("Hvad betyder hovedentreprise for dig?", [
            "Ved en hovedentreprise har du kun én aftalepart: os. Vi indhenter tilbud fra murer, elektriker, VVS, maler og de andre fag, vi lægger tidsplanen, og vi står for at fagene kommer i den rigtige rækkefølge.",
            "Går noget skævt mellem to fag, er det vores problem at løse og ikke dit. Det er den største forskel i hverdagen: du skal ikke selv være byggeleder ved siden af dit arbejde.",
        ]),
        ("Tømrermester og bygningskonstruktør", [
            "Sebastian er både tømrermester og uddannet bygningskonstruktør. Det betyder at vi kan hjælpe med planlægning og tegninger tidligt i projektet, og at vi kender konstruktionen indefra, når det skal bygges.",
            "Vi taler også gerne med din arkitekt eller ingeniør, hvis projektet allerede er tegnet.",
        ]),
        ("Typiske opgaver i hovedentreprise", ('ul', [
            "Tilbygninger og nye boliger",
            "Totalrenovering af hus eller sommerhus",
            "Gæstehuse, anneks og udhuse",
            "Nyt tag med efterisolering og nye vinduer i samme projekt",
        ])),
        ("Foretrækker du fagentreprise?", [
            "Har du selv styr på de andre fag, eller vil du stå for koordineringen, laver vi også tømrerarbejdet som ren fagentreprise. Vi siger ærligt hvad vi tror passer bedst til dit projekt.",
        ]),
    ],
    faq=[
        ("Hvad er forskellen på hovedentreprise og totalentreprise?", "Ved en hovedentreprise udfører vi byggeriet efter et projekt, som enten du eller en rådgiver har fået tegnet. Ved en totalentreprise står entreprenøren også for projekteringen. Vi hjælper gerne med begge dele og gennemgår forskellen konkret for jeres projekt."),
        ("Er hovedentreprise dyrere end at hyre fagene selv?", "Der er et tillæg for koordineringen, men til gengæld slipper du for spildtid mellem fagene og for selv at bære risikoen, når de skal passe sammen. Vi lægger tallene frem, så du kan vurdere det."),
        ("Hjælper I med byggetilladelse?", "Ja. Vi kan hjælpe med tegninger og ansøgning til kommunen, eller samarbejde med den rådgiver du allerede har."),
        ("Hvilke fag samarbejder I med?", "Vi har faste samarbejdspartnere inden for murer, el, VVS, maler og kloak i Nordsjælland. Du får ét samlet tilbud."),
    ],
    anm="brian"),
"nybyg": dict(
    title="Nybyg og tilbygning i Nordsjælland · Rosendal",
    desc="Tilbygning, anneks, gæstehus eller nyt hus. Tømrermester og bygningskonstruktør fra Hundested, der tager byggeriet fra tegning til aflevering.",
    h1="Nybyg og tilbygning",
    intro="Mere plads uden at flytte. Vi bygger tilbygninger, gæstehuse og nye boliger i hele Nordsjælland.",
    sek=[
        ("Fra idé til færdigt byggeri", [
            "En tilbygning skal se ud som om den altid har hørt til huset. Det handler om taghældning, vinduesplacering, materialer og om hvordan det nye rum hænger sammen med resten af boligen.",
            "Vi starter med at se på huset og høre hvad pladsen skal bruges til. Derefter laver vi et oplæg, og når det er på plads, et fast tilbud med tidsplan.",
        ]),
        ("Det bygger vi", ('ul', [
            "Tilbygninger til bolig og sommerhus",
            "Gæstehuse og anneks",
            "Carporte, garager og udhuse",
            "Nye huse i hovedentreprise",
        ])),
        ("Gæstehus eller tilbygning?", [
            "Et fritliggende gæstehus kan være enklere at bygge, fordi det ikke skal kobles på det eksisterende hus. En tilbygning giver til gengæld mere sammenhængende plads i hverdagen. Vi gennemgår fordele og ulemper ved jeres grund og hus, før I beslutter jer.",
        ]),
    ],
    faq=[
        ("Skal jeg have byggetilladelse til en tilbygning?", "Som udgangspunkt ja, når der bygges til selve boligen. Reglerne afhænger af størrelse, placering og lokalplan. Vi hjælper med at afklare det og med ansøgningen."),
        ("Hvad med carport og udhus?", "Mindre småbygninger kan ofte opføres uden byggetilladelse, men der gælder regler for areal, højde og afstand til skel. Kommunen har det sidste ord, og vi tjekker det sammen med dig før vi bygger."),
        ("Hvor lang tid tager en tilbygning?", "Det afhænger af størrelse og hvor mange fag der er involveret. Du får altid en tidsplan sammen med tilbuddet, så du ved hvad du kan regne med."),
        ("Kan vi bo i huset mens I bygger til?", "Som regel ja. Vi planlægger arbejdet så der først åbnes ind til det eksisterende hus, når tilbygningen er lukket og tæt."),
    ],
    anm="rita"),
"tag": dict(
    title="Nyt tag og tagrenovering i Nordsjælland · Rosendal",
    desc="Nyt tag, tagrenovering og efterisolering i Nordsjælland. Vi tager hele tagprojektet, fra nedtagning af det gamle tag til et tæt og færdigt resultat.",
    h1="Nyt tag og tagrenovering",
    intro="Et tag skal holde i mange år. Vi skifter, renoverer og efterisolerer tage på huse og sommerhuse i Nordsjælland.",
    sek=[
        ("Hele tagprojektet", [
            "Et nyt tag er mere end nye plader eller sten. Undertag, lægter, inddækninger og ventilation skal spille sammen, ellers får man problemer med fugt længe før selve tagbelægningen er slidt op.",
            "Vi gennemgår taget og spærene inden vi giver tilbud, så du ved om der er skjulte skader der skal udbedres samtidig.",
        ]),
        ("Det laver vi", ('ul', [
            "Nyt tag på eksisterende hus eller sommerhus",
            "Udskiftning af undertag og lægter",
            "Efterisolering i forbindelse med tagskifte",
            "Ovenlysvinduer og kviste",
            "Reparation af tagudhæng, stern og vindskeder",
        ])),
        ("Gamle eternittage", [
            "Ældre eternittage kan indeholde asbest, og så skal nedtagningen håndteres efter særlige regler. Vi får det afklaret før arbejdet går i gang, så både du og vores folk er trygge.",
        ]),
    ],
    faq=[
        ("Hvornår skal mit tag skiftes?", "Typiske tegn er knækkede eller porøse plader, fugtpletter på loftet og et undertag der er gået i stykker. Vi kommer gerne ud og giver en ærlig vurdering af om det kan repareres, eller om det er tid til et nyt."),
        ("Kan I efterisolere samtidig med at taget skiftes?", "Ja, og det er det bedste tidspunkt at gøre det på, fordi taget alligevel er åbent."),
        ("Hvad sker der hvis det regner undervejs?", "Vi åbner kun så meget af taget ad gangen, som vi kan nå at lukke igen, og dækker af når det er nødvendigt."),
        ("Leverer I også stillads?", "Ja. Vi har selv stillads og trailer, så det er med i tilbuddet."),
    ],
    anm="ulla"),
"doere-og-vinduer": dict(
    title="Udskiftning af døre og vinduer i Nordsjælland",
    desc="Nye vinduer, yderdøre, terrassedøre og franske altaner i Nordsjælland. Korrekt montering og tætning udført af tømrere fra Hundested.",
    h1="Døre og vinduer",
    intro="Nye vinduer og døre giver et lunere hus og et pænere udtryk. Vi står for opmåling, levering og montering.",
    sek=[
        ("Monteringen er det vigtigste", [
            "Et godt vindue kan blive et dårligt vindue, hvis det sættes forkert i. Fugerne skal være tætte både inde og ude, og vinduet skal sidde rigtigt i muren, så der ikke opstår kuldebroer og fugt.",
            "Vi tager os af det hele: opmåling, valg af produkt, montering, lysninger og fuger, så du står med et færdigt resultat.",
        ]),
        ("Det skifter og monterer vi", ('ul', [
            "Vinduer i træ og træ/alu",
            "Yderdøre og terrassedøre",
            "Foldedøre og skydedøre",
            "Franske altaner",
            "Ovenlysvinduer",
        ])),
        ("Træ eller træ/alu?", [
            "Træ/alu-vinduer kræver mindre vedligehold udvendigt, mens rene trævinduer ofte passer bedst til ældre huse. Vi hjælper dig med at vælge ud fra hus, beliggenhed og budget.",
        ]),
    ],
    faq=[
        ("Hvor lang tid tager det at skifte et vindue?", "Et almindeligt vindue skiftes typisk på få timer, og hullet i facaden er kun åbent kort tid. Ved større opgaver planlægger vi rækkefølgen, så huset ikke står åbent natten over."),
        ("Kan I lave en fransk altan i et eksisterende hus?", "Ja. Det kræver som regel at hullet i muren gøres større, og det kan kræve tilladelse. Vi hjælper med at afklare det."),
        ("Hvad med lysninger og indvendig afslutning?", "Det er med i opgaven. Du skal ikke have en maler eller anden håndværker ind bagefter for at gøre det færdigt, medmindre du ønsker det."),
        ("Leverer I selv vinduerne?", "Ja, vi bestiller og leverer vinduer og døre, så du kun har ét sted at henvende dig, også hvis der skulle være noget med produktet senere."),
    ],
    anm="anita"),
"terrasse": dict(
    title="Træterrasse og trappetrin i Nordsjælland · Rosendal",
    desc="Træterrasser, repos og trappetrin i ipé og andre træsorter. Vi bygger terrassen med en stabil underkonstruktion, så den holder i mange år.",
    h1="Terrasser i træ",
    intro="En terrasse er hverdagens udestue. Vi bygger træterrasser, repos og trappetrin i Nordsjælland.",
    sek=[
        ("Det der ikke ses, betyder mest", [
            "En træterrasse står eller falder med underkonstruktionen. Afstand mellem strøer, luft under brædderne og afvanding afgør, om terrassen ligger plant og tørt om ti år.",
            "Derfor starter vi altid med fundamentet og konstruktionen, før vi taler om brædder og overflade.",
        ]),
        ("Det bygger vi", ('ul', [
            "Træterrasser i hårdttræ og nåletræ",
            "Repos og trappetrin fra dør til have",
            "Hævede terrasser på skrå grunde",
            "Terrasser med indbygget bænk eller plantekasse",
        ])),
        ("Valg af træ", [
            "Hårdttræ som ipé er tungt, tæt og holdbart, men koster mere. Trykimprægneret træ er billigere og fint til mange opgaver. Vi gennemgår forskellen på holdbarhed, udseende og vedligehold, så du kan vælge med åbne øjne.",
        ]),
    ],
    faq=[
        ("Hvilket træ holder længst?", "Tætte hårdttræsorter som ipé holder typisk længst og kræver mindst vedligehold. Vi rådgiver ud fra hvordan terrassen skal bruges, og hvor meget sol og fugt den får."),
        ("Kan I bygge videre på en eksisterende stenterrasse?", "Ja. Vi har fx bygget et fem meter langt repos-trin i ipé fra en foldedør ned til en eksisterende stenterrasse."),
        ("Skal terrassen behandles?", "Det afhænger af træsorten og det udtryk du ønsker. Lader man træet stå ubehandlet, bliver det sølvgråt med tiden."),
        ("Laver I også belægning omkring terrassen?", "Belægning og haveanlæg laver vi i samarbejde med en lokal anlægsgartner, så du kan få det hele i ét projekt."),
    ],
    anm="morten"),
"gaardhaver": dict(
    title="Gårdhaver, udestuer og overdækning · Rosendal",
    desc="Overdækket gårdhave, udestue eller pergola. Vi bygger uderum i træ, der kan bruges en større del af året. Tømrer i Nordsjælland.",
    h1="Gårdhaver og udestuer",
    intro="Et overdækket uderum forlænger sæsonen. Vi bygger gårdhaver, udestuer og pergolaer i træ.",
    sek=[
        ("Et rum mellem hus og have", [
            "En overdækket gårdhave giver læ og skygge, og den kan bruges i regnvejr og sent på året. Med glas i siderne bliver den til en udestue, der kan bruges endnu mere.",
            "Vi tegner konstruktionen, så den passer til husets tag og facade, og så tagvandet bliver ført væk det rigtige sted.",
        ]),
        ("Det bygger vi", ('ul', [
            "Overdækkede gårdhaver",
            "Udestuer og vinterhaver",
            "Pergolaer og halvtage",
            "Læhegn og afskærmning i træ",
        ])),
    ],
    faq=[
        ("Kræver en overdækning byggetilladelse?", "Det afhænger af størrelse og placering i forhold til skel. Vi hjælper med at afklare det med kommunen før vi bygger."),
        ("Hvilket tag skal der på?", "Det kommer an på hvor meget lys du vil have igennem. Klare plader giver lys, mens et tæt tag giver mere skygge og læ. Vi viser dig mulighederne."),
        ("Kan I bygge en udestue på et eksisterende hus?", "Ja. Den kobles på huset ligesom en tilbygning, og vi sørger for at samlingen mod facade og tag bliver tæt."),
    ],
    anm="anne"),
"renovering": dict(
    title="Renovering af hus og sommerhus · Rosendal Tømrer",
    desc="Renovering af hus og sommerhus i Nordsjælland: vægge, gulve, isolering, lofter og indvendigt tømrerarbejde. Én kontakt gennem hele forløbet.",
    h1="Renovering",
    intro="Fra et enkelt rum til hele huset. Vi renoverer boliger og sommerhuse i Nordsjælland, både indvendigt og udvendigt.",
    sek=[
        ("Renovering kræver overblik", [
            "Når man åbner op i et ældre hus, finder man ofte noget man ikke havde regnet med. Vi siger det med det samme, forklarer mulighederne og aftaler prisen med dig, før vi går videre.",
            "Mange renoveringer involverer flere fag. Vi kan tage hele opgaven som hovedentreprise, så du kun har én kontakt.",
        ]),
        ("Det renoverer vi", ('ul', [
            "Nye vægge, gulve og lofter",
            "Efterisolering af vægge, gulv og loft",
            "Indvendige døre, paneler og lister",
            "Udskiftning af bærende stolper og rådne konstruktioner",
            "Sommerhuse der skal gøres klar til mange flere år",
        ])),
        ("Sommerhuse", [
            "Mange af vores opgaver ligger i sommerhusområderne omkring Hundested og Nordkysten. Her er efterisolering, nyt tag og nye vinduer ofte det der gør huset brugbart en større del af året.",
        ]),
    ],
    faq=[
        ("Hvad hvis I finder skjulte skader?", "Så stopper vi op, viser dig hvad vi har fundet, og giver en pris på udbedringen, før vi fortsætter. Du skal aldrig blive overrasket over regningen."),
        ("Kan vi bo i huset under renoveringen?", "Ofte ja. Vi planlægger arbejdet så der er mindst muligt rod og støv i de rum, I bruger."),
        ("Rydder I op efter jer?", "Ja. Oprydning er en del af opgaven, både undervejs og når vi afleverer."),
        ("Laver I små opgaver også?", "Ja. Vi skifter også en enkelt dør, et par paneler eller en rådden stolpe. Ring og fortæl hvad det drejer sig om."),
    ],
    anm="erik"),
"materieludlejning": dict(
    title="Materieludlejning: stillads og trailer · Rosendal",
    desc="Lej stillads og trailer hos Rosendal Tømrer i Hundested. Ring og hør hvad vi har ledigt, og hvordan afhentning og levering foregår.",
    h1="Materieludlejning",
    intro="Vi lejer stillads og trailer ud, når vi ikke selv bruger det. Ring og hør hvad der er ledigt.",
    sek=[
        ("Hvad kan du leje?", [
            "Vi har stillads og trailer, som vi bruger på vores egne opgaver. Når det står ledigt, kan du leje det til dit eget projekt.",
            "Ring til os og fortæl hvad du skal bruge, og hvornår. Så finder vi ud af om det kan lade sig gøre, og hvordan afhentning eller levering skal foregå.",
        ]),
        ("Godt at vide", ('ul', [
            "Afhentning fra Engdraget 11 i Hundested efter aftale",
            "Vi forklarer gerne hvordan stilladset sættes korrekt op",
            "Pris efter aftale og lejeperiode",
        ])),
    ],
    faq=[
        ("Kan I levere og stille stilladset op?", "Det kan aftales. Ring og fortæl om opgaven, så finder vi den bedste løsning."),
        ("Hvor længe kan jeg leje?", "Det afhænger af hvornår vi selv skal bruge materiellet. Vi aftaler en periode, når du ringer."),
    ],
    anm=None),
}
