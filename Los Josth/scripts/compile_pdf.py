#!/usr/bin/env python3
"""
Script de compilación de PDF con Pandoc + LaTeX
Combina todos los capítulos en un único PDF maquetado profesionalmente
Soporta: epígrafes, ilustraciones [ilustracion:descripcion], pensamientos en cursiva
"""

import subprocess
import sys
import re
from pathlib import Path
import tempfile
import yaml

# Contador global de ilustraciones
ilustracion_counter = 0

def extract_metadata(filepath: Path) -> dict:
    """Extrae el frontmatter YAML de un archivo markdown"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        try:
            end = content.index('---', 3)
            yaml_content = content[3:end].strip()
            return yaml.safe_load(yaml_content) or {}
        except:
            return {}
    return {}

def process_illustrations(content: str, chapter_num: int) -> str:
    """
    Convierte [ilustracion:descripcion] a comandos LaTeX
    Formato: [ilustracion:Yen archivista]
    Resultado: \\ilustracionplaceholder{cap01_001}{Yen archivista}{01}
    """
    global ilustracion_counter
    
    def replace_illustration(match):
        global ilustracion_counter
        ilustracion_counter += 1
        descripcion = match.group(1).strip()
        # Generar nombre de archivo esperado: cap01_001, cap01_002, etc.
        img_num = f"{ilustracion_counter:03d}"
        img_filename = f"cap{chapter_num:02d}_{img_num}"
        
        # Por ahora usamos placeholder (cuando existan las imágenes reales, 
        # cambiar a \ilustracion)
        return f"\\ilustracionplaceholder{{{img_filename}}}{{{descripcion}}}{{{chapter_num}.{ilustracion_counter:03d}}}"
    
    # Patrón: [ilustracion:descripcion]
    pattern = r'\[ilustracion:([^\]]+)\]'
    return re.sub(pattern, replace_illustration, content)

def process_epigraphs(content: str, metadata_epigraph: str = None) -> str:
    """
    Procesa epígrafes en formato markdown quote a LaTeX epigraph
    Si metadata_epigraph existe, usa ese y elimina los bloques > del cuerpo
    Formato esperado:
    > Texto del epígrafe
    > — Autor, *Obra*
    """
    # Si hay epígrafe en metadata, eliminar bloques de quote del cuerpo
    if metadata_epigraph:
        # Eliminar bloques de quote consecutivos (que serían el epígrafe duplicado)
        lines = content.split('\n')
        result = []
        skip_quote = False
        in_quote_block = False
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('>'):
                in_quote_block = True
                continue
            elif in_quote_block and not stripped:
                # Línea vacía después del bloque de quote
                in_quote_block = False
                continue
            elif in_quote_block:
                in_quote_block = False
            result.append(line)
        
        content = '\n'.join(result)
        
        # Procesar el epígrafe de metadata
        epigraph_lines = metadata_epigraph.strip().split('\n')
        if len(epigraph_lines) >= 1:
            texto = ' '.join(epigraph_lines)
            # Formatear como epígrafe LaTeX usando el nuevo entorno
            latex_epigraph = f"""\\begin{{epigrafe}}
{texto}
\\end{{epigrafe}}

"""
            content = latex_epigraph + content
        return content
    
    # Procesa bloques de quote consecutivos del cuerpo
    lines = content.split('\n')
    result = []
    in_epigraph = False
    epigraph_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('>') and not in_epigraph:
            in_epigraph = True
            epigraph_lines = [stripped[1:].strip()]
        elif stripped.startswith('>') and in_epigraph:
            epigraph_lines.append(stripped[1:].strip())
        elif in_epigraph:
            if len(epigraph_lines) >= 2:
                texto = ' '.join(epigraph_lines[:-1])
                fuente = epigraph_lines[-1]
                fuente = re.sub(r'^[-—]\s*', '', fuente)
                fuente = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', fuente)
                
                result.append(f"\\begin{{epigrafe}}")
                result.append(texto)
                result.append(f"\\\\[0.3em]")
                result.append(f"{{--- {fuente}}}")
                result.append(f"\\end{{epigrafe}}")
                result.append("")
            else:
                for el in epigraph_lines:
                    result.append(f"> {el}")
            
            in_epigraph = False
            epigraph_lines = []
            result.append(line)
        else:
            result.append(line)
    
    if in_epigraph and len(epigraph_lines) >= 2:
        texto = ' '.join(epigraph_lines[:-1])
        fuente = epigraph_lines[-1]
        fuente = re.sub(r'^[-—]\s*', '', fuente)
        fuente = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', fuente)
        
        result.append(f"\\begin{{epigrafe}}")
        result.append(texto)
        result.append(f"\\\\[0.3em]")
        result.append(f"{{--- {fuente}}}")
        result.append(f"\\end{{epigrafe}}")
    elif in_epigraph:
        for el in epigraph_lines:
            result.append(f"> {el}")
    
    return '\n'.join(result)

def process_dialogues(content: str) -> str:
    """
    Preserva los saltos de línea para que cada línea sea un párrafo separado.
    Las líneas que empiezan con — (em-dash) para diálogos
    necesitan mantenerse como párrafos independientes.
    """
    lines = content.split('\n')
    result = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            # Línea vacía, mantenerla
            result.append(line)
        elif stripped.startswith('—') or stripped.startswith('-'):
            # Diálogo: asegurar que sea un párrafo separado agregando línea vacía después
            result.append(line)
            result.append('')  # Línea vacía para separar párrafos
        else:
            # Texto narrativo: si la línea anterior no fue diálogo, 
            # mantener como párrafo continuo
            result.append(line)
    
    return '\n'.join(result)


def process_thoughts(content: str) -> str:
    """Asegura que los pensamientos en cursiva tengan formato correcto"""
    # Normalizar espacios alrededor de asteriscos de apertura
    content = re.sub(r'\*\s+', '*', content)  # Eliminar espacio después de *
    content = re.sub(r'\s+\*', '*', content)  # Eliminar espacio antes de *
    
    # Asegurar que haya espacio antes de * si no está al inicio de línea
    content = re.sub(r'([^\s\n])\*([^\*])', r'\1 *\2', content)
    
    # Normalizar múltiples asteriscos consecutivos
    content = re.sub(r'\*{2,}', '*', content)
    
    return content

def prepare_chapter(filepath: Path, chapter_num: int) -> str:
    """
    Prepara un capítulo para incluir en el PDF.
    Procesa: frontmatter, epígrafes, ilustraciones, pensamientos
    Filtra anotaciones (todo después de --- o ## Continúa aquí...)
    """
    global ilustracion_counter
    ilustracion_counter = 0  # Reset por capítulo
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = extract_metadata(filepath)
    
    # Extraer solo el contenido (sin frontmatter)
    if content.startswith('---'):
        try:
            end = content.index('---', 3)
            body = content[end+3:].strip()
        except:
            body = content
    else:
        body = content
    
    # Filtrar anotaciones: detenerse al encontrar separador horizontal --- o ## Continúa aquí...
    # Buscar el separador que indica fin del contenido principal
    stop_patterns = [
        r'\n---\s*\n',  # Separador horizontal
        r'\n##\s*Continúa aquí.*',  # Sección "Continúa aquí..."
        r'\n#\s*Notas?.*',  # Sección de notas
        r'\n#\s*Anotaciones?.*',  # Sección de anotaciones
    ]
    
    for pattern in stop_patterns:
        match = re.search(pattern, body, re.IGNORECASE)
        if match:
            body = body[:match.start()].strip()
            break
    
    # Obtener epígrafe de metadata si existe (también buscar 'epigraphe' con 'e' al final)
    metadata_epigraph = metadata.get('epigraph') or metadata.get('epigraphe')
    
    # Buscar epígrafe en el cuerpo en formato: *Epígrafe:* *"texto"*
    epigraph_body_pattern = r'^\*Epígrafe:\*\s*\*"([^"]+)"\*\s*$'
    match = re.search(epigraph_body_pattern, body, re.MULTILINE | re.IGNORECASE)
    if match and not metadata_epigraph:
        metadata_epigraph = match.group(1)
        # Eliminar la línea del epígrafe del cuerpo
        body = re.sub(epigraph_body_pattern, '', body, flags=re.MULTILINE | re.IGNORECASE).strip()
    
    # Procesar elementos especiales
    body = process_illustrations(body, chapter_num)
    body = process_epigraphs(body, metadata_epigraph)
    body = process_thoughts(body)
    body = process_dialogues(body)
    
    # Construir el capítulo procesado
    title = metadata.get('title', f'Capítulo {chapter_num}')
    
    # Agregar salto de página antes del capítulo (excepto el primero)
    pagebreak = "\\clearpage\n\n" if chapter_num > 1 else ""
    
    # Eliminar el título markdown del body
    body = re.sub(r'^# .+$', '', body, flags=re.MULTILINE, count=1)
    body = body.strip()
    
    processed = f"""{pagebreak}\\chapter*{{{title}}}
\\addcontentsline{{toc}}{{chapter}}{{{title}}}
\\markboth{{{title}}}{{{title}}}

{body}
"""
    
    return processed

def build_pdf(output_path: Path = None):
    """Compila el PDF final"""
    
    base_dir = Path(__file__).parent.parent
    capitulos_dir = base_dir / 'capitulos'
    template_dir = base_dir / 'pdf_template'
    ilustraciones_dir = base_dir / 'ilustraciones'
    
    if output_path is None:
        output_path = base_dir / 'Los_Josth.pdf'
    
    # Verificar dependencias
    deps = ['pandoc', 'pdflatex']
    for dep in deps:
        result = subprocess.run(['which', dep], capture_output=True)
        if result.returncode != 0:
            print(f"Error: {dep} no está instalado")
            print("Instala con: sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-latex-extra texlive-xetex")
            sys.exit(1)
    
    # Recopilar capítulos (buscar recursivamente en subcarpetas)
    capitulos = sorted(capitulos_dir.glob('**/*.md'))
    if not capitulos:
        print("Error: No se encontraron capítulos")
        sys.exit(1)
    
    print(f"Capítulos encontrados: {len(capitulos)}")
    
    # Crear archivo markdown combinado temporal
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        combined_path = Path(f.name)
        
        # Encabezado YAML con metadata del libro
        f.write("""---
title: "Los Josth"
author: ""
date: ""
lang: es
---

""")
        
        # Procesar cada capítulo
        for i, cap in enumerate(capitulos, 1):
            print(f"Procesando: {cap.name}")
            processed = prepare_chapter(cap, i)
            f.write(processed)
            f.write("\n\n")
    
    # Compilar con pandoc
    template_path = template_dir / 'template.tex'
    
    cmd = [
        'pandoc',
        str(combined_path),
        '-o', str(output_path),
        '--pdf-engine=pdflatex',
        '--template', str(template_path),
        '--toc',
        '--toc-depth=2',
        '-V', 'documentclass=book',
        '-V', 'papersize=a5',
        '-V', 'fontsize=11pt',
        '-V', 'geometry:margin=2cm',
        '-V', 'linestretch=1.5',
        '-V', 'lang=es',
        '--variable', 'graphics=yes',
        '--variable', 'links-as-notes=true',
    ]
    
    print(f"\nCompilando PDF: {output_path}")
    print(f"Usando plantilla: {template_path}")
    
    if ilustraciones_dir.exists():
        print(f"Carpeta de ilustraciones: {ilustraciones_dir}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Limpiar archivo temporal
    combined_path.unlink(missing_ok=True)
    
    if result.returncode == 0:
        print(f"✓ PDF generado exitosamente: {output_path}")
        print(f"  Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
        print(f"\nNota: Las ilustraciones usarán placeholders hasta que agregues")
        print(f"      las imágenes en: {ilustraciones_dir}/")
        print(f"      Formato esperado: cap01_001.png, cap01_002.png, etc.")
    else:
        print("✗ Error al compilar:")
        print(result.stderr)
        if result.stdout:
            print("Salida:")
            print(result.stdout)
        sys.exit(1)

def main():
    output = Path('Los_Josth.pdf')
    if len(sys.argv) > 1:
        output = Path(sys.argv[1])
    
    build_pdf(output)

if __name__ == '__main__':
    main()
