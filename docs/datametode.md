# Datametode og publiseringskriterier

Versjon 0.2, 2026-10-01. Naturhovedsporet og pilotmetoden er godkjent av brukeren. Research-filene er innsamlede arbeidsdata og skal normaliseres og kontrolleres før publisering.

## Grunnenhet og sporbarhet

Prosjekt, fysisk anlegg, byggetrinn, eiendom og juridisk selskap har separate ID-er. Ett prosjekt kan omfatte flere anlegg og faser. En operatør kan drive flere prosjekter. Unngå å summere campuskapasitet og underliggende byggetrinn to ganger.

Hver faktapåstand skal ha:

- stabil ID, prosjekt-/fase-ID, felt og verdi; null for ukjent verdi;
- måleenhet, begrepsdefinisjon og geografisk avgrensning;
- observasjonsperiode eller tidspunktet opplysningen gjelder; ukjent dersom ikke dokumentert;
- status: observert, vedtatt, omsøkt, annonsert, modellert eller ukjent;
- én eller flere kilde-ID-er med presis side, tabell, avsnitt eller API-felt;
- usikkerhetstype, begrunnelse og eventuelle intervallgrenser;
- innsamler, kontrollør, kontrolltid og kontrollstatus;
- relasjon til tidligere versjoner og motstridende påstander.

En kildepost inneholder URL, tittel, utgiver, kildetype, publiseringsdato, oppdateringsdato, innhentingstid, opprinnelig datasettversjon og tilgangsstatus. Manglende publiseringsdato lagres som null med forklaring; innhentingsdato erstatter den ikke. Når det er mulig lagres kildefil eller relevant uttrekk med sjekksum. Fulltekst som ikke er tilgjengelig merkes eksplisitt. Sitat og parafrase skilles.

Partskilde, myndighet, forskning og presse er forskjellige kildetyper, ikke en automatisk sannhetsrangering. En operatør kan være primærkilde til egne planer uten å dokumentere at planen er realisert. En avis som gjengir en rapport er ikke en uavhengig bekreftelse av rapporten.

## Koordinater og arealer

Kartobjekter merkes som adressepunkt, dokumentert anleggspunkt, planpolygon, eiendomsgrense, planlagt inngrep eller observert inngrep. Kommune- eller stedsmidtpunkter skal aldri presenteres som prosjektplassering. Et adressepunkt dokumenterer adressen, ikke datasenterets utstrekning. Ingen automatisk buffer rundt et punkt brukes som arealbeslag.

Behold kildekoordinatsystem, akseorden, originalgeometri, metode, geometridato, plan-ID og kilde. Kartvisning bruker GeoJSON med lengdegrad før breddegrad; transformasjoner til WGS84 dokumenteres. Ikke antyd større nøyaktighet enn kilden støtter. Et koordinatsystems oppgitte desimaler er ikke en måling av stedfestingsnøyaktighet.

Beregn areal i et egnet projisert koordinatsystem eller med dokumentert geodetisk metode, aldri direkte i kvadratgrader. Lagre metode, CRS, verktøyversjon, input-sjekksum og avrunding. Polygoner kontrolleres for gyldighet, lukking, hull og overlapp. Summer union av overlappende geometrier for samlet areal; behold opprinnelige objektarealer separat.

Vis følgende størrelser hver for seg: tomteareal, samlet planområde, areal regulert til datasenter, bygningenes fotavtrykk, samlet gulvareal, midlertidig anleggsareal, permanent nedbygd areal og tilknyttet infrastruktur. Plangrense er ikke dokumentasjon på at hele området er nedbygd.

## Kraft og energi

Skill IT-effekt, samlet tilknytningseffekt, omsøkt effekt, reservert nettkapasitet, installert effekt, faktisk maksimal effekt og målt årsforbruk. MW og TWh er forskjellige størrelser. En omregning fra MW til årsenergi krever dokumentert brukstid og eventuelt PUE, og publiseres som et beregnet scenario med formel og forutsetninger. Standard full last i 8 760 timer må ikke fremstilles som faktisk forbruk.

Et nasjonalt sektoranslag skal ikke fordeles på anlegg uten datagrunnlag. Nettkø, reservekapasitet og byggetrinn kan være overlappende eller alternativer; summering krever eksplisitt kontroll. Prognoser sammenlignes etter publiseringsår, målår, prosjektmodenhet og forutsetninger.

## Naturpåvirkning

Natur er et obligatorisk hovedspor med egen dokumentasjons- og GIS-kontroll. `docs/naturmetode.md` beskriver arbeidsstandarden, pilotvalg, kartleggingsdekning og datakontrakt. Hvert prosjekt får et naturkort med førtilstand, endring, konsekvens og kunnskapshull; KU kontrolleres per komponent og planversjon.

Skill eksisterende naturverdier, beregnet romlig overlapp, konsekvensutredet påvirkning og observert endring. Registrer naturtype, myr, skog, jordbruksareal, vassdrag, vannbruk, støy, utslipp og eventuell infrastruktur der dokumentert. Bevar førtilstand og kartleggingsdato.

Fravær av registrerte arter eller naturtyper betyr ikke fravær av naturverdier. Overlapp viser ikke alene økologisk konsekvens eller årsak. Avbøtende tiltak registreres separat som foreslått, vedtatt eller dokumentert gjennomført. Planlagt spillvarmeutnyttelse er ikke dokumentert varmeleveranse.

Geografiske søketreff merkes som bbox-kandidater, betinget polygonoverlapp eller verifisert polygonoverlapp. Bekreft kilde-CRS og prosjektgeometri før arealberegning. Før-/ettergrunnlag skal ha opptaksdato; dagens industriklassifisering erstatter ikke naturen før inngrep. Dokumenter også vei, nett, massedeponi og kjølevann der prosjektkoblingen er kjent.

Metode- og rødlisteutgave følger hvert naturfunn. Antall artsobservasjoner brukes ikke som biodiversitetsscore, og utilstrekkelig kartlegging merkes ikke som liten påvirkning. Ukjent faktisk naturtap lagres som null med begrunnelse. Det innføres ingen samlet naturpoengsum.

## Verdiskaping og eierskap

Skill omsetning, investering, bruttoprodukt/bearbeidingsverdi, skatt og samfunnsøkonomisk nettoeffekt. Behold valuta, prisår, beregningsmetode og geografisk nivå. Skill varige arbeidsplasser, personer, årsverk, byggefasens samlede årsverk, innleide og modellberegnede ringvirkninger. Direkte, indirekte og induserte effekter holdes fra hverandre.

Skill grunneier, utbygger, anleggseier, operatør, kunde, morselskap og dokumentert ultimate eier. Organisasjonsnummer identifiserer norsk juridisk enhet. Eierandeler, land og eierkjede gjelder en bestemt dato. En kjent stor kunde dokumenterer ikke eierskap. Uavklart ultimate eierskap skal stå uavklart.

## Usikkerhet

| Type | Når den brukes | Obligatorisk dokumentasjon |
|---|---|---|
| Statistisk konfidensintervall | Reell statistisk estimering med forsvarlig metode | Parameter, utvalg, estimator, konfidensgrad, nedre/øvre grense, antakelser og metodekilde |
| Dokumentert spenn | Kilden oppgir et spenn, eller eksplisitte scenarier gir ytterpunkter | Begge grenser, definisjon, kilder og om scenariene er sammenlignbare |
| Kvalitativ konfidens | Dokumentasjonen gir ikke statistisk grunnlag | Høy/middels/lav og konkret begrunnelse |
| Ukjent | Opplysningen mangler eller kan ikke tolkes forsvarlig | Hva som mangler, søk/tilgangsforsøk og neste dokumentasjonsbehov |

Kvalitativ konfidens er en redaksjonell vurdering av evidensen, ikke en sannsynlighet for realisering. Høy krever klart samsvar mellom kilde, definisjon og tidspunkt samt relevant kontroll. Middels brukes ved identifiserbare begrensninger, som udaterte operatørdata. Lav brukes ved vesentlig uavklart grunnlag; ubekreftede søkespor vises ikke som fakta. Motstridende definisjoner skal ikke gjøres om til et tilsynelatende statistisk intervall.

## Teknologirådet og motbevis

Hver undersøkt påstand får identifiserbar avsender, dato, kanal, avgrenset ordlyd/parafrase, tilhørende rapport hvis funnet, og presis henvisning. Omtale, kronikk, intervju, arrangement og publisert rapport skilles. En rapport omtalt som kommende registreres ikke som publisert. Et mislykket søk dokumenterer bare at rapporten ikke er funnet i den avgrensede undersøkelsen.

Registrer støttende, motstridende og nyanserende dokumentasjon, også om den kommer fra samme kilde. Vurder samme tidsperiode, populasjon, effektmål og systemgrense. Mulige utfall: støttet innen avgrensning, delvis støttet, motsagt innen avgrensning eller uavklart. Normative råd merkes som vurderinger og behandles ikke som sanne/usanne faktapåstander.

## Publiseringsporter

1. Alle viste faktaverdier har fungerende kildereferanse eller merket utilgjengelig historisk kilde, datoopplysninger og usikkerhet.
2. Kartobjekter har kildegeometri/metode og type. Ukjent geometri gir synlig listeoppføring, ikke oppdiktet plassering.
3. Ingen aggregater blander faser, enheter, definisjoner, tidspunkter eller plan/faktisk uten eksplisitt forklaring.
4. Dekning vises som antall i dette utvalget med kjente/ukjente felt; ikke som andel av alle norske prosjekter uten dokumentert nevner.
5. Uavklarte konflikter og kunnskapshull er tilgjengelige direkte fra prosjektvisningen.
6. Data valideres maskinelt og et utvalg kontrolleres mot originalkilder av en annen agent enn innsamleren. Kontrollomfang oppgis; ingen generell QA-merkelapp uten faktisk kontroll.
7. Grensesnittet testes på mobil, med tastatur, uten karttilgang og med tomme treff. Nedlastbare data beholder kilder og usikkerhet.
