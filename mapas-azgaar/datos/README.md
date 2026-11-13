# Datos editables y exportación GeoJSON

Esta carpeta reúne herramientas para conservar y derivar datos de los mapas Azgaar.

## Reconstrucción de .map

Los componentes extraídos por mundo son:

- `header.txt`: cabecera original.
- `world.json` y `biomes.json`: secciones JSON editables.
- `map.svg` y `tail.dat`: contenido adicional conservado.
- `layout.json`: separadores, tamaños y hashes.
- `world.compact.json` y `biomes.compact.json`: JSON compactos originales.

Usa `compile_map.py` para reconstruir el archivo. Con `--preserve-original` se conserva el JSON original compacto.

## Exportación GIS / GeoJSON

Azgaar produce GeoJSON de celdas, rutas, ríos, marcadores y zonas desde su menú Export. La exportación de celdas contiene polígonos y propiedades como altura, bioma, población y adscripciones territoriales. Consulta la [guía GIS oficial](https://github.com/Azgaar/Fantasy-Map-Generator/wiki/GIS-data-export).

Se agregó `export_azgaar_geojson.py` para convertir el JSON **Full** de Azgaar a capas GeoJSON reproducibles:

1. Abre el `.map` original en Azgaar.
2. Selecciona Export → Export To JSON → Full.
3. Guarda el JSON descargado.
4. Ejecuta:

```bash
python export_azgaar_geojson.py mapa_full.json --out salida/Mundo
```

El script genera `cells.geojson`, `routes.geojson`, `rivers.geojson`, `markers.geojson`, `zones.geojson` y `export_manifest.json`. Conserva los valores internos de altura y población como atributos sin inventar conversiones de unidades. Las zonas se representan mediante las geometrías de sus celdas constituyentes.

## Mundos preparados

Amitia, Atharis, Derat (Alfaguara), Khorza/Korza, Návar y Teknara figuran en `mapas-azgaar/manifest.json`. Los archivos binarios originales siguen siendo la fuente de verdad; no sobrescribas los `.map` al generar capas GIS.

## Compilar

```bash
python compile_map.py carpeta_extraida -o Mundo.map --preserve-original
```


## Auditoría de atributos nativos del .map legado

Para archivos guardados por Azgaar 1.158.0, `auditar_celdas_nativas_azgaar.py` lee los registros internos respetando los separadores CRLF y valida los tamaños de los arrays. No normalices los finales de línea del .map antes de ejecutarlo.

Ejemplo:

```bash
python auditar_celdas_nativas_azgaar.py --map "derat(continente de alfaguara).map" --summary estados.csv --cells-csv celdas_atributos.csv
```

- El resumen incluye todos los estados y sus conteos de celdas empaquetadas, suma bruta de población generada y número de burgs.
- El CSV opcional contiene una fila por celda empaquetada y sus atributos nativos, sin coordenadas ni geometría.
- La geometría de las celdas se regenera al cargar el mapa a partir de la cuadrícula, el límite y la triangulación Delaunator. Este script no pretende sustituir esa reconstrucción ni convertir los paths SVG en celdas.
- La exportación oficial `Export → GeoJSON → cells` sigue siendo la vía preferida para obtener polígonos de celda listos para GIS.


## Mapa nativo editable de Derat — build provisional v1

Se preparó un archivo nativo Azgaar 1.158.0 con tres features terrestres marcadas `subtype=continent`. La cuadrícula de 100.280 puntos y los 678 puntos de borde se preservan; el pipeline regenerado produce 31.299 celdas empaquetadas. El resultado y las fuentes reproducibles se entregan en un paquete adjunto, mientras el README y la auditoría se versionan en GitHub.

El constructor requiere como entrada el .map base 1.158.0 de Derat y `Derat_continentes.geojson`. Acepta `--map`, `--continents`, `--out` y `--audit`. No copia los burgs, estados, ríos o rutas de Bouneia. El relieve es procedural, y Vardena/Edravia siguen siendo nombres propuestos. La validación local cubre el formato nativo, arrays y enlaces de vértice; la apertura en la interfaz no pudo probarse en vivo desde este entorno.
