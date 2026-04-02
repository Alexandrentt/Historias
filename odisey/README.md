# Odisea - Nueva Saga Literaria

## 📖 Descripción
Proyecto literario colaborativo desarrollado con FOAM (Feature-Oriented Architecture for Markdown) para gestionar una nueva saga. Sistema de notas interconectadas que facilita la escritura, organización y revisión de contenido narrativo.

## 🗂️ Estructura del Proyecto

- **capitulos/** - Capítulos finalizados de la novela
- **borradores/** - Versiones en desarrollo y ediciones anteriores
- **personajes/** - Fichas de caracteres principales
- **tierras/** - Mundos y locaciones
- **tramas/** - Arcos narrativos principales
- **notas-temas/** - Temas centrales y conflictos
- **draft/** - Contenido en fase de concepto

## 🔗 Índices

- [INDICE.md](INDICE.md) - Índice tradicional del proyecto
- [Biblia-de-la-serie.md](Biblia-de-la-serie.md) - Biblia narrativa y worldbuilding

## 🚀 Comenzar con FOAM

### Extensiones Recomendadas
- Foam for VSCode
- Markdown All in One
- GitLens

### Uso de Wikilinks
Las notas se conectan mediante wikilinks `[[NombreDeNota]]` para crear una red de conocimiento:

```markdown
[[Personaje]] se desplazó hacia [[Locación]]
```

## 📝 Workflow de Escritura

1. Crear notas nuevas en carpetas temáticas
2. Usar wikilinks para conectar conceptos
3. Revisar el gráfico de Foam para visualizar conexiones
4. Combinar notas en capítulos finalizados

## 📚 Archivos de Configuración

- `.vscode/settings.json` - Configuración de editor y Foam
- `.vscode/extensions.json` - Extensiones recomendadas
- `.gitignore` - Archivos excluidos del repositorio
- `babel.json` - Configuración de transpilación (si aplica)
