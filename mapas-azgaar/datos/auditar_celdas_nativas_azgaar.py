#!/usr/bin/env python3
"""Audit native attribute arrays in an Azgaar Fantasy Map Generator 1.158.0 .map save.

The legacy .map format is record-delimited with CRLF. The embedded SVG is one record;
do not open with universal-newline conversion and do not split the whole file by LF.
This script extracts exact native pack-cell attributes, but does not invent cell geometry.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def parse_array(record: str, label: str) -> list[float]:
    if not record:
        return []
    try:
        return [float(value) for value in record.split(",")]
    except ValueError as exc:
        raise ValueError(f"Malformed numeric array: {label}") from exc


def read_records(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        raw = stream.read()
    if "\r\n" not in raw:
        raise ValueError("Expected CRLF record separators. Preserve the original .map bytes; do not normalize line endings.")
    records = raw.split("\r\n")
    if len(records) < 56:
        raise ValueError(f"Unexpected legacy .map record count: {len(records)}")
    version = records[0].split("|", 1)[0]
    if version != "1.158.0":
        raise ValueError(f"This extractor is pinned to Azgaar 1.158.0; received {version!r}")
    return records


def write_state_summary(records: list[str], output: Path) -> dict:
    settings = json.loads(records[1])
    grid = json.loads(records[6])
    features = json.loads(records[12])
    cultures = json.loads(records[13])
    states = json.loads(records[14])
    burgs = json.loads(records[15])

    # Grid attributes, one value per grid point.
    grid_arrays = {
        "height": parse_array(records[7], "grid.height"),
        "precipitation": parse_array(records[8], "grid.precipitation"),
        "feature": parse_array(records[9], "grid.feature"),
        "type": parse_array(records[10], "grid.type"),
        "temperature": parse_array(records[11], "grid.temperature"),
    }
    grid_count = len(grid.get("points", []))
    for name, values in grid_arrays.items():
        if len(values) != grid_count:
            raise ValueError(f"Grid array {name} has {len(values)} values; expected {grid_count}")

    # Packed-cell attributes. The state array is the native cell-to-state assignment.
    pack_arrays = {
        "biome": parse_array(records[16], "pack.biome"),
        "burg": parse_array(records[17], "pack.burg"),
        "confidence": parse_array(records[18], "pack.confidence"),
        "culture": parse_array(records[19], "pack.culture"),
        "river": parse_array(records[20], "pack.river"),
        "population_raw": parse_array(records[21], "pack.population"),
        "religion": parse_array(records[26], "pack.religion"),
        "province": parse_array(records[27], "pack.province"),
        "state": parse_array(records[25], "pack.state"),
    }
    pack_count = len(pack_arrays["state"])
    for name, values in pack_arrays.items():
        if len(values) != pack_count:
            raise ValueError(f"Pack array {name} has {len(values)} values; expected {pack_count}")

    cell_counts = Counter(int(value) for value in pack_arrays["state"])
    population_sums = defaultdict(float)
    for state_id, population in zip(pack_arrays["state"], pack_arrays["population_raw"]):
        population_sums[int(state_id)] += population

    burg_counts = Counter()
    for burg in burgs:
        if isinstance(burg, dict):
            burg_counts[int(burg.get("state", 0))] += 1

    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "state_id", "state_name", "state_full_name", "pack_cell_count",
        "generated_cell_population_sum_raw", "burg_records_in_whole_map",
        "capital_burg_id", "source_map_version", "map_name", "map_seed",
        "classification"
    ]
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for state in states:
            state_id = int(state.get("i", 0))
            writer.writerow({
                "state_id": state_id,
                "state_name": state.get("name", ""),
                "state_full_name": state.get("fullName", ""),
                "pack_cell_count": cell_counts[state_id],
                "generated_cell_population_sum_raw": f"{population_sums[state_id]:.4f}",
                "burg_records_in_whole_map": burg_counts[state_id],
                "capital_burg_id": state.get("capital", 0),
                "source_map_version": records[0].split("|", 1)[0],
                "map_name": settings.get("lore", {}).get("name", ""),
                "map_seed": settings.get("seed", ""),
                "classification": "Azgaar-generated; noncanonical"
            })

    return {
        "map_version": records[0].split("|", 1)[0],
        "map_name": settings.get("lore", {}).get("name", ""),
        "map_seed": settings.get("seed", ""),
        "grid_points": grid_count,
        "packed_cells": pack_count,
        "states": len(states),
        "burg_records": sum(burg_counts.values()),
        "features": len(features),
        "cultures": len(cultures),
        "grid_spacing": grid.get("spacing"),
        "grid_dimensions": [grid.get("cellsX"), grid.get("cellsY")],
        "arrays_validated": True
    }


def write_pack_attributes(records: list[str], output: Path) -> int:
    # This optional export is attribute-only: cell geometry and center coordinates are not stored
    # in these legacy records and are intentionally not fabricated here.
    columns = {
        "cell_index": list(range(len(parse_array(records[25], "pack.state")))),
        "state_id": parse_array(records[25], "pack.state"),
        "biome_id": parse_array(records[16], "pack.biome"),
        "burg_id": parse_array(records[17], "pack.burg"),
        "confidence": parse_array(records[18], "pack.confidence"),
        "culture_id": parse_array(records[19], "pack.culture"),
        "river_id": parse_array(records[20], "pack.river"),
        "population_raw": parse_array(records[21], "pack.population"),
        "religion_id": parse_array(records[26], "pack.religion"),
        "province_id": parse_array(records[27], "pack.province"),
    }
    lengths = {len(values) for values in columns.values()}
    if len(lengths) != 1:
        raise ValueError(f"Packed attribute arrays have inconsistent lengths: {sorted(lengths)}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(columns.keys())
        writer.writerows(zip(*columns.values()))
    return next(iter(lengths))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", required=True, type=Path, help="Original Azgaar 1.158.0 .map file")
    parser.add_argument("--summary", type=Path, default=Path("Derat_Azgaar_estados_nativos.csv"))
    parser.add_argument("--cells-csv", type=Path, help="Optional attribute-only CSV for every packed cell")
    args = parser.parse_args()

    records = read_records(args.map)
    report = write_state_summary(records, args.summary)
    if args.cells_csv:
        report["cell_attribute_rows"] = write_pack_attributes(records, args.cells_csv)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
