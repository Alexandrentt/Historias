#!/usr/bin/env python3
"""
Publica localmente en el repositorio los 7 mapas Azgaar:
- 310 archivos de capas JSON/SVG y documentación
- 7 .map originales
- 7 .map recompilados

Coloca los tres ZIP descargados de ChatGPT en la raíz del clon del repositorio
y ejecuta: python publicar_paquete_completo.py
Requiere Python 3 y Git configurado con acceso de escritura al repositorio.
"""
from pathlib import Path
from zipfile import ZipFile
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
ARCHIVES = {
    "layers": ROOT / "Mapas_Azgaar_Capas_JSON_7_Mapas.zip",
    "source": ROOT / "Mapas_Azgaar_Originales_7_MAP.zip",
    "rebuilt": ROOT / "Mapas_Azgaar_Recompilados_7_MAP.zip",
}
DESTINATIONS = {
    "source_maps/": ROOT / "mapas-azgaar" / "mapas-originales",
    "rebuilt_maps/": ROOT / "mapas-azgaar" / "mapas-recompilados",
}
MAX_FILE_BYTES = 100 * 1024 * 1024

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def safe_extract(archive: Path, mode: str):
    with ZipFile(archive) as z:
        for info in z.infolist():
            name = info.filename.replace("\\\\", "/")
            if name.startswith("/") or ".." in Path(name).parts:
                raise RuntimeError(f"Ruta insegura dentro de ZIP: {name}")
            if info.file_size > MAX_FILE_BYTES:
                raise RuntimeError(f"Archivo supera 100 MB: {name}")
            if mode == "layers":
                target = ROOT / name
            else:
                prefix = "source_maps/" if mode == "source" else "rebuilt_maps/"
                if not name.startswith(prefix):
                    continue
                target = DESTINATIONS[prefix] / Path(name).name
            target.parent.mkdir(parents=True, exist_ok=True)
            if not info.is_dir():
                target.write_bytes(z.read(info))
    print(f"OK: {archive.name}")

def main():
    missing = [str(p.name) for p in ARCHIVES.values() if not p.is_file()]
    if missing:
        print("Faltan estos ZIP en la raíz del repositorio:", ", ".join(missing))
        sys.exit(2)
    if not (ROOT / ".git").exists():
        print("Ejecuta este script desde un clon Git del repositorio Historias.")
        sys.exit(2)
    for mode, archive in ARCHIVES.items():
        safe_extract(archive, mode)

    run("git", "add", "mapas-azgaar/capas-json",
        "mapas-azgaar/mapas-originales", "mapas-azgaar/mapas-recompilados")
    status = subprocess.run(["git", "status", "--short"], cwd=ROOT,
                            capture_output=True, text=True, check=True)
    if not status.stdout.strip():
        print("No hay cambios nuevos que publicar.")
        return
    run("git", "commit", "-m", "Add complete editable Azgaar map sources and layers")
    run("git", "push", "origin", "HEAD")
    print("Publicado. Comprueba el árbol del repositorio en GitHub.")

if __name__ == "__main__":
    main()
