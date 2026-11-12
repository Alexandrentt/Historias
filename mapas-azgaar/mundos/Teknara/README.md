# Teknara — ficha cartográfica

**Nombre interno de Azgaar:** Thia.  
**Archivo fuente:** `Teknara.map.gz`.  
**Contenedor:** `Teknara.map.gz (raíz del repositorio)`.  
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

**Tierra:** 19.73%.  
**Agua:** 80.27%.  
**Celdas que intersectan la banda:** 1,059.  
**Error de cierre geométrico:** 0.0084%.

Temperatura configurada en el ecuador: 20 °C. Precipitación configurada: 170.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **19.38%** de la línea cubierta por el mapa es tierra y **80.62%** es agua. La fuente cubre 123.6° de los 360°; el resto queda fuera del mapa. El error de cierre de la intersección es 0.0050%.

Altura media de la tierra sobre la línea: 29.74 (índice relativo, no metros). Temperatura media: 17.64 °C. Rugosidad vecinal: 5.15.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Teknara.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 29.48 |
| Superficie terrestre en altura 20–39 | 88.91% |
| Superficie terrestre en altura 40–59 | 11.09% |
| Superficie terrestre en altura 60–79 | 0.00% |
| Superficie terrestre en altura 80–100 | 0.00% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 19.93% |
| Temperatura media sobre tierra | 17.70 °C |
| Índice medio de precipitación | 13.27 |
| Rugosidad vecinal media | 5.24 |

No se detectaron sectores de altura relativa alta (60+) con predominio terrestre en la franja.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 21° O (Δ 12.5); 22° O (Δ 12.5); 23° O (Δ 10.7).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 16 |
| Estados (incluye neutral) | 101 |
| Asentamientos/burgs (incluye marcador reservado) | 1711 |
| Religiones (incluye registro reservado) | 38 |
| Provincias (incluye marcador reservado) | 704 |
| Ríos | 1069 |
| Rutas | 1660 |
| Marcadores | 491 |
| Zonas | 14 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Teknara.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Teknara-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Teknara.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Teknara.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
