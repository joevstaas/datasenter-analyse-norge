import {test,expect} from '@playwright/test';
const url='http://127.0.0.1:3000/labs/datasenter-analyse-norge';
test('real ODP data, filters, sourced details, shared link, nature and mobile',async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(url);await expect(page.locator('.project-row')).toHaveCount(8,{timeout:60000});await expect(page.locator('.map-marker')).toHaveCount(8,{timeout:30000});
 await page.getByRole('textbox',{name:'Søk etter prosjekt eller kommune'}).fill('Undheim');await expect(page.locator('.project-row')).toHaveCount(1);await expect(page.locator('.map-marker')).toHaveCount(1);
 await page.locator('.project-row').click();await expect(page.getByRole('heading',{name:'Green Mountain SVG-Undheim',exact:true})).toBeVisible();
 await page.getByRole('button',{name:'Kraft',exact:true}).click();await expect(page.getByText('Målt årlig kraftbruk: ikke dokumentert')).toBeVisible();
 await page.locator('.location summary').click();await expect(page.getByText('58.659687',{exact:false})).toBeVisible();await expect(page.locator('.location a').first()).toHaveAttribute('href',/^https:/);
 await expect(page).toHaveURL(/prosjekt=undheim/);await page.reload();await expect(page.getByRole('heading',{name:'Green Mountain SVG-Undheim',exact:true})).toBeVisible();
 await page.getByRole('button',{name:'Lukk prosjektdetaljer'}).click();await page.getByRole('textbox').fill('ingen treff her');await expect(page.getByText('Ingen prosjekter matcher')).toBeVisible();await expect(page.locator('.map-marker')).toHaveCount(0);
 await page.getByRole('button',{name:'Vis alle prosjekter',exact:true}).click();await expect(page.locator('.project-row')).toHaveCount(8);
 const natureResponse=page.waitForResponse(r=>r.url().includes('/api/vern?')&&r.status()===200,{timeout:30000});await page.getByRole('button',{name:'Vis verneområder',exact:true}).click();await natureResponse;
 await expect(page.getByText('Registrerte verneområder',{exact:true})).toBeVisible();await page.screenshot({path:'/tmp/datasenter-tested-desktop.png'});
 await page.setViewportSize({width:390,height:844});await expect(page.locator('.project-row').first()).toBeVisible();await page.locator('.project-row').first().click();await expect(page.getByRole('complementary',{name:'Prosjektdetaljer'})).toBeVisible();await page.screenshot({path:'/tmp/datasenter-tested-mobile.png'});
 await page.getByRole('button',{name:'Lukk prosjektdetaljer'}).click();await page.getByRole('button',{name:'Kart',exact:true}).click();await expect(page.locator('.map-canvas')).toBeVisible();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);expect(errors).toEqual([]);
});
test('ODP failure remains explicit; no silent fabricated fallback',async({page})=>{await page.route('**/api/atlas',r=>r.fulfill({status:503,contentType:'application/json',body:'{}'}));await page.goto(url);await expect(page.locator('.empty-card[role=alert]')).toContainText('kunne ikke hente');await expect(page.locator('.project-row')).toHaveCount(0);});
