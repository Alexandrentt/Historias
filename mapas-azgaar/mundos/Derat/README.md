# Derat — geografía y geopolítica v2.8

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
- `Derat_Azgaar_estados_candidatos_Alfaguara.geojson`: cuatro polígonos de estado extraídos del mapa regional y recortados al contorno propuesto de Alfaguara; solo para revisión visual, no canónicos; se detectó un cruce de límites entre Combrierolia y Neutiersia, por lo que no sirven para medir áreas ni fronteras.
- `Geopolitica_Derat_v1.md`: análisis de actores, recursos, corredores, ocupación y decisiones pendientes.

## Auditoría de capas v2.8
- Las distancias `nearest_azgaar_*` proceden de trazos del mapa regional; `proximity_to_global_proposed_physical_layer` usa el atlas físico conceptual. No mezclar ambas redes.
- El atlas físico conceptual y el mapa regional Azgaar aún no están reconciliados espacialmente. No desplazar geometrías a ojo.
- La capa de estados Azgaar candidatos tiene anillos individuales cerrados y sin auto-intersecciones, pero presenta cuatro cruces de segmentos entre Combrierolia y Neutiersia. El nombre Neutiersia se verificó en el archivo .map nativo. No usar como partición territorial válida.
- Bowit tiene influencia documentada sobre buena parte de Alfaguara, sin perímetro conocido; Águila Roja está fragmentada; las ciudades-estado no tienen inventario georreferenciado.

## Reglas de lectura
- No hay fronteras políticas nuevas ni áreas de control dibujadas.
- Cuatro puntos proceden de etiquetas burg del mapa Azgaar y están marcados como candidatos no canónicos. Cuatro polígonos estatales también se ofrecen en una capa separada para revisión; ni sus nombres ni sus límites equivalen a soberanías narrativas.
- No se han inventado coordenadas para las demás ciudades-estado, el Consejo de Alfaguara, la veta de Balatium, la Vía de las Sombras, el poblado de 586 DT, minas, guarniciones o bases de facciones.
- Los ejes de conectividad hipotéticos no son carreteras ni rutas navegables confirmadas. La Vía de las Sombras sí está documentada como corredor nocturno, pero su trazado aún no está georreferenciado.
- Cuenca de Ceniza es una zona propuesta de presión extractiva, no un mapa certificado de yacimientos de Madianita o Balatium.
- Vardena y Edravia siguen siendo nombres propuestos.
- Las capas son GeoJSON/SVG editables, no archivos nativos `.map` de Azgaar. El mapa regional original de Alfaguara se conserva sin sobrescribir.
