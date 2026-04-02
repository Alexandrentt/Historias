#!/usr/bin/env python3
"""
Script de normalización de pensamientos para Los Josth
Limpia el formato inconsistente de asteriscos en pensamientos
Actualiza automáticamente: modified, wordCount
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def normalize_thoughts(content: str) -> str:
    """
    Normaliza pensamientos al formato estándar: *texto*
    
    Maneja casos como:
    - *No, no, no** ¡Sí me van a sacar!***** → *No, no, no ¡Sí me van a sacar!*
    - *¿**N**ació aquí? *pensó Yen → *¿Nació aquí?* pensó Yen
    - *texto** → *texto*
    - **texto** → *texto* (en contexto de pensamiento)
    """
    
    # Caso 1: Limpiar múltiples asteriscos consecutivos
    # Ej: *No, no, no** ¡Sí me van a sacar!*****
    pattern1 = r'\*+([^*\n]+?)\*+'
    
    def replace_thought(match):
        text = match.group(1).strip()
        # Limpiar asteriscos internos sueltos
        text = re.sub(r'\*+', '', text)
        return f'*{text}*'
    
    content = re.sub(pattern1, replace_thought, content)
    
    # Caso 2: Pensamientos que terminan con espacio antes del cierre
    # Ej: *texto * → *texto*
    content = re.sub(r'\*([^*]+?)\s*\*', r'*\1*', content)
    
    # Caso 3: Doble asterisco que debería ser simple
    # Ej: **texto** → *texto* (solo en contexto de pensamiento corto)
    content = re.sub(r'\*\*([^*\n]{1,50}?)\*\*', r'*\1*', content)
    
    return content

def extract_body_content(content: str) -> str:
    """Extrae el contenido del cuerpo sin el frontmatter YAML"""
    if content.startswith('---'):
        try:
            end = content.index('---', 3)
            body = content[end+3:].strip()
            return body
        except:
            return content
    return content

def count_words(content: str) -> int:
    """Cuenta las palabras en el contenido"""
    body = extract_body_content(content)
    # Limpiar markdown básico para conteo más preciso
    # Remover código, bloques de quote para el conteo
    body = re.sub(r'```[\s\S]*?```', '', body)  # Bloques de código
    body = re.sub(r'`[^`]+`', '', body)  # Código inline
    body = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', body)  # Links
    body = re.sub(r'[#*_\-]', ' ', body)  # Caracteres markdown
    
    # Contar palabras
    words = body.split()
    return len(words)

def update_frontmatter(content: str, word_count: int) -> str:
    """Actualiza modified y wordCount en el frontmatter"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Actualizar modified
    content = re.sub(
        r'^(modified:\s*)"?[^"\n]+"?',
        lambda m: f'{m.group(1)}"{today}"',
        content,
        flags=re.MULTILINE
    )
    
    # Actualizar wordCount
    content = re.sub(
        r'^(wordCount:\s*)[^\n]+',
        lambda m: f'{m.group(1)}{word_count}',
        content,
        flags=re.MULTILINE
    )
    
    return content

def process_file(filepath: Path) -> bool:
    """Procesa un archivo y retorna True si hubo cambios"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        normalized = normalize_thoughts(original)
        
        # Siempre actualizar metadata (modified y wordCount)
        word_count = count_words(normalized)
        updated = update_frontmatter(normalized, word_count)
        
        if original != updated:
            # Crear carpeta de backups si no existe
            backups_dir = filepath.parent.parent / 'backups'
            backups_dir.mkdir(exist_ok=True)
            
            # Crear backup en carpeta separada
            backup = backups_dir / (filepath.name + '.bak')
            with open(backup, 'w', encoding='utf-8') as f:
                f.write(original)
            
            # Escribir actualizado
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            
            print(f"✓ Actualizado: {filepath} ({word_count} palabras)")
            return True
        else:
            print(f"✓ Sin cambios: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error en {filepath}: {e}")
        return False

def main():
    capitulos_dir = Path(__file__).parent.parent / 'capitulos'
    
    if not capitulos_dir.exists():
        print(f"Error: No se encuentra directorio {capitulos_dir}")
        sys.exit(1)
    
    print("=" * 50)
    print("Normalizando y actualizando metadatos...")
    print("=" * 50)
    
    changed = 0
    total = 0
    
    # Buscar recursivamente en subcarpetas
    for md_file in sorted(capitulos_dir.rglob('*.md')):
        total += 1
        if process_file(md_file):
            changed += 1
    
    print("=" * 50)
    print(f"Total archivos: {total}")
    print(f"Archivos modificados: {changed}")
    print("Backups creados con extensión .bak")
    print("=" * 50)

if __name__ == '__main__':
    main()
