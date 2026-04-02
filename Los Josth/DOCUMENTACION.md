# DOCUMENTACION.md - Los Josth

## Version 1.0 - Estandarización Foam (31 Marzo 2026)

### Cambios Realizados

Esta versión estandariza todos los archivos de la Biblia de la Serie con el formato **Foam** para VS Code, permitiendo navegación por knowledge graph y wikilinks.

### Archivos Modificados

#### Personajes (7 archivos)
- **Yen.md** — Añadido frontmatter YAML con tags: `[personaje, protagonista, equipo-b4, navar]`
- **Lena.md** — Añadido frontmatter YAML con tags: `[personaje, equipo-b4, amitia]`
- **Rish.md** — Añadido frontmatter YAML con tags: `[personaje, equipo-b4, amitia]`
- **Bastean.md** — Añadido frontmatter YAML con tags: `[personaje, antagonista, arco-bastean, navar]`
- **Alec.md** — Añadido frontmatter YAML con tags: `[personaje, equipo-b4, amitia]`
- **Herday.md** — Añadido frontmatter YAML con tags: `[personaje, equipo-b4, amitia]`
- **Zhan.md** — Añadido frontmatter YAML con tags: `[personaje, equipo-b4, amitia]`

#### Tierras (8 archivos)
- **Amitia.md** — Añadido frontmatter YAML con tags: `[tierra, amitia, sede-satt, capital]`
- **Navar.md** — Añadido frontmatter YAML con tags: `[tierra, navar, origen-yen, religión]`
- **Atharis.md** — Añadido frontmatter YAML con tags: `[tierra, atharis, ecología, tecnología, lísys]`
- **Derat.md** — Añadido frontmatter YAML con tags: `[tierra, derat, minería, resistencia, ocupación]`
- **Khorza.md** — Añadido frontmatter YAML con tags: `[tierra, khorza, josthe, colonialismo, bosques]`
- **Teknara.md** — Añadido frontmatter YAML con tags: `[tierra, teknara, biopunk, gremios, medicina]`
- **Transtierra(resumen).md** — Añadido frontmatter YAML con tags: `[mundo, transtierra, portales, worldbuilding]`
- **mundo.md** — Añadido frontmatter YAML con tags: `[mundo, transtierra, worldbuilding, portales, sistema]`

#### Tramas/Arcos (6 archivos)
- **Arco-Novata.md** — Añadido frontmatter YAML con tags: `[arco, volumen-1, arco-novata, 589-dt, yen]`
- **Arco-Bastean.md** — Añadido frontmatter YAML con tags: `[arco, volumen-2, arco-bastean, 590-591-dt, corrupción, venganza]`
- **Arco-Tras-la-Tempestad.md** — Añadido frontmatter con tags: `[arco, volumen-3, arco-tras-la-tempestad, 592-594-dt, romance, secreto]`
- **Arco-Navar.md** — Añadido frontmatter con tags: `[arco, volumen-4, arco-navar, 595-596-dt, raíces, familia]`
- **Arco-La-Isla.md** — Añadido frontmatter con tags: `[arco, volumen-5, arco-la-isla, 597-dt, tragedia, horror]`
- **Arco-Depresion-y-Final.md** — Añadido frontmatter con tags: `[arco, volumen-6, arco-final, 598-599-dt, depresión, muerte]`

#### Notas-Temas (4 archivos)
- **La-Playa.md** — Añadido frontmatter con tags: `[tema, símbolo, leitmotiv, playa, amor, muerte, yen, rish]`
- **Linea-Temporal.md** — Añadido frontmatter con tags: `[tema, cronología, timeline, historia]`
- **Represion-Dictadura.md** — Añadido frontmatter con tags: `[tema, historia, dictadura, represión, rish, bastean]`
- **Corrupcion-SATT.md** — Añadido frontmatter con tags: `[tema, corrupción, satt, sistema, poder]`

### Formato Foam Aplicado

Cada archivo ahora incluye:

```yaml
---
tags: [tag1, tag2, tag3]
---
```

Esta estructura permite:
- **Navegación por tags** en Foam
- **Visualización de grafo de conocimiento** con conexiones entre archivos
- **Búsqueda y filtrado** por categorías
- **Detección automática de wikilinks** [[nombre-archivo]]

### Sistema de Tags

Los tags siguen un patrón jerárquico:
- **personaje** — Para todos los archivos de personajes
- **tierra** — Para archivos de lugares/tierras específicas
- **mundo** — Para documentos de worldbuilding general
- **arco** — Para archivos de tramas/arcos narrativos
- **tema** — Para notas temáticas y símbolos

Tags adicionales específicos:
- **equipo-b4** — Miembros del equipo B4
- **protaganista/antagonista** — Rol narrativo
- **volumen-X** — Arcos por volumen
- **lugar-específico** — Como `amitia`, `navar`, `satt`

### Wikilinks

Todos los archivos mantienen sus wikilinks [[ ]] para referencias cruzadas:
- Personajes referencian a otros personajes: `[[Yen]]`, `[[Rish]]`, `[[Lena]]`
- Lugares referencian a instituciones: `[[SATT]]`, `[[Torre-Central-SATT]]`
- Arcos referencian a personajes principales
- Notas-temas referencian a personajes relacionados

### Beneficios del Formato Foam

1. **Knowledge Graph Visual** — Foam genera automáticamente un grafo de conexiones entre todos los archivos
2. **Navegación Bidireccional** — Ctrl+Click sobre cualquier wikilink navega al archivo
3. **Backlinks** — Cada archivo muestra qué otros archivos lo referencian
4. **Tag Explorer** — Panel lateral para filtrar por tags
5. **Graph View** — Vista gráfica de toda la base de conocimiento

### Uso en VS Code

Para aprovechar Foam:
1. Instalar extensión **Foam** en VS Code
2. Abrir workspace desde la carpeta raíz del proyecto
3. Usar `Ctrl+Click` sobre wikilinks para navegar
4. Abrir **Foam: Show Graph** para ver el grafo de conocimiento
5. Usar **Tag Explorer** para filtrar contenido

### Conexión con Biblia de la Serie

Los archivos en `tramas/` contienen la descomposición completa de los 6 volúmenes de la serie:
- Estructura por capítulos
- Evolución de personajes
- Temas centrales
- Epígrafes
- Símbolos y leitmotivs

Estos documentos están totalmente interconectados con los personajes en `personajes/` y las tierras en `tierras/` mediante wikilinks.

---

## Historial de Versiones

### v1.0 (31-03-2026)
- Estandarización completa de 25 archivos con formato Foam
- Añadidos metadatos YAML frontmatter a todos los documentos
- Sistema de tags jerárquico implementado
- Documentación de uso creada

---

## Notas Técnicas

### Convenciones de Nombres
- Archivos de personajes: `Nombre.md` (capitalizado)
- Archivos de tierras: `Nombre.md` (capitalizado)
- Archivos de arcos: `Arco-Nombre.md` (kebab-case con prefijo)
- Archivos de temas: `Tema-Descriptivo.md`

### Convenciones de Tags
- Minúsculas con guiones para espacios: `arco-novata`
- Sin acentos en tags para compatibilidad: `corrupcion`
- Orden jerárquico: categoría → específico → temporal

### Mantenimiento
Al crear nuevos archivos, seguir este patrón:
1. Añadir frontmatter YAML con tags relevantes
2. Usar wikilinks [[ ]] para todas las referencias internas
3. Mantener título de primer nivel (#) coincidente con nombre de archivo
4. Incluir metadatos básicos (período, tema central, etc.)
