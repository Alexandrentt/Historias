# Derat — geografía y geopolítica v3.0

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
- `Derat_Azgaar_estados_candidatos_Alfaguara.geojson`: cuatro polígonos candidatos reconstruidos desde los paths del states.geojson derivado del SVG, agrupados por ID nativo y recortados al contorno propuesto de Alfaguara. La reconstrucción elimina los cruces detectados; siguen siendo geometrías Azgaar no canónicas, no fronteras políticas.
- `Geopolitica_Derat_v1.md`: análisis de actores, recursos, corredores, ocupación y decisiones pendientes.

## Auditoría de capas v3.0
- Las distancias `nearest_azgaar_*` proceden de trazos del mapa regional; `proximity_to_global_proposed_physical_layer` usa el atlas físico conceptual. No mezclar ambas redes.
- El atlas físico conceptual y el mapa regional Azgaar aún no están reconciliados espacialmente. No desplazar geometrías a ojo.
- La capa de estados candidatos fue reconstruida con coverage_simplify (tolerancia 0.12°) preservando bordes compartidos. La auditoría local con Shapely 2.1.2 confirma geometrías válidas, anillos cerrados y ausencia de solapamientos de área o cruces de límites entre los cuatro estados seleccionados. El nombre Neutiersia se verificó en el .map nativo. La geometría sigue procediendo de paths SVG, no de celdas nativas.
- La auditoría v3.0 cruza los cuatro polígonos con los paths regionales de ríos y rutas Azgaar; los conteos y longitudes se guardan en las propiedades de cada estado. Son métricas del generador, no infraestructura verificada. El export regional de lagos está vacío.
- El .map disponible no contiene las celdas nativas necesarias para extraer polígonos de estado; la geometría candidata se reconstruyó desde paths SVG y mantiene esa limitación de procedencia.
- Bowit tiene influencia documentada sobre buena parte de Alfaguara, sin perímetro conocido; Águila Roja está fragmentada; las ciudades-estado no tienen inventario georreferenciado.

## Reglas de lectura
- No hay fronteras políticas nuevas ni áreas de control dibujadas.
- Cuatro puntos proceden de etiquetas burg del mapa Azgaar y están marcados como candidatos no canónicos. Cuatro polígonos estatales reconstruidos se ofrecen en una capa separada para revisión; ni sus nombres ni sus límites equivalen a soberanías narrativas.
- No se han inventado coordenadas para las demás ciudades-estado, el Consejo de Alfaguara, la veta de Balatium, la Vía de las Sombras, el poblado de 586 DT, minas, guarniciones o bases de facciones.
- Los ejes de conectividad hipotéticos no son carreteras ni rutas navegables confirmadas. La Vía de las Sombras sí está documentada como corredor nocturno, pero su trazado aún no está georreferenciado.
- Cuenca de Ceniza es una zona propuesta de presión extractiva, no un mapa certificado de yacimientos de Madianita o Balatium.
- Vardena y Edravia siguen siendo nombres propuestos.
- Las capas son GeoJSON/SVG editables, no archivos nativos `.map` de Azgaar. El mapa regional original de Alfaguara se conserva sin sobrescribir.
