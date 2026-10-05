import {test} from 'node:test';
import assert from 'node:assert/strict';
import {filterProjects,coordinates,claimLabel,safeUrl,type Row} from '../lib/model';
const p:Row={name:'Google / WS Computing – Gromstul',municipality:'Skien',status:'Byggestart dokumentert 2024',longitude:9.518779,latitude:59.269954};
test('filters combine and empty results stay empty',()=>{assert.equal(filterProjects([p],'grom','Skien','Google / WS Computing','Bygging / utvikling').length,1);assert.equal(filterProjects([p],'grom','Time','','').length,0);});
test('unknown and invalid coordinates never become invented points',()=>{assert.equal(coordinates({...p,longitude:null}),null);assert.equal(coordinates({...p,latitude:NaN}),null);assert.equal(coordinates({...p,latitude:91}),null);assert.deepEqual(coordinates(p),[9.518779,59.269954]);});
test('attributed claims remain visibly unverified',()=>{assert.match(claimLabel({attributed_publication_allowed:false}),/Uverifisert/);assert.match(claimLabel({details_json:'{"publishAsFact":false}'}),/Uverifisert/);});
test('source links reject executable schemes',()=>{assert.equal(safeUrl('javascript:alert(1)'),undefined);assert.equal(safeUrl('https://nve.no/'),'https://nve.no/');});
