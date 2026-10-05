#!/usr/bin/env python3
"""Validate the nature pilot and fail closed on unsupported fact/area claims.

Requires jsonschema. Reads saved evidence only; does not query live services.
"""
import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/natur"


def validate_cards(data, schema):
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(data)
    sources = {s["id"]: s for s in data["sources"]}
    assert len(sources) == len(data["sources"]), "Duplicate source ID"
    assert len({c["id"] for c in data["cards"]}) == len(data["cards"]), "Duplicate card ID"
    finding_ids = []
    for card in data["cards"]:
        assert card["projectId"] in {"hamar", "gromstul", "narvik"}
        for row in card["ku"]:
            assert set(row["sourceIds"]) <= sources.keys(), "Unknown KU source"
        for section in ("baseline", "change", "consequence", "knowledge_gap"):
            for f in card[section]:
                finding_ids.append(f["id"])
                assert set(f["sourceIds"]) <= sources.keys(), "Unknown finding source"
                if f["evidenceKind"] == "documented_change":
                    assert any(sources[s]["access"] == "fulltext" for s in f["sourceIds"]), "No full evidence for change"
                if all(sources[s]["access"] in {"reference_only", "access_failed"} for s in f["sourceIds"]):
                    assert f["evidenceKind"] == "knowledge_gap", "Reference-only evidence used as fact"
        for source in sources.values():
            if source.get("localEvidence"):
                assert (ROOT / source["localEvidence"]).is_file(), "Missing evidence file"
    assert len(set(finding_ids)) == len(finding_ids), "Duplicate finding ID"


def validate_saved_gis():
    gis = json.loads((OUT / "gis-screening.json").read_text())
    assert gis["sourcePlanCrsConfirmed"] is False
    assert gis["trueOverlapCount"] is None and gis["overlapArea"] is None
    assert gis["planSourceSha256"] == hashlib.sha256((ROOT / "research/planomriss.geojson").read_bytes()).hexdigest()
    for filename, expected in gis["rawFileSha256"].items():
        assert hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == expected, filename
    for filename, expected in gis["scriptFileSha256"].items():
        assert hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == expected, filename
    for result in gis["results"]:
        assert result["paging"]["completeForQuery"] and not result["paging"]["exceededTransferLimit"]
        assert result["countReturned"] == result["idCount"] == result["serverCount"]
        assert result["trueOverlapCount"] is None
        c = result["conditionalPolygonIntersection"]
        assert c["countTested"] == result["countReturned"] and not c["invalidUntestedObjectIds"]
        assert c["countIntersects"] == len(c["objectIds"])
        assert c["countIntersects"] + c["countBboxFalsePositivesConditional"] == c["countTested"]
    return len(gis["results"]), len(gis["rawFileSha256"])


def main():
    schema = json.loads((OUT / "naturkort.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    data = json.loads((OUT / "naturkort.json").read_text())
    validate_cards(data, schema)
    checks = []
    def reject(label, alter):
        invalid = copy.deepcopy(data)
        alter(invalid)
        try:
            validate_cards(invalid, schema)
        except (AssertionError, __import__("jsonschema").ValidationError):
            checks.append(label)
        else:
            raise AssertionError("Unsafe value accepted: " + label)
    reject("unknown_loss_is_not_zero", lambda d: d["cards"][0]["screening"].update(actualHabitatLossM2=0))
    reject("unreviewed_area_cannot_be_approved", lambda d: d["cards"][0]["screening"].update(areaCalculationApproved=True))
    reject("missing_source_rejected", lambda d: d["cards"][0]["baseline"][0].update(sourceIds=["nonexistent-source"]))
    reject("knowledge_gaps_required", lambda d: d["cards"][0].update(knowledge_gap=[]))
    reject("nature_score_forbidden", lambda d: d["cards"][0].update(natureScore=99))
    queries, raw_files = validate_saved_gis()
    print(json.dumps(dict(status="passed", cards=len(data["cards"]), sources=len(data["sources"]),
                         completeQueries=queries, checkedRawFiles=raw_files,
                         rejectedInvalidCases=checks,
                         limitation="Structural/evidence integrity only; no field verification or geodetic CRS approval."),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
