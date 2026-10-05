import {test,expect} from '@playwright/test';
test('Mapbox tile error offers working Kartverket basemap; keyboard dialog',async({page})=>{
 await page.route('**/v4/*.vector.pbf*',r=>r.fulfill({status:403,body:'Forbidden'}));
 await page.goto('http://127.0.0.1:3000/labs/datasenter-analyse-norge');
 await expect(page.getByRole('button',{name:'Bruk Kartverkets basiskart'})).toBeVisible({timeout:30000});
 const tile=page.waitForResponse(r=>r.url().includes('cache.kartverket.no')&&r.status()===200);
 await page.getByRole('button',{name:'Bruk Kartverkets basiskart'}).click();await tile;
 await expect(page.locator('.map-marker')).toHaveCount(8,{timeout:30000});await expect(page.locator('.map-error')).toHaveCount(0);
 await page.getByRole('button',{name:'Vis verneområder'}).click();await page.waitForResponse(r=>r.url().includes('/api/vern?')&&r.status()===200);
 await page.screenshot({path:'/tmp/datasenter-working-map.png'});
 await page.getByRole('button',{name:'Om dataene'}).click();await expect(page.getByRole('dialog')).toBeVisible();await page.keyboard.press('Escape');await expect(page.getByRole('dialog')).toHaveCount(0);
});
