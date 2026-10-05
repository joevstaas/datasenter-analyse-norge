import {parseShareCode} from '@/lib/quiz';
import {quizCard, CARD_PORTRAIT} from '@/lib/quiz-card';

/** Portrait picture (1080×1350) for Instagram and other image-first apps. */
export async function GET(_request: Request, {params}: {params: Promise<{code: string}>}) {
  const shared = parseShareCode((await params).code);
  if (!shared) return new Response('Ugyldig delingskode', {status: 404});
  return quizCard(shared.score, shared.fact, CARD_PORTRAIT);
}
