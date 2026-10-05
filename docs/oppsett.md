# Oppsett for den åpne kartdemoen

Prosjektnavn: **Datasentre i Norge – åpen kartdemo**. GitHub-navnet `datasenter-analyse-norge` beholdes: det er beskrivende og samsvarer med prosjektmappen.

## Lokale variabler

En lokal `.env` er klargjort. Fyll inn `ODP_API_KEY` og `NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN`. `.env.example` er den tomme, delbare malen. `.gitignore` utelater lokale env-filer. Ikke legg nøklene i kilderegister, dokumenter eller chat.

- `ODP_API_KEY`: hemmelig nøkkel for import og servertilgang; aldri send den til nettleseren.
- `ODP_API_BASE_URL`: ODP-tjenestens baseadresse. SDK-/importintegrasjonen må eksplisitt kobles til denne variabelen.
- `ODP_COLLECTION_ID`: brukerens eksisterende kolleksjon, ferdig utfylt.
- `ODP_*_DATASET_ID`: tomme inntil datasett faktisk er opprettet. Ingen oppdiktede UUID-er.
- `NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN`: offentlig Mapbox-token (`pk.*`), med relevante domenebegrensninger. Den er synlig i nettleseren etter bygging.
- `NEXT_PUBLIC_SITE_URL`: lokal adresse foreløpig. Endelig URL og eventuell Labs-understi avklares ved integrasjon.

`scripts/sync_odp.py` laster `.env` og bruker ODP-variablene. Webappen er ennå ikke implementert. Ved Vercel-deploy legges nødvendige variabler i prosjektets miljøinnstillinger; en lokal `.env` overføres ikke automatisk. GitHub- og Vercel-tokens er ikke nødvendige i denne malen når deres vanlige CLI-/plattforminnlogging brukes.

## ODP-navn og beskrivelser

`config/odp-catalog.json` er en ikke-hemmelig metadataplan for eksisterende kolleksjon og fem tilknyttede datasett. Kolleksjonen er bekreftet gjennom autentisert API og har fått oppdatert beskrivelse. Alle fem datasett er opprettet og knyttet til kolleksjonen. Ett versjonert JSON-uttrekk per datasett er lastet opp og lest tilbake med SHA-256-kontroll. UUID-ene er lagret i konfigurasjonen og den lokale `.env`. Kolleksjonen og datasettene er private; ingen offentlig publisering er forespurt.

Ved import brukes stabile prosjekt- og kilde-ID-er, og en felles utgivelsesversjon på tvers av datasettene. Bevar historikk og ukjentverdier. Kontroller lesetilgang separat fra publiseringsstatus, og verifiser at data kan leses tilbake før kartdemoen bruker dem.

## Åpen publisering

Demoformål og KI-basert innhenting skal stå i både README, ODP-metadata og nettsiden. Et offentlig repo alene gir ikke en åpen kildekodelisens. Prosjektlisens må fastsettes før det presenteres som lisensiert open source; tredjepartsrapporter og datasett beholder sine egne rettigheter. Ingen ny lisens er lagt på disse filene.

Arbeidsmappen er koblet til GitHub-repoet lokalt. Forskning og rapportfiler er ikke automatisk pushet eller publisert som del av oppsettet.

## Synkronisering

Installer `requirements-odp.txt`, og kjør `python3 scripts/sync_odp.py` fra prosjektet. Skriptet gjenbruker lagrede datasett-ID-er og filer med samme innholdshash. Det sletter ingen data og endrer ikke synlighet. Ved uklart utfall ved opprettelse sjekkes navnet før et nytt datasett opprettes. Utgivelsen er et forskningsøyeblikksbilde merket `2026-10-05-r2`; revider utgivelsesnavn ved neste innholdsrunde.

Datasettene har både bevarte JSON-uttrekk og typede tabeller. Prosjekttabellen har åtte WGS84-adressepunkter med klassifisert og indeksert geometri, samt klassifiserte bredde-/lengdegradskolonner. Planområdenes kilde-CRS er ubekreftet; deres WKT er derfor bevisst vanlig tekst uten kartklassifisering. Mapbox-tokenets tilstedeværelse er sjekket, men dets tilgang og domenebegrensninger er ikke testet i nettleser.

## Typede tabeller

Kjør `python3 scripts/sync_odp_tables.py --check` for lokal skjemakontroll, og `python3 scripts/sync_odp_tables.py` for opprettelse og tilbake-lesing. Alle felt har beskrivelser, numeriske verdier er float64, kontrollflagg er boolske og naturkortenes kontrollerte datoer er date32. Kildedatoer med varierende presisjon og sammensatte perioder bevares som tekst. Kilder kobles med navneromsbestemte nøkler (`projects:`, `national:`, `nature:`).

Verifisert tabellinnhold: prosjekter 8 rader, opplysninger 93, planområder 2, natur/vann 45 og kilder/metode 77. Alle åtte prosjekter har dokumentert adressepunkt; faktisk arealavgrensning må fortsatt kontrolleres. Narvik finnes i naturpiloten, men er ennå ikke innlemmet som prosjekt i hovedregisteret. Naturtabellen er en tabell over funn og metrikker, ikke over 45 prosjekter. Komplekst underlag bevares i tillegg i `details_json`.

Skriptet kontrollerer alle radverdier og kolonnemetadata etter opplasting. Det gjenbruker identiske tabeller og stopper hvis eksisterende skjema eller verdier avviker, fremfor å slette eller overskrive. Koordinatrettelsen 2026-10-05 utføres med `python3 scripts/apply_location_review.py`, som kontrollerer forventet førtilstand og endrer bare to prosjektrader samt legger til seks kilder i transaksjoner. Kommandoen kan gjentas trygt; uventede samtidige endringer avbryter. Senere endringer krever en ny dokumentert oppdateringsstrategi. Fil- og tabellimport er separate kommandoer: kjør begge ved en koordinert ny utgivelse. JSON-filene beholdes som øyeblikksbilder; tabellene er laget fra samme lokale forskningsgrunnlag.

EPSG:4258-adressepunkter er transformert til EPSG:4326 med pyproj (`always_xy=True`). Transformasjon gir ikke større presisjon enn kildepunktet, og adressepunkter er fortsatt ikke anleggsgrenser. Ingen arealberegning er gjort. Portalens visuelle kartvisning er ikke nettlesertestet; tabellverdier og kartmetadata er verifisert via SDK.

## Webapp og Vercel Preview

Appen er implementert. Start med `npm ci` og `npm run dev`, og åpne `/labs/datasenter-analyse-norge`. Vercel-prosjektet heter `datasenter-analyse-norge`. Brukeren legger selv inn `ODP_API_KEY` som Sensitive/Secret i Preview. Offentlig Mapbox-token bruker navnet `NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN`. Endrede miljøvariabler krever ny deploy.

Se [verifikasjonsloggen](implementation/verification-2026-10-05.md) for testomfang, faktisk preview-adresse, ekstern datatilgang og kjente Mapbox-begrensninger.
