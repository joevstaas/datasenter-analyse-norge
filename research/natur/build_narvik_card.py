#!/usr/bin/env python3
"""Normalize the scoped Narvik pilot; never transfer old KU conclusions to new cooling."""
import json
from build_naturkort import OUT, SOURCES, add_source, base_card, finding, action


def main():
    data = json.loads((OUT / 'narvik.json').read_text())
    for s in data['sources']:
        add_source('narvik-' + s['id'], s['title'],
                   'Narvik kommune' if s['id'] in ('N1', 'N3', 'N4') else 'Norconsult; publisert av Narvik kommune',
                   s['url'], s['documentDate'],
                   published='2026-04-09' if s['id'] == 'N4' else None,
                   local=s['rawFile'], date_note=s['dateNote'], version=s['version'])
    c = base_card('narvik', 'Narvik – Skoglund og separat kjølevannsløsning',
                  ['2023003', '2026007'],
                  'Industriplanen Skoglund–Lallasletta og kjølevannsplanen Bjerkvik har forskjellig omfang og utredningshistorikk. Ingen inngrepspolygon er validert.', False)
    c['ku'] = [dict(component='Historisk industriprosjekt Skoglund–Lallasletta',
        status='found_fulltext', documentType='Natur-KU 2024, versjon 02',
        scopeNote='Hydrogen/ammoniakk og tilknyttet infrastruktur. Ikke KU for kjølevannsplan 2026007. Oppdatert fagrapport ikke innhentet.', sourceIds=['narvik-N6']),
        dict(component='Kjølevannsløsning Bjerkvik 2026007', status='planned_not_obtained',
        documentType='Utredningskrav i oppstartsreferat 2026',
        scopeNote='Kommunen angir utredning av natur på land, i ferskvann og sjø. Fullført KU ikke innhentet.', sourceIds=['narvik-N3'])]
    c['baseline'] = [finding('n-baseline',
        'Natur-KU fra 2024 beskriver blant annet flommarksskog og marine naturverdier i sitt historiske undersøkelsesområde. Dette dokumenterer ikke overlapp med den nye kjølevannstraseen.',
        ['narvik-N6'], 's. 51–58; prosjektbeskrivelse og kart må leses samlet', when='2024-02-19')]
    c['change'] = [finding('n-warning-area',
        'Planinitiativet oppgir omtrent 6200 dekar varslingsområde, inkludert alternativer og sjøareal. Området ventes innsnevret; tallet er ikke naturtap eller faktisk arealbeslag.',
        ['narvik-N2'], 's. 7', when='2026-08-31', confidence='high'),
        finding('n-change-gap', 'Faktisk samlet naturinngrep og datasenterets andel er ikke beregnet i piloten.',
        ['narvik-N5'], 's. 92–93; historisk grunnarbeid og nullalternativ', kind='knowledge_gap', confidence='unknown',
        reason='Mangler datert førtilstand, inngrepspolygon og fordeling mellom tiltak.')]
    c['consequence'] = [finding('n-cooling',
        'Planinitiativet oppgir at temperaturforskjellen mellom inntak og utslipp ennå ikke er avklart. Kommunens oppstartsreferat krever naturutredning; en dokumentert effektberegning for ny kjøling er ikke innhentet.',
        ['narvik-N2', 'narvik-N3'], 'planinitiativ s. 10; oppstartsreferat pkt. 2.3', when='2026-08-31'),
        finding('n-counterfactual',
        'Planbeskrivelsens naturvurdering bruker allerede tillatt industriutbygging som del av nullalternativet. En vurdert tilleggseffekt kan derfor ikke leses som samlet naturtap fra opprinnelig tilstand.',
        ['narvik-N5'], 's. 92–93', when='2025-10-17')]
    c['knowledge_gap'] = [finding('n-current-ku',
        'Oppdatert natur-KU og konsekvensutredning for den nye kjølevannsløsningen mangler i pilotgrunnlaget. Eldre rapporter gjelder andre prosjektutforminger.',
        ['narvik-N3', 'narvik-N6', 'narvik-N7'], 'oppstartsreferat pkt. 2.3; KU-rapportenes prosjektbeskrivelser', kind='knowledge_gap', confidence='unknown',
        reason='Historisk rapport kan ikke overføres til ny teknologi og trasé uten faglig kontroll.'),
        finding('n-water-status',
        'Vann-Nett-status gjengitt i planbeskrivelsen er historisk. Dagens vannforekomststatus og en uavhengig romlig kontroll av ny trasé er ikke innhentet.',
        ['narvik-N5'], 's. 44–45, tabell 4-2; datagrunnlag 12.12.2023', kind='knowledge_gap', confidence='unknown',
        reason='Historisk avskrift er ikke en oppdatert overvåkingsserie eller årsaksanalyse.')]
    c['nextActions'] = [action('naturutredninger', 'Innhent gjeldende fagrapporter for hver prosjektkomponent.',
        'Versjon, dato, feltkalender og dokumentert kobling til 2023003/2026007.'),
        action('natur-GIS', 'Avgrens faktisk inngrep og alternative kjølevannstraseer mot datert førtilstand.',
        'Kildebelagte polygoner, bekreftet CRS, ortofoto og relevante natur- og artslag.'),
        action('naturutredninger', 'Undersøk vannpåvirkning og samlet belastning.',
        'Gjeldende Vann-Nett, temperatur/vannmengde, utslippsmodell og dokumentert økologisk vurdering.')]
    (OUT / 'narvik-normalisert.json').write_text(json.dumps(dict(sources=list(SOURCES.values()), card=c), ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
