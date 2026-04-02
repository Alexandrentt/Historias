# DOCUMENTACION.md - Odisea

## Version 0.3 - Actualización de Personajes (31 Marzo 2026)

### Cambios Realizados

Esta versión actualiza los personajes principales basándose en la aclaración del usuario sobre el grupo y el secuestro.

### Personajes Actualizados

#### Grupo de Protagonistas
- **Jay Cowler**: Hermano mayor, líder del grupo (mantenido del borrador)
- **Emma Cowler**: Hermana menor, inteligencia del grupo (mantenida del borrador)
- **Noah**: Amigo leal, parte del grupo principal (ascendido de secundario)
- **Kan**: Personaje secuestrado, catalizador del viaje (nuevo rol)

#### Cambios Clave
- **Jay y Emma**: Confirmados como hermanos (no solo conocidos)
- **Noah**: Ahora parte del grupo principal (no secundario)
- **Kan**: El personaje secuestrado (no la hermana adoptiva)

### Archivos Actualizados

#### Personajes Principales
- **Protagonistas.md**: Actualizado con nombres y roles específicos
- **Biblia-de-la-serie.md**: Actualizado con personajes correctos
- **Arco-Principal.md**: Actualizado para reflejar secuestro de Kan

### Elementos Mantenidos del Borrador
- **Personalidades**: Basadas en los personajes del material original
- **Habilidades**: Mismas skills y características
- **Dinámica**: Compañerismo que se vuelve genuino
- **Mundo**: Idaho/Boise → Alfaguara (mismo concepto)

### Ventajas de esta Configuración
- **Dinámica equilibrada**: Tres protagonistas activos más el secuestrado
- **Motivación clara**: Rescatar a Kan, su amigo
- **Conexión emocional**: Lazos fraternales + amistad
- **Material existente**: Kan y Noah ya tenían contexto en el borrador

---

## Version 0.2 - Conceptualización de Odisea (31 Marzo 2026)

### Cambios Realizados

Esta versión establece el concepto narrativo y mundo de "Odisea", basándose en el universo de Transtierra pero enfocándose en Derat post-guerra.

### Concepto Desarrollado

#### Mundo y Ambientación
- **Ubicación**: Derat, continente de Alfaguara (años ~600 DT)
- **Contexto**: Post-guerra, sociedad fragmentada en ciudades-estado
- **Conflicto central**: Ocupación del "Régimen" (fuerzas CTT/empresas Amitianas)
- **Recurso clave**: Madianíta (metal estratégico, monopolio Amitiano)

#### Personajes Principales
- **Hermano Mayor**: Protector, skills de supervivencia
- **Hermana Menor**: Cuidadora, inteligencia práctica
- **Hermana Adoptiva**: Secuestrada, catalizador del viaje
- **Amigo**: Acompañante en la odisea

#### Arco Narrativo
1. **Secuestro** de la hermana adoptiva
2. **Viaje épico** por Alfaguara buscando pistas
3. **Descubrimiento** de la verdad sobre la opresión
4. **Confrontación** con las fuerzas del Régimen

### Archivos Procesados

#### Conversión de Borradores
- **Script creado**: `scripts/docx_to_md.py` para convertir .docx a .md
- **Archivos convertidos**:
  - `temporada 1.docx` → `temporada 1.md` (41,246 palabras)
  - `Temporada 2.docx` → `Temporada 2.md` (6,000+ palabras)
- **Material previo**: Versión con personajes Jay y Emma como referencia

#### Biblia de la Serie Actualizada
- **Concepto completo**: Mundo, personajes, arcos, temas
- **Conexiones**: Vínculos directos con universo Los Josth
- **Inspiraciones**: Odisea homérica, Mad Max, road movies
- **Temáticas**: Odisea personal, resiliencia, verdad vs opresión

### Estructura de Folders Mantenida
Todas las carpetas estructurales listas para desarrollo:
- `personajes/` - Para fichas de personajes
- `tierras/` - Para mundo y locaciones
- `tramas/` - Para arcos narrativos
- `notas-temas/` - Para temas y símbolos
- `capitulos/` - Para capítulos finalizados
- `borradores/` - Con material convertido
- `draft/` - Para contenido conceptual

---

## Version 0.1 - Configuración Inicial (31 Marzo 2026)

### Cambios Realizados

Esta versión establece la estructura base del proyecto "Odisea", siguiendo el mismo patrón organizacional que "Los Josth" con sistema FOAM.

### Estructura Creada

#### Archivos de Configuración
- **README.md** — Descripción del proyecto y guía de uso
- **INDICE.md** — Índice navegable del contenido (vacío por ahora)
- **DOCUMENTACION.md** — Este archivo, registro de cambios y decisiones
- **.vscode/settings.json** — Configuración de VS Code para FOAM
- **.gitignore** — Archivos excluidos del control de versiones

#### Carpetas Estructurales (por crear)
- **personajes/** — Para fichas de personajes
- **tierras/** — Para mundos y locaciones
- **tramas/** — Para arcos narrativos
- **notas-temas/** — Para temas y símbolos
- **capitulos/** — Para capítulos finalizados
- **borradores/** — Para versiones en desarrollo
- **draft/** — Para contenido conceptual

### Formato FOAM Aplicado

Se seguirá el mismo patrón que "Los Josth":

```yaml
---
tags: [tag1, tag2, tag3]
---
```

### Sistema de Tags (a implementar)

Los tags seguirán un patrón jerárquico:
- **personaje** — Para todos los archivos de personajes
- **tierra** — Para archivos de lugares/tierras específicas
- **mundo** — Para documentos de worldbuilding general
- **arco** — Para archivos de tramas/arcos narrativos
- **tema** — Para notas temáticas y símbolos

### Próximos Pasos

1. Definir el mundo y concepto central de "Odisea"
2. Crear personajes principales
3. Establecer arcos narrativos
4. Desarrollar la biblia de la serie

---

## Historial de Versiones

### v0.1 (31-03-2026)
- Configuración inicial del proyecto
- Estructura de carpetas definida
- Archivos base creados siguiendo patrón "Los Josth"

---

## Notas Técnicas

### Convenciones de Nombres
- Archivos de personajes: `Nombre.md` (capitalizado)
- Archivos de tierras: `Nombre.md` (capitalizado)
- Archivos de arcos: `Arco-Nombre.md` (kebab-case con prefijo)
- Archivos de temas: `Tema-Descriptivo.md`

### Mantenimiento
Al crear nuevos archivos, seguir este patrón:
1. Añadir frontmatter YAML con tags relevantes
2. Usar wikilinks [[ ]] para todas las referencias internas
3. Mantener título de primer nivel (#) coincidente con nombre de archivo
4. Incluir metadatos básicos (período, tema central, etc.)
