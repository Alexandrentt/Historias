#!/usr/bin/env python3
"""Exporta polígonos de celdas Azgaar de Alfaguara desde un .map 1.158.0.

La geometría de las celdas empaquetadas no está serializada como polígonos en el
formato .map legado. Este programa regenera los puntos pack con las mismas reglas
del build de Derat y reconstruye sus regiones Voronoi de forma independiente.
Por ello, las geometrías exportadas son derivadas y deben conservar esa procedencia.

Dependencias probadas: numpy, scipy y shapely. No modifica el .map ni el GeoJSON fuente.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, Point, box, shape
from shapely.strtree import STRtree


def parse_records(path: Path) -> tuple[bytes, list[str], dict, dict, dict]:
    raw = path.read_bytes()
    records = raw.decode("utf-8").split("\r\n")
    if len(records) != 56:
        raise ValueError(f"Se esperaban 56 registros CRLF; se encontraron {len(records)}")
    header = records[0].split("|")
    if header[0] != "1.158.0":
        raise ValueError(f"Este exportador está fijado a Azgaar 1.158.0; recibido {header[0]!r}")
    settings = json.loads(records[1])
    grid = json.loads(records[6])
    return raw, records, settings, grid, json.loads(records[12])


def export(map_path: Path, continents_path: Path, output_path: Path, continent_name: str) -> dict:
    raw, records, settings, grid, grid_features = parse_records(map_path)
    header = records[0].split("|")
    width, height = map(int, header[4:6])
    points = np.asarray(grid["points"], dtype=float)
    boundary = np.asarray(grid["boundary"], dtype=float)
    grid_count = len(points)
    heights = np.fromstring(records[7], sep=",", dtype=np.uint8)
    distance = np.fromstring(records[10], sep=",", dtype=np.int8)
    grid_feature_ids = np.fromstring(records[9], sep=",", dtype=np.uint16)
    if not (len(heights) == len(distance) == len(grid_feature_ids) == grid_count):
        raise ValueError("Los arrays de cuadrícula no coinciden con grid.points")

    source = json.loads(continents_path.read_text(encoding="utf-8"))
    if source.get("type") != "FeatureCollection":
        raise ValueError("El archivo de continentes no es una FeatureCollection")
    continent_polygons = {
        feature["properties"]["name"]: Polygon(feature["geometry"]["coordinates"][0])
        for feature in source["features"]
        if feature.get("geometry", {}).get("type") == "Polygon"
    }
    if continent_name not in continent_polygons:
        raise ValueError(f"No se encontró el polígono de {continent_name!r}")

    def continent_at(x: float, y: float) -> str | None:
        lon = x / width * 360 - 180
        lat = 90 - y / height * 180
        point = Point(lon, lat)
        for name, polygon in continent_polygons.items():
            if polygon.contains(point):
                return name
        return None

    grid_continents = [continent_at(x, y) for x, y in points]

    # Reconstruye vecindades de cuadrícula con Voronoi; se comprueba el mismo recuento
    # de pack points que el generador publicado para esta versión del mapa.
    grid_voronoi = Voronoi(np.vstack([points, boundary]))
    neighbors = [set() for _ in range(grid_count)]
    border_cells = np.zeros(grid_count, dtype=bool)
    for a, b in grid_voronoi.ridge_points:
        if a < grid_count:
            if b < grid_count:
                neighbors[a].add(int(b))
                neighbors[b].add(int(a))
            else:
                border_cells[a] = True
        if b < grid_count and a >= grid_count:
            border_cells[b] = True

    split = grid["spacing"] * (1 + (0.9 - settings["graph"]["jitter"]))
    split_squared = split * split
    pack_points: list[list[float]] = []
    parent_points: list[int] = []
    pack_heights: list[int] = []
    pack_continents: list[str | None] = []
    for i, (x, y) in enumerate(points):
        h = int(heights[i])
        d = int(distance[i])
        if h < 20 and d not in (-1, -2):
            continue
        if d == -2 and (i % 4 == 0 or grid_features[int(grid_feature_ids[i]) - 1]["type"] == "lake"):
            continue
        pack_points.append([x, y])
        parent_points.append(i)
        pack_heights.append(h)
        pack_continents.append(grid_continents[i])
        if d in (1, -1):
            if border_cells[i]:
                continue
            for j in sorted(neighbors[i]):
                if i > j or int(distance[j]) != d:
                    continue
                xx, yy = points[j]
                if (y - yy) ** 2 + (x - xx) ** 2 < split_squared:
                    continue
                pack_points.append([(x + xx) / 2, (y + yy) / 2])
                parent_points.append(i)
                pack_heights.append(h)
                pack_continents.append(grid_continents[i])

    pack_points_array = np.asarray(pack_points, dtype=float)
    pack_count = len(pack_points_array)
    if pack_count != 31299:
        raise ValueError(f"Recuento pack inesperado: {pack_count}; se esperaba 31299")

    array_records = {
        "biome_id": 16, "burg_id": 17, "confidence": 18, "culture_id": 19,
        "river_id": 20, "population_raw": 21, "religion_id": 26,
        "province_id": 27, "state_id": 25, "good_id": 40,
        "market_id": 44, "prosperity": 54, "development": 55,
    }
    attributes = {name: np.fromstring(records[index], sep=",", dtype=float)
                  for name, index in array_records.items()}
    for name, values in attributes.items():
        if len(values) != pack_count:
            raise ValueError(f"Array {name} tiene {len(values)} valores; se esperaban {pack_count}")

    pack_voronoi = Voronoi(np.vstack([pack_points_array, boundary]))
    frame = box(0, 0, width, height)
    selected = [i for i, name in enumerate(pack_continents) if name == continent_name]
    features = []
    empty_regions = 0
    for i in selected:
        region = pack_voronoi.regions[pack_voronoi.point_region[i]]
        if not region or -1 in region:
            empty_regions += 1
            continue
        polygon = Polygon(pack_voronoi.vertices[region]).intersection(frame)
        if polygon.is_empty or polygon.area <= 1e-8:
            empty_regions += 1
            continue
        if polygon.geom_type == "MultiPolygon":
            polygon = max(polygon.geoms, key=lambda part: part.area)
        if not polygon.is_valid:
            raise ValueError(f"Celda {i} inválida: {polygon.wkt[:160]}")

        def to_lonlat(x: float, y: float) -> list[float]:
            return [round(x / width * 360 - 180, 7), round(90 - y / height * 180, 7)]

        ring = [to_lonlat(x, y) for x, y in polygon.exterior.coords]
        if ring[0] != ring[-1]:
            ring.append(ring[0])
        parent = int(parent_points[i])
        center = to_lonlat(*pack_points_array[i])
        parent_center = to_lonlat(*points[parent])
        props = {
            "cell_id": i,
            "parent_grid_point": parent,
            "center_lonlat": center,
            "parent_lonlat": parent_center,
            "continent_candidate": continent_name,
            "continent_status": "propuesta geográfica; no canon",
            "height_native_reconstructed": int(pack_heights[i]),
            "provenance": "Atributos serializados en Azgaar 1.158.0; centro/celda reconstruidos independientemente por Voronoi desde grid.points + boundary; no es geometría guardada literalmente en .map",
        }
        for name, values in attributes.items():
            value = float(values[i])
            props[name] = round(value, 4) if name == "population_raw" else int(value)
        features.append({"type": "Feature", "id": f"azgaar-pack-cell-{i}",
                         "properties": props,
                         "geometry": {"type": "Polygon", "coordinates": [ring]}})

    output_geometries = [shape(feature["geometry"]) for feature in features]
    invalid = sum(not geometry.is_valid for geometry in output_geometries)
    if invalid:
        raise ValueError(f"{invalid} celdas inválidas después de redondear coordenadas")
    tree = STRtree(output_geometries)
    overlaps = 0
    for i, geometry in enumerate(output_geometries):
        for j in tree.query(geometry):
            j = int(j)
            if j > i and geometry.intersection(output_geometries[j]).area > 1e-7:
                overlaps += 1
    if overlaps:
        raise ValueError(f"Se detectaron {overlaps} solapamientos de área positiva")

    collection = {
        "type": "FeatureCollection",
        "name": f"Celdas Voronoi reconstruidas de {continent_name} — Azgaar 1.158.0",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "metadata": {
            "source_map": map_path.name,
            "source_map_sha256": hashlib.sha256(raw).hexdigest(),
            "source_map_bytes": len(raw),
            "map_version": "1.158.0",
            "seed": settings["seed"],
            "grid_points": grid_count,
            "packed_cells_total": pack_count,
            "selected_cells": len(selected),
            "exported_cells": len(features),
            "method": "pack points regenerados con las reglas del build; polígonos reconstruidos independientemente con scipy.spatial.Voronoi y recortados al marco nativo; transformación a CRS84",
            "status": "geometría derivada editable; no son coordenadas de polígonos guardadas literalmente en .map",
            "warnings": [
                "Este es el mapa nuevo de tres continentes, no el mapa regional original de Alfaguara.",
                "Los atributos de Azgaar son datos generados, no canon narrativo.",
                "Las geometrías de celdas se reconstruyen independientemente desde los puntos nativos.",
                "La importación del .map en la interfaz Azgaar no se ha probado en vivo.",
            ],
        },
        "features": features,
    }
    output_path.write_text(json.dumps(collection, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "output": str(output_path), "bytes": output_path.stat().st_size,
        "source_map_sha256": collection["metadata"]["source_map_sha256"],
        "grid_points": grid_count, "packed_cells": pack_count,
        "selected_cells": len(selected), "exported_cells": len(features),
        "empty_regions": empty_regions, "invalid_geometries": invalid,
        "positive_area_overlaps": overlaps,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", type=Path, default=Path("Derat_Azgaar_Tres_Continentes_v1.map"))
    parser.add_argument("--continents", type=Path, default=Path("Derat_Azgaar_Tres_Continentes/Derat_continentes.geojson"))
    parser.add_argument("--continent", default="Alfaguara")
    parser.add_argument("--out", type=Path, default=Path("Derat_Azgaar_celdas_Alfaguara_v1.geojson"))
    args = parser.parse_args()
    print(json.dumps(export(args.map, args.continents, args.out, args.continent), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()