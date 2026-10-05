# Naturpåvirkning: mandat, metode og datakontrakt

Versjon 1.0, 2026-10-01. Brukeren godkjente dette hovedsporet og en pilot før videre nasjonal kartlegging. Metoden er prosjektets arbeidsstandard; den er ikke i seg selv en utført konsekvensutredning.

## Formål og ansvar

For hvert datasenter undersøker vi fire spørsmål: Hvilke naturverdier fantes før inngrep? Hva er planlagt eller faktisk endret? Hvilke konsekvenser er faglig vurdert eller observert? Hva vet vi ennå ikke?

Natur er et eget hovedspor på samme nivå som kraft og økonomi. Prosjektet kan ikke merkes ferdig kartlagt ved å fylle ut et generelt felt om kjøling eller spillvarme. En egen dokumentansvarlig leser naturutredninger og myndighetsmerknader, en GIS-ansvarlig gjør etterprøvbare kartspørringer, og en annen kontrollør sjekker avgrensningene. Koordinatoren eier datakontrakten og publiseringsstatusen.

## Pilot og geografisk analyseenhet

| Pilot | Hva metoden skal prøve | Kritisk avgrensning |
|---|---|---|
| Gromstul, Skien | Sammenholde reguleringsplan, naturutredning og kartdata | Hele planområdet er ikke faktisk nedbygging |
| Heggvin, Hamar | Kontrollere planversjon og naturdata over tid | Hamar 079500 og tilgrensende Løten-planer må holdes atskilt |
| Narvik/Kvandal | Undersøke campus og tilknyttet kjølevann hver for seg | Kjølevannsplan 2026007 er ikke hele campusens planområde |

Piloten tester arbeidsflyten. Den er ikke representativ for alle norske datasentre. Prosjektene er valgt på grunnlag av eksisterende kildespor, planomriss og ulike avgrensningsbehov, ikke en antakelse om størst eller minst naturpåvirkning.

## 1. Dokumentkontroll

Søk i kommunens planregister og politiske saker, vedlegg til søknad, NVE og miljømyndighetenes uttalelser. Logg søk, tilgang og dokumentkobling. Skill mellom full natur-KU, avgrenset fagnotat, planprogram som bestiller fremtidig utredning, miljøoppfølgingsplan og myndighetsuttalelse.

En dokumentpost skal minst registrere prosjekt/komponent, plan-ID, dokumentdato og revisjon, utgiver/forfatter og oppdragsgiver, geografisk dekning, undersøkt prosjektalternativ, feltarbeidsdato/-sesong, undersøkte artsgrupper, metodikk og rødlisteutgave. Publisert rapportdato og feltarbeidsdato er ulike felt.

Fang opp fagutreders egne begrensninger og hva som ikke er undersøkt. Registrer myndighetsmerknader, innsigelser og eventuelle tilsvar med dato og status. Et krav om utredning dokumenterer ikke at den er gjennomført. At en KU finnes dokumenterer ikke at kunnskapen er fullstendig eller at planen er miljømessig uproblematisk.

Bruk disse tilgangsstatusene: `found_fulltext`, `found_reference_only`, `planned_not_obtained`, `not_found_in_search`, `access_failed`. Den siste gruppen er ikke bevis for at dokumentet ikke eksisterer. Dokumentets relevans og dekning vurderes separat fra tilgang.

Vurder naturverdi, påvirkning og konsekvens som separate størrelser. Behold kildens vurderingsskala og metodeår, og merk alle gjengivelser som utreders konklusjon. Vår kartanalyse skal ikke automatisk overstyre eller gjenbruke en faglig konsekvensgrad.

Metodisk referanse: [Miljødirektoratets M-1941](https://www.miljodirektoratet.no/konsekvensutredninger), lest 2026-10-01; publiseringsdato ikke vist i den leste siden. Håndboken gjelder kartlegging og utredning av klima- og miljøtema, med detaljering tilpasset plannivået.

## 2. Førtilstand og arealendring

Lagre ulike geometrier og datoer for planområde, foreslått inngrep, midlertidig anleggsareal, observert inngrep og tilknyttet infrastruktur. Et adressepunkt eller planomriss er ikke erstatning for et faktisk inngrepspolygon.

Velg førbilder fra før første dokumenterte inngrep, ikke bare før offisiell byggestart. Behold flyfotoprosjekt-ID, opptaksdato, oppløsning, produsent, bruksvilkår og kartreferanse. Sammenlign mot daterte etterbilder og dokumenter skygge, snø, sesong og tvetydig klassifisering. Logging av et flybildes eksistens er ikke det samme som å ha tolket bildet.

Der geometrien tillater det, beregn endring per arealklasse. Tegning eller klassifisering skal ha metode, person/verktøyversjon og uavhengig kontroll. Avskoging må ikke uten videre likestilles med permanent nedbygging eller tilskrives datasenteret; koblingen til prosjektet må dokumenteres.

Kartverkets [Norge i bilder](https://www.kartverket.no/om-kartverket/nyheter/geodataarbeid/2026/juli/norge-i-bilder-er-oppgradert) tilbyr historiske og nyere ortofoto med opptaksinformasjon. Kildesiden er publisert 02.07.2026, oppdatert 03.07.2026, lest 01.10.2026. Offentlig innsyn gir ikke automatisk rett til nedlasting og videredistribusjon av alle bilder; rettigheter kontrolleres per leveranse.

## 3. Autoritative kartlag og analyse

| Tema | Foretrukket datagrunnlag | Hva dataene kan støtte |
|---|---|---|
| Naturtyper | Naturbase, Miljødirektoratets instruks og eldre DN-håndbok 13/19 | Registrert naturtype, lokalitetskvalitet, verdi og kartleggingsår etter angitt metode |
| Vern | Miljødirektoratets verneområder | Geografisk og datert vernestatus; ikke komplett kart over naturverdier |
| Arter og funksjonsområder | Artskart, arter av nasjonal forvaltningsinteresse, relevante fagkart | Dokumenterte funn og registrerte leve-/funksjonsområder med presisjon og dato |
| Skog, myr og jord | NIBIO AR5, tilgjengelige skog-/MiS-data | Arealressurser og særskilte registreringer; ingen automatisk økologisk tilstandsvurdering |
| Grove økosystemer | Nasjonalt grunnkart for arealanalyse | Sammenlignbar arealdekkeoversikt, ikke detaljert naturverdi |
| Vann og sjø | Vann-Nett, aktuelle marine naturtypedata og fagutredninger | Vannforekomst, registrert tilstand, påvirkningshistorikk og marine naturverdier |
| Kartleggingsdekning | Kartleggingsområder/prosjektgrenser og originalrapport | Hvor, når og etter hvilken instruks det faktisk er kartlagt |

For hvert lag lagres dataeier, datasett-/lag-ID, tjeneste-URL, lisens, kilde-CRS, uttrekksdato, datasettversjon/oppdatering og objektets egen kartleggingsdato. At en tjeneste er nylig oppdatert betyr ikke at lokaliteten er nylig undersøkt. WMS-bilder kan brukes til innsyn; etterprøvbare arealberegninger trenger egnede vektor-/rasterdata og dokumentert behandling.

Søk først etter kandidater. Skill `bbox_candidate`, `conditional_polygon_intersection` og `verified_polygon_intersection`. En treffliste fra en omsluttende firkant er ikke en liste over lokaliteter inne i prosjektet. Et geometrisk treff under antatt CRS beholder forbeholdet selv om algoritmen er korrekt. Ingen direkte arealbeslags- eller naturtapstall publiseres fra disse foreløpige treffene.

For godkjente geometriske analyser må kilde-CRS og eventuell transformasjon være dokumentert; prosjektets geometrirolle og revisjon må være kjent. Hent alle resultatsider, sjekk feilmeldinger og tjenestens maksimale antall treff. Arkiver forespørsel, råsvar, sjekksum og kodeversjon. Et API-svar med feil eller avkuttede data må aldri tolkes som null treff.

Ved arealberegning oppgis både overlapp i m²/dekar og andel av den berørte naturlokaliteten, med fornuftig avrunding. Dette beskriver geografisk overlapp. Økologisk betydning vurderes separat. Ikke summer samme lokalitet flere ganger fordi den finnes i både gammel og ny kartlegging eller flere temalag.

## 4. Artsdata og kartleggingsdekning

Registrer artsnavn/takson-ID, observasjons-ID og opprinnelig dataeier, funndato, presisjon, dokumentert kvalitet, kartleggingsmetode og eventuell generalisering. Dedupliser samme observasjon som formidles gjennom flere portaler. Antall observasjoner eller antall registrerte arter skal ikke brukes som sammenlignbar biodiversitetsscore uten standardisert innsats og begrunnet analyse.

Et usikkert eller generalisert punkt nær en plangrense gir usikker geografisk tilordning. Behold offentlig generaliseringsnivå for skjermede funn, og ikke forsøk å rekonstruere presise lokaliteter. Artskart gjør begrenset kvalitetskontroll; original dataeier har ansvar for innholdet, og noen sensitive funn er skjermet. [Artsdatabankens dokumentasjon](https://artsdatabanken.no/kart/artskart/kvalitetssikring-og-foredling-av-data-i-artskart), publiseringsdato ikke oppgitt, lest 2026-10-01.

Kartleggingsdekning vurderes per tema og tidspunkt. Et kartlagt område kan være undersøkt for utvalgte naturtyper uten at alle artsgrupper er undersøkt. Skill fullført kartlegging med angitt metode, delvis dekning, ukjent dekning, ingen registrerte treff og teknisk mislykket søk. Ingen av de siste tre dokumenterer lav naturverdi.

Metode- og rødlisteversjoner beholdes. Miljødirektoratet beskriver en overgangsordning i 2026: kartlegging på land etter instruksen fra 2024 bygger fortsatt på rødliste 2018, mens ny instruks basert på rødliste 2025 og NiN3 er planlagt fra 2027. Gamle DN13/19-vurderinger krever eget samsvar mellom naturtypene ved oppdatering. Vi skal derfor ikke automatisk erstatte historiske kategorier med nyeste rødliste. [Offisiell metodebeskrivelse](https://www.miljodirektoratet.no/ansvarsomrader/overvaking-arealplanlegging/naturkartlegging/myndigheter/kartlegging-av-naturtyper-etter-miljodirektoratets-instruks/kartlegging-av-naturtyper-pa-land/), publiseringsdato ikke oppgitt, lest 2026-10-01.

## 5. Indirekte og samlet påvirkning

Kartlegg prosjektbundet vei, kraftnett, transformatorstasjoner, massedeponier, vannuttak, kjølevannsledninger og utslippspunkt som egne komponenter. Skill eksisterende anlegg fra nye tiltak, og dedikerte tiltak fra delt infrastruktur. Ingen vilkårlig prosentandel av et felles inngrep tilskrives datasenteret.

Påvirkningsområdet begrunnes for hver mekanisme: hydrologisk sammenheng, vannforekomst, støyberegning, lys, fragmentering eller dokumentert økologisk funksjon. En søkebuffer er bare et søkeområde. Nærmeste vannforekomst er ikke nødvendigvis mottaker for utslipp. Hydrologisk kobling, vannmengder og temperatur-/utslippsdata må være dokumentert før en konkret effekt kan vurderes.

Samlet belastning beskrives mot andre dokumenterte inngrep i samme økologiske system og tidsperiode. Skille mellom lokal direkte påvirkning og scenarioer for økt kraftproduksjon; ikke tilordne hypotetiske nasjonale naturinngrep til ett anlegg uten modellgrunnlag.

Avbøtende tiltak registreres etter trinn og status: unngå, begrense, restaurere eller kompensere; foreslått, vedtatt, gjennomført eller effektmålt. En lovet restaurering trekkes ikke fra dokumentert naturtap. Vurderingsgrunnlaget for spillvarme, klimaeffekt og naturpåvirkning beholdes separat.

## 6. Naturkort og maskinlesbare data

Hvert naturkort har fire synlige deler: `baseline`, `change`, `consequence`, `knowledge_gap`. Kortet skal vise hvem som fremsetter hvert utsagn og hvilket nivå evidensen støtter: utredningsfunn, myndighetsutsagn, foreløpig geografisk treff, dokumentert endring eller kunnskapshull.

`research/natur/naturkort.json` er det normaliserte pilotuttrekket. Skjemaet `research/natur/naturkort.schema.json` definerer felt, kildekrav, kontrollstatus og usikkerhet. Underlagsfiler beholdes i tillegg; normalisering må ikke miste deres begrensninger. Narvik er en pilotkandidat fra utvidelseskøen og blir ikke automatisk et godkjent hovedregisterobjekt.

Planlagt og faktisk påvirkning har separate felt. Kartleggingskvalitet og konsekvens er to ulike dimensjoner. Vi bruker ingen samlet naturpoengsum og ingen grønn «ufarlig»-etikett basert på null treff. Kort uten fullstendig grunnlag merkes `screening_only` eller `insufficient_evidence`.

Usikkerhet oppgis per utsagn, ikke som en felles prosent for prosjektet. Statistiske konfidensintervall krever metode og datagrunnlag. Dokumenterte spenn og følsomhetsanalyser merkes etter hva de faktisk beskriver; tids-, arts- og stedfestingsusikkerhet behandles eksplisitt.

## Publiseringskrav og pilotens ferdigkriterier

1. Tre naturkort med kilder, geografisk avgrensning og synlige hull; tomme felt gis aldri verdien 0.
2. KU-status oppgis per komponent, ikke bare som ja/nei for hele prosjektet.
3. Kartdata kommer med råsvar og spørringslogg, eller en konkret dokumentert tilgangsbegrensning.
4. Planområde, karttreff, konsekvensutreders vurdering og faktisk naturtap er tydelig atskilt.
5. Ukjent kartleggingsdekning vises, også når søket gir null treff.
6. Faktiske arealendringer krever validert inngrepsgeometri og datert før-/ettergrunnlag; ellers står verdien ukjent.
7. Minst én annen agent/koordinator kontrollerer sentrale kildehenvisninger og avgrensninger før kortene merkes kontrollert. Omfanget dokumenteres; pilotkontroll er ikke en naturfaglig feltgodkjenning.
8. Pilotrapporten identifiserer konkrete neste dokumenter/data, ansvar og tekniske hindringer. En full nasjonal analyse skal ikke startes ved bare å kopiere uavklarte forutsetninger.


## Tillegg 2026-10-05: vannbalanse og følgeinngrep

`research/natur/vann-og-folgeinngrep.json` konkretiserer målebehovet for tre piloter: årlig uttak, forbruk og retur, maksimalt uttak, utslippstemperatur og temperaturøkning, sesongprofil og WUE. WUE må ha uttrykkelig IT-energi som nevner og samme måleperiode. Ukjent er null; manglende utslipp av kjølevann er ikke bevis for fravær av vannpåvirkning fra overvann. Intern kjølekrets og endelig varmeavgivelse dokumenteres separat. Førtilstand krever observasjonsdato og kilde, ikke bare rapportdato. Følgeinngrep trenger egen geometri og dokumentert prosjektkobling.

Gromstuls nye kildekontroll gjelder tillatelse for datasenter 1, datert 25.08.2025 og lest 05.10.2026. Historiske artsregistreringer i tillatelsen supplerer, men erstatter ikke, selvstendig artsuttrekk. Se rapportoppdateringen for kilde og avgrensning.
