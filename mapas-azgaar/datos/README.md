# Datos y componentes de los mapas

Los seis mapas originales son accesibles desde el repositorio. Cinco están comprimidos como `.map.gz` dentro de `Historias_mapas_gz_GitHub.zip`; el sexto, `Teknara.map.gz`, está en la raíz. GitHub Actions los descomprime y procesa directamente. No hace falta volver a subirlos ni duplicarlos en carpetas organizadas.

## Formato comprobado

Cada archivo contiene 56 registros separados por CRLF. El registro SVG puede contener saltos de línea LF internos, por lo que no se debe dividir el archivo con un `splitlines()` genérico: eso rompe la correspondencia de los registros. La primera posición es la cabecera; la segunda, la configuración JSON; la sexta, el SVG; la séptima, los metadatos de la malla. Después aparecen los arreglos de alturas, precipitación, características, temperatura, entidades y atributos de las celdas.

El registro de malla guarda `spacing`, `cellsX`, `cellsY`, `boundary`, `points` y `features`. Los puntos y los puntos auxiliares de borde permiten reconstruir el diagrama de Voronoi. Las alturas de la malla usan 20 como umbral mínimo de tierra emergida. Las capas de entidades incluyen culturas, Estados, asentamientos, religiones, provincias, ríos, marcadores, rutas y zonas.

La correspondencia completa de los 56 registros está en `../herramientas/inspeccionar_azgaar.py`. El lector conserva la fuente original y escribe derivados regenerables. La reconstrucción de celdas y el recorte de la franja están en `../herramientas/muestrear_voronoi.mjs`.

## Auditoría geométrica completada

La banda de 145 km norte-sur centrada en el ecuador se reconstruyó sobre los polígonos de Voronoi, no solo mediante muestras de centros. Además, se calculó por separado la intersección de la línea exacta de latitud 0° con esos polígonos, porque el Portal está sobre esa línea. Se usaron los puntos y límites originales, Delaunator y recorte poligonal contra los límites de la banda. El error de cierre entre el área reconstruida y el área teórica del lienzo es inferior a 0.009% en los seis mapas.

Consulta [Resumen de la franja ecuatorial](Resumen-franja-ecuatorial.md) para la comparación, [Perfil físico de la franja](Perfil-fisico-franja-ecuatorial.md) para relieve y clima, y [inspeccion-tecnica-fuentes.md](inspeccion-tecnica-fuentes.md) para el formato y las fuentes. Los datos máquina están en `inspeccion-estructura.json` y `franja-ecuatorial.json`.

## Archivos derivados

- `inspeccion-estructura.json`: versiones, metadatos, tamaños, hashes, estructura y conteos de entidades.
- `franja-ecuatorial.json`: área de tierra/agua por mapa y por grado de longitud.
- `franja-ecuatorial/<Tierra>.csv`: desglose exacto por grado de longitud, obtenido mediante intersección de polígonos.
- `muestras-centros-franja-ecuatorial/<Tierra>.csv`: muestreo secundario de centros de celda, útil como control, no como resultado principal.
- `../visualizaciones/vistas-previas/`: mapas completos y mapas con la franja resaltada.
- `../visualizaciones/fuentes/`: SVG extraído y comprimido.

## Hallazgos que condicionan el trabajo

Solo Derat cubre los 360° de longitud. Los otros cinco mapas representan intervalos longitudinales parciales; por tanto, no bastan para validar el recorrido completo del Portal. Khorza no contiene Estados, asentamientos ni rutas registrados, aunque sí tiene una malla terrestre extensa, ríos, marcadores y zonas. No se ha modificado para corregirlo: primero hay que decidir si ese estado es intencional.

## Estado

- [x] Localizar y descomprimir los cinco mapas del ZIP y Teknara.
- [x] Verificar las seis fuentes y sus hashes.
- [x] Interpretar correctamente los 56 registros de cada archivo.
- [x] Extraer y validar los SVG originales.
- [x] Reconstruir las celdas Voronoi y calcular la intersección ecuatorial.
- [x] Generar CSV por grado de longitud y vistas generales/resaltadas.
- [x] Documentar las limitaciones de cobertura y las anomalías de capas.
- [ ] Resolver cómo completar o representar los tramos longitudinales no cubiertos por cinco mapas.
- [ ] Revisar el estado cartográfico de Khorza.
- [ ] Cruzar la geometría con relieve, clima, hidrografía y accesibilidad.
- [ ] Diseñar rutas físicas y logísticas del Portal por periodo histórico.

Los seis archivos fuente originales siguen sin alteraciones. No se han creado ni modificado costas, celdas, biomas, asentamientos, Estados, fronteras o rutas.
