# Primera auditoría geométrica de la franja ecuatorial

**Fecha:** 12 de noviembre de 2026.  
**Fuentes:** seis mapas Azgaar originales del repositorio.  
**Estado:** reconstrucción geométrica y cálculo de cobertura completados; interpretación de rutas y accesibilidad pendiente.

## Método

Se descomprimieron los seis archivos originales sin modificarlos. Cada archivo contiene 56 registros separados por CRLF; el registro SVG puede contener saltos LF internos. Se extrajeron la configuración, la geometría de la malla, las alturas y las capas administrativas.

La banda analizada mide 145 km norte-sur, centrada en el ecuador. Los límites se calcularon sobre WGS 84 como 72.5 km de arco meridiano a cada lado: ±0.6556676° aproximadamente. Las coordenadas del lienzo se transformaron usando los límites geográficos equirectangulares declarados por cada mapa.

No se utilizó solo el centro de cada celda. Se reconstruyó el diagrama de Voronoi de Azgaar a partir de los puntos originales y sus puntos auxiliares de borde, siguiendo el método de Delaunator del generador. Después se recortaron los polígonos de las celdas contra la banda ecuatorial y se sumaron sus áreas según la altura. En Azgaar, la altura 20 es el umbral mínimo de tierra emergida.

La suma de áreas reconstruidas y el área teórica de la franja difieren menos de 0.009% en los seis mapas. Esto valida el cierre geométrico de la reconstrucción sobre el lienzo. No convierte los mapas de fantasía en cartografía geodésica real: los resultados son relativos a los límites y coordenadas configurados en cada archivo.

## Resultados

| Tierra | Longitudes cubiertas | Cobertura de 360° | Tierra en la banda | Agua en la banda | Celdas que intersectan la banda | Estados (entradas) | Burgs (entradas) | Rutas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Amitia | 43.3° | 12.03% | 50.40% | 49.60% | 2,419 | 101 | 1,897 | 1,724 |
| Atharis | 123.3° | 34.25% | 72.79% | 27.21% | 1,486 | 101 | 1,686 | 1,634 |
| Derat | 360° | 100% | 72.57% | 27.43% | 1,246 | 101 | 1,091 | 1,293 |
| Khorza | 123.6° | 34.33% | 79.13% | 20.87% | 1,060 | 1 | 1 | 0 |
| Návar | 18.5° | 5.14% | 75.83% | 24.17% | 5,226 | 101 | 1,582 | 1,519 |
| Teknara | 123.6° | 34.33% | 19.73% | 80.27% | 1,059 | 101 | 1,711 | 1,660 |

## Línea ecuatorial exacta: dónde está el Portal

La banda anterior describe el corredor de terreno cercano al Portal. Pero el Portal está sobre la línea de latitud 0°, así que para saber si la pared coincide directamente con tierra o agua hay que medir esa línea por separado. Se intersectó la línea horizontal exacta con los polígonos Voronoi reconstruidos de cada mapa.

| Tierra | Tierra sobre el ecuador exacto | Agua sobre el ecuador exacto | Error de cierre de la línea |
|---|---:|---:|---:|
| Amitia | 50.66% | 49.34% | 0.0000% |
| Atharis | 72.90% | 27.10% | <0.0001% |
| Derat | 72.10% | 27.90% | <0.0001% |
| Khorza | 79.50% | 20.50% | 0.0423% |
| Návar | 74.10% | 25.90% | 0.0050% |
| Teknara | 19.38% | 80.62% | 0.0050% |

Solo Derat cubre toda la circunferencia. Los porcentajes de los demás mapas describen únicamente sus longitudes representadas. En Khorza queda un residuo de línea sin clasificar de aproximadamente 0.34 px; no se ha asignado arbitrariamente a tierra o agua.

La distribución exacta por grado de longitud está en `ecuador-exacto/<Tierra>.csv`. La comparación visual está en [Portal-linea-ecuatorial.png](../visualizaciones/Portal-linea-ecuatorial.png). No confundirla con [la comparación de la banda de 145 km](../visualizaciones/Portal-cobertura-ecuatorial.png): la banda es el corredor de terreno cercano; la línea exacta es el lugar donde se encuentra el Portal.

Las entradas de Estados incluyen el registro neutral reservado por Azgaar; las de burgs incluyen el elemento cero reservado como marcador. Por tanto, Khorza tiene **cero Estados y cero asentamientos registrados**, no uno de cada. El conteo de otras capas aún no descuenta posibles entidades marcadas como eliminadas.

Los porcentajes de tierra y agua son proporciones de superficie de la franja **dentro de la cobertura representada por cada mapa**. No describen el planeta entero cuando el mapa cubre menos de 360° de longitud, ni indican por sí solos transitabilidad, clima seguro o presencia de infraestructura.

## Hallazgos principales

**Cobertura longitudinal insuficiente en cinco mapas.** Solo Derat representa los 360° del ecuador. Amitia cubre 43.3°, Atharis 123.3°, Khorza 123.6°, Návar 18.5° y Teknara 123.6°. Los tramos restantes no pueden clasificarse con estos mapas. No deben completarse inventando océano o tierra.

**Diferencias marcadas en la banda ecuatorial.** Teknara es predominantemente agua (80.27% de la banda representada); Khorza, Návar, Atharis y Derat son predominantemente tierra. Amitia queda casi equilibrada. Son resultados de superficie cartográfica, no una explicación climática ni política.

**Khorza requiere una decisión de canon o una revisión de datos.** El mapa contiene una gran superficie terrestre, 1,682 ríos, 466 marcadores y 220 zonas, pero su registro no contiene Estados, asentamientos ni rutas. No se ha corregido. Puede ser intencional, un mapa naturalista o un mapa social sin terminar; hace falta decidirlo antes de generar entidades.

## Archivos derivados

- `inspeccion-estructura.json`: estructura y metadatos de los seis archivos.
- `franja-ecuatorial.json`: resultados geométricos completos y desglose por grado de longitud.
- `franja-ecuatorial/<Tierra>.csv`: áreas de tierra y agua por cada grado de longitud.
- `muestras-centros-franja-ecuatorial/<Tierra>.csv`: muestreo preliminar de centros de celda; sirve como control secundario, no como resultado principal.
- `../visualizaciones/vistas-previas/<Tierra>.png`: vista general del mapa.
- `../visualizaciones/vistas-previas/<Tierra>-franja-ecuatorial.png`: vista general con la franja resaltada.
- `../visualizaciones/fuentes/<Tierra>.svg.gz`: SVG extraído y comprimido del mapa original.

## Qué no se ha hecho

No se han movido costas, montañas, ríos ni celdas. Tampoco se han creado ciudades, Estados, biomas, recursos o fronteras nuevas. No se ha declarado que una ruta terrestre sea segura por el mero hecho de que exista tierra en la franja. La auditoría de rutas debe combinar la geometría con relieve, clima, hidrografía, navegación, infraestructura y periodo histórico.
