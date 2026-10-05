'use client';
import {useEffect,useRef,useState} from 'react';
import Link from 'next/link';
import {ArrowRight,Check,X,Flame,Share2,Download,Copy,RotateCcw,ExternalLink,ArrowLeft} from 'lucide-react';
import {BASE} from '@/lib/model';
import {QUIZ_LENGTH,REPORT,allQuestions,drawQuiz,rank,shareCode,shareText,type Question} from '@/lib/quiz';

type Phase='intro'|'playing'|'result';
const LETTERS=['A','B','C'];

export default function QuizGame(){
 const [phase,setPhase]=useState<Phase>('intro');
 const [questions,setQuestions]=useState<Question[]>([]);
 const [index,setIndex]=useState(0);
 const [picked,setPicked]=useState<string|null>(null);
 const [score,setScore]=useState(0);
 const [streak,setStreak]=useState(0);
 const [results,setResults]=useState<boolean[]>([]);
 const [seen,setSeen]=useState<string[]>([]);
 const next=useRef<HTMLButtonElement>(null);
 const heading=useRef<HTMLHeadingElement>(null);
 const q=questions[index];
 const answered=picked!==null;

 useEffect(()=>{if(answered)next.current?.focus();},[answered]);
 useEffect(()=>{if(phase!=='intro')heading.current?.focus();},[phase,index]);

 function start(){
  const set=drawQuiz(QUIZ_LENGTH,seen);
  setQuestions(set);setSeen(set.map(x=>x.id));setIndex(0);setPicked(null);setScore(0);setStreak(0);setResults([]);setPhase('playing');
  window.scrollTo({top:0});
 }
 function answer(key:string){
  if(answered||!q)return;
  const ok=key===q.correctKey;
  setPicked(key);setResults(r=>[...r,ok]);
  if(ok){setScore(s=>s+1);setStreak(s=>s+1);}else setStreak(0);
 }
 function advance(){
  if(index+1>=questions.length){setPhase('result');window.scrollTo({top:0});return;}
  setIndex(i=>i+1);setPicked(null);
 }

 if(phase==='intro')return <Intro onStart={start}/>;
 if(phase==='result')return <Result questions={questions} results={results} score={score} onRestart={start}/>;
 if(!q)return null;
 const correct=picked===q.correctKey;
 return <section className="qz-card" aria-labelledby="qz-question">
  <div className="qz-top">
   <span className="qz-count">Spørsmål {index+1} av {questions.length}</span>
   <span className="qz-score" aria-live="polite">Poeng: <strong>{score}</strong>{streak>=2&&<span className="qz-streak"><Flame size={14}/>{streak} på rad</span>}</span>
  </div>
  <div className="qz-progress" role="progressbar" aria-valuemin={0} aria-valuemax={questions.length} aria-valuenow={index+(answered?1:0)} aria-label="Fremdrift"><div style={{width:`${(index+(answered?1:0))/questions.length*100}%`}}/></div>
  <h2 id="qz-question" ref={heading} tabIndex={-1}>{q.question}</h2>
  <div className="qz-options" role="group" aria-label="Svaralternativer">
   {q.options.map((o,i)=>{
    const state=!answered?'':o.key===q.correctKey?'right':o.key===picked?'wrong':'dim';
    return <button key={o.key} className={'qz-option '+state} disabled={answered} onClick={()=>answer(o.key)} aria-pressed={picked===o.key}>
     <span className="qz-letter">{state==='right'?<Check size={16}/>:state==='wrong'?<X size={16}/>:LETTERS[i]}</span>
     <span>{o.text}</span>
    </button>;
   })}
  </div>
  {answered&&<div className={'qz-feedback '+(correct?'ok':'no')} role="status">
   <p className="qz-verdict">{correct?'Riktig! +1 poeng':'Ikke helt. Riktig svar er markert i grønt.'}</p>
   <p>{q.explanation}</p>
   <p className="qz-source">Kilde: {REPORT.publisher} 2026, side {q.page}. {q.chapter}</p>
   <button ref={next} className="qz-primary" onClick={advance}>{index+1>=questions.length?'Se resultatet':'Neste spørsmål'} <ArrowRight size={16}/></button>
  </div>}
 </section>;
}

function Intro({onStart}:{onStart:()=>void}){
 return <section className="qz-card qz-intro">
  <p className="eyebrow">QUIZ · DATASENTRE I NORGE</p>
  <h1>Hvor mye vet du om <em>datasentre?</em></h1>
  <p className="qz-lead">{QUIZ_LENGTH} tilfeldige spørsmål om strøm, vann, varme og regelverk. Du får poeng for hvert riktig svar, og forklaring med sidehenvisning etter hvert spørsmål. Alt er hentet fra Teknologirådets rapport «{REPORT.title}» ({REPORT.year}).</p>
  <ul className="qz-facts"><li><strong>{QUIZ_LENGTH}</strong> spørsmål av {allQuestions.length}, nye hver gang</li><li><strong>~3</strong> minutter</li><li><strong>Del</strong> resultatet og lær bort noe</li></ul>
  <button className="qz-primary big" onClick={onStart}>Start quizen <ArrowRight size={18}/></button>
 </section>;
}

function Result({questions,results,score,onRestart}:{questions:Question[];results:boolean[];score:number;onRestart:()=>void}){
 const r=rank(score);
 const correct=questions.filter((_,i)=>results[i]);
 const pool=correct.length?correct:questions;
 const [factQ]=useState(()=>pool[Math.floor(Math.random()*pool.length)]);
 const code=shareCode(score,allQuestions.findIndex(x=>x.id===factQ.id));
 return <section className="qz-card qz-result" aria-labelledby="qz-result-title">
  <p className="eyebrow">RESULTAT</p>
  <div className="qz-big"><strong>{score}</strong><span>/{questions.length}</span></div>
  <h1 id="qz-result-title" tabIndex={-1}>{r.title}</h1>
  <p className="qz-lead">{r.line}</p>
  <SharePanel score={score} code={code}/>
  <div className="qz-actions"><button className="qz-primary" onClick={onRestart}><RotateCcw size={16}/> Prøv igjen med nye spørsmål</button><Link className="qz-secondary" href="/"><ArrowLeft size={16}/> Utforsk datasentrene på kartet</Link></div>
  <h2 className="qz-sub">Gå gjennom svarene</h2>
  <ol className="qz-review">{questions.map((x,i)=><li key={x.id} className={results[i]?'ok':'no'}><span className="qz-mark">{results[i]?<Check size={14}/>:<X size={14}/>}</span><div><strong>{x.question}</strong><p>{x.options.find(o=>o.key===x.correctKey)?.text}</p><small>Side {x.page} i rapporten</small></div></li>)}</ol>
 </section>;
}

function SharePanel({score,code}:{score:number;code:string}){
 const [copied,setCopied]=useState(false);
 const [canShare,setCanShare]=useState(false);
 const [busy,setBusy]=useState(false);
 const [origin,setOrigin]=useState('');
 useEffect(()=>{setCanShare(typeof navigator.share==='function');setOrigin(window.location.origin);},[]);
 const path=`${BASE}/quiz/del/${code}`;
 const url=()=>`${origin||window.location.origin}${path}`;
 const imageUrl=`${path}/portrett`;
 const text=shareText(score);

 async function nativeShare(){
  setBusy(true);
  try{
   const data:ShareData={title:'Quiz: datasentre i Norge',text,url:url()};
   try{
    const blob=await (await fetch(imageUrl)).blob();
    const file=new File([blob],'datasenter-quiz.png',{type:'image/png'});
    if(navigator.canShare?.({files:[file]}))data.files=[file];
   }catch{/* share without picture */}
   await navigator.share(data);
  }catch{/* cancelled */}finally{setBusy(false);}
 }
 async function copy(){
  try{await navigator.clipboard.writeText(`${text} ${url()}`);setCopied(true);setTimeout(()=>setCopied(false),2500);}catch{window.prompt('Kopier teksten:',`${text} ${url()}`);}
 }
 return <div className="qz-share">
  <h2 className="qz-sub">Del resultatet og lær bort noe</h2>
  <p className="qz-share-lead">Bildet viser poengene dine og ett overraskende faktum med kilde. Mottakerne kan ta quizen selv.</p>
  <div className="qz-share-body">
   {/* eslint-disable-next-line @next/next/no-img-element */}
   <img className="qz-preview" src={imageUrl} alt={`Delebilde: ${score} av ${QUIZ_LENGTH} riktige i quizen om datasentre i Norge`} width={1080} height={1350}/>
   <div className="qz-share-buttons">
    {canShare&&<button className="qz-primary" onClick={nativeShare} disabled={busy}><Share2 size={16}/> Del bilde og lenke</button>}
    {origin&&<a className="qz-secondary" target="_blank" rel="noreferrer" href={`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(origin+path)}`}><ExternalLink size={16}/> Del på LinkedIn</a>}
    <a className="qz-secondary" href={imageUrl} download={`datasenter-quiz-${score}-av-${QUIZ_LENGTH}.png`}><Download size={16}/> Last ned bilde (Instagram)</a>
    <button className="qz-secondary" onClick={copy}><Copy size={16}/> {copied?'Kopiert!':'Kopier tekst og lenke'}</button>
    <p className="qz-hint">Instagram har ikke lenkedeling fra nettsider: last ned bildet og legg lenken i bildeteksten eller i story.</p>
   </div>
  </div>
 </div>;
}
