# Norske datasenterprosjekter – første kildebelagte utvalg

Lest 2026-10-01. Åtte prosjekter; ikke uttømmende og ikke et statistisk representativt utvalg. Maskinlesbare påstander og kilde-ID-er ligger i `prosjekter.json`.

## Metode og begrensninger

Hver påstand har kilde, observasjonsperiode (eller null), type og dokumentert konfidensnivå. Publiseringsdato og lesedato er separate. Ingen konfidensintervaller konstrueres uten statistisk modell. Null betyr ukjent, aldri null fysisk påvirkning.

Seks punkter er hentet fra Kartverkets adresse-API. Råsvar ligger i `raw/`. EPSG:4258 er bevart. Alle svar har `stedfestingverifisert=false`; punktene kan brukes som dokumenterte adresser med middels konfidens, ikke som arealgrenser. Enebakk-søket gir også en annen kommune: kun eksakt adresse i Enebakk er brukt. Lefdals registeradresse må kontrolleres mot anleggsplan.

To ekte planomriss (Heggvin og Gromstul) er hentet fra kommunalt register og lagret i planomriss.geojson. De viser hele reguleringsområdet, ikke faktisk arealbeslag eller bare datasenteret. Ringlukking og topologi er kontrollert; CRS er tolket fra registerets frontend, men ikke oppgitt i API-responsen. Ingen målt årlig TWh eller faktisk nedbygd areal er dokumentert her.

## Green Mountain OSL-Hamar / Heggvin

Hamar — I drift; videre utvidelse planlagt.

Adressepunkt: Stabekkvegen 140; lat 60.84134903994555, lon 11.267875011605103 (EPSG:4258). Kilder: gm-contact, kartverket-stabekkvegen-140.

- **status / reported_status:** I drift; videre utvidelse planlagt . Periode: 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-2025.
- **ownership / reported_group_owner:** Green Mountain; Azrieli Group oppgis som konserneier . Periode: 2021 acquisition; current webpage undated. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-owner.
- **municipality / location:** Hamar . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-hamar.
- **power / contracted_IT_capacity:** 90 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-hamar.
- **power / planned_maximum_IT_capacity:** 150 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-hamar.
- **area / potential_campus_area:** 280000 m2. Periode: ikke oppgitt. Konfidens: middels. Operatørens potensielle campusareal; ikke målt nedbygd natur. Kilder: gm-hamar.
- **jobs / more_than_current_workplace_count:** 200 persons. Periode: ikke oppgitt. Konfidens: middels. Operatør oppgir mer enn 200; ikke antall direkte ansatte eller årsverk. Kilder: gm-hamar.
- **value_creation / modelled_construction_gross_value_added:** 6100000000 NOK. Periode: Byggefase første tre bygg, inkludert forventede 2025–2026-utgifter. Konfidens: lav. 5,7 mrd beregnet fra gjennomførte investeringer + 0,4 mrd prognose. Ekskluderer TikToks egne investeringer. Ikke realisert netto eller årlig gevinst. Kilder: hamar-menon-full.
- **nature / operator_design_claim:** Tilrettelagt for varmegjenvinning; faktisk utnyttet varme ikke dokumentert her. . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-hamar.
- **power / reported_total_power_capacity:** 110 MW. Periode: rapport august 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: hamar-menon-full.
- **area / reported_site_size_first_three_buildings:** 139000 m2. Periode: rapport august 2025. Konfidens: middels. Rapportens tomtestørrelse for eksisterende utbygging, ikke faktisk naturtap. Må avstemmes mot 280 000 m2 potensielt campus på nettsiden. Kilder: hamar-menon-full.
- **jobs / reported_regular_workplace_count:** 220 persons. Periode: rapport august 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: hamar-menon-full.
- **plan_extent / regulatory_plan_area_not_actual_land_take:** Detaljreguleringsplan for Heggvin næringspark . Periode: 2022-04-27T00:00:00. Konfidens: middels. Reell digital plangrense fra kommunalt register. Polygon er ikke arealbeslag. Kilder: plan-hamar.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. Planomriss hentet; gjeldende revisjon, formålsflater, eiendomsavgrensning og faktisk nedbygging må fortsatt kvalitetssikres.

## Green Mountain SVG-Rennesøy

Stavanger — I drift.

Adressepunkt: Hodneveien 260; lat 59.06854209888397, lon 5.758031501966236 (EPSG:4258). Kilder: gm-contact, kartverket-hodneveien-260.

- **status / reported_status:** I drift . Periode: 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-2025.
- **ownership / reported_group_owner:** Green Mountain; Azrieli Group oppgis som konserneier . Periode: 2021 acquisition; current webpage undated. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-owner.
- **municipality / location:** Stavanger . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rennesoy.
- **power / maximum_IT_capacity:** 25 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rennesoy.
- **area / reported_site_area:** 144700 m2. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-three.
- **area / reported_available_mountain_hall_space:** 23000 m2. Periode: ikke oppgitt. Konfidens: middels. Kilden kaller dette både campus footprint og tilgjengelig areal i fjellhaller. Ikke tolket som nedbygd overflate. Kilder: gm-rennesoy.
- **jobs / regular_workplace_count:** 80 persons. Periode: 2024. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: rennesoy-economy.
- **value_creation / modelled_cumulative_gross_value_added:** 2300000000 NOK. Periode: 2011–2024. Konfidens: lav. Kumulativ ringvirkningsmodell inkludert investering/drift; 2024 delvis budsjett. Ikke årlig verdi. Kilder: rennesoy-economy.
- **nature / reported_site_characteristics:** Gjenbruk av tidligere NATO-fjellhaller; fjordkjøling. . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rennesoy.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede.

## Green Mountain TEL-Rjukan

Tinn — I drift.

Adressepunkt: Svaddevegen 161; lat 59.88108325483751, lon 8.669421227037606 (EPSG:4258). Kilder: gm-contact, kartverket-svaddevegen-161.

- **status / reported_status:** I drift . Periode: 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-2025.
- **ownership / reported_group_owner:** Green Mountain; Azrieli Group oppgis som konserneier . Periode: 2021 acquisition; current webpage undated. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-owner.
- **municipality / location:** Tinn . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rjukan.
- **power / design_capacity:** 40 MW. Periode: 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-2025.
- **power / potential_maximum_IT_capacity:** 50 MW. Periode: ikke oppgitt. Konfidens: middels. Operatørens nyere udaterte nettside; kan ikke likestilles med 40 MW designkapasitet for 2025. Kilder: gm-rjukan.
- **area / reported_campus_area:** 29000 m2. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rjukan.
- **nature / operator_design_claim:** Luftkjøling; klargjort for varmegjenvinning. . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-rjukan.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. 40 MW design i rapport for 2025 og 50 MW potensial på nettside må avstemmes; dette er ikke et statistisk intervall.

## Green Mountain OSL-Enebakk

Enebakk — I drift.

Adressepunkt: Granittveien 110; lat 59.75739221276422, lon 10.99371918458457 (EPSG:4258). Kilder: gm-contact, kartverket-granittveien-110.

- **status / reported_status:** I drift . Periode: 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-2025.
- **ownership / reported_group_owner:** Green Mountain; Azrieli Group oppgis som konserneier . Periode: 2021 acquisition; current webpage undated. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-owner.
- **municipality / location:** Enebakk . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-enebakk.
- **power / headline_total_IT_capacity:** 75 MW. Periode: ikke oppgitt. Konfidens: lav. Samme side oppgir også 93 MW maksimum og 94 MW line-of-sight; definisjonene er ikke avstemt. Kilder: gm-enebakk.
- **power / maximum_capacity:** 93 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-enebakk.
- **power / line_of_sight_capacity:** 94 MW. Periode: ikke oppgitt. Konfidens: lav. Operatørens eget begrep; ingen realiseringsgaranti. Kilder: gm-enebakk.
- **area / reported_acquired_site_area:** 72200 m2. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-enebakk.
- **area / reported_site_area_in_economic_summary:** 81205 m2. Periode: ikke oppgitt. Konfidens: lav. Avviker fra 72 200 m2 nettside. Ulik avgrensning eller tidspunkt ikke avklart. Kilder: gm-three.
- **jobs / regular_workplace_count:** 98 persons. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-three.
- **nature / operator_design_claim:** Klargjort for varmegjenvinning; faktisk leveranse ikke dokumentert her. . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-enebakk.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. Effektdefinisjoner 75/93/94 MW og arealavvik 72 200/81 205 m2 trenger avklaring; ikke slå sammen til konfidensintervaller.

## Green Mountain SVG-Undheim

Time — Under bygging ifølge operatør; planlagt ferdigstillelse 2028.

Koordinater: ukjent.

- **status / reported_status:** Under bygging ifølge operatør; planlagt ferdigstillelse 2028 . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.
- **ownership / reported_group_owner:** Green Mountain; Azrieli Group oppgis som konserneier . Periode: 2021 acquisition; current webpage undated. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-owner.
- **municipality / location:** Time . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.
- **power / planned_IT_capacity:** 80 MW. Periode: full completion planned 2028. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.
- **power / planned_site_capacity:** 100 MW. Periode: full completion planned 2028. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.
- **area / reported_campus_area:** 76000 m2. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.
- **jobs / approximately_forecast_regular_workplace_count:** 100 persons. Periode: future operations. Konfidens: lav. Operatørprognose, ikke observerte arbeidsplasser. Kilder: gm-undheim.
- **nature / operator_design_claim:** Design for luft- og væskekjøling samt mottakere av overskuddsvarme. . Periode: planned. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: gm-undheim.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede.

## Google / WS Computing – Gromstul

Skien — Byggestart dokumentert 2024; søknad byggetrinn 2 i august 2025. Drift ikke bekreftet..

Koordinater: ukjent.

- **status / documented_historical_status:** Byggestart dokumentert 2024; søknad byggetrinn 2 i august 2025. Drift ikke bekreftet. . Periode: 2024–2025. Konfidens: høy. Kommunal prosjektkronologi; dagens driftsstatus er ikke avklart. Kilder: skien-timeline.
- **municipality / location:** Skien . Periode: ikke oppgitt. Konfidens: høy. Kommunal prosjektkilde. Kilder: skien-timeline.
- **ownership / reported_group_owner:** Tomtekjøper WS Computing AS, Google-selskap; Google er del av Alphabet. . Periode: 2019 acquisition / 2024 statement. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: skien-timeline, google-release.
- **area / approximately_purchased_plot_area:** 2000000 m2. Periode: 2019. Konfidens: høy. Nær 2000 mål tomt; ikke faktisk nedbygd areal. Kilder: skien-timeline.
- **area / approximately_regulated_total_area:** 3000000 m2. Periode: 2018. Konfidens: høy. Nær 3000 mål reguleringsområde; videre avgrensning ikke hentet. Kilder: skien-timeline.
- **power / allocated_capacity_operator_statement:** 240 MW. Periode: 2024-02-07 first phase. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: google-release.
- **power / historical_permitted_connection:** 50 MW. Periode: 2020-11-23. Konfidens: høy. NVE beskriver denne nettkonsesjonsendringen; ikke påstand om dagens samlede anleggskapasitet. Kilder: gromstul-nve.
- **value_creation / forecast_construction_gross_value_added:** 6700000000 NOK. Periode: 2024–2025. Konfidens: lav. Deloitte-modell bestilt av Google, sitert i pressemelding. Ikke realisert eller netto verdi. Kilder: google-release.
- **nature / municipal_planning_notice:** Planlagt massedeponi fra byggetrinn 1: ca. 500 000 m3. Varslingsområde omfatter skog, bekker og grøftet myr; konsekvensutredning kreves. . Periode: 2026 planning notice. Konfidens: høy. Dokumentert utredningsbehov og tiltak, ikke ferdig vurdering av faktisk naturtap. Kilder: gromstul-deponi.
- **plan_extent / regulatory_plan_area_not_actual_land_take:** Reguleringsplan for gbnr. 11/1 - datasenter Gromstul . Periode: 2018-05-31T00:00:00. Konfidens: middels. Reell digital plangrense fra kommunalt register. Polygon er ikke arealbeslag. Kilder: plan-gromstul.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. 240 MW fra operatør er ikke kontrollert mot gjeldende nettilknytningsavtale. 2026 var en forventet driftsstart i 2024; faktisk oppstart må verifiseres. Planomriss hentet; gjeldende revisjon, formålsflater, eiendomsavgrensning og faktisk nedbygging må fortsatt kvalitetssikres.

## Bulk N01 Campus – Støleheia

Vennesla — Drift og utbygging dokumentert i rapport for Q4 2025.

Adressepunkt: Stølevegen 39; lat 58.25757326329835, lon 7.892050117139653 (EPSG:4258). Kilder: bulk-address, kartverket-stølevegen-39.

- **municipality / location:** Vennesla . Periode: ikke oppgitt. Konfidens: høy. Kommunens utbyggingsavtale. Kilder: n01-va.
- **status / reported_status:** Drift og utbygging dokumentert i rapport for Q4 2025 . Periode: Q4 2025. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: bulk-q4.
- **power / marketed_potential_site_capacity:** 1000 MW. Periode: ikke oppgitt. Konfidens: lav. Markedsført skaleringspotensial; ikke forbruk eller bekreftet nettilknytning. Side ble kun tilgjengelig som søkeuttrekk. Kilder: n01-site.
- **power / announced_target_power_capacity:** 400 MW. Periode: target 2026 announced 2024. Konfidens: lav. Historisk mål, ikke bekreftet levert kapasitet i 2026. Kilder: n01-invest.
- **area / marketed_campus_area:** 3000000 m2. Periode: ikke oppgitt. Konfidens: lav. 3 km2 markedsført campus; kun søkeuttrekk tilgjengelig, ingen avgrensningskontroll. Kilder: n01-site.
- **ownership / reported_group_shareholding:** {"Bulk Industrier AS": 35.8, "BGO Europe IV": 30.8, "BGO King HoldCo": 15.2, "Geveran Trading Co. Ltd.": 7.8, "others": 10.5} %. Periode: 2025-12. Konfidens: middels. Selskapets eieroversikt, avrundet; sum 100,1 %. Ikke matrikkelens tomteeier. Kilder: bulk-owner.
- **nature / planning_process:** Kommunal utbyggingsavtale for VA-anlegg lagt ut på høring. . Periode: 2026-03-10 decision. Konfidens: høy. Sier ikke hvor stort naturtap tiltaket medfører. Kilder: n01-va.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. 1 GW markedsføring, 400 MW 2026-mål og 2 GW ambisjon fra 2024 gjelder ulike stadier; trenger oppdatert avstemming. Prosjektspesifikke driftsjobber og verdiskaping mangler. Konsernets 125 FTE i Q4 2025 er ikke fordelt på N01.

## Lefdal Mine Data Centers

Stad — Operativt anlegg ifølge operatør.

Adressepunkt: Nordfjordvegen 7300; lat 61.93203463076023, lon 5.506214036146013 (EPSG:4258). Kilder: lefdal-register, kartverket-nordfjordvegen-7300.

- **municipality / registered_location:** Stad . Periode: ikke oppgitt. Konfidens: høy. Brønnøysundregistrenes forretningsadresse. Kilder: lefdal-register.
- **status / reported_status:** Operativt anlegg ifølge operatør . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-power.
- **power / available_power_capacity:** 80 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-power.
- **power / reserved_for_current_customers:** 20 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-power.
- **power / potential_facility_capacity:** 200 MW. Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-site.
- **area / potential_underground_whitespace:** 120000 m2. Periode: ikke oppgitt. Konfidens: middels. Potensielt IT-gulvareal i gruve; ikke tomt eller overflateinngrep. Kilder: lefdal-site.
- **ownership / superseded_ownership_webpage:** {"Columbia Threadneedle European Sustainable Infrastructure Fund": 66.67, "other_named_main_shareholder": "Professor Friedhelm Loh"} . Periode: ikke oppgitt. Konfidens: lav. Utdatert operatørside: motsies av datert 3i-sluttføringsmelding 03.09.2026. Kilder: lefdal-owner.
- **nature / operator_site_characteristics:** Gjenbruk av underjordisk gruve og fjordbasert kjøling. . Periode: ikke oppgitt. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-site.
- **ownership / completed_transaction_reported_shareholding:** 3i forvalter 90 %: 3i Infrastructure litt over 45 %, medinvestorer ca. 45 %. Gjenværende minoritet 10 %. %. Periode: 2026-09-02. Konfidens: høy. Datert investors sluttføringsmelding. Første kjøp 28.08.2026, tillegg 02.09.2026. Ikke uavhengig aksjeeierbok. Kilder: lefdal-3i-close.
- **power / reported_operational_capacity:** 37 MW. Periode: 2026-03-11. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-3i-agreement.
- **power / contracted_capacity_under_construction:** 43 MW. Periode: 2026-03-11. Konfidens: middels. Partsopplysning; ikke uavhengig bekreftet. Kilder: lefdal-3i-agreement.

Kunnskapshull: Faktisk årlig kraftbruk (målt TWh og år) mangler. Faktisk nedbygd areal med måledato og metode mangler. Validert planpolygon, bygningsfotavtrykk og naturtypeoverlegg mangler. Eiendomseier og endelig reell eier er ikke kontrollert mot full eierkjede. Prosjektspesifikke driftsjobber og verdiskaping ikke dokumentert. Udatert effektmelding gir ingen sikker observasjonsdato for 80 MW. 80 MW tilgjengelig nettkapasitet på udatert operatørside må holdes adskilt fra 37 MW drift / 43 MW under bygging oppgitt 11.03.2026.

## Kilderegister

- `gm-contact` — [Kontaktadresser for datasentre](https://greenmountain.no/contact-us/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-owner` — [Hvem eier Green Mountain?](https://info.greenmountain.no/faq/azrieli-group/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-2025` — [Sustainability report 2025](https://greenmountain.no/wp-content/uploads/Sustainability-Report-2025-1.pdf). Green Mountain; operator. Publisert: 2026-05. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-three` — [Key facts – The three data centers](https://greenmountain.no/wp-content/uploads/Summary-Economic-Impact-Report-SVG-Rennesoy-TEL-Rjukan-OSL-Enebakk.pdf). Green Mountain / Menon; commissioned_analysis. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-hamar` — [OSL-Hamar](https://greenmountain.no/data-center/osl-hamar/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-rennesoy` — [SVG-Rennesøy](https://greenmountain.no/data-center/svg-rennesoy/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-rjukan` — [TEL-Rjukan](https://greenmountain.no/data-center/tel-rjukan/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-enebakk` — [OSL-Enebakk](https://greenmountain.no/data-center/osl-enebakk/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gm-undheim` — [SVG-Undheim](https://greenmountain.no/data-center/svg-undheim/). Green Mountain; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `hamar-plan` — [Heggvin: planreferanser og prosjekt](https://www.hamar.kommune.no/utviklingsomrader/heggvin). Hamar kommune; municipality. Publisert: 2023-12-15. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `rennesoy-economy` — [Sammendrag av ringvirkninger Rennesøy (tittel i PDF feilaktig Rjukan)](https://greenmountain.no/wp-content/uploads/MENON-Economic-Impact-Report-Green-Mountain-SVG-Rennesoy-Summary_01.11.2024.pdf). Menon / Green Mountain; commissioned_analysis. Publisert: 2024-11-01. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `skien-timeline` — [Tidslinje for Google-etablering](https://www.skien.kommune.no/by-og-naeringsutvikling/google-etablering-i-skien-kommune/tidslinje-hva-har-skjedd-fram-til-naa/). Skien kommune; municipality. Publisert: 2024-02-19. Oppdatert: 2025-09-18. Lest: 2026-10-01.
- `google-release` — [Google starter bygging i Skien](https://kommunikasjon.ntb.no/pressemelding/18046820/google-starter-bygging-av-et-nytt-datasenter-i-skien-investerer-600-millioner-euro?lang=no&publisherId=8930805). Google Norge (NTB distribusjon); operator. Publisert: 2024-02-07. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gromstul-nve` — [Gromstul (Kise) koblingsstasjon med 132 kV nettilknytning](https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak/?id=4885&type=A-1). NVE; authority. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gromstul-plan` — [Bystyret sak 75/18: Gromstul sluttbehandling](https://opengov.360online.com/Meetings/skien/Meetings/Details/819161?agendaItemId=222580). Skien kommune; municipality. Publisert: 2018-05-31. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `gromstul-deponi` — [Detaljregulering Fjellimellomdalen](https://www.skien.kommune.no/politikk/kunngjoeringer/detaljregulering-for-gbnr-111-fjellimellomdalen/). Skien kommune; municipality. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `n01-site` — [N01 Data Center Campus](https://bulkinfrastructure.com/data-centers/locations/n01). Bulk Infrastructure; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `n01-invest` — [BGO investering og N01-utbygging](https://bgo.com/press-release/bulk-infrastructure-announces-350msup1/sup-equity-investment-by-bgo-and-plans-for-over-1bn-of-investments-by-2026-to-grow-sustainable-data-centre-l-1717514270601). BGO / Bulk; operator. Publisert: 2024-06-05. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `bulk-owner` — [Investor relations: eierfordeling desember 2025](https://bulkinfrastructure.com/about-us/investor-relations). Bulk Infrastructure; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `bulk-q4` — [Fourth Quarter 2025 Results](https://bulkinfrastructure.com/uploads/Financial-report/Bulk-Infrastructure-Group-Financial-statements-Q4-2025.pdf). Bulk Infrastructure; operator. Publisert: 2026-02-05. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `bulk-address` — [ISO-sertifikat med stedsliste (utløpt; kun adressebelegg)](https://bulkinfrastructure.com/uploads/ISO-cert-14001.PDF). LRQA / Bulk; certification. Publisert: 2022-10-03. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `n01-va` — [Utbyggingsavtale Stølen datalagringspark](https://www.vennesla.kommune.no/kunngjoringer-og-planer-pa-horing/utbyggingsavtale-stolen-datalagrinspark.9114.aspx). Vennesla kommune; municipality. Publisert: 2026-03-13. Oppdatert: 2026-03-13. Lest: 2026-10-01.
- `lefdal-site` — [Lefdal Mine Data Centers](https://www.lefdalmine.com/). Lefdal Mine Data Centers; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `lefdal-power` — [Utvidelse av tilgjengelig effekt med 60 MW](https://www.lefdalmine.com/news/lefdal-mine-datacenter-expand-power-capacity-with-60-mw). Lefdal Mine Data Centers; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `lefdal-owner` — [Ownership](https://www.lefdalmine.com/about/ownership). Lefdal Mine Data Centers; operator. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `lefdal-register` — [Lefdal Mine Datacenter AS – registeradresse](https://virksomhet.brreg.no/nn/oppslag/enheter/911599252). Brønnøysundregistrene; authority. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `kartverket-stabekkvegen-140` — [Kartverket adressepunkt: Stabekkvegen 140](https://ws.geonorge.no/adresser/v1/sok?sok=Stabekkvegen+140&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2024-06-27T10:12:25. Lest: 2026-10-01.
- `kartverket-hodneveien-260` — [Kartverket adressepunkt: Hodneveien 260](https://ws.geonorge.no/adresser/v1/sok?sok=Hodneveien+260&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2021-02-24T22:11:36. Lest: 2026-10-01.
- `kartverket-svaddevegen-161` — [Kartverket adressepunkt: Svaddevegen 161](https://ws.geonorge.no/adresser/v1/sok?sok=Svaddevegen+161&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2024-01-01T00:00:00. Lest: 2026-10-01.
- `kartverket-granittveien-110` — [Kartverket adressepunkt: Granittveien 110](https://ws.geonorge.no/adresser/v1/sok?sok=Granittveien+110&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2024-09-05T09:45:16. Lest: 2026-10-01.
- `kartverket-stølevegen-39` — [Kartverket adressepunkt: Stølevegen 39](https://ws.geonorge.no/adresser/v1/sok?sok=St%C3%B8levegen+39&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2020-06-15T18:31:24. Lest: 2026-10-01.
- `kartverket-nordfjordvegen-7300` — [Kartverket adressepunkt: Nordfjordvegen 7300](https://ws.geonorge.no/adresser/v1/sok?sok=Nordfjordvegen+7300&treffPerSide=10). Kartverket; authority. Publisert: ikke oppgitt. Oppdatert: 2020-06-15T18:28:21. Lest: 2026-10-01.
- `lefdal-3i-close` — [3i Infrastructure completes investment in Lefdal](https://www.3i-infrastructure.com/newsroom/press-releases/2026/3i-infrastructure-plc-completes-investment-in-the-lefdal-mine-datacenter-campus/). 3i Infrastructure; investor. Publisert: 2026-09-03. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `lefdal-3i-agreement` — [3i Infrastructure invests in Lefdal](https://www.3i-infrastructure.com/newsroom/press-releases/2026/3i-infrastructure-plc-invests-in-lefdal-mine-datacenter/). 3i Infrastructure; investor. Publisert: 2026-03-11. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `hamar-menon-full` — [Economic impact analysis OSL-Hamar construction, Menon 96/2025](https://greenmountain.no/wp-content/uploads/Report-Economic-Impact-Analysis-of-OSL-Hamar-Construction-english.pdf). Menon / Green Mountain; commissioned_analysis. Publisert: 2025-08. Oppdatert: ikke oppgitt. Lest: 2026-10-01.
- `plan-hamar` — [Detaljreguleringsplan for Heggvin næringspark](https://arealplaner.no/hamar3403/arealplaner/156). Kommunalt planregister / Norkart; municipal_plan_register. Publisert: ikke oppgitt. Oppdatert: 2024-11-26T00:00:00. Lest: 2026-10-01.
- `plan-gromstul` — [Reguleringsplan for gbnr. 11/1 - datasenter Gromstul](https://arealplaner.no/skien4003/arealplaner/726). Kommunalt planregister / Norkart; municipal_plan_register. Publisert: ikke oppgitt. Oppdatert: ikke oppgitt. Lest: 2026-10-01.

## Søkelogg og videre kontroll

- 2026-10-01: Operatørsøk Green Mountain, Bulk N01, Lefdal og Skygard. Skygard ble ikke inkludert i første åtte; søk avdekket forskjellige eierlister og udokumenterte MW-tall hos kataloger.
- 2026-10-01: Kommunesøk Skien/Gromstul, Hamar/Heggvin, Vennesla/Støleheia. Heggvin 079500 og Gromstul 2017004 identifisert. Kommunale metadata og digitale planomriss hentet via Arealplaner offentlig API; råsvar og GeoJSON lagret.
- 2026-10-01: NVE konsesjon 4885 gjennomgått. Historisk 50 MW tillatelse kan ikke overstyre senere opplysninger om 240 MW tildeling uten kontroll av endringshistorikk.
- 2026-10-01: Kartverkets adresse-API hentet for seks eksakte adresser; råsvar lagret. Operatøradresse som geokodingsinput for fire GM-anlegg; LRQA-stedsliste for N01; Brønnøysundregister for Lefdal.
- 2026-10-01: Statsforvalterens søketreff om Heggvin viste naturkartleggingsvedlegg, men åpning videresendte til portal. Ikke brukt som verifisert naturkonklusjon.
- 2026-10-01: Bulk N01-nettsiden feilet ved fulltekstinnhenting. Kun markedsførte 3 km2/1 GW fra søkeuttrekk beholdt med lav konfidens og eksplisitt flagg.
- Videre: hent gjeldende plandata fra kommunal plandatabase (SOSI/GML/GeoJSON), dokumenter plan-ID/revisjon/CRS, og beregn areal i projisert CRS. Sammenhold historiske ortofoto/byggetrinn med vedtatt plan.
- Videre: innhent årsvis målt kraft, godkjent tilknytning, IT-last, kjøling, faktisk varmeleveranse, utslippsvilkår, naturtypekartlegging og observerte arbeidsplasser. Hold gross ringvirkninger adskilt fra netto samfunnsøkonomisk nytte.
