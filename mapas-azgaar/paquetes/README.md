# Paquetes comprimidos de mapas

Los archivos .map.gz son compresiones gzip sin pérdida. Deben conservarse por separado para facilitar la restauración y la verificación individual.

## Paquete ZIP

En la raíz del repositorio existe Historias_mapas_gz_GitHub.zip, que corresponde a un paquete anterior de cinco mapas. No lo confundas con el paquete actualizado de seis mapas preparado localmente después de añadir Teknara.

## Teknara

- Original: Teknara.map
- Comprimido: Teknara.map.gz
- Tamaño original: 14,982,851 bytes
- Tamaño comprimido: 3,704,720 bytes
- SHA-256 original: dd9bc3f301e5c2b2be2eeb63c242930f4b5e54e30fe59a44e21f982fd6a40f50
- SHA-256 gzip: 3fc8d367a2dd8a47403b7a5e63d925620e22f6c0eaefa11f1750d2ea3dbe2042

La copia gzip se descomprimió y se comparó byte por byte con el original. La verificación fue correcta. El binario todavía está pendiente de incorporarse a este repositorio; los hashes también están registrados en ../manifest.json.

## Incorporación recomendada

Coloca los seis .map.gz y SHA256SUMS.json en esta carpeta, actualiza el ZIP y comprueba los hashes antes de confirmar los cambios. No elimines ni reemplaces los originales locales.
