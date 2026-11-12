# Datos editables de los mundos Azgaar

Esta carpeta documenta el formato de trabajo para editar los mapas sin perder su capacidad de reconstrucción.

## Estructura por mundo

El paquete de extracción contiene una carpeta por mundo:

- `header.txt`: cabecera original de Azgaar.
- `world.json`: datos principales editables.
- `biomes.json`: catálogo de biomas editable.
- `map.svg`: SVG original del mapa.
- `tail.dat`: datos adicionales posteriores al SVG, conservados byte por byte.
- `layout.json`: separadores, orden, tamaños y SHA-256 originales.
- `world.compact.json` y `biomes.compact.json`: JSON originales compactos para reconstrucción exacta.

Mundos: Amitia, Atharis, Derat, Korza, Navar y Teknara.

## Compilar

Con Python 3:

```bash
python compile_map.py mapas-azgaar/datos/Amitia -o Amitia.map
```

Para reconstruir exactamente el original, sin aplicar cambios de los JSON legibles:

```bash
python compile_map.py mapas-azgaar/datos/Amitia -o Amitia_original.map --preserve-original
```

Para compilar los cambios, edita `world.json` o `biomes.json` y ejecuta el primer comando.

## Importante

No elimines ni alteres `header.txt`, `map.svg`, `tail.dat` ni `layout.json` al editar los datos. El formato .map contiene secciones adicionales además de los objetos JSON.

La extracción completa validada se conserva como paquete ZIP descargable desde la conversación de ChatGPT. Los componentes pesados (SVG y tail) no se han copiado individualmente a este repositorio en este commit; esta carpeta contiene la documentación del formato y el compilador.
