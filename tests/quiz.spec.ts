import {test,expect} from '@playwright/test';
const base=(process.env.TEST_APP_URL||'http://127.0.0.1:3000/labs/datasenter-analyse-norge');
const shots=process.env.QUIZ_SHOTS||'';

test('quiz: 10 random questions, live points, result and share',async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route('**/api/atlas',r=>r.fulfill({status:503,contentType:'application/json',body:'{}'}));
 await page.goto(base);
 await page.getByRole('link',{name:'Ta quizen'}).click();
 await expect(page).toHaveURL(/\/quiz$/);
 await expect(page.getByRole('heading',{name:/Hvor mye vet du om/})).toBeVisible();
 await page.getByRole('button',{name:/Start quizen/}).click();
 const seen=new Set<string>();
 for(let i=1;i<=10;i++){
  await expect(page.getByText(`Spørsmål ${i} av 10`)).toBeVisible();
  seen.add(await page.locator('#qz-question').innerText());
  const options=page.locator('.qz-option');await expect(options).toHaveCount(3);
  if(i===1&&shots)await page.screenshot({path:`${shots}/quiz-question.png`});
  await options.first().click();
  await expect(page.getByRole('status')).toContainText(/Riktig|Ikke helt/);
  await expect(page.getByRole('status')).toContainText('Kilde: Teknologirådet 2026, side');
  await expect(page.locator('.qz-option.right')).toHaveCount(1);
  if(i===1&&shots)await page.screenshot({path:`${shots}/quiz-answered.png`});
  await page.getByRole('button',{name:i<10?'Neste spørsmål':'Se resultatet'}).click();
 }
 expect(seen.size).toBe(10);
 await expect(page.getByRole('heading',{name:'Gå gjennom svarene'})).toBeVisible();
 await expect(page.locator('.qz-review li')).toHaveCount(10);
 const img=page.getByRole('img',{name:/Delebilde/});await expect(img).toBeVisible();
 const src=await img.getAttribute('src');expect(src).toMatch(/\/quiz\/del\/\d{1,2}-\d{1,2}\/portrett$/);
 const res=await page.request.get(new URL(src!,page.url()).href);expect(res.status()).toBe(200);expect(res.headers()['content-type']).toContain('image/png');
 await expect(page.getByRole('link',{name:/Del på LinkedIn/})).toHaveAttribute('href',/linkedin\.com\/sharing\/share-offsite\/\?url=.*%2Fquiz%2Fdel%2F/);
 await expect(page.getByRole('link',{name:/Last ned bilde/})).toHaveAttribute('download',/datasenter-quiz-\d+-av-10\.png/);
 if(shots)await page.screenshot({path:`${shots}/quiz-result.png`,fullPage:true});
 // shared link: lands on a page with the score and a call to take the quiz
 const code=src!.match(/del\/(\d{1,2}-\d{1,2})\//)![1];
 await page.goto(`${base}/quiz/del/${code}`);
 await expect(page.getByText('Visste du at')).toBeVisible();
 await expect(page.locator('meta[property="og:image"]')).toHaveAttribute('content',/opengraph-image/);
 await page.getByRole('link',{name:/Ta quizen selv/}).click();await expect(page).toHaveURL(/\/quiz$/);
 expect(errors).toEqual([]);
});

test('quiz: invalid share code is 404 and mobile has no horizontal scroll',async({page})=>{
 const r=await page.goto(`${base}/quiz/del/99-1`);expect(r?.status()).toBe(404);
 await page.setViewportSize({width:390,height:844});await page.goto(`${base}/quiz`);
 await page.getByRole('button',{name:/Start quizen/}).click();await page.locator('.qz-option').first().click();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
 if(shots)await page.screenshot({path:`${shots}/quiz-mobile.png`});
});
