import type {Metadata} from 'next';
import Link from 'next/link';
import {notFound} from 'next/navigation';
import {ArrowRight} from 'lucide-react';
import {BASE} from '@/lib/model';
import {parseShareCode, QUIZ_LENGTH, rank, REPORT} from '@/lib/quiz';

type Props = {params: Promise<{code: string}>};

export async function generateMetadata({params}: Props): Promise<Metadata> {
  const shared = parseShareCode((await params).code);
  if (!shared) return {};
  const title = `Jeg fikk ${shared.score} av ${QUIZ_LENGTH} i quizen om datasentre i Norge`;
  const description = `Visste du at ${shared.fact.fact.charAt(0).toLowerCase()}${shared.fact.fact.slice(1)} Ta quizen og test hva du vet.`;
  return {title, description, openGraph: {title, description, type: 'website'}, twitter: {card: 'summary_large_image', title, description}};
}

export default async function SharedResult({params}: Props) {
  const {code} = await params;
  const shared = parseShareCode(code);
  if (!shared) notFound();
  const r = rank(shared.score);
  return (
    <main className="qz-page">
      <header className="qz-header"><Link href="/" className="qz-back">Til kartet</Link><span className="brand"><span className="brand-symbol">≋</span> OCEAN DATA JO <span className="labs">/ LABS</span></span></header>
      <section className="qz-card qz-result">
        <p className="eyebrow">NOEN HAR TATT QUIZEN</p>
        <div className="qz-big"><strong>{shared.score}</strong><span>/{QUIZ_LENGTH}</span></div>
        <h1>{r.title}</h1>
        <div className="qz-feedback ok" style={{marginTop: 20}}>
          <p className="qz-verdict">Visste du at …</p>
          <p>{shared.fact.fact}</p>
          <p className="qz-source">Kilde: {REPORT.publisher} 2026, side {shared.fact.page}. {REPORT.title}</p>
        </div>
        <p className="qz-lead">Kan du slå dette? Quizen har {QUIZ_LENGTH} tilfeldige spørsmål om strøm, vann, varme og regelverk for datasentre i Norge.</p>
        <div className="qz-actions"><Link className="qz-primary" href="/quiz">Ta quizen selv <ArrowRight size={16}/></Link></div>
      </section>
    </main>
  );
}
