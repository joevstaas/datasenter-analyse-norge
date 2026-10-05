# To visuelle retninger – designutkast

Branch: `design/atlas-visual-directions`, opprettet fra `16662c6` på main.
Lokal sammenligning: http://localhost:5174/labs/datasenter-analyse-norge/design

Brukeren godkjente to sammenlignbare utkast før valg av endelig retning.
Utkastene gjenbruker AtlasView og ekte ODP-data. A/B-knapper endrer kun scoped
CSS; valgt prosjekt, filtre og kart beholdes. Ingen data er endret. Ingen globale
skills er installert. Hovedruten og produksjonsbranchen er uendret.

## A – rolig naturatlas

Varme papirtoner, botanisk grønn aksent, serifoverskrifter og tydeligere
lesehierarki. Passer formidling og utforskning. Mer lesbar kildetekst og
usikkerhet enn i utgangspunktet. Lite skygger og rolige kontroller.

## B – presist infrastrukturobservatorium

Blågrå nøytraler, smalere prosjektindeks og tydelig sans-serif-typografi.
Monospace til utvalgte metadata/tall; hovedtekst forblir lettlest sans-serif.
Mer kompakt oversikt og tydelige skillelinjer. Ingen terminaleffekter.

## Felles rammer

Kartlag, tegnforklaringer, geografiske markører og kildedata er uendret.
Usikkerhet, AI/demo-merking og kunnskapshull beholdes. Ingen oppdiktede tall eller
datoer. Eksisterende ikoner beholdes for å begrense endringsomfang og avhengigheter.
Designskissen gjelder kartgrensesnittet; quizlenken går til eksisterende quiz.
Quiz og delingskort kan få valgt uttrykk etter brukerens vurdering av retning.

Inspirert av følgende skills, lest 05.10.2026:
- https://github.com/Leonxlnx/taste-skill/blob/main/skills/redesign-skill/SKILL.md
- https://github.com/Leonxlnx/taste-skill/blob/main/skills/minimalist-skill/SKILL.md

Stilråd er tilpasset et faglig kartverktøy: ingen tilfeldige data/datoer,
markedsføringsbilder, scroll-effekter, nye ikonpakker eller faglig omfarging.

## Verifisering og tilbakeføring

TypeScript kontrollert. Nettleser: begge stiler har åtte prosjektpunkter og
prosjekter; stilbytte bevarer valgt prosjekt, naturmenyen åpnes, mobilkartet kan
vises og dokumentbredden holder seg innenfor skjermen. Ingen JavaScript-feil i
kontrollen. Mobiloversikten er komprimert for å bevare plass til prosjektlisten.

Hele utkastet ligger i `app/design/`. Det kan fjernes uten å endre AtlasView.
For å forlate forsøket lokalt: `git switch main` når arbeidsmappen er ren.
Ingen merge til main utføres før brukeren har valgt retning.

Produksjonsbygg (`npm run build`) bestod med den nye `/design`-ruten.
Skjermbilder: `naturatlas.png`, `observatorium.png` og `mobil.png` i samme mappe.

## Valgt kombinasjon

Brukeren foretrekker B med fargetonene fra A. B beholder oppsett, sans-serif,
kompakt prosjektindeks og talltypografi, men bruker nå As papirtoner og grønne
aksenter. Kombinasjonen er forhåndsvalgt på designsiden. Endringen er fortsatt
avgrenset til designbranchen; main og produksjon er ikke endret.
