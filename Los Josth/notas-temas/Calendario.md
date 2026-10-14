---
tags: [worldbuilding, calendario, cronologia, canon]
---

# Calendario oficial de la Transtierra

**Estado:** propuesta de normalización del calendario amitiano existente.  
**Autoridad:** este documento desarrolla las unidades ya fijadas en `Canon.md` y `tierras/mundo.md`; no modifica los años ni los acontecimientos de la cronología.

## Estructura del calendario

El calendario oficial amitiano es un calendario civil de **500 días por año**. Se conserva la estructura establecida en el worldbuilding y se resuelve la contradicción entre las semanas de diez días y los cinco nombres de días ya existentes.

| Unidad | Duración | Equivalencia |
|---|---:|---|
| Año | 500 días | 10 meses |
| Mes | 50 días | 10 semanas |
| Semana | 5 días | 5 días con nombre |
| Año | 100 semanas | 10 × 10 semanas |
| Estación | 125 días | 25 semanas |
| Estaciones | 4 | 500 días |

Los días de la semana se repiten de forma continua; no se reinician al comenzar un mes ni un año. Como los meses tienen 50 días y los años 500, ambos números son múltiplos de cinco: cada mes y cada año empiezan en el mismo día de la semana.

## Días de la semana

Los cinco nombres fijados son **Zira, Kato, Leif, Pazu y Miku**. Para que la fecha histórica ya establecida —**06 de Qyloz de 2015, día Kato**— sea matemáticamente posible, el orden cíclico se ancla así:

1. Kato
2. Leif
3. Pazu
4. Miku
5. Zira

Después de Zira vuelve Kato. Por tanto, los días 1 y 6 de cualquier mes comparten el mismo nombre de día. La lista tradicional de nombres se conserva; el orden anterior es el orden de avance del ciclo, no una jerarquía entre los nombres.

## Meses del año

| N.º | Mes | Días del mes | Semanas |
|---:|---|---|---:|
| 1 | Zinex | 01–50 | 10 |
| 2 | Ovryn | 01–50 | 10 |
| 3 | Jynex | 01–50 | 10 |
| 4 | Kylix | 01–50 | 10 |
| 5 | Leifx | 01–50 | 10 |
| 6 | Pazyn | 01–50 | 10 |
| 7 | Mikon | 01–50 | 10 |
| 8 | Syron | 01–50 | 10 |
| 9 | Qyloz | 01–50 | 10 |
| 10 | Vornx | 01–50 | 10 |

La fecha se escribe **día + mes + año DT**, y se puede añadir el día de la semana para dar precisión: `06 Qyloz 2015 DT, Kato`.

## Estaciones

Las estaciones son divisiones civiles del año; no implican que las siete Tierras compartan clima o ciclos agrícolas idénticos.

| Estación | Días del año | Semanas del año | Meses que abarca |
|---|---:|---:|---|
| Primera | 001–125 | 01–25 | Zinex, Ovryn y primeros 25 días de Jynex |
| Segunda | 126–250 | 26–50 | Últimos 25 días de Jynex, Kylix y Leifx |
| Tercera | 251–375 | 51–75 | Pazyn, Mikon y primeros 25 días de Syron |
| Cuarta | 376–500 | 76–100 | Últimos 25 días de Syron, Qyloz y Vornx |

Los nombres estacionales quedan descriptivos —Primera, Segunda, Tercera y Cuarta— hasta que el worldbuilding defina nombres culturales. Así no se inventan términos que quizá no pertenezcan a la cultura amitiana.

## Cómo fechar un acontecimiento

Para registrar un evento con precisión, se recomienda conservar cuatro campos:

- **Fecha civil:** `DD Mes AAAA DT`.
- **Día de la semana:** uno de los cinco nombres.
- **Semana del año:** `01–100`.
- **Día del año:** `001–500`.

Cálculos de referencia:

- Día del año = `50 × (número del mes − 1) + día del mes`.
- Semana del año = la semana de cinco días que contiene ese día del año.
- Día de la semana: avanzar un nombre por cada día transcurrido, respetando el ancla histórica.

Para la línea temporal, no se deben deducir meses o días concretos de frases como «en primavera» o «a mediados de año». Se asignan fechas exactas solo cuando el texto o la secuencia de acontecimientos permiten fijarlas; en los demás casos se registra un intervalo y se marca como pendiente.

## Fecha de referencia

El worldbuilding ya fija la aparición del Portal en **06 Qyloz 2015**, día **Kato**. Este calendario conserva esa fecha como ancla. Los años DT usados en la historia de Yen (589–599 DT) son el cómputo local de esa cronología y no deben confundirse con el año 2015 de la fecha de aparición del Portal en el calendario amitiano.

## Decisiones pendientes

- Confirmar si las estaciones tienen nombres propios en amitiano o si son categorías administrativas.
- No asignar fechas diarias a sucesos de la novela hasta revisar capítulos y documentos de arco.
- Si aparece un diario o documento con un día de semana incompatible, corregir el dato secundario; no cambiar la estructura del calendario para acomodar una fecha aislada.
