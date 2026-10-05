'use client';
import {useEffect,useRef,useState} from 'react';
import {NatureControls,NatureFacts,type NatureResult} from './nature-controls';
import {natureLayers,natureLayerKeys,type NatureLayer} from '@/lib/nature-layers';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import {BASE,coordinates,type Row} from '@/lib/model';
export default function Map({projects,selected,onSelect,nature,reset}:{projects:Row[];selected:string;onSelect:(id:string)=>void;nature:boolean;reset:number}){
 const container=useRef<HTMLDivElement>(null),map=useRef<mapboxgl.Map|null>(null),markers=useRef<mapboxgl.Marker[]>([]),callback=useRef(onSelect);
 const [ready,setReady]=useState(false),[error,setError]=useState(''),[natureError,setNatureError]=useState(false),[backup,setBackup]=useState(false);
 const [enabled,setEnabled]=useState<NatureLayer[]>([]),[zoom,setZoom]=useState(4.5),[layerErrors,setLayerErrors]=useState<NatureLayer[]>([]),[facts,setFacts]=useState<NatureResult[]|null>(null),[factsLoading,setFactsLoading]=useState(false);
 const enabledRef=useRef(enabled),query=useRef<AbortController|null>(null);enabledRef.current=enabled;
 const changeLayers=(v:NatureLayer[])=>{query.current?.abort();setFacts(null);setEnabled(v);setLayerErrors([]);};
 const useBackup=()=>{if(!map.current)return;setReady(false);setError('');setBackup(true);map.current.setStyle({version:8,sources:{kartverket:{type:'raster',tiles:['https://cache.kartverket.no/v1/wmts/1.0.0/topograatone/default/webmercator/{z}/{y}/{x}.png'],tileSize:256,maxzoom:18,attribution:'© Kartverket'}},layers:[{id:'background',type:'background',paint:{'background-color':'#e5eae2'}},{id:'kartverket',type:'raster',source:'kartverket'}]});};
 callback.current=onSelect;
 useEffect(()=>{
 const token=process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN;
 if(!token?.startsWith('pk.')){setError('Kartet mangler en gyldig offentlig Mapbox-token. Prosjektlisten og kildene er fortsatt tilgjengelige.');return;}
 if(!container.current)return;
 let m:mapboxgl.Map;
 try{m=new mapboxgl.Map({container:container.current,accessToken:token,style:'mapbox://styles/mapbox/light-v11',center:[9,61],zoom:4.5,minZoom:3,maxZoom:17,attributionControl:true});}catch{setError('Nettleseren kunne ikke starte kartet. Bruk prosjektlisten for å utforske dataene.');return;}
 map.current=m;m.addControl(new mapboxgl.NavigationControl({showCompass:false}),'bottom-right');
 const timeout=setTimeout(()=>{if(!m.isStyleLoaded())setError('Kartet bruker lang tid på å laste. Kontroller nettforbindelse og Mapbox-tilgang.');},20000);
 m.on('style.load',()=>{clearTimeout(timeout);m.resize();setError('');m.addSource('vern',{type:'raster',tiles:[`${window.location.origin}${BASE}/api/vern?bbox={bbox-epsg-3857}`],tileSize:256,attribution:'Verneområder © Miljødirektoratet / Naturbase'});m.addLayer({id:'vern',type:'raster',source:'vern',paint:{'raster-opacity':0.58},layout:{visibility:'none'}});for(const key of natureLayerKeys){m.addSource(key,{type:'raster',tiles:[`${window.location.origin}${BASE}/api/natur?layer=${key}&bbox={bbox-epsg-3857}`],tileSize:256,attribution:'Naturtyper og dekning © Miljødirektoratet / Naturbase'});m.addLayer({id:key,type:'raster',source:key,minzoom:natureLayers[key].minzoom,paint:{'raster-opacity':0.7},layout:{visibility:'none'}});}setReady(true);});
 m.on('zoomend',()=>setZoom(m.getZoom()));
 m.on('click',async e=>{
 if((e.originalEvent.target as HTMLElement)?.closest('.map-marker'))return;
 const active=enabledRef.current.filter(k=>m.getZoom()>=natureLayers[k].minzoom);if(!active.length)return;
 query.current?.abort();const controller=new AbortController();query.current=controller;setFacts([]);setFactsLoading(true);
 const results=await Promise.all(active.map(async layer=>{try{const r=await fetch(`${BASE}/api/natur?mode=identify&layer=${layer}&point=${e.lngLat.lng},${e.lngLat.lat}`,{signal:controller.signal});if(!r.ok)throw new Error();return {layer,...await r.json()} as NatureResult;}catch{return {layer,features:[],error:true} as NatureResult;}}));
 if(!controller.signal.aborted){setFacts(results);setFactsLoading(false);}
 });
 m.on('error',e=>{const key=natureLayerKeys.find(k=>('sourceId' in e&&e.sourceId===k)||e.error.message.includes(`layer=${k}`));if(key){setLayerErrors(old=>old.includes(key)?old:[...old,key]);return;}if(('sourceId' in e && e.sourceId==='vern') || e.error.message.includes('/api/vern'))setNatureError(true);else setError('Basiskartet kunne ikke lastes fullstendig fra Mapbox. Kontroller tokenets rettigheter og tillatte domener. Adressepunkter og prosjektdata er fortsatt tilgjengelige.');});
 const observer=new ResizeObserver(()=>m.resize());observer.observe(container.current);
 return()=>{query.current?.abort();clearTimeout(timeout);observer.disconnect();markers.current.forEach(x=>x.remove());m.remove();map.current=null;};
 },[]);
 useEffect(()=>{if(!ready||!map.current)return;markers.current.forEach(m=>m.remove());markers.current=[];for(const p of projects){const c=coordinates(p);if(!c)continue;const b=document.createElement('button');b.className='map-marker'+(p.project_id===selected?' chosen':'');b.title=String(p.name)+' – adressepunkt';b.setAttribute('aria-label','Vis '+String(p.name));b.textContent='';b.onclick=()=>callback.current(String(p.project_id));markers.current.push(new mapboxgl.Marker({element:b}).setLngLat(c).addTo(map.current));}},[projects,selected,ready]);
 useEffect(()=>{if(!ready||!map.current)return;const p=projects.find(p=>p.project_id===selected);const c=p&&coordinates(p);if(c)map.current.flyTo({center:c,zoom:9,duration:window.matchMedia('(prefers-reduced-motion: reduce)').matches?0:1100});},[selected,ready]); // Filtering alone should not recenter the map.
 useEffect(()=>{if(ready&&map.current)for(const key of natureLayerKeys)map.current.setLayoutProperty(key,'visibility',enabled.includes(key)?'visible':'none');},[enabled,ready]);
 useEffect(()=>{if(ready&&map.current){setNatureError(false);map.current.setLayoutProperty('vern','visibility',nature?'visible':'none');}},[nature,ready]);
 useEffect(()=>{if(ready&&map.current)map.current.fitBounds([[4.3,57.7],[13,63.8]],{padding:55,duration:500});},[reset,ready]);
 return <div className="map-surface"><NatureControls enabled={enabled} onChange={changeLayers} zoom={zoom}/>{facts!==null&&<NatureFacts results={facts} loading={factsLoading} onClose={()=>{query.current?.abort();setFacts(null);}}/>}{layerErrors.some(k=>enabled.includes(k))&&<p className="nature-layer-error" role="alert">Kunne ikke laste {layerErrors.filter(k=>enabled.includes(k)).map(k=>natureLayers[k].name).join(", ")}. Manglende farge er ikke dokumentasjon på fravær av naturverdier.</p>}<div ref={container} style={{position:"absolute",inset:0,width:"100%",height:"100%"}} className="map-canvas" aria-label="Kart over datasenterprosjekter"/>{error&&<div className="map-error" role="status">{error}{!backup&&<button className="backup-button" onClick={useBackup}>Bruk Kartverkets basiskart</button>}</div>}{nature&&natureError&&<p className="map-error" role="status">Verneområdelaget kunne ikke lastes fullstendig. Fravær av farge betyr ikke fravær av vern.</p>}<div className="map-caption">○ Adressepunkter · ikke arealgrenser{backup&&<span>Basiskart: Kartverket · Kartmotor: Mapbox</span>}{nature&&<span>Verneområder: kontekst, ikke dokumentert påvirkning</span>}</div></div>;
}
