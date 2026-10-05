# Avgrenset kvalitetskontroll – 2026-10-01

Kontrollør: hovedagent. Naturutrednings- og GIS-agentene leverte sine egne undersøkelsesgrunnlag. Agenten med navnet kvalitetssikring innhentet Narvik-data og regnes derfor ikke som uavhengig kontrollør av egne Narvik-funn.

## Kontrollert

- Lest LE01-fulltekst for geografisk omfang og konklusjon om netto biodiversitetstap. Konklusjonen beholdes på samlet Heggvin/Sirkula-nivå. Forsøk på PDF-skjermbilde lyktes ikke; ingen full visuell tabellkontroll påstås. Intern forskjell i verdiangivelse for korridor er fortsatt uavklart i underlagsnotatet.
- Lest Gromstuls miljøprogram for historisk myr/drenering og miljøkrav. Original natur-KU er fortsatt referanse, ikke fulltekstbevis. Programkrav er ikke dokumentasjon på gjennomført avbøting.
- Kontrollert Narviks historiske natur-KU og lokalt lagret tekst fra nytt kjølevannsplaninitiativ/oppstartsreferat: eget KU-krav, uavklart temperatur og varslingsområde med alternative traseer. Historisk rapport brukes ikke som godkjenning av ny kjøling. Dokumentenes versjonsavvik beholdes i kilderegisteret.
- Gjennomgått GIS-skriptets skille mellom søkerektangel og betinget polygonberøring. Kjørt polygontesten på nytt: 52 geometrier testet, ingen ugyldige/utelatte. Ingen arealberegning utført; plan-CRS fortsatt ubekreftet.
- Kjørt `python3 research/natur/validate_natur.py`: bestått for tre naturkort, 16 kilder, åtte komplette spørringer og 30 råfiler med hashkontroll. Fem negative kontroller bestått.

## Ikke kontrollert eller godkjent

Ingen feltbefaring, full økologisk fagfellevurdering, bekreftet plan-CRS, komplett kartleggingsdekning, før-/etteranalyse eller målt naturtap. Ikke alle originalrapporter eller nyeste revisjoner er innhentet. Dekningspolygoner er ikke bevis på full temadekning. Ukjente publiseringsdatoer beholdes som ukjent.

Skjemaet er bevisst begrenset til pilotens dokumentasjonsnivå: faktisk naturtap må være `null`, og arealberegning kan ikke være godkjent. Det må versjoneres før kvalitetssikrede arealmålinger senere kan inkluderes. Maskinell kontroll verifiserer struktur og bevart evidens, ikke at naturfaglige utsagn er sanne.

## Reprodusering

Kjør fra prosjektroten, med Python, jsonschema og Shapely tilgjengelig:

```sh
python3 research/natur/build_narvik_card.py
python3 research/natur/build_naturkort.py
python3 research/natur/run_conditional_intersections.py
python3 research/natur/validate_natur.py
```

Dette bruker lagrede kilder. Nytt nettuttrekk via `run_screening.py` kan gi andre resultater og krever ny faglig kontroll. Bevar tidligere uttrekk før oppdatering. PDF-kildene og deres manifest ligger i `raw/`; utredningsagentens fulltekstuttrekk er tekstbevis, ikke et komplett PDF-arkiv.


## Tillegg 2026-10-05

Hovedagenten har lest Statsforvalterens tillatelse for Gromstul datasenter 1, s. 1–4, via nettverktøy. Den lokale PDF-nedlastingen feilet på DNS; kontrollnotat med URL/tilgangsbegrensning er lagret. Ingen full arkivert kopi påstås. Nye opplysninger er historiske myndighetsutsagn, ikke uavhengig feltkontroll. Naturvalidatoren består fortsatt: tre kort, nå 17 kilder, åtte tidligere GIS-spørringer og 30 råfiler. GIS-data er ikke oppdatert til 05.10. Separat `validate_report_update.py` kontrollerer vannpilotens nullverdier, kildereferanser og bevaring av tidligere prosjektdata.
