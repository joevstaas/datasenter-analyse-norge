#!/usr/bin/env python3
"""Assemble reviewed pilot findings, preserving their scopes and source dates.

This is a research artifact builder, not an ecological impact model.
Run from any directory after the three agent input files exist.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/natur"
DATE = "2026-10-01"
SOURCES = {}


def add_source(sid, title, publisher, url, document_date=None, published=None,
               access="fulltext", locator="Se utsagnets henvisning", local=None,
               date_note="Nettpubliseringsdato ukjent; dokumentdato er separat.", **extra):
    source = dict(id=sid, title=title, publisher=publisher, url=url,
                  publishedAt=published, documentDate=document_date, accessedAt=DATE,
                  access=access, locator=locator, dateNote=date_note, localEvidence=local)
    source.update(extra)
    SOURCES[sid] = source


def finding(fid, text, refs, locator, kind="report_finding", when=None,
            confidence="medium", reason="Dokumentert kildeutsagn innen oppgitt avgrensning; ikke målt naturtap."):
    return dict(id=fid, statement=text, evidenceKind=kind, validTime=when,
                sourceIds=refs, locator=locator,
                uncertainty=dict(type="unknown" if confidence == "unknown" else "qualitative",
                                 confidence=confidence, reason=reason))


def action(owner, description, evidence):
    return dict(owner=owner, action=description, evidenceRequired=evidence)


def base_card(pid, name, plans, scope, has_geometry=True):
    return dict(id=f"nature-{pid}", projectId=pid, name=name,
                status="screening_only" if has_geometry else "insufficient_evidence",
                planIds=plans, geometryRole="regulatory_plan_extent" if has_geometry else "not_acquired",
                scopeNote=scope, ku=[], baseline=[], change=[], consequence=[], knowledge_gap=[],
                screening=dict(status="performed_preliminary" if has_geometry else "not_performed",
                    inputCrsStatus="unconfirmed" if has_geometry else "not_available",
                    spatialRelation="conditional_polygon_intersection" if has_geometry else "not_computed",
                    areaCalculationApproved=False, actualHabitatLossM2=None,
                    knowledgeCoverage="unknown",
                    resultFile="research/natur/gis-screening.json" if has_geometry else None,
                    limitations=["Ingen validert faktisk inngrepsgeometri eller arealberegning.",
                                 "Kartleggingsdekning og før-/ettertilstand er ikke fullstendig kontrollert."]),
                review=dict(reviewer="hovedagent", reviewedAt=DATE, status="limited_desk_review",
                            scope="Avgrenset kilde- og avgrensningskontroll; se qa-natur.md. Ingen feltvalidering."),
                nextActions=[])


def main():
    docs = json.loads((OUT / "utredninger.json").read_text())
    gis = json.loads((OUT / "gis-screening.json").read_text())
    for s in docs["sources"]:
        add_source(s["id"], s["title"], s["publisher"], s["url"], s.get("documentDate"),
                   s.get("publishedAt"), "fulltext" if s["access"] == "found_fulltext" else "reference_only",
                   local="research/natur/utredninger.json", updatedAt=s.get("updatedAt"), version=s.get("version"))
    projects = json.loads((ROOT / "research/prosjekter.json").read_text())
    for s in projects["sources"]:
        if s["id"] in ("plan-hamar", "plan-gromstul"):
            add_source(s["id"], s["title"], s["publisher"], s["dataUrl"],
                       access="api_response", local=s["rawGeometry"],
                       date_note="Geometridatum ikke eksplisitt deklarert; ikraftdato finnes i separat planmetadata.",
                       updatedAt=s.get("updatedAt"))
    for r in gis["results"]:
        sid = f"gis-{r['projectId']}-{r['service']}-{r['layerId']}"
        add_source(sid, r["layerName"] + " – foreløpig søk " + r["projectId"], "Miljødirektoratet",
                   r["idsQueryUrl"], access="api_response", local="research/natur/gis-screening.json",
                   locator=f"results: {r['projectId']}/{r['service']}/{r['layerId']}",
                   date_note="Publiseringsdato for dette datasettuttrekket ukjent. Objektenes kartleggingsår er separate.")

    hamar = base_card("hamar", "Heggvin – Hamar, med separat naboområdekontekst", ["079500"],
        "Karttesten gjelder Hamar 079500. Løten-KU og LE01 har andre/bredere avgrensninger og brukes kun med eksplisitt scope.")
    hamar["ku"] = [
        dict(component="Hamar 079500 – original naturutredning", status="found_reference_only", documentType="Naturutredning 2018",
             scopeNote="Referert i senere rapport; originalens geografi og feltkalender ikke kontrollert.", sourceIds=["u-hegg-loten"]),
        dict(component="Tilgrensende Løten-område", status="found_fulltext", documentType="Naturfaglig vurdering 2022",
             scopeNote="Ikke samme område som Hamar 079500.", sourceIds=["u-hegg-loten"]),
        dict(component="Heggvin og Sirkula samlet", status="found_fulltext", documentType="BREEAM LE01-strategi 2024",
             scopeNote="Bredere område og flere utbyggere. Ikke ny feltkartlegging eller observert ettertilstand.", sourceIds=["u-hegg-le01"])]
    hamar["baseline"] = [finding("h-baseline", "Løten-utredningen vurderer Stabekken og hjorteviltkorridoren som verdifulle økologiske funksjoner. Funnene gjelder dens undersøkelsesområde, ikke automatisk hele Hamar-planen.",
        ["u-hegg-loten"], "s. 7–9; geografisk avgrensning s. 2", when="2022-01-17")]
    hamar["change"] = [finding("h-change", "Hamar-planomrisset viser et reguleringsområde. Faktisk naturareal som er endret av datasenteret er ikke målt i piloten.",
        ["plan-hamar"], "plan 079500; rawGeometry", kind="knowledge_gap", confidence="unknown",
        reason="Mangler kontrollert før-/ettergrunnlag og geometri for faktisk inngrep.")]
    hamar["consequence"] = [finding("h-effect", "LE01-strategien vurderer netto biodiversitetstap og manglende grunnlag for LE01-poeng. Vurderingen gjelder det samlede området Heggvin/Sirkula og er ikke et målt tap for datasenteret alene.",
        ["u-hegg-le01"], "s. 1, 4, 14–15 og 19", when="2024-03-22", confidence="high"),
        finding("h-mitigation", "Hamar-bestemmelsene har krav om hensyn til vegetasjon, hogstperiode og bekk. Gjennomføringen av disse kravene er ikke kontrollert.",
        ["u-hegg-best"], "pkt. 2.6, 4.1 og 5.3; historisk versjon vedtatt 10.05.2023", kind="authority_statement", when="2023-05-10")]
    hamar["knowledge_gap"] = [finding("h-survey", "NiN-dekningsuttrekket har to Løten-registrerte kartleggingsområder fra 2021 som berører Hamar-planen i en betinget geometritest. Dette dokumenterer ikke full kartleggingsdekning eller fravær av naturverdier.",
        ["gis-hamar-naturtyper_nin-1"], "OBJECTID 4023/4387; conditionalPolygonIntersection", kind="spatial_screening", when="2021 / uttrekk 2026-10-01",
        reason="Plan-CRS er ubekreftet; dekningsgrad og tematisk scope er ikke fastslått."),
        finding("h-original", "Original Hamar-utredning fra 2018, oppdatert artsgrunnlag og dokumentasjon på faktisk gjennomført avbøting mangler i piloten.",
        ["u-hegg-loten", "u-hegg-best"], "Løten s. 2/litteraturliste; bestemmelser gir krav, ikke gjennomføringsbevis", kind="knowledge_gap", confidence="unknown",
        reason="Rapportreferanse og vedtaksbestemmelser er ikke erstatning for originalrapport og effektoppfølging.")]
    hamar["nextActions"] = [action("naturutredninger", "Hent original Hamar 2018 og gjeldende planvedlegg.", "Full rapport med kart, feltkalender og dokumentert kobling til plan 079500."),
        action("natur-GIS", "Avklar CRS, dekning, førbilder og faktisk inngrep.", "Planmetadata, datert ortofoto, temadekning og kontrollert inngrepspolygon.")]

    grom = base_card("gromstul", "Gromstul – Skien", ["2017004"],
        "Karttesten gjelder hele reguleringsområdet 2017004. Miljøprogram 2018 beskriver planfasen; dagens inngrep er ikke målt.")
    grom["ku"] = [dict(component="Gromstul natur-KU", status="found_reference_only", documentType="Natur-KU J03 fra 2018",
        scopeNote="Originalrapporten er identifisert, men fulltekst ikke lest i piloten.", sourceIds=["u-grom-ku", "u-grom-miljo"]),
        dict(component="Planlagt utbygging", status="found_fulltext", documentType="Miljøprogram 2018",
        scopeNote="Programkrav og førtilstandsbeskrivelse er ikke full KU eller dokumentert gjennomføring.", sourceIds=["u-grom-miljo"])]
    grom["baseline"] = [finding("g-baseline", "Miljøprogrammet fra 2018 beskriver tidligere myr/torv og omfattende drenering; torvkvaliteten var ukjent. Det dokumenterer et historisk kunnskapsgrunnlag, ikke dagens naturtilstand.",
        ["u-grom-miljo"], "s. 12, Grunn", when="2018-01-05", confidence="high")]
    grom["change"] = [finding("g-change", "Planområdet er dokumentert, men piloten har ikke beregnet faktisk nedbygd areal eller tap av myr/skog.",
        ["plan-gromstul", "u-grom-miljo"], "plan 2017004; miljøprogram 2018 er ikke etterundersøkelse", kind="knowledge_gap", confidence="unknown",
        reason="Mangler validert inngrepsgeometri og før-/etterbilder med dokumentert metode.")]
    grom["consequence"] = [finding("g-program", "Miljøprogrammet beskriver vegetasjonshensyn langs Bjordamsbekken, revegetering og håndtering av fremmede arter. Endelig vedtak og gjennomføring av disse programkravene er ikke kontrollert her.",
        ["u-grom-miljo"], "s. 11, Naturmangfold", when="2018-01-05"),
        finding("g-screen", "Søkerektangelet gir 38 NiN- og 7 DN13-kandidater. Ingen berører planringen i den betingede testen. Dette er ikke bevis for at naturverdier eller tidligere naturtap mangler.",
        ["gis-gromstul-naturtyper_nin-0", "gis-gromstul-naturtyper_hb13-0"], "countReturned og conditionalPolygonIntersection; raw features", kind="spatial_screening", when=DATE,
        reason="Ubekreftet plan-CRS, utvalgte temalag og ulike kartleggingsår; ingen effektanalyse.")]
    grom["knowledge_gap"] = [finding("g-ku-gap", "Original natur-KU, feltarbeidskalender og samsvar med senere prosjektendringer må kontrolleres. Søkeutdrag er ikke brukt som verifiserte naturfunn.",
        ["u-grom-ku", "u-grom-miljo"], "KU-referanse og tilgangslogg i utredninger.json", kind="knowledge_gap", confidence="unknown",
        reason="Full KU er ikke tilgjengelig i denne kontrollen."),
        finding("g-coverage", "Tre av fem dekningskandidater berører planen betinget. Full temadekning, førtilstand, AR5 og et eget Artskart-uttrekk er ikke kontrollert.",
        ["gis-gromstul-naturtyper_nin-1"], "conditionalPolygonIntersection; OBJECTID 6218/6380/6734", kind="knowledge_gap", confidence="unknown",
        reason="Berøring er ikke arealdekning; nye kartlegginger beskriver ikke automatisk natur før bygging.")]
    grom["nextActions"] = [action("naturutredninger", "Hent original natur-KU og senere faglige revisjoner.", "Fulltekst med kart/feltkalender og kobling til gjeldende prosjektutforming."),
        action("natur-GIS", "Koble dokumentert førtilstand mot faktisk inngrep og naturdatasett.", "CRS-bekreftelse, eldre ortofoto, AR5/artsdata og validert endringsgeometri.")]

    add_source("grom-permit-2025", "Tillatelse – WS Computing AS, datasenter 1 Gromstul", "Statsforvalteren i Vestfold og Telemark",
        "https://webfileservice.nve.no/API/PublishedFiles/Download/dddf6fda-38d1-491f-abc5-9464c85e35eb/202422995/3446684", "2025-08-25",
        local="research/natur/raw/gromstul-tillatelse-kildekontroll-2026-10-05.json",
        locator="s. 1–4", date_note="Dokumentdato kjent; publiseringsdato ukjent. PDF-tekst lest via nettverktøy; lokal nedlasting mislyktes.")
    SOURCES["grom-permit-2025"]["accessedAt"] = "2026-10-05"
    grom["baseline"].append(finding("g-permit-species", "Tillatelsen omtaler registrert ildsandbie (2022) og hagtornsommerfugl (2009, publisert 2021) i planområdet. Dette supplerer naturtypekarttesten; eget artsuttrekk mangler.",
        ["grom-permit-2025"], "s. 4", kind="authority_statement", when="2025-08-25",
        reason="Historiske registreringer gjengitt av myndighet; ikke bekreftet nåtilstand eller påvist skade."))
    grom["consequence"].append(finding("g-permit-water", "Tillatelsen beskriver overvann til Bjordamsbekken via rensing/fordrøyning og ingen utslipp av kjølevann eller prosessavløpsvann fra datasenter 1. Aksept med vilkår er ikke dokumentert ettertilstand eller samlet prosjektgodkjenning.",
        ["grom-permit-2025"], "s. 2–4", kind="authority_statement", when="2025-08-25"))
    grom["review"].update(reviewedAt="2026-10-05", scope="Tidligere pilotkontroll supplert med avgrenset lesing av tillatelse for datasenter 1. Ikke feltkontroll eller full KU.")

    # Narvik is maintained separately because its component and plan scopes differ.
    narvik = json.loads((OUT / "narvik-normalisert.json").read_text())
    for source in narvik["sources"]:
        assert source["id"] not in SOURCES
        SOURCES[source["id"]] = source
    cards = [grom, hamar, narvik["card"]]
    refs = set()
    def collect(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "sourceIds": refs.update(item)
                collect(item)
        elif isinstance(value, list):
            for item in value: collect(item)
    collect(cards)
    assert refs <= SOURCES.keys(), refs-SOURCES.keys()
    output = dict(schemaVersion="1.0.0", generatedAt="2026-10-05",
        scope="Tre naturpiloter. Foreløpig skrivebordskontroll med eksplisitte kunnskapshull; ingen nasjonal eller målt naturtapsanalyse.",
        sources=[SOURCES[s] for s in sorted(refs)], cards=cards)
    (OUT / "naturkort.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
