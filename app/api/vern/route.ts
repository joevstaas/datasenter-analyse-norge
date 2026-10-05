// A fixed public upstream: no arbitrary URL proxy or credentials.
const SERVICE='https://kart.miljodirektoratet.no/arcgis/rest/services/vern/MapServer';
export async function GET(req:Request){
 const b=new URL(req.url).searchParams.get('bbox')?.split(',').map(Number);
 if(!b||b.length!==4||b.some(v=>!Number.isFinite(v))||b[0]<-20037509||b[1]<-20037509||b[2]>20037509||b[3]>20037509||b[0]>=b[2]||b[1]>=b[3])return new Response('Invalid bbox',{status:400});
 const q=new URLSearchParams({bbox:b.join(','),bboxSR:'3857',imageSR:'3857',size:'256,256',format:'png32',transparent:'true',layers:'show:0',f:'image'});
 try {const r=await fetch(`${SERVICE}/export?${q}`,{signal:AbortSignal.timeout(15000),next:{revalidate:86400}});if(!r.ok||!r.headers.get('content-type')?.includes('image/'))throw new Error();return new Response(await r.arrayBuffer(),{headers:{'Content-Type':'image/png','Cache-Control':'public, max-age=3600, s-maxage=86400','X-Data-Source':'Miljodirektoratet Naturbase; live cartographic context, not impact analysis'}});}catch{return new Response('Naturbase er midlertidig utilgjengelig',{status:502});}
}
