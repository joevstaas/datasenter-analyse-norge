import { loadAtlas } from '@/lib/odp';
export const runtime='nodejs';
export const maxDuration=60;
export async function GET(){try{return Response.json(await loadAtlas(),{headers:{'Cache-Control':'public, s-maxage=300, stale-while-revalidate=60'}});}catch(e){const code=e instanceof Error && /^ODP_[A-Z_0-9]+$/.test(e.message)?e.message:'ODP_UNEXPECTED_ERROR';console.error('[atlas]',code);return Response.json({error:'Prosjektdata kunne ikke hentes fra ODP. Prøv igjen om litt.'},{status:503,headers:{'Cache-Control':'no-store'}});}}
