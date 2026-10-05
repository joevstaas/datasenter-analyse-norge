'use client';
import {useState} from 'react';
import AtlasView from '@/components/atlas';
import {BASE} from '@/lib/model';
import styles from './preview.module.css';
export default function DesignPreview(){
 const [direction,setDirection]=useState<'nature'|'observatory'>('nature');
 return <div className={`${styles.preview} ${styles[direction]}`}>
  <nav className={styles.reviewbar} aria-label="Sammenlign designutkast">
   <span className={styles.reviewlabel}>Designstudie <small>To retninger · samme data</small></span>
   <div className={styles.choices}>
    <button aria-pressed={direction==='nature'} onClick={()=>setDirection('nature')}>A <span>Rolig naturatlas</span></button>
    <button aria-pressed={direction==='observatory'} onClick={()=>setDirection('observatory')}>B <span>Presist observatorium</span></button>
   </div>
   <a href={BASE}>Dagens app ↗</a>
  </nav>
  <AtlasView/>
 </div>;
}
