# Publicación completa de los mapas Azgaar

La conexión de GitHub usada en ChatGPT permite crear archivos de texto, pero no transferir directamente los ZIP/binarios de esta entrega. Para incorporar los archivos reales al repositorio, se incluye un publicador local.

## Qué publica

- Las 310 entradas del paquete de capas JSON/SVG en `mapas-azgaar/capas-json/`.
- Los siete originales `.map` en `mapas-azgaar/mapas-originales/`.
- Los siete reconstruidos `.map` en `mapas-azgaar/mapas-recompilados/`.

## Pasos

1. Descarga desde la conversación los tres paquetes: `Mapas_Azgaar_Capas_JSON_7_Mapas.zip`, `Mapas_Azgaar_Originales_7_MAP.zip` y `Mapas_Azgaar_Recompilados_7_MAP.zip`.
2. Clona `https://github.com/Alexandrentt/Historias.git` en un ordenador con Git y Python 3.
3. Copia los tres ZIP a la carpeta raíz del clon.
4. Coloca este archivo y el script en `mapas-azgaar/` (ya están versionados en el repositorio).
5. Desde la raíz del clon, ejecuta `python mapas-azgaar/publicar_paquete_completo.py`.

El script valida rutas del ZIP y evita archivos individuales de 100 MB o más; extrae los contenidos, crea un commit y ejecuta `git push`. Requiere que Git esté autenticado con permiso de escritura. Revisa el commit antes de continuar si prefieres publicar manualmente.

El ZIP integral es redundante para este proceso y no hace falta copiarlo al repositorio. No se versionan los ZIP grandes: se versionan sus contenidos editables y los archivos `.map` por separado.
