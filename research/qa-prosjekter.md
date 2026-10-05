# Avgrenset krysskontroll av prosjektdata

Kontrolldato: 2026-10-01. Uavhengig QA-agent kontrollerte opplysningene nedenfor i `prosjekter.json` versjon 0.1.0. Dette er ikke godkjenning av hele datasettet, naturvurderingene eller prosjektdekningen.

## 1. Bulk N01: koordinat

Ny forespørsel mot [Kartverkets adresse-API](https://ws.geonorge.no/adresser/v1/sok?sok=St%C3%B8levegen%2039&treffPerSide=10) ga ett treff: Stølevegen 39, Vennesla, 58.25757326329835 nord / 7.892050117139653 øst i EPSG:4258. Samsvarer med prosjektfilen og lagret råsvar. Registeroppdatering 15.06.2020; `stedfestingverifisert=false`. Filens forbehold om adressepunkt, ikke anleggsgrense eller sentrum, er nødvendig. Kontrollen bekrefter registerpunktet; den bekrefter ikke bygningsfotavtrykk eller nøyaktigheten til koblingen mellom adresse og hele campusområdet. Ingen statistisk feilradius kan utledes.

## 2. Gromstul: arealbegrep

[Skien kommunes tidslinje](https://www.skien.kommune.no/by-og-naeringsutvikling/google-etablering-i-skien-kommune/tidslinje-hva-har-skjedd-fram-til-naa/) (publisert 19.02.2024, oppdatert 18.09.2025) støtter nær 2 000 mål kjøpt i 2019 og et reguleringsområde på nær 3 000 mål fra 2018, med rundt 2 000 mål næringsformål. Omregning til henholdsvis omtrent 2 og 3 millioner m² er korrekt. Ingen av størrelsene dokumenterer faktisk nedbygd areal. Kildens avrunding må beholdes i visningen. Polygon og dagens inngrepsstatus er fortsatt ukjent.

## 3. Hamar: effekt og verdiskaping

[Operatørens Hamar-side](https://greenmountain.no/data-center/osl-hamar/) (udatert, lest 01.10.2026) skiller 90 MW kontrahert IT-kapasitet fra mulig 150 MW med fem bygg. Dette støtter filens separate typer. Ingen av dem er målt årsenergi.

Fulltekst av [Menon, Economic Impact Analysis of OSL-Hamar Construction, nr. 96/2025](https://greenmountain.no/wp-content/uploads/Report-Economic-Impact-Analysis-of-OSL-Hamar-Construction-english.pdf), datert august 2025, avklarer avgrensningen. PDF-side 5: 6,1 milliarder gjelder tre bygg i 2022–2026, uten TikToks investeringer. Av dette er 5,7 milliarder beregnet fra gjennomførte investeringer og 0,4 milliarder forventet etter rapporttidspunktet. Side 6 og 9: tidligere 9 milliarder gjaldt fem bygg og inkluderte TikTok. Side 11–12 forklarer at dette er en brutto ringvirkningsmodell, ikke netto samfunnsøkonomisk nytte. **6,1 og 9 milliarder er derfor ikke sammenlignbare enkeltmålinger eller et konfidensintervall.** SSBs Hamar-rad må holdes atskilt fra originalrapportens avgrensninger inntil eventuell tabellfeil eller annen kildeversjon er avklart. Dataagenten har fått den daterte originalkilden og presiseringene.

## Ekstra funn: foreldet eieropplysning for Lefdal

Gjeldende fil ved første lesing brukte en udatert operatørside med Columbia Threadneedle som eier. [3is daterte melding 03.09.2026](https://www.3i-infrastructure.com/newsroom/press-releases/2026/3i-infrastructure-plc-completes-investment-in-the-lefdal-mine-datacenter-campus/) dokumenterer gjennomførte transaksjoner 28.08 og 02.09.2026: 3i forvalter 90 % av egenkapitalen; litt over 45 % tilhører 3i Infrastructure og omtrent 45 % medinvestorer, mens en minoritet beholder 10 %. Det betyr ikke at 3i Infrastructure alene eier 90 %. Dataagenten har overtatt rettingen av generator og JSON; gammel eierinfo skal merkes historisk/erstattet.

## Tillegg: teknisk kontroll av to planområder

Utført 01.10.2026 etter at dataagenten hentet fire råfiler fra kommunenes Arealplaner-tjeneste. Omfanget er metadataidentitet og geometrisk ringintegritet; ingen full planrevisjon eller feltkontroll.

| Plan | Metadataidentitet | Rå geometri | Resultat |
| --- | --- | --- | --- |
| Heggvin | Kommune 3403, plan 079500, «Detaljreguleringsplan for Heggvin næringspark», id 156, ikraft 27.04.2022 | Én ytre ring, 267 posisjoner inkludert lukking, 266 unike, ingen innerringer | Eksakt lukket, endelige numeriske koordinater, gyldig polygon ved Shapely-kontroll |
| Gromstul | Kommune 4003, plan 2017004, «Reguleringsplan for gbnr. 11/1 - datasenter Gromstul», id 726, ikraft 31.05.2018 | Én ytre ring, 98 posisjoner inkludert lukking, 97 unike, ingen innerringer | Eksakt lukket, endelige numeriske koordinater, gyldig polygon ved Shapely-kontroll |

Begge metadataobjekter angir endelig vedtatt detaljregulering og vertikalnivå 2, på grunnen/vannoverflaten. Heggvin har `sistBehandlet=2024-11-26`; ikraftdato alene er derfor ikke tilstrekkelig versjonsbeskrivelse. Metadata bekrefter ikke at geometrien er identisk med en bestemt datert PDF-revisjon.

Kildeendepunkter, hentet 01.10.2026:

- [Heggvin planområde](https://api.arealplaner.no/api/gi/kunder/hamar3403/planomraader/3403/079500)
- [Gromstul planområde](https://api.arealplaner.no/api/gi/kunder/skien4003/planomraader/4003/2017004)

Koordinatene er i lengde-/breddegradslignende verdier med x før y. API-svarene deklarerer ikke EPSG. Dataagenten opplyser at Arealplaners kartkode mapper x/y direkte til GeoJSON; denne frontend-observasjonen er ikke selvstendig revidert i QA. **CRS er avledet og ubekreftet, ikke autoritativt dokumentert EPSG:4326.** Ingen projisering eller arealberegning er godkjent. Shapely-testen kontrollerer ringens matematiske integritet i råkoordinatrommet, ikke geodetisk riktighet eller juridisk plangrense.

Geometriene skal merkes **planområde**. Heggvin er næringsparkens planavgrensning; Gromstul er reguleringsområdet. De er ikke dokumentert datasenterfotavtrykk, tomtegrense eller faktisk arealbeslag. De bør ikke danne grunnlag for naturtap eller summerte arealtall.

Etterkontroll samme dag av `research/planomriss.geojson`: begge Polygon-geometrier samsvarer eksakt, verdi for verdi, med råresponsenes x/y-ringer. Ingen posisjoner er tapt eller endret. Begge er fortsatt gyldige etter konvertering. Feature-egenskapene har korrekt planId/navn og eksplisitt advarsel om planområde, ikke fotavtrykk. Denne kontrollen bekrefter overføringen, ikke det udeklarerte kildedatumet. CRS-forbeholdet bør også følge en eventuell frittstående GeoJSON-nedlasting.

## Restanse

Hovedagentens etterkontroll av sluttfilen 01.10.2026 bekrefter at CRS-forbehold, QA-status, metode og kilde-URL nå følger hver GeoJSON-feature. Det tidligere påpekte nedlastingsforbeholdet er dermed ivaretatt; selve kilde-CRS er fortsatt ubekreftet.

To kildebelagte planområders rå ringintegritet og planidentitet er kontrollert med forbeholdene ovenfor. Fysisk nedbygd areal, målte prosjektvise energiår og fullstendige reelle eierkjeder er ikke godkjent gjennom denne kontrollen. Videre arbeid må bekrefte CRS, geometriens revisjonsdato og naturkartleggingsdekning før arealberegninger og naturtapsoverlegg tas i bruk.
