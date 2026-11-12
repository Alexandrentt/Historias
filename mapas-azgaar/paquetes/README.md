# Paquetes comprimidos de mapas

Los archivos `.map.gz` son compresiones gzip sin pérdida. Se conservan como fuentes para restaurar y verificar individualmente los mapas.

## Fuentes disponibles en GitHub

En la raíz del repositorio existe `Historias_mapas_gz_GitHub.zip`, un paquete histórico que contiene cinco archivos `.map.gz`: Amitia, Atharis, Derat, Khorza y Návar. También existe `Teknara.map.gz` en la raíz. No es necesario reemplazar el ZIP ni subir otra copia para inspeccionar y procesar los seis mapas: GitHub Actions puede leer y descomprimir ambas fuentes.

Los tamaños, hashes, versiones de Azgaar y nombres internos están registrados en `../manifest.json`. La estructura de los archivos descomprimidos se describe en `../datos/inspeccion-tecnica-fuentes.md`.

## Teknara

- Original: `Teknara.map`
- Comprimido: `Teknara.map.gz`
- Tamaño original: 14,982,851 bytes
- Tamaño comprimido: 3,704,720 bytes
- SHA-256 original: `dd9bc3f301e5c2b2be2eeb63c242930f4b5e54e30fe59a44e21f982fd6a40f50`
- SHA-256 gzip: `3fc8d367a2dd8a47403b7a5e63d925620e22f6c0eaefa11f1750d2ea3dbe2042`

El nombre interno del mapa en Azgaar es **Thia**; Teknara es el nombre canónico de la Tierra. La fuente gzip se descomprimió y se leyó correctamente.

## Copias organizadas

Las copias individuales en `mundos/<Tierra>/` o `paquetes/` todavía no se han creado. Antes de duplicar los binarios se debe decidir si realmente aportan valor, dado que las fuentes ya son accesibles dentro del ZIP y en la raíz. Los originales comprimidos no se sobrescriben.
