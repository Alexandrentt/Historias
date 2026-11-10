# Auditoría de congruencia documental — La Transtierra / Yen

**Primera revisión:** 13 de octubre de 2026  
**Actualización de sincronización:** 9 de noviembre de 2026  
**Repositorio revisado:** `Alexandrentt/Historias`, rama predeterminada consultada durante la auditoría.  
**Propósito:** registrar contradicciones documentales y mantener el estado de su resolución. La primera auditoría fue diagnóstica; la actualización de noviembre registra cambios ya aplicados en canon, fichas y documentos de estructura.  
**Jerarquía aplicada:** `notas-temas/Canon.md` prevalece sobre biblias, fichas y arcos, tal como declara el propio documento. Esta auditoría distingue contradicciones textuales, ambigüedades narrativas y decisiones que siguen abiertas.

## Resumen ejecutivo

La documentación tiene una arquitectura útil, pero el canon no está propagado de forma fiable. Los problemas más graves no son de estilo: afectan la fecha de acontecimientos centrales, la duración de la relación Yen–Rish, la cronología del prólogo, la regla de la vox y el desenlace. Hay, además, alternativas de borrador mezcladas con hechos supuestamente fijados.

La auditoría inicial no modificó archivos. Desde entonces se aplicó una ronda de sincronización documental; el estado actualizado de cada hallazgo aparece al final. Las decisiones pendientes siguen sin convertirse en canon por inferencia.

## Hallazgos prioritarios

### A-01 — Muerte de Herday: 589 o 590 DT
**Severidad:** crítica · **Tipo:** contradicción explícita

`notas-temas/Canon.md`, `notas-temas/Linea-Temporal.md`, `tramas/Lista-40.md`, `tramas/Arco-Novata.md` y el capítulo 7 sitúan la muerte de Herday en 589 DT. Sin embargo, `personajes/Yen.md` la fecha en 590 DT; `tramas/Esquema-6-Volumenes.md` también conserva una referencia a 590 en su tabla final, y `Linea-Temporal.md` contiene una tabla de edades que dice que Herday muere en 590.

**Resolución recomendada:** fijar 589 DT, que es la decisión más consistente con el canon y el cierre del volumen 1. Corregir todas las menciones restantes, incluidas tablas, resúmenes y biblias largas.

### A-02 — Muerte de Rish: 597, 598 o una edad posterior a su muerte
**Severidad:** crítica · **Tipo:** contradicción explícita

El canon fija el estrangulamiento de Rish en la isla, en 597 DT. `Lista-40.md` también dice 597. Pero `personajes/Rish.md` mantiene el intervalo de la isla como 597–598 DT y describe la relación hasta 598. `notas-temas/Linea-Temporal.md` incluye «40 (muere en 598)» en la tabla de edades, aunque en la misma cronología Rish ya muere en 597.

**Resolución recomendada:** fijar la muerte en 597 DT. Rish no debe tener una edad viva asignada en 599 ni figurar como fallecido en 598 en ninguna tabla biográfica. Revisar asimismo las edades que se calculan desde 589.

### A-03 — La relación Yen–Rish no puede durar cinco años exactos con las fechas actuales
**Severidad:** crítica · **Tipo:** contradicción aritmética/narrativa

`Canon.md`, `personajes/Rish.md` y `notas-temas/La-Playa.md` sitúan el inicio de la relación en 593 DT. La muerte de Rish está fijada en 597 DT, pero su ficha repite «cinco años exactos: 593–598» y la describe como estable entre 594–596.

**Resolución recomendada:** conservar las fechas canónicas de la playa y la isla y eliminar «cinco años exactos». Describir la relación como una relación de aproximadamente cuatro años, o precisar meses/fechas dentro del calendario si se necesita una duración exacta. No mover la muerte a 598 solo para sostener una frase de la ficha.

### A-04 — El prólogo no está sincronizado con el canon temporal
**Severidad:** crítica · **Tipo:** contradicción explícita

`Canon.md` fija el prólogo y la caída en el mismo día de 599 DT, y fija un intervalo de año y medio entre la isla y la caída. Sin embargo, `capitulos/00 prologo.md` aún dice «meses atrás» al recordar el primer intento de suicidio. También contiene referencias temporales que pueden sugerir que el tramo isla–caída es menor o indeterminado.

**Resolución recomendada:** revisar todas las expresiones temporales del prólogo contra el calendario maestro. No basta con sustituir una frase: hay que diferenciar el primer intento, la isla, el regreso a Návar y la noche de la caída.

### A-05 — La vox de Yen: regla de intimidad frente al prólogo
**Severidad:** alta · **Tipo:** contradicción entre regla y escena

`Canon.md` establece que Yen solo se quita la vox en su cubículo vital y en la playa, que es una bolsa atmosférica compatible. En `capitulos/00 prologo.md`, Yen se desprende de la vox en la azotea y la deja caer. Aunque no haya otra persona presente, el lugar no aparece establecido como excepción atmosférica y contradice la regla literal de los únicos lugares donde se la quita.

La escena también dice que Yen respira una atmósfera a una presión que su especie no puede soportar. Esto puede ser deliberado como acto final, pero debe quedar claro si la vox se quita antes de la caída, durante ella o en un instante de desesperación; ahora la mecánica física y la regla de la vox no están reconciliadas.

**Resolución recomendada:** decidir explícitamente si la azotea constituye una tercera excepción o si el gesto debe cambiar. La solución no debería violar accidentalmente una característica tan importante del personaje.

### A-06 — ¿Yen salta, se resbala o cambia de decisión durante la caída?
**Severidad:** alta · **Tipo:** ambigüedad de desenlace

`Canon.md` y `Arco-Depresion-y-Final.md` fijan arrepentimiento a mitad de caída y caída accidental: Yen se resbala y cae, no consigue consumar un suicidio deliberado. El prólogo, en cambio, presenta el abismo como una llamada, la sitúa al borde y narra que deja de sentir el borde antes de que empiece el terror; la acción física no deja inequívoco si salta voluntariamente o resbala.

**Resolución recomendada:** conservar el arrepentimiento a mitad de caída, pero hacer legible la secuencia física: Yen llega al borde con intención suicida, decide no hacerlo o vacila, pierde el apoyo y cae. La narración puede mantener la incertidumbre emocional, no la mecánica del accidente.

### A-07 — La regla del Espectro no coincide aún con la cronología de la escena
**Severidad:** alta · **Tipo:** regla metafísica por precisar

`Regla-de-Narracion.md` y `Canon.md` dicen que el Espectro/Dhë habla con cada alma una vez, al morir, y que toda la novela es esa conversación con Yen. El prólogo empieza mientras Yen sigue cayendo y su cuerpo aún no ha impactado. El texto dice que su conciencia se desprende y que su Saol flota en el umbral de la existencia, pero no fija claramente cuándo se considera muerta ni cómo se relaciona la visión con la desintegración posterior en el Portal.

**Resolución recomendada:** fijar una regla breve y uniforme: cuándo empieza la conversación, qué significa «al morir» en este caso y si el cuerpo continúa cayendo mientras la conciencia entra en el Saol. Esto debe quedar igual en canon, cosmología y prólogo.

### A-08 — La rebelión, la demolición de la Central y la caída requieren una secuencia única
**Severidad:** alta · **Tipo:** causalidad/cronología insuficientemente especificada

`Esquema-6-Volumenes.md` y `Arco-Depresion-y-Final.md` sitúan la rebelión de Lena y Zhan, la toma temporal de la Central, la contrarrevolución y la demolición inminente del edificio en 599 DT. Yen, que ha permanecido aislada en Návar, regresa a Amitia y sube a la Central esa misma noche. Los documentos no fijan con suficiente precisión quién controla el edificio en ese momento, si la demolición está anunciada o en curso, cómo llega Yen a la torre y en qué orden ocurren la toma, la derrota rebelde, la ejecución de Lena y la caída.

**Resolución recomendada:** crear una cronología de acontecimientos dentro de 599 DT con orden relativo, lugar y conocimiento de cada personaje. La fecha anual por sí sola no resuelve el problema.

### A-09 — El capítulo 1 ya corrigió el origen del nombre «Yen», pero la biblia conserva la versión anterior
**Severidad:** media · **Tipo:** canon no propagado

`Canon.md` dice que Lena le pone el nombre «Yen» y señala expresamente que el capítulo 1 debe corregirse porque antes Yen pedía que la llamaran así. El capítulo actual `capitulos/La novata/01.md` sí contiene a Lena proponiendo «¿Puedo llamarte Yen?». La biblia larga `Biblia-de-la-serie-Yen.md` conserva material antiguo y necesita verificarse antes de usarla como referencia.

**Resolución recomendada:** actualizar la biblia para que refleje la escena vigente, y retirar la instrucción de corrección pendiente si ya se cumplió. Este caso muestra por qué las listas de tareas no deben quedarse desactualizadas.

### A-10 — «Tali hermana o cuñada» sigue apareciendo en una propuesta pese a estar fijado
**Severidad:** media · **Tipo:** borrador obsoleto

`Canon.md` fija a Tali como hermana mayor de Yen. `tramas/Arco-Navar.md` todavía dice que no está definido si Tali es hermana o cuñada. El documento mezcla planificación útil con una alternativa que ya no está abierta.

**Resolución recomendada:** eliminar la alternativa y conservar únicamente los aspectos de Tali que realmente sigan pendientes.

### A-11 — La regla del narrador está decidida, pero su aplicación sigue pendiente
**Severidad:** alta · **Tipo:** inconsistencia entre política editorial y estado real

`Regla-de-Narracion.md` exige una o dos intervenciones del Espectro por capítulo y reconoce que falta marcar su presencia en los capítulos existentes. `Plan-Editorial.md`, sin embargo, da por decidida la regla y marca su aplicación como tarea incompleta. Esto no prueba que todos los capítulos incumplan, pero sí confirma que no hay verificación sistemática.

**Resolución recomendada:** auditar prólogo y capítulos 1–7 línea por línea antes de extender el método al resto de volúmenes. No insertar frases mecánicamente: cada intervención debe aportar perspectiva, presagio o una evaluación coherente con la voz del Espectro.

### A-12 — La versión de la muerte de Bastean necesita una formulación canónica estable
**Severidad:** alta · **Tipo:** contradicción interna de la ficción que debe ser intencional

`Arco-Bastean.md`, `Lista-40.md`, `Esquema-6-Volumenes.md` y la biblia presentan la muerte de Bastean como un suicidio imposible: tres disparos por la espalda, con la evidencia destruida y una versión oficial que lo hace pasar por un caso cerrado. Es una buena señal de corrupción institucional, pero algunos documentos lo describen como «suicidio (3 disparos)» y otros como «muere en custodia», sin separar claramente la versión oficial de la verdad narrativa.

**Resolución recomendada:** en cada documento, distinguir explícitamente «versión oficial» de «lo que realmente ocurrió». No normalizarlo como un suicidio real si la imposibilidad de esa versión es deliberada.

### A-13 — El material del mundo contiene una versión extensa y resúmenes que pueden divergir
**Severidad:** media · **Tipo:** riesgo de sincronización

El repositorio conserva `Transtierra.md`, `tierras/mundo.md`, `tierras/Transtierra(resumen).md`, `Biblia-de-la-serie-Yen.md`, PDFs exportados y documentos de planificación. `Canon.md` fija siete Tierras, con Amitia como Tierra 1, Derat como Tierra 5 y Návar como Tierra 6. Los resúmenes y las versiones largas deben contrastarse con esa tabla, especialmente en menciones históricas y en el número de Tierras.

**Resolución recomendada:** tratar los PDF como exportaciones, no como fuentes de autoridad; revisar los documentos Markdown vivos y regenerar los PDF al final. No se debe declarar que todo el material está alineado hasta completar esa comparación.

### A-14 — El estado final de Zhan continúa deliberadamente abierto, pero se presenta de dos formas
**Severidad:** media · **Tipo:** decisión narrativa pendiente

`personajes/Zhan.md` pregunta si vive o muere en la rebelión. `Arco-Depresion-y-Final.md` dice que es ejecutado como traidor, mientras que `Esquema-6-Volumenes.md` conserva «ejecutado (o destino incierto)» y otras tablas indican «ejecutado (o destino incierto)». Esto no es una contradicción resuelta por el canon actual: es una decisión abierta mezclada con una versión afirmativa.

**Resolución recomendada:** mantenerlo marcado como pendiente hasta decidirlo. Si se fija la ejecución, propagarla; si sigue abierto, no redactar la muerte como hecho consumado en la sinopsis principal.

## Riesgos de estructura documental

### Canon y tareas editoriales desincronizadas
`Plan-Editorial.md` conserva tareas ya completadas como si todavía hubiera que corregirlas, junto a tareas pendientes. Esto hace difícil saber qué queda por hacer y fomenta cambios duplicados.

### Biblias antiguas y copias exportadas
La biblia larga, los PDFs de la raíz y el material bajo `Los Josth` no deben tratarse como igualmente autoritativos. Las exportaciones deberían regenerarse solo después de cerrar una ronda de cambios.

### Propuestas sin estado
Los arcos incluyen formulaciones como «puede ser», «o», «lo que falta» y alternativas de parentesco o destino. Son útiles durante el diseño, pero deben llevar una etiqueta visible de **PROPUESTA**, **PENDIENTE** o **DESCARTADO** cuando conviven con hechos fijados.

## Orden recomendado de corrección

**Primero:** fechas y edades (Herday, Rish, relación Yen–Rish, 589–599).  
**Segundo:** prólogo, vox, caída y reglas del Espectro.  
**Tercero:** secuencia política del volumen 6 y destino de Zhan.  
**Cuarto:** propagación de nombres, parentescos, Tierras y versiones oficiales.  
**Quinto:** revisión de la voz narrativa en los capítulos y actualización de las biblias.  
**Sexto:** regeneración de PDF y limpieza del plan editorial.

## Alcance y limitaciones de esta pasada

Se inspeccionaron el canon, la línea temporal, las reglas narrativas, las fichas de Yen/Rish/Herday/Zhan, el índice, los seis volúmenes, arcos seleccionados, la lista de responsables, los capítulos iniciales y los resúmenes de worldbuilding; además se buscaron referencias cruzadas en el repositorio. Esta es una auditoría documental de primera pasada, no una validación exhaustiva de cada párrafo de los documentos de cientos de miles de caracteres ni de cada PDF exportado.

**Estado:** informe creado; archivos existentes sin modificar. Las decisiones marcadas como propuestas no se consideran canon hasta que se aplique la ronda de sincronización.


---

## Actualización de estado — 9 de noviembre de 2026

Esta sección prevalece sobre el estado histórico de las recomendaciones anteriores. Se sincronizaron el canon maestro, las fichas de personaje, la línea temporal, la wiki, los arcos y la sinopsis de seis volúmenes.

| Hallazgo | Estado actual | Aplicación |
|---|---|---|
| A-01 — Muerte de Herday | **Resuelto** | Fijada en 589 DT, al cierre del volumen 1; corregidas ficha, canon y sinopsis. |
| A-02 — Muerte de Rish | **Resuelto** | Fijada en 597 DT; eliminada su edad posterior a la muerte. |
| A-03 — Duración Yen–Rish | **Resuelto** | Relación 593–597 DT; ya no se afirma «cinco años exactos». |
| A-04 — Prólogo y referencias temporales | **Parcial** | Canon y línea temporal fijan el tramo isla–caída en aproximadamente año y medio. Falta una auditoría línea por línea del prólogo y las cartas. |
| A-05 — Vox | **Resuelto en documentación maestra** | No traduce automáticamente en 589–599; Yen conserva la Vox en la playa y se la quita solo en las excepciones fijadas. La azotea es una excepción deliberada. |
| A-06 — Caída de Yen | **Resuelto en documentación maestra** | Se fija la secuencia: intención, cambio de decisión, intento de retroceder, resbalón y caída. Falta comprobar que el capítulo lo exprese con claridad física. |
| A-07 — Momento de intervención del Espectro | **Pendiente** | Falta precisar cómo se articula el diálogo con el instante de muerte y el impacto, y propagarlo a la escena. |
| A-08 — Secuencia política de 599 DT | **Parcial** | Se fijan el gobierno 599–605 y la ejecución posterior de Lena. El orden exacto de toma de la Central, control del edificio, demolición y regreso de Yen sigue pendiente. |
| A-09 — Origen del apodo Yen | **Resuelto** | Lena propone el apodo; la ficha de Yen y el canon ya lo reflejan. |
| A-10 — Parentesco de Tali | **Resuelto** | Tali es hermana mayor; Varrily es tía. |
| A-11 — Presencia del Espectro por capítulo | **Pendiente** | Requiere auditoría de capítulos y no se resuelve con esta sincronización de fichas. |
| A-12 — Muerte de Bastean | **Resuelto en formulación documental** | Se distingue muerte bajo custodia, versión oficial y referencia sospechosa a tres disparos. No se afirma un suicidio comprobado. |
| A-13 — Worldbuilding heredado | **Parcial** | Canon y Ensayo-Worldbuilding fijan siete Tierras y eliminan anexos. La Biblia antigua y el ensayo histórico se marcan como documentos de archivo o borradores cuando conservan alternativas. Falta una pasada exhaustiva por todos los materiales derivados y capítulos. |
| A-14 — Destino de Zhan | **Pendiente, explícito** | Se conserva como decisión abierta. No afirmar su ejecución como hecho. |

### Criterio para la siguiente pasada

No conviene seguir corrigiendo frases aisladas sin una secuencia de verificación. La próxima revisión debe cotejar el prólogo y los capítulos con las fechas ancla, después revisar las menciones residuales de Tierras descartadas y, por último, comprobar la presencia del Espectro y regenerar los materiales exportados. El destino de Zhan, el momento exacto de la visión y el orden político de 599 no deben cerrarse sin una decisión narrativa expresa.
