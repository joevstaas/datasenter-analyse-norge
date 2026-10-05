"""Apply the reviewed 2026-10-05 location correction, preserving all other rows.
Uses explicit before/after records and atomic per-dataset transactions; safe to rerun.
Follow with sync_odp_tables.py for complete read-back verification.
"""
import json
from shapely import wkt
from dotenv import dotenv_values
from odp.client import Client
from sync_odp_tables import R, read, build, normalize

def same(a,b):
 if a is None or b is None:return a is b
 for key,val in b.items():
  av=a.get(key)
  if key=='geometry' and val is not None:
   if av is None or not wkt.loads(val).equals(wkt.loads(av) if isinstance(av,str) else av):return False
  elif normalize(av)!=normalize(val):return False
 return True

def apply():
 patch=read('research/raw/location-review-2026-10-05/table-patch.json')
 cfg=read('config/odp-catalog.json');data=build()
 assert set(patch)=={'projects','sources'}
 assert {v['after']['project_id'] for v in patch['projects']}=={'undheim','gromstul'}
 assert all(v['before'] is None for v in patch['sources'])
 env=dotenv_values(R/'.env');assert env['ODP_API_BASE_URL'].rstrip('/')=='https://api.hubocean.earth'
 assert env['ODP_COLLECTION_ID']==cfg['collection']['id']
 client=Client(base_url=env['ODP_API_BASE_URL'],api_key=env['ODP_API_KEY'])
 # Sources first: new project references are resolvable when project rows commit.
 for key in ['sources','projects']:
  d=next(a for a in cfg['datasets'] if a['key']==key);ds=client.dataset(d['id'])
  schema,rows=data[key];assert ds.table.schema().equals(schema,check_metadata=True)
  desired={r['id']:r for r in rows}
  for change in patch[key]:assert same(desired[change['after']['id']],change['after'])
  current=[r for frame in ds.table.select().dataframes() for r in frame.to_dict('records')]
  by={r['id']:r for r in current};assert len(by)==len(current)
  pending=[]
  for change in patch[key]:
   rid=change['after']['id'];actual=by.get(rid)
   if same(actual,change['after']):continue
   assert same(actual,change['before']), 'Unexpected live state: '+key+'/'+rid
   pending.append(change)
  if pending:
   with ds as tx:
    for change in pending:
     rid=change['after']['id']
     removed=[r for frame in tx.replace(filter='id == $rid',vars={'rid':rid}).dataframes() for r in frame.to_dict('records')]
     assert len(removed)==(0 if change['before'] is None else 1), 'Concurrent change detected'
     if removed:assert same(removed[0],change['before']), 'Concurrent modification detected'
     tx.insert(change['after'])
  print(key,len(pending),'reviewed changes applied',flush=True)
if __name__=='__main__':
 try:apply()
 except Exception as e:
  print(str(e) if isinstance(e,AssertionError) else type(e).__name__)
  raise SystemExit(1)
