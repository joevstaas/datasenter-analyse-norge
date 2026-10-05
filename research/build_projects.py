# HISTORICAL BASELINE GENERATOR: overwrites later research enrichment.
# Do not rerun against current research; coordinate correction and report enrichment must be preserved.
"""Rebuild the sourced research dataset. No inferred project locations or polygons."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
READ = '2026-10-01'
sources = {}
def source(id, title, url, publisher, type='operator', published=None, updated=None):
    sources[id] = dict(id=id,title=title,url=url,publisher=publisher,type=type,publishedAt=published,updatedAt=updated,accessedAt=READ)
    return id

source('gm-contact','Kontaktadresser for datasentre','https://greenmountain.no/contact-us/','Green Mountain')
source('gm-owner','Hvem eier Green Mountain?','https://info.greenmountain.no/faq/azrieli-group/','Green Mountain')
source('gm-2025','Sustainability report 2025','https://greenmountain.no/wp-content/uploads/Sustainability-Report-2025-1.pdf','Green Mountain',published='2026-05')
source('gm-three','Key facts – The three data centers','https://greenmountain.no/wp-content/uploads/Summary-Economic-Impact-Report-SVG-Rennesoy-TEL-Rjukan-OSL-Enebakk.pdf','Green Mountain / Menon',type='commissioned_analysis')
for id,name in [('hamar','OSL-Hamar'),('rennesoy','SVG-Rennesøy'),('rjukan','TEL-Rjukan'),('enebakk','OSL-Enebakk'),('undheim','SVG-Undheim')]:
    source('gm-'+id,name,'https://greenmountain.no/data-center/'+{'hamar':'osl-hamar','rennesoy':'svg-rennesoy','rjukan':'tel-rjukan','enebakk':'osl-enebakk','undheim':'svg-undheim'}[id]+'/','Green Mountain')
source('hamar-plan','Heggvin: planreferanser og prosjekt','https://www.hamar.kommune.no/utviklingsomrader/heggvin','Hamar kommune','municipality','2023-12-15')
source('rennesoy-economy','Sammendrag av ringvirkninger Rennesøy (tittel i PDF feilaktig Rjukan)','https://greenmountain.no/wp-content/uploads/MENON-Economic-Impact-Report-Green-Mountain-SVG-Rennesoy-Summary_01.11.2024.pdf','Menon / Green Mountain','commissioned_analysis','2024-11-01')
source('skien-timeline','Tidslinje for Google-etablering','https://www.skien.kommune.no/by-og-naeringsutvikling/google-etablering-i-skien-kommune/tidslinje-hva-har-skjedd-fram-til-naa/','Skien kommune','municipality','2024-02-19','2025-09-18')
source('google-release','Google starter bygging i Skien','https://kommunikasjon.ntb.no/pressemelding/18046820/google-starter-bygging-av-et-nytt-datasenter-i-skien-investerer-600-millioner-euro?lang=no&publisherId=8930805','Google Norge (NTB distribusjon)','operator','2024-02-07')
source('gromstul-nve','Gromstul (Kise) koblingsstasjon med 132 kV nettilknytning','https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak/?id=4885&type=A-1','NVE','authority')
source('gromstul-plan','Bystyret sak 75/18: Gromstul sluttbehandling','https://opengov.360online.com/Meetings/skien/Meetings/Details/819161?agendaItemId=222580','Skien kommune','municipality','2018-05-31')
source('gromstul-deponi','Detaljregulering Fjellimellomdalen','https://www.skien.kommune.no/politikk/kunngjoeringer/detaljregulering-for-gbnr-111-fjellimellomdalen/','Skien kommune','municipality')
source('n01-site','N01 Data Center Campus','https://bulkinfrastructure.com/data-centers/locations/n01','Bulk Infrastructure')
source('n01-invest','BGO investering og N01-utbygging','https://bgo.com/press-release/bulk-infrastructure-announces-350msup1/sup-equity-investment-by-bgo-and-plans-for-over-1bn-of-investments-by-2026-to-grow-sustainable-data-centre-l-1717514270601','BGO / Bulk','operator','2024-06-05')
source('bulk-owner','Investor relations: eierfordeling desember 2025','https://bulkinfrastructure.com/about-us/investor-relations','Bulk Infrastructure')
source('bulk-q4','Fourth Quarter 2025 Results','https://bulkinfrastructure.com/uploads/Financial-report/Bulk-Infrastructure-Group-Financial-statements-Q4-2025.pdf','Bulk Infrastructure',published='2026-02-05')
source('bulk-address','ISO-sertifikat med stedsliste (utløpt; kun adressebelegg)','https://bulkinfrastructure.com/uploads/ISO-cert-14001.PDF','LRQA / Bulk','certification','2022-10-03')
source('n01-va','Utbyggingsavtale Stølen datalagringspark','https://www.vennesla.kommune.no/kunngjoringer-og-planer-pa-horing/utbyggingsavtale-stolen-datalagrinspark.9114.aspx','Vennesla kommune','municipality','2026-03-13','2026-03-13')
source('lefdal-site','Lefdal Mine Data Centers','https://www.lefdalmine.com/','Lefdal Mine Data Centers')
source('lefdal-power','Utvidelse av tilgjengelig effekt med 60 MW','https://www.lefdalmine.com/news/lefdal-mine-datacenter-expand-power-capacity-with-60-mw','Lefdal Mine Data Centers')
source('lefdal-owner','Ownership','https://www.lefdalmine.com/about/ownership','Lefdal Mine Data Centers')
source('lefdal-register','Lefdal Mine Datacenter AS – registeradresse','https://virksomhet.brreg.no/nn/oppslag/enheter/911599252','Brønnøysundregistrene','authority')

def claim(field,value,unit,kind,period,sourceIds,confidence='middels',reason='Partsopplysning; ikke uavhengig bekreftet.'):
    return dict(field=field,value=value,unit=unit,kind=kind,period=period,sourceIds=sourceIds,confidence=confidence,reason=reason,uncertaintyType='documented_confidence_level',confidenceInterval=None)
def coords(address,municipality,sourceIds):
    raw=json.loads((ROOT/'raw'/f'{address.replace(" ","-")}.json').read_text())
    a=next(x for x in raw['response']['adresser'] if x['adressetekst']==address and x['kommunenavn']==municipality.upper())
    sid='kartverket-'+address.replace(' ','-').lower()
    source(sid,'Kartverket adressepunkt: '+address,raw['source_url'],'Kartverket','authority',updated=a['oppdateringsdato'])
    return dict(lat=a['representasjonspunkt']['lat'],lon=a['representasjonspunkt']['lon'],crs='EPSG:4258',kind='address_point',address=address,sourceIds=sourceIds+[sid],confidence='middels',method='Eksakt adresse og kommune matchet i Kartverkets adresse-API. Adresse knyttet til anlegget via oppgitt kilde.',reason='Dokumentert adressepunkt; stedfestingverifisert=false i registeret. Punktet er ikke eiendomsgrense eller anleggets sentrum. EPSG:4258 er bevart; ingen statistisk presisjon er oppgitt.',rawFile='research/raw/'+address.replace(' ','-')+'.json')
def project(id,name,municipality,status,point=None):
    return dict(id=id,name=name,municipality=municipality,status=status,coordinates=point,geometry=dict(type=None,coordinates=None,sourceIds=[],planReferences=[],status='Kunnskapshull: ingen validert digital avgrensning'),claims=[],gaps=['Faktisk årlig kraftbruk (målt TWh og år) mangler.','Faktisk nedbygd areal med måledato og metode mangler.','Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler.','Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede.'])

projects=[]
for id,name,municipality,address,status in [
 ('hamar','Green Mountain OSL-Hamar / Heggvin','Hamar','Stabekkvegen 140','I drift; videre utvidelse planlagt'),
 ('rennesoy','Green Mountain SVG-Rennesøy','Stavanger','Hodneveien 260','I drift'),
 ('rjukan','Green Mountain TEL-Rjukan','Tinn','Svaddevegen 161','I drift'),
 ('enebakk','Green Mountain OSL-Enebakk','Enebakk','Granittveien 110','I drift'),
 ('undheim','Green Mountain SVG-Undheim','Time',None,'Under bygging ifølge operatør; planlagt ferdigstillelse 2028')]:
    p=project(id,name,municipality,status,coords(address,municipality,['gm-contact']) if address else None)
    p['claims']=[claim('status',status,None,'reported_status','2025' if id!='undheim' else None,['gm-2025'] if id!='undheim' else ['gm-undheim']),claim('ownership','Green Mountain; Azrieli Group oppgis som konserneier',None,'reported_group_owner','2021 acquisition; current webpage undated',['gm-owner']),claim('municipality',municipality,None,'location',None,['gm-'+id])]
    projects.append(p)
byid={p['id']:p for p in projects}
byid['hamar']['claims'] += [claim('power',90,'MW','contracted_IT_capacity',None,['gm-hamar']),claim('power',150,'MW','planned_maximum_IT_capacity',None,['gm-hamar']),claim('area',280000,'m2','potential_campus_area',None,['gm-hamar'],reason='Operatørens potensielle campusareal; ikke målt nedbygd natur.'),claim('jobs',200,'persons','more_than_current_workplace_count',None,['gm-hamar'],reason='Operatør oppgir mer enn 200; ikke antall direkte ansatte eller årsverk.'),claim('value_creation',6100000000,'NOK','modelled_construction_gross_value_added','construction of first three buildings',['gm-hamar'],'lav','Sammendrag av ringvirkningsanalyse; modell og motfaktisk alternativ ikke gjennomgått. Ikke årlig netto samfunnsøkonomisk gevinst.'),claim('nature','Tilrettelagt for varmegjenvinning; faktisk utnyttet varme ikke dokumentert her.',None,'operator_design_claim',None,['gm-hamar'])]
byid['hamar']['geometry']['planReferences']=[dict(planId='079500',effectiveDate='2022-04-27',amendedDate='2023-05-10',sourceIds=['hamar-plan']),dict(planId='165',description='Kryss og veg; ikke datasentertomt',effectiveDate='2023-05-10',sourceIds=['hamar-plan'])]
byid['rennesoy']['claims'] += [claim('power',25,'MW','maximum_IT_capacity',None,['gm-rennesoy']),claim('area',144700,'m2','reported_site_area',None,['gm-three']),claim('area',23000,'m2','reported_available_mountain_hall_space',None,['gm-rennesoy'],reason='Kilden kaller dette både campus footprint og tilgjengelig areal i fjellhaller. Ikke tolket som nedbygd overflate.'),claim('jobs',80,'persons','regular_workplace_count','2024',['rennesoy-economy']),claim('value_creation',2300000000,'NOK','modelled_cumulative_gross_value_added','2011–2024',['rennesoy-economy'],'lav','Kumulativ ringvirkningsmodell inkludert investering/drift; 2024 delvis budsjett. Ikke årlig verdi.'),claim('nature','Gjenbruk av tidligere NATO-fjellhaller; fjordkjøling.',None,'reported_site_characteristics',None,['gm-rennesoy'])]
byid['rjukan']['claims'] += [claim('power',40,'MW','design_capacity','2025',['gm-2025']),claim('power',50,'MW','potential_maximum_IT_capacity',None,['gm-rjukan'],reason='Operatørens nyere udaterte nettside; kan ikke likestilles med 40 MW designkapasitet for 2025.'),claim('area',29000,'m2','reported_campus_area',None,['gm-rjukan']),claim('nature','Luftkjøling; klargjort for varmegjenvinning.',None,'operator_design_claim',None,['gm-rjukan'])]
byid['rjukan']['gaps'].append('40 MW design i rapport for 2025 og 50 MW potensial på nettside må avstemmes; dette er ikke et statistisk intervall.')
byid['enebakk']['claims'] += [claim('power',75,'MW','headline_total_IT_capacity',None,['gm-enebakk'],'lav','Samme side oppgir også 93 MW maksimum og 94 MW line-of-sight; definisjonene er ikke avstemt.'),claim('power',93,'MW','maximum_capacity',None,['gm-enebakk']),claim('power',94,'MW','line_of_sight_capacity',None,['gm-enebakk'],'lav','Operatørens eget begrep; ingen realiseringsgaranti.'),claim('area',72200,'m2','reported_acquired_site_area',None,['gm-enebakk']),claim('area',81205,'m2','reported_site_area_in_economic_summary',None,['gm-three'],'lav','Avviker fra 72 200 m2 nettside. Ulik avgrensning eller tidspunkt ikke avklart.'),claim('jobs',98,'persons','regular_workplace_count',None,['gm-three']),claim('nature','Klargjort for varmegjenvinning; faktisk leveranse ikke dokumentert her.',None,'operator_design_claim',None,['gm-enebakk'])]
byid['enebakk']['gaps'].append('Effektdefinisjoner 75/93/94 MW og arealavvik 72 200/81 205 m2 trenger avklaring; ikke slå sammen til konfidensintervaller.')
byid['undheim']['claims'] += [claim('power',80,'MW','planned_IT_capacity','full completion planned 2028',['gm-undheim']),claim('power',100,'MW','planned_site_capacity','full completion planned 2028',['gm-undheim']),claim('area',76000,'m2','reported_campus_area',None,['gm-undheim']),claim('jobs',100,'persons','approximately_forecast_regular_workplace_count','future operations',['gm-undheim'],'lav','Operatørprognose, ikke observerte arbeidsplasser.'),claim('nature','Design for luft- og væskekjøling samt mottakere av overskuddsvarme.',None,'operator_design_claim','planned',['gm-undheim'])]

p=project('gromstul','Google / WS Computing – Gromstul','Skien','Byggestart dokumentert 2024; søknad byggetrinn 2 i august 2025. Drift ikke bekreftet.')
p['claims']=[claim('status',p['status'],None,'documented_historical_status','2024–2025',['skien-timeline'],'høy','Kommunal prosjektkronologi; dagens driftsstatus er ikke avklart.'),claim('municipality','Skien',None,'location',None,['skien-timeline'],'høy','Kommunal prosjektkilde.'),claim('ownership','Tomtekjøper WS Computing AS, Google-selskap; Google er del av Alphabet.',None,'reported_group_owner','2019 acquisition / 2024 statement',['skien-timeline','google-release']),claim('area',2000000,'m2','approximately_purchased_plot_area','2019',['skien-timeline'],'høy','Nær 2000 mål tomt; ikke faktisk nedbygd areal.'),claim('area',3000000,'m2','approximately_regulated_total_area','2018',['skien-timeline'],'høy','Nær 3000 mål reguleringsområde; videre avgrensning ikke hentet.'),claim('power',240,'MW','allocated_capacity_operator_statement','2024-02-07 first phase',['google-release']),claim('power',50,'MW','historical_permitted_connection','2020-11-23',['gromstul-nve'],'høy','NVE beskriver denne nettkonsesjonsendringen; ikke påstand om dagens samlede anleggskapasitet.'),claim('value_creation',6700000000,'NOK','forecast_construction_gross_value_added','2024–2025',['google-release'],'lav','Deloitte-modell bestilt av Google, sitert i pressemelding. Ikke realisert eller netto verdi.'),claim('nature','Planlagt massedeponi fra byggetrinn 1: ca. 500 000 m3. Varslingsområde omfatter skog, bekker og grøftet myr; konsekvensutredning kreves.',None,'municipal_planning_notice','2026 planning notice',['gromstul-deponi'],'høy','Dokumentert utredningsbehov og tiltak, ikke ferdig vurdering av faktisk naturtap.')]
p['geometry']['planReferences']=[dict(description='Gromstul gbnr 11/1, bystyresak 75/18',effectiveDate='2018-05-31',url=sources['gromstul-plan']['url'],sourceIds=['gromstul-plan']),dict(planId='2026008',description='Fjellimellomdalen massedeponi: tilknyttet tiltak, ikke datasentertomt',sourceIds=['gromstul-deponi'])]
p['gaps'] += ['240 MW fra operatør er ikke kontrollert mot gjeldende nettilknytningsavtale.','2026 var en forventet driftsstart i 2024; faktisk oppstart må verifiseres.']
projects.append(p)
p=project('n01','Bulk N01 Campus – Støleheia','Vennesla','Drift og utbygging dokumentert i rapport for Q4 2025',coords('Stølevegen 39','Vennesla',['bulk-address']))
p['claims']=[claim('municipality','Vennesla',None,'location',None,['n01-va'],'høy','Kommunens utbyggingsavtale.'),claim('status',p['status'],None,'reported_status','Q4 2025',['bulk-q4']),claim('power',1000,'MW','marketed_potential_site_capacity',None,['n01-site'],'lav','Markedsført skaleringspotensial; ikke forbruk eller bekreftet nettilknytning. Side ble kun tilgjengelig som søkeuttrekk.'),claim('power',400,'MW','announced_target_power_capacity','target 2026 announced 2024',['n01-invest'],'lav','Historisk mål, ikke bekreftet levert kapasitet i 2026.'),claim('area',3000000,'m2','marketed_campus_area',None,['n01-site'],'lav','3 km2 markedsført campus; kun søkeuttrekk tilgjengelig, ingen avgrensningskontroll.'),claim('ownership',{'Bulk Industrier AS':35.8,'BGO Europe IV':30.8,'BGO King HoldCo':15.2,'Geveran Trading Co. Ltd.':7.8,'others':10.5},'%','reported_group_shareholding','2025-12',['bulk-owner'],reason='Selskapets eieroversikt, avrundet; sum 100,1 %. Ikke matrikkelens tomteeier.'),claim('nature','Kommunal utbyggingsavtale for VA-anlegg lagt ut på høring.',None,'planning_process','2026-03-10 decision',['n01-va'],'høy','Sier ikke hvor stort naturtap tiltaket medfører.')]
p['gaps'] += ['1 GW markedsføring, 400 MW 2026-mål og 2 GW ambisjon fra 2024 gjelder ulike stadier; trenger oppdatert avstemming.','Prosjektspesifikke driftsjobber og verdiskaping mangler. Konsernets 125 FTE i Q4 2025 er ikke fordelt på N01.']
projects.append(p)
p=project('lefdal','Lefdal Mine Data Centers','Stad','Operativt anlegg ifølge operatør',coords('Nordfjordvegen 7300','Stad',['lefdal-register']))
p['claims']=[claim('municipality','Stad',None,'registered_location',None,['lefdal-register'],'høy','Brønnøysundregistrenes forretningsadresse.'),claim('status',p['status'],None,'reported_status',None,['lefdal-power']),claim('power',80,'MW','available_power_capacity',None,['lefdal-power']),claim('power',20,'MW','reserved_for_current_customers',None,['lefdal-power']),claim('power',200,'MW','potential_facility_capacity',None,['lefdal-site']),claim('area',120000,'m2','potential_underground_whitespace',None,['lefdal-site'],reason='Potensielt IT-gulvareal i gruve; ikke tomt eller overflateinngrep.'),claim('ownership',{'Columbia Threadneedle European Sustainable Infrastructure Fund':66.67,'other_named_main_shareholder':'Professor Friedhelm Loh'},None,'reported_shareholders',None,['lefdal-owner']),claim('nature','Gjenbruk av underjordisk gruve og fjordbasert kjøling.',None,'operator_site_characteristics',None,['lefdal-site'])]
p['coordinates']['reason'] += ' Registeradresse er forretningsadresse; fysisk anleggsplassering krever egen plankontroll.'
p['gaps'] += ['Prosjektspesifikke driftsjobber og verdiskaping ikke dokumentert.','Udatert effektmelding gir ingen sikker observasjonsdato for 80 MW.']
projects.append(p)

source('lefdal-3i-close','3i Infrastructure completes investment in Lefdal','https://www.3i-infrastructure.com/newsroom/press-releases/2026/3i-infrastructure-plc-completes-investment-in-the-lefdal-mine-datacenter-campus/','3i Infrastructure','investor','2026-09-03')
source('lefdal-3i-agreement','3i Infrastructure invests in Lefdal','https://www.3i-infrastructure.com/newsroom/press-releases/2026/3i-infrastructure-plc-invests-in-lefdal-mine-datacenter/','3i Infrastructure','investor','2026-03-11')
lefdal=next(p for p in projects if p['id']=='lefdal')
for c in lefdal['claims']:
    if c['field']=='ownership':
        c.update(kind='superseded_ownership_webpage',confidence='lav',publishAsFact=False,reason='Utdatert operatørside: motsies av datert 3i-sluttføringsmelding 03.09.2026.',supersededBySourceIds=['lefdal-3i-close'])
lefdal['claims'] += [claim('ownership','3i forvalter 90 %: 3i Infrastructure litt over 45 %, medinvestorer ca. 45 %. Gjenværende minoritet 10 %.','%','completed_transaction_reported_shareholding','2026-09-02',['lefdal-3i-close'],'høy','Datert investors sluttføringsmelding. Første kjøp 28.08.2026, tillegg 02.09.2026. Ikke uavhengig aksjeeierbok.'),claim('power',37,'MW','reported_operational_capacity','2026-03-11',['lefdal-3i-agreement']),claim('power',43,'MW','contracted_capacity_under_construction','2026-03-11',['lefdal-3i-agreement'])]
lefdal['gaps'].append('80 MW tilgjengelig nettkapasitet på udatert operatørside må holdes adskilt fra 37 MW drift / 43 MW under bygging oppgitt 11.03.2026.')
source('hamar-menon-full','Economic impact analysis OSL-Hamar construction, Menon 96/2025','https://greenmountain.no/wp-content/uploads/Report-Economic-Impact-Analysis-of-OSL-Hamar-Construction-english.pdf','Menon / Green Mountain','commissioned_analysis','2025-08')
for c in byid['hamar']['claims']:
    if c['field']=='value_creation':
        c.update(sourceIds=['hamar-menon-full'],period='Byggefase første tre bygg, inkludert forventede 2025–2026-utgifter',reason='5,7 mrd beregnet fra gjennomførte investeringer + 0,4 mrd prognose. Ekskluderer TikToks egne investeringer. Ikke realisert netto eller årlig gevinst.',sourceLocators={'hamar-menon-full':'side 5'})
for c in [claim('power',110,'MW','reported_total_power_capacity','rapport august 2025',['hamar-menon-full']),claim('area',139000,'m2','reported_site_size_first_three_buildings','rapport august 2025',['hamar-menon-full'],reason='Rapportens tomtestørrelse for eksisterende utbygging, ikke faktisk naturtap. Må avstemmes mot 280 000 m2 potensielt campus på nettsiden.'),claim('jobs',220,'persons','reported_regular_workplace_count','rapport august 2025',['hamar-menon-full'])]:
    c['sourceLocators']={'hamar-menon-full':'side 8, faktaboks'}
    byid['hamar']['claims'].append(c)

features=[]
for project_id,customer,planid in [('hamar','hamar3403','079500'),('gromstul','skien4003','2017004')]:
    p=next(p for p in projects if p['id']==project_id)
    raw=json.loads((ROOT/'raw'/f'{customer}-{planid}-geometry.json').read_text())
    plan=json.loads((ROOT/'raw'/f'{customer}-{planid}-metadata.json').read_text())
    sourceid='plan-'+project_id
    source(sourceid,plan['planNavn'],f'https://arealplaner.no/{customer}/arealplaner/{plan["id"]}','Kommunalt planregister / Norkart','municipal_plan_register',updated=plan['sistBehandlet'])
    sources[sourceid].update(metadataUrl=f'https://api.arealplaner.no/api/kunder/{customer}/arealplaner/{plan["id"]}',dataUrl=raw['url'],effectiveDate=plan['iKraft'],rawMetadata=f'research/raw/{customer}-{planid}-metadata.json',rawGeometry=f'research/raw/{customer}-{planid}-geometry.json')
    polygons=[]
    for area in raw['response']['omraader']:
        rings=[[[v['x'],v['y']] for v in area['exterior']['positions']]]
        rings += [[[v['x'],v['y']] for v in inner['positions']] for inner in area.get('interiors') or []]
        assert all(len(r)>=4 and r[0]==r[-1] for r in rings), 'Invalid or unclosed ring'
        polygons.append(rings)
    geo={'type':'Polygon','coordinates':polygons[0]} if len(polygons)==1 else {'type':'MultiPolygon','coordinates':polygons}
    p['geometry'].update(**geo,sourceIds=[sourceid],kind='regulatory_plan_extent',planId=planid,effectiveDate=plan['iKraft'],lastProcessedAt=plan['sistBehandlet'],confidence='middels',status='Hentet kommunalt planomriss; ringlukking kontrollert. Ikke full planjuridisk eller landmålingsmessig validering.',crs='Geografisk lon/lat som publisert for kartvisning; tolket som GeoJSON/WGS84 etter registerets frontend, EPSG ikke oppgitt i API-responsen.',method='Eksakt plan-ID hentet via offentlig planomriss-endepunkt. x/y overført uendret til GeoJSON [lon,lat], samme metode som registerets frontend. Ingen håndtegning, simplifisering eller arealberegning.',limitation='Hele planområdet; kan omfatte vei, grøntareal og flere virksomheter. Ikke datasenterets fotavtrykk eller faktisk nedbygd natur.',dataUrl=raw['url'])
    p['gaps']=[g for g in p['gaps'] if not g.startswith('Validert planpolygon')]
    p['gaps'].append('Planomriss hentet; gjeldende revisjon, formålsflater, eiendomsavgrensning og faktisk nedbygging må fortsatt kvalitetssikres.')
    p['claims'].append(claim('plan_extent',plan['planNavn'],None,'regulatory_plan_area_not_actual_land_take',plan['iKraft'],[sourceid],'middels','Reell digital plangrense fra kommunalt register. Polygon er ikke arealbeslag.'))
    features.append(dict(type='Feature',id=project_id,geometry=geo,properties=dict(projectId=project_id,planId=planid,name=plan['planNavn'],sourceId=sourceid,kind='regulatory_plan_extent',effectiveDate=plan['iKraft'],accessedAt=READ,confidence='middels',sourceCrs=p['geometry']['crs'],qaStatus='Ringer lukket og topologisk gyldige; uavhengig landmåling, CRS-bekreftelse og faglig planvalidering gjenstår.',lastProcessedAt=plan['sistBehandlet'],sourceUrl=raw['url'],metadataUrl=sources[sourceid]['metadataUrl'],method=p['geometry']['method'],warning=p['geometry']['limitation'])))
(ROOT/'planomriss.geojson').write_text(json.dumps(dict(type='FeatureCollection',features=features),ensure_ascii=False,indent=2)+'\n')

for p in projects:
    p['statusType']='reported_or_historical; see status claim period and source'
    p['statusVerifiedAsCurrent']=False
    for c in p['claims']:
        c.setdefault('publishAsFact',True)
        c.setdefault('sourceLocators',{})
        if c['field']=='status':
            c['sourceLocators']={sid: 'Prosjektbeskrivelse / status; se oppgitt periode' for sid in c['sourceIds']}
        if 'n01-site' in c['sourceIds']:
            c.update(publishAsFact=False,access='search_excerpt_only')
sources['n01-site']['access']='search_excerpt_only'
sources['n01-site']['publishAsFact']=False
meta=dict(version='0.2.0',accessedAt=READ,coverage='Første kildebelagte utvalg på åtte prosjekter; ikke uttømmende eller representativt.',status='Research baseline; ikke komplett kartlegging. Prosjektstatus er rapportert/historisk, ikke verifisert driftsstatus på lesedato.',coordinatePolicy='Kun kildebelagte adressepunkter. Null når dokumentasjon mangler. To reelle planomriss hentet fra kommunalt register; ingen konstruerte polygoner.',uncertaintyPolicy='Ingen statistiske konfidensintervaller: datagrunnlaget er dokumentopplysninger og prognoser, ikke en estimert utvalgsfordeling. Konfidensnivå gjelder belegg og avgrensning, ikke sannsynlighet.',datesPolicy='Publisert/oppdatert dato er null dersom siden ikke oppgir dette. Lest dato er ikke observasjonsdato. Udaterte nettpåstander har period=null.',areaPolicy='Tomt, planareal, campus, IT-gulvareal og faktisk arealbeslag er ulike størrelser. Ingen samlet arealsum beregnes.',energyPolicy='MW er effekt/kapasitet. Målt TWh mangler for alle utvalgte anlegg. Ingen årsenergi beregnes fra kapasitet.',sourcePolicy='Operatør- og bestilte analyseopplysninger er eksplisitte partsopplysninger. Søkeuttrekk er flagget publishAsFact=false. publishAsFact=true betyr at dokumentert påstand kan presenteres med kildetype, konfidens og forbehold; det er ikke uavhengig QA-godkjenning eller bekreftelse av partsopplysningens riktighet.')
(ROOT/'prosjekter.json').write_text(json.dumps(dict(meta=meta,sources=list(sources.values()),projects=projects),ensure_ascii=False,indent=2)+'\n')

lines=['# Norske datasenterprosjekter – første kildebelagte utvalg','',f'Lest {READ}. Åtte prosjekter; ikke uttømmende og ikke et statistisk representativt utvalg. Maskinlesbare påstander og kilde-ID-er ligger i `prosjekter.json`.','', '## Metode og begrensninger','','Hver påstand har kilde, observasjonsperiode (eller null), type og dokumentert konfidensnivå. Publiseringsdato og lesedato er separate. Ingen konfidensintervaller konstrueres uten statistisk modell. Null betyr ukjent, aldri null fysisk påvirkning.','', 'Seks punkter er hentet fra Kartverkets adresse-API. Råsvar ligger i `raw/`. EPSG:4258 er bevart. Alle svar har `stedfestingverifisert=false`; punktene kan brukes som dokumenterte adresser med middels konfidens, ikke som arealgrenser. Enebakk-søket gir også en annen kommune: kun eksakt adresse i Enebakk er brukt. Lefdals registeradresse må kontrolleres mot anleggsplan.','', 'To ekte planomriss (Heggvin og Gromstul) er hentet fra kommunalt register og lagret i planomriss.geojson. De viser hele reguleringsområdet, ikke faktisk arealbeslag eller bare datasenteret. Ringlukking og topologi er kontrollert; CRS er tolket fra registerets frontend, men ikke oppgitt i API-responsen. Ingen målt årlig TWh eller faktisk nedbygd areal er dokumentert her.','']
for p in projects:
    lines += ['## '+p['name'],'',p['municipality']+' — '+p['status']+'.','']
    if p['coordinates']:
        c=p['coordinates']; lines += [f"Adressepunkt: {c['address']}; lat {c['lat']}, lon {c['lon']} (EPSG:4258). Kilder: "+', '.join(c['sourceIds'])+'.','']
    else: lines += ['Koordinater: ukjent.','']
    for c in p['claims']:
        value=json.dumps(c['value'],ensure_ascii=False) if isinstance(c['value'],dict) else str(c['value'])
        lines += [f"- **{c['field']} / {c['kind']}:** {value} {c['unit'] or ''}. Periode: {c['period'] or 'ikke oppgitt'}. Konfidens: {c['confidence']}. {c['reason']} Kilder: {', '.join(c['sourceIds'])}."]
    lines += ['', 'Kunnskapshull: '+' '.join(p['gaps']),'']
lines += ['## Kilderegister','']
for s in sources.values():
    lines += [f"- `{s['id']}` — [{s['title']}]({s['url']}). {s['publisher']}; {s['type']}. Publisert: {s['publishedAt'] or 'ikke oppgitt'}. Oppdatert: {s['updatedAt'] or 'ikke oppgitt'}. Lest: {READ}."]
lines += ['','## Søkelogg og videre kontroll','', '- 2026-10-01: Operatørsøk Green Mountain, Bulk N01, Lefdal og Skygard. Skygard ble ikke inkludert i første åtte; søk avdekket forskjellige eierlister og udokumenterte MW-tall hos kataloger.','- 2026-10-01: Kommunesøk Skien/Gromstul, Hamar/Heggvin, Vennesla/Støleheia. Heggvin 079500 og Gromstul 2017004 identifisert. Kommunale metadata og digitale planomriss hentet via Arealplaner offentlig API; råsvar og GeoJSON lagret.','- 2026-10-01: NVE konsesjon 4885 gjennomgått. Historisk 50 MW tillatelse kan ikke overstyre senere opplysninger om 240 MW tildeling uten kontroll av endringshistorikk.','- 2026-10-01: Kartverkets adresse-API hentet for seks eksakte adresser; råsvar lagret. Operatøradresse som geokodingsinput for fire GM-anlegg; LRQA-stedsliste for N01; Brønnøysundregister for Lefdal.','- 2026-10-01: Statsforvalterens søketreff om Heggvin viste naturkartleggingsvedlegg, men åpning videresendte til portal. Ikke brukt som verifisert naturkonklusjon.','- 2026-10-01: Bulk N01-nettsiden feilet ved fulltekstinnhenting. Kun markedsførte 3 km2/1 GW fra søkeuttrekk beholdt med lav konfidens og eksplisitt flagg.','- Videre: hent gjeldende plandata fra kommunal plandatabase (SOSI/GML/GeoJSON), dokumenter plan-ID/revisjon/CRS, og beregn areal i projisert CRS. Sammenhold historiske ortofoto/byggetrinn med vedtatt plan.','- Videre: innhent årsvis målt kraft, godkjent tilknytning, IT-last, kjøling, faktisk varmeleveranse, utslippsvilkår, naturtypekartlegging og observerte arbeidsplasser. Hold gross ringvirkninger adskilt fra netto samfunnsøkonomisk nytte.','']
(ROOT/'prosjekter.md').write_text('\n'.join(lines))
print(f'Wrote {len(projects)} projects, {len(sources)} sources, {sum(p["coordinates"] is not None for p in projects)} documented address points.')

# This builder recreates the 2026-10-01 baseline. After intentionally rebuilding it,
# run update_report_research.py to reapply the 2026-10-05 report enrichment.
# Preserve subsequent manual research changes before rebuilding either version.
