"""Check provenance, retained baseline, and unknown-value semantics after report enrichment."""
import hashlib
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
claims=load('research/pastander.json'); projects=load('research/prosjekter.json')
for data,items in [(claims,claims['claims']),(projects,[c for p in projects['projects'] for c in p['claims']])]:
 ids=[s['id'] for s in data['sources']]
 assert len(ids)==len(set(ids))
 for c in items: assert set(c['sourceIds']) <= set(ids)
 assert next(s for s in data['sources'] if s['id']=='tr-report-2026-10')['sha256']==hashlib.sha256((R/'report/Datasentre-i-Norge.pdf').read_bytes()).hexdigest()
old=load('research/history/2026-10-01/prosjekter.json')
for p in projects['projects']:
 before=next(a for a in old['projects'] if a['id']==p['id'])
 assert before['geometry']==p['geometry']
 if p['id'] in {'undheim','gromstul'}:
  co=p['coordinates'];assert before['coordinates'] is None
  assert co['reviewedAt']=='2026-10-05' and co['kind']=='address_point'
  assert set(co['sourceIds']) <= {s['id'] for s in projects['sources']}
  raw=load(co['rawFile'])['adresser'];assert len(raw)==1
  a=raw[0];assert co['lat']==a['representasjonspunkt']['lat'] and co['lon']==a['representasjonspunkt']['lon']
  assert co['crs']==a['representasjonspunkt']['epsg'] and co['address']==a['adressetekst']
  assert co['confidenceInterval'] is None and co['accuracyMetres'] is None
 else:assert before['coordinates']==p['coordinates']
 assert all(c in p['claims'] for c in before['claims']), 'Historical claim lost'
 for c in p['claims']:
  if c.get('addedIn')=='2026-10-05-report-review':
   assert not c['publishAsFact'] and c['sourceLocators'] and c['confidenceInterval'] is None
nature=load('research/natur/naturkort.json'); src={s['id'] for s in nature['sources']}
water=load('research/natur/vann-og-folgeinngrep.json')
assert {p['projectId'] for p in water['projects']}=={'gromstul','hamar','narvik'}
for p in water['projects']:
 assert set(p['sourceIds'])<=src
 assert p['quantityStatus']=='not_obtained' and all(v is None for v in p['quantities'].values())
 assert p['gaps'] and p['nextEvidence'] and p['scope']
assert all(c['screening']['actualHabitatLossM2'] is None for c in nature['cards'])
print(json.dumps({'status':'passed','claims':len(claims['claims']),'projects':len(projects['projects']),'projectClaims':sum(len(p['claims']) for p in projects['projects']),'waterPilots':len(water['projects']),'baseline':'Earlier claims and geometry retained; two documented address points added, six unchanged','scope':'Structural and historical integrity; no ecological or independent national-data validation'},ensure_ascii=False,indent=2))
