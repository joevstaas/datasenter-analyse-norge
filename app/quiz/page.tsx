import type {Metadata} from 'next';
import Link from 'next/link';
import {ArrowLeft} from 'lucide-react';
import QuizGame from '@/components/quiz';

export const metadata: Metadata = {
  title: 'Quiz: hvor mye vet du om datasentre i Norge?',
  description: '10 tilfeldige spørsmål om strøm, vann, varme og regelverk, basert på Teknologirådets rapport om datasentre i Norge.',
};

export default function QuizPage() {
  return (
    <main className="qz-page">
      <header className="qz-header"><Link href="/" className="qz-back"><ArrowLeft size={15}/> Til kartet</Link><span className="brand"><span className="brand-symbol">≋</span> OCEAN DATA JO <span className="labs">/ LABS</span></span></header>
      <QuizGame />
    </main>
  );
}
