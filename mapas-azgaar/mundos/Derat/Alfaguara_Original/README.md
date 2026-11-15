# Alfaguara — mapa regional original

Esta carpeta contiene el índice JSON estructurado y la documentación de la exportación del mapa regional original de Alfaguara (nombre interno del mapa: **Bouneia**).

## Índice de datos

- [manifest_exportacion.json](./manifest_exportacion.json): inventario de capas, conteos, procedencia, formatos y advertencias de coordenadas.

## Fuente y paquete completo

- Fuente nativa: `derat(continente de alfaguara).map`, Azgaar 1.158.0.
- SHA-256: `6d5277174b51997b83960cdef349cd100f3ad223e7497c31eea492726978cb44`.
- Paquete ZIP completo (98 archivos): `Derat_Alfaguara_Mapa_Regional_Original_Exportado.zip`, conservado en la Biblioteca de ChatGPT.

## Estado de publicación

El índice JSON está versionado en este repositorio. El paquete completo y el archivo .map original todavía no están en GitHub. Los archivos de datos detallados (JSON/GeoJSON/SVG) están inventariados en el índice y se conservan en el ZIP de la Biblioteca.

## Advertencias

1. Las coordenadas de los GeoJSON son coordenadas locales x/y de Azgaar, no longitud/latitud ni CRS84.
2. Los polígonos de celdas se regeneran mediante Voronoi al cargar el mapa; no deben confundirse con geometrías originales almacenadas.
3. Los atributos generados por Azgaar no se convierten automáticamente en canon narrativo.
4. Editar las capas SVG no modifica automáticamente los datos lógicos del mapa.
