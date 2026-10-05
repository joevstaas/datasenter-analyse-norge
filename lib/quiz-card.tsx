import {ImageResponse} from 'next/og';
import {QUIZ_LENGTH, REPORT, rank, type Question} from '@/lib/quiz';

const ink = '#183c39';
const muted = '#647672';
const green = '#35694d';
const lime = '#dce8bf';
const paper = '#f8f9f4';

/** Three wave bars, drawn with boxes so no special font glyph is needed. */
function Mark({size}: {size: number}) {
  const bar = {display: 'flex', height: size / 6, background: green, borderRadius: size / 12} as const;
  return (
    <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between', width: size, height: size * 0.7, marginRight: 16}}>
      <div style={{...bar, width: size}} />
      <div style={{...bar, width: size * 0.8}} />
      <div style={{...bar, width: size}} />
    </div>
  );
}

export const CARD_LANDSCAPE = {width: 1200, height: 630};
export const CARD_PORTRAIT = {width: 1080, height: 1350};

/**
 * Share picture. Landscape fits link previews (LinkedIn, Facebook, X),
 * portrait fits Instagram posts and stories.
 */
export function quizCard(score: number, fact: Question, size: {width: number; height: number}) {
  const portrait = size.height > size.width;
  const pad = portrait ? 80 : 56;
  const r = rank(score);
  const pct = score / QUIZ_LENGTH;

  return new ImageResponse(
    (
      <div style={{width: '100%', height: '100%', display: 'flex', flexDirection: 'column', background: paper, color: ink, padding: pad, justifyContent: 'space-between'}}>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: portrait ? 28 : 22, letterSpacing: 4, fontWeight: 700}}>
          <div style={{display: 'flex', alignItems: 'center'}}>
            <Mark size={portrait ? 44 : 34} />
            <span>OCEAN DATA JO</span>
            <span style={{color: muted, fontWeight: 400, marginLeft: 12}}>/ LABS</span>
          </div>
        </div>

        <div style={{display: 'flex', flexDirection: portrait ? 'column' : 'row', alignItems: portrait ? 'flex-start' : 'center', gap: portrait ? 40 : 56}}>
          <div style={{display: 'flex', flexDirection: 'column'}}>
            <div style={{display: 'flex', fontSize: portrait ? 30 : 22, letterSpacing: 3, color: green, fontWeight: 700}}>QUIZ · DATASENTRE I NORGE</div>
            <div style={{display: 'flex', alignItems: 'baseline', marginTop: 8}}>
              <span style={{fontSize: portrait ? 300 : 210, fontWeight: 700, lineHeight: 1, letterSpacing: -8}}>{score}</span>
              <span style={{fontSize: portrait ? 120 : 84, color: muted, marginLeft: 8}}>/{QUIZ_LENGTH}</span>
            </div>
            <div style={{display: 'flex', width: portrait ? 560 : 400, height: 14, background: '#e3e8dd', borderRadius: 7, marginTop: 12}}>
              <div style={{display: 'flex', width: `${pct * 100}%`, height: 14, background: green, borderRadius: 7}} />
            </div>
            <div style={{display: 'flex', fontSize: portrait ? 56 : 40, fontWeight: 700, marginTop: 28}}>{r.title}</div>
          </div>

          <div style={{display: 'flex', flexDirection: 'column', flex: portrait ? 'none' : 1, alignSelf: portrait ? 'stretch' : 'auto', background: lime, padding: portrait ? 44 : 36, borderRadius: 8}}>
            <div style={{display: 'flex', fontSize: portrait ? 26 : 20, letterSpacing: 3, fontWeight: 700, color: green}}>VISSTE DU AT …</div>
            <div style={{display: 'flex', fontSize: portrait ? 46 : 32, lineHeight: 1.3, marginTop: 14, fontWeight: 600}}>{fact.fact}</div>
            <div style={{display: 'flex', fontSize: portrait ? 24 : 18, color: '#4d6155', marginTop: 20}}>
              Kilde: {REPORT.publisher} 2026, side {fact.page.replace('–', ' – ')}
            </div>
          </div>
        </div>

        <div style={{display: 'flex', flexDirection: portrait ? 'column' : 'row', justifyContent: 'space-between', alignItems: portrait ? 'flex-start' : 'center', fontSize: portrait ? 34 : 22}}>
          <div style={{display: 'flex', fontWeight: 700}}>Hvor mye vet du om datasentre? Ta quizen selv.</div>
          <div style={{display: 'flex', color: muted, marginTop: portrait ? 8 : 0}}>oceandatajo.com/labs</div>
        </div>
      </div>
    ),
    {...size},
  );
}

/** Generic picture for the quiz start page when no result is shared. */
export function quizIntroCard(size: {width: number; height: number}) {
  return new ImageResponse(
    (
      <div style={{width: '100%', height: '100%', display: 'flex', flexDirection: 'column', background: paper, color: ink, padding: 64, justifyContent: 'space-between'}}>
        <div style={{display: 'flex', alignItems: 'center', fontSize: 22, letterSpacing: 4, fontWeight: 700}}>
          <Mark size={34} />
          <span>OCEAN DATA JO</span>
          <span style={{color: muted, fontWeight: 400, marginLeft: 12}}>/ LABS</span>
        </div>
        <div style={{display: 'flex', flexDirection: 'column'}}>
          <div style={{display: 'flex', fontSize: 24, letterSpacing: 3, color: green, fontWeight: 700}}>QUIZ</div>
          <div style={{display: 'flex', fontSize: 84, fontWeight: 700, lineHeight: 1.05, marginTop: 12, letterSpacing: -2}}>Hvor mye vet du om datasentre i Norge?</div>
          <div style={{display: 'flex', fontSize: 34, color: muted, marginTop: 24}}>10 spørsmål om strøm, vann og varme. Basert på rapport fra Teknologirådet.</div>
        </div>
        <div style={{display: 'flex', background: lime, alignSelf: 'flex-start', padding: '14px 28px', fontSize: 28, fontWeight: 700, borderRadius: 6}}>Ta quizen på 3 minutter</div>
      </div>
    ),
    {...size},
  );
}
