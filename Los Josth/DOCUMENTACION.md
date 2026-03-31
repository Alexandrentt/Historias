# DOCUMENTACION.md - Novela

## Versión 1.3.0 - Migración de Contenido Completa

**Fecha:** 30 de Marzo, 2026  
**Versión:** 1.3.0  
**Estado:** Migración completada - estructura operativa con contenido real

---

### v1.3.0 Cambios:
- **Migración de worldbuilding:** Contenido de `Biblia-de-la-serie-Yen.md` y `Transtierra-El-primer-milenio.md` → `mundo.md`
- **Migración de personajes:** Fichas de Yen, Lena, Rish, Zhan, Alec, Herday, Bastean → `personajes.md`
- **Creación de esquema de capítulos:** Estructura completa de 7 capítulos para Volumen 1 → `INDICE.md`
- **Migración de prólogo:** Extraído de `Borrador-original-capitulo-1-Vath.md` → `capitulo-00-prologo.md` (~1800 palabras)
- **Preparación capítulo 1:** Estructura de reescritura → `capitulo-01.md` (listo para escribir)
- **Creación caps 2-7:** Esquemas detallados con metadatos YAML → `capitulo-02.md` a `capitulo-07.md`
- **Actualización de versionado:** `HISTORIAL-CAMBIO.md` documenta separación de prólogo y reescritura

**Justificación de cambios:**
El usuario solicitó que "pase el contenido íntegramente a donde corresponde". Se realizó migración completa:

1. **Worldbuilding consolidado:** Información de las 7 Tierras, Portal, calendario, historia, especies (josthe), tecnología 90s, sistema de borrado de memorias.

2. **Personajes documentados:** Fichas completas con arcos, motivaciones, relaciones, edades cronológicas (589-599 DT).

3. **Estructura narrativa:** Volumen 1 completamente esquematizado con niveles de importancia (1-3), sinopsis por capítulo, y conexiones de presagios.

4. **Separación de prólogo:** El borrador original mezclaba prólogo + capítulo 1. Se extrajo el prólogo como capítulo 0 independiente con metadatos YAML.

5. **Sistema de reescritura:** Capítulo 1 listo para escribirse desde cero con estructura de 7 escenas definidas.

**Estado post-migración:**
```
CAPÍTULOS LISTOS:
✅ Cap 0: Prólogo (finalizado, ~1800 palabras)
🔄 Cap 1: Vath (en reescritura, estructura lista)
📝 Cap 2-7: Esquemas completos, listos para escribir

DOCUMENTACIÓN:
✅ mundo.md: Worldbuilding completo
✅ personajes.md: 7 personajes principales documentados
✅ INDICE.md: Estructura 6 volúmenes + 7 caps Vol. 1
✅ HISTORIAL-CAMBIO.md: Versionado del Cap 1
```

**Relación de archivos migrados:**
| Archivo fuente | Destino | Estado |
|----------------|---------|--------|
| `Biblia-de-la-serie-Yen.md` | `mundo.md` + `personajes.md` + `INDICE.md` | ✅ Migrado |
| `Transtierra-El-primer-milenio.md` | `mundo.md` (complemento) | ✅ Migrado |
| `Borrador-original-capitulo-1-Vath.md` (líneas 1-25) | `capitulo-00-prologo.md` | ✅ Extraído |
| `Borrador-original-capitulo-1-Vath.md` (líneas 26+) | `capitulo-01.md` (referencia) | 📋 Reescribiendo |
| Esquema Biblia (Caps 2-7) | `capitulo-02.md` a `07.md` | ✅ Estructurado |

---

## Versión 1.2.0 - Estrategia Híbrida .docx + Markdown

**Fecha:** 30 de Marzo, 2026  
**Versión:** 1.2.0  
**Estado:** Flujo de trabajo definido - archivos .docx como fuente maestra + Markdown para reescrituras

---

### v1.2.0 Cambios:
- **Definición de estrategia híbrida:**
  - `Biblia de la serie (Yen).docx` = Fuente maestra (worldbuilding + esquema + capítulos 0, 1, 2)
  - Markdown = Reescrituras (capítulo 1) + nuevos capítulos futuros
  - Sincronización incremental solo cuando sea necesario
- **Documentación de flujo de trabajo:** Creación de `FLUJO-TRABAJO.md`
- **Decisión de diseño:** No migrar todo ahora por eficiencia

**Justificación de cambios:**
El usuario ya tiene un archivo .docx consolidado con TODO el material. En lugar de migración masiva (costosa en tiempo), se adopta estrategia pragmática:
1. Mantener .docx como referencia permanente
2. Usar Markdown para capítulos que se reescriben (caso capítulo 1)
3. Usar Markdown para capítulos nuevos (capítulo 3+)
4. Archivos Markdown actúan como "snapshot activo" mientras .docx es "archivo maestro"

**Relación de componentes:**
```
Biblia de la serie (Yen).docx (fuente maestra - TODO)
         │
         ├─Worldbuilding──────────────→ mundo.md (resumen)
         ├─Esquema serie──────────────→ indice.md + notas.md
         ├─Prólogo────────────────────→ capitulo-00-prologo.md (a migrar)
         ├─Capítulo 1 (viejo)─────────→ borradores/ (archivado)
         └─Capítulo 2─────────────────→ capitulo-02.md (a migrar)
                              ↓
                    NUEVOS: capitulo-01.md (reescritura desde cero)
                           capitulo-03.md+ (nuevos en MD)
```

---

## Versión 1.1.0 - Integración de Borradores Existentes

**Fecha:** 30 de Marzo, 2026  
**Versión:** 1.1.0  
**Estado:** Migración de archivos .docx originales + Sistema de versionado de borradores

---

### v1.1.0 Cambios:
- Identificación de 3 archivos fuente en formato .docx
- Migración de "Borrador original capitulo 1 Vath.docx" a carpeta borradores/
- Creación de sistema de documentación de cambios entre versiones
- Preparación de plantillas para migración de contenido .docx a Markdown
- Ajuste de prioridades: No se requiere README.md para GitHub

**Justificación de cambios:**
El usuario ya tiene contenido escrito en Word que necesita integrar. El capítulo 1 será reescrito, por lo que la versión original se archiva en borradores/ con documentación de qué cambiará. Esto establece un sistema de versionado donde cada reescritura queda documentada.

---

## Versión 1.0.0 - Estructura Inicial

**Fecha:** 30 de Marzo, 2026  
**Versión:** 1.0.0  
**Estado:** Estructura base creada

---

## Descripción del Proyecto

Sistema de archivos para escribir novelas con estructura profesional, inspirado en herramientas como Scrivener pero usando archivos Markdown locales y la extensión Novel Writer de VS Code.

---

## Componentes del Sistema

### 1. README.md
**Propósito:** Guía de usuario rápida  
**Relación:** Punto de entrada para nuevos colaboradores o cuando el autor regresa al proyecto  
**Funcionamiento:** Documenta la estructura de carpetas y convenciones de uso  
**Justificación:** Necesario para mantener consistencia a largo plazo

### 2. DOCUMENTACION.md (este archivo)
**Propósito:** Documentación técnica y versionado del proyecto  
**Relación:** Historial completo de cambios y decisiones de diseño  
**Funcionamiento:** Se actualiza con cada versión, acumulando cambios sin borrar historial  
**Justificación:** Cumple con la regla del usuario de mantener documentación versionada

### 3. indice.md
**Propósito:** Tabla de contenidos navegable de la novela  
**Relación:** Conecta todos los capítulos y proporciona vista general  
**Funcionamiento:** Lista enlaces a cada capítulo con estado y sinopsis  
**Justificación:** Permite navegación rápida sin depender solo de la extensión

### 4. personajes.md
**Propósito:** Fichas de personajes principales y secundarios  
**Relación:** Referencia para mantener consistencia en descripciones y comportamientos  
**Funcionamiento:** Una sección por personaje con datos clave  
**Justificación:** Evita contradicciones en caracterización a través de capítulos

### 5. mundo.md
**Propósito:** Worldbuilding, ambientación, lugares, reglas del mundo  
**Relación:** Referencia para mantener coherencia en el escenario  
**Funcionamiento:** Secciones organizadas por categorías (lugares, cronología, reglas)  
**Justificación:** Esencial para novelas de fantasía, sci-fi o históricas

### 6. notas.md
**Propósito:** Notas sueltas del autor, ideas, investigación  
**Relación:** Espacio libre sin estructura rígida  
**Funcionamiento:** Simple archivo de texto  
**Justificación:** Captura ideas espontáneas sin perturbar la estructura organizada

### 7. capitulos/ (directorio)
**Propósito:** Contener cada capítulo como archivo independiente  
**Relación:** Núcleo del proyecto, contiene el contenido real de la novela  
**Funcionamiento:** Un archivo .md por capítulo con formato estandarizado  
**Justificación:** 
- Permite trabajo granular (un capítulo a la vez)
- Facilita reorganización de capítulos
- Mejor rendimiento en VS Code
- Compatible con control de versiones (Git)

### 8. capitulos/capitulo-XX.md
**Propósito:** Contenido individual de cada capítulo  
**Relación:** Forma parte del directorio capitulos/  
**Estructura interna:**
```
# Capítulo X: Título (H1 - título del capítulo)
Metadatos (palabras, estado, sinopsis)
--- (separador)
Contenido del capítulo con escenas separadas por ---
--- (separador final)
Notas específicas del capítulo
```
**Justificación:** El formato estandarizado permite:
- Parsing automático por extensiones
- Exportación consistente a otros formatos
- Mantenimiento de metadatos por capítulo

### 9. borradores/ (directorio)
**Propósito:** Almacenar versiones antiguas o alternativas de capítulos  
**Relación:** Respaldo de cambios mayores  
**Funcionamiento:** Archivos movidos aquí antes de reescrituras completas  
**Justificación:** Proporciona seguridad para experimentar con reescrituras

---

## Historial de Versiones

### v1.0.0 (30 Mar 2026)
**Cambios:**
- Creación de estructura base del proyecto
- Definición de convenciones de formato
- Creación de archivos de soporte (README, DOCUMENTACION)
- Creación de directorios capitulos/ y borradores/

**Justificación de cambios:**
El usuario solicitó un sistema tipo "Novel Writer" para escribir una novela con capítulos. Esta estructura profesional permite:
1. Organización clara del contenido
2. Navegación eficiente con extensiones de VS Code
3. Control de versiones efectivo
4. Escalabilidad (fácil agregar más capítulos)

---

## Notas Técnicas

### Formato Markdown
Se usa Markdown por ser:
- Portable (funciona en cualquier editor)
- Legible sin procesar
- Compatible con múltiples exportadores (PDF, EPUB, HTML)
- Standard en la industria para escritura técnica y creativa

### Nomenclatura de Archivos
- `capitulo-XX.md` donde XX es número de dos dígitos (01, 02, ..., 99)
- Permite ordenamiento alfabético correcto
- Soporta hasta 99 capítulos (escalable a 999 con tres dígitos si es necesario)

### Metadatos por Capítulo
Cada capítulo incluye:
- **Palabras:** Estimación de extensión para seguimiento
- **Estado:** Indica madurez del borrador
- **Sinopsis:** Resumen para navegación rápida sin leer contenido completo

---

## Relaciones entre Componentes

```
DOCUMENTACION.md (este archivo - mapa del sistema)
        ↓
   README.md (guía de usuario)
        ↓
   indice.md (navegación de contenido)
        ↓
   ┌─────┬─────┬─────┐
   ↓     ↓     ↓     ↓
personajes.md  mundo.md  notas.md  capitulos/
                                      ↓
                              capitulo-01.md
                              capitulo-02.md
                                  ...
```

La estructura está diseñada para que el flujo de trabajo sea:
1. Consultar índice para ver estado general
2. Elegir capítulo a trabajar
3. Usar archivos de referencia (personajes, mundo) para mantener consistencia
4. Documentar notas sueltas en notas.md
5. Actualizar DOCUMENTACION.md al finalizar cada versión
