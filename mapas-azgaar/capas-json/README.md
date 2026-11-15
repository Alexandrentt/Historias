# Capas JSON editables — mapas Azgaar de Historias

Este directorio indexa la extracción de los seis mundos principales y un mapa auxiliar de Derat.

## Mapas principales

Amitia, Atharis, Derat (mapa regional de Alfaguara), Khorza, Návar y Teknara.

## Mapa auxiliar

`Derat_Tres_Continentes` es una composición provisional y separada del mapa regional de Derat. No se debe tratar como una versión que sustituya a Alfaguara.

## Qué contiene la extracción completa

Cada carpeta de mundo en el paquete integral contiene configuración, biomas, topología de cuadrícula, campos físicos, atributos por celda, entidades (estados, burgs, ríos, rutas, religiones, provincias, zonas, etc.), estilos, registro de capas, bases de nombres y SVG comprimido. Incluye scripts para extraer y reconstruir los .map.

## Validación

Los siete mapas tienen 56 registros nativos. Se reconstruyeron desde JSON y se compararon con sus fuentes: cabecera, SVG, bases de nombres, todos los registros JSON, arrays numéricos y slots vacíos coinciden. El archivo recompilado no es byte-idéntico por la reserialización de JSON. No se verificó su apertura en la interfaz web de Azgaar.

## Precauciones

- Los datos Azgaar no son automáticamente canon narrativo.
- Las coordenadas x/y son locales del mapa, no longitud/latitud.
- Los GeoJSON GIS heredados se derivan del SVG embebido y no equivalen a la exportación nativa de celdas de Azgaar.
- Los originales se mantienen intactos en el paquete integral, separados de los .map recompilados.

Consulta `index.json` y `VALIDACION_RECONSTRUCCION.json` para hashes y resultados por mapa.
