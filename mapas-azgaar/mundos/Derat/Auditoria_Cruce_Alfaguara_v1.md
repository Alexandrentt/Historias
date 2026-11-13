# Auditoría cruzada de Alfaguara — v1.0

**Fecha de revisión:** 13 de noviembre de 2026  
**Repositorio / rama:** `Alexandrentt/Historias` / `main`  
**Commit de entrada:** `da566a48c4719a3af00b120ac3419e4a4032db0b`  
**Alcance:** polígonos estatales candidatos, burgs Azgaar, relieve, hidrografía, rutas, recursos y cronología.  
**Resultado:** auditoría diagnóstica. No se modifican geometrías ni se elevan topónimos o divisiones de Azgaar a canon.

## 1. Jerarquía de evidencia

Se volvió a leer `Los Josth/notas-temas/Canon.md` (blob `8bc8a65171d724afdeee94e4f0f88db92cf4fc15`) antes de revisar las capas. También se contrastaron `Los Josth/tierras/Derat.md`, `Los Josth/Transtierra.md`, `Los Josth/notas-temas/Linea-Temporal.md` y `Los Josth/tramas/Arco-Bastean.md`.

| Clase | Qué queda respaldado | Qué no autoriza |
|---|---|---|
| **Canon** | Derat es la Tierra 5; su historia está ligada a minería y ocupación. En 586 DT ocurre la Operación Tierra 5 en un poblado minero; muere la hija de Bastean y se incauta el arma ceremonial, que desaparece del inventario. | No da nombre ni coordenadas al poblado, minas, ciudades, guarniciones o fronteras. |
| **Hecho documentado fuera de Canon** | La historia de Derat registra la derrota de 127 DT, ocupación indirecta desde 132 DT, primeras células de Águila Roja en 153 DT, surgimiento de ciudades-estado en 166 DT, rumores de alianzas en 178 DT y el Consejo de Alfaguara como foco de resistencia en 191 DT. También documenta hitos de la era SATT: concesiones (505 Zinex), Cronistas (515 Leifx), veta de Balatium (520 Ovryn), Comité de Reclamos (535 Leifx), Ritos de Exilio (545 Mikon), pozos (550 Pazyn) y monitoreo nocturno (570 Syron). | Son hechos narrativos escritos, pero no aportan coordenadas suficientes para situarlos en una geometría. No todos están fijados en `Canon.md`. |
| **Propuesta cartográfica** | Cordillera de la Muralla Norte, Altiplano de las Cuencas, ríos, lagos y Cuenca de Ceniza son elementos del atlas conceptual. | No son levantamiento topográfico ni prueba de yacimientos, caudales, rutas operativas o jurisdicciones. |
| **Dato generado por Azgaar** | Nombres/IDs de estados, etiquetas burg, población, trazos de ríos y rutas y atributos de celdas del mapa regional Bouneia 1.158.0. | No equivalen a nombres canónicos, ciudades-estado, población narrativa, carreteras, ríos verificados ni soberanías. |

**Distinción institucional importante:** el «Régimen» local de la historia de Derat se refiere a fuerzas extranjeras de la CTT que protegían intereses y rutas. No debe equipararse automáticamente con el Régimen de Excepción de Amitia de 579–588 DT fijado en `Canon.md`, ni confundirse CTT, SATT, empresas privadas y fuerzas amitianas como si fueran una sola cadena de mando invariable.

## 2. Polígonos estatales candidatos

Fuente: `Derat_Azgaar_estados_candidatos_Alfaguara.geojson` (blob `8a7416faf85f73e6026497f4311f756fcf2ccf5b`) y `Derat_Azgaar_estados_nativos_Alfaguara.csv` (blob `2127096951ac11a72f931e288ed52ab00a5a18e1`).

Los cuatro polígonos son reconstrucciones de paths SVG derivados del mapa regional, agrupados por ID estatal, recortados al contorno propuesto de Alfaguara y simplificados con tolerancia 0.12°. **No son polígonos extraídos de celdas nativas.** Los conteos de celdas de la tabla proceden por separado de arrays nativos del .map y no reconstruyen estas geometrías.

| Candidato Azgaar | Ratio de solape guardado con Alfaguara | Celdas nativas (CSV) | Paths de ríos / longitud aprox. dentro | Paths de rutas / longitud aprox. dentro | Intersección numérica con atlas físico propuesto |
|---|---:|---:|---:|---:|---|
| **Bory** (state87) | 0.2232 | 157 | 1 / 10.1 km | 6 / 759.5 km | Río del Deshielo; Lago de las Nieves |
| **Combrierolia** (state36) | 1.0000 | 162 | 6 / 3,875 km | 4 / 1,563.9 km | Altiplano de las Cuencas |
| **Maclifia** (state61) | 0.6341 | 744 | 17 / 8,946.1 km | 16 / 7,887.3 km | Río Rojo; Cuenca de Ceniza |
| **Neutiersia** (state6) | 0.8593 | 588 | 13 / 12,494.5 km | 27 / 8,473.6 km | Cordillera de la Muralla Norte; Río de las Cuencas; Lago de las Nieves |

Los conteos y longitudes de ríos/rutas son métricas de paths SVG del mismo mapa Azgaar. No prueban navegabilidad, caudal, mantenimiento, acceso público ni infraestructura existente. La intersección con el atlas físico es una comparación numérica entre capas aún no reconciliadas espacialmente; sirve para detectar alertas de alineación, no para afirmar que un estado real contiene esos accidentes geográficos.

### Lectura por candidato

- **Bory:** su polígono coincide numéricamente con el corredor conceptual del Río del Deshielo y el Lago de las Nieves. El burg Bory cae dentro del polígono correspondiente. El único path fluvial regional contabilizado es corto (10.1 km dentro del candidato) frente a seis paths de ruta; no se deduce escasez o abundancia hídrica real.
- **Combrierolia:** registra seis paths fluviales y cuatro de ruta. La coincidencia con el Altiplano de las Cuencas es solo geométrica y no establece una cuenca hidrográfica real ni una ciudad-estado. Monthimozoy queda dentro de su candidato.
- **Maclifia:** concentra una red densa de paths Azgaar y es el único candidato que intersecta numéricamente el polígono propuesto de Cuenca de Ceniza. Esa coincidencia **no localiza Madianita ni Balatium**, no confirma una mina y no atribuye control a Maclifia. Cochambe queda dentro de su candidato.
- **Neutiersia:** tiene el mayor conteo de paths de rutas y la mayor longitud fluvial registrada entre los cuatro candidatos. La superposición numérica con la cordillera, el Río de las Cuencas y el Lago de las Nieves no demuestra pasos transitables ni abastecimiento. Chaus queda dentro de su candidato.

Los cuatro candidatos conservan el estado no canónico. La selección cubre solo estados con un burg etiquetado dentro de Alfaguara; los espacios no cubiertos son omisiones de selección, no territorios vacíos.

## 3. Burgs: relieve, agua y rutas

Fuente: cuatro features `azgaar_burg_label_candidate` de `Derat_geopolitica_Alfaguara.geojson` (blob `53e4f9ce0bffbb6e2f07c079e33cdca3a411102a`). Se comprobó punto-en-polígono: cada burg cae dentro del polígono candidato con el mismo ID estatal.

| Burg generado | Coordenadas lon, lat | Estado Azgaar asociado | Ruta / río Azgaar más cercanos | Referencia física conceptual más cercana | Agua conceptual más cercana | Distancia a Cuenca de Ceniza |
|---|---|---|---|---|---|---:|
| **Cochambe** (burg61) | -73.566392, 70.909177 | Maclifia | 0.1 / 82.3 km | Cordillera de la Muralla Norte, 80.6 km | Río Rojo, 867 km | 1,444.3 km |
| **Chaus** (burg6) | -129.057164, 70.416456 | Neutiersia | 1.3 / 4.7 km | Lago de las Nieves, 163.6 km | Lago de las Nieves, 163.6 km; Río del Deshielo, 173.6 km | 2,421 km |
| **Monthimozoy** (burg36) | -137.564291, 64.532278 | Combrierolia | 0.4 / 16.6 km | Cordillera de la Muralla Norte, 545.4 km | Lago de las Nieves, 719.6 km; Río de las Cuencas, 793 km | 2,664.7 km |
| **Bory** (burg87) | -130.431808, 76.312025 | Bory | 0.3 / 175 km | Río del Deshielo, 86.5 km | Río del Deshielo, 86.5 km; Lago de las Nieves, 124.6 km | 2,758.9 km |

En la columna Azgaar se muestran distancias geodésicas aproximadas a paths regionales; en las columnas físicas, distancias a accidentes del atlas conceptual. **No son una sola red y no deben compararse como si lo fueran.** Por ejemplo, Cochambe está a 82.3 km del río Azgaar más cercano, pero a 867 km del Río Rojo propuesto; esa diferencia señala falta de reconciliación entre fuentes, no un error que deba corregirse desplazando puntos a ojo.

Las poblaciones asociadas a burgs (38.91, 54.795, 2.685 y 2.63) son valores generados por Azgaar. No se usan para estimar población canónica, jerarquía urbana o importancia política.

## 4. Recursos y anclajes cronológicos

### Recursos

- La documentación narrativa sitúa una **veta de Balatium en la meseta de Alfaguara**, descubierta en 520 Ovryn por un equipo de la SATT. La explotación se relaciona con desertificación y agotamiento de mantos freáticos superficiales; en 550 Pazyn se instala una red limitada de pozos para zonas mineras clave. La veta y los pozos carecen de coordenadas: sus features conservan `geometry: null`.
- Madianita y Balatium aparecen como materiales estratégicos de Derat vinculados a la tecnología Vox. La redacción histórica sobre la sustitución de un material por otro requiere una lectura terminológica cuidadosa; no autoriza a inventar dos depósitos separados ni a ubicar Madianita en Cuenca de Ceniza.
- **Cuenca de Ceniza** es una zona propuesta de presión extractiva. Su propiedad `resources` registra los materiales de interés regional, pero `resource_location_status` aclara que no hay ubicación confirmada dentro del polígono. La coincidencia con Maclifia no cambia ese estado.
- No hay coordenadas para minas, concesiones concretas, pozos, instalaciones de extracción ni la Vía de las Sombras. El corredor está documentado como ruta nocturna de exmineros y comerciantes que bordea asentamientos abandonados y evita peajes SATT, pero no tiene extremos ni trazado descritos.

### Cronología que sí puede sostenerse

| Fecha narrativa | Hecho documentado | Consecuencia cartográfica |
|---|---|---|
| 127 DT | Derrota de Derat; la CTT impone zona desmilitarizada alrededor del Portal y ocupa posiciones clave. | No se conoce la geometría de esas posiciones en Alfaguara; no trasladarlas a los candidatos Azgaar. |
| 132 DT | Comienza la ocupación indirecta y empresas amitianas controlan la extracción con protección militar. | Sin concesiones ni instalaciones georreferenciadas. |
| 153 / 166 / 178 / 191 DT | Primeras células de Águila Roja; surgimiento de ciudades-estado casi independientes; rumores de alianzas sin unidad real; Consejo de Alfaguara como foco de resistencia. | No hay inventario ni coordenadas de ciudades, Consejo o áreas de influencia. |
| 505–570 (fechas con mes narrativo) | Renegociación de concesiones, Cronistas Deratitas, veta de Balatium, Comité de Reclamos, Ritos de Exilio, pozos y monitoreo nocturno. | Los anclajes siguen sin puntos o líneas verificables; no se asignan a burgs. |
| 586 DT | Operación Tierra 5 en un poblado minero sin nombre; muere la hija de Bastean y se incauta el arma ceremonial. | Hecho canónico, pero sin coordenadas; no se asigna a Bory, Cochambe, Chaus ni Monthimozoy. |

El mapa regional Azgaar está fechado el 12-11-2026 y no declara una equivalencia con un año histórico DT. Por tanto, sus estados y burgs no pueden usarse para reconstruir automáticamente el mapa político de 127, 166, 191, 520 o 586 DT.

## 5. Hallazgos, decisiones y límites

1. **Bowit:** `Derat.md` lo resume como controlador de Alfaguara, mientras `Transtierra.md` describe poder sobre buena parte del continente. Se conserva la lectura más prudente ya aplicada en la capa: influencia amplia documentada, perímetro y administración directa no definidos. No se dibuja un área.
2. **Águila Roja:** las fuentes describen células fragmentadas con intereses propios; no se representa como bloque territorial continuo ni mando unificado.
3. **Ciudades-estado:** su existencia y surgimiento están documentados, pero no hay inventario georreferenciado. Los burgs Azgaar no llenan ese vacío.
4. **Operación Tierra 5:** el lugar se mantiene con `geometry: null`. Ningún candidato se vincula al poblado por proximidad o por etiqueta.
5. **Recursos:** no se asigna ningún yacimiento a Maclifia ni a Cuenca de Ceniza. La veta de Balatium sigue sin coordenadas y Madianita no tiene un depósito localizado en las fuentes consultadas.
6. **Régimen y ocupación:** no se cartografían guarniciones ni límites de la CTT, SATT o fuerzas amitianas. Los períodos y las cadenas institucionales deben mantenerse diferenciados.

### Verificación técnica

- Se analizaron 4 polígonos candidatos, 4 burgs, 18 elementos del atlas físico y 14 features de la capa geopolítica.
- Los tres GeoJSON consultados se parsearon correctamente. No se detectaron IDs duplicados, coordenadas no finitas o fuera de rango, ni anillos poligonales abiertos.
- No se editaron geometrías. La validación topológica previa registrada en README/manifiesto (Shapely 2.1.2) indica polígonos candidatos válidos, anillos cerrados y ausencia de solapamientos de área positiva o cruces de límites entre los cuatro candidatos; esta auditoría no altera ni sustituye ese resultado.
- El manifiesto previo enumeraba 20 archivos y todas sus referencias resolvían en la rama `main` antes de añadir este informe.
- El mapa regional `.map` original y los exports fuente completos `states.geojson`, `rivers.geojson` y `routes.geojson` no aparecen versionados en el repositorio consultado. Sin ellos no puede repetirse desde cero la extracción de paths ni reconstruirse la geometría estatal a partir de celdas nativas.

### Pendientes que requieren evidencia

- Incorporar el .map regional original y/o una exportación reproducible de celdas nativas con sus geometrías.
- Reconciliar espacialmente el atlas físico conceptual con las capas regionales Azgaar, sin desplazar entidades manualmente.
- Obtener coordenadas documentadas para el Consejo de Alfaguara, la veta de Balatium, pozos, Vía de las Sombras, ciudades-estado y poblado de 586 DT.
- Precisar el período histórico al que debe representar el mapa político y el alcance temporal/espacial de Bowit, Águila Roja y las fuerzas de ocupación.
- Resolver con las fuentes narrativas la relación terminológica entre Madianita y Balatium antes de modelar depósitos separados.

**Decisión de esta ronda:** se conservan intactas las geometrías y atributos de origen; no se añaden fronteras, control de facciones, nombres canónicos, ciudades, coordenadas ni instalaciones. Los datos sin respaldo continúan ausentes o con geometría nula.
