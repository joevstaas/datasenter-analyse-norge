"""Create/update the configured ODP draft datasets and verify versioned JSON files.
No visibility changes, publication, deletion, or third-party PDF uploads.
Run: python3 scripts/sync_odp.py (loads the project .env without logging values).
Requires odp-sdk, python-dotenv and requests.
"""
import hashlib
import json
import re
from pathlib import Path
import requests
from dotenv import dotenv_values
from odp.client import Client

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/'config/odp-catalog.json'
def read(path):return json.loads((ROOT/path).read_text())
def save(config):CONFIG.write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
def bundles():
    p=read('research/prosjekter.json'); c=read('research/pastander.json'); n=read('research/natur/naturkort.json')
    common={'release':'2026-10-05-r2','purpose':'AI-assisted demo only; not decision support','limitations':'Incomplete coverage and limited review. Unknown is not zero. Source file references may point to the research repository and are not all uploaded.'}
    return {
      'projects':{**common,'projects':[{k:v for k,v in a.items() if k not in ('claims','geometry')} for a in p['projects']],'sources':p['sources']},
      'claims':{**common,'projectClaims':[{'project_id':a['id'],'claim_id':f"{a['id']}-claim-{i+1}",**v} for a in p['projects'] for i,v in enumerate(a['claims'])],'projectSources':p['sources'],'nationalClaims':c},
      'geometries':{**common,'displayApproved':False,'reason':'Source plan CRS unconfirmed. Plan boundaries are not actual land take.','geojson':read('research/planomriss.geojson')},
      'nature_water':{**common,'natureCards':n,'waterAndInfrastructure':read('research/natur/vann-og-folgeinngrep.json')},
      'sources':{**common,'sourceRegisters':{'projects':p['sources'],'nationalClaims':c['sources'],'nature':n['sources']},'documentation':{s:(ROOT/s).read_text() for s in ['docs/datametode.md','docs/naturmetode.md','research/rapportoppdatering-2026-10-05.md']}}
    }
def main():
    env=dotenv_values(ROOT/'.env'); cfg=read('config/odp-catalog.json')
    assert env.get('ODP_API_KEY'), 'ODP_API_KEY missing'
    assert env.get('ODP_COLLECTION_ID')==cfg['collection']['id'], 'Collection ID mismatch'
    base=env.get('ODP_API_BASE_URL','https://api.hubocean.earth').rstrip('/')
    assert base=='https://api.hubocean.earth', 'Unexpected API host; refusing to send credentials'
    client=Client(base_url=base,api_key=env['ODP_API_KEY'])
    def api(method,path,payload=None):
        r=client._request(requests.Request(method,base+path,json=payload),retry=False)
        if not r.ok:raise RuntimeError(f'ODP {method} {path}: HTTP {r.status_code}')
        return r.json() if r.content else None
    cp='/api/catalog/v2/data-collections/'+cfg['collection']['id']
    initial=api('GET',cp)
    api('PUT',cp,{k:cfg['collection'][k] for k in ['name','description']})
    listed=api('GET','/api/catalog/v2/datasets')
    payloads=bundles()
    for ds in cfg['datasets']:
        if not ds['id']:
            matches=[d for d in listed if d.get('name')==ds['name']]
            if len(matches)>1:raise RuntimeError('Ambiguous existing dataset name: '+ds['key'])
            if matches:ds['id']=matches[0]['id']
            else:
                created=api('POST','/api/catalog/v2/datasets',{'name':ds['name'],'description':ds['description']})
                ds['id']=created['id']
            save(cfg) # persist ID before linking/uploading; safe restart after interruption
        api('PATCH','/api/catalog/v2/datasets/'+ds['id']+'/metadata/general',{'name':ds['name'],'description':ds['description'],'tags':['Norway','data-centres','AI-assisted','demo']})
        collection=api('GET',cp)
        if ds['id'] not in {d['id'] for d in (collection.get('datasets') or [])}:
            api('POST',cp+'/datasets/'+ds['id'])
        content=(json.dumps(payloads[ds['key']],ensure_ascii=False,indent=2)+'\n').encode()
        digest=hashlib.sha256(content).hexdigest();name=ds['key']+'-2026-10-05-r2-'+digest[:12]+'.json'
        target=client.dataset(ds['id']);files=list(target.files.list())
        match=next((f for f in files if f['name']==name),None)
        if not match:
            target.files.upload(name,content)
            match=next(f for f in target.files.list() if f['name']==name)
        response=target.files.download(match['id'])
        downloaded=response.read() if hasattr(response,'read') else response
        assert hashlib.sha256(downloaded).hexdigest()==digest, 'Read-back checksum mismatch'
        state=api('GET','/api/catalog/v2/datasets/'+ds['id'])
        ds.update(status='uploaded_readback_verified',file={'id':match['id'],'name':name,'sha256':digest},visibility=state.get('visibility'),publishStatus=state.get('publish_status'))
        save(cfg)
        print(ds['key']+': uploaded and checksum verified')
    final=api('GET',cp)
    assert final['name']==cfg['collection']['name'] and final['description']==cfg['collection']['description']
    assert {d['id'] for d in cfg['datasets']}<={d['id'] for d in final['datasets']}
    assert final.get('visibility')==initial.get('visibility'), 'Unexpected visibility change'
    cfg['collection'].update(remoteMetadataStatus='verified',visibility=final.get('visibility'),accessNote='Authenticated catalog access and child dataset membership verified.')
    save(cfg)
    text=(ROOT/'.env').read_text()
    for ds in cfg['datasets']:
        key='ODP_'+ds['key'].upper()+'_DATASET_ID'
        text=re.sub(r'^'+re.escape(key)+r'=.*$',lambda m:key+'='+ds['id'],text,flags=re.M)
    (ROOT/'.env').write_text(text)
    print('Collection metadata and five datasets verified; dataset IDs saved to .env. No public publication requested.')
if __name__=='__main__':
    try:main()
    except Exception as e:
        # Avoid SDK tracebacks that could include signed URLs or request details.
        print('Sync stopped:',str(e) if isinstance(e,(RuntimeError,AssertionError)) else type(e).__name__)
        raise SystemExit(1)
