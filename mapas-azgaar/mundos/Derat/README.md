# Derat — ficha cartográfica

**Nombre interno de Azgaar:** Bouneia.  
**Archivo fuente:** `derat(continente de alfaguara).map.gz`.  
**Contenedor:** `Historias_mapas_gz_GitHub.zip`.  
**Versión:** 1.158.0.  
**Lienzo:** 1333 × 632 px.  
**Estado:** fuente inspeccionada; geometría original sin modificar.

## Extensión geográfica configurada

Latitud: 90° a -90°.  
Longitud: -180° a 180°.  
Cobertura longitudinal: 360.0° (100.00% del ecuador).

La fuente cubre los 360° de longitud.

## Franja ecuatorial del Portal

La banda analizada mide 145 km norte-sur, centrada en el ecuador, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron las celdas Voronoi y se recortaron sus polígonos contra la banda.

**Tierra:** 72.57%.  
**Agua:** 27.43%.  
**Celdas que intersectan la banda:** 1,246.  
**Error de cierre geométrico:** 0.0000%.

Temperatura configurada en el ecuador: 44 °C. Precipitación configurada: 500.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **72.10%** de la línea cubierta por el mapa es tierra y **27.90%** es agua. La fuente cubre 360.0° de los 360° y representa la circunferencia completa. El error de cierre de la intersección es 0.0000%.

Altura media de la tierra sobre la línea: 38.68 (índice relativo, no metros). Temperatura media: 39.13 °C. Rugosidad vecinal: 5.56.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Derat.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 38.67 |
| Superficie terrestre en altura 20–39 | 55.80% |
| Superficie terrestre en altura 40–59 | 34.68% |
| Superficie terrestre en altura 60–79 | 9.37% |
| Superficie terrestre en altura 80–100 | 0.15% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 7.87% |
| Temperatura media sobre tierra | 39.14 °C |
| Índice medio de precipitación | 10.51 |
| Rugosidad vecinal media | 5.55 |

Sectores de altura relativa alta (60+) con al menos 50% de tierra por grado: 81° E–91° E; 93° E–110° E; 117° E.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 149° E (Δ 14.5); 82° O (Δ 14.2); 85° E (Δ 13.9).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 16 |
| Estados (incluye neutral) | 101 |
| Asentamientos/burgs (incluye marcador reservado) | 1091 |
| Religiones (incluye registro reservado) | 83 |
| Provincias (incluye marcador reservado) | 517 |
| Ríos | 1766 |
| Rutas | 1293 |
| Marcadores | 450 |
| Zonas | 12 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Derat.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Derat-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Derat.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Derat.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
