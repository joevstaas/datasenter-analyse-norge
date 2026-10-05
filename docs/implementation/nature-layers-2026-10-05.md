# Naturkartlag – kontrollert 5. oktober 2026

Første utvidelse omfatter Naturtyper på land (NiN), tilhørende dekningskart og
Naturtyper på land og i ferskvann (HB13). Myr/AR5 er neste foreslåtte trinn og er ikke implementert.

## Kilder og teknisk kontroll

- NiN: https://kart.miljodirektoratet.no/arcgis/rest/services/naturtyper_nin/MapServer/0
- Dekning: https://kart.miljodirektoratet.no/arcgis/rest/services/naturtyper_nin/MapServer/1
- HB13: https://kart.miljodirektoratet.no/arcgis/rest/services/naturtyper_hb13/MapServer/0
- Dekningsforklaring: https://register.geonorge.no/geolett/1087/
- NiN-tjeneste i Geonorge: https://kartkatalog.geonorge.no/Metadata/uuid/fed10e38-5850-4e80-948b-10c34ae323fb
- HB13: https://kartkatalog.geonorge.no/metadata/naturtyper-paa-land-og-i-ferskvann-hb13/d776ff93-104d-4aa5-a8d9-276df01eb51c

Tjenestemetadata, felter, skala og tegneregler lest 05.10.2026. Innhentingsdato er
ikke kartleggingsdato. Kartleggingsår/instruks for NiN og dekning, samt
registrerings-/datafangstdato for HB13 vises ved punktoppslag der oppgitt.
Kildeleverandør: Miljødirektoratet / Naturbase. Kartlagene holdes utenfor ODP-utgivelsen.

Kartet bruker leverandørens raster og tegnforklaring, ikke egne verdiklasser.
NiN/HB13 har minScale 1280001; appen viser dem fra zoom 8 og gir zoomveiledning.
Dekningslaget har ingen slik skalagrense. Attributter dekodes med tjenestens egne
kodelister, eksempelvis HB13 D06 → Beiteskog og C → Lokalt viktig.

`/api/natur` godtar bare tre forhåndsdefinerte lag og modus tile/legend/identify.
Punkt og bbox valideres. Ingen fri URL, SQL eller nøkler videresendes. Oppslag
bruker eksakt punktinterseksjon, ikke en antatt påvirkningssone; inntil ti treff
per lag med eksplisitt avkortingsvarsel. Feil skilles fra tomme treff. Resultater
kan bufres inntil ett døgn. Skifte av lag eller nytt klikk avbryter gamle oppslag.

## Faglig avgrensning

Adressepunkt er ikke anleggsgrense. Ingen overlappsarealer, naturtap, risikoscore
eller nasjonale summer beregnes. Fravær av registrering er ikke fravær av naturverdi.
Dekning beskriver kartleggingsarbeid, ikke økologisk kvalitet. NiN og HB13 kan
over­lappe og har ulike metoder; de summeres ikke. Kvalitetsvurdering i kilden er
ikke dokumentasjon på påvirkning fra et datasenter. Registreringer beskriver ikke
nødvendigvis naturens tilstand på dagens dato.

## Kontroller

TypeScript og fire enhetstester bestod. Ny Playwright-test bestod mot localhost:5174:
alle tre lag returnerte PNG, fire legendesymboler lastet, zoomveiledning vises,
punktoppslag returnerer svar, mobilmeny fungerer uten horisontal overløp og
ugyldige lag/bbox/punkter gir 400. Ingen JavaScript-feil i testen.

Reelle punktoppslag kontrollert i hver tjeneste: Hatlarørene nord (NiN, 2023),
ToftøyNord (dekning, 2020), Bartnes NØ (HB13, Beiteskog D06, Lokalt viktig C).
Disse er tekniske kontrollpunkter, ikke funn om datasenterprosjektene.

Produksjonsbygg bestod. Eksisterende nettlesertester for data/mobil, ODP-feil og
Kartverket-alternativ bestod etter endringen. Naturtesten ble justert til å
registrere vellykkede flisresponser før aktivering, fordi en ny aktivering av et
allerede lastet lag ikke nødvendigvis lager en ny nettverksforespørsel. Oppdatert
test bestod på nytt (10,2 sekunder).
