#!/usr/bin/env python3
"""Reconstruye un .map de Azgaar desde los componentes extraídos."""
from pathlib import Path
import argparse
import hashlib
import json

def rebuild(folder: Path, destination: Path, preserve_original: bool = False) -> str:
    layout = json.loads((folder / "layout.json").read_text(encoding="utf-8"))
    if preserve_original:
        world = (folder / "world.compact.json").read_bytes()
        biomes = (folder / "biomes.compact.json").read_bytes()
    else:
        world_obj = json.loads((folder / "world.json").read_text(encoding="utf-8"))
        biome_obj = json.loads((folder / "biomes.json").read_text(encoding="utf-8"))
        world = json.dumps(world_obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        biomes = json.dumps(biome_obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")

    parts = [
        (folder / layout["header_file"]).read_bytes(),
        world,
        bytes.fromhex(layout["separator_after_world_hex"]),
        biomes,
        bytes.fromhex(layout["separator_after_biomes_hex"]),
        (folder / layout["svg_file"]).read_bytes(),
        (folder / layout["tail_file"]).read_bytes(),
    ]
    data = b"".join(parts)
    json.loads(world.decode("utf-8"))
    json.loads(biomes.decode("utf-8"))
    if not data.startswith((folder / "header.txt").read_bytes()):
        raise ValueError("Cabecera inválida")
    if b"</svg>" not in parts[5]:
        raise ValueError("SVG incompleto")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    exact = len(data) == layout["original_size_bytes"] and digest == layout["original_sha256"]
    print(f"OK: {destination} | {len(data)} bytes | SHA256 {digest} | "
          f"{'idéntico al original' if exact else 'reconstruido con cambios'}")
    return digest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Carpeta del mundo con layout.json")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Archivo .map de salida")
    parser.add_argument("--preserve-original", action="store_true",
                        help="Usa los JSON compactos originales para reconstrucción exacta")
    args = parser.parse_args()
    rebuild(args.folder, args.output, args.preserve_original)
