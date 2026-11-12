# Inspección técnica de los mapas fuente

**Fecha:** 12 de noviembre de 2026.  
**Método:** lectura reproducible de los archivos comprimidos originales mediante GitHub Actions.  
**Resultado:** las seis fuentes se descomprimieron, parsearon y renderizaron. Se reconstruyó su malla Voronoi y se midió la banda ecuatorial. Los archivos originales no se modificaron.

## Fuentes y correspondencia

| Tierra | Archivo fuente | Contenedor | Nombre interno Azgaar | Versión | Lienzo | Puntos de malla |
|---|---|---|---|---:|---:|---:|
| Amitia | `Amitia.map.gz` | ZIP histórico | Bacsesia | 1.157.0 | 800 × 1165 | 100,084 |
| Atharis | `Atharis.map.gz` | ZIP histórico | Iscia | 1.157.0 | 777 × 760 | 100,160 |
| Derat | `derat(continente de alfaguara).map.gz` | ZIP histórico | Bouneia | 1.158.0 | 1333 × 632 | 100,280 |
| Khorza | `Korza .map.gz` | ZIP histórico | Vileland | 1.158.0 | 800 × 1165 | 100,084 |
| Návar | `Návar.map.gz` | ZIP histórico | Ereia | 1.158.0 | 800 × 1165 | 100,084 |
| Teknara | `Teknara.map.gz` | Archivo en raíz | Thia | 1.158.0 | 800 × 1165 | 100,084 |

Los tamaños comprimidos, tamaños descomprimidos, hashes SHA-256, semillas, fechas y coordenadas están registrados en `manifest.json` y en `datos/inspeccion-estructura.json`. Los rangos de latitud y longitud son los límites configurados en Azgaar; no demuestran por sí solos que los mapas estén georreferenciados con precisión externa.

## Estructura real del archivo

Cada fuente contiene **56 registros delimitados por CRLF**. El SVG guardado en el registro 5 contiene saltos LF internos. Por eso, un análisis con `splitlines()` produce falsamente unas 178 líneas físicas y desplaza todos los índices posteriores. El parser correcto separa únicamente por CRLF.

Los registros relevantes son:

| Índice | Contenido |
|---:|---|
| 0–5 | Cabecera, opciones, campos obsoletos, biomas, notas obsoletas y SVG completo |
| 6 | Metadatos de la malla: separación, dimensiones, puntos, límites y características |
| 7–11 | Altura, precipitación, id de característica, distancia al agua y temperatura de la malla |
| 12–15 | Características empaquetadas, culturas, Estados y asentamientos |
| 16–28 | Atributos por celda: bioma, asentamiento, cultura, población, ríos, puntuación, Estado, religión y provincia, entre otros |
| 29–32 | Religiones, provincias, bases de nombres y ríos |
| 34–39 | Fuentes tipográficas, marcadores, conexiones de rutas, rutas, zonas y hielo |
| 40–55 | Recursos, mercados, comercio, mediciones, etiquetas, estilos, relieve, capas, cambios manuales, viajes, leyendas y atributos finales |

Las posiciones y nombres exactos están definidos en `herramientas/inspeccionar_azgaar.py`. El orden de serialización se contrastó con el código de guardado/carga de Azgaar: [save.ts](https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/src/services/io/save.ts) y [load.ts](https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/src/services/io/load.ts).

## Geometría reconstruida

El registro 6 conserva los puntos de la malla y los puntos auxiliares de borde; los polígonos no se guardan directamente, porque Azgaar los reconstruye al cargar el mapa. El proceso de auditoría repite esa reconstrucción Voronoi con Delaunator, usando los puntos originales y los límites auxiliares. Para cada celda, recupera el polígono de vértices y lo recorta contra la franja ecuatorial.

El umbral de tierra es altura 20 o superior. Esta convención coincide con la documentación del modelo de datos de Azgaar: [data-model.md](https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/docs/architecture/data-model.md). Se hicieron dos intersecciones distintas: una banda de 145 km norte-sur centrada en el ecuador, calculada como 72.5 km de arco meridiano a cada lado sobre WGS 84 (límite aproximado ±0.6556676°), y la línea horizontal exacta de latitud 0°, donde está el Portal.

El área de celdas reconstruida cierra contra el área teórica de la banda con error inferior a 0.009% en cada mapa. Esto valida la reconstrucción de la malla y el recorte sobre el lienzo. No valida que las coordenadas de fantasía correspondan a una geografía planetaria real.

## Hallazgos cuantitativos

La comparación de tierra y agua de la banda, su cobertura longitudinal y el conteo de entidades está en [Resumen-franja-ecuatorial.md](Resumen-franja-ecuatorial.md). Solo Derat cubre 360° de longitud; los demás mapas son coberturas parciales. Khorza tiene una sola entrada reservada en los arreglos de Estados y burgs (sin Estados ni asentamientos), y cero rutas.

## Derivados generados

- `datos/inspeccion-estructura.json`: configuración, hashes, dimensiones, malla, conteos y registros.
- `datos/franja-ecuatorial.json`: áreas de tierra/agua por mapa y por grado de longitud.
- `datos/franja-ecuatorial/<Tierra>.csv`: desglose de la banda de 145 km por longitud.\n- `datos/ecuador-exacto/<Tierra>.csv`: intersección de la línea del Portal con tierra/agua y perfil físico por grado de longitud.
- `visualizaciones/fuentes/<Tierra>.svg.gz`: SVG original extraído y comprimido.
- `visualizaciones/vistas-previas/<Tierra>.png`: vista general.
- `visualizaciones/vistas-previas/<Tierra>-franja-ecuatorial.png`: vista con la banda resaltada.

## Integridad y límites

La inspección fue de solo lectura respecto de las fuentes comprimidas. No se alteraron alturas, biomas, geometría, ríos, asentamientos, Estados, rutas ni SVG de los seis mapas. Los informes y visualizaciones son derivados regenerables.

La banda y la línea calculadas representan el terreno dentro de la cobertura de cada mapa, no la circunferencia completa cuando el mapa cubre menos de 360°. Tampoco determina por sí sola si el tránsito es seguro: faltan análisis de relieve, clima, hidrografía, infraestructura, navegación y contexto histórico.
