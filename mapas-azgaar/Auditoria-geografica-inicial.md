# Auditoría geográfica inicial de los mapas

**Fecha:** 12 de noviembre de 2026.  
**Fuentes:** manifiesto y seis archivos Azgaar originales.  
**Estado:** metadatos, estructura interna, geometría de la banda ecuatorial y vistas de los seis mapas inspeccionados.

## Inventario y cobertura

| Tierra | Nombre interno | Versión | Lienzo | Latitud configurada | Longitud configurada | Cobertura longitudinal | Tierra en la banda ecuatorial |
|---|---|---:|---:|---:|---:|---:|---:|
| Amitia | Bacsesia | 1.157.0 | 800 × 1165 | 32.7° N a 30.3° S | 21.6° O a 21.7° E | 43.3° (12.03% del ecuador) | 50.40% |
| Atharis | Iscia | 1.157.0 | 777 × 760 | 45.4° N a 75.2° S | 61.6° O a 61.7° E | 123.3° (34.25%) | 72.79% |
| Derat | Bouneia | 1.158.0 | 1333 × 632 | 90° N a 90° S | 180° O a 180° E | 360° (100%) | 72.57% |
| Khorza | Vileland | 1.158.0 | 800 × 1165 | 90° N a 90° S | 61.8° O a 61.8° E | 123.6° (34.33%) | 79.13% |
| Návar | Ereia | 1.158.0 | 800 × 1165 | 13.5° N a 13.5° S | 9.2° O a 9.3° E | 18.5° (5.14%) | 75.83% |
| Teknara | Thia | 1.158.0 | 800 × 1165 | 90° N a 90° S | 61.8° O a 61.8° E | 123.6° (34.33%) | 19.73% |
| Terra | — | — | Globo completo | Planeta Tierra real completo | 360° | 360° en el mapa del autor | Franja de 145 km como límite cartográfico de la época de Yen |

**Advertencia:** los porcentajes de tierra son proporciones de la franja dentro del intervalo que representa cada mapa. No describen el planeta completo salvo que el mapa cubra los 360°.

## 1. Cobertura insuficiente para la continuidad completa del Portal

El Portal recorre el ecuador completo de cada Tierra. Solo Derat cubre toda la circunferencia. Los mapas de Amitia, Atharis, Khorza, Návar y Teknara dejan sin representar entre 65.7% y 94.9% de las longitudes ecuatoriales.

Esto no significa que los tramos faltantes sean océano ni que no existan tierras allí. Significa que estos archivos no contienen geometría para clasificarlos. No se debe inventar una continuidad terrestre o marítima en esos vacíos.

**Decisión pendiente:** determinar si los mapas existentes son recortes regionales deliberados o si hay que ampliar la cobertura de esos planetas. Si se amplían, la geometría nueva debe construirse como una extensión coherente, no estirando los mapas actuales ni deformando las costas.

## 2. Diferencias en la franja representada

Dentro de la cobertura existente, Teknara es predominantemente acuática en el ecuador (80.27% de agua); Amitia está casi equilibrada; Atharis, Derat, Khorza y Návar tienen predominio terrestre. El desglose por grado de longitud está en `datos/franja-ecuatorial/<Tierra>.csv`.

Los resultados se calcularon mediante intersección de polígonos Voronoi con la banda de 145 km, usando las alturas originales de Azgaar. El cierre de área queda por debajo de 0.009%. Esto es una medición geométrica de los mapas, no una evaluación de seguridad, navegabilidad o clima.

## 3. Khorza carece de entidades políticas y asentamientos

Khorza tiene 100,084 celdas de malla, una gran proporción de tierra, 1,682 ríos, 466 marcadores y 220 zonas, pero sus arreglos de Estados y asentamientos solo contienen los elementos reservados de Azgaar: no hay Estados, burgs ni rutas registradas. Tampoco hay provincias. El mapa conserva una cultura y una religión además de sus registros reservados.

No se ha añadido ninguna entidad. Hay que decidir si Khorza debe permanecer sin Estados y asentamientos, si el mapa es una base física deliberadamente vacía o si falta completar su capa social.

## 4. Los mapas tienen datos internos suficientes para trabajar

Los seis archivos tienen 56 registros, malla de aproximadamente 100,000 puntos, alturas, precipitación, temperatura, SVG y capas de entidades. La malla Voronoi se reconstruyó desde los puntos y límites originales; las visualizaciones y tablas derivadas se generaron sin editar los archivos fuente.

La inspección técnica está en `datos/inspeccion-tecnica-fuentes.md`; el resumen comparativo está en `datos/Resumen-franja-ecuatorial.md`; las vistas están en `visualizaciones/README.md`.

## 5. Terra: geografía global y cartografía diegética

El mapa físico del autor debe representar todo el planeta Tierra real. La franja de 145 km norte-sur centrada en el ecuador es únicamente el límite de la cartografía sistemática alcanzada en tiempos de Yen por las condiciones climáticas y radiactivas. Fuera de ella, la geografía existe pero no está cartografiada en esa época. La franja no es el mapa completo de Terra.

## Próxima fase

1. Decidir si se amplían los cinco mapas con cobertura longitudinal parcial o si sus longitudes no representadas quedan explícitamente abiertas.
2. Revisar Khorza y definir si la ausencia de Estados, burgs y rutas es intencional.
3. Auditar la franja por segmentos: costas, islas, relieve, agua, clima y puntos de acceso.
4. Comprobar rutas terrestres y marítimas, puertos, pasos, abastecimiento y riesgos.
5. Solo después, añadir o revisar infraestructura, asentamientos, fronteras y control político con fechas históricas.

No se han modificado celdas, biomas, costas, ríos, Estados, asentamientos, rutas ni fronteras de los mapas originales.
