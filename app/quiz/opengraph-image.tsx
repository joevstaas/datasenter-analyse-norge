import {quizIntroCard, CARD_LANDSCAPE} from '@/lib/quiz-card';

export const alt = 'Quiz: Hvor mye vet du om datasentre i Norge?';
export const size = CARD_LANDSCAPE;
export const contentType = 'image/png';

export default function Image() {
  return quizIntroCard(size);
}
