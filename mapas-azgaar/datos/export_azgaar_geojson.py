#!/usr/bin/env python3
"""Exporta capas GeoJSON desde el JSON "Full" de Azgaar Fantasy Map Generator.

Uso:
  python export_azgaar_geojson.py mapa_full.json --out mapas_geojson/Mundo

El JSON de entrada se obtiene abriendo el .map original en Azgaar y usando
Export -> Export To JSON -> Full. El script no modifica el .map original.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def feature(geometry: dict[str, Any] | None, properties: dict[str, Any]) -> dict[str, Any]:
    return {"type": "Feature", "geometry": geometry, "properties": properties}


def collection(features: list[dict[str, Any]]) -> dict[str, Any]:
    return {"type": "FeatureCollection", "features": features}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="JSON Full exportado por Azgaar")
    parser.add_argument("--out", type=Path, required=True, help="Carpeta de salida")
    args = parser.parse_args()

    root = json.loads(args.source.read_text(encoding="utf-8-sig"))
    pack = root["pack"]
    info = root.get("info", {})
    coords = root["mapCoordinates"]
    width = float(info["width"])
    height = float(info["height"])

    def geographic(point: list[float]) -> list[float]:
        x, y = point
        lon = round(float(coords["lonW"]) + (float(x) / width) * float(coords["lonT"]), 4)
        lat = round(float(coords["latN"]) - (float(y) / height) * float(coords["latT"]), 4)
        return [lon, lat]

    vertices = pack["vertices"]
    vertex_points = {int(v["i"]): v["p"] for v in vertices}
    cell_rows = pack["cells"]["cells"]
    cells_by_id = {int(c["i"]): c for c in cell_rows}
    cell_geometries: dict[int, dict[str, Any]] = {}

    def cell_geometry(cell: dict[str, Any]) -> dict[str, Any] | None:
        ids = cell.get("v") or []
        ring = [geographic(vertex_points[int(vertex_id)]) for vertex_id in ids if int(vertex_id) in vertex_points]
        if len(ring) < 3:
            return None
        if ring[0] != ring[-1]:
            ring.append(ring[0])
        return {"type": "Polygon", "coordinates": [ring]}

    features_catalog = pack.get("features", [])
    cell_features = []
    for cell in cell_rows:
        cid = int(cell["i"])
        geometry = cell_geometry(cell)
        if geometry is None:
            continue
        cell_geometries[cid] = geometry
        feature_id = int(cell.get("f", 0) or 0)
        map_feature = features_catalog[feature_id] if 0 <= feature_id < len(features_catalog) else {}
        properties = {
            "id": cid,
            "height_raw": cell.get("h"),
            "biome": cell.get("biome"),
            "feature_type": map_feature.get("type"),
            "feature_id": feature_id,
            "population_raw": cell.get("pop"),
            "state": cell.get("state"),
            "province": cell.get("province"),
            "culture": cell.get("culture"),
            "religion": cell.get("religion"),
            "burg": cell.get("burg"),
            "neighbors": cell.get("c", []),
            "area_raw": cell.get("area"),
            "development": cell.get("development"),
            "prosperity": cell.get("prosperity"),
        }
        cell_features.append(feature(geometry, properties))

    args.out.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, list[dict[str, Any]]] = {"cells": cell_features}

    route_features = []
    for route in pack.get("routes", []):
        points = route.get("points") or []
        line = [geographic(point) for point in points]
        if len(line) >= 2:
            route_features.append(feature(
                {"type": "LineString", "coordinates": line},
                {k: route.get(k) for k in ("i", "group", "name")}
            ))
    outputs["routes"] = route_features

    river_features = []
    for river in pack.get("rivers", []):
        points = river.get("points") or []
        line = [geographic(point) for point in points]
        if len(line) >= 2:
            river_features.append(feature(
                {"type": "LineString", "coordinates": line},
                {k: river.get(k) for k in (
                    "i", "source", "mouth", "parent", "basin", "widthFactor",
                    "sourceWidth", "discharge", "name", "type", "group"
                )}
            ))
    outputs["rivers"] = river_features

    marker_features = []
    for marker in pack.get("markers", []):
        if marker.get("x") is None or marker.get("y") is None:
            continue
        marker_features.append(feature(
            {"type": "Point", "coordinates": geographic([marker["x"], marker["y"]])},
            {k: marker.get(k) for k in (
                "i", "type", "icon", "x", "y", "name", "note", "size", "fill", "stroke"
            )}
        ))
    outputs["markers"] = marker_features

    zone_features = []
    for zone in pack.get("zones", []):
        polygons = []
        for cell_id in zone.get("cells") or []:
            geometry = cell_geometries.get(int(cell_id))
            if geometry and geometry["type"] == "Polygon":
                polygons.append(geometry["coordinates"])
        if not polygons:
            continue
        geometry = {"type": "MultiPolygon", "coordinates": polygons}
        zone_features.append(feature(geometry, {
            "id": zone.get("i"),
            "name": zone.get("name"),
            "type": zone.get("type"),
            "color": zone.get("color"),
            "cell_ids": zone.get("cells", []),
        }))
    outputs["zones"] = zone_features

    summary = {
        "source": str(args.source),
        "map_name": info.get("mapName"),
        "azgaar_version": info.get("version"),
        "crs": "OGC:CRS84",
        "coordinate_order": "[longitude, latitude]",
        "features": {name: len(items) for name, items in outputs.items()},
        "note": "height_raw y population_raw conservan los valores internos exportados; no se reinterpretan como unidades físicas."
    }

    for name, items in outputs.items():
        path = args.out / f"{name}.geojson"
        path.write_text(json.dumps(collection(items), ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        print(f"{path}: {len(items)} entidades")
    (args.out / "export_manifest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
