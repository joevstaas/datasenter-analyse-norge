import general from '@/quiz/datasentre-i-norge-quiz.json';
import regulation from '@/quiz/datasentre-i-norge-quiz-reguleringer.json';

export const QUIZ_LENGTH = 10;

type RawQuestion = {
  id: number;
  question: string;
  options: {id: string; text: string}[];
  correct: string;
  explanation: string;
  fact: string;
  reference: {page: string; chapter: string};
};

export type Option = {key: string; text: string};
export type Question = {
  id: string;
  question: string;
  options: Option[];
  correctKey: string;
  explanation: string;
  fact: string;
  page: string;
  chapter: string;
};

const prefixed = (prefix: string, items: RawQuestion[]): Question[] =>
  items.map(q => ({
    id: prefix + q.id,
    question: q.question,
    options: q.options.map(o => ({key: o.id, text: o.text})),
    correctKey: q.correct,
    explanation: q.explanation,
    fact: q.fact,
    page: q.reference.page,
    chapter: q.reference.chapter,
  }));

export const allQuestions: Question[] = [
  ...prefixed('a', general.questions as RawQuestion[]),
  ...prefixed('b', regulation.questions as RawQuestion[]),
];

export const questionById = (id: string) => allQuestions.find(q => q.id === id);

export function shuffle<T>(items: readonly T[]): T[] {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/** Picks a random set of questions (preferring ones not in `exclude`), with the answer options shuffled too. */
export function drawQuiz(count = QUIZ_LENGTH, exclude: string[] = []): Question[] {
  const fresh = shuffle(allQuestions.filter(q => !exclude.includes(q.id)));
  const rest = shuffle(allQuestions.filter(q => exclude.includes(q.id)));
  return shuffle([...fresh, ...rest].slice(0, count))
    .map(q => ({...q, options: shuffle(q.options)}));
}

export const REPORT = {
  title: 'Datasentre i Norge: Vurderinger av samfunnsnytte',
  publisher: 'Teknologirådet',
  year: 2026,
};

export function rank(score: number, total = QUIZ_LENGTH) {
  const share = score / total;
  if (share >= 0.9) return {title: 'Datasenter-ekspert', line: 'Du kan bransjen bedre enn de fleste.'};
  if (share >= 0.7) return {title: 'Godt orientert', line: 'Du har god oversikt over datasentre i Norge.'};
  if (share >= 0.4) return {title: 'På god vei', line: 'Du kan en del, men bransjen byr på overraskelser.'};
  return {title: 'Nysgjerrig nybegynner', line: 'Bransjen er full av overraskende fakta. Prøv igjen!'};
}

/** Share code: "<score>-<index of the fact shown in the picture>", e.g. "7-12". */
export function shareCode(score: number, factIndex: number) {
  return `${score}-${factIndex}`;
}

export function parseShareCode(code: string): {score: number; fact: Question} | null {
  const m = /^(\d{1,2})-(\d{1,2})$/.exec(code);
  if (!m) return null;
  const score = Number(m[1]);
  const fact = allQuestions[Number(m[2])];
  if (score > QUIZ_LENGTH || !fact) return null;
  return {score, fact};
}

export function shareText(score: number, total = QUIZ_LENGTH) {
  return `Jeg fikk ${score} av ${total} i quizen om datasentre i Norge. Hvor mye vet du om bransjens strøm-, vann- og varmeforbruk? Ta quizen:`;
}
