# Rapportoppdatering 5. oktober 2026

Teknologirådets **Datasentre i Norge – vurderinger av samfunnsnytte**, ISBN 978-82-8400-045-9, er lest som lokal fulltekst i `report/Datasentre-i-Norge.pdf`. [Offisiell publiseringsside](https://teknologiradet.no/publication/datasentre-i-norge-vurderinger-av-samfunnsnytte/) er datert 05.10.2026 og kontrollert samme dag. PDF-en oppgir oktober 2026. Dette er analyserapporten; en rapport med anbefalinger varsles separat. Trykte sidetall ligger to foran PDF-sidene fra trykt side 4.

## Endringer i påstandsregisteret

- Publikasjonsstatus er bekreftet. Historisk kontroll 01.10 ligger i `history/2026-10-01/`.
- Eierskap: rapporten oppgir omtrent 90 %, mens eldre omtale oppgir 90,6 %. Figur 13 er datert 21.05.2026. Metoden fordeler MW etter aksjeandeler/eierland (s. 65, 68–69). Ingen selvstendig reproduksjon; eierland er ikke automatisk lik jurisdiksjon eller faktisk kontroll.
- Nettreservasjon: rapporten oppgir 4220 MW og over 50 % i september 2026, med total 8179 MW (s. 15, 18). Egen aritmetikk gir 51,60 %. Felles populasjon og rader må avstemmes; eldre 47 % beholdes separat.
- 87,8 TWh er et fullrealiseringsscenario med 70 % kapasitetsfaktor, ikke målt forbruk, sannsynlig prognose eller konfidensintervall (s. 13, 15–17).
- 587/913 kroner per MWh i 2023 støttes med eksisterende avgrensning til historiske populasjoner. 677 direkte sysselsatte og bransjens 4400 årsverk har ulike avgrensninger; ikke behandle dem som konkurrerende anslag på samme størrelse (s. 38–40).
- Rapportens naturkapittel gir ikke et nasjonalt, prosjektbasert naturtapsregnskap (s. 51–55). Tidligere kunnskapshull består.

## Interne avvik som må avklares

| Kontroll | Resultat | Referanse |
|---|---|---|
| Historisk basis | Kartlagt før 2019: 126,05 MW. NVE-basis: 135 MW. Med 799,4 + 30 gir dette 955,45 eller 964,4 MW. | s. 13–14 og 69; fotnote 31 forklarer forskjellen |
| Sum for 2026 | 955 + 930 = 1885, mens brødteksten oppgir 1894. Sistnevnte svarer omtrent til alternativ historisk basis. | s. 14 |
| Konsentrasjon | Teksten omtaler fire anlegg; figur 14 gjelder operatører. Bitdeer/Straitdeer har 26 % i teksten og 25 % i figur. | s. 65 |

Disse er dokumenterte avvik, ikke grunnlag for å forkaste rapporten samlet eller velge en ny «riktig» nasjonal totalsum uten raddata. Rapportens 192 rader er ikke automatisk 192 anlegg. Datasenteroversikten er omtalt, men ikke innhentet. Ingen forespørsel er sendt.

## Prosjektberiking

Prosjektdata v0.3.0 bevarer alle tidligere påstander. Nye opplysninger har egne kilder, perioder, sidetall og kontrollstatus:

- Gromstul: rapportens 126 MW, hyperscale-klassifisering og WS Computing → Raiden → Alphabet. Behold historiske 240 MW. Transformatorbasert kobling av WSC/WS Computing er ikke selvstendig verifisert prosjektidentitet.
- Bulk N01: rapportens 625 MW reservert frem mot 2035; ikke markedsført 1000 MW eller eldre 400 MW-mål.
- Rjukan: omtalt varmeavtaker Hima Seafood; ingen målt varmeleveranse innført.
- Heggvin: rapporten støtter 6,1 mrd for tre bygg fremfor eldre 9 mrd for fem. Eksisterende Menon-presisering om modell og forventede utgifter beholdes.

Driftsmodell, arbeidslast, eierskapsnivåer og energitjenester har eksplisitte felt for manglende dokumentasjon. Rapportpåstander finnes i `claims`, og er ikke løftet til uavhengig verifiserte dimensjonsverdier. Narvik/Tydal blir stående som egne kandidater. Rapportens omtale av Anthropic i Tydal og Akers eierandel i Nscale er spor for primærkildekontroll, ikke automatisk oppdatering av juridisk eierkjede eller ukjent sluttkunde.

## Natur og vann

En ny kontroll av Statsforvalterens tillatelse 25.08.2025 for Gromstul datasenter 1 supplerer pilotgrunnlaget. Den omtaler ildsandbie (2022) og hagtornsommerfugl (2009, publisert 2021) i planområdet, med kategorier slik kilden angir. Det er kildeopplysninger, ikke et eget artsuttrekk eller påvist skade. Overvann beskrives ledet via oljeutskillere og fordrøyning til Bjordamsbekken, mens kjølevanns-/prosessavløpsutslipp ikke er beskrevet for dette tiltaket. Tillatelsen avgrenser vurderingen til datasenter 1, og tar ikke stilling til KU-plikt. Myndigheten vurderer påvirkningen akseptabel med vilkår; det er ikke målt ettertilstand eller en samlet vurdering av hele utbyggingen. [Primærkilde, s. 1–4](https://webfileservice.nve.no/API/PublishedFiles/Download/dddf6fda-38d1-491f-abc5-9464c85e35eb/202422995/3446684), lest 05.10.2026.

Se `natur/vann-og-folgeinngrep.json` for målefelter og evidensbehov for alle tre piloter. Uttak, forbruk og retur holdes atskilt; intern kjølekrets er ikke det samme som varmeavgivelse til omgivelsene. Ukjente tall er null, ikke 0. Historiske vannstatuser oppdateres ikke uten nye kilder.

## Videre evidensbehov

Prioriter 192-raders Datasenteroversikt og datert Statnett-uttrekk, deretter primærkilder for nye prosjektpåstander. For natur: bekreftet CRS og inngrepsgeometri, historiske flybilder/artsdata, oppdatert KU per komponent og vann-/overvannsoppfølging. Rapporten alene løser ingen av disse.
