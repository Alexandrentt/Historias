# Makefile para compilar Los Josth a PDF
# Uso: make pdf

BOOK_NAME = Los_Josth
CAPITULOS_DIR = capitulos
TEMPLATE_DIR = pdf_template
SCRIPTS_DIR = scripts
ILUSTRACIONES_DIR = ilustraciones
BACKUPS_DIR = backups

.PHONY: all pdf clean normalize help install_deps ilustraciones

all: pdf

help:
	@echo "Comandos disponibles:"
	@echo "  make normalize    - Normaliza formato de pensamientos en todos los capítulos"
	@echo "  make pdf          - Compila el libro completo a PDF"
	@echo "  make clean        - Elimina archivos temporales, PDF y backups"
	@echo "  make ilustraciones - Crea carpeta de ilustraciones si no existe"
	@echo "  make install_deps  - Instala dependencias necesarias (Ubuntu/Debian)"

normalize:
	@echo "Normalizando pensamientos..."
	@python3 $(SCRIPTS_DIR)/normalizar_pensamientos.py

ilustraciones:
	@mkdir -p $(ILUSTRACIONES_DIR)
	@echo "Carpeta de ilustraciones creada: $(ILUSTRACIONES_DIR)/"
	@echo "Formato de archivos: cap01_001.png, cap01_002.png, etc."

pdf: normalize
	@echo "Compilando PDF..."
	@python3 $(SCRIPTS_DIR)/compile_pdf.py $(BOOK_NAME).pdf

clean:
	@echo "Limpiando archivos temporales..."
	@rm -f $(BOOK_NAME).pdf
	@rm -rf $(BACKUPS_DIR)
	@rm -f *.aux *.log *.out *.toc *.lof *.lot
	@find . -name "*.tmp" -delete

install_deps:
	@echo "Instalando dependencias..."
	sudo apt-get update
	sudo apt-get install -y pandoc texlive-latex-base texlive-fonts-recommended \
		texlive-latex-extra texlive-xetex texlive-lang-spanish

# Compilar un solo capítulo (para pruebas)
# Uso: make cap CAP=01
cap:
	@if [ -z "$(CAP)" ]; then \
		echo "Uso: make cap CAP=01"; \
		exit 1; \
	fi
	pandoc $(CAPITULOS_DIR)/$(CAP).md -o capitulo_$(CAP).pdf \
		--pdf-engine=pdflatex --variable documentclass=article \
		--variable papersize=a5 --variable fontsize=11pt
