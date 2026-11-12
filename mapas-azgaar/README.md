# Mapas de Azgaar — Historias

Este directorio organiza el inventario y las copias de los seis mundos registrados: Amitia, Atharis, Derat (continente de Alfaguara), Korza, Návar y Teknara.

## Estructura

- manifest.json: inventario técnico, dimensiones, semillas y hashes SHA-256.
- paquetes/: documentación de los archivos comprimidos y del paquete ZIP.
- originales/: destino reservado para los .map originales cuando se incorporen individualmente.
- exportaciones/: destino para imágenes y formatos derivados, nunca sustitutos del original.
- versiones/: snapshots aprobados antes de cambios importantes.

## Conservación e integridad

- El archivo .map original es la fuente de verdad y debe conservarse byte por byte.
- Los .map.gz son copias comprimidas sin pérdida; al descomprimirlos deben reproducir exactamente el original.
- Antes de aceptar una copia, verificar su SHA-256 con manifest.json.
- No editar directamente el único original; crear una copia o una versión nueva.
- PNG, SVG, JSON parciales y otros derivados no sustituyen un proyecto editable de Azgaar.

## Estado actual de GitHub

El ZIP que ya está en la raíz del repositorio, Historias_mapas_gz_GitHub.zip, contiene la versión anterior de cinco mapas. Teknara ya está registrado en el manifiesto con sus hashes, pero el ZIP actualizado de seis mapas y el archivo individual Teknara.map.gz todavía no se han incorporado a GitHub.

El manifiesto marca explícitamente los originales como no cargados individualmente. No se debe interpretar el registro de metadatos como si el archivo binario estuviera respaldado en GitHub.

## Abrir un mapa

En Azgaar's Fantasy Map Generator, usa Load → Machine y selecciona el archivo .map original o una copia descomprimida.

- Generador: https://azgaar.github.io/Fantasy-Map-Generator/
- Formato y datos: https://github.com/Azgaar/Fantasy-Map-Generator/wiki/Data-import
