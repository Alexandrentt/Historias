# Návar — ficha cartográfica

**Nombre interno de Azgaar:** Ereia.  
**Archivo fuente:** `Návar.map.gz`.  
**Contenedor:** `Historias_mapas_gz_GitHub.zip`.  
**Versión:** 1.158.0.  
**Lienzo:** 800 × 1165 px.  
**Estado:** fuente inspeccionada; geometría original sin modificar.

## Extensión geográfica configurada

Latitud: 13.5° a -13.5°.  
Longitud: -9.2° a 9.3°.  
Cobertura longitudinal: 18.5° (5.14% del ecuador).

La fuente solo cubre 18.5° de los 360°; el resto del ecuador queda fuera del mapa y no se puede clasificar.

## Franja ecuatorial del Portal

La banda analizada mide 145 km norte-sur, centrada en el ecuador, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron las celdas Voronoi y se recortaron sus polígonos contra la banda.

**Tierra:** 75.83%.  
**Agua:** 24.17%.  
**Celdas que intersectan la banda:** 5,226.  
**Error de cierre geométrico:** 0.0044%.

Temperatura configurada en el ecuador: 25 °C. Precipitación configurada: 89.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **74.10%** de la línea cubierta por el mapa es tierra y **25.90%** es agua. La fuente cubre 18.5° de los 360°; el resto queda fuera del mapa. El error de cierre de la intersección es 0.0050%.

Altura media de la tierra sobre la línea: 36.35 (índice relativo, no metros). Temperatura media: 20.64 °C. Rugosidad vecinal: 6.27.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Návar.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 36.42 |
| Superficie terrestre en altura 20–39 | 66.16% |
| Superficie terrestre en altura 40–59 | 28.23% |
| Superficie terrestre en altura 60–79 | 4.33% |
| Superficie terrestre en altura 80–100 | 1.28% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 11.87% |
| Temperatura media sobre tierra | 20.69 °C |
| Índice medio de precipitación | 6.01 |
| Rugosidad vecinal media | 6.04 |

Sectores de altura relativa alta (60+) con al menos 50% de tierra por grado: 3° E.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 3° E (Δ 12.3); 2° E (Δ 11.4); 6° O (Δ 8.4).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 16 |
| Estados (incluye neutral) | 101 |
| Asentamientos/burgs (incluye marcador reservado) | 1582 |
| Religiones (incluye registro reservado) | 39 |
| Provincias (incluye marcador reservado) | 636 |
| Ríos | 860 |
| Rutas | 1519 |
| Marcadores | 430 |
| Zonas | 15 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Návar.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Návar-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Návar.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Návar.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
