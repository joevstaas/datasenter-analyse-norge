import {test,expect} from '@playwright/test';
const url=process.env.TEST_APP_URL||'http://localhost:5174/labs/datasenter-analyse-norge';
test('nature layers, legends, zoom guidance, point lookup and mobile menu',async({page,request})=>{
 const tiles=new Set<string>();page.on('response',r=>{if(r.status()===200&&r.url().includes('/api/natur?')&&r.url().includes('bbox='))tiles.add(new URL(r.url()).searchParams.get('layer')||'');});
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(url);await expect(page.locator('.map-marker')).toHaveCount(8,{timeout:60000});
 await page.getByRole('button',{name:/Natur rundt prosjektet/}).click();
 await page.getByRole('checkbox',{name:'Naturtyper (NiN)',exact:true}).check();
 await expect(page.getByText('Zoom inn for å se dette laget',{exact:false})).toBeVisible();
 await page.getByRole('textbox',{name:'Søk etter prosjekt eller kommune'}).fill('Gromstul');await page.locator('.project-row').click();
 await page.getByRole('button',{name:'Lukk prosjektdetaljer'}).click();
 for(const [key,name] of [['nin','Naturtyper (NiN)'],['coverage','Hvor er naturen kartlagt?'],['hb13','Naturtyper (HB13)']]){
  const checkbox=page.getByRole('checkbox',{name,exact:true});
  await checkbox.check();await expect.poll(()=>tiles.has(key),{timeout:30000}).toBe(true);
 }
 await expect(page.locator('.nature-legend img')).toHaveCount(4);
 await page.getByRole('button',{name:/Natur rundt prosjektet/}).click();
 const canvas=page.locator('.map-canvas');const b=await canvas.boundingBox();if(!b)throw new Error('No map');
 const result=page.waitForResponse(r=>r.url().includes('/api/natur?mode=identify')&&r.status()===200);
 await canvas.click({position:{x:b.width*.7,y:b.height*.55}});await result;
 await expect(page.getByRole('complementary',{name:'Naturfakta på kartpunkt'})).toBeVisible();
 await expect(page.getByText('Henter naturfakta …')).toHaveCount(0);
 await page.getByRole('button',{name:'Lukk naturfakta'}).click();
 await page.setViewportSize({width:390,height:844});await page.getByRole('button',{name:'Kart',exact:true}).click();await page.getByRole('button',{name:/Natur rundt prosjektet/}).click();
 await expect(page.getByRole('checkbox',{name:'Naturtyper (NiN)',exact:true})).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 await page.screenshot({path:'/tmp/nature-mobile.png'});expect(errors).toEqual([]);
 for(const q of ['layer=unknown','layer=nin&bbox=0,0,1','layer=nin&mode=identify&point=Infinity,0'])expect((await request.get(url+'/api/natur?'+q)).status()).toBe(400);
});
