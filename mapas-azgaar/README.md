# Mapas de Azgaar — Historias

Los seis mapas preparados corresponden a estos mundos:

- Amitia — `mundos/Amitia/Amitia.map`
- Atharis — `mundos/Atharis/Atharis.map`
- Derat — mapa regional existente de Alfaguara; la geografía mundial de tres continentes está documentada por separado.
- Khorza (identificador histórico del archivo: Korza) — `mundos/Korza/Korza .map`
- Návar — `mundos/Navar/Návar.map`
- Teknara — `mundos/Teknara/Teknara.map`

## Fuente de verdad y estado

Los archivos originales `.map` / `.map.gz` son la fuente de verdad. El manifiesto conserva el registro de los mapas originales. La publicación de los seis binarios originales en sus carpetas individuales sigue pendiente.

## GeoJSON extraído desde SVG

Se generó un paquete GIS a partir de las geometrías SVG incrustadas en los seis archivos `.map`. Contiene capas de ríos, rutas, estados, fronteras, hielo y etiquetas, además de manifiestos por mundo. El informe `datos/EXTRACCION_SVG_GEOJSON.md` detalla el método y los conteos.

**Limitación importante:** esta extracción vectoriza elementos visibles del SVG. No equivale a una exportación nativa completa de Azgaar: no reconstruye la malla de celdas, alturas, biomas ni todos los objetos internos. La capa de lagos está vacía porque los símbolos SVG de lagos no se convirtieron en esta pasada. No debe usarse como sustituto de los datos fuente.

El paquete ZIP está publicado en la raíz del repositorio como [`GeoJSON_Seis_Mundos_Azgaar_descarga.zip`](../../GeoJSON_Seis_Mundos_Azgaar_descarga.zip) (49 archivos; 24.976 entidades). Los archivos internos están disponibles dentro del ZIP; todavía no se han expandido como archivos individuales en las carpetas de cada mundo.

## Exportación nativa completa

Se incorporó `datos/export_azgaar_geojson.py` para generar capas GIS desde la exportación JSON Full de cada mapa. Produce polígonos de celdas y capas de rutas, ríos, marcadores y zonas. Consulta `datos/README.md` para los pasos.

## Derat

La carpeta `mundos/Derat/` contiene las capas conceptuales de Alfaguara, Vardena y Edravia, además de `Derat_geopolitica_Alfaguara.geojson` y `Geopolitica_Derat_v1.md`. La capa geopolítica distingue zonas de análisis, hidrografía y conectividad hipotética; no inventa fronteras ni áreas de control. Vardena y Edravia son nombres propuestos; el mapa mundial no es aún un archivo Azgaar nativo.

Para abrir mapas, usa Azgaar's Fantasy Map Generator → Load → Machine: https://azgaar.github.io/Fantasy-Map-Generator/.
