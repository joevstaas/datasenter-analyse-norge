#!/usr/bin/env python3
"""Conditional topology only; requires shapely. Run after run_screening.py.
No datum verification, projection, area calculation or nature-loss inference.
"""
import json
import hashlib
from pathlib import Path
import shapely
from shapely.geometry import Polygon, shape

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'research/natur'
data_path = OUT/'gis-screening.json'
data = json.loads(data_path.read_text())
assert data['planSourceSha256'] == hashlib.sha256((ROOT/'research/planomriss.geojson').read_bytes()).hexdigest(), 'Plan input changed after extraction'
plans = {f['id']: shape(f['geometry']) for f in json.loads((ROOT/'research/planomriss.geojson').read_text())['features']}
for result in data['results']:
    plan = plans[result['projectId']]
    assert plan.is_valid
    tested, hits, invalid = [], [], []
    for page_index in range(len(result['featureQueryUrls'])):
        filename = OUT/'raw'/(Path(result['rawPrefix']).name+f'-features-{page_index}.json')
        page = json.loads(filename.read_text())
        assert page['spatialReference']['wkid'] == 4326
        for feature in page['features']:
            attrs = feature['attributes']
            fid = attrs['OBJECTID']
            rings = [Polygon(ring) for ring in feature['geometry']['rings']]
            if not all(r.is_valid for r in rings):
                invalid.append(fid)
                continue
            # ArcGIS rings may represent separate shells and holes. Even/odd parity
            # yields their topology without assuming the first ring is the only shell.
            geometry = rings[0]
            for ring in rings[1:]:
                geometry = geometry.symmetric_difference(ring)
            if not geometry.is_valid:
                invalid.append(fid)
                continue
            tested.append(fid)
            if plan.intersects(geometry):
                hits.append(fid)
    result['conditionalPolygonIntersection'] = {
        'spatialRelation': 'conditional_polygon_intersection',
        'predicate': 'Shapely intersects including boundary contact',
        'coordinateSpace': 'unprojected lon/lat; conditional on source plan being compatible with EPSG:4326',
        'crsConfirmed': False,
        'countTested': len(tested),
        'countIntersects': len(hits),
        'objectIds': hits,
        'countBboxFalsePositivesConditional': len(tested)-len(hits),
        'invalidUntestedObjectIds': invalid,
        'shapelyVersion': shapely.__version__,
        'geometryConversion': 'symmetric difference of valid ArcGIS rings (even/odd shells and holes); no repair, snapping or simplification',
        'warning': 'Betinget topologisk planberøring. Ikke validert geodetisk overlapp, feltkartleggingsdekning eller naturtap.'
    }
    print(result['projectId'], result['service'],result['layerId'],len(hits),'of',len(tested),'invalid',invalid)
data['rawFileSha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((OUT/'raw').glob('gis-*'))}
data['scriptFileSha256'] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [OUT/'run_screening.py',Path(__file__)]}
data_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
