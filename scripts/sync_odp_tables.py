"""Create typed ODP tables from research, retain JSON snapshots, verify read-back.
Existing rows must match this release; never delete or overwrite a differing table.
"""
import json,uuid,datetime,math
from pathlib import Path
import pyarrow as pa
from pyproj import Transformer
from shapely.geometry import shape
from shapely import wkt
from dotenv import dotenv_values
from odp.client import Client
R=Path(__file__).resolve().parents[1]
NS=uuid.UUID('97f29d3a-9bbd-4bcc-ad93-c7b0d752dd33')
def read(p):return json.loads((R/p).read_text())
def j(x):return json.dumps(x,ensure_ascii=False,sort_keys=True)
def refs(scope,ids):return '; '.join(scope+':'+s for s in ids)
def row(key,**kw):return {'id':str(uuid.uuid5(NS,key)),**kw}
def field(name,kind,description,spatial=None):
 meta={'description':description+' NULL means unknown or not documented.'}
 if spatial:meta['class']=spatial
 if spatial=='geometry':meta.update(isGeometry='1',index='1')
 return pa.field(name,kind,nullable=name!='id',metadata=meta)
S=pa.string();F=pa.float64();B=pa.bool_();D=pa.date32()
def schema(spec):return pa.schema([field('id',S,'Stable UUID primary key.')]+[field(*a) for a in spec])
G=('geometry',S,'WGS84 WKT, longitude first. Address location only; not a footprint.','geometry')

def build():
 p=read('research/prosjekter.json');n=read('research/natur/naturkort.json');c=read('research/pastander.json');water=read('research/natur/vann-og-folgeinngrep.json')
 out={};transform=Transformer.from_crs(4258,4326,always_xy=True)
 points={};projects=[]
 for a in p['projects']:
  co=a.get('coordinates') or {};lon=lat=geom=None
  if co.get('lon') is not None:
   assert co['crs']=='EPSG:4258'
   lon,lat=transform.transform(co['lon'],co['lat']);geom=f'POINT ({lon} {lat})';points[a['id']]=geom
  projects.append(row('project:'+a['id'],project_id=a['id'],name=a['name'],municipality=a['municipality'],status=a['status'],status_verified=a['statusVerifiedAsCurrent'],longitude=lon,latitude=lat,geometry=geom,location_role=co.get('kind'),original_crs=co.get('crs'),location_sources=refs('projects',co.get('sourceIds',[])),location_uncertainty=co.get('reason'),knowledge_gaps='; '.join(a['gaps'])))
 out['projects']=(schema([('project_id',S,'Project join key.'),('name',S,'Project name.'),('municipality',S,'Municipality.'),('status',S,'Reported or historical project status; not proof of operation.'),('status_verified',B,'Whether status has been verified as current.'),('longitude',F,'WGS84 longitude, transformed from EPSG:4258.','longitude'),('latitude',F,'WGS84 latitude, transformed from EPSG:4258.','latitude'),G,('location_role',S,'Location role, e.g. address_point.'),('original_crs',S,'Original coordinate reference system.'),('location_sources',S,'Semicolon-separated source join keys.'),('location_uncertainty',S,'Location limitations and confidence rationale.'),('knowledge_gaps',S,'Known missing evidence.')]),projects)
 claims=[]
 for a in p['projects']:
  for i,v in enumerate(a['claims']):
   val=v['value'];num=float(val) if isinstance(val,(int,float)) and not isinstance(val,bool) else None
   claims.append(row('claim:'+a['id']+':'+str(i+1),project_id=a['id'],topic=v['field'],statement=str(val),numeric_value=num,unit=v.get('unit'),value_kind=v.get('kind'),reference_period=v.get('period'),source_keys=refs('projects',v['sourceIds']),source_locator=j(v.get('sourceLocators',{})),confidence=v.get('confidence'),assessment=v.get('verificationStatus',v.get('reason')),attributed_publication_allowed=v.get('publishAsFact'),details_json=j(v)))
 for v in c['claims']:
  claims.append(row('national:'+v['id'],project_id=None,topic=v['topic'],statement=v['claim'],numeric_value=None,unit=None,value_kind=v.get('claimType'),reference_period=v.get('referencePeriod'),source_keys=refs('national',v['sourceIds']),source_locator=v.get('locator') or j(v.get('sourceLocators',{})),confidence=j(v.get('uncertainty')),assessment=v['assessment'],attributed_publication_allowed=v['publishAsFact'],details_json=j(v)))
 out['claims']=(schema([('project_id',S,'Project join key; NULL for national claims.'),('topic',S,'Claim topic.'),('statement',S,'Claim text or source value.'),('numeric_value',F,'Numeric value only when source supplies a scalar. Never sum across kinds/periods.'),('unit',S,'Source unit; see value_kind.'),('value_kind',S,'Definition, such as IT capacity or reserved capacity.'),('reference_period',S,'Source period, preserved at original precision.'),('source_keys',S,'Semicolon-separated source join keys.'),('source_locator',S,'Page or section references.'),('confidence',S,'Qualitative evidence confidence; not a probability.'),('assessment',S,'Verification status or limitations.'),('attributed_publication_allowed',B,'Permission to display as attributed research claim, NOT independent verification.'),('details_json',S,'Complete original claim including conflicts and nested evidence.')]),claims)
 geos=[]
 for a in p['projects']:
  v=a.get('geometry') or {}
  if not v.get('coordinates'):continue
  geos.append(row('plan:'+a['id'],project_id=a['id'],name=a['name'],plan_id=v.get('planId'),geometry_role=v.get('kind'),source_crs=v.get('crs'),crs_confirmed=False,map_display_approved=False,source_wkt=shape(v).wkt,source_keys=refs('projects',v.get('sourceIds',[])),limitations=v.get('limitation'),actual_land_take_m2=None))
 out['geometries']=(schema([('project_id',S,'Project join key.'),('name',S,'Project name.'),('plan_id',S,'Municipal plan identifier.'),('geometry_role',S,'Regulatory plan extent, not actual land take.'),('source_crs',S,'Source CRS description; unconfirmed.'),('crs_confirmed',B,'Whether original CRS is verified.'),('map_display_approved',B,'Whether suitable for spatial publication.'),('source_wkt',S,'Unconfirmed source coordinates preserved as plain WKT TEXT; deliberately NOT classified as map geometry.'),('source_keys',S,'Source join keys.'),('limitations',S,'Geographic interpretation limits.'),('actual_land_take_m2',F,'Measured actual land take in square metres, currently unknown.')]),geos)
 nature=[]
 for card in n['cards']:
  for section in ['baseline','change','consequence','knowledge_gap']:
   for v in card[section]:nature.append(row('nature:'+v['id'],project_id=card['projectId'],section=section,statement=v['statement'],evidence_kind=v['evidenceKind'],reference_period=v.get('validTime'),reviewed_at=datetime.date.fromisoformat(card['review']['reviewedAt']),source_keys=refs('nature',v['sourceIds']),source_locator=v['locator'],confidence=v['uncertainty']['confidence'],limitations=v['uncertainty']['reason'],metric=None,numeric_value=None,unit=None,details_json=j(v)))
 for a in water['projects']:
  for key,val in a['quantities'].items():
   unit='m2' if key.endswith('M2') else 'degrees C' if key.endswith('C') else 'litre/kWh IT' if 'WUE' in key else 'm3/hour' if 'Hour' in key else 'm3/year'
   nature.append(row('water:'+a['projectId']+':'+key,project_id=a['projectId'],section='water_and_land_metrics',statement=a['documentedContext'],evidence_kind='knowledge_gap',reference_period=a['measurementPeriod'],reviewed_at=datetime.date.fromisoformat(a['reviewedAt']),source_keys=refs('nature',a['sourceIds']),source_locator='See source register and nature card',confidence='unknown',limitations=a['scope'],metric=key,numeric_value=val,unit=unit,details_json=j(a)))
 out['nature_water']=(schema([('project_id',S,'Project join key; includes Narvik pilot not in main project register.'),('section',S,'Baseline, change, consequence, gap or metric.'),('statement',S,'Scoped statement.'),('evidence_kind',S,'Report finding, authority statement, spatial screening or gap.'),('reference_period',S,'Original observation/report period.'),('reviewed_at',D,'Date of desk review, not measurement date.'),('source_keys',S,'Source join keys.'),('source_locator',S,'Page/section.'),('confidence',S,'Qualitative evidence confidence.'),('limitations',S,'Scope and uncertainty.'),('metric',S,'Metric identifier; NULL for narrative findings.'),('numeric_value',F,'Documented measured value; missing is never zero.'),('unit',S,'Metric unit.'),('details_json',S,'Complete source finding or water record.')]),nature)
 sources=[]
 for scope,values in [('projects',p['sources']),('national',c['sources']),('nature',n['sources'])]:
  for v in values:sources.append(row('source:'+scope+':'+v['id'],source_key=scope+':'+v['id'],record_kind='source',title=v['title'],publisher=v.get('publisher'),url=v.get('url'),published_at=v.get('publishedAt'),document_date=v.get('documentDate'),accessed_at=v.get('accessedAt',v.get('retrievedAt')),locator=v.get('locator'),content=j(v)))
 for path in ['docs/datametode.md','docs/naturmetode.md','research/rapportoppdatering-2026-10-05.md']:
  sources.append(row('method:'+path,source_key='method:'+path,record_kind='method_document',title=path,publisher='Project research team',url=None,published_at=None,document_date=None,accessed_at=None,locator=path,content=(R/path).read_text()))
 out['sources']=(schema([('source_key',S,'Namespaced source join key.'),('record_kind',S,'source or method_document.'),('title',S,'Source title.'),('publisher',S,'Source publisher, not necessarily independent.'),('url',S,'Original source URL.'),('published_at',S,'Publication date at original precision; not ingestion date.'),('document_date',S,'Document date at original precision.'),('accessed_at',S,'Source access date.'),('locator',S,'Page or file reference.'),('content',S,'Full source metadata or project methodology text.')]),sources)
 return out

def normalize(v):
 if v is None:return None
 if isinstance(v,float) and math.isnan(v):return None
 if hasattr(v,'isoformat'):return v.isoformat()[:10]
 if hasattr(v,'item'):return v.item()
 return v

def main():
 cfg=read('config/odp-catalog.json');data=build()
 for key,(sc,rows) in data.items():
  pa.Table.from_pylist(rows,schema=sc)
  assert len({r['id'] for r in rows})==len(rows)
  assert all(f.metadata.get(b'description') for f in sc)
 if '--check' in __import__('sys').argv:
  print({k:len(v[1]) for k,v in data.items()});return
 env=dotenv_values(R/'.env');assert env['ODP_API_BASE_URL'].rstrip('/')=='https://api.hubocean.earth'
 client=Client(api_key=env['ODP_API_KEY'])
 for d in cfg['datasets']:
  sc,rows=data[d['key']];ds=client.dataset(d['id']);existing=ds.table.schema()
  if existing is None:ds.table.create(sc)
  else:
   assert existing.equals(sc,check_metadata=True), 'Existing schema differs: '+d['key']
  fetched=[r for frame in ds.table.select().dataframes() for r in frame.to_dict('records')]
  if not fetched:
   with ds as tx:tx.insert(rows)
   fetched=[r for frame in ds.table.select().dataframes() for r in frame.to_dict('records')]
  by={r['id']:r for r in fetched};assert len(by)==len(rows)==len(fetched)
  for expected in rows:
   actual=by[expected['id']]
   for key,val in expected.items():
    av=actual.get(key)
    if key=='geometry' and val is not None:
     assert wkt.loads(val).equals(wkt.loads(av) if isinstance(av,str) else av)
    else:assert normalize(av)==normalize(val), f'Value mismatch {d["key"]}/{key}'
  returned=ds.table.schema()
  for f in sc:assert returned.field(f.name).metadata==f.metadata
  d['table']={'status':'typed_table_readback_verified','rows':len(rows),'columns':len(sc),'geometryPolicy':'EPSG:4258 address points transformed to WGS84; unconfirmed plan WKT kept non-spatial.','schema':[{'name':f.name,'type':str(f.type),'metadata':{k.decode():v.decode() for k,v in f.metadata.items()}} for f in sc]}
  (R/'config/odp-catalog.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
  print(d['key'],len(rows),'rows verified',flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  print(str(e) if isinstance(e,AssertionError) else type(e).__name__)
  raise SystemExit(1)
