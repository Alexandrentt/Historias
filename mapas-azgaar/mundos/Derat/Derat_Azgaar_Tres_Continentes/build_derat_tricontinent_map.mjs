#!/usr/bin/env node
/**
 * Build an Azgaar 1.158.0 editable .map for Derat from a preserved base grid
 * and three proposed continent outlines. Physical geography is provisional.
 * The political layer is cleared rather than copied from the unrelated base.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {makeVoronoi, markupPack} from './graph_tools.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const option=(n,d=null)=>{const i=process.argv.indexOf(n);return i>=0?process.argv[i+1]:d;};
const inputMap=option('--map',path.resolve(here,'../derat(continente de alfaguara).map'));
const inputGeo=option('--continents',path.resolve(here,'Derat_continentes.geojson'));
const outputMap=option('--out',path.resolve(here,'../Derat_Azgaar_Tres_Continentes_v1.map'));
const outputAudit=option('--audit',path.resolve(here,'../Derat_Azgaar_Tres_Continentes_audit.json'));
const W=1333,H=632;
const fail=m=>{throw new Error(m);};
const parse=(s,n)=>{try{return JSON.parse(s);}catch(e){fail(n+': '+e.message);}};
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
const rnd=(v,d=0)=>{const m=10**d;return Math.round(v*m)/m;};
const csv=a=>Array.from(a,v=>String(v)).join(',');
const zeros=n=>new Array(n).fill(0);
function inRing(x,y,ring){let inside=false;for(let i=0,j=ring.length-1;i<ring.length;j=i++){const [xi,yi]=ring[i],[xj,yj]=ring[j];if(((yi>y)!==(yj>y))&&(x<((xj-xi)*(y-yi))/(yj-yi)+xi))inside=!inside;}return inside;}
function inFeature(x,y,f){const r=f.geometry.coordinates;if(!inRing(x,y,r[0]))return false;for(let i=1;i<r.length;i++)if(inRing(x,y,r[i]))return false;return true;}
const records=fs.readFileSync(inputMap,'utf8').split('\r\n');
if(records.length!==56)fail('Expected 56 CRLF records; got '+records.length);
const header=records[0].split('|');if(header[0]!=='1.158.0')fail('Expected Azgaar 1.158.0 base map');
const settings=parse(records[1],'settings'),grid=parse(records[6],'grid');
const geo=parse(fs.readFileSync(inputGeo,'utf8'),'continents GeoJSON');
if(geo.type!=='FeatureCollection'||geo.features.length!==3)fail('Expected exactly 3 continent features');
const names=['Alfaguara','Vardena','Edravia'],byName=new Map(geo.features.map(f=>[f.properties?.name,f]));
for(const n of names)if(!byName.has(n))fail('Missing continent '+n);
const continents=names.map(n=>byName.get(n));
for(const f of continents){if(f.geometry?.type!=='Polygon')fail(f.properties.name+' must be Polygon');const r=f.geometry.coordinates?.[0];if(!r||r.length<4||r[0][0]!==r.at(-1)[0]||r[0][1]!==r.at(-1)[1])fail('Invalid closed ring: '+f.properties.name);}
const points=grid.points,boundary=grid.boundary,N=points.length;
const srcH=records[7].split(',').map(Number),prec=records[8].split(',').map(Number),temp=records[11].split(',').map(Number);
if(N!==100280||srcH.length!==N||prec.length!==N||temp.length!==N)fail('Unexpected base grid arrays');
if(grid.spacing!==2.9||grid.cellsX!==460||grid.cellsY!==218)fail('Unexpected base grid metadata');
const namesAt=new Int8Array(N).fill(-1),counts=Object.fromEntries(names.map(n=>[n,0]));
const heights=new Uint8Array(N),newPrec=Uint8Array.from(prec,v=>clamp(Math.round(v),0,255)),newTemp=Int8Array.from(temp,v=>clamp(Math.round(v),-128,127));
for(let i=0;i<N;i++){
 const [x,y]=points[i],lon=x/W*360-180,lat=90-y/H*180;let match=-1;
 for(let c=0;c<continents.length;c++)if(inFeature(lon,lat,continents[c])){if(match!==-1)fail('Overlapping continents at grid point '+i);match=c;}
 if(match>=0){namesAt[i]=match;counts[names[match]]++;const nx=x/W,ny=y/H;const wave=Math.sin(nx*17.3+Math.cos(ny*8.1))*.5+Math.cos(ny*23.7-nx*4.2)*.3+Math.sin((nx+ny)*41.1)*.2;const regional=7*Math.sin(nx*5.7+ny*2.1)+5*Math.cos(ny*9.3-nx*3.6);heights[i]=clamp(Math.round(27+Math.abs(wave)*22+regional),20,82);}else heights[i]=0;
}
for(const [n,c] of Object.entries(counts))if(c<100)fail(n+' contains too few grid points: '+c);
const gridGraph=makeVoronoi(points,boundary);if(!gridGraph.cells.c.every(Array.isArray))fail('Grid Voronoi incomplete');
const gridFids=new Uint16Array(N),distance=new Int8Array(N),gridFeatures=[];let next=0;
while(next!==-1){const first=next,land=heights[first]>=20;let border=false;gridFids[first]=gridFeatures.length+1;const q=[first];while(q.length){const cell=q.pop();if(!border&&gridGraph.cells.b[cell])border=true;for(const j of gridGraph.cells.c[cell]){const jl=heights[j]>=20;if(land===jl&&gridFids[j]===0){gridFids[j]=gridFeatures.length+1;q.push(j);}else if(land&&!jl){distance[cell]=1;distance[j]=-1;}}}gridFeatures.push({i:gridFeatures.length+1,land,border,type:land?'island':(border?'ocean':'lake')});next=-1;for(let i=0;i<N;i++)if(!gridFids[i]){next=i;break;}}
const propagate=(start,inc,limit)=>{for(let d=start,marked=Infinity;marked>0&&d!==limit;d+=inc){marked=0;const prev=d-inc;for(let i=0;i<N;i++)if(distance[i]===prev)for(const j of gridGraph.cells.c[i])if(distance[j]===0){distance[j]=d;marked++;}}};propagate(-2,-1,-10);
const packPoints=[],parents=[],packHeights=[],packNames=[];
const split=grid.spacing*(1+(0.9-settings.graph.jitter)),split2=split*split;
for(let i=0;i<N;i++){const h=heights[i],t=distance[i];if(h<20&&t!==-1&&t!==-2)continue;if(t===-2&&(i%4===0||gridFeatures[gridFids[i]-1]?.type==='lake'))continue;const [x,y]=points[i];packPoints.push([x,y]);parents.push(i);packHeights.push(h);packNames.push(namesAt[i]);if(t===1||t===-1){if(gridGraph.cells.b[i])continue;for(const j of gridGraph.cells.c[i]){if(i>j||distance[j]!==t)continue;const [xx,yy]=points[j];if((y-yy)**2+(x-xx)**2<split2)continue;packPoints.push([rnd((x+xx)/2,1),rnd((y+yy)/2,1)]);parents.push(i);packHeights.push(h);packNames.push(namesAt[i]);}}}
const pack=makeVoronoi(packPoints,boundary),P=packPoints.length;pack.cells.h=Uint8Array.from(packHeights);if(P!==pack.cells.i.length||!pack.cells.c.every(Array.isArray))fail('Pack graph incomplete');
const namesByCell=packNames.map(i=>i>=0?names[i]:null),marked=markupPack(pack,W,H,namesByCell),features=marked.features;
const lands=features.filter(f=>f?.land),oceans=features.filter(f=>f?.type==='ocean'),lakes=features.filter(f=>f?.type==='lake');
if(lands.length!==3||lakes.length!==0||oceans.length<1)fail('Expected exactly three lands, no lakes, and ocean');
for(const n of names){const found=lands.filter(f=>f.name===n);if(found.length!==1)fail('Expected one feature '+n);found[0].note='Contorno de Derat_continentes.geojson; propuesta no canónica; relieve provisional.';found[0].tags=['derat','provisional','continente'];}
oceans.forEach((f,i)=>{f.name=oceans.length===1?'Océano de Derat':'Región oceánica '+(i+1)+' de Derat';f.subtype=f.cells>N/25?'ocean':f.cells>N/1000?'sea':'gulf';f.note='Conectividad de celdas en proyección rectangular; fragmentos del borde no implican otros océanos planetarios.';});
const neutral=parse(records[14],'states')[0];Object.assign(neutral,{diplomacy:[],neighbors:[],provinces:[],military:[],burgs:0,cells:0,area:0,urban:0,rural:0,name:'Neutrales'});
const wild=parse(records[13],'cultures')[0],religion=parse(records[29],'religions')[0];
const s=structuredClone(settings);s.lore.name='Derat — tres continentes (provisional)';s.lore.description='Mapa físico provisional editable; contornos de Derat_continentes.geojson; relieve procedural; Vardena y Edravia son nombres propuestos. Sin fronteras políticas ni asentamientos no georreferenciados.';s.seed=String(settings.seed);s.graph.width=W;s.graph.height=H;
const svg='<svg id="map" data-layer="map" width="'+W+'" height="'+H+'" version="1.1" xmlns="http://www.w3.org/2000/svg"><defs/><g id="viewbox"><g id="ocean" data-layer="ocean"/><g id="landmass" data-layer="landmass"/><g id="heightmap" data-layer="heightmap"/><g id="coastline" data-layer="coastline"/><g id="biomes" data-layer="biomes"/><g id="cells" data-layer="cells"/><g id="grid" data-layer="grid"/><g id="rivers" data-layer="rivers"/><g id="relief" data-layer="relief"/><g id="states" data-layer="states"/><g id="borders" data-layer="borders"/><g id="routes" data-layer="routes"/><g id="ice" data-layer="ice"/><g id="goods" data-layer="goods"/><g id="markets" data-layer="markets"/><g id="emblems"/><g id="burgIcons" data-layer="burgIcons"/><g id="labels" data-layer="labels"/><g id="military" data-layer="military"/><g id="markers" data-layer="markers"/></g><g id="scaleBar" data-layer="scaleBar"/><g id="vignette" data-layer="vignette"/><g id="legend" data-layer="legend"/></svg>';
const biome=new Uint8Array(N);for(let i=0;i<N;i++){if(heights[i]<20){biome[i]=0;continue;}const t=newTemp[i],p=newPrec[i];if(t< -12)biome[i]=11;else if(t< -3)biome[i]=10;else if(t<3)biome[i]=9;else if(t<8)biome[i]=p<65?2:9;else if(t>22&&p<55)biome[i]=1;else if(t>19&&p>170)biome[i]=7;else if(t>18&&p>90)biome[i]=3;else if(t>12&&p>160)biome[i]=5;else if(t>5&&p>150)biome[i]=8;else if(p<70)biome[i]=4;else biome[i]=6;}
const packBiome=parents.map(i=>biome[i]);
const arrays={biome:packBiome,burg:zeros(P),conf:zeros(P),culture:zeros(P),fl:zeros(P),pop:zeros(P),r:zeros(P),s:zeros(P),state:zeros(P),religion:zeros(P),province:zeros(P),good:zeros(P),market:zeros(P),prosperity:zeros(P),development:zeros(P)};
const gridSave={spacing:grid.spacing,cellsX:grid.cellsX,cellsY:grid.cellsY,boundary,points,features:[0,...gridFeatures]};
const set=(i,v)=>{records[i]=typeof v==='string'?v:JSON.stringify(v);};
header[0]='1.158.0';header[1]='File can be loaded in azgaar.github.io/Fantasy-Map-Generator';header[2]='2026-11-12';header[3]=s.seed;header[4]=String(W);header[5]=String(H);header[6]=String(Date.now());records[0]=header.join('|');
set(1,s);set(5,svg);set(6,gridSave);set(7,csv(heights));set(8,csv(newPrec));set(9,csv(gridFids));set(10,csv(distance));set(11,csv(newTemp));set(12,features);set(13,[wild]);set(14,[neutral]);set(15,[0]);
set(16,csv(arrays.biome));set(17,csv(arrays.burg));set(18,csv(arrays.conf));set(19,csv(arrays.culture));set(20,csv(arrays.fl));set(21,csv(arrays.pop));set(22,csv(arrays.r));set(23,'');set(24,csv(arrays.s));set(25,csv(arrays.state));set(26,csv(arrays.religion));set(27,csv(arrays.province));set(28,'');set(29,[religion]);set(30,[0]);set(32,[]);set(35,[]);set(36,{});set(37,[]);set(38,[]);set(39,[]);set(40,csv(arrays.good));set(41,'');set(42,[]);set(43,[]);set(44,csv(arrays.market));set(46,[]);set(47,[]);set(49,[]);set(52,[]);set(53,[]);set(54,csv(arrays.prosperity));set(55,csv(arrays.development));
for(const [n,a] of Object.entries(arrays))if(a.length!==P)fail('Array '+n+' length mismatch');
fs.writeFileSync(outputMap,records.join('\r\n'),'utf8');
const audit={product:'Derat — Azgaar editable map',map_version:'1.158.0',source_map:path.basename(inputMap),source_seed:settings.seed,output_map:path.basename(outputMap),dimensions:{width:W,height:H},grid:{points:N,boundary_points:boundary.length,spacing:grid.spacing,features:gridFeatures.length},pack:{cells:P,features:features.length-1,land_features:lands.map(f=>({name:f.name,cells:f.cells,firstCell:f.firstCell,vertices:f.vertices.length})),ocean_features:oceans.map(f=>({name:f.name,cells:f.cells})),lakes:lakes.length},grid_land_points:counts,data_arrays_all_match_pack_cells:true,political_geography:'cleared; no city/state/culture/religion assignments inherited from base',source_geometry:'Derat_continentes.geojson; provisional, not canon',relief:'procedural and provisional',azgaar_load_test:'not executed in live browser; format checked structurally',limitations:['Live Azgaar import has not been witnessed.','Alfaguara contour is used exactly as in the supplied GeoJSON.','No settlements, rivers, roads, political borders or canonical resource sites were invented.']};
fs.writeFileSync(outputAudit,JSON.stringify(audit,null,2)+'\n');
const written=fs.readFileSync(outputMap,'utf8').split('\r\n');if(written.length!==56)fail('Output record count mismatch');
const rf=parse(written[12],'output features');const lens=[16,17,18,19,20,21,22,24,25,26,27,40,44,54,55].map(i=>written[i].split(',').length);if(!lens.every(n=>n===P))fail('Pack array mismatch');
if(rf.filter(f=>f?.land).length!==3)fail('Output must have three land features');
for(const f of rf.filter(f=>f?.land))for(const v of f.vertices)if(!Number.isInteger(v)||v<0||v>=pack.vertices.p.length||!pack.vertices.p[v])fail('Invalid feature vertex '+v);
console.log(JSON.stringify({outputMap,bytes:fs.statSync(outputMap).size,gridPoints:N,packCells:P,landFeatures:lands.map(f=>({name:f.name,cells:f.cells,vertices:f.vertices.length})),oceanFeatures:oceans.map(f=>f.name),lakes:lakes.length,cellArrayLengths:[...new Set(lens)]},null,2));
