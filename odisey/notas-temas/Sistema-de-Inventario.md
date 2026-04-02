---
tags: [tema, sistema, inventario, rpg, supervivencia]
---

# Sistema de Inventario - Odisea

## 🎮 Concepto RPG

### **Inspiración Fallout**
- **Gestión de recursos**: Cada objeto cuenta
- **Peso y espacio**: Limitaciones realistas
- **Estado de objetos**: Desgaste y reparación
- **Valor de trueque**: Sistema económico basado en objetos

### **Propósito Narrativo**
- **Precariedad visible**: El inventario muestra su situación
- **Decisiones estratégicas**: Qué llevar, qué dejar atrás
- **Misiones secundarias**: Necesidades específicas generan quests
- **Progresión**: Mejora de equipo through exploración

---

## 📋 Sistema de Inventario

### **Categorías Principales**

#### **Armas y Combate**
- **Armas cuerpo a cuerpo**: Cuchillos, palos, herramientas improvisadas
- **Armas de fuego**: Pistolas, rifles (munición limitada)
- **Proyectiles**: Flechas, lanzamientos (recuperables o no)
- **Protección**: Ropa resistente, armaduras improvisadas

#### **Supervivencia**
- **Agua y comida**: Botellas, raciones, carne seca
- **Medicina**: Básicos, antibióticos, vendas
- **Herramientas**: Cuerdas, mecheros, kits de reparación
- **Refugio**: Tiendas, mantas, material de construcción

#### **Exploración**
- **Iluminación**: Linternas, antorchas, baterías
- **Navegación**: Mapas, brújulas, GPS (si funciona)
- **Equipamiento**: Mochilas, contenedores, cuerdas

#### **Objetos Especiales**
- **Tecnología del Régimen**: Artefactos valiosos
- **Historia**: Libros, documentos, grabaciones
- **Llaves y acceso**: Tarjetas, códigos, llaves físicas

---

## 🎯 Inventario Inicial

### **Jay Cowler**
```yaml
armas:
  - cuchillo_caza: 1
  - palo_madera: 1
supervivencia:
  - botella_agua: 1 (3/4 lleno)
  - carne_seca: 3 raciones
  - venda_reutilizable: 1
herramientas:
  - mechero: 1 (medio combustible)
  - cuerda_3m: 1
equipamiento:
  - mochila_tela: 1
  - botas_gastadas: 1
```

### **Emma Cowler**
```yaml
armas:
  - cuchillo_bolsillo: 1
supervivencia:
  - botella_agua: 1 (1/2 lleno)
  - hierbas_medicinales: 1 manojo
  - vendas_limpías: 3
herramientas:
  - navaja_multiusos: 1
  - kit_reparacion_basico: 1
equipamiento:
  - mochila_cuero: 1
  - botas_resistentes: 1
objetos_especiales:
  - libro_historia: 1 ("Archivo de recuperación...")
```

### **Noah**
```yaml
armas:
  - pistola_vieja: 1
  - municion: 6 balas
supervivencia:
  - botella_agua: 1 (lleno)
  - raciones_enlatadas: 2
herramientas:
  - linterna_manual: 1
  - mapa_zona: 1 (parcial)
equipamiento:
  - mochila_militar: 1
  - botas_militares: 1
```

---

## 📊 Mecánicas del Sistema

### **Limitaciones**
- **Espacio**: Mochilas con capacidad limitada
- **Peso**: Afecta movilidad y resistencia
- **Durabilidad**: Armas y herramientas se desgastan
- **Consumo**: Comida y agua disminuyen con el tiempo

### **Trueque y Comercio**
- **Valor relativo**: Los objetos tienen diferente valor según el lugar
- **Necesidades específicas**: Cada vendedor busca ciertos items
- **Negociación**: Habilidad de Emma para mejores tratos
- **Escasez**: Algunos objetos son muy raros y valiosos

### **Misiones Secundarias por Inventario**

#### **Necesidades Básicas**
- **"Busca agua limpia"**: Manantial contaminado, necesitas filtros
- **"Medicina para Samuel"**: Enfermo en Mountain Home, requiere hierbas específicas
- **"Repara el generador"**: Piezas mecánicas necesarias para electricidad

#### **Mejora de Equipo**
- **"Mejora tu arma"**: Busca materiales para afilar/reparar
- **"Mejor refugio"**: Materiales de construcción para fortificar
- **"Armadura del Régimen"**: Peligrosa misión para conseguir equipo militar

#### **Objetos Especiales**
- **"Libros perdidos"**: Recupera conocimiento de la guerra
- **"Tecnología antigua"**: Artefactos pre-guerra con valor
- **"Comunicación con otras ciudades"**: Establece red de información

---

## 🔄 Evolución del Sistema

### **Progresión Natural**
- **Mejora de equipo**: Encontrar mejores versiones de objetos existentes
- **Nuevos tipos**: Desbloquear categorías (tecnología, armas avanzadas)
- **Habilidades**: Jay (combate), Emma (diplomacia), Noah (exploración)

### **Integración con la Trama**
- **Objetos de misión**: Items necesarios para avanzar la historia principal
- **Recompensas**: Equipo especial por completar misiones
- **Consecuencias**: Perder objetos en combate o decisiones difíciles

### **Sistema Económico**
- **Mountain Home**: Sistema de trueque (sin dinero)
- **Ciudades del Régimen**: Tarjetas de racionamiento
- **Asentamientos rebeldes**: Economía basada en confianza

---

## 🎭 Impacto Narrativo

### **Toma de Decisiones**
- **¿Qué llevar?**: No puedes cargar todo
- **¿Qué sacrificar?**: Dejar objetos valiosos por necesidad
- **¿Qué arriesgar?**: Misiones peligrosas por recompensas

### **Caracterización**
- **Jay**: Pragmático, prioriza armas y supervivencia
- **Emma**: Estratégica, mantiene objetos de conocimiento
- **Noah**: Explorador, colecciona mapas y herramientas

### **Tensión Dramática**
- **Escasez constante**: Siempre necesitas algo más
- **Decisiones difíciles**: ¿Comida o medicina? ¿Armas o herramientas?
- **Pérdidas significativas**: Perder equipo puede ser devastador

---

## 🔗 Conexiones

- **[[Protagonistas]]** - Inventario individual de cada personaje
- **[[Mountain Home]]** - Sistema de trueque y economía local
- **[[El Régimen]]** - Tecnología y equipo militar
- **[[Misiones-Secundarias]]** - Quests generadas por necesidades
