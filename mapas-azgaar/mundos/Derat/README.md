# Derat — geografía y geopolítica v3.3

## Continentes
- `Alfaguara.geojson`: continente polar septentrional.
- `Vardena.geojson`: continente austral que cruza el ecuador; nombre propuesto.
- `Edravia.geojson`: continente nororiental separado por océanos; nombre propuesto.

## Capas físicas
- `Derat_continentes.geojson`: contornos de los tres continentes.
- `Derat_relieve_hidrografia.geojson`: 18 elementos físicos propuestos; las entidades de Alfaguara incluyen atributos de relevancia geopolítica.
- `Derat_mundo.svg`: vista general del planeta.

## Capas geopolíticas
- `Derat_geopolitica_Alfaguara.geojson`: zonas estratégicas, anclajes históricos, cuatro etiquetas de asentamiento Azgaar para revisión con proximidad diferenciada a la red hidrográfica regional y al atlas físico conceptual, entidades sin coordenadas y conectividad hipotética.
- `Derat_Azgaar_estados_candidatos_Alfaguara.geojson`: cuatro polígonos candidatos reconstruidos desde paths del `states.geojson` derivado del SVG, agrupados por ID nativo y recortados al contorno propuesto de Alfaguara. La reconstrucción elimina los cruces detectados; siguen siendo geometrías Azgaar no canónicas, no fronteras políticas.
- `Derat_Azgaar_estados_nativos_Alfaguara.csv`: conteos y atributos agregados leídos de los arrays nativos de celdas empaquetadas del .map 1.158.0; población generada, no canon.
- `Geopolitica_Derat_v1.md`: análisis de actores, recursos, corredores, ocupación y decisiones pendientes.
- `Auditoria_Cruce_Alfaguara_v1.md`: cruce de los cuatro polígonos y cuatro burgs candidatos con relieve, hidrografía, rutas, recursos y cronología. Separa hechos canónicos, documentación narrativa, propuestas y datos Azgaar.

## Auditoría de capas v3.3

- Las distancias `nearest_azgaar_*` proceden de trazos del mapa regional; `proximity_to_global_proposed_physical_layer` usa el atlas físico conceptual. No mezclar ambas redes.
- El atlas físico conceptual y el mapa regional Azgaar aún no están reconciliados espacialmente. Las intersecciones numéricas entre sus geometrías son diagnósticos de alineación, no prueba de accidentes físicos, recursos o control territorial. No desplazar geometrías a ojo.
- La capa de estados candidatos fue reconstruida con coverage_simplify (tolerancia 0.12°) preservando bordes compartidos. La auditoría local con Shapely 2.1.2 confirma geometrías válidas, anillos cerrados y ausencia de solapamientos de área o cruces de límites entre los cuatro estados seleccionados. El nombre Neutiersia se verificó en el .map nativo. La geometría sigue procediendo de paths SVG, no de celdas nativas.
- Los cuatro burgs candidatos (Cochambe, Chaus, Monthimozoy y Bory) caen dentro de sus polígonos Azgaar asociados por ID. Esa correspondencia es una relación interna del generador, no una validación de ciudades-estado narrativas.
- Los candidatos registran 1/6, 6/4, 17/16 y 13/27 paths de ríos/rutas, respectivamente (Bory, Combrierolia, Maclifia y Neutiersia). Conteos y longitudes describen trazos SVG generados, no infraestructura verificada. El export regional de lagos está vacío.
- La auditoría cruzada detecta una intersección numérica entre Maclifia y la zona propuesta Cuenca de Ceniza. No localiza Madianita o Balatium, no demuestra minas y no implica control territorial.
- El .map conserva 100.280 puntos de cuadrícula y arrays de atributos para 71.635 celdas empaquetadas. Los polígonos de esas celdas se regeneran al cargar el mapa; el CSV contiene atributos nativos, no geometría. Los polígonos estatales publicados siguen procediendo de paths SVG.
- Bowit tiene influencia documentada sobre buena parte de Alfaguara, sin perímetro conocido; Águila Roja está fragmentada; las ciudades-estado no tienen inventario georreferenciado.

## Reglas de lectura
- No hay fronteras políticas nuevas ni áreas de control dibujadas.
- Cuatro puntos proceden de etiquetas burg del mapa Azgaar y están marcados como candidatos no canónicos. Cuatro polígonos estatales reconstruidos se ofrecen en una capa separada para revisión; ni sus nombres ni sus límites equivalen a soberanías narrativas.
- No se han inventado coordenadas para las demás ciudades-estado, el Consejo de Alfaguara, la veta de Balatium, la Vía de las Sombras, el poblado de 586 DT, minas, guarniciones o bases de facciones. Los anclajes históricos conservan `geometry: null` mientras no haya ubicación verificable.
- Los ejes de conectividad hipotéticos no son carreteras ni rutas navegables confirmadas. La Vía de las Sombras sí está documentada como corredor nocturno, pero su trazado aún no está georreferenciado.
- Cuenca de Ceniza es una zona propuesta de presión extractiva, no un mapa certificado de yacimientos de Madianita o Balatium.
- Vardena y Edravia siguen siendo nombres propuestos.
- Las capas conceptuales siguen en GeoJSON/SVG. Se generó aparte `Derat_Azgaar_Tres_Continentes_v1.map`, nativo de Azgaar 1.158.0, con tres features terrestres `subtype=continent` y 31.299 celdas empaquetadas. El `.map` se entrega como adjunto; no está subido a GitHub. No sobrescribe el mapa regional original.
- La auditoría y las limitaciones del build están en `Derat_Azgaar_Tres_Continentes_v1.md` y `Derat_Azgaar_Tres_Continentes_audit.json`. El relieve es procedural; no se arrastran ciudades, estados ni fronteras de Bouneia. La importación en la interfaz no pudo probarse en vivo desde el entorno de construcción.
- `../../datos/auditar_celdas_nativas_azgaar.py` permite extraer los atributos nativos del .map 1.158.0; requiere conservar CRLF. No genera geometrías. El .map fuente sigue sin estar subido a GitHub.

## Fuentes del build nativo v1 publicadas en GitHub

La carpeta `Derat_Azgaar_Tres_Continentes/` contiene ahora:
- `build_derat_tricontinent_map.mjs`: generador de mapa nativo Azgaar 1.158.0.
- `graph_tools.mjs`: reconstrucción Voronoi y marcado de features.
- `delaunator.mjs`: triangulación adaptada, con licencia.
- `Derat_continentes.geojson`: contornos de entrada usados por el build.
- `README_AZGAAAR_DERAT.txt`: instrucciones y límites.
- `THIRD_PARTY_NOTICES.md`: avisos y licencias de terceros.

**Archivos grandes no versionados:** el mapa de salida `.map`, el mapa base Bouneia y los ZIP de entrega no se subieron mediante la integración disponible. Se mantienen como adjuntos descargables de la conversación. El generador requiere el .map base de entrada, por lo que el repositorio aún no es autosuficiente para reconstruir el .map sin ese archivo.

La fuente de construcción se añadió para que pueda revisarse y reproducirse cuando se disponga del mapa base. No equivale a confirmar la importación en la interfaz de Azgaar.
