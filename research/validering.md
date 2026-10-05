# Sluttkontroll av forskningsfiler

Kontrollert 2026-10-01 av hovedagenten, etter at innsamlerens filer var ferdig skrevet. Versjon 0.2.0 av prosjektutvalget.

- 8 prosjekter, 75 prosjektopplysninger og 37 prosjektkilder.
- 6 adressepunkter samsvarer eksakt med koordinatpar i lagrede Kartverket-svar.
- 2 planomriss samsvarer eksakt med råresponsenes x/y-ringer; begge er lukket og har endelige numeriske koordinater.
- CRS-forbehold, QA-status, kilde-URL og felt for siste behandling følger hver GeoJSON-feature. Ukjent siste behandlingsdato er tillatt som null.
- 8 påstander/kontrollspørsmål og 12 kilder i påstandsregisteret.
- Begge JSON-registre kan parses, har unike kilde-ID-er og gyldige interne kildereferanser. Alle kilder har innhentingsdato.
- Alle prosjektopplysninger har kilde-ID, konfidensnivå og begrunnelse; ingen har konstruert statistisk konfidensintervall.

Kontrollen bekrefter struktur og tapsfri overføring. Den bekrefter ikke innholdets sannhet, dagens driftsstatus, alle lenkers tilgjengelighet, geodetisk korrekthet, juridisk plangrense eller full datadekning. Se `qa-prosjekter.md` for uavhengig, avgrenset kildekontroll.

SHA-256 for kontrollerte sluttfiler:

| Fil | SHA-256 |
|---|---|
| prosjekter.json | 72d745f0683f97c00ceb29dd514e124c62b5e0dd3bc76dab81616426b8cb8e53 |
| pastander.json | 128e093fee9305d21ed070ff8e75ce71cffcad0610ceff7e4115b6ed3b392d2e |
| planomriss.geojson | 4c779465348bb273001347df14d7f6c393c7b77a2fe2a352ea07df6a61a0d824 |

## Tillegg 2026-10-05: koordinatretting

Undheim og Gromstul er supplert med dokumenterte Kartverket-adressepunkter. Åtte prosjekter har nå punkter. Den daterte kontrollen og kontrollsummene over gjelder tidligere filversjon. Nytt kildebelegg, SHA-256 og avgrensning er dokumentert i `raw/location-review-2026-10-05/manifest.json` og `stedfesting-2026-10-05.md`. Naturpolygonene er uendret.
