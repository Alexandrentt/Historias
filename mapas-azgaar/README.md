# Mapas de Azgaar — Historias

El repositorio contiene seis fuentes de mapas Azgaar accesibles y verificadas. Cinco están comprimidas dentro de `Historias_mapas_gz_GitHub.zip` y la sexta, `Teknara.map.gz`, está en la raíz. El proceso de auditoría las descomprime y trabaja directamente con ellas; no es necesario volver a subirlas ni duplicar los originales.

La correspondencia, versiones, dimensiones, semillas, rangos geográficos y hashes están en `manifest.json`. La inspección técnica del formato está en `datos/inspeccion-tecnica-fuentes.md`.

## Mundos

- Amitia — fuente `Amitia.map.gz`; nombre interno Azgaar: Bacsesia.
- Atharis — fuente `Atharis.map.gz`; nombre interno: Iscia.
- Derat — fuente `derat(continente de alfaguara).map.gz`; nombre interno: Bouneia.
- Khorza — fuente `Korza .map.gz`; nombre interno: Vileland.
- Návar — fuente `Návar.map.gz`; nombre interno: Ereia.
- Teknara — fuente `Teknara.map.gz`; nombre interno: Thia.
- Terra — mapa físico global pendiente, basado en la geografía completa del planeta Tierra real. La franja ecuatorial de 145 km representa únicamente el alcance cartográfico alcanzado en tiempos de Yen. Ver `mundos/Terra/README.md`.

## Primera auditoría cartográfica

Los seis mapas fueron descomprimidos, parseados y renderizados. Se extrajo el SVG original de cada archivo. También se reconstruyó la malla Voronoi a partir de sus puntos y límites originales. Se calcularon por separado la intersección de las celdas con la banda de 145 km alrededor del ecuador y la intersección de la línea exacta de latitud 0°, donde está el Portal.

**Hallazgo crítico:** solo Derat cubre los 360° de longitud. Amitia cubre 43.3°, Atharis 123.3°, Khorza 123.6°, Návar 18.5° y Teknara 123.6°. Por tanto, cinco mapas no permiten comprobar el recorrido completo del Portal. Los tramos no representados permanecen desconocidos; no se deben completar por suposición.

Khorza tiene una base física extensa, pero no registra Estados, asentamientos ni rutas. No se ha alterado; primero hay que decidir si esa ausencia es intencional.

El resumen cuantitativo está en `datos/Resumen-franja-ecuatorial.md`; el perfil de relieve y clima en `datos/Perfil-fisico-franja-ecuatorial.md`; los CSV del corredor de 145 km en `datos/franja-ecuatorial/` y los de la línea exacta del Portal en `datos/ecuador-exacto/`. Las visualizaciones comparan ambas capas en `visualizaciones/README.md`.

## Terra: mapa global y alcance cartográfico en tiempos de Yen

El mapa físico completo de Terra debe representar el planeta Tierra real entero: todas sus masas terrestres, islas, costas y océanos. La franja de 145 km norte-sur centrada en el ecuador (0°), extendida por los 360° de longitud, no es el mapa completo: representa todo el alcance de la cartografía sistemática conseguida en tiempos de Yen debido a las condiciones climáticas y radiactivas. Sus límites aproximados son 0.6556676° S–0.6556676° N sobre WGS 84. El Portal coincide con la línea central. Fuera de la banda, los mapas diegéticos deben señalar geografía no cartografiada, no océano ni vacío.

## Acceso, herramientas y conservación

El flujo reproducible está en `.github/workflows/auditar-mapas.yml`. Los scripts `herramientas/inspeccionar_azgaar.py` y `herramientas/muestrear_voronoi.mjs` extraen datos, reconstruyen celdas, calculan la banda y generan visualizaciones. No modifican los archivos originales.

Los derivados se regeneran desde las fuentes comprimidas. No se han alterado alturas, costas, biomas, ríos, asentamientos, Estados, rutas ni fronteras. Las copias individuales de los binarios no se han duplicado en `mundos/<Tierra>/` porque no son necesarias para procesar las fuentes actuales.

El marco metodológico está en `Metodo-de-trabajo-geografico.md`; la auditoría general en `Auditoria-geografica-inicial.md`, la plantilla de fichas en `plantilla-ficha-geografica.md` y la continuidad ecuatorial en `rutas/Continuidad-ecuatorial.md` y la planificación física preliminar de accesos en `rutas/Planificacion-accesos-Portal.md`.

Para abrir los mapas originales, usa Azgaar's Fantasy Map Generator → Load → Machine: https://azgaar.github.io/Fantasy-Map-Generator/.
