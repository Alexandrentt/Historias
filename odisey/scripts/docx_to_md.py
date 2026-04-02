#!/usr/bin/env python3
"""
Script para convertir archivos .docx a .md
Convierte documentos Word a Markdown manteniendo formato básico
"""

import sys
import re
from pathlib import Path
from datetime import datetime

try:
    from docx import Document
except ImportError:
    print("Error: Se necesita instalar python-docx")
    print("Ejecuta: pip install python-docx")
    sys.exit(1)

def clean_text(text: str) -> str:
    """Limpia y normaliza el texto del documento"""
    # Limpiar espacios múltiples
    text = re.sub(r'\s+', ' ', text)
    
    # Reemplazar comillas tipográficas
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace(''', "'").replace(''', "'")
    
    # Limpiar caracteres especiales problemáticos
    text = text.replace('–', '-')  # Guion largo
    text = text.replace('…', '...')  # Elipsis
    
    return text.strip()

def convert_paragraphs_to_markdown(paragraphs) -> str:
    """Convierte párrafos de docx a markdown"""
    markdown_content = []
    
    for para in paragraphs:
        if para.text.strip():
            text = clean_text(para.text)
            
            # Detectar encabezados (texto en negrita y corto)
            if any(run.bold for run in para.runs) and len(text) < 100:
                # Determinar nivel de encabezado por longitud
                if len(text) < 30:
                    level = 1
                elif len(text) < 50:
                    level = 2
                else:
                    level = 3
                
                markdown_content.append(f"{'#' * level} {text}")
            else:
                # Párrafo normal
                markdown_content.append(text)
        else:
            # Línea en blanco
            markdown_content.append("")
    
    return '\n\n'.join(markdown_content)

def add_frontmatter(content: str, filename: str) -> str:
    """Añade frontmatter YAML al documento"""
    today = datetime.now().strftime('%Y-%m-%d')
    word_count = len(re.findall(r'\b\w+\b', content))
    
    frontmatter = f"""---
title: "{filename.replace('.md', '')}"
created: "{today}"
modified: "{today}"
wordCount: {word_count}
tags: [borrador, conversion]
---

"""
    
    return frontmatter + content

def convert_docx_to_md(docx_path: Path) -> bool:
    """Convierte un archivo .docx a .md"""
    try:
        # Leer documento
        doc = Document(docx_path)
        
        # Convertir a markdown
        markdown_content = convert_paragraphs_to_markdown(doc.paragraphs)
        
        # Generar nombre de archivo .md
        md_filename = docx_path.stem + '.md'
        md_path = docx_path.parent / md_filename
        
        # Añadir frontmatter
        final_content = add_frontmatter(markdown_content, md_filename)
        
        # Escribir archivo .md
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"✓ Convertido: {docx_path.name} → {md_filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error convirtiendo {docx_path.name}: {e}")
        return False

def main():
    """Función principal"""
    borradores_dir = Path(__file__).parent.parent / 'borradores'
    
    if not borradores_dir.exists():
        print(f"Error: No se encuentra directorio {borradores_dir}")
        sys.exit(1)
    
    print("=" * 60)
    print("Conversor de .docx a .md para Odisea")
    print("=" * 60)
    
    # Buscar archivos .docx
    docx_files = list(borradores_dir.glob('*.docx'))
    
    if not docx_files:
        print("No se encontraron archivos .docx en la carpeta borradores/")
        sys.exit(0)
    
    print(f"Archivos encontrados: {len(docx_files)}")
    print()
    
    converted = 0
    
    for docx_file in sorted(docx_files):
        if convert_docx_to_md(docx_file):
            converted += 1
    
    print()
    print("=" * 60)
    print(f"Archivos convertidos: {converted}/{len(docx_files)}")
    print("Los archivos .md se han guardado en la misma carpeta")
    print("=" * 60)

if __name__ == '__main__':
    main()
