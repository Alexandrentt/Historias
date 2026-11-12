# Auditoría de continuidad ecuatorial del Portal

**Estado:** primera auditoría geométrica completada sobre los seis mapas existentes; cobertura global incompleta en cinco de ellos.  
**Regla física:** el Portal recorre el ecuador de cada Tierra. El Trópico de Cáncer y otros paralelos son referencias distintas.

## Línea exacta del Portal (latitud 0°)

El Portal está sobre el ecuador exacto, no en cualquier punto de la franja de 145 km. Por eso se calculó la intersección de la línea de latitud 0° con los polígonos Voronoi. Los porcentajes siguientes miden la longitud de la línea que atraviesa celdas de tierra o agua, no el área de la banda.

| Tierra | Tierra sobre la línea | Agua sobre la línea | Cobertura longitudinal |
|---|---:|---:|---:|
| Amitia | 50.66% | 49.34% | 43.3° |
| Teknara | 19.38% | 80.62% | 123.6° |
| Atharis | 72.90% | 27.10% | 123.3° |
| Khorza | 79.50% | 20.50% | 123.6° |
| Derat | 72.10% | 27.90% | 360° |
| Návar | 74.10% | 25.90% | 18.5° |

Solo Derat representa la circunferencia completa. Los demás porcentajes describen únicamente sus longitudes representadas.

### Intervalos de tierra y agua sobre el ecuador exacto

Cada grado se clasifica según la proporción de longitud de línea ocupada por tierra o agua. Los intervalos simplifican los CSV; los grados mixtos siguen siendo transiciones costeras.

| Tierra | Predominio terrestre | Predominio acuático |
|---|---|---|
| Amitia | 14°–13° O; 11° O–2° E; 4°–10° E | 22°–15° O; 12° O; 3° E; 11°–21° E |
| Teknara | 29°–20° O; 15° E; 34°–47° E | 62°–30° O; 19° O–14° E; 16°–33° E; 48°–61° E |
| Atharis | 58°–56° O; 44°–13° O; 3°–57° E | 62°–59° O; 55°–45° O; 12° O–2° E; 58°–61° E |
| Khorza | 62°–48° O; 41° O–1° O; 5° E; 18° E; 20°–22° E; 24°–61° E | 47°–42° O; 0°–4° E; 6°–17° E; 19° E; 23° E |
| Derat | 160°–78° O; 76°–27° O; 9°–11° E; 13°–17° E; 24°–65° E; 67°–138° E; 141°–142° E; 149° E | 180°–161° O; 77° O; 26° O–8° E; 12° E; 18°–23° E; 66° E; 139°–140° E; 143°–148° E; 150°–180° E |
| Návar | 10°–8° O; 6°–2° O; 0°–1° E; 3°–5° E; 8° E | 7° O; 1° O; 2° E; 6°–7° E; 9° E |

### Relieve relativo sobre el ecuador exacto

Las alturas son índices relativos de Azgaar, no metros.

| Tierra | Sectores con altura alta (60+) | Picos de rugosidad vecinal |
|---|---|---|
| Amitia | 1° E | 4° E y 3° O |
| Atharis | Ninguno | 44° E y 24° O |
| Derat | 81°–91° E; 94°–110° E; 117° E | 85° E, 117° E, 149° E, 24° E y 82° O |
| Khorza | 58°–54° O; 47° E; 51°–61° E | 50°–51° E, 54° O, 39° O y 57° E |
| Návar | 3° E | 1° E y 3° E |
| Teknara | Ninguno | 22°–23° O y 25° O |

Khorza y Derat presentan los sectores más exigentes de relieve relativo en la línea del Portal. En Návar, el foco de 3° E combina altura alta con temperatura media de celda cercana a 6.4 °C, muy inferior a las longitudes vecinas. Estos puntos requieren inspección antes de definir pasos.

**Cierre de línea:** la reconstrucción cierra prácticamente al 100% en cinco mapas. Khorza deja un residuo sin clasificar de 0.0423% de la longitud del lienzo (aprox. 0.34 px); no se ha asignado por suposición a tierra o agua.

## Referencia longitudinal entre Tierras: decisión pendiente

El comparador alinea las longitudes configuradas de cada archivo en un mismo eje de −180° a +180°. Esto permite ver la cobertura y los tramos de cada mapa, pero **no demuestra que 0° de longitud sea el mismo meridiano físico o cultural en todas las Tierras**. Todavía no se ha establecido un meridiano de referencia compartido por los siete planetas ni que una posición longitudinal del Portal corresponda directamente con la misma posición en otra Tierra.

Hasta que esa regla se defina, las longitudes sirven para analizar cada Tierra por separado y comparar la forma de sus coberturas, no para afirmar que dos territorios están enfrentados o conectados entre mundos en el mismo punto angular.

### Prueba condicional de una misma longitud entre mundos

El intervalo longitudinal que los seis mapas cubren simultáneamente es aproximadamente 9.2° O–9.3° E, limitado por la cobertura estrecha de Návar. **Si** se decide que los meridianos están alineados entre Tierras, no existe un grado de ese intervalo donde los seis mapas tengan tierra sobre el ecuador exacto: Teknara es agua a lo largo de todo ese tramo y Derat también es agua entre aproximadamente 9° O y 8° E.

Esto no impide cruzar el Portal; indica que, bajo esa hipótesis de alineación, la logística tendría que contemplar acceso marítimo al menos en Teknara y en buena parte de ese tramo de Derat. Si las longitudes de las Tierras son independientes, esta comparación no define una ruta entre ellas.

## Corredor de 145 km alrededor del Portal

La banda medida tiene 145 km de altura norte-sur, centrada en latitud 0°, con 72.5 km de arco meridiano a cada lado sobre WGS 84. Se reconstruyeron los polígonos Voronoi de Azgaar a partir de los puntos y límites guardados y se recortaron contra la banda. La altura 20 o superior se clasificó como tierra emergida.

| Tierra | Longitud cubierta | % del ecuador representado | Tierra dentro de la banda | Agua dentro de la banda | Celdas que intersectan la banda | Error de cierre de área |
|---|---:|---:|---:|---:|---:|---:|
| Amitia | 43.3° | 12.03% | 50.40% | 49.60% | 2,419 | 0.0006% |
| Teknara | 123.6° | 34.33% | 19.73% | 80.27% | 1,059 | 0.0084% |
| Atharis | 123.3° | 34.25% | 72.79% | 27.21% | 1,486 | 0.0035% |
| Khorza | 123.6° | 34.33% | 79.13% | 20.87% | 1,060 | 0.0068% |
| Derat | 360° | 100% | 72.57% | 27.43% | 1,246 | <0.0001% |
| Návar | 18.5° | 5.14% | 75.83% | 24.17% | 5,226 | 0.0044% |

Los porcentajes de tierra y agua describen únicamente la superficie de la franja dentro de la cobertura del mapa. Solo Derat tiene cobertura suficiente para describir los 360° del ecuador. En los demás, los intervalos exteriores al mapa siguen siendo desconocidos; no deben rellenarse como mar ni como tierra.

## Segmentos de predominio en el corredor de 145 km

El CSV de cada Tierra divide la franja en intervalos de un grado y calcula qué porcentaje del área de cada intervalo es tierra o agua. Los siguientes rangos agrupan los intervalos donde una de las dos superficies ocupa al menos la mitad del área de ese grado. Son una lectura de predominio, no una línea de costa ni una ruta de tránsito.

| Tierra | Intervalos con predominio terrestre | Intervalos con predominio acuático |
|---|---|---|
| Amitia | 14°–13° O; 10° O–10° E | 22°–15° O; 12°–11° O; 11°–21° E |
| Teknara | 28°–20° O; 15° E; 34°–47° E | 62°–29° O; 19° O–14° E; 16°–33° E; 48°–61° E |
| Atharis | 58°–56° O; 44°–13° O; 3°–58° E | 62°–59° O; 55°–45° O; 12° O–2° E; 59°–61° E |
| Khorza | 62°–48° O; 41° O–1° O; 5° E; 18° E; 20°–22° E; 24°–61° E | 47°–42° O; 0°–4° E; 6°–17° E; 19° E; 23° E |
| Derat | 160°–78° O; 76°–27° O; 8°–11° E; 13°–17° E; 24°–64° E; 67°–138° E | 180°–161° O; 26° O–7° E; 18°–23° E; 65°–66° E; 139°–140° E; 142°–143° E; 145°–148° E; 150°–180° E |
| Návar | 10°–2° O; 0°–6° E | 1° O; 7°–9° E |

**Nota de lectura:** el orden de los extremos en intervalos occidentales va de mayor a menor longitud porque se expresan como grados oeste. Para decisiones precisas se debe consultar el CSV, que conserva los grados y porcentajes exactos. Los intervalos de un solo grado pueden corresponder a islas, penínsulas estrechas o celdas costeras; no deben generalizarse como grandes continentes.

## Problemas que ya se pueden afirmar

**Cinco mapas no permiten comprobar la continuidad planetaria completa.** Solo Derat cubre el ecuador entero. No podemos concluir qué hay en los tramos no representados de Amitia, Teknara, Atharis, Khorza o Návar. Es necesario decidir si esos mapas son recortes regionales deliberados o si falta ampliar su cobertura.

**Teknara tiene un ecuador mayoritariamente marítimo dentro del mapa existente.** El 80.27% de la banda representada es agua. Esto hace que la aproximación al Portal probablemente dependa de navegación en una parte importante de ese intervalo, pero todavía no identifica puertos ni rutas seguras.

**Khorza tiene un ecuador mayoritariamente terrestre, pero no tiene rutas ni asentamientos registrados.** El mapa conserva una gran superficie terrestre y 1,682 ríos, pero no contiene Estados, burgs ni rutas. No se ha modificado; primero hay que decidir si la ausencia de infraestructura y entidades es intencional.

**Amitia combina tierra y agua casi por igual.** La cobertura ecuatorial representada está dividida aproximadamente en mitades, por lo que habrá que estudiar pasos costeros y navegación además de rutas terrestres.

## Relieve y clima que pueden condicionar el tránsito

El perfil físico de la banda muestra diferencias que importan para decidir rutas. Las alturas son índices relativos de Azgaar, no metros; los sectores de 60–100 son candidatos a relieve alto y los cambios fuertes entre celdas indican rugosidad, no pendiente física calculada.

| Tierra | Sectores con índice de altura alto (60+) | Sectores con mayor rugosidad vecinal |
|---|---|---|
| Amitia | 1° E | 3° O y 3° E |
| Atharis | Ninguno dentro de la banda | 24° O y 44° E |
| Derat | 81°–91° E; 93°–110° E; foco en 117° E | 82°–86° E, 101° E y sectores alrededor de 82° O |
| Khorza | 58°–54° O; 50°–61° E; focos en 39° O, 37° O y 45°–48° E | 41°–38° O y 50°–58° E |
| Návar | 3° E | 2°–3° E |
| Teknara | Ninguno dentro de la banda | 23°–21° O |

Khorza destaca por el relieve relativo y la rugosidad más altos del conjunto. Derat presenta una franja de elevación alta en su sector oriental. Návar tiene un foco alto cerca de 3° E, con temperatura de celda mucho más baja que en longitudes vecinas. Estos sectores deben revisarse sobre el mapa y las celdas antes de declararlos cordilleras, pasos o barreras.

El perfil cuantitativo, los promedios de temperatura y las limitaciones de cada índice están en [Perfil físico de la franja](../datos/Perfil-fisico-franja-ecuatorial.md).

## Qué falta para convertir esto en rutas

La intersección de la franja con tierra no demuestra que una persona pueda llegar hasta el Portal. Cada segmento requiere revisar el relieve, la pendiente, los ríos, los humedales, el clima, los riesgos, la costa, el oleaje, los puertos, las embarcaciones y la infraestructura disponible en el periodo correspondiente.

No se debe saltar de una cordillera a un océano ni de un océano a un desierto sin documentar la transición. Tampoco se debe asumir que la proximidad al Portal produce prosperidad o seguridad de manera automática.

## Comparación visual de cobertura

[Comparador de la línea exacta del Portal](../visualizaciones/Portal-linea-ecuatorial.png) muestra tierra y agua sobre latitud 0°. [Comparador del corredor de 145 km](../visualizaciones/Portal-cobertura-ecuatorial.png) muestra el terreno cercano en la misma escala longitudinal. Las zonas grises son ausencia de cobertura en la fuente, no océano. La fila de Terra señala que su base física global aún no se ha generado.

## Archivos de trabajo

- [Planificación física preliminar de accesos al Portal](Planificacion-accesos-Portal.md)

- [Resumen comparativo de la banda](../datos/Resumen-franja-ecuatorial.md)
- [Resumen de la línea exacta y la banda](../datos/franja-ecuatorial.json)
- [Datos de la línea exacta por grado](../datos/ecuador-exacto/)
- [Datos del corredor de 145 km por grado](../datos/franja-ecuatorial/)
- [Vistas generales y con la banda resaltada](../visualizaciones/README.md)
- [Inspección técnica del formato Azgaar](../datos/inspeccion-tecnica-fuentes.md)

## Registro obligatorio por tramo

| Campo | Qué debe anotarse |
|---|---|
| Coordenada | Longitud/posición y tolerancia cartográfica |
| Cobertura | Tierra firme, costa, mar, isla, humedal, hielo u otra |
| Relieve | Llanura, meseta, montaña, depresión, fondo oceánico |
| Clima | Temperatura, precipitación, vientos y estacionalidad |
| Acceso | Camino, puerto, embarcadero, instalación, paso o ausencia de acceso |
| Riesgo | Oleaje, tormentas, deslizamientos, fauna, conflicto, aislamiento |
| Autoridad | Quién administra, reclama o controla el acceso en ese periodo |
| Economía | Abastecimiento, peajes, comercio y dependencia local |
| Fecha | Periodo del mapa y fecha de la información |

## Terra

Terra requiere dos capas distintas. La geografía física global del autor representa todo el planeta Tierra real. La cartografía diegética de la época de Yen alcanza únicamente una franja de 145 km norte-sur centrada en el ecuador, debido a las condiciones climáticas y radiactivas. El Portal coincide con la línea central. Fuera de esa banda, la geografía existe, pero no está cartografiada en esa época.

El mapa global del autor servirá para identificar qué terreno existe realmente a lo largo del recorrido. La capa diegética señalará qué partes han podido cartografiarse. La franja no es el mapa completo de Terra.

## Estado de validación

La geometría de la franja está reconstruida y su cierre de área es inferior a 0.009% en los seis mapas. La continuidad planetaria completa **no está aprobada**: cinco mapas no cubren 360°, y aún falta analizar accesibilidad física y logística. No se deben añadir rutas, puertos o fronteras ficticias hasta resolver estas limitaciones.
