# Mapas de Azgaar — Historias

Los seis mapas preparados corresponden a estos mundos:

- Amitia — `mundos/Amitia/Amitia.map`
- Atharis — `mundos/Atharis/Atharis.map`
- Derat — mapa regional existente de Alfaguara; la geografía mundial de tres continentes está documentada por separado.
- Khorza (identificador histórico del archivo: Korza) — `mundos/Korza/Korza .map`
- Návar — `mundos/Navar/Návar.map`
- Teknara — `mundos/Teknara/Teknara.map`

## Fuente de verdad y estado

Los archivos originales `.map` / `.map.gz` son la fuente de verdad. El ZIP histórico y los comprimidos no deben reemplazarse sin verificar los hashes. El manifiesto enumera seis mapas preparados, pero los seis binarios individuales aún no están publicados en sus carpetas de mundo.

## GeoJSON

Se incorporó `datos/export_azgaar_geojson.py` para generar capas GIS desde la exportación JSON Full de cada mapa. Produce polígonos de celdas y capas de rutas, ríos, marcadores y zonas. Consulta `datos/README.md` para los pasos.

**Estado de las exportaciones:** la herramienta ya está publicada; los GeoJSON completos de los seis mapas todavía no se han generado ni subido. No se crearán polígonos aproximados a partir de los metadatos del manifiesto ni se presentarán como exportaciones reales.

## Derat

La carpeta `mundos/Derat/` contiene las capas conceptuales de Alfaguara, Vardena y Edravia. Vardena y Edravia son nombres propuestos; el mapa mundial no es aún un archivo Azgaar nativo.

Para abrir mapas, usa Azgaar's Fantasy Map Generator → Load → Machine: https://azgaar.github.io/Fantasy-Map-Generator/.
