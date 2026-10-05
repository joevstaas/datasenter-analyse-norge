> Oppdatert 05.10.2026: Naturkortene har nå 17 kilder og supplerende myndighetsopplysninger for Gromstul datasenter 1. Se [rapportoppdateringen](../rapportoppdatering-2026-10-05.md) og [vann-/følgeinngrepsdata](vann-og-folgeinngrep.json). Den daterte pilotbeskrivelsen nedenfor er historisk.

# Naturpiloter – 1. oktober 2026

Naturpåvirkning er nå et eget, obligatorisk spor i kartleggingen. Tre skrivebordspiloter har prøvd metoden: Gromstul, Heggvin og Narvik. Dette er et etterprøvbart forskningsgrunnlag for webkartet, ikke en ferdig konsekvensutredning eller måling av naturtap.

## Resultater

| Pilot | Dokumentasjon og funn | Viktigste avgrensning |
|---|---|---|
| Gromstul | Miljøprogram fra 2018 beskriver tidligere myr/torv og drenering. Original natur-KU er identifisert, men fulltekst ikke lest. | Dagens kartdata kan ikke rekonstruere natur før inngrep. Faktisk tap av myr/skog er ukjent. |
| Heggvin | Løten-utredning og bredere LE01-strategi er lest. LE01 vurderer netto biodiversitetstap for det samlede Heggvin/Sirkula-området. | Dette er ikke målt naturtap for datasenteret alene. Løten, Hamar og samlet industriområde må holdes geografisk atskilt. |
| Narvik | Historiske natur- og vannmiljøutredninger er funnet. Ny kjølevannsplan har egne utredningskrav; temperaturforskjell var uavklart i planinitiativet. | Eldre industri-KU gjelder en annen prosjektutforming. Varslingsområdet på ca. 6200 dekar er ikke arealbeslag. |

Hver opplysning i [naturkortene](naturkort.json) har kilde-ID, dokument-/innhentingsdato, sidehenvisning, tidsmessig avgrensning og begrunnet usikkerhet. Konfidensnivå beskriver sikkerheten i det avgrensede utsagnet, ikke en sannsynlighet for naturpåvirkning. Ingen statistiske konfidensintervaller er brukt uten grunnlag.

## Karttesten

Åtte avgrensede uttrekk fra Miljødirektoratet dekker NiN-naturtyper, eldre DN13-kartlegging, verneområder og NiN-kartleggingsområder for to planområder. Råsvar og skript er lagret. Uttrekkene er komplette for de konkrete spørringene; det betyr ikke at naturen er fullstendig kartlagt.

Gromstuls søkerektangel ga 38 NiN- og 7 DN13-kandidater. Ingen av disse 45 berører planringen i den betingede polygontesten. Kartleggingsområder berører planen, men deres dekningsgrad er ikke beregnet. Heggvin-testen viser berøring med to kartleggingsområder registrert i Løten, uten at dette dokumenterer full dekning av Hamar-planen.

**Planenes kilde-CRS er fortsatt ubekreftet. Ingen overlappsarealer eller faktiske naturtap er derfor godkjent.** Narvik er ikke romlig testet. AR5, selvstendige Artskart-uttrekk og datert før-/etteranalyse gjenstår. Null treff i utvalgte kartlag betyr ikke null naturverdier eller null naturtap.

Se [GIS-metode og resultater](gis-screening.md), [utredningskontroll](utredninger.md) og [Narvik-kontroll](narvik.md) for kildegrunnlaget.

## Datamodell og ansvar

[Naturmetoden](../../docs/naturmetode.md) krever fire feltgrupper i hvert naturkort: førtilstand, endring, konsekvens og kunnskapshull. Utredningsstatus registreres per prosjektkomponent. Planområde, faktisk inngrep og påvirkningsområde holdes atskilt. Indirekte og samlet påvirkning omfatter blant annet kraftinfrastruktur, vann, fragmentering og andre tiltak i området, med dokumentert tilordning.

Naturutredningsrollen har ansvar for rapporter, prosjektversjoner og feltgrunnlag. GIS-rollen har ansvar for geometri, kartdata og tidsserier. En annen rolle må kontrollere vesentlige konklusjoner. Utviklingsrollen skal bevare kildespor, ukjentverdier og kartleggingsdekning i brukergrensesnittet. Ingen samlet naturkarakter er etablert.

## Kontroll og videre arbeid

Tre naturkort med 16 anvendte kilder består skjemakontroll og referanseintegritet. Åtte GIS-spørringer og 30 råfiler er kontrollert. Fem negative kontroller avviser blant annet at ukjent naturtap settes til null, at manglende kilder aksepteres og at en udokumentert naturkarakter legges til. Dette er datakontroll, ikke økologisk validering. Se [QA-notatet](qa-natur.md).

Neste evidensbehov står per prosjekt i naturkortene: fullstendige og gjeldende KU-er, bekreftet CRS, faktisk inngrepsgeometri, historiske flybilder, arts- og arealressursdata, dokumentert avbøting og vannpåvirkning. Før disse er avklart, skal kartet vise kunnskapshullene eksplisitt.
