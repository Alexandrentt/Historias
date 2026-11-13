/**
 * Azgaar 1.158.0 Voronoi and Features.markupPack port.
 * Source reference: Azgaar/Fantasy-Map-Generator, src/model/graph/voronoi.ts,
 * src/model/physical/features-generator.ts and src/utils/path-utils.ts.
 * Copyright (c) 2017-2024 Max Haniyeu (Azgaar); MIT license.
 */
import Delaunator from './delaunator.mjs';

export function makeVoronoi(points, boundary) {
  const allPoints = points.concat(boundary);
  const del = Delaunator.from(allPoints);
  const triangles = del.triangles, halfedges = del.halfedges, pointCount = points.length;
  const vertexCount = triangles.length / 3;
  const cells = {i: Uint32Array.from({length:pointCount},(_,i)=>i), p:points, c:new Array(pointCount), v:new Array(pointCount), b:new Uint8Array(pointCount), area:new Uint16Array(pointCount)};
  const vertices = {p:new Array(vertexCount), v:new Array(vertexCount), c:new Array(vertexCount)};
  const nextHalfedge = e => (e % 3 === 2 ? e - 2 : e + 1);
  const triangleOfEdge = e => (e < 0 ? -1 : Math.floor(e / 3));
  const edgesAroundPoint = start => {
    const edges=[]; let incoming=start;
    do { edges.push(incoming); const outgoing=nextHalfedge(incoming); incoming=halfedges[outgoing]; }
    while(incoming!==-1 && incoming!==start && edges.length < 20);
    return edges;
  };
  const circumcenter = (a,b,c) => {
    const [ax,ay]=a,[bx,by]=b,[cx,cy]=c;
    const dx=bx-ax,dy=by-ay,ex=cx-ax,ey=cy-ay;
    const bl=dx*dx+dy*dy,cl=ex*ex+ey*ey,d=0.5/(dx*ey-dy*ex);
    return [ax+(ey*bl-dy*cl)*d, ay+(dx*cl-ex*bl)*d];
  };
  for(let e=0;e<triangles.length;e++){
    const cellId=triangles[nextHalfedge(e)];
    if(cellId<pointCount && !cells.c[cellId]){
      const edges=edgesAroundPoint(e);
      cells.v[cellId]=edges.map(e=>Math.floor(e/3));
      cells.c[cellId]=edges.map(e=>triangles[e]).filter(id=>id<pointCount);
      cells.b[cellId]=edges.length>cells.c[cellId].length?1:0;
    }
    const t=Math.floor(e/3);
    if(!vertices.p[t]){
      const p0=triangles[t*3],p1=triangles[t*3+1],p2=triangles[t*3+2];
      vertices.p[t]=circumcenter(allPoints[p0],allPoints[p1],allPoints[p2]);
      vertices.v[t]=[0,1,2].map(j=>triangleOfEdge(halfedges[t*3+j]));
      vertices.c[t]=[p0,p1,p2];
    }
  }
  for(let cell=0;cell<pointCount;cell++){
    const ring=cells.v[cell].map(v=>vertices.p[v]);
    let area=0;
    for(let i=0;i<ring.length;i++){
      const a=ring[i],b=ring[(i+1)%ring.length]; area+=a[0]*b[1]-b[0]*a[1];
    }
    cells.area[cell]=Math.min(65535,Math.abs(area/2));
  }
  return {cells, vertices, del, allPoints};
}

export function markupPack(pack, width, height, namesByLandCell = null) {
  const {cells, vertices} = pack;
  const n=cells.i.length;
  const featureIds=new Uint16Array(n), distanceField=new Int8Array(n), haven=new Uint32Array(n), harbor=new Uint8Array(n);
  const features=[];
  const isLand=i=>cells.h[i]>=20;
  const connectVertices=(startVertex, same) => {
    const chain=[]; let next=startVertex;
    for(let i=0;i<=vertices.c.length && (i===0 || next!==startVertex);i++){
      const previous=chain.length?chain[chain.length-1]:undefined;
      const current=next; chain.push(current);
      const nc=vertices.c[current];
      const [c1,c2,c3]=nc.map(same);
      const [v1,v2,v3]=vertices.v[current];
      if(v1!==previous && c1!==c2) next=v1;
      else if(v2!==previous && c2!==c3) next=v2;
      else if(v3!==previous && c1!==c3) next=v3;
      if(next<0 || next>=vertices.c.length || next===current) break;
    }
    return chain;
  };
  const clipPolygon=(pts) => {
    let poly=pts.map(p=>[p[0],p[1]]);
    const edges=[
      {inside:p=>p[0]>=0, intersect:(a,b)=>{const t=(0-a[0])/(b[0]-a[0]);return [0,a[1]+t*(b[1]-a[1])];}},
      {inside:p=>p[0]<=width, intersect:(a,b)=>{const t=(width-a[0])/(b[0]-a[0]);return [width,a[1]+t*(b[1]-a[1])];}},
      {inside:p=>p[1]>=0, intersect:(a,b)=>{const t=(0-a[1])/(b[1]-a[1]);return [a[0]+t*(b[0]-a[0]),0];}},
      {inside:p=>p[1]<=height, intersect:(a,b)=>{const t=(height-a[1])/(b[1]-a[1]);return [a[0]+t*(b[1]-a[1]),height];}}
    ];
    for(const edge of edges){
      const input=poly; poly=[]; if(!input.length)break;
      let S=input[input.length-1];
      for(const E of input){
        if(edge.inside(E)){if(!edge.inside(S)) poly.push(edge.intersect(S,E));poly.push(E);}
        else if(edge.inside(S)) poly.push(edge.intersect(S,E));
        S=E;
      }
    }
    return poly;
  };
  const polygonArea=pts=>{let area=0;for(let i=0;i<pts.length;i++){const a=pts[i],b=pts[(i+1)%pts.length];area+=a[0]*b[1]-b[0]*a[1];}return area/2;};
  const queue=[0]; let fid=1;
  while(queue[0]!==-1){
    const firstCell=queue[0]; featureIds[firstCell]=fid;
    const land=isLand(firstCell); let border=Boolean(cells.b[firstCell]), totalCells=1, cellsArea=cells.area[firstCell];
    while(queue.length){
      const cell=queue.pop(); if(cells.b[cell]) border=true;
      for(const neib of cells.c[cell]){
        const neibLand=isLand(neib);
        if(land && !neibLand){distanceField[cell]=1;distanceField[neib]=-1;}
        else if(land && neibLand){
          if(distanceField[neib]===0 && distanceField[cell]===1) distanceField[neib]=2;
          else if(distanceField[cell]===0 && distanceField[neib]===1) distanceField[cell]=2;
        }
        if(!featureIds[neib] && land===neibLand){queue.push(neib);featureIds[neib]=fid;totalCells++;cellsArea+=cells.area[neib];}
      }
    }
    const type=land?'island':(border?'ocean':'lake');
    let startCell=firstCell, featureVertices=[];
    if(type!=='ocean'){
      const same=i=>i<n && featureIds[i]===fid;
      const onBorder=i=>Boolean(cells.b[i]) || cells.c[i].some(j=>!same(j));
      if(!onBorder(firstCell)) startCell=cells.i.find(i=>same(i)&&onBorder(i));
      if(startCell===undefined) throw new Error(`Feature ${fid} has no border cell`);
      const startVertex=cells.v[startCell].find(v=>vertices.c[v].some(i=>!same(i)));
      if(startVertex===undefined) throw new Error(`Feature ${fid} has no start vertex`);
      featureVertices=connectVertices(startVertex,same);
    }
    const rawPoints=featureVertices.map(v=>vertices.p[v]);
    const clipped=type==='ocean'?[]:clipPolygon(rawPoints);
    const rawArea=type==='ocean'?cellsArea:polygonArea(clipped);
    const area=type==='ocean'?cellsArea:Math.abs(Math.round(rawArea));
    if(type==='lake' && rawArea>0) featureVertices.reverse();
    const shoreline=type==='lake'?[...new Set(featureVertices.flatMap(v=>vertices.c[v].filter(i=>i<n&&isLand(i))))]:[];
    const lakeHeight=type==='lake'?(Math.round(((shoreline.length?Math.min(...shoreline.map(i=>cells.h[i])):20)-0.1)*100)/100):0;
    const name=namesByLandCell?.[firstCell] || (land?`Continente ${fid-1}`:type==='ocean'?'Océano':'Lago');
    const f={i:fid,type,land,border,cells:totalCells,firstCell:startCell,vertices:featureVertices,area,shoreline,height:lakeHeight,tags:[],name};
    if(land){f.subtype='continent';f.group='sea_island';}
    else if(type==='ocean'){f.subtype='ocean';}
    else {f.subtype='freshwater';f.group='freshwater';}
    features.push(f);
    let next=-1; for(let i=0;i<featureIds.length;i++) if(featureIds[i]===0){next=i;break;}
    queue.length=0; queue.push(next); fid++;
  }
  const markup=(start,increment,limit)=>{
    for(let distance=start,marked=Infinity;marked>0 && distance!==limit;distance+=increment){
      marked=0; const prev=distance-increment;
      for(let i=0;i<n;i++) if(distanceField[i]===prev) for(const j of cells.c[i]) if(distanceField[j]===0){distanceField[j]=distance;marked++;}
    }
  };
  markup(3,1,127); markup(-2,-1,-10);
  return {features:[0,...features], featureIds, distanceField, haven, harbor};
}
