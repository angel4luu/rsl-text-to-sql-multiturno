# Reglas de la matriz de decisión (Fase 14, paso 3)

Se puntúan quince candidatos —OE1–OE5 (paso 1), DA–DG (paso 2) y las tres combinaciones DA+DC, DB+DD y DE+DF+DG— en
cinco criterios con escala ordinal de 0 a 3 (más alto = más favorable). Las puntuaciones de evidencia se calculan con
`analysis/src/tesis/matriz_decision.py` a partir de `datos/mapa_oe_indicadores.csv`, `datos/mapa_oe_contrastes.csv` y
`datos/mapa_direcciones_indicadores.csv`; todos los porcentajes se refieren a la población principal (72 estudios
multiturno que superan el umbral de validez). La matriz no designa un ganador: ordena bajo cuatro ponderaciones, informa
el intervalo de rangos y la dominancia de Pareto, y muestra el efecto de cada entrada de juicio
(`datos/matriz_alternativas.csv`). La relevancia local se excluye porque la autora la declaró no determinante
(`restricciones_autora.md`).

## Tipos de candidato

- **Técnica:** propone un mecanismo cuyo beneficio puede contrastarse (OE1–OE4, DA).
- **Evaluación:** propone medir, construir datos o comparar (OE5, DB–DG). Su resultado es informativo aunque no haya mejora.

## C1 — Evidencia del problema

Se usa el indicador del problema específico del candidato y se aplica la regla según su clase:

| Clase de indicador | 3 | 2 | 1 |
|---|---|---|---|
| Déficit (fallo o coste reportado) | ≥ 33,3 % de los estudios | 10–33,3 % | < 10 % |
| Brecha de reporte (estudios que *no* reportan algo que afecta la validez; sin consecuencia medida) | — | ≥ 50 % | < 50 % |
| Brecha de cobertura (tema poco estudiado; no es un problema por sí mismo) | — | — | siempre |

Sin indicador: 1 si el problema es inherente a la tarea pero no se midió en la extracción; 0 si no hay indicador ni
argumento cualitativo. Con varios indicadores se toma el máximo. «Poco estudiado» nunca supera 1.

## C2 — Evidencia de beneficio potencial

Se usan solo los contrastes dentro del estudio del paso 1 (clase correspondiente al candidato). No se usa la magnitud de
la mediana, porque mezcla *benchmarks*, métricas y modelos.

| Puntuación | Regla |
|---|---|
| 3 | ≥ 5 estudios, ≥ 80 % de estudios con dirección positiva, confianza alta y la clase coincide con el componente central (alcance exacto) |
| 2 | ≥ 3 estudios, mayoría positiva y confianza alta o moderada (o cumple 3, pero la clase es más amplia que el componente) |
| 1 | Hay contrastes, pero no se alcanzan las condiciones anteriores |
| 0 | Sin contrastes |

Los candidatos de evaluación sin clase de contraste reciben 0 en los escenarios E0–E2; en E3 el criterio se trata como
no aplicable y se renormalizan los pesos.

## C3 — Novedad

Inversa de la cobertura del componente central del candidato en la población principal: 3 si < 5 %; 2 si 5–15 %;
1 si 15–30 %; 0 si ≥ 30 %.

## C4 — Factibilidad

Parte de 3 y resta 1 por cada requisito presente; mínimo 0. Un requisito inviable sin sustituto (GPU para
entrenamiento, usuarios reales o datos empresariales sin alternativa pública) fija 0. Requisitos: `SUSTITUTO` (simular
usuarios o sustituir datos empresariales por datos públicos), `ANOTACION` (construir o anotar datos),
`MULTICOMPONENTE` (varios componentes nuevos que interactúan), `COSTE_API_ALTO` (muchas llamadas por turno o
contextos largos) e `INFO_NO_OBSERVABLE` (depende de información no observable, como los datos de entrenamiento de
modelos cerrados). Restricciones de partida: sin GPU, acceso por API, sin usuarios reales ni datos empresariales, tesis
de pregrado con implementación desde noviembre de 2026.

## C5 — Riesgo de resultado nulo (3 = riesgo bajo)

- Evaluación: 3 (una medición o comparación es informativa en cualquier dirección).
- Técnica: 2 si alguna clase tiene ≥ 5 estudios con ≥ 80 % positivos; 1 si hay contrastes que no cumplen esa
  condición; 0 sin contrastes.

## Combinaciones

C1 y C2 = media de los componentes (en E3, la media de C2 solo considera los componentes en los que aplica);
C3 = máximo; C4 y C5 = mínimo, porque todos los componentes deben ser factibles.

## Escenarios de ponderación

| Escenario | C1 | C2 | C3 | C4 | C5 | Nota |
|---|---|---|---|---|---|---|
| E0 — pesos iguales (base) | 1 | 1 | 1 | 1 | 1 | |
| E1 — prioridad a factibilidad | 1 | 1 | 1 | 2 | 2 | |
| E2 — prioridad a evidencia | 2 | 2 | 1 | 1 | 1 | |
| E3 — pesos iguales, C2 no aplicable a evaluación | 1 | 1 | 1 | 1 | 1 | sin C2 para evaluación sin contrastes |

Puntuación total = suma ponderada / máximo posible × 100. Los empates comparten el mejor rango. Un candidato está
dominado si otro es igual o mejor en los cinco criterios y estrictamente mejor en al menos uno.
