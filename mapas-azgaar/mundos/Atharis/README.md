# Atharis — ficha cartográfica

**Nombre interno de Azgaar:** Iscia.  
**Archivo fuente:** `Atharis.map.gz`.  
**Contenedor:** `Historias_mapas_gz_GitHub.zip`.  
**Versión:** 1.157.0.  
**Lienzo:** 777 × 760 px.  
**Estado:** fuente inspeccionada; geometría original sin modificar.

## Extensión geográfica configurada

Latitud: 45.4° a -75.2°.  
Longitud: -61.6° a 61.7°.  
Cobertura longitudinal: 123.3° (34.25% del ecuador).

La fuente solo cubre 123.3° de los 360°; el resto del ecuador queda fuera del mapa y no se puede clasificar.

## Franja ecuatorial del Portal

La banda analizada mide 145 km norte-sur, centrada en el ecuador, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron las celdas Voronoi y se recortaron sus polígonos contra la banda.

**Tierra:** 72.79%.  
**Agua:** 27.21%.  
**Celdas que intersectan la banda:** 1,486.  
**Error de cierre geométrico:** 0.0035%.

Temperatura configurada en el ecuador: 35 °C. Precipitación configurada: 143.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **72.90%** de la línea cubierta por el mapa es tierra y **27.10%** es agua. La fuente cubre 123.3° de los 360°; el resto queda fuera del mapa. El error de cierre de la intersección es 0.0000%.

Altura media de la tierra sobre la línea: 34.12 (índice relativo, no metros). Temperatura media: 31.81 °C. Rugosidad vecinal: 4.26.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Atharis.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 34.26 |
| Superficie terrestre en altura 20–39 | 75.79% |
| Superficie terrestre en altura 40–59 | 24.21% |
| Superficie terrestre en altura 60–79 | 0.00% |
| Superficie terrestre en altura 80–100 | 0.00% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 7.01% |
| Temperatura media sobre tierra | 31.77 °C |
| Índice medio de precipitación | 5.80 |
| Rugosidad vecinal media | 4.13 |

No se detectaron sectores de altura relativa alta (60+) con predominio terrestre en la franja.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 44° E (Δ 15.7); 24° O (Δ 14.2); 43° E (Δ 9.1).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 16 |
| Estados (incluye neutral) | 101 |
| Asentamientos/burgs (incluye marcador reservado) | 1686 |
| Religiones (incluye registro reservado) | 39 |
| Provincias (incluye marcador reservado) | 796 |
| Ríos | 1114 |
| Rutas | 1634 |
| Marcadores | 426 |
| Zonas | 16 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Atharis.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Atharis-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Atharis.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Atharis.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
