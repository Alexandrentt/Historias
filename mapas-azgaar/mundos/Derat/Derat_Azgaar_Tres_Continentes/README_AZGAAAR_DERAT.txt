DERAT — MAPA EDITABLE AZGAAR 1.158.0
====================================

ARCHIVO PRINCIPAL
  Derat_Azgaar_Tres_Continentes_v1.map

El .map es un mapa nativo de Azgaar, no un GeoJSON renombrado. Se construyó
con el formato de guardado 1.158.0, conservando la cuadrícula original de
100.280 puntos y 678 puntos de borde, y regenerando el grafo Voronoi y la
malla empaquetada. El archivo contiene 31.299 celdas empaquetadas y tres
features terrestres que llevan subtype="continent": Alfaguara, Vardena y
Edravia.

Los polígonos de origen son los que están en Derat_continentes.geojson. Vardena
y Edravia siguen siendo nombres propuestos; los tres contornos y el relieve
generado son provisionales, no canon. El relieve es procedural y editable.
Se eliminaron burgs, estados políticos, culturas, religiones, ríos, rutas,
mercados e instalaciones heredados del mapa base, porque no están
georreferenciados de forma fiable para Derat. La capa política queda neutral.

Hay tres regiones de agua separadas por la conectividad del borde rectangular
del mapa (dos son fragmentos de 2 y 3 celdas); eso no establece tres océanos
físicos distintos. No se dibujaron océanos extra en la geografía canónica.

IMPORTACIÓN
  Abrir Azgaar Fantasy Map Generator 1.158.0.
  Usar Load / cargar mapa desde archivo y seleccionar el .map.
  Al abrir, comprobar los tres continentes en la capa de mapa/heightmap y
  guardar una copia desde Azgaar para confirmar el ciclo de edición/exportación.

VALIDACIÓN REALIZADA
  - 56 registros CRLF, cabecera 1.158.0.
  - 100.280 puntos y 678 puntos de borde.
  - 31.299 pack cells.
  - Los 15 arrays por celda serializados tienen exactamente 31.299 valores.
  - 3 features terrestres, todas subtype="continent".
  - Los índices de vértice de los tres contornos están dentro del grafo Voronoi.
  - Un solo estado neutro, cero burgs y cero asignaciones políticas.

LÍMITE DE VERIFICACIÓN
  El entorno de construcción bloqueó el acceso del navegador a azgaar.github.io,
  por lo que no fue posible abrir la aplicación en vivo. El archivo fue
  validado estructuralmente contra el loader y MapRepair del código 1.158.0,
  pero no afirmamos que la importación en la interfaz haya sido probada.

RECONSTRUIR
  Node.js 22+, sin dependencias externas:
  node build_derat_tricontinent_map.mjs \
    --map "derat(continente de alfaguara).map" \
    --continents Derat_continentes.geojson \
    --out Derat_Azgaar_Tres_Continentes_v1.map \
    --audit Derat_Azgaar_Tres_Continentes_audit.json

El archivo base .map usado en este build es Bouneia (seed 182800799), que
aporta la cuadrícula. No se reutilizaron sus ciudades, estados ni fronteras.
