import {isNatureLayer,natureLayers,natureService} from '@/lib/nature-layers';
export async function GET(req:Request){
 const p=new URL(req.url).searchParams,key=p.get('layer');
 if(!isNatureLayer(key))return new Response('Unknown layer',{status:400});
 const layer=natureLayers[key],base=natureService(key),mode=p.get('mode')||'tile';
 let url:string;
 if(mode==='identify'){
  const point=p.get('point')?.split(',').map(Number);
  if(!point||point.length!==2||point.some(n=>!Number.isFinite(n))||Math.abs(point[0])>180||Math.abs(point[1])>85)return new Response('Invalid point',{status:400});
  const q=new URLSearchParams({f:'json',geometry:point.join(','),geometryType:'esriGeometryPoint',inSR:'4326',spatialRel:'esriSpatialRelIntersects',outFields:layer.fields.join(','),returnGeometry:'false',resultRecordCount:'10'});
  url=`${base}/${layer.layer}/query?${q}`;
 }else if(mode==='legend'){url=`${base}/legend?f=json`;}
 else if(mode==='tile'){
  const b=p.get('bbox')?.split(',').map(Number);
  if(!b||b.length!==4||b.some(v=>!Number.isFinite(v))||b.some(v=>Math.abs(v)>20037509)||b[0]>=b[2]||b[1]>=b[3])return new Response('Invalid bbox',{status:400});
  const q=new URLSearchParams({bbox:b.join(','),bboxSR:'3857',imageSR:'3857',size:'256,256',format:'png32',transparent:'true',layers:`show:${layer.layer}`,f:'image'});
  url=`${base}/export?${q}`;
 }else return new Response('Unknown mode',{status:400});
 try{
  const r=await fetch(url,{signal:AbortSignal.timeout(15000),next:{revalidate:86400}});
  if(!r.ok)throw new Error();
  const headers={'Cache-Control':'public, max-age=3600, s-maxage=86400'};
  if(mode==='tile'){
   if(!r.headers.get('content-type')?.includes('image/'))throw new Error();
   return new Response(await r.arrayBuffer(),{headers:{...headers,'Content-Type':'image/png'}});
  }
  const data=await r.json();if(data.error)throw new Error();
  if(mode==='legend')return Response.json({legend:data.layers?.find((l:{layerId:number})=>l.layerId===layer.layer)?.legend??[]},{headers});
  const metaResponse=await fetch(`${base}/${layer.layer}?f=json`,{signal:AbortSignal.timeout(10000),next:{revalidate:86400}});
  if(!metaResponse.ok)throw new Error();const meta=await metaResponse.json();if(meta.error||!Array.isArray(meta.fields))throw new Error();
  const features=(data.features??[]).map((f:{attributes:Record<string,unknown>})=>Object.fromEntries(Object.entries(f.attributes).map(([key,value])=>{
   const field=meta.fields.find((x:{name:string})=>x.name===key);
   const label=field?.domain?.codedValues?.find((x:{code:unknown})=>x.code===value)?.name;
   return [field?.alias||key,label?`${label} (${value})`:value];
  })));
  return Response.json({features,truncated:!!data.exceededTransferLimit,source:`${base}/${layer.layer}`,retrievedAt:new Date().toISOString()},{headers});
 }catch{return new Response('Naturbase er midlertidig utilgjengelig',{status:502});}
}
