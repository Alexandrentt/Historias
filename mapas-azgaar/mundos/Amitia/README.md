# Amitia — ficha cartográfica

**Nombre interno de Azgaar:** Bacsesia.  
**Archivo fuente:** `Amitia.map.gz`.  
**Contenedor:** `Historias_mapas_gz_GitHub.zip`.  
**Versión:** 1.157.0.  
**Lienzo:** 800 × 1165 px.  
**Estado:** fuente inspeccionada; geometría original sin modificar.

## Extensión geográfica configurada

Latitud: 32.7° a -30.3°.  
Longitud: -21.6° a 21.7°.  
Cobertura longitudinal: 43.3° (12.03% del ecuador).

La fuente solo cubre 43.3° de los 360°; el resto del ecuador queda fuera del mapa y no se puede clasificar.

## Franja ecuatorial del Portal

La banda analizada mide 145 km norte-sur, centrada en el ecuador, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron las celdas Voronoi y se recortaron sus polígonos contra la banda.

**Tierra:** 50.40%.  
**Agua:** 49.60%.  
**Celdas que intersectan la banda:** 2,419.  
**Error de cierre geométrico:** 0.0006%.

Temperatura configurada en el ecuador: 23 °C. Precipitación configurada: 127.

## Contacto exacto con el Portal

La línea del Portal coincide con latitud 0°. En esta fuente, **50.66%** de la línea cubierta por el mapa es tierra y **49.34%** es agua. La fuente cubre 43.3° de los 360°; el resto queda fuera del mapa. El error de cierre de la intersección es 0.0000%.

Altura media de la tierra sobre la línea: 32.25 (índice relativo, no metros). Temperatura media: 19.98 °C. Rugosidad vecinal: 4.76.

- [Datos del ecuador exacto por longitud](../../datos/ecuador-exacto/Amitia.csv)
- [Comparador global del ecuador exacto](../../visualizaciones/Portal-linea-ecuatorial.png)

## Perfil físico preliminar

La altura es un índice relativo de Azgaar, no metros. La precipitación es un índice interno sin unidad física documentada. La proximidad al agua es una aproximación basada en el campo de distancia de la malla; la rugosidad es diferencia de altura relativa entre celdas vecinas, no pendiente física.

| Indicador | Resultado |
|---|---:|
| Altura media relativa de tierra | 32.19 |
| Superficie terrestre en altura 20–39 | 77.94% |
| Superficie terrestre en altura 40–59 | 20.35% |
| Superficie terrestre en altura 60–79 | 1.71% |
| Superficie terrestre en altura 80–100 | 0.00% |
| Tierra próxima al agua (hasta 2 pasos de malla) | 15.09% |
| Temperatura media sobre tierra | 20.08 °C |
| Índice medio de precipitación | 8.20 |
| Rugosidad vecinal media | 4.51 |

Sectores de altura relativa alta (60+) con al menos 50% de tierra por grado: 1° E.

Picos de rugosidad vecinal dentro de los grados predominantemente terrestres: 3° E (Δ 10.7); 3° O (Δ 10.1); 4° E (Δ 9.7).

## Capas registradas

| Capa | Entradas |
|---|---:|
| Culturas (incluye registro reservado) | 14 |
| Estados (incluye neutral) | 101 |
| Asentamientos/burgs (incluye marcador reservado) | 1897 |
| Religiones (incluye registro reservado) | 24 |
| Provincias (incluye marcador reservado) | 674 |
| Ríos | 1194 |
| Rutas | 1724 |
| Marcadores | 438 |
| Zonas | 17 |

Los conteos incluyen los registros reservados de Azgaar cuando se indica; no equivalen automáticamente a entidades activas.

## Visualización

- [Mapa completo](../../visualizaciones/vistas-previas/Amitia.png)
- [Mapa con franja ecuatorial resaltada](../../visualizaciones/vistas-previas/Amitia-franja-ecuatorial.png)
- [Datos por grado de longitud](../../datos/franja-ecuatorial/Amitia.csv)
- [SVG extraído y comprimido](../../visualizaciones/fuentes/Amitia.svg.gz)

## Decisiones pendientes

La banda ecuatorial permite describir tierra, agua, relieve relativo y clima dentro de la cobertura existente. Todavía no demuestra que una ruta sea transitable ni segura. Falta cruzar estos datos con ríos, pendientes, puertos, navegación, infraestructura, abastecimiento y periodo histórico.

No añadir carreteras, puertos, asentamientos, Estados ni fronteras para resolver vacíos sin una decisión de canon. Los tramos longitudinales no cubiertos por la fuente deben permanecer como desconocidos.
