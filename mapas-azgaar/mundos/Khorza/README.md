# Khorza — ficha cartográfica

**Nombre interno de Azgaar:** Vileland.  
**Archivo fuente:** `Korza .map.gz`.  
**Contenedor:** `Historias_mapas_gz_GitHub.zip`.  
**Versión:** 1.158.0.  
**Lienzo:** 800 × 1165 px.  
**Estado:** fuente inspeccionada; geometría original sin modificar.

## Extensión geográfica configurada

Latitud: 90° a -90°.  
Longitud: -61.8° a 61.8°.  
Cobertura longitudinal: 123.6° (34.33% del ecuador).

La fuente solo cubre 123.6° de los 360°; el resto del ecuador queda fuera del mapa y no se puede clasificar.

## Franja ecuatorial del Portal

La banda analizada mide 145 km norte-sur, centrada en el ecuador, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron las celdas Voronoi y se recortaron sus polígonos contra la banda.

**Tierra:** 79.13%.  
**Agua:** 20.87%.  
**Celdas que intersectan la banda:** 1,060.  
**Error de cierre geométrico:** 0.0068%.

Temperatura configurada en el ecuador: 44 °C. Precipitación configurada: 500.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **79.50%** de la línea cubierta por el mapa es tierra y **20.50%** es agua. La fuente cubre 123.6° de los 360°; el resto queda fuera del mapa. El error de cierre de la intersección es 0.0423%.

Altura media de la tierra sobre la línea: 42.20 (índice relativo, no metros). Temperatura media: 37.31 °C. Rugosidad vecinal: 8.15.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Khorza.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 42.28 |
| Superficie terrestre en altura 20–39 | 57.85% |
| Superficie terrestre en altura 40–59 | 27.58% |
| Superficie terrestre en altura 60–79 | 10.16% |
| Superficie terrestre en altura 80–100 | 4.42% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 9.01% |
| Temperatura media sobre tierra | 37.30 °C |
| Índice medio de precipitación | 11.05 |
| Rugosidad vecinal media | 7.85 |

Sectores de altura relativa alta (60+) con al menos 50% de tierra por grado: 58° O–54° O; 39° O; 37° O; 45° E; 47° E–48° E; 50° E–61° E.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 50° E (Δ 29.5); 54° O (Δ 28.0); 39° O (Δ 24.2).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 2 |
| Estados (incluye neutral) | 1 |
| Asentamientos/burgs (incluye marcador reservado) | 1 |
| Religiones (incluye registro reservado) | 2 |
| Provincias (incluye marcador reservado) | 1 |
| Ríos | 1682 |
| Rutas | 0 |
| Marcadores | 466 |
| Zonas | 3 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Khorza.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Khorza-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Khorza.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Khorza.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
