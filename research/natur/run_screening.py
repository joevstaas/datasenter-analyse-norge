#!/usr/bin/env python3
"""Public Naturebase bbox screening. No plan-polygon intersection or area calculation.
Run from repository root: python3 research/natur/run_screening.py
Uses only Python stdlib. Network access required. Each execution is a new snapshot.
"""
import datetime
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/natur'
RAW = OUT / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
BASE = 'https://kart.miljodirektoratet.no/arcgis/rest/services/'
LAYERS = [('naturtyper_nin', 0), ('naturtyper_nin', 1), ('naturtyper_hb13', 0), ('vern', 0)]

def fetch(url, filename):
    request = urllib.request.Request(url, headers={'User-Agent': 'Norwegian-datacenter-nature-screening/1.0'})
    with urllib.request.urlopen(request, timeout=90) as response:
        body = response.read()
    (RAW / filename).write_bytes(body)
    value = json.loads(body)
    if 'error' in value:
        raise RuntimeError(value['error'])
    return value

def url(base, **params):
    return base + '?' + urllib.parse.urlencode(params)

def record(attributes):
    # Whole-source-polygon area must not look like a plan intersection or nature loss.
    clean = {k:v for k,v in attributes.items() if not k.startswith('SHAPE.')}
    for k in ['Kartleggingsdato', 'registreringsDato', 'datafangstdato']:
        if isinstance(attributes.get(k), (int, float)):
            clean[k+'ISO'] = datetime.datetime.fromtimestamp(attributes[k]/1000, datetime.timezone.utc).date().isoformat()
    return clean

def main():
    plans_path = ROOT / 'research/planomriss.geojson'
    plans = json.loads(plans_path.read_text())['features']
    result = {
        'retrievedAt': datetime.date.today().isoformat(),
        'sourceAuthority': 'Miljødirektoratet',
        'status': 'preliminary_bbox_screening',
        'planSourceSha256': hashlib.sha256(plans_path.read_bytes()).hexdigest(),
        'sourcePlanCrsConfirmed': False,
        'queryCrs': 'EPSG:4326 assumed for input envelope; source plan datum unconfirmed',
        'naturalDataNativeCrs': 'EPSG:25833',
        'returnedGeometryCrs': 'EPSG:4326 requested explicitly',
        'spatialRelation': 'bbox_candidate',
        'trueOverlapCount': None,
        'overlapArea': None,
        'warning': 'Planområde er ikke faktisk arealbeslag. Bbox-treff er ikke verifiserte planoverlapp. Ingen funn betyr ikke fravær av naturverdier.',
        'services': [], 'results': []}
    for service, layer in LAYERS:
        endpoint = BASE + f'{service}/MapServer'
        meta = fetch(url(endpoint, f='pjson'), f'gis-service-{service}.json')
        layer_url = endpoint + f'/{layer}'
        lm = fetch(url(layer_url, f='pjson'), f'gis-layer-{service}-{layer}.json')
        result['services'].append({
            'service': service, 'layerId': layer, 'name': lm['name'],
            'url': layer_url, 'metadataUrl': url(layer_url, f='pjson'),
            'catalogUrl': f'https://kartkatalog.miljodirektoratet.no/MapService/Details/{service}',
            'nativeSpatialReference': meta['spatialReference'],
            'geometryType': lm.get('geometryType'),
            'copyrightText': lm.get('copyrightText'),
            'maxRecordCount': lm.get('maxRecordCount', meta.get('maxRecordCount')),
            'editingInfo': lm.get('editingInfo'),
            'year': 'Mixed feature-level survey/update years; retrieval year is not survey year',
            'license': 'NLOD; see saved official catalog HTML and documentation in gis-screening.md',
            'datasetCoverage': 'known_national_register' if service == 'vern' else 'unknown',
            'coverageNote': 'NiN layer 1 supplies surveyed-area records; full plan coverage is not established by bbox candidates.'})
        for plan in plans:
            pts = plan['geometry']['coordinates'][0]
            bbox = [min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)]
            env = dict(zip(['xmin','ymin','xmax','ymax'], bbox))
            env['spatialReference'] = {'wkid': 4326}
            stem = f"gis-{plan['id']}-{service}-{layer}"
            params = dict(f='json', where='1=1', geometry=json.dumps(env, separators=(',',':')), geometryType='esriGeometryEnvelope', inSR=4326, spatialRel='esriSpatialRelIntersects')
            ids_url = url(layer_url+'/query', **params, returnIdsOnly='true')
            ids_data = fetch(ids_url, stem+'-ids.json')
            ids = sorted(ids_data.get('objectIds') or [])
            count_url = url(layer_url+'/query', **params, returnCountOnly='true')
            count_data = fetch(count_url, stem+'-count.json')
            features, queries, truncation = [], [], False
            for index in range(0,len(ids),100):
                q = url(layer_url+'/query', f='json', objectIds=','.join(map(str, ids[index:index+100])), outFields='*', returnGeometry='true', outSR=4326)
                data = fetch(q, stem+f'-features-{index//100}.json')
                queries.append(q)
                features.extend(data.get('features', []))
                truncation |= data.get('exceededTransferLimit', False)
            id_field = ids_data.get('objectIdFieldName')
            returned_ids = [f['attributes'].get(id_field) for f in features]
            complete = not truncation and len(ids) == count_data['count'] == len(features) and sorted(returned_ids) == ids
            result['results'].append({
                'projectId': plan['id'], 'planId': plan['properties']['planId'],
                'planGeometryType': plan['geometry']['type'], 'planGeometryRole': 'regulatory_plan_extent',
                'planSourceUrl': plan['properties']['sourceUrl'],
                'service': service, 'layerId': layer, 'layerName': lm['name'],
                'bbox': bbox, 'bboxOrder': '[xmin,ymin,xmax,ymax]',
                'spatialRelation': 'bbox_candidate', 'queryPredicate': 'esriSpatialRelIntersects with envelope, not plan polygon',
                'geometryType': lm.get('geometryType'),
                'serverCount': count_data['count'], 'idCount': len(ids), 'countReturned': len(features),
                'trueOverlapCount': None, 'datasetCoverage': 'known_national_register' if service == 'vern' else 'unknown',
                'planSurveyCoverage': 'unknown',
                'coverageCandidatesReturned': len(features) if layer == 1 and service == 'naturtyper_nin' else None,
                'paging': {'method':'returnIdsOnly, then objectIds batches of 100', 'batches':len(queries), 'exceededTransferLimit':truncation, 'completeForQuery':complete},
                'idsQueryUrl': ids_url, 'countQueryUrl': count_url, 'featureQueryUrls': queries,
                'rawPrefix': 'research/natur/raw/'+stem,
                'records': [record(f['attributes']) for f in features]})
            print(plan['id'], service, layer, 'returned:',len(features), 'complete:',complete)
            if not complete:
                raise RuntimeError('Incomplete query result')
    (OUT/'gis-screening.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')

if __name__ == '__main__':
    main()
