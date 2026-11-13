# Derat — mapa nativo editable de Azgaar v1

## Entrega

Se generó **`Derat_Azgaar_Tres_Continentes_v1.map`**, un archivo de guardado nativo de Azgaar 1.158.0. No es un GeoJSON renombrado: contiene la cuadrícula, atributos de altura y temperatura, datos de la malla empaquetada y las referencias de vértices que Azgaar reconstruye al cargar.

El archivo binario se entrega como adjunto descargable en la conversación. **No está almacenado en GitHub** en este momento. La guía, auditoría y fuentes de construcción acompañan el paquete descargable.

## Resultado estructural

- 100.280 puntos de cuadrícula y 678 puntos de borde, conservados del mapa base.
- 31.299 celdas empaquetadas, con los 15 arrays serializados del mismo tamaño.
- Tres features terrestres con `subtype="continent"`: Alfaguara (8.619 celdas), Edravia (4.921) y Vardena (14.939).
- Cero lagos internos.
- Se limpiaron los asentamientos, estados, culturas, religiones, ríos, rutas, mercados y datos militares heredados del mapa base. No se trasladaron elementos de Bouneia a Derat sin georreferenciación.
- El relieve y los biomas son generados de forma provisional; los contornos parten de `Derat_continentes.geojson`.

Azgaar separa la masa de agua en tres componentes por la conectividad de la proyección rectangular: uno contiene 2 celdas, otro 3 y el principal 2.815. Esos fragmentos de borde no representan océanos planetarios adicionales.

## Canon y procedencia

Alfaguara conserva su nombre. **Vardena y Edravia siguen siendo nombres propuestos.** Los tres contornos se usan exactamente como están en el GeoJSON actual; el build no los convierte en canon ni corrige a ojo el cierre polar. El mapa no incorpora fronteras políticas ni ciudades inventadas.

## Importación y verificación

El archivo está escrito con cabecera y registros CRLF de Azgaar 1.158.0. Se validaron los 56 registros, las longitudes de arrays, los índices de las features y las referencias de vértices; también se revisó el guard de integridad `MapRepair` del código 1.158.0.

No se pudo abrir la aplicación en vivo desde el entorno de construcción porque el acceso del navegador a `azgaar.github.io` está bloqueado. Por tanto, el formato está validado contra el código de carga, pero la apertura real en la interfaz todavía no ha sido presenciada. Para la prueba de uso, abre el archivo en Azgaar 1.158.0, modifica una elevación y guarda una copia desde Azgaar.

## Archivos de apoyo

- `Derat_Azgaar_Tres_Continentes_audit.json`: cifras y límites de la construcción.
- `README_AZGAAAR_DERAT.txt`: instrucciones de importación y reconstrucción.
- `build_derat_tricontinent_map.mjs`, `graph_tools.mjs` y `delaunator.mjs`: fuentes incluidas en el paquete reproducible.
- `THIRD_PARTY_NOTICES.md`: atribuciones y licencias de los algoritmos adaptados.
