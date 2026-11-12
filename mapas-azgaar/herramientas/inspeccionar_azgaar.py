#!/usr/bin/env python3
"""Read-only extraction and audit of the original Azgaar map sources."""
from __future__ import annotations
import csv, gzip, hashlib, json, math, pathlib, subprocess, zipfile
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(".")
DATA = ROOT / "mapas-azgaar" / "datos"
SVG_OUT = ROOT / "mapas-azgaar" / "visualizaciones" / "fuentes"
PNG_OUT = ROOT / "mapas-azgaar" / "visualizaciones" / "vistas-previas"
BAND_OUT = DATA / "muestras-centros-franja-ecuatorial"
ARCHIVE = ROOT / "Historias_mapas_gz_GitHub.zip"
STANDALONE = ROOT / "Teknara.map.gz"
WORLD_BY_FILE = {
    "Amitia.map.gz": "Amitia",
    "Atharis.map.gz": "Atharis",
    "derat(continente de alfaguara).map.gz": "Derat",
    "Korza .map.gz": "Khorza",
    "Návar.map.gz": "Návar",
    "Teknara.map.gz": "Teknara",
}
RECORDS = {
    0: "header", 1: "map_options", 2: "deprecated_map_coordinates",
    3: "biomes", 4: "deprecated_notes", 5: "svg",
    6: "grid_metadata", 7: "grid_height", 8: "grid_precipitation",
    9: "grid_feature_ids", 10: "grid_distance_to_water", 11: "grid_temperature",
    12: "pack_features", 13: "cultures", 14: "states", 15: "burgs",
    16: "pack_biome_ids", 17: "pack_burg_ids", 18: "pack_confluence",
    19: "pack_culture_ids", 20: "pack_river_flux", 21: "pack_population",
    22: "pack_river_ids", 23: "deprecated_roads", 24: "pack_cell_score",
    25: "pack_state_ids", 26: "pack_religion_ids", 27: "pack_province_ids",
    28: "deprecated_crossroads", 29: "religions", 30: "provinces",
    31: "name_bases", 32: "rivers", 33: "deprecated_rulers", 34: "fonts",
    35: "markers", 36: "cell_routes", 37: "routes", 38: "zones", 39: "ice",
    40: "pack_good_ids", 41: "deprecated_goods", 42: "markets", 43: "deals",
    44: "pack_market_ids", 45: "deprecated_custom_good_icons",
    46: "measurers", 47: "added_labels", 48: "styles", 49: "relief",
    50: "layers", 51: "graph_overrides", 52: "journeys", 53: "legends",
    54: "pack_prosperity", 55: "pack_development",
}

def parse_json(records, index, default=None):
    value = records[index] if index < len(records) else ""
    return json.loads(value) if value else default

def parse_numbers(records, index):
    value = records[index] if index < len(records) else ""
    return [float(part) if "." in part else int(part) for part in value.split(",")] if value else []

def summarize_array(values):
    if not isinstance(values, list):
        return {"type": type(values).__name__}
    return {"count": len(values), "item_type": type(values[0]).__name__ if values else None}

def latitude_limit_for_meridian_distance(distance_m):
    # WGS84 meridional arc, inverted by bisection from the equator.
    a = 6378137.0
    flattening = 1 / 298.257223563
    e2 = flattening * (2 - flattening)
    e4, e6 = e2**2, e2**3
    def meridian_arc(phi):
        return a * (
            (1 - e2/4 - 3*e4/64 - 5*e6/256) * phi
            - (3*e2/8 + 3*e4/32 + 45*e6/1024) * math.sin(2*phi)
            + (15*e4/256 + 45*e6/1024) * math.sin(4*phi)
            - (35*e6/3072) * math.sin(6*phi)
        )
    lo, hi = 0.0, math.radians(2)
    for _ in range(80):
        mid = (lo + hi) / 2
        if meridian_arc(mid) < distance_m:
            lo = mid
        else:
            hi = mid
    return math.degrees((lo + hi) / 2)

def inspect(filename, compressed, raw, container):
    # Split only on CRLF record separators; the SVG record contains LF.
    records = raw.decode("utf-8").split("\r\n")
    if len(records) != 56:
        raise ValueError(f"{filename}: expected 56 records, found {len(records)}")
    header = records[0].split("|")
    options = parse_json(records, 1, {})
    grid = parse_json(records, 6, {})
    heights = parse_numbers(records, 7)
    precipitation = parse_numbers(records, 8)
    feature_ids = parse_numbers(records, 9)
    distance_to_water = parse_numbers(records, 10)
    temperatures = parse_numbers(records, 11)
    states = parse_json(records, 14, [])
    burgs = parse_json(records, 15, [])
    cultures = parse_json(records, 13, [])
    religions = parse_json(records, 29, [])
    provinces = parse_json(records, 30, [])
    rivers = parse_json(records, 32, [])
    routes = parse_json(records, 37, [])
    markers = parse_json(records, 35, [])
    zones = parse_json(records, 38, [])
    biomes = parse_json(records, 3, [])
    pack_features = parse_json(records, 12, [])
    grid_points = grid.get("points", [])
    land = sum(1 for value in heights if value >= 20)
    water = sum(1 for value in heights if value < 20)

    world = WORLD_BY_FILE[filename]
    source_svg = records[5]
    svg_path = SVG_OUT / f"{world}.svg.gz"
    png_path = PNG_OUT / f"{world}.png"
    SVG_OUT.mkdir(parents=True, exist_ok=True)
    PNG_OUT.mkdir(parents=True, exist_ok=True)
    ET.fromstring(source_svg)
    with gzip.open(svg_path, "wb", compresslevel=9) as stream:
        stream.write(source_svg.encode("utf-8"))
    temp_svg = pathlib.Path("/tmp") / f"{world}.svg"
    temp_svg.write_text(source_svg, encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "2000", "-o", str(png_path), str(temp_svg)], check=True)

    # Azgaar's geographic canvas is equirectangular: grid point centers map
    # linearly to the configured latitude and longitude bounds.
    coordinates = options.get("geography", {}).get("coordinates", {})
    lat_n, lat_s = coordinates.get("latN", 90), coordinates.get("latS", -90)
    lon_w, lon_e = coordinates.get("lonW", -180), coordinates.get("lonE", 180)
    width, height = int(header[4]), int(header[5])
    band_limit = latitude_limit_for_meridian_distance(72500)
    y_north = (lat_n - band_limit) / (lat_n - lat_s) * height
    y_south = (lat_n + band_limit) / (lat_n - lat_s) * height
    band_preview_path = PNG_OUT / f"{world}-franja-ecuatorial.png"
    overlay = (
        f'<rect x="0" y="{y_north:.6f}" width="{width}" height="{y_south-y_north:.6f}" '
        'fill="#ff3b30" fill-opacity="0.28" stroke="#ff3b30" stroke-width="1.5"/>'
        f'<line x1="0" x2="{width}" y1="{height/2 if lat_n == -lat_s else (lat_n/(lat_n-lat_s)*height):.6f}" '
        f'y2="{height/2 if lat_n == -lat_s else (lat_n/(lat_n-lat_s)*height):.6f}" '
        'stroke="#ff3b30" stroke-width="1.5"/>'
    )
    closing = source_svg.rfind("</svg>")
    if closing < 0:
        raise ValueError(f"{world}: SVG closing tag not found")
    band_svg = source_svg[:closing] + overlay + source_svg[closing:]
    temp_band_svg = pathlib.Path("/tmp") / f"{world}-franja.svg"
    temp_band_svg.write_text(band_svg, encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "2000", "-o", str(band_preview_path), str(temp_band_svg)], check=True)
    band_rows, longitude_bins = [], {}
    for cell_id, point in enumerate(grid_points):
        if cell_id >= len(heights) or not isinstance(point, list) or len(point) < 2:
            continue
        x, y = point[0], point[1]
        if not (0 <= x <= width and 0 <= y <= height):
            continue
        lat = lat_n - (y / height) * (lat_n - lat_s)
        if abs(lat) > band_limit:
            continue
        lon = lon_w + (x / width) * (lon_e - lon_w)
        h = heights[cell_id]
        band_rows.append({
            "cell_id": cell_id, "longitude": round(lon, 6), "latitude": round(lat, 6),
            "height": h, "land": int(h >= 20),
            "precipitation": precipitation[cell_id] if cell_id < len(precipitation) else "",
            "temperature": temperatures[cell_id] if cell_id < len(temperatures) else "",
            "feature_id": feature_ids[cell_id] if cell_id < len(feature_ids) else "",
            "distance_to_water": distance_to_water[cell_id] if cell_id < len(distance_to_water) else "",
        })
        key = math.floor(lon)
        bucket = longitude_bins.setdefault(key, {"land": 0, "water": 0, "samples": 0})
        bucket["samples"] += 1
        bucket["land" if h >= 20 else "water"] += 1

    BAND_OUT.mkdir(parents=True, exist_ok=True)
    band_path = BAND_OUT / f"{world}.csv"
    fields = ["cell_id", "longitude", "latitude", "height", "land", "precipitation", "temperature", "feature_id", "distance_to_water"]
    with band_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(band_rows)
    band_land = sum(row["land"] for row in band_rows)
    band_water = len(band_rows) - band_land
    band_summary = {
        "definition": "145 km north-south, centered on latitude 0",
        "wgs84_limit_degrees_approx": round(band_limit, 7),
        "method": "equirectangular bounds + grid point centers; preliminary sample, not polygon intersection",
        "sampled_cells": len(band_rows), "land_samples": band_land, "water_samples": band_water,
        "land_sample_percent": round(100 * band_land / len(band_rows), 2) if band_rows else None,
        "longitude_min_sampled": round(min((row["longitude"] for row in band_rows), default=0), 4),
        "longitude_max_sampled": round(max((row["longitude"] for row in band_rows), default=0), 4),
        "one_degree_bins": [{"longitude_degree": key, **value} for key, value in sorted(longitude_bins.items())],
        "csv_path": str(band_path),
    }

    temp_dir = pathlib.Path("/tmp/azgaar")
    temp_dir.mkdir(parents=True, exist_ok=True)
    (temp_dir / f"{world}.json").write_text(json.dumps({
        "world": world, "width": width, "height": height,
        "coordinates": coordinates, "points": grid_points,
        "boundary": grid.get("boundary", []), "heights": heights,
        "temperatures": temperatures, "precipitation": precipitation,
        "distance_to_water": distance_to_water,
    }), encoding="utf-8")

    record_summary = []
    for index, name in RECORDS.items():
        raw_record = records[index]
        if index in (0, 1, 3, 5, 6, 12, 13, 14, 15, 29, 30, 32, 35, 37, 38, 42, 46, 47, 48, 49, 50, 51, 52, 53):
            try:
                parsed = json.loads(raw_record) if raw_record else None
                shape = summarize_array(parsed) if isinstance(parsed, list) else {"type": type(parsed).__name__ if parsed is not None else "empty"}
                if isinstance(parsed, dict):
                    shape["keys"] = list(parsed.keys())[:25]
                if isinstance(parsed, list) and parsed and isinstance(parsed[0], dict):
                    shape["first_item_keys"] = list(parsed[0].keys())[:25]
            except json.JSONDecodeError:
                shape = {"type": "text"}
        elif index in (2, 4, 23, 28, 33, 41, 45):
            shape = {"type": "deprecated_or_empty", "length": len(raw_record)}
        elif index == 31:
            shape = {"type": "name_base_text", "length": len(raw_record)}
        elif index in (34, 36, 39):
            shape = {"type": "json", "length": len(raw_record)}
        elif index in range(7, 12) or index in range(16, 29) or index in (40, 44, 54, 55):
            shape = {"type": "numeric_array", "count": len(raw_record.split(",")) if raw_record else 0, "length": len(raw_record)}
        else:
            shape = {"type": "record", "length": len(raw_record)}
        record_summary.append({"index": index, "name": name, "length": len(raw_record), **shape})

    geography = options.get("geography", {}).get("coordinates", {})
    return {
        "world": world, "source_file": filename, "container": container,
        "compressed_size_bytes": len(compressed),
        "compressed_sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_size_bytes": len(raw),
        "uncompressed_sha256": hashlib.sha256(raw).hexdigest(),
        "record_count": len(records), "azgaar_version": header[0],
        "saved_date": header[2], "seed": header[3],
        "canvas": {"width": width, "height": height},
        "map_name": options.get("lore", {}).get("name"),
        "geography": geography, "graph": options.get("graph", {}),
        "grid": {
            "spacing": grid.get("spacing"), "cellsX": grid.get("cellsX"), "cellsY": grid.get("cellsY"),
            "points": summarize_array(grid_points), "boundary": summarize_array(grid.get("boundary", [])),
            "grid_features": summarize_array(grid.get("features", [])),
        },
        "terrain": {
            "height_values": summarize_array(heights), "land_cells_height_ge_20": land,
            "water_cells_height_lt_20": water, "precipitation_values": summarize_array(precipitation),
            "feature_id_values": summarize_array(feature_ids), "distance_to_water_values": summarize_array(distance_to_water),
            "temperature_values": summarize_array(temperatures),
        },
        "entities": {
            "biomes": len(biomes), "pack_features": len(pack_features),
            "cultures_including_wildlands": len(cultures), "states_including_neutrals": len(states),
            "states_excluding_neutrals": max(0, len(states)-1),
            "burgs_including_placeholder": len(burgs), "burgs_excluding_placeholder": max(0, len(burgs)-1),
            "religions_including_none": len(religions), "religions_excluding_none": max(0, len(religions)-1),
            "provinces_including_placeholder": len(provinces), "provinces_excluding_placeholder": max(0, len(provinces)-1),
            "rivers": len(rivers), "routes": len(routes), "markers": len(markers), "zones": len(zones),
        },
        "svg": {"path": str(svg_path), "characters": len(source_svg), "xml_valid": True},
        "preview_png": str(png_path), "band_preview_png": str(band_preview_path),
        "center_sample_band": band_summary, "records": record_summary,
    }

def load_sources():
    found = []
    with zipfile.ZipFile(ARCHIVE) as archive:
        for member in archive.infolist():
            if member.is_dir() or not member.filename.lower().endswith(".map.gz"):
                continue
            compressed = archive.read(member.filename)
            found.append((pathlib.Path(member.filename).name, compressed, gzip.decompress(compressed), ARCHIVE.name))
    compressed = STANDALONE.read_bytes()
    found.append((STANDALONE.name, compressed, gzip.decompress(compressed), STANDALONE.name))
    return found

def main():
    reports = [inspect(*source) for source in load_sources()]
    found = {report["source_file"] for report in reports}
    missing = set(WORLD_BY_FILE) - found
    if missing:
        raise SystemExit(f"Missing map sources: {sorted(missing)}")
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "inspeccion-estructura.json").write_text(json.dumps(reports, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{
        "world": r["world"], "version": r["azgaar_version"], "canvas": r["canvas"],
        "geography": r["geography"], "grid": r["grid"], "terrain": r["terrain"],
        "entities": r["entities"], "center_sample_band": r["center_sample_band"],
        "record_count": r["record_count"], "svg": r["svg"]
    } for r in reports], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
