# Verifikasjon – kartdemo 2026-10-05

- Next.js 16.3.8, Node.js 22.x, låste npm-avhengigheter.
- Produksjonsbygg og TypeScript-kontroll består.
- Fire tester består: kombinerte filtre, ugyldig/ukjent posisjon, merking av uverifiserte påstander, sikker URL-protokoll.
- Tre Playwright-nettlesertester består: ekte ODP-tabeller, kildevisning, koordinater, delbar URL etter reload, tomme treff, verneområdefliser, mobil uten horisontal overflow; separat ODP-feiltest; separat Mapbox-feiltest med Kartverket-basiskart og tastaturstyrt dialog.
- Live ODP fra lokal server: 8 prosjekter, 93 påstander, 45 natur/vannposter, 77 kilde-/metodeposter. Ingen hemmelig ODP-nøkkel funnet i klientbyggets filer.
- Produksjonsavhengigheter: npm audit rapporterte 0 sårbarheter. Utviklingsverktøy har egne transitive varsler; disse er ikke en del av produksjonskjøringen.
- Mapbox Light v11: stil kan hentes, men vektorfliser gir 403 med gjeldende token lokalt. Årsak ikke endelig fastslått; rettigheter/domenebegrensning må kontrolleres. Appen tilbyr eksplisitt valg av Kartverkets gråtonekart og beholder Mapbox som kartmotor. Kartverkets fliser og Miljødirektoratets rasterlag er nettlesertestet med HTTP 200.
- Kilder for karttjenester: https://cache.kartverket.no/ og https://kart.miljodirektoratet.no/arcgis/rest/services/vern/MapServer, kontrollert 2026-10-05. Verneområder er kontekst; ingen overlapps- eller arealtapsberegning.
- Preview krever at brukeren selv legger inn ODP_API_KEY i Vercel og redeployer etterpå. Automatisk kontroll avviste agentens nøkkeloverføring; ingen ODP-nøkkel ble sendt til Vercel av agenten.
- Gateway på oceandatajo.com er ikke endret. Preview-gjennomgang og fungerende ekstern datatilgang gjenstår før integrasjon.

## Vercel-resultat

- Ferdig Preview: https://datasenter-analyse-norge-ez9abgnwg-jo-ovstaas-projects.vercel.app/labs/datasenter-analyse-norge
- Deployment-ID: dpl_HtGrMJL4PNfD31nApAsfdGS9ZX5C. Vercel build READY, beskyttet med Vercel Authentication.
- Verifisert med `vercel curl`: hovedside HTTP 200; `/api/atlas` HTTP 503 fordi ODP_API_KEY ikke var konfigurert for Preview. ODP-data er derfor ikke bekreftet fra Vercel ennå.
- Offentlig Mapbox pk-token og ODP-baseadresse er konfigurert for Preview. ODP-nøkkelen skal legges inn av brukeren som Sensitive/Secret, etterfulgt av ny Preview-deploy.
- Vercel opprettet først automatisk en Production-deploy siden prosjektet var nytt. Den ufullstendige deployen ble fjernet; den eksplisitte Preview-deployen beholdes. Ingen ruter på oceandatajo.com er endret.
- Lokale skjermbilder: `demo-desktop.png` (Kartverket-basiskart i Mapbox) og `demo-mobile.png` (naturpanel).

Neste gjennomføring etter nøkkeloppsett: `npx vercel deploy --target preview --yes --scope jo-ovstaas-projects`, kontroller `/api/atlas` og alle fire radantall, test Mapbox-fliser fra preview-domenet og oppdater den daterte verifikasjonsloggen. Gateway integreres først etter fungerende preview.

## Oppfølging etter brukerens nøkkeloppsett

Brukeren la ODP_API_KEY inn som Sensitive/Secret for Production. Dette ga fortsatt HTTP 503 i første nye Preview (dpl_F5mPE8U93WbK45Euzn6W43kCSPbi). Kun variabelens miljøvalg ble deretter utvidet til Production + Preview gjennom Vercel API; nøkkelverdien ble ikke hentet ut eller endret.

## Produksjon og offentlig kildekode

Brukeren autoriserte commit/push til main og integrasjon i oceandatajo.com/labs.
README er omskrevet med faktisk appstatus, metode, kjente begrensninger, lokal kjøring og deploy.
Egen kode får MIT-lisens; tredjeparts-PDF-er, HTML-kopier og tekstuttrekk utelates fra offentlig Git.
Kontroll mot lokale nøkkelverdier ga null treff blant 125 aktuelle filer før LICENSE/README-commit.
Enhetstester (4) og TypeScript-kontroll bestod på nytt.
Produksjonsbygg dpl_ug3vvtWYRSP9yYasBB8fy8ny4Xry bestod på Vercel.
Offentlig side på datasenter-analyse-norge.vercel.app svarte 200; API svarte 503.
Siste diagnostiserte upstream-feil var ODP_HTTP_403; datatilgang er ikke verifisert i produksjon.
Eksisterende Mapbox/base-URL-variabler ble utvidet til Production uten å endre verdiene.
ODP-nøkkelen er brukerens egen Vercel-variabel og ble ikke overskrevet fra lokal .env.

## Sluttkontroll – offentlig Labs-adresse

Brukeren ga ODP-nøkkelen tilgang til selve datasettene i ODP-admin. Deretter svarte
https://oceandatajo.com/labs/datasenter-analyse-norge/api/atlas med HTTP 200 og
utgivelse 2026-10-05-r2: 8 prosjekter, 93 påstander, 45 natur-/vannrader og 77 kilder.
Ingen lokal nøkkel ble lastet opp som del av denne rettingen.

Appens main-commit 8d49251 utløste vellykket Git-deploy
(dpl_4dKCQDNPSKuCmjsWuHPc1EhJ3EGM). Gatewayens main-commit 650f074 la til to
rewrites og utløste vellykket produksjonsdeploy (dpl_JAQjc7zHHikMePtkwjJsowE7vYSS).
Eksisterende rewrites og redirects ble sammenlignet og beholdt uendret.
Offentlig Labs-side, CSS og JavaScript svarte HTTP 200.

Playwright mot offentlig Labs-adresse bestod:
- Ekte ODP-data, 8 markører, søk, kilder, prosjektvalg, delbar URL, tomt søk,
  verneområder og mobilvisning uten horisontal overløp eller JavaScript-feil.
- Eksplisitt feilvisning når ODP-feil simuleres.
- Kartverkets basiskart ved simulert Mapbox-feil, samt tastaturlukking av dialog.

Første kjøring av fallback-testen feilet fordi det gamle glob-mønsteret ikke
matchet Mapbox-fliser med flere stisegmenter. Testen ble rettet til URL-predikat
for api.mapbox.com og .vector.pbf; ny kjøring bestod. Produksjonskode var uendret.
TEST_APP_URL kan nå velge testmål. Produksjonsskjermbilder erstatter lokale bilder.
Mapbox-basiskart fungerte på produksjonsdomenet ved sluttkontrollen.
