# Etterprøving av offentlig omtalte datasenterpåstander

Kontrollert 2026-10-01. Dette er en første kildekontroll, ikke en full revisjon av en publisert datasenterrapport. Maskinlesbare påstander, kildedatoer og vurderinger finnes i `pastander.json`.

## Publikasjonsstatus

Teknologirådets [prosjektside](https://teknologiradet.no/project/datasentre-i-norge-ringvirkninger-og-ressursbruk/) er datert 22.10.2025 og varsler rapport sommeren 2026. Den åpne [publikasjonslisten](https://teknologiradet.no/list-publikasjoner/) og prosjektsiden ga ingen tilgjengelig sluttrapport i denne kontrollen. Søkefravær beviser ikke at rapporten ikke finnes eller er offentliggjort et annet sted. Status skal derfor være **«publisert fulltekst ikke funnet ved kontroll 01.10.2026»**, med rapportdato og versjon ukjent.

[Faktaportalen](https://faktaportalen.no/blogg/2026-09-29-teknologiradets-datasenterrapport-er-ikke-ute-dette-sier-tallene-vi-har), publisert 29.09 og rettet 30.09.2026, omtaler NRKs sak som basert på et sammendrag. NRK-lenken feilet ved åpning. Vi har derfor ikke kontrollert NRKs fulltekst, sammendraget eller rapportgrunnlaget. Tallene 90,6 % utenlandsk eid kapasitet, 47 % reservert nett og 964 MW tilknyttet behandles som **sekundært gjengitte påstander**, ikke verifiserte funn. Antall sentre og andel kapasitet er forskjellige nevnere.

## Hva primærkildene avklarer

[SSB, 28.04.2026, endret 18.06.2026](https://www.ssb.no/teknologi-og-innovasjon/informasjons-og-kommunikasjonsteknologi-ikt/artikler/datasentrene-vokser-raskt-men-hvilke-verdier-skaper-de-for-norge) viser i tabell 1 henholdsvis 587 og 913 kroner/MWh for datasentre og kraftintensiv industri i 2023. Analysen avgrenser tradisjonelle kommersielle sentre; den estimerer ikke fremtidens KI-industri. I 2020 var rekkefølgen motsatt. Dette støtter en tidsavgrenset sammenligning, ikke en universell påstand om at datasentre alltid skaper mindre verdi. «Lokal» verdiskaping kan ikke utledes direkte fra en nasjonal tabell.

[Samfunnsøkonomisk Analyse R.33/2024](https://samfunnsokonomisk-analyse.no/publikasjoner/verdiskaping-i-norsk-datasenterindustri), bestilt av bransjeforeningen NDI, oppgir 4 400 årsverk og 4,7 milliarder kroner i 2024 med bredere aktivitet, særlig etablering og leverandører. Dette er relevant motvekt til en påstand om ingen nytte, men ikke direkte motbevis mot SSBs mål per MWh. Framskrivingene forutsetter realisering og må skilles fra observerte resultater.

[Elhub, 21.09.2026](https://elhub.no/artikler/ny-rapport-gir-innsikt-i-datasentrenes-faktiske-stromforbruk) oppgir 3,14 TWh og 2,26 % av norsk strømforbruk i 2025. [NVE, oppdatert 26.08.2026](https://www.nve.no/energi/energisystem/energibruk/energibruk-i-datasenter/) oppgir 3,3 TWh for samme år. Forskjellen er uavklart i denne kontrollen; vis begge kildeverdier, ikke et statistisk konfidensintervall. Elhubs [datadokumentasjon](https://elhub.no/data-og-innsikt/stromforbruk-i-datasentre) advarer om både manglende og feilinkluderte virksomheter ved næringskodebasert utvalg.

[NVE rapport 17/2026](https://publikasjoner.nve.no/rapport/2026/rapport2026_17.pdf), PDF-side 21 og 23, har et anslag på rundt 8 TWh i 2030. Dette er framskrevet energibruk. Teknologirådets eldre 9 TWh-omtale er tilskrevet THEMA. Ulike modeller og årganger er ikke observerte yttergrenser og skal ikke presenteres som et sannsynlighetsintervall.

[Statnett](https://www.statnett.no/nettkapasitet-til-produksjon-og-forbruk/foresporsler-og-reservasjon-i-nettet/) opplyser at statistikken bygger på manuell registrering fra 2018 og kan ha mangler. Saker på særlige vilkår kan finnes både under reservasjon og kø. Dynamiske Power BI-tall er ikke hentet ut i denne kontrollen. Tallene må ha felles uttrekksdato, status og nevner før summering. MW er effekt; MWh/TWh er energi. Reservasjon er verken målt forbruk eller installerte servere.

Eierskap må etterprøves anlegg for anlegg, gjennom datert selskapskjede og definisjon av kontroll. [Green Mountains melding 19.07.2021](https://greenmountain.no/green-mountain-data-centers-acquired-by-azrieli-group-ltd/) dokumenterer avtale om salg til Azrieli, ikke alene sluttføring eller nåsituasjon. [Bulks aksjonæroversikt](https://bulkinfrastructure.com/about-us/investor-relations) er merket desember 2025. Eksempler på eierskap kan ikke validere en landsdekkende kapasitetsvektet prosent.

## Åpne kontrollpunkter

- Hent Teknologirådets sluttrapport, versjon, fullstendig sammendrag og underliggende tabeller. Lås attribusjon til omtale frem til dette er gjort.
- Reproduser eierandelen med entydig anleggsunivers, kapasitetsbegrep, referansetid, eierkjeder og behandling av joint ventures. Ikke sett konfidensprosent på skjønnsmessig evidens.
- Hent Statnetts daterte eksport og forklar tilknyttet/reservert/kø, dobbelttelling og dekning.
- Avklar avgrensningen bak Elhub/NVE-avviket før nasjonale totalsummer velges.
- Ingen tallfestet nasjonal naturpåstand fra Teknologirådet er verifisert i materialet. Naturpåvirkning krever prosjektvis plan/KU, kartlag, arealhistorikk og kontroll av faktisk inngrep. Fravær av data betyr ukjent, ikke null.

## Publiseringskriterier for web-løsningen

1. Hver opplysning må ha kilde, dato (eller «ukjent»), referansetid, kildeavsnitt/side, enhet, definisjon og kontrollstatus. Bevar påstand og egen vurdering separat.
2. Polygon må ha geografisk originalkilde, CRS, dokumentert transformasjon, dato og geometrirolle: planområde, tomt, byggeareal eller faktisk nedbygd areal. Et punkt dokumenterer aldri arealavgrensning. Kommunesentroider og håndtegnede bokser må ikke brukes som anleggsgrenser.
3. Arealbeslag må ikke beregnes av planareal uten begrunnelse. Naturregistreringers dekningsgrad og årgang må synliggjøres; ingen registrering er ikke det samme som ingen naturverdi.
4. Skill drift, bygging, vedtatt plan og forslag; skill IT-effekt, nettkapasitet og målt årsforbruk. Summer bare kompatible tall.
5. Bruk statistiske konfidensintervall bare med dokumentert modell, populasjon, metode og dekningsnivå. Ellers vis kildebestemt spenn eller kvalitativt evidensnivå med begrunnelse. Konflikter vises som konflikt.
6. Kvalitetssikrer skal være en annen agent/person enn innsamleren. Uverifiserte opplysninger kan vises som åpne kontrollpunkter, men må ikke brukes i rangering eller totaler.
