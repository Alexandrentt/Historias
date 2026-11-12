import fs from "node:fs";
import path from "node:path";
import Delaunator from "delaunator";

const worlds = ["Amitia", "Atharis", "Derat", "Khorza", "Návar", "Teknara"];
const outputDir = "mapas-azgaar/datos/franja-ecuatorial";
fs.mkdirSync(outputDir, {recursive: true});

function latitudeLimit(distanceM) {
  const a = 6378137;
  const f = 1 / 298.257223563;
  const e2 = f * (2 - f);
  const e4 = e2 ** 2, e6 = e2 ** 3;
  const arc = phi => a * (
    (1 - e2/4 - 3*e4/64 - 5*e6/256) * phi
    - (3*e2/8 + 3*e4/32 + 45*e6/1024) * Math.sin(2*phi)
    + (15*e4/256 + 45*e6/1024) * Math.sin(4*phi)
    - (35*e6/3072) * Math.sin(6*phi)
  );
  let lo = 0, hi = Math.PI / 90;
  for (let i = 0; i < 80; i++) {
    const mid = (lo + hi) / 2;
    if (arc(mid) < distanceM) lo = mid;
    else hi = mid;
  }
  return (lo + hi) / 2 * 180 / Math.PI;
}

function nextHalfedge(e) { return e % 3 === 2 ? e - 2 : e + 1; }
function triangleOfEdge(e) { return Math.floor(e / 3); }
function polygonArea(poly) {
  if (!poly || poly.length < 3) return 0;
  let sum = 0;
  for (let i = 0; i < poly.length; i++) {
    const a = poly[i], b = poly[(i + 1) % poly.length];
    sum += a[0] * b[1] - b[0] * a[1];
  }
  return Math.abs(sum) / 2;
}
function clipEdge(poly, axis, bound, keepGreater) {
  if (!poly.length) return [];
  const result = [];
  const inside = p => keepGreater ? p[axis] >= bound - 1e-9 : p[axis] <= bound + 1e-9;
  for (let i = 0; i < poly.length; i++) {
    const current = poly[i];
    const previous = poly[(i + poly.length - 1) % poly.length];
    const ci = inside(current), pi = inside(previous);
    if (ci !== pi) {
      const delta = current[axis] - previous[axis];
      if (Math.abs(delta) > 1e-12) {
        const t = (bound - previous[axis]) / delta;
        result.push([
          previous[0] + t * (current[0] - previous[0]),
          previous[1] + t * (current[1] - previous[1])
        ]);
      }
    }
    if (ci) result.push(current);
  }
  return result;
}
function clipRect(poly, x0, x1, y0, y1) {
  let result = poly;
  result = clipEdge(result, 0, x0, true);
  result = clipEdge(result, 0, x1, false);
  result = clipEdge(result, 1, y0, true);
  result = clipEdge(result, 1, y1, false);
  return result;
}
function circumcenter(a, b, c) {
  const [ax, ay] = a, [bx, by] = b, [cx, cy] = c;
  const ad = ax*ax + ay*ay, bd = bx*bx + by*by, cd = cx*cx + cy*cy;
  const d = 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by));
  if (Math.abs(d) < 1e-12) return [(ax+bx+cx)/3, (ay+by+cy)/3];
  return [
    (ad*(by-cy) + bd*(cy-ay) + cd*(ay-by)) / d,
    (ad*(cx-bx) + bd*(ax-cx) + cd*(bx-ax)) / d
  ];
}
function buildCellVertices(points, boundary) {
  const allPoints = points.concat(boundary);
  const delaunay = Delaunator.from(allPoints);
  const triangles = delaunay.triangles, halfedges = delaunay.halfedges;
  const centers = new Array(triangles.length / 3);
  const cells = new Array(points.length);
  const neighbors = new Array(points.length);
  function edgesAroundPoint(start) {
    const result = [];
    let incoming = start;
    do {
      result.push(incoming);
      const outgoing = nextHalfedge(incoming);
      incoming = halfedges[outgoing];
    } while (incoming !== -1 && incoming !== start && result.length < 20);
    return result;
  }
  for (let e = 0; e < triangles.length; e++) {
    const p = triangles[nextHalfedge(e)];
    if (p < points.length && !cells[p]) {
      const edges = edgesAroundPoint(e);
      cells[p] = edges.map(triangleOfEdge);
      neighbors[p] = edges.map(edge => triangles[edge]).filter(cell => cell < points.length);
    }
    const t = triangleOfEdge(e);
    if (!centers[t]) {
      centers[t] = circumcenter(
        allPoints[triangles[3*t]],
        allPoints[triangles[3*t+1]],
        allPoints[triangles[3*t+2]]
      );
    }
  }
  return {
    polygons: cells.map(cell => cell?.map(t => centers[t]).filter(Boolean) ?? []),
    neighbors
  };
}

function inspectWorld(world) {
  const data = JSON.parse(fs.readFileSync("/tmp/azgaar/" + world + ".json", "utf8"));
  const {width, height, coordinates, points, boundary, heights, temperatures, precipitation, distance_to_water} = data;
  if (points.length !== heights.length || points.length !== temperatures.length || points.length !== precipitation.length || points.length !== distance_to_water.length) {
    throw new Error(world + ": grid arrays have different lengths");
  }
  const latN = coordinates.latN, latS = coordinates.latS;
  const lonW = coordinates.lonW, lonE = coordinates.lonE;
  const limit = latitudeLimit(72500);
  const yNorth = (latN - limit) / (latN - latS) * height;
  const ySouth = (latN + limit) / (latN - latS) * height;
  const expectedArea = width * (ySouth - yNorth);
  const {polygons: cells, neighbors} = buildCellVertices(points, boundary);
  const maxNeighborDelta = new Float64Array(points.length);
  for (let i = 0; i < neighbors.length; i++) {
    for (const neighbor of neighbors[i] ?? []) {
      maxNeighborDelta[i] = Math.max(maxNeighborDelta[i], Math.abs(heights[i] - heights[neighbor]));
    }
  }
  const bins = new Map();
  const profile = {lowland:0, midland:0, highland:0, very_high:0, near_coast:0, land_height_sum:0, land_temperature_sum:0, land_precipitation_sum:0, roughness_sum:0};
  let landArea = 0, waterArea = 0, cellsIntersecting = 0;
  for (let i = 0; i < cells.length; i++) {
    const polygon = cells[i];
    if (polygon.length < 3) continue;
    const bandPolygon = clipRect(polygon, 0, width, yNorth, ySouth);
    const area = polygonArea(bandPolygon);
    if (area <= 1e-8) continue;
    cellsIntersecting++;
    const h = heights[i], temp = temperatures[i], prec = precipitation[i], coastDistance = distance_to_water[i];
    const isLand = h >= 20;
    if (isLand) {
      landArea += area;
      profile.land_height_sum += h * area;
      profile.land_temperature_sum += temp * area;
      profile.land_precipitation_sum += prec * area;
      profile.roughness_sum += maxNeighborDelta[i] * area;
      if (h < 40) profile.lowland += area;
      else if (h < 60) profile.midland += area;
      else if (h < 80) profile.highland += area;
      else profile.very_high += area;
      if (coastDistance > 0 && coastDistance <= 2) profile.near_coast += area;
    } else waterArea += area;

    const minX = Math.min(...bandPolygon.map(p => p[0]));
    const maxX = Math.max(...bandPolygon.map(p => p[0]));
    const lonMin = lonW + minX / width * (lonE - lonW);
    const lonMax = lonW + maxX / width * (lonE - lonW);
    const firstBin = Math.floor(lonMin);
    const lastBin = Math.floor(Math.min(lonMax, lonE - 1e-9));
    for (let bin = firstBin; bin <= lastBin; bin++) {
      const lo = Math.max(lonW, bin), hi = Math.min(lonE, bin + 1);
      if (hi <= lo) continue;
      const x0 = (lo - lonW) / (lonE - lonW) * width;
      const x1 = (hi - lonW) / (lonE - lonW) * width;
      const partArea = polygonArea(clipRect(polygon, x0, x1, yNorth, ySouth));
      if (partArea <= 1e-8) continue;
      const row = bins.get(bin) ?? {
        longitude_degree: bin, land_area_px2: 0, water_area_px2: 0, cells_intersecting: 0,
        lowland_area_px2: 0, midland_area_px2: 0, highland_area_px2: 0, very_high_area_px2: 0,
        near_coast_land_area_px2: 0, land_height_sum: 0, land_temperature_sum: 0, land_precipitation_sum: 0, roughness_sum: 0
      };
      row[isLand ? "land_area_px2" : "water_area_px2"] += partArea;
      if (isLand) {
        row.land_height_sum += h * partArea;
        row.land_temperature_sum += temp * partArea;
        row.land_precipitation_sum += prec * partArea;
        row.roughness_sum += maxNeighborDelta[i] * partArea;
        if (h < 40) row.lowland_area_px2 += partArea;
        else if (h < 60) row.midland_area_px2 += partArea;
        else if (h < 80) row.highland_area_px2 += partArea;
        else row.very_high_area_px2 += partArea;
        if (coastDistance > 0 && coastDistance <= 2) row.near_coast_land_area_px2 += partArea;
      }
      row.cells_intersecting++;
      bins.set(bin, row);
    }
  }
  const binRows = [...bins.values()].sort((a,b) => a.longitude_degree-b.longitude_degree).map(row => {
    const total = row.land_area_px2 + row.water_area_px2;
    const land = row.land_area_px2;
    return {
      longitude_degree: row.longitude_degree,
      land_area_px2: row.land_area_px2,
      water_area_px2: row.water_area_px2,
      cells_intersecting: row.cells_intersecting,
      total_area_px2: total,
      land_percent: total ? 100 * land / total : 0,
      mean_land_height_index: land ? row.land_height_sum / land : null,
      lowland_percent_of_land: land ? 100 * row.lowland_area_px2 / land : null,
      midland_percent_of_land: land ? 100 * row.midland_area_px2 / land : null,
      highland_percent_of_land: land ? 100 * row.highland_area_px2 / land : null,
      very_high_percent_of_land: land ? 100 * row.very_high_area_px2 / land : null,
      near_coast_percent_of_land: land ? 100 * row.near_coast_land_area_px2 / land : null,
      mean_land_temperature_c: land ? row.land_temperature_sum / land : null,
      mean_land_precipitation_index: land ? row.land_precipitation_sum / land : null,
      mean_max_neighbor_height_delta: land ? row.roughness_sum / land : null
    };
  });
  const totalArea = landArea + waterArea;

  // The Portal lies on the exact equator. Measure the line itself separately
  // from the 145 km corridor by intersecting every Voronoi cell polygon.
  const yEquator = latN / (latN - latS) * height;
  const equatorBins = new Map();
  const equatorProfile = {lowland:0, midland:0, highland:0, very_high:0, near_coast:0, land_height_sum:0, land_temperature_sum:0, land_precipitation_sum:0, roughness_sum:0};
  let landLine = 0, waterLine = 0, equatorCells = 0;
  for (let i = 0; i < cells.length; i++) {
    const polygon = cells[i];
    if (polygon.length < 3) continue;
    const xs = [];
    for (let j = 0; j < polygon.length; j++) {
      const a = polygon[j], b = polygon[(j + 1) % polygon.length];
      if ((a[1] <= yEquator && b[1] > yEquator) || (b[1] <= yEquator && a[1] > yEquator)) {
        const t = (yEquator - a[1]) / (b[1] - a[1]);
        xs.push(a[0] + t * (b[0] - a[0]));
      }
    }
    if (xs.length < 2) continue;
    const x0 = Math.max(0, Math.min(...xs));
    const x1 = Math.min(width, Math.max(...xs));
    if (x1 - x0 <= 1e-8) continue;
    equatorCells++;
    const h = heights[i], temp = temperatures[i], prec = precipitation[i], coastDistance = distance_to_water[i];
    const isLand = h >= 20;
    const segmentLength = x1 - x0;
    if (isLand) {
      landLine += segmentLength;
      equatorProfile.land_height_sum += h * segmentLength;
      equatorProfile.land_temperature_sum += temp * segmentLength;
      equatorProfile.land_precipitation_sum += prec * segmentLength;
      equatorProfile.roughness_sum += maxNeighborDelta[i] * segmentLength;
      if (h < 40) equatorProfile.lowland += segmentLength;
      else if (h < 60) equatorProfile.midland += segmentLength;
      else if (h < 80) equatorProfile.highland += segmentLength;
      else equatorProfile.very_high += segmentLength;
      if (coastDistance > 0 && coastDistance <= 2) equatorProfile.near_coast += segmentLength;
    } else waterLine += segmentLength;
    const lon0 = lonW + x0 / width * (lonE - lonW);
    const lon1 = lonW + x1 / width * (lonE - lonW);
    const first = Math.floor(lon0);
    const last = Math.floor(Math.min(lon1, lonE - 1e-9));
    for (let degree = first; degree <= last; degree++) {
      const lo = Math.max(lonW, degree), hi = Math.min(lonE, degree + 1);
      if (hi <= lo) continue;
      const bx0 = (lo - lonW) / (lonE - lonW) * width;
      const bx1 = (hi - lonW) / (lonE - lonW) * width;
      const overlap = Math.max(0, Math.min(x1, bx1) - Math.max(x0, bx0));
      if (overlap <= 1e-8) continue;
      const row = equatorBins.get(degree) ?? {
        longitude_degree: degree, land_length_px: 0, water_length_px: 0, cells_intersecting: 0,
        lowland_length_px: 0, midland_length_px: 0, highland_length_px: 0, very_high_length_px: 0,
        near_coast_land_length_px: 0, land_height_sum: 0, land_temperature_sum: 0,
        land_precipitation_sum: 0, roughness_sum: 0
      };
      row[isLand ? "land_length_px" : "water_length_px"] += overlap;
      if (isLand) {
        row.land_height_sum += h * overlap;
        row.land_temperature_sum += temp * overlap;
        row.land_precipitation_sum += prec * overlap;
        row.roughness_sum += maxNeighborDelta[i] * overlap;
        if (h < 40) row.lowland_length_px += overlap;
        else if (h < 60) row.midland_length_px += overlap;
        else if (h < 80) row.highland_length_px += overlap;
        else row.very_high_length_px += overlap;
        if (coastDistance > 0 && coastDistance <= 2) row.near_coast_land_length_px += overlap;
      }
      row.cells_intersecting++;
      equatorBins.set(degree, row);
    }
  }
  const equatorRows = [...equatorBins.values()].sort((a,b) => a.longitude_degree-b.longitude_degree).map(row => {
    const total = row.land_length_px + row.water_length_px;
    const land = row.land_length_px;
    return {
      longitude_degree: row.longitude_degree,
      land_length_px: land,
      water_length_px: row.water_length_px,
      cells_intersecting: row.cells_intersecting,
      total_length_px: total,
      land_percent: total ? 100 * land / total : 0,
      mean_land_height_index: land ? row.land_height_sum / land : null,
      lowland_percent_of_land: land ? 100 * row.lowland_length_px / land : null,
      midland_percent_of_land: land ? 100 * row.midland_length_px / land : null,
      highland_percent_of_land: land ? 100 * row.highland_length_px / land : null,
      very_high_percent_of_land: land ? 100 * row.very_high_length_px / land : null,
      near_coast_percent_of_land: land ? 100 * row.near_coast_land_length_px / land : null,
      mean_land_temperature_c: land ? row.land_temperature_sum / land : null,
      mean_land_precipitation_index: land ? row.land_precipitation_sum / land : null,
      mean_max_neighbor_height_delta: land ? row.roughness_sum / land : null
    };
  });
  const lineLength = landLine + waterLine;
  const equatorCsvPath = "mapas-azgaar/datos/ecuador-exacto/" + world + ".csv";
  fs.mkdirSync("mapas-azgaar/datos/ecuador-exacto", {recursive: true});
  const equatorHeaders = ["longitude_degree","land_length_px","water_length_px","cells_intersecting","total_length_px","land_percent","mean_land_height_index","lowland_percent_of_land","midland_percent_of_land","highland_percent_of_land","very_high_percent_of_land","near_coast_percent_of_land","mean_land_temperature_c","mean_land_precipitation_index","mean_max_neighbor_height_delta"];
  const equatorCsv = [equatorHeaders.join(","), ...equatorRows.map(row => equatorHeaders.map(key => row[key]).join(","))].join("\n") + "\n";
  fs.writeFileSync(equatorCsvPath, equatorCsv);
  const exactEquator = {
    latitude: 0,
    y_pixel: yEquator,
    land_length_px: landLine,
    water_length_px: waterLine,
    total_length_px: lineLength,
    land_percent: lineLength ? 100 * landLine / lineLength : null,
    water_percent: lineLength ? 100 * waterLine / lineLength : null,
    line_closure_error_percent: width ? 100 * Math.abs(width-lineLength) / width : null,
    intersecting_cells: equatorCells,
    terrain_profile: {
      mean_land_height_index: landLine ? equatorProfile.land_height_sum / landLine : null,
      lowland_percent_of_land: landLine ? 100 * equatorProfile.lowland / landLine : null,
      midland_percent_of_land: landLine ? 100 * equatorProfile.midland / landLine : null,
      highland_percent_of_land: landLine ? 100 * equatorProfile.highland / landLine : null,
      very_high_percent_of_land: landLine ? 100 * equatorProfile.very_high / landLine : null,
      near_coast_percent_of_land: landLine ? 100 * equatorProfile.near_coast / landLine : null,
      mean_land_temperature_c: landLine ? equatorProfile.land_temperature_sum / landLine : null,
      mean_land_precipitation_index: landLine ? equatorProfile.land_precipitation_sum / landLine : null,
      mean_max_neighbor_height_delta: landLine ? equatorProfile.roughness_sum / landLine : null
    },
    longitude_coverage_degrees: lonE-lonW,
    covers_full_circumference: lonW <= -179.999 && lonE >= 179.999,
    bins: equatorRows,
    csv_path: equatorCsvPath,
    method: "Exact horizontal-line intersection with reconstructed Azgaar Voronoi cell polygons at latitude 0"
  };

  const csvPath = path.join(outputDir, world + ".csv");
  const headers = ["longitude_degree","land_area_px2","water_area_px2","cells_intersecting","total_area_px2","land_percent","mean_land_height_index","lowland_percent_of_land","midland_percent_of_land","highland_percent_of_land","very_high_percent_of_land","near_coast_percent_of_land","mean_land_temperature_c","mean_land_precipitation_index","mean_max_neighbor_height_delta"];
  const csv = [headers.join(","), ...binRows.map(row => headers.map(key => row[key]).join(","))].join("\n") + "\n";
  fs.writeFileSync(csvPath, csv);
  return {
    world,
    geography: coordinates,
    equator: exactEquator,
    band: {
      definition: "145 km north-south, centered on the equator; 72.5 km meridional arc each side",
      datum: "WGS 84",
      latitude_limit_degrees: limit,
      y_north_px: yNorth,
      y_south_px: ySouth,
      expected_band_area_px2: expectedArea,
      reconstructed_band_area_px2: totalArea,
      area_closure_error_percent: expectedArea ? 100 * Math.abs(expectedArea-totalArea) / expectedArea : null,
      intersecting_grid_cells: cellsIntersecting,
      land_area_px2: landArea,
      water_area_px2: waterArea,
      land_percent: totalArea ? 100 * landArea / totalArea : null,
      water_percent: totalArea ? 100 * waterArea / totalArea : null,
      terrain_profile: {
        mean_land_height_index: landArea ? profile.land_height_sum / landArea : null,
        lowland_percent_of_land: landArea ? 100 * profile.lowland / landArea : null,
        midland_percent_of_land: landArea ? 100 * profile.midland / landArea : null,
        highland_percent_of_land: landArea ? 100 * profile.highland / landArea : null,
        very_high_percent_of_land: landArea ? 100 * profile.very_high / landArea : null,
        near_coast_percent_of_land: landArea ? 100 * profile.near_coast / landArea : null,
        mean_land_temperature_c: landArea ? profile.land_temperature_sum / landArea : null,
        mean_land_precipitation_index: landArea ? profile.land_precipitation_sum / landArea : null,
        mean_max_neighbor_height_delta: landArea ? profile.roughness_sum / landArea : null,
        elevation_note: "Azgaar relative height index grouped into 20–39, 40–59, 60–79 and 80–100; not metres",
        coastal_note: "Near-coast proxy: land cells with positive distance-field value <= 2 grid steps",
        roughness_note: "Area-weighted maximum height-index difference between neighbouring grid cells; not a physical slope"
      },
      longitude_coverage_degrees: lonE-lonW,
      covers_full_circumference: lonW <= -179.999 && lonE >= 179.999,
      bins: binRows,
      csv_path: csvPath,
      method: "Azgaar Delaunator Voronoi reconstruction from original grid points and boundary pseudo-points; polygon clipping to the equatorial band"
    }
  };
}

const reports = worlds.map(inspectWorld);
const summaryReports = reports.map(report => ({
  world: report.world,
  geography: report.geography,
  equator: {...report.equator, bins: undefined},
  band: {...report.band, bins: undefined}
}));
fs.writeFileSync("mapas-azgaar/datos/franja-ecuatorial.json", JSON.stringify(summaryReports, null, 2) + "\n");

// A common 360-degree longitude strip makes missing map coverage explicit.
const chartWorlds = ["Amitia", "Teknara", "Atharis", "Khorza", "Derat", "Návar", "Terra"];
const chartWidth = 1800, labelWidth = 145, plotWidth = 1500, rowHeight = 42, top = 100;
const chartHeight = top + chartWorlds.length * rowHeight + 145;
const xAt = lon => labelWidth + (lon + 180) / 360 * plotWidth;
const interpolate = (a, b, t) => a.map((v, i) => Math.round(v + (b[i] - v) * t));
const color = land => {
  const water = [103, 164, 190], landColor = [104, 133, 79];
  const rgb = interpolate(water, landColor, Math.max(0, Math.min(1, land / 100)));
  return "#" + rgb.map(v => v.toString(16).padStart(2, "0")).join("");
};
const defs = '<defs>' +
  '<pattern id="unknown" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e4e6e7"/><path d="M-2 2 L2 -2 M0 8 L8 0 M6 10 L10 6" stroke="#a9afb3" stroke-width="1"/></pattern>' +
  '<pattern id="pending" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#f1e8d4"/><path d="M0 0 L8 8 M8 0 L0 8" stroke="#c6a76a" stroke-width="1"/></pattern>' +
  '</defs>';
let chart = '<svg xmlns="http://www.w3.org/2000/svg" width="' + chartWidth + '" height="' + chartHeight + '" viewBox="0 0 ' + chartWidth + ' ' + chartHeight + '">' + defs;
chart += '<rect width="100%" height="100%" fill="#ffffff"/>';
chart += '<text x="24" y="38" font-family="sans-serif" font-size="25" font-weight="700" fill="#20252a">Cobertura ecuatorial del Portal — comparación de los seis mapas</text>';
chart += '<text x="24" y="66" font-family="sans-serif" font-size="14" fill="#4b535a">Cada columna representa 1° de longitud. El color mezcla la proporción de tierra y agua dentro de la banda de 145 km.</text>';
for (let row = 0; row < chartWorlds.length; row++) {
  const world = chartWorlds[row], y = top + row * rowHeight;
  chart += '<text x="20" y="' + (y + 25) + '" font-family="sans-serif" font-size="16" font-weight="600" fill="#20252a">' + world + '</text>';
  const report = reports.find(r => r.world === world);
  const byBin = new Map((report?.band.bins ?? []).map(b => [b.longitude_degree, b]));
  for (let degree = -180; degree < 180; degree++) {
    const bin = byBin.get(degree);
    const fill = world === "Terra" ? "url(#pending)" : bin ? color(bin.land_percent) : "url(#unknown)";
    chart += '<rect x="' + xAt(degree).toFixed(3) + '" y="' + y + '" width="' + (plotWidth / 360 + 0.15).toFixed(3) + '" height="30" fill="' + fill + '" stroke="#ffffff" stroke-width="0.35"/>';
  }
  chart += '<rect x="' + labelWidth + '" y="' + y + '" width="' + plotWidth + '" height="30" fill="none" stroke="#727a80" stroke-width="0.7"/>';
  if (world === "Terra") {
    chart += '<text x="' + (labelWidth + plotWidth + 12) + '" y="' + (y + 21) + '" font-family="sans-serif" font-size="13" fill="#7b5c25">Base global pendiente</text>';
  } else {
    chart += '<text x="' + (labelWidth + plotWidth + 12) + '" y="' + (y + 21) + '" font-family="sans-serif" font-size="13" fill="#4b535a">' + report.band.longitude_coverage_degrees.toFixed(1) + '°</text>';
  }
}
const axisY = top + chartWorlds.length * rowHeight + 12;
for (const tick of [-180, -120, -60, 0, 60, 120, 180]) {
  const x = xAt(tick);
  chart += '<line x1="' + x + '" y1="' + (top - 12) + '" x2="' + x + '" y2="' + axisY + '" stroke="#6e777d" stroke-opacity="0.28" stroke-width="1"/>';
  chart += '<text x="' + x + '" y="' + (axisY + 22) + '" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#343b40">' + tick + '°</text>';
}
const legendY = axisY + 60;
const legendItems = [
  ["#67a4be", "Predominio de agua"],
  ["#a4a07f", "Superficie mixta"],
  ["#68854f", "Predominio de tierra"],
  ["url(#unknown)", "Sin cobertura en el mapa"],
  ["url(#pending)", "Terra: base física pendiente"]
];
let lx = 24;
for (const [fill, label] of legendItems) {
  chart += '<rect x="' + lx + '" y="' + legendY + '" width="22" height="16" fill="' + fill + '" stroke="#6e777d" stroke-width="0.6"/>';
  chart += '<text x="' + (lx + 29) + '" y="' + (legendY + 13) + '" font-family="sans-serif" font-size="12" fill="#343b40">' + label + '</text>';
  lx += label.length * 7.2 + 65;
}
chart += '<text x="24" y="' + (chartHeight - 15) + '" font-family="sans-serif" font-size="11" fill="#60686e">El gris indica falta de datos cartográficos en la fuente, no océano. Esta franja no representa por sí sola accesibilidad ni seguridad.</text>';
chart += '</svg>';
const chartSvgPath = "mapas-azgaar/visualizaciones/Portal-cobertura-ecuatorial.svg";
const chartPngPath = "mapas-azgaar/visualizaciones/Portal-cobertura-ecuatorial.png";
fs.writeFileSync(chartSvgPath, chart);
const {execFileSync} = await import("node:child_process");
execFileSync("rsvg-convert", ["-o", chartPngPath, chartSvgPath]);

// Exact equator line: unlike the 145 km corridor, this is where the Portal sits.
let lineChart = '<svg xmlns="http://www.w3.org/2000/svg" width="' + chartWidth + '" height="' + chartHeight + '" viewBox="0 0 ' + chartWidth + ' ' + chartHeight + '">' + defs;
lineChart += '<rect width="100%" height="100%" fill="#ffffff"/>';
lineChart += '<text x="24" y="38" font-family="sans-serif" font-size="25" font-weight="700" fill="#20252a">Tierra y agua sobre el ecuador exacto del Portal</text>';
lineChart += '<text x="24" y="66" font-family="sans-serif" font-size="14" fill="#4b535a">Cada columna representa 1° de longitud. El color muestra la proporción de tierra y agua en la línea de latitud 0°.</text>';
for (let row = 0; row < chartWorlds.length; row++) {
  const world = chartWorlds[row], y = top + row * rowHeight;
  lineChart += '<text x="20" y="' + (y + 25) + '" font-family="sans-serif" font-size="16" font-weight="600" fill="#20252a">' + world + '</text>';
  const report = reports.find(r => r.world === world);
  const byBin = new Map((report?.equator.bins ?? []).map(b => [b.longitude_degree, b]));
  for (let degree = -180; degree < 180; degree++) {
    const bin = byBin.get(degree);
    const fill = world === "Terra" ? "url(#pending)" : bin ? color(bin.land_percent) : "url(#unknown)";
    lineChart += '<rect x="' + xAt(degree).toFixed(3) + '" y="' + y + '" width="' + (plotWidth / 360 + 0.15).toFixed(3) + '" height="30" fill="' + fill + '" stroke="#ffffff" stroke-width="0.35"/>';
  }
  lineChart += '<rect x="' + labelWidth + '" y="' + y + '" width="' + plotWidth + '" height="30" fill="none" stroke="#727a80" stroke-width="0.7"/>';
  if (world === "Terra") {
    lineChart += '<text x="' + (labelWidth + plotWidth + 12) + '" y="' + (y + 21) + '" font-family="sans-serif" font-size="13" fill="#7b5c25">Base global pendiente</text>';
  } else {
    lineChart += '<text x="' + (labelWidth + plotWidth + 12) + '" y="' + (y + 21) + '" font-family="sans-serif" font-size="13" fill="#4b535a">' + report.equator.longitude_coverage_degrees.toFixed(1) + '°</text>';
  }
}
const lineAxisY = top + chartWorlds.length * rowHeight + 12;
for (const tick of [-180, -120, -60, 0, 60, 120, 180]) {
  const x = xAt(tick);
  lineChart += '<line x1="' + x + '" y1="' + (top - 12) + '" x2="' + x + '" y2="' + lineAxisY + '" stroke="#6e777d" stroke-opacity="0.28" stroke-width="1"/>';
  lineChart += '<text x="' + x + '" y="' + (lineAxisY + 22) + '" text-anchor="middle" font-family="sans-serif" font-size="13" fill="#343b40">' + tick + '°</text>';
}
const lineLegendY = lineAxisY + 60;
let lineLegendX = 24;
for (const [fill, label] of legendItems) {
  lineChart += '<rect x="' + lineLegendX + '" y="' + lineLegendY + '" width="22" height="16" fill="' + fill + '" stroke="#6e777d" stroke-width="0.6"/>';
  lineChart += '<text x="' + (lineLegendX + 29) + '" y="' + (lineLegendY + 13) + '" font-family="sans-serif" font-size="12" fill="#343b40">' + label + '</text>';
  lineLegendX += label.length * 7.2 + 65;
}
lineChart += '<text x="24" y="' + (chartHeight - 15) + '" font-family="sans-serif" font-size="11" fill="#60686e">El gris indica falta de cobertura en el mapa fuente, no océano. La banda de 145 km es un análisis separado del terreno cercano al Portal.</text>';
lineChart += '</svg>';
const lineSvgPath = "mapas-azgaar/visualizaciones/Portal-linea-ecuatorial.svg";
const linePngPath = "mapas-azgaar/visualizaciones/Portal-linea-ecuatorial.png";
fs.writeFileSync(lineSvgPath, lineChart);
execFileSync("rsvg-convert", ["-o", linePngPath, lineSvgPath]);

console.log(JSON.stringify(reports.map(r => ({
  world: r.world,
  longitude_coverage_degrees: r.band.longitude_coverage_degrees,
  covers_full_circumference: r.band.covers_full_circumference,
  intersecting_grid_cells: r.band.intersecting_grid_cells,
  land_percent: r.band.land_percent,
  water_percent: r.band.water_percent,
  area_closure_error_percent: r.band.area_closure_error_percent,
  csv_path: r.band.csv_path
})), null, 2));
