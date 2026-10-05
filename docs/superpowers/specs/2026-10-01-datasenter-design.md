# Norske datasentre: kildebasert kart under Labs

Designforslag for gjennomgang, 2026-10-01. Ikke implementert eller deployet.

Naturhovedsporet er godkjent og konkretisert av brukeren i etterfølgende samtale 2026-10-01. Naturmetode og pilot inngår nå i kravene; dette dokumenterer ikke en ferdig webimplementering.

## Formål og avgrensning

Brukerens bestilling: et agentteam skal kartlegge norske datasenterprosjekter for en interaktiv kartbasert web-løsning på oceandatajo.com/labs, deployet på Vercel. Koordinater, arealavgrensninger, arealbeslag, kraft, naturpåvirkning, verdiskaping og eierskap skal være dokumentert. Alle fakta skal være daterte og ha etterprøvbare kilder og forsvarlig usikkerhet. Teknologirådets offentlig omtalte påstander skal etterprøves med både støttende og motstridende dokumentasjon; omtale skal skilles fra publisert rapport.

Arbeidsantakelse: norsk bokmål og offentlig tilgjengelig, nøytral forsknings-/opplysningsløsning. Første dataversjon er et avgrenset og tydelig merket prosjektutvalg. Nasjonal fullstendighet hevdes ikke. Løsningen skal kunne utvides med flere prosjekter og dokumentasjon uten å endre kjernearkitekturen.

## Valgt retning og alternativer

Anbefaling: separat Next.js-app med versjonerte JSON-/GeoJSON-data, interaktivt kart og synkronisert liste. Egen Vercel-deploy rutes fra eksisterende Labs. Dette gir en enkel, etterprøvbar publiseringskjede for kuraterte data.

Alternativet med å bygge alt direkte i gatewayen gir færre deployer, men kobler kartets kode og avhengigheter til alle eksisterende Labs-ruter. En database med administrasjonsgrensesnitt gir bedre samtidig redigering, men krever autentisering og mer drift enn første dataversjon trenger. Slike løsninger kan vurderes når datamengde og oppdateringsbehov er kjent.

## Brukeropplevelse

Foreslått URL: `/labs/datasenter-analyse-norge`. Labs-forsiden lenker inn til løsningen. Endelig apex/www-adresse følger det eksisterende domenets verifiserte oppsett.

Startsiden viser et norgeskart, prosjektliste og tydelig dataversjon. Oversikten oppgir antall undersøkte prosjekter, antall med dokumenterte kartpunkter og antall med kontrollerte arealgrenser. Den viser ikke udokumenterte nasjonale totalsummer.

Brukeren kan filtrere på kommune, prosjektfase og dokumentasjonsnivå. Prosjektpanel åpnes fra kart eller liste og inneholder areal, kraft, natur, økonomi, eierskap, kildehistorikk og kunnskapshull. Filtre og valgt prosjekt kan deles med URL. Kartets signatur forklarer forskjellen mellom adressepunkt og anleggsgrense.

Kilder og usikkerhet vises ved den enkelte opplysningen. Et tall merket «annonsert» kan ikke forveksles med observert drift. «Ukjent» vises eksplisitt og forsvinner ikke gjennom filtrering eller summering. Et anlegg uten geometri beholdes i listen med forklaring. Adressepunkter får egen signatur og merkes «adressepunkt – ikke arealavgrensning».

Egen visning for «Påstandskontroll» viser hvem som fremsatte påstanden, hvor og når, nøyaktig avgrensning, dokumentasjon for og imot, og konklusjonens begrensninger. Rapportens publikasjonsstatus er et eget felt. Medieomtale kan vises som omtale selv når underliggende rapport mangler, men ikke brukes som bekreftet måling.

Tilgjengelig tabell gir samme faktainnhold som kartet. Mobilvisning veksler mellom kart og liste. Tastaturfokus, lesbar kontrast og tekstlige statusetiketter er påkrevd. Kartet skal ikke være eneste måte å finne data på.

Hvert prosjekt får et eget naturkort med fire deler: naturverdier før inngrep, planlagt/observert arealendring, vurderte konsekvenser og kunnskapshull. KU-status oppgis per komponent. Kartlag viser naturtyper, vern, artsgrunnlag og kartleggingsdekning når datatilgang og kvalitet tillater det. Treff med ukjent dekning får ingen grønn lavrisikoindikator. Naturpoengsum inngår ikke. Daterte før-/etterbilder og inngrepsgeometri kobles inn først når disse faktisk er innhentet og kontrollert.

## Data og kvalitetsgrenser

Datakontrakten er beskrevet i `docs/datametode.md`. Kildepost, faktapåstand, geometri, prosjekt og kontrollresultat er separate enheter. Research-filene beholdes som innsamling; publiserte filer normaliseres og versjoneres separat.

Statistiske konfidensintervaller krever statistisk grunnlag. Ellers brukes dokumenterte spenn eller begrunnet kvalitativ konfidens. Opplysninger med uforenlige definisjoner beholdes som konflikt. Prosjektdekning og feltdekning er separate mål.

Første utvalg skal ikke automatisk løftes til publiseringsstatus. Presise publiseringsporter i metodefilen avgjør hva som er godkjent, hva som bare kan vises som partsopplysning, og hva som fortsatt er et kunnskapshull. Ubekreftede søkespor inngår ikke i summer eller rangeringer.

## Arkitektur

- Next.js og TypeScript i dette arbeidsområdet; støttet versjon låses ved implementering.
- Statiske, versjonerte data fra en kontrollert normaliserings-/valideringsprosess.
- MapLibre GL JS med valgt og kontrollert basiskartleverandør, tydelig attribusjon og dokumenterte bruksvilkår. Leverandørvalg gjennomføres før produksjon; ingen betalt avtale forutsettes.
- Semantiske kartlag for punkter, planavgrensning og dokumentert inngrep; tomme lag forklares og tegnes ikke som fiktive objekter.
- Dataversjon og kildehenvisninger følger nedlastingene.
- Ingen innlogging, database eller automatiske kildescrapere i første versjon.

## Feilhåndtering

Hvis kart eller fliser feiler, beholdes liste, filtre og kildepanel og brukeren får en konkret melding. Utilgjengelige originalkilder beholder historisk URL og sist verifisert dato, med tilgangsstatus. Ugyldige poster stoppes av valideringen før deploy; de erstattes ikke med standardverdier. Null er ukjent, mens tallet 0 krever egen dokumentasjon.

## Vercel og eksisterende Labs

Utviklingsagentens funn og tekniske detaljer står i `docs/utvikling.md`. Eksisterende gateway er prosjektet `mpa_insights`. Den lokale gateway-kopien er eldre enn sist identifiserte produksjonsdeploy. Integrasjon må derfor gjøres mot oppdatert kilde med alle eksisterende ruter bevart.

Appen får basePath `/labs/datasenter-analyse-norge`. Etter verifisert app-deploy får gatewayen to avgrensede rewrites for grunnsti og understier, til appens faktisk opprettede stabile alias. Deretter legges lenke til fra Labs. Ingen generell omskriving av hele `/labs` innføres.

Forhåndsvisning kontrolleres før produksjon; publisert URL og eksisterende Labs-ruter kontrolleres etterpå. Deploylogg skal inneholde commit, dataversjon, deploy-ID og tidspunkt. Offentlig UI og domenealiaser er ennå ikke verifisert, og Vercel-lesetilgang bekrefter ikke i seg selv rettigheter til deploy.

## Akseptansekriterier

1. Brukeren kan finne prosjekter via kart og liste og dele valgt prosjekt.
2. Alle publiserte faktaverdier har daterte kildeopplysninger, definisjon og usikkerhet.
3. Ukjent geometri gir ingen oppdiktet markør; adressepunkter er tydelig skilt fra anleggsgrenser.
4. Planareal og faktisk beslag, MW og årsenergi, og byggeårsverk og faste arbeidsplasser vises separat.
5. Kildemotsetninger og uverifiserte påstander er tydelige; Teknologirådets rapportstatus er sporbar.
6. Relevante datavalideringer, typekontroll, produksjonsbygg og nettlesertester passerer.
7. Kartfeil, tomme treff, mobil, tastatur og direkte lenker fungerer uten tap av kildeinformasjon.
8. Appen er verifisert på faktisk Labs-URL, og eksisterende Labs-ruter er regresjonstestet.
9. Naturkortene følger `docs/naturmetode.md` og det maskinlesbare pilotskjemaet. Brukeren kan skille KU-utsagn, karttreff og dokumentert naturtap, samt se hva som er undersøkt og hva som mangler.

## Neste gjennomføringsetappe

Fullfør uavhengig feltkontroll, dokumenter polygonhull og normaliser første datasnapshot. Implementer kart/liste/påstandskontroll, test og deploy via oppdatert gateway. Utvid deretter prosjektuniverset systematisk med egen søkedekningslogg. Det er ikke opprettet noen tilbakevendende bakgrunnsjobb.

Designet er skrevet som konkret gjennomgangsgrunnlag. Arbeidsområdet var tomt og er ikke et Git-repository; dokumentet er derfor ikke committet. Team- og forskningsarbeidet er utført, mens produktimplementering og deploy gjenstår.
