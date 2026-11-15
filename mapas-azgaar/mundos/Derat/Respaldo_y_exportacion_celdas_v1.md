# Respaldo y exportación de celdas de Derat — v1

**Fecha:** 15 de noviembre de 2026  
**Repositorio:** `Alexandrentt/Historias`  
**Rama de trabajo:** `main`

## Copia de seguridad del repositorio

Se creó la rama `backup/Derat-main-2026-11-15` desde el estado de `main` cuyo HEAD era `f15246aedbe54de637f6f272137b79243abde65a`.

La rama conserva el árbol del repositorio de ese momento. No incluye archivos que solo estuvieran en la Biblioteca o como adjuntos externos.

[Consultar la rama de respaldo](https://github.com/Alexandrentt/Historias/tree/backup/Derat-main-2026-11-15).

## Recuperación del mapa nativo generado

Se recuperó de la Biblioteca el archivo `Derat_Azgaar_Tres_Continentes_v1.map`.

- Tamaño: 3.863.664 bytes.
- SHA-256: `0e99e077e61e643306db68fbdfae488432556c45379484bf7d104d865e7045e1`.
- Versión: Azgaar 1.158.0.
- Ubicación conservada: Biblioteca de ChatGPT, `/Derat/Derat_Azgaar_Tres_Continentes_v1.map`.
- Estado GitHub: el binario todavía no está versionado en el repositorio.

El hash coincide con el registrado en `Derat_Azgaar_Tres_Continentes_audit.json`. No se modificó el archivo nativo.

## Exportación derivada de celdas

Se generaron tres capas GeoJSON, conservadas en la Biblioteca de ChatGPT:

| Continente | Archivo | Celdas | Bytes |
|---|---|---:|---:|
| Alfaguara | `Derat_Azgaar_celdas_Alfaguara_v1.geojson` | 8.619 | 7.874.720 |
| Vardena | `Derat_Azgaar_celdas_Vardena_v1.geojson` | 14.939 | 13.646.770 |
| Edravia | `Derat_Azgaar_celdas_Edravia_v1.geojson` | 4.921 | 4.452.380 |

Total: 28.479 celdas asignadas a los tres contornos propuestos. Cada capa pasó las verificaciones: 0 regiones vacías, 0 geometrías inválidas y 0 solapamientos de área positiva.

Los polígonos son reconstrucciones independientes de Voronoi desde puntos pack regenerados; no son geometrías almacenadas literalmente en el .map. Los atributos siguen siendo datos Azgaar generados, no canon.

## Herramienta reproducible

Se añadió al repositorio `exportar_celdas_alfaguara_v1.py`. Requiere Python, NumPy, SciPy y Shapely. No modifica el mapa fuente.

Ejemplo:

```bash
python exportar_celdas_alfaguara_v1.py \
  --map Derat_Azgaar_Tres_Continentes_v1.map \
  --continents Derat_Azgaar_Tres_Continentes/Derat_continentes.geojson \
  --continent Alfaguara \
  --out Derat_Azgaar_celdas_Alfaguara_v1.geojson
```

## Pendientes y límites

1. El mapa regional original de Alfaguara/Bouneia que se usó como base del build no se ha recuperado todavía.
2. La copia nativa generada y las tres capas GeoJSON (28.479 celdas en total) están en la Biblioteca, no en GitHub.
3. La prueba de apertura del `.map` en la interfaz de Azgaar sigue pendiente.
4. No se añadieron nombres canónicos, ciudades, fronteras, recursos localizados ni áreas de control.
5. Las celdas reconstruidas son una capa de trabajo derivada; cualquier reconciliación con el atlas físico debe ser independiente y documentada.

