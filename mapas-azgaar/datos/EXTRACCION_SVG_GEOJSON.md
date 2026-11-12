# Extracción vectorial GeoJSON desde los mapas Azgaar

## Estado

Se procesaron localmente los seis mapas originales del paquete `Historias_Mapas_Organizados_6_mundos.zip`. El resultado local está empaquetado como `GeoJSON_Seis_Mundos_Azgaar.zip` (7,452,860 bytes; 49 archivos, 24,976 entidades).

**Importante:** este artefacto aún no está publicado en este repositorio. El conector de GitHub disponible en esta sesión permite crear objetos Git y commits, pero no puede leer los archivos del contenedor local ni transmitir el ZIP binario desde allí. No se declara que los datos estén subidos.

## Método y alcance

Se extrajeron elementos vectoriales del SVG embebido en cada archivo `.map` y se convirtieron a GeoJSON. Capas: `rivers`, `routes`, `states`, `borders`, `lakes`, `ice` y `labels`.

Esta conversión **no equivale a una exportación nativa completa de Azgaar**. No reconstruye la malla de celdas ni todos sus atributos. La capa `lakes.geojson` está vacía porque los lagos se representan mediante elementos SVG `<use>` que no se convirtieron en esta pasada. Los seis archivos `.map` originales siguen siendo la fuente de verdad.

## Conteos extraídos

| Mundo | Ríos | Rutas | Estados | Fronteras | Hielo | Etiquetas | Lagos | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Amitia | 1,194 | 1,724 | 501 | 1,200 | 4 | 100 | 0 | 4,723 |
| Atharis | 717 | 1,154 | 482 | 1,359 | 1,023 | 121 | 0 | 4,856 |
| Derat | 1,766 | 1,293 | 683 | 872 | 0 | 100 | 0 | 4,714 |
| Korza (Khorza) | 1,682 | 0 | 0 | 0 | 220 | 0 | 0 | 1,902 |
| Navar (Návar) | 860 | 1,519 | 457 | 1,069 | 17 | 100 | 0 | 4,022 |
| Teknara | 1,069 | 1,660 | 488 | 1,270 | 172 | 100 | 0 | 4,759 |
| **Total** | **7,288** | **7,350** | **2,611** | **5,770** | **1,436** | **521** | **0** | **24,976** |

## Publicación pendiente

El archivo ZIP y sus 48 archivos internos deben añadirse como archivos binarios/textuales al repositorio. La herramienta de GitHub de esta sesión no tiene una vía para adjuntar directamente un archivo local del contenedor; por eso este documento solo registra la extracción y no simula una subida inexistente.

Para una exportación cartográfica completa, generar desde cada mapa un **JSON Full** de Azgaar y ejecutar `datos/export_azgaar_geojson.py`, que está versionado en este repositorio.
