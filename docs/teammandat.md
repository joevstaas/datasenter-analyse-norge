# Agentteam: Norske datasentre

Opprettet 2026-10-01. Arbeidsområde: `/Users/joovstaas/Projects/datasenter-analyse-norge`.

Oppdatert etter brukerens godkjenning 2026-10-01: Naturpåvirkning er et eget hovedspor med tre piloter før nasjonal skalering. Se `docs/naturmetode.md`.

## Mandat

Bygg et etterprøvbart kunnskapsgrunnlag for en interaktiv kartløsning under oceandatajo.com/labs, med Vercel som publiseringsplattform. Vis dokumentert kunnskap, uenighet og mangler uten å fylle hull med antakelser. Første innsamling er et eksplisitt utvalg, ikke en nasjonal fulltelling.

## Ansvar og leveranser

| Rolle | Aktiv agent | Ansvar | Leveranse |
|---|---|---|---|
| Datainnhenting | datainnhenting | Prosjektidentitet, geografi, areal, kraft, natur, økonomi og eierskap | research/prosjekter.json og research/prosjekter.md |
| Kvalitetssikring | kvalitetssikring | Etterprøve Teknologirådets påstander; søke motbevis; kontrollere definisjoner, tidspunkt og kildeavhengighet | research/pastander.json og research/teknologiradet.md |
| Utvikling | utvikling | Undersøke eksisterende nettsted, Vercel og integrasjon; definere kart og dataflyt | docs/utvikling.md |
| Redaktør og integrasjon | hovedagent | Datakontrakt, avgrensning, tverrkontroll, kunnskapshull og publiseringskriterier | docs/datametode.md og samlet design |
| Naturutredninger | natur_utredninger | KU, feltarbeid, myndighetsmerknader og tiltaksstatus for Gromstul/Heggvin | research/natur/utredninger.md og .json |
| Natur og kartanalyse | natur_gis | Autoritative tjenester, kartleggingsdekning, etterprøvbare søk og geometritolkning | research/natur/gis-screening.md og .json, råsvar |
| Natur og vannmiljø | kvalitetssikring | Narvik/Kvandal: campus kontra kjølevann, planprogram og natur-/vannkilder | research/natur/narvik.md og .json |

I naturpiloten er kvalitetssikring-agenten også innsamler for Narvik. Hovedagenten kontrollerer derfor Narvik-kortet; agentens eget arbeid merkes ikke uavhengig kontrollert av samme agent. Hovedagenten samordner alle tre naturkort og kontrollerer utvalgte funn fra de øvrige agentene. Naturfaglig feltvalidering inngår ikke i agentenes skrivebordsanalyse.

Agentene arbeider parallelt i separate filer. Datainnsamlerens egen konfidensvurdering er ikke det samme som uavhengig QA. QA-agenten har i første runde hovedansvar for påstandsetterprøving; prosjektdata skal gjennom en egen krysskontroll før de merkes kvalitetssikret.

## Arbeidsflyt

1. Registrer kilden og hva som faktisk er lest. Søketreff er søkespor, ikke bekreftelse.
2. Identifiser prosjekt, anlegg, byggetrinn og operatør separat. Behold alternative navn som aliaser.
3. Registrer hver opplysning med enhet, definisjon, periode, kilder og usikkerhet.
4. Undersøk avvik mot uavhengige kilder. Uavklarte motstridende opplysninger beholdes side om side.
5. Kontroller geometri og kildegrunnlag før kartvisning. Manglende geometri gir listeoppføring.
6. Valider datasettet og kvalitetssikringsstatus. Publiser et versjonert øyeblikksbilde.
7. Verifiser forhåndsvisning, kildepanel, filtrering og navigasjon før produksjonsdeploy.

## Prioritert videre kartlegging

- Sammenstill Nkom-operatører, Statnett-tilknytningssaker, kommunale planregistre og offentlig annonserte anlegg; logg søkedekning.
- Hent vedtatte plangrenser med plan-ID og vedtaksdato for hvert valgt prosjekt.
- Skill regulert areal, tomt, planlagt inngrep, observert nedbygging og gulvareal.
- Innhent kraftforbruk per anlegg der tilgjengelig; behold ellers feltet som ukjent.
- Gjennomfør naturpilotene Gromstul, Heggvin og Narvik/Kvandal etter `docs/naturmetode.md`. Lag naturkort med førtilstand, planlagt/observert endring, vurderte konsekvenser og kunnskapshull. Registrer egen dokumentasjonsstatus for tilknyttet infrastruktur, og skill kartoverlapp fra dokumentert skade.
- Kontroller eierkjeder og faktisk lokal sysselsetting mot daterte selskapskilder.

Ingen vedvarende bakgrunnsdrift eller automatisk oppdateringsplan er opprettet. Teamet gjelder dette arbeidet; senere oppdateringer krever en ny kjøring eller en eksplisitt avtalt automasjon.
