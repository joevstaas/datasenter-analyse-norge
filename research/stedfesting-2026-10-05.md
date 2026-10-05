# Undheim og Gromstul: stedfesting kontrollert 2026-10-05

Begge prosjektene har nå dokumenterte adressepunkter fra Kartverket. Det første søket stoppet for tidlig ved manglende eksplisitt adresse på prosjektsidene. Et nytt søk via primærkilder, underenhet og matrikkelnummer fant adressene. Punktene er egnet til en oversiktsdemo med forbehold; de dokumenterer ikke arealbeslag.

| Prosjekt | Adresse | Breddegrad | Lengdegrad | Matrikkel |
|---|---|---:|---:|---|
| Undheim | Undheimsvegen 759 | 58.65968677839994 | 5.794339715544289 | 1121 / 46 / 317 |
| Gromstul | Gromstulvegen 82 | 59.26995366923121 | 9.518779375062875 | 4003 / 11 / 28 |

Koordinater over er originalverdier i EPSG:4258. ODP-tabellen bruker EPSG:4326, transformert med pyproj. Antall desimaler fra registeret er ikke dokumentert stedfestingsnøyaktighet. Konfidens er middels: begge registerpunktene har `stedfestingverifisert=false`. Numerisk feilmargin og statistisk konfidensintervall er ukjent/ikke begrunnet. Ikke bruk punktene til å beregne naturtap eller som anleggets sentrum.

Undheim: Green Mountains stillingsannonse på NAV Arbeidsplassen oppgir adressen og knytter den eksplisitt til det nye datasenteret. Publisert 2026-09-28 ifølge annonsedata. Kartverket returnerer ett treff på gnr. 46/bnr. 317 i Time. NVE-søknaden revisjon J02 datert 2026-07-10 omtaler samme matrikkelnummer blant berørte eiendommer. Selskapets kontaktadresse på Rennesøy er ikke brukt som kartpunkt.

Gromstul: Statsforvalterens tillatelse datert 2025-08-25 identifiserer datasenter 1 på gnr. 11/bnr. 28. Brønnøysundregistrenes underenhet 925646334 har beliggenhetsadresse Gromstulvegen 82. Kartverket gir ett adressepunkt på denne eiendommen. Tillatelsen gjelder datasenter 1, ikke alle framtidige bygg.

Alle seks kilder med URL, lesedato, råfil og SHA-256 er registrert i `prosjekter.json`. Råfiler og innhentingsmanifest ligger i `raw/location-review-2026-10-05/`. `table-patch.json` dokumenterer de to før-/etterradene og seks nye kilder. Andre prosjektopplysninger og planpolygoner er uendret. Rettingen endrer ikke feltet for verifisert driftsstatus.

## Nye spor for senere naturgjennomgang

NVE-sak 202608496 inneholder vedlegg om naturmangfold, vannmiljø og øvrige følgeinngrep ved Undheim. Kartpunktkontrollen er ikke en kvalitetssikring av disse konsekvensvurderingene.

Søket fant også Ecofact rapport 1191, «Undersøkelser etter utslipp av finstoff i Stormyråna, VUU1 AS». Søkeuttrekket knytter rapporten til eiendom 46/317 og utslipp våren 2025. Fulltekstinnhenting via webverktøyet feilet. Rapporten er derfor kun et oppfølgingsspor, ikke innarbeidet som verifisert naturkonklusjon: https://www.ecofact.no/rapporter/1191-VUU1-Unders%C3%B8kelser%20etter%20utslipp%20i%20Stormyr%C3%A5na.pdf
