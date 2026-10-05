# Foreløpig Naturbase-screening av to planområders søkerektangler

Hentet **2026-10-01** fra Miljødirektoratets offentlige ArcGIS REST-tjenester. Resultatene er **bbox-kandidater**, ikke bekreftede overlapp med planpolygon, datasentertomt eller faktisk nedbygd areal. Ingen overlappsareal eller naturtap er beregnet.

## Resultat og tolkning

| Kommunalt planområde | NiN-lokaliteter, lag 0 | DN-håndbok 13, lag 0 | Naturvernområder, lag 0 | NiN-dekningspolygoner, lag 1 |
| --- | ---: | ---: | ---: | ---: |
| Heggvin, Hamar 3403 / 079500 | 0 | 0 | 0 | 2 |
| Gromstul, Skien 4003 / 2017004 | 38 | 7 | 0 | 5 |

Tallene er antall komplette feature records returnert ved `esriSpatialRelIntersects` mot **søkerektangelet**, ikke mot planområdet. Sant overlappsantall er `null` (ukjent), ikke null treff. Et naturpolygon kan treffe rektangelets hjørner uten å berøre planen. NiN- og DN13-tall skal ikke summeres til unike naturforekomster; metodene og polygonene kan overlappe. Null treff i valgte datasett betyr ikke fravær av naturverdi, artsforekomster, økologiske forbindelser eller naturtap.

**Heggvin har ikke dokumentert full kartleggingsdekning.** De to dekningskandidatene heter «Heggvin næringsområde øst 1» og «øst 2», med **Løten kommune** som oppdragsgiver, Norconsult AS som oppdragstaker og år 2021. Treffene gir ikke grunnlag for å overføre Løten-rapportens konklusjoner til Hamar plan 079500. Deres kode «Kartlagt uten funn» gjelder deres egne kartleggingspolygoner og utvalg av naturtyper, ikke automatisk Hamar-planen.

**Gromstul har faktiske registrerte naturkandidater i søkerektangelet.** Alle 38 returnerte NiN-lokaliteter har `Kartleggingsår=2025`; dekningslagets fem kandidater er fra 2021, 2022, 2025 og 2026. Hentetidspunkt er ikke kartleggingsår. Treffer ikke målte konsekvenser eller situasjonen før en bestemt utbyggingsfase.

### Tillegg: betinget topologisk planberøring

På koordinatorens forespørsel er kandidatpolygonene også testet mot de uendrede planringene i samme uprojiserte lon/lat-koordinatrom. Dette er `conditional_polygon_intersection`, **avhengig av at det avledede plan-CRS er kompatibelt med EPSG:4326**. Det er ikke en CRS-bekreftet `exact_intersection`. `intersects` inkluderer grenseberøring; intet areal er beregnet.

| Plan | Lag | Bbox-kandidater | Betinget planberøring | Betinget utenfor plan |
| --- | --- | ---: | ---: | ---: |
| Heggvin | NiN-naturtyper | 0 | 0 | 0 |
| Heggvin | DN13 | 0 | 0 | 0 |
| Heggvin | Vern | 0 | 0 | 0 |
| Heggvin | NiN-dekning | 2 | 2 | 0 |
| Gromstul | NiN-naturtyper | 38 | 0 | 38 |
| Gromstul | DN13 | 7 | 0 | 7 |
| Gromstul | Vern | 0 | 0 | 0 |
| Gromstul | NiN-dekning | 5 | 3 | 2 |

Dette forklarer hvorfor bbox-tallene ikke kan omtales som naturforekomster i Gromstul-planen. Ingen av de 45 NiN/DN13-kandidatene berører planringen under CRS-forutsetningen. Det sier fortsatt ikke at naturverdier manglet før inngrep eller ikke finnes nå. Heggvin-Løten-dekningspolygonene berører begge Hamar-planringen betinget; dette dokumenterer verken hvor stor del av planen de dekker eller rapportenes tematisk fullstendige relevans.

`run_conditional_intersections.py` kjøres **etter** uttrekksscriptet, på allerede lagrede råfiler. Python med Shapely 2.1.2 er brukt. ArcGIS-ringer er omdannet ved even/odd-topologi (symmetrisk differanse mellom ringer), som håndterer separate ytre ringer og hull. Alle plan- og kandidatringer og resulterende geometrier var gyldige; ingen reparasjon, snapping eller forenkling. Alle 52 returnerte natur-/dekningsrecords ble testet, ingen ugyldige ble hoppet over. JSON beholder bbox-tallene og gir separate testtall, OBJECTIDer, versjon og forbehold i `conditionalPolygonIntersection`. Feltet `trueOverlapCount` er fortsatt `null`.

## Autoritative tjenester, geometri og lisens

| Kilde | Lag brukt | Kildens CRS / geometri | Metode/år og dekning |
| --- | --- | --- | --- |
| [Naturtyper på land, NiN](https://kartkatalog.miljodirektoratet.no/MapService/Details/naturtyper_nin) | `naturtyper_nin/MapServer/0` | EPSG:25833 / polygon | Naturtypelokaliteter etter Miljødirektoratets instruks; individuelle instruks-URLer og kartleggingsår følger rådata og JSON. Ikke heldekkende kart over all natur. |
| [NiN kartleggingsdekning](https://kart.miljodirektoratet.no/arcgis/rest/services/naturtyper_nin/MapServer/1) | `naturtyper_nin/MapServer/1` | EPSG:25833 / polygon | Kartleggingsområde, år, program og dekningskode. Full planvis dekning fortsatt ukjent. |
| [Naturtyper etter DN-håndbok 13](https://kartkatalog.miljodirektoratet.no/MapService/Details/naturtyper_hb13) | `naturtyper_hb13/MapServer/0` | EPSG:25833 / polygon | Historiske naturtypevurderinger A/B/C; her Gromstul-kandidater med datafangst 2004–2017. Fullstendighet ukjent. |
| [Vern](https://kartkatalog.miljodirektoratet.no/MapService/Details/vern) | `vern/MapServer/0` | EPSG:25833 / polygon | Register over vedtatte naturvernområder. Kartkatalogen dokumenterer nasjonal registerdekning. Dette er ikke en heldekkende naturverdivurdering. Foreslåtte verneområder (lag 4) inngår ikke i denne testen. |

Miljødirektoratet er datakilde for alle lag. De tre offisielle kartkatalogsidene angir **Norsk lisens for offentlige data (NLOD)**. Lisensversjon er ikke oppgitt på disse sidene; ingen versjon er antatt. HTML-kopier er bevart som `raw/gis-catalog-*.html`. Service- og lagmetadata er bevart som `raw/gis-service-*.json` og `raw/gis-layer-*.json`, inkludert domenekoder, CRS, geometri og recordgrenser.

Tjenesteopprettelse er ikke naturkartleggingsår: kartkatalogen daterer NiN-tjenesten 20.03.2019, HB13 24.01.2019 og verntjenestens plattform 11.06.2018. Ingen entydig dato for komplett datasett-snapshot fremgår av lagmetadata (`editingInfo` mangler). Bruk hente- og objektdato separat. Objekters opprinnelige `Kartleggingsinstruks` beholdes; ingen rekoding til nyere rødliste, NiN-versjon eller verdi gjøres her.

## Konkrete records og datoer

Utvalgte NiN-kandidater i **Gromstul-rektangelet**:

| Stabil ID | Navn / naturtype | Kartleggingsdato | Objektnøkkel |
| --- | --- | --- | --- |
| [NINFP2510187501](https://nin-faktaark.miljodirektoratet.no/naturtyper?id=NINFP2510187501) | Dyrkollåsen øst / Frisk kalkgranskog | 2025-05-28 | OBJECTID 1480 |
| [NINFP2510195382](https://nin-faktaark.miljodirektoratet.no/naturtyper?id=NINFP2510195382) | Kåsa_4 / Kalkedellauvskog | 2025-07-08 | OBJECTID 9198 |

Begge oppgir [2025-instruksen](https://nedlasting.miljodirektoratet.no/NiN_Instrukser/Ntyp2025_kartleggingsinstruks.pdf) i selve recorden. Dette er bevarte metadata, ikke en ny vurdering etter instruksen. Miljødirektoratets numeriske kvalitetskoder er bevart uendret; de er ikke vår vurdering av utbyggingens påvirkning.

Alle sju DN13-kandidater i Gromstul-rektangelet:

| Stabil ID | Navn | Kildeverdi | Datafangstdato |
| --- | --- | --- | --- |
| [BN00077727](https://faktaark.naturbase.no?id=BN00077727) | Bøelva-Hoppestadelva | B | 2004-08-31 |
| [BN00091311](https://faktaark.naturbase.no?id=BN00091311) | Kiseåsen | A | 2012-11-14 |
| [BN00106737](https://faktaark.naturbase.no?id=BN00106737) | Kåsa V | B | 2013-10-17 |
| [BN00106744](https://faktaark.naturbase.no?id=BN00106744) | Bjørnhol SV | B | 2014-09-25 |
| [BN00106750](https://faktaark.naturbase.no?id=BN00106750) | Bjørnhol V | B | 2014-09-25 |
| [BN00125571](https://faktaark.naturbase.no?id=BN00125571) | Dyrkollåsen sørvest | B | 2016-10-23 |
| [BN00131183](https://faktaark.naturbase.no?id=BN00131183) | Haukelikollen | B | 2017-05-23 |

NiN-dekningskandidater; domenebetydning er direkte fra lagets feltskjema:

| Søkerektangel | OBJECTID | Prosjektområdenavn | År | Dekningskode |
| --- | ---: | --- | ---: | --- |
| Heggvin | 4023 | Heggvin næringsområde øst 1 | 2021 | 4: Kartlagt uten funn |
| Heggvin | 4387 | Heggvin næringsområde øst 2 | 2021 | 4: Kartlagt uten funn |
| Gromstul | 867 | Rød-Nordre Bø | 2022 | 1: Grundig kartlagt med funn |
| Gromstul | 3633 | Skuggedalskollen | 2021 | 4: Kartlagt uten funn |
| Gromstul | 6218 | Bjordamsbekken | 2025 | 4: Kartlagt uten funn |
| Gromstul | 6380 | Kalkområder - Skien | 2025 | 1: Grundig kartlagt med funn |
| Gromstul | 6734 | VLB3 | 2026 | 4: Kartlagt uten funn |

Fullstendige stabile NiN/DN13-IDer, prosjekt-GUIDer, tidsstempel i Unix-millisekunder og normaliserte ISO-datoer er i `gis-screening.json`. Samtlige geometrier og originale attributter ligger i råsvarene. Kildenes `SHAPE.STArea()` er **hele natur-/dekningspolygonets areal**, ikke overlapp eller naturtap; feltene er derfor utelatt fra den avledede JSON, men bevart i råsvarene.

## CRS, søk og reproduserbarhet

Planpolygonene er lest uendret fra `research/planomriss.geojson` og kryssjekket mot prosjektidentiteten i `research/prosjekter.json` og forbeholdene i `research/qa-prosjekter.md`. Begge er Polygon og har rollen `regulatory_plan_extent`. For Heggvin brukes Hamar 079500, ikke et annet næringsområde i Løten.

Kildens API-svar deklarerer fortsatt ikke EPSG. Søk i tilgjengelig offentlig Arealplaner-dokumentasjon ga ingen autoritativ CRS-bekreftelse for disse endepunktene. Koordinatenes geografiske utseende er ikke en slik bekreftelse. **Antatt EPSG:4326 gjelder bare innsending av foreløpige søkerektangler.** Naturbasens egne service-metadata deklarerer EPSG:25833; utgående geometri ble uttrykkelig bestilt med `outSR=4326`. Naturbasens CRS-bekreftelse bekrefter ikke planenes datum.

Søkerektangler i `[xmin, ymin, xmax, ymax]`, dannet av planringenes min/maks uten buffer:

- Heggvin: `[11.25923287152275, 60.83131956854819, 11.275530418714263, 60.85123743309795]`.
- Gromstul: `[9.500617623875113, 59.26547333703958, 9.537731197091905, 59.28897634652845]`.

`run_screening.py` bruker Python standardbibliotek. Kjør fra repo med `python3 research/natur/run_screening.py`; en ny kjøring lager et nytt live-snapshot og erstatter JSON/råsvar. Kjør deretter `python3 research/natur/run_conditional_intersections.py` for betinget topologi. Markdownrapportens tall må oppdateres manuelt ved et nytt snapshot. Uttrekksscriptet lagrer eksakte URLer for ID-, count- og feature-spørringer i JSON. Det henter først alle IDs for rektangelet, uavhengig count-svar, deretter feature-batcher på maksimalt 100 IDs. Det sjekker antall og faktisk ID-sett. Dermed må `serverCount == idCount == countReturned`, IDene være like og `exceededTransferLimit=false`. Alle åtte tester bestod. Laggrensene er 5000 records for NiN/DN13 og 2000 for vern; største respons her var 38. Ingen respons ble trunkert. Ingen CRS-bekreftet eksakt planinterseksjon er kjørt.

Råfilnavn starter med `gis-{projectId}-{service}-{layerId}-` og slutter med `ids.json`, `count.json` eller `features-0.json`. Ved null IDs er et feature-kall unødvendig; ID/count-råsvar dokumenterer nullet. GeoJSON-inputens SHA-256 er registrert for sporbarhet. NIBIO AR5, arter, foreslått vern og natur uten registrerte naturtypepolygoner er ikke testet.

## QA-status og nødvendig neste steg

Teknisk hentetest godkjent for **bbox-screening med eksplisitt CRS-antakelse**: autoritative endpoints, riktige planidentiteter, fullstendige resultater, kildeår og rekord-IDer bevart. Ikke godkjent for naturtap, fraværskonklusjoner, verdsetting eller presise arealtall.

Før eksakt overlapp må plan-CRS og revisjon bekreftes fra registereier, feltkartleggingsdekning vurderes mot hele korrekt planpolygon, og tidslig samsvar mellom naturregistrering og inngrepsfase avklares. Et planoverlapp vil fortsatt være et planoverlapp; faktisk naturtap krever separat dokumentert inngrepsgeometri og før-/ettergrunnlag.
