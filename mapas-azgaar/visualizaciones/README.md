# Visualizaciones de los mapas fuente

Estas imágenes y archivos vectoriales se generaron directamente a partir de los seis mapas Azgaar comprimidos que ya estaban en el repositorio. No sustituyen los originales ni alteran sus datos.

## Comparación global de cobertura

[Portal-linea-ecuatorial.png](Portal-linea-ecuatorial.png) muestra tierra y agua sobre la **línea exacta del ecuador (0°)**, donde se encuentra el Portal. [Portal-cobertura-ecuatorial.png](Portal-cobertura-ecuatorial.png) muestra la **banda de 145 km** alrededor del ecuador, útil para estudiar el terreno cercano. En ambos gráficos el gris rayado significa que el mapa fuente no cubre ese tramo; no significa océano. Terra aparece como base física pendiente.

## Vistas generales

| Tierra | Mapa completo | Franja ecuatorial resaltada |
|---|---|---|
| Amitia | [PNG](vistas-previas/Amitia.png) | [PNG](vistas-previas/Amitia-franja-ecuatorial.png) |
| Atharis | [PNG](vistas-previas/Atharis.png) | [PNG](vistas-previas/Atharis-franja-ecuatorial.png) |
| Derat | [PNG](vistas-previas/Derat.png) | [PNG](vistas-previas/Derat-franja-ecuatorial.png) |
| Khorza | [PNG](vistas-previas/Khorza.png) | [PNG](vistas-previas/Khorza-franja-ecuatorial.png) |
| Návar | [PNG](vistas-previas/Návar.png) | [PNG](vistas-previas/Návar-franja-ecuatorial.png) |
| Teknara | [PNG](vistas-previas/Teknara.png) | [PNG](vistas-previas/Teknara-franja-ecuatorial.png) |

La banda roja representa 145 km norte-sur centrados en el ecuador según los límites geográficos configurados en cada mapa. No indica que todo ese terreno sea accesible o esté cartografiado por los habitantes; esa distinción es especialmente importante para Terra.

## Vectores

Los SVG extraídos se conservan comprimidos en `fuentes/<Tierra>.svg.gz`. Se pueden descomprimir para inspección vectorial. Las vistas PNG se renderizan con librsvg a partir del SVG original.

## Advertencia

Los mapas Azgaar tienen extensiones geográficas diferentes. La vista completa de un mapa no equivale necesariamente a una cobertura planetaria de 360°. Consulta [la primera auditoría de la franja ecuatorial](../datos/Resumen-franja-ecuatorial.md) antes de usar una imagen para diseñar una ruta.
