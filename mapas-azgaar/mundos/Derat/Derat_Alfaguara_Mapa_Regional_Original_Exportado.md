# Recuperación del mapa regional original de Alfaguara

**Fecha:** 15-11-2026  
**Estado:** recuperado y exportado; paquete completo conservado en la Biblioteca de ChatGPT, aún no incorporado al árbol Git.

## Fuente original

- Archivo: `derat(continente de alfaguara).map`
- Formato: mapa nativo Azgaar Fantasy Map Generator, versión 1.158.0
- Nombre interno de mapa: `Bouneia`
- Dimensiones declaradas: 1333 × 632
- Semilla: `182800799`
- Tamaño original: 15.745.658 bytes
- SHA-256: `6d5277174b51997b83960cdef349cd100f3ad223e7497c31eea492726978cb44`

El archivo .map original se conservó byte por byte en el paquete exportado. No se reescribió ni se sustituyó por el mapa sintético de tres continentes.

## Auditoría estructural

- 100.280 puntos de cuadrícula
- 71.635 registros de celdas en los arrays empaquetados
- 271 features geográficas no centinela
- 16 culturas
- 101 estados, incluido Neutral
- 1.090 burgs reales
- 83 religiones
- 1.766 ríos
- 450 marcadores
- 1.293 rutas
- 12 zonas
- 71 mercados
- 1 journey
- SVG principal con 39 grupos/capas identificadas por `data-layer`

## Paquete de exportación

Archivo: `Derat_Alfaguara_Mapa_Regional_Original_Exportado.zip`  
Tamaño: 23.510.275 bytes  
Ubicación actual: Biblioteca de ChatGPT, `/Derat/Derat_Alfaguara_Mapa_Regional_Original_Exportado.zip`.

Incluye 98 archivos:
- El mapa .map original intacto.
- SVG completo y 39 capas SVG separadas.
- 50 estructuras JSON validadas sintácticamente.
- Capas GeoJSON de burgs, marcadores, rutas y puntos de cuadrícula.
- CSV de coordenadas locales de la cuadrícula.
- Secciones nativas sin clasificar preservadas por número de línea.
- Metadatos, hashes, índices, README y script de exportación.

## Precauciones de interpretación

1. Las coordenadas de las exportaciones GeoJSON conservan el sistema local x/y de Azgaar. **No son longitud/latitud ni están georreferenciadas.** No superponerlas directamente sobre capas CRS84 ni usarlas para asignar ubicaciones reales sin una transformación documentada.
2. Los polígonos de celdas se regeneran mediante el motor Voronoi al cargar el mapa; el archivo .map almacena puntos y atributos empaquetados, no esos polígonos como geometrías independientes.
3. Las capas SVG son representaciones visuales. Editarlas no modifica automáticamente los arrays lógicos del mapa.
4. Las secciones cuya semántica no se identificó se preservaron como datos nativos sin clasificar. No se inventaron nombres ni significados.
5. Los valores de población, estados, burgs y demás atributos son datos generados por Azgaar. No pasan a ser canon narrativo automáticamente.
6. Esta exportación no modifica fronteras, asentamientos, accidentes físicos ni capas geopolíticas de la biblia de Derat.

## Publicación

El informe se versiona en este repositorio. El .map original y el ZIP completo todavía no están en GitHub: la integración GitHub disponible en esta sesión permite crear/actualizar texto, pero no transfiere archivos binarios locales o referencias de adjuntos. Se mantienen en la Biblioteca de ChatGPT para descarga y no se afirma que el contenido completo esté versionado en Git.
