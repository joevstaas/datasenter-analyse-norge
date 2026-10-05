import {notFound} from 'next/navigation';
import {parseShareCode} from '@/lib/quiz';
import {quizCard, CARD_LANDSCAPE} from '@/lib/quiz-card';

export const alt = 'Resultat fra quizen om datasentre i Norge';
export const size = CARD_LANDSCAPE;
export const contentType = 'image/png';

export default async function Image({params}: {params: Promise<{code: string}>}) {
  const shared = parseShareCode((await params).code);
  if (!shared) notFound();
  return quizCard(shared.score, shared.fact, size);
}
