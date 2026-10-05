# Utvikling og Vercel-integrasjon

Undersøkt 2026-10-01. Dette er en teknisk kartlegging og et implementeringsforslag. Ingen produktkode, eksterne innstillinger eller deployer er endret.

## Bekreftede funn

| Funn | Dokumentasjon og begrensning |
|---|---|
| Vercel-tilgang finnes | Connectorens `vercel_list_teams` returnerte «Jo Øvstaas' projects»; `vercel_list_projects` og `vercel_list_deployments` virket 2026-10-01. Dette bekrefter lesetilgang, ikke gjennomført deploy eller mutasjonsrettigheter. |
| Eksisterende labs-gateway er `mpa_insights` | Lokal `../norwegian-marine-protection-explorer/README.md`, linje 38–46, dokumenterer `joevstaas/mpa-insights-generator` som gateway. Vercel-deployhistorikken bekrefter repoet og flere commits som legger til labs-ruter. |
| Lokal gateway er eldre enn produksjon | Lokal `../mpa-insights-generator` HEAD er `055c8de`, datert 2026-05-06. Nyeste returnerte READY-produksjonsdeploy har SHA `0a1977314019abfd51d9dbf6beae20f42dd78a3c` og meldingen «Route Norwegian marine protection explorer under labs». Se [Vercel-deploy](https://vercel.com/jo-ovstaas-projects/mpa_insights/HmLreA159peRBhSt45iuSjgVhPyw). Lokal gateway har også eksisterende usporede brukerfiler. |
| Gateway bruker avgrensede eksterne rewrites | Lokal `../mpa-insights-generator/vercel.json` ruter hver labs-app med egen grunnsti og understier. Den gamle lokale filen er evidens for mønsteret, ikke fasit for produksjonens komplette ruter. |
| Et ferskt naboprosjekt bruker Next.js basePath | `../norwegian-marine-protection-explorer/next.config.ts` bruker `/labs/norwegian-marine-protection-explorer` i Vercel. README bekrefter appens eget Vercel-prosjekt og gateway-rewrites med bevart prefiks. |
| Mapbox er allerede brukt lokalt | Blant annet `../argo/frontend/package.json` og konfigurasjonen i gateway viser Mapbox GL. Dette er ikke dokumentasjon på at en eksisterende token/lisens kan gjenbrukes til denne appen. |
| Publisert nettside er ikke visuelt kontrollert | Web-verktøyet kunne ikke åpne apex eller www `/labs`; curl i sandbox fikk DNS-feil. Dette sier ikke at nettsiden er nede. |

`vercel_get_project` hadde en konflikt mellom connectorens og serverens parametervalidering (`projectId` / `idOrName`); prosjektinnstillinger og domenealiaser ble derfor ikke bekreftet med dette endepunktet. Vercels prosjektliste ga første side med 20 prosjekter; pagination-forsøket returnerte samme side. Listen er ikke en full inventarliste.

## Anbefalt integrasjon

Lag appen i dette arbeidsområdet, som eget Vercel-prosjekt. Foreslått offentlig adresse er `https://www.oceandatajo.com/labs/datasenter-analyse-norge`. Den eksisterende `/labs`-forsiden beholdes. Et nytt kort/lenke legges til når gatewayens aktuelle kilde er hentet og inspisert.

Bruk Next.js med TypeScript og `basePath: '/labs/datasenter-analyse-norge'`. Velg og lås den aktuelle støttede versjonen ved oppstart etter å ha lest versjonens medfølgende dokumentasjon. Appen skal fungere på samme sti både under Vercels appdomene og gjennom gateway. Offentlige datafiler, kartstil, bilder og fetch-kall må bruke samme prefiks; ikke hardkod rot-relative `/data/...` som bypasser appen.

I **oppdatert** gateway legges kun to avgrensede rewrites til: grunnstien og alle dens understier, med samme prefiks til appens verifiserte stabile produksjonsalias. Destinasjonsdomene fylles først etter at det faktisk finnes. Ikke bruk en generell `/labs/:path*`-rewrite. Rewrites er en dokumentert måte å kombinere apper uten å endre adressen i nettleseren på: [Vercel Rewrites](https://vercel.com/docs/routing/rewrites), lest 2026-10-01.

Før gateway endres: hent gjeldende remote i separat checkout/worktree, sammenlign med produksjonens SHA og behold samtlige nyere ruter og brukerfiler. Den gamle lokale checkouten må ikke deployes slik den står.

## Kart og grensesnitt

Anbefalt utgangspunkt er MapLibre GL JS og en eksplisitt valgt, lisensiert basiskartleverandør. MapLibre støtter interaktive WebGL-kart og GeoJSON-lag: [offisiell dokumentasjon](https://maplibre.org/maplibre-gl-js/docs/), lest 2026-10-01. Leverandør, pris, attribusjon og kapasitet må kontrolleres før produksjon; MapLibre i seg selv leverer ikke et produksjonsbasiskart. Mapbox er et mulig alternativ dersom eksisterende bruk og tokenavgrensning skal videreføres.

- Kart og synkronisert liste, med filtre for prosjektfase, kommune, dataår og dokumentasjonsnivå.
- Ulike kartlag for dokumentert anleggsposisjon, planområde, tomtegrense, bygningsavtrykk og registrert naturinngrep. Signaturene må ikke antyde at disse betyr samme areal.
- Prosjekter uten forsvarlig posisjon blir stående i listen under «Mangler stedfesting». Ingen syntetisk kommune- eller eiendomsposisjon presenteres som anlegget.
- Prosjektpanel viser påstander med enhet, periode, status, kildelenke, kildedato og hvorfor opplysningen er usikker. Åpne spørsmål har like synlig plass som tall.
- «Påstandskontroll» viser Teknologirådets omtale og publiserte rapporter som forskjellige kildetyper, med støttende, motstridende og utilstrekkelig dokumentasjon knyttet til samme presise påstand.
- Delbare filter-/prosjektlenker, tilgjengelig tabell som alternativ til kartet, tastaturnavigasjon, mobilvisning og nedlasting av publisert datasnapshot.

## Datakontrakt til utvikling

Endelig schema eies av koordinator og kvalitetssikring. Anbefalt struktur er separate tabeller/JSON-filer for `projects`, `observations`, `geometries`, `sources`, `claims` og `reviews`. Ikke gjem prosjektets kildehistorikk i én enkelt «kilde»-lenke.

En observasjon bør minst ha `id`, `projectId`, `metric`, `value` eller dokumentert `range`, `unit`, `scope`, `status`, `validTime`, `sourceIds`, `locator`, `uncertainty`, `reviewStatus` og `reviewedAt`. Kilden trenger `publisher`, `title`, `url`, `publishedAt`, `accessedAt`, `documentType` og ved behov `page`/`section`, `version` og arkiv/hash. Ukjent publiseringsdato er `null` med forklaring; innhentingsdato erstatter ikke publiseringsdato.

Usikkerhet er en diskriminert datatype: `statistical_ci` (metode, nivå og forutsetninger påkrevd), `documented_range` (grunnlag for begge ender), `qualitative` (lav/middels/høy med begrunnelse), eller `unknown`. Et spenn mellom kilder er ikke et statistisk konfidensintervall. Ingen tallverdi brukes for å kode manglende data.

Geometri lagres som GeoJSON i WGS84 med korrekt lengdegrad/breddegrad-rekkefølge. Hver geometri har semantisk type, opphav, kilde-CRS, transformasjon, gyldighetsdato, metode, nøyaktighet og QA-status. Planpolygon og faktisk beslag holdes adskilt. Areal beregnes i egnet metrisk CRS eller med dokumentert geodetisk metode, aldri direkte som kvadratgrader. Samme geometri kan ha kildeoppgitt og beregnet areal som separate observasjoner.

Effekt (MW), årlig energi (GWh/år), nettkø/reservasjon, omsøkt kapasitet og realisert forbruk er forskjellige indikatorer. Jobber, årsverk, anleggsfase og permanente driftsjobber er forskjellige indikatorer. Eierskap har tidsperiode, foretak/organisasjonsnummer og rolle. Summer trenger eksplisitt populasjon, fase, periode og datadekning; manglende prosjekter eller tall gjør en delsum til en delsum.

## Publiseringsflyt og tester

1. Datainnhenting leverer kildebelagte observasjoner og dokumenterte hull; QA godkjenner feltvis, ikke bare hele prosjektet. Ukjent eller bestridt informasjon kan publiseres med korrekt status.
2. Versjonert schema validerer typer, referanseintegritet, enheter, geometri og krav til usikkerhetsmetode. Test spesifikt at kildeintervaller ikke får CI-etikett, MW ikke summeres med GWh, og ukjente data aldri blir nullverdier i summer.
3. Bygg genererer et immutable datasnapshot med dataversjon, kuttidspunkt og endringslogg. Første versjon kan bruke statiske JSON/GeoJSON-filer; ingen database er nødvendig for en liten, kuratert prosjektbase.
4. Kjør typekontroll, produksjonsbygg og relevante datatester. Nettlesertest kontrollerer punkt/polygon, kildeåpning, filterdeling, tomme tilstander, mobil, tastatur og grunn-/understier gjennom basePath.
5. Opprett Vercel preview for appen. Kontroller preview før produksjon. Preview-adressen er ikke den publiserte `/labs`-løsningen.
6. Deploy app, bekreft stabilt alias, legg avgrensede rewrites i ajourført gateway, og kontroller gateway-preview. Test eksisterende labs-ruter som regresjonstest før gateway produksjon.
7. Kontroller offentlig URL, assets, lenker, data og kildevisning etter deploy. Registrer faktisk deploy-ID, commit, dataversjon, klokkeslett og testresultat. Behold forrige verifiserte deploy som rollback-mål.

## Uavklart før gjennomføring

Offentlig UI, domenealiaser og siste gateway-fil må inspiseres direkte når tilgangen tillater det. Basiskartleverandør er ikke valgt. Datasettet og schema er ikke ferdig QA-godkjent. Ingen Vercel-app er opprettet for datasenteranalysen, ingen utviklingstester er kjørt, og løsningen er ikke deployet av dette arbeidet.


## Naturdata etter pilot

Bruk [naturkortskjemaet](../research/natur/naturkort.schema.json) og [pilotdata](../research/natur/naturkort.json) som forskningskontrakt for naturvisningen. Vis førtilstand, endring, konsekvens og kunnskapshull med kilder og datoer. KU-status gjelder komponenter, og planpolygon må merkes som planområde. Betingede karttester må ikke få symbolikk som bekreftet naturtap. `null` skal vises som ukjent, aldri null påvirkning. Ingen samlet naturkarakter. Se [naturmetoden](naturmetode.md) for publiseringskrav. Dette er et integrasjonskrav; ingen app er implementert ennå.
