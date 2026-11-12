# Mapas de Azgaar — Historias

Este directorio documenta los cinco mapas recibidos para el proyecto.

## Regla de conservación

- Los archivos `.map` originales son la fuente de verdad y deben conservarse byte por byte.
- No reconstruir un mapa únicamente desde PNG, SVG, GeoJSON o exportaciones parciales: esas salidas no sustituyen el proyecto editable.
- Las copias desglosadas (JSON, SVG, CSV o GeoJSON) se guardarán como material auxiliar para inspección, nunca en lugar del original.
- Antes de editar un mapa, crear una copia con fecha o una rama/commit independiente.
- Tras subir los originales, verificar el SHA-256 contra `manifest.json`.

## Estructura prevista

```
mapas-azgaar/
  README.md
  manifest.json
  originales/
    Amitia.map
    Atharis.map
    Korza .map
    Návar.map
    derat(continente de alfaguara).map
  exportaciones/       # derivados auxiliares, si se generan
  versiones/           # snapshots aprobados
```

## Estado de carga

Los metadatos y huellas de los cinco archivos adjuntos están registrados en `manifest.json`. **Los archivos .map originales todavía no están almacenados en este repositorio**; no se marcarán como respaldados hasta verificar su presencia y checksum en GitHub.

## Restauración

Abrir https://azgaar.github.io/Fantasy-Map-Generator/, elegir **Load → Machine** y seleccionar el archivo `.map` original. No editar el archivo manualmente.

Documentación del formato: https://github.com/Azgaar/Fantasy-Map-Generator/wiki/Data-import
