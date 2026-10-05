import 'server-only';
import { tableFromIPC } from 'apache-arrow';
import catalog from '@/config/odp-catalog.json';
import type { Atlas, Row } from './model';
import { coordinates, sourceKeys } from './model';
// Release-bound queries fail closed on partial responses or unexpected row counts.
// This prevents displaying an incomplete cursor response as a complete dataset.
export async function readTable(key: string): Promise<Row[]> {
 const d=catalog.datasets.find(d=>d.key===key);
 if(!d?.id || !process.env.ODP_API_KEY)throw new Error('ODP_CONFIGURATION_MISSING');
 const base=process.env.ODP_API_BASE_URL||'https://api.hubocean.earth';
 if(base!=='https://api.hubocean.earth')throw new Error('ODP_UNEXPECTED_HOST');
 const res=await fetch(`${base}/api/table/v2/sdk/select?table_id=${d.id}`,{method:'POST',headers:{Authorization:`ApiKey ${process.env.ODP_API_KEY}`,'Content-Type':'application/json'},body:JSON.stringify({query:null,cursor:'',timeout:20}),signal:AbortSignal.timeout(25000),cache:'no-store'});
 if(!res.ok)throw new Error(`ODP_HTTP_${res.status}`);
 let tab;
 try {tab=tableFromIPC(new Uint8Array(await res.arrayBuffer()));}catch{throw new Error('ODP_ARROW_DECODE');}
 const rows=Array.from(tab).map(r=>JSON.parse(JSON.stringify(r.toJSON(),(_,v)=>typeof v==='bigint'?Number(v):v)) as Row);
 if(rows.length!==d.table.rows || new Set(rows.map(r=>r.id)).size!==rows.length)throw new Error('ODP_RELEASE_MISMATCH');
 return rows;
}
let cached: {at:number;value:Atlas}|undefined;
let pending: Promise<Atlas>|undefined;
export async function loadAtlas(): Promise<Atlas> {
 if(cached && Date.now()-cached.at<300000)return cached.value;
 if(pending)return pending;
 pending=(async()=>{
 const [projects,claims,nature,sources]=await Promise.all(['projects','claims','nature_water','sources'].map(readTable));
 const keys=new Set(sources.map(s=>s.source_key));
 for(const r of [...claims,...nature])for(const id of sourceKeys(r.source_keys))if(!keys.has(id))throw new Error('ODP_MISSING_SOURCE');
 for(const p of projects){if(!coordinates(p))throw new Error('ODP_INVALID_COORDINATE');for(const id of sourceKeys(p.location_sources))if(!keys.has(id))throw new Error('ODP_MISSING_LOCATION_SOURCE');}
 const value:Atlas={projects,claims,nature,sources,release:'2026-10-05-r2',fetchedAt:new Date().toISOString(),origin:'ODP – typede tabeller'};
 cached={at:Date.now(),value};return value;
 })().finally(()=>{pending=undefined;});
 return pending;
}
