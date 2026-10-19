# Matriz de decisión

## Introducción

La matriz compara quince candidatos —OE1–OE5, DA–DG y las combinaciones DA+DC, DB+DD y DE+DF+DG— mediante cinco criterios ordinales puntuados de 0 a 3, donde un valor mayor es más favorable: evidencia del problema, evidencia de beneficio potencial, novedad, factibilidad y bajo riesgo de resultado nulo. <!-- reglas_matriz.md: candidatos; criterios; escala --> Se presentan cuatro ponderaciones: E0 asigna pesos iguales; E1 duplica factibilidad y riesgo de resultado nulo; E2 duplica evidencia del problema y del beneficio; y E3 mantiene pesos iguales, pero considera C2 no aplicable para candidatos de evaluación sin contrastes y renormaliza el total. <!-- reglas_matriz.md: Escenarios de ponderación --> La matriz ordena los candidatos bajo esos escenarios, informa sus rangos y la dominancia de Pareto, pero no declara un ganador.

## Matriz

| Candidato | Tipo | C1 | C2 | C3 | C4 | C5 | E0 | E1 | E2 | E3 | rangos (mín–máx) | dominado por |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| OE1 | tecnica | 1 | 2 | 1 | 3 | 2 | 60.0 | 66.7 | 57.1 | 60.0 | 3–10 | — | <!-- matriz_decision.csv: OE1 -->
| OE2 | tecnica | 3 | 2 | 2 | 2 | 2 | 73.3 | 71.4 | 76.2 | 73.3 | 1–8 | — | <!-- matriz_decision.csv: OE2 -->
| OE3 | tecnica | 2 | 0 | 3 | 3 | 0 | 53.3 | 52.4 | 47.6 | 53.3 | 12–15 | — | <!-- matriz_decision.csv: OE3 -->
| OE4 | tecnica | 1 | 2 | 2 | 2 | 2 | 60.0 | 61.9 | 57.1 | 60.0 | 3–11 | OE2 | <!-- matriz_decision.csv: OE4 -->
| OE5 | evaluacion | 3 | 0 | 1 | 2 | 3 | 60.0 | 66.7 | 57.1 | 75.0 | 3–6 | DC | <!-- matriz_decision.csv: OE5 -->
| DA | tecnica | 1 | 2 | 1 | 2 | 2 | 53.3 | 57.1 | 52.4 | 53.3 | 9–14 | OE1, OE2, OE4 | <!-- matriz_decision.csv: DA -->
| DB | evaluacion | 1 | 0 | 3 | 2 | 3 | 60.0 | 66.7 | 47.6 | 75.0 | 4–13 | DB+DD | <!-- matriz_decision.csv: DB -->
| DC | evaluacion | 3 | 0 | 1 | 3 | 3 | 66.7 | 76.2 | 61.9 | 83.3 | 1–2 | — | <!-- matriz_decision.csv: DC -->
| DD | evaluacion | 2 | 0 | 2 | 2 | 3 | 60.0 | 66.7 | 52.4 | 75.0 | 4–9 | — | <!-- matriz_decision.csv: DD -->
| DE | evaluacion | 0 | 3 | 0 | 3 | 3 | 60.0 | 71.4 | 57.1 | 60.0 | 2–10 | — | <!-- matriz_decision.csv: DE -->
| DF | evaluacion | 3 | 0 | 0 | 3 | 3 | 60.0 | 71.4 | 57.1 | 75.0 | 2–5 | DC | <!-- matriz_decision.csv: DF -->
| DG | evaluacion | 1 | 0 | 3 | 1 | 3 | 53.3 | 57.1 | 42.9 | 66.7 | 9–15 | DB, DB+DD, DE+DF+DG | <!-- matriz_decision.csv: DG -->
| DA+DC | combinacion | 2 | 1 | 1 | 2 | 2 | 53.3 | 57.1 | 52.4 | 60.0 | 9–12 | OE2 | <!-- matriz_decision.csv: DA+DC -->
| DB+DD | combinacion | 1.5 | 0 | 3 | 2 | 3 | 63.3 | 69.0 | 52.4 | 79.2 | 2–9 | — | <!-- matriz_decision.csv: DB+DD -->
| DE+DF+DG | combinacion | 1.33 | 1 | 3 | 1 | 3 | 62.2 | 63.5 | 55.5 | 75.5 | 3–10 | — | <!-- matriz_decision.csv: DE+DF+DG -->

## Justificación por candidato

### OE1 — Preprocesamiento lingüístico y restauración del contexto

- **C1:** Al no existir un indicador extraído y considerarse el problema inherente a la tarea, se aplica la regla cualitativa y se asigna 1. <!-- matriz_decision.json: candidatos/OE1/evidencia/C1; candidatos/OE1/p -->
- **C2:** La clase amplia de reescritura, reformulación o discurso reúne 11 estudios, 10 con dirección positiva y confianza alta, por lo que cumple la regla de mayoría positiva con al menos 3 estudios, pero no el alcance exacto exigido para 3, y recibe 2; los estudios son R00033 (Zhou2026RoseSQL), R00072 (Zhang2024CoESQL), R00074 (Liu2024TPLink), R00097 (Xiao2022CQRSQL), R00101 (Qi2022RASAT), R00107 (Chen2021Decoupled), R00222 (Jiang2025SiriusBI), R00868 (Fu2023MIGA), R00924 (Li2023DIR), R00927 (Ascoli2025Advancing) y R01034 (Liu2019FANDA). <!-- matriz_decision.json: candidatos/OE1/evidencia/C2; candidatos/OE1/p; mapa_oe_contrastes.csv: OE1/principal_nivel2_umbral/Reescritura / reformulación / discurso, estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** La reescritura de la pregunta alcanza una cobertura de 16,7 %, situada en el intervalo de 15–30 %, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/OE1/evidencia/C3; candidatos/OE1/p -->
- **C4:** No se registra ningún requisito de SUSTITUTO, ANOTACION, MULTICOMPONENTE, COSTE_API_ALTO o INFO_NO_OBSERVABLE, de modo que no se descuenta del valor inicial de 3 y se asigna 3. <!-- matriz_decision.json: candidatos/OE1/evidencia/C4; candidatos/OE1/p; penalizaciones -->
- **C5:** Los mismos contrastes reúnen al menos 5 estudios y al menos 80 % de direcciones positivas, así que la regla para candidatos técnicos asigna 2. <!-- matriz_decision.json: candidatos/OE1/evidencia/C2; candidatos/OE1/p -->

### OE2 — Grafo semántico de estado de dos capas

- **C1:** El coste de contexto que crece con los turnos es un déficit observado en 50,0 % de la población principal, valor igual o superior a 33,3 %, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/OE2/evidencia/C1; candidatos/OE2/p -->
- **C2:** La clase amplia de grafo, estado o memoria estructurada reúne 11 estudios, 10 con dirección positiva y confianza alta, por lo que cumple la regla de mayoría positiva con al menos 3 estudios, pero no el alcance exacto exigido para 3, y recibe 2; los estudios son R00033 (Zhou2026RoseSQL), R00096 (Cai2022STAR), R00099 (Hu2022InContext), R00117 (Cai2020IGSQL), R00435 (Tummalapenta2026Memory), R00438 (Wang2026Learning), R00480 (Teixeira2026SemPlan), R00499 (Yang2026GitHarness), R00936 (Yu2021Interactionmodeling), R00954 (Khadija2026Intelligent) y R01029 (Wang2021Tracking). <!-- matriz_decision.json: candidatos/OE2/evidencia/C2; candidatos/OE2/p; mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/Grafo / estado / memoria estructurada, estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** El grafo dinámico entre turnos alcanza una cobertura de 9,7 %, situada en el intervalo de 5–15 %, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE2/evidencia/C3; candidatos/OE2/p -->
- **C4:** Se parte de 3 y se descuenta el requisito MULTICOMPONENTE, es decir, implementar varios componentes nuevos que interactúan, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE2/evidencia/C4; candidatos/OE2/p; penalizaciones/MULTICOMPONENTE -->
- **C5:** Los mismos contrastes reúnen al menos 5 estudios y al menos 80 % de direcciones positivas, así que la regla para candidatos técnicos asigna 2. <!-- matriz_decision.json: candidatos/OE2/evidencia/C2; candidatos/OE2/p -->

### OE3 — Enrutamiento relacional simbólico

- **C1:** Los errores de *join* reportados constituyen un déficit observado en 13,9 % de la población principal, valor situado en el intervalo de 10–33,3 %, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE3/evidencia/C1; candidatos/OE3/p -->
- **C2:** La clase exacta de *joins*, claves foráneas o caminos no contiene estudios ni contrastes, por lo que se aplica la regla de ausencia de contrastes y se asigna 0. <!-- matriz_decision.json: candidatos/OE3/evidencia/C2; candidatos/OE3/p -->
- **C3:** Los *joins* por algoritmo de caminos alcanzan una cobertura de 1,4 %, inferior a 5 %, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/OE3/evidencia/C3; candidatos/OE3/p -->
- **C4:** No se registra ningún requisito de SUSTITUTO, ANOTACION, MULTICOMPONENTE, COSTE_API_ALTO o INFO_NO_OBSERVABLE, de modo que no se descuenta del valor inicial de 3 y se asigna 3. <!-- matriz_decision.json: candidatos/OE3/evidencia/C4; candidatos/OE3/p; penalizaciones -->
- **C5:** Al no existir contrastes para el candidato técnico, la regla de riesgo de resultado nulo asigna 0. <!-- matriz_decision.json: candidatos/OE3/evidencia/C2; candidatos/OE3/p -->

### OE4 — Verificación por ejecución y autocorrección

- **C1:** Al no existir un indicador extraído y considerarse el problema inherente a la tarea, se aplica la regla cualitativa y se asigna 1. <!-- matriz_decision.json: candidatos/OE4/evidencia/C1; candidatos/OE4/p -->
- **C2:** La clase amplia de autocorrección, ejecución o verificación reúne 10 estudios, todos con dirección positiva y confianza moderada, por lo que cumple la regla de al menos 3 estudios con mayoría positiva y confianza alta o moderada y recibe 2; los estudios son R00030 (Guo2026MTSQLR1), R00078 (Li2024MultiSQL), R00105 (Elgohary2021NLEDIT), R00123 (Elgohary2020Speak), R00312 (Sun2024QDASQL), R00373 (Huo2025BIRDINTERACT), R00374 (Lin2025Prompt), R00508 (Yang2026HarnessSQL), R00524 (Guo2025Evaluating) y R00526 (Almohaimeed2025Prompt). <!-- matriz_decision.json: candidatos/OE4/evidencia/C2; candidatos/OE4/p; mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Autocorrección / ejecución / verificación, estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** La retroalimentación de errores de ejecución alcanza una cobertura de 13,9 %, situada en el intervalo de 5–15 %, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE4/evidencia/C3; candidatos/OE4/p -->
- **C4:** Se parte de 3 y se descuenta el requisito COSTE_API_ALTO, correspondiente a muchas llamadas por turno o contextos largos, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE4/evidencia/C4; candidatos/OE4/p; penalizaciones/COSTE_API_ALTO -->
- **C5:** Los mismos contrastes reúnen al menos 5 estudios y al menos 80 % de direcciones positivas, así que la regla para candidatos técnicos asigna 2. <!-- matriz_decision.json: candidatos/OE4/evidencia/C2; candidatos/OE4/p -->

### OE5 — Evaluación multiturno y degradación por turno

- **C1:** La degradación por turno reportada es un déficit observado en 52,8 % de la población principal, valor igual o superior a 33,3 %, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/OE5/evidencia/C1; candidatos/OE5/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/OE5/evidencia/C2; candidatos/OE5/p; candidatos/OE5/c2_E3 -->
- **C3:** Los resultados desagregados por turno alcanzan una cobertura de 19,4 %, situada en el intervalo de 15–30 %, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/OE5/evidencia/C3; candidatos/OE5/p -->
- **C4:** Se parte de 3 y se descuenta el requisito SUSTITUTO, pues los esquemas empresariales deben reemplazarse por datos públicos, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/OE5/evidencia/C4; candidatos/OE5/p; penalizaciones/SUSTITUTO -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/OE5/p; reglas_matriz.md: C5 -->

### DA — Aclaración con el usuario e interacción, incluida la abstención

- **C1:** Al no existir un indicador extraído y considerarse el problema inherente a la tarea, se aplica la regla cualitativa y se asigna 1. <!-- matriz_decision.json: candidatos/DA/evidencia/C1; candidatos/DA/p -->
- **C2:** La clase exacta de aclaración o interacción con el usuario reúne 5 estudios, 4 con dirección positiva y confianza moderada, por lo que cumple la regla de al menos 3 estudios con mayoría positiva y confianza alta o moderada y recibe 2; los estudios son R00123 (Elgohary2020Speak), R00222 (Jiang2025SiriusBI), R00311 (Chen2024Learning), R00312 (Sun2024QDASQL) y R00480 (Teixeira2026SemPlan). <!-- matriz_decision.json: candidatos/DA/evidencia/C2; candidatos/DA/p; mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Aclaración / interacción con el usuario (alternativa), estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** El mecanismo de aclaración con el usuario alcanza una cobertura de 25,0 %, situada en el intervalo de 15–30 %, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/DA/evidencia/C3; candidatos/DA/p -->
- **C4:** Se parte de 3 y se descuenta el requisito SUSTITUTO, pues debe simularse a los usuarios ante la falta de participantes reales, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DA/evidencia/C4; candidatos/DA/p; penalizaciones/SUSTITUTO -->
- **C5:** Los mismos contrastes reúnen al menos 5 estudios y al menos 80 % de direcciones positivas, así que la regla para candidatos técnicos asigna 2. <!-- matriz_decision.json: candidatos/DA/evidencia/C2; candidatos/DA/p -->

### DB — Datos en español y multilingües

- **C1:** Los datos en español tienen una cobertura de 0,0 % en la población principal, pero una brecha de cobertura se puntúa siempre con 1 porque la escasez no constituye por sí sola evidencia del problema. <!-- matriz_decision.json: candidatos/DB/evidencia/C1; candidatos/DB/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/DB/evidencia/C2; candidatos/DB/p; candidatos/DB/c2_E3 -->
- **C3:** Los datos en español tienen una cobertura de 0,0 %, inferior a 5 %, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DB/evidencia/C3; candidatos/DB/p -->
- **C4:** Se parte de 3 y se descuenta el requisito ANOTACION, es decir, construir o anotar un conjunto de datos, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DB/evidencia/C4; candidatos/DB/p; penalizaciones/ANOTACION -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DB/p; reglas_matriz.md: C5 -->

### DC — Metodología de evaluación multiturno

- **C1:** Se toma el máximo entre la degradación por turno reportada, déficit de 52,8 % que puntúa 3, y la ausencia de resultados desagregados por turno, brecha de reporte de 80,6 % que puntúa 2, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DC/evidencia/C1; candidatos/DC/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/DC/evidencia/C2; candidatos/DC/p; candidatos/DC/c2_E3 -->
- **C3:** Los resultados desagregados por turno alcanzan una cobertura de 19,4 %, situada en el intervalo de 15–30 %, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/DC/evidencia/C3; candidatos/DC/p -->
- **C4:** No se registra ningún requisito de SUSTITUTO, ANOTACION, MULTICOMPONENTE, COSTE_API_ALTO o INFO_NO_OBSERVABLE, de modo que no se descuenta del valor inicial de 3 y se asigna 3. <!-- matriz_decision.json: candidatos/DC/evidencia/C4; candidatos/DC/p; penalizaciones -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DC/p; reglas_matriz.md: C5 -->

### DD — Contaminación de *benchmarks* y fecha de los modelos

- **C1:** Se toma el máximo de dos brechas de reporte: 90,3 % no discute contaminación y 80,6 % no informa la fecha o versión del modelo, ambas por encima de 50 % y ambas con puntuación 2, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DD/evidencia/C1; candidatos/DD/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/DD/evidencia/C2; candidatos/DD/p; candidatos/DD/c2_E3 -->
- **C3:** La contaminación discutida alcanza una cobertura de 9,7 %, situada en el intervalo de 5–15 %, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DD/evidencia/C3; candidatos/DD/p -->
- **C4:** Se parte de 3 y se descuenta el requisito INFO_NO_OBSERVABLE, pues se depende de información no observable como los datos de entrenamiento de modelos cerrados, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DD/evidencia/C4; candidatos/DD/p; penalizaciones/INFO_NO_OBSERVABLE -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DD/p; reglas_matriz.md: C5 -->

### DE — Líneas base simples fuertes

- **C1:** No hay indicador ni argumento cualitativo de que falten líneas base simples, por lo que se aplica la regla correspondiente y se asigna 0. <!-- matriz_decision.json: candidatos/DE/evidencia/C1; candidatos/DE/p -->
- **C2:** Se toma el máximo entre la clase exacta de SQL previo, edición o ventana, con 12 estudios, 11 positivos y confianza alta, que puntúa 3, y la clase exacta de concatenación o historial, con 3 estudios, todos positivos y confianza moderada, que puntúa 2, por lo que se asigna 3; la primera incluye R00072 (Zhang2024CoESQL), R00079 (Ryu2024EHRSeqSQL), R00093 (Zheng2022HIESQL), R00120 (Wang2020PGGSQL), R00126 (Yu2019SParC), R00131 (Zhang2019EditSQL), R00148 (Urban2025Utilizing), R00435 (Tummalapenta2026Memory), R00453 (Lian2026CoeusBI), R00499 (Yang2026GitHarness), R00508 (Yang2026HarnessSQL) y R00868 (Fu2023MIGA), y la segunda incluye R00078 (Li2024MultiSQL), R00079 (Ryu2024EHRSeqSQL) y R00927 (Ascoli2025Advancing). <!-- matriz_decision.json: candidatos/DE/evidencia/C2; candidatos/DE/p; mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa) y OE1/principal_nivel2_umbral/Concatenación / historial (alternativa), estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** La representación mediante historial plano alcanza una cobertura de 52,8 %, igual o superior a 30 %, por lo que se asigna 0. <!-- matriz_decision.json: candidatos/DE/evidencia/C3; candidatos/DE/p -->
- **C4:** No se registra ningún requisito de SUSTITUTO, ANOTACION, MULTICOMPONENTE, COSTE_API_ALTO o INFO_NO_OBSERVABLE, de modo que no se descuenta del valor inicial de 3 y se asigna 3. <!-- matriz_decision.json: candidatos/DE/evidencia/C4; candidatos/DE/p; penalizaciones -->
- **C5:** Aunque existen contrastes, por tratarse de un candidato de evaluación una comparación resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DE/evidencia/C2; candidatos/DE/p; reglas_matriz.md: C5 -->

### DF — Coste y eficiencia

- **C1:** Se toma el máximo entre el coste de contexto creciente, déficit de 50,0 % que puntúa 3, y la ausencia de reporte de costes, brecha de reporte de 62,5 % que puntúa 2, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DF/evidencia/C1; candidatos/DF/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/DF/evidencia/C2; candidatos/DF/p; candidatos/DF/c2_E3 -->
- **C3:** Para medir la cobertura del componente central se usa el complemento de 62,5 % sin reporte, es decir, 37,5 % con algún coste reportado, valor igual o superior a 30 %, por lo que se asigna 0. <!-- matriz_decision.json: candidatos/DF/evidencia/C3; candidatos/DF/p -->
- **C4:** No se registra ningún requisito de SUSTITUTO, ANOTACION, MULTICOMPONENTE, COSTE_API_ALTO o INFO_NO_OBSERVABLE, de modo que no se descuenta del valor inicial de 3 y se asigna 3. <!-- matriz_decision.json: candidatos/DF/evidencia/C4; candidatos/DF/p; penalizaciones -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DF/p; reglas_matriz.md: C5 -->

### DG — Esquemas grandes o empresariales

- **C1:** Los resultados en datos propios o industriales alcanzan una cobertura de 4,2 %, pero una brecha de cobertura se puntúa siempre con 1 porque la escasez no constituye por sí sola evidencia del problema. <!-- matriz_decision.json: candidatos/DG/evidencia/C1; candidatos/DG/p -->
- **C2:** Al ser un candidato de evaluación sin clase de contraste, se asigna 0 en E0–E2 y el criterio se considera no aplicable en E3. <!-- matriz_decision.json: candidatos/DG/evidencia/C2; candidatos/DG/p; candidatos/DG/c2_E3 -->
- **C3:** Los resultados en datos propios o industriales alcanzan una cobertura de 4,2 %, inferior a 5 %, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DG/evidencia/C3; candidatos/DG/p -->
- **C4:** Se parte de 3 y se descuentan SUSTITUTO, por reemplazar datos empresariales con datos públicos, y COSTE_API_ALTO, por las llamadas o contextos extensos asociados, con lo cual se asigna 1. <!-- matriz_decision.json: candidatos/DG/evidencia/C4; candidatos/DG/p; penalizaciones/SUSTITUTO; penalizaciones/COSTE_API_ALTO -->
- **C5:** Por tratarse de un candidato de evaluación, una medición resulta informativa en cualquier dirección y la regla asigna 3. <!-- matriz_decision.json: candidatos/DG/p; reglas_matriz.md: C5 -->

### DA+DC — Aclaración con el usuario e interacción más metodología de evaluación multiturno

- **C1:** La regla de combinación usa la media de las puntuaciones de DA y DC, 1 y 3, respectivamente, y produce 2. <!-- matriz_decision.json: candidatos/DA/p; candidatos/DC/p; candidatos/DA+DC/p -->
- **C2:** En E0–E2 se usa la media entre 2 para DA, sustentado por los contrastes de R00123 (Elgohary2020Speak), R00222 (Jiang2025SiriusBI), R00311 (Chen2024Learning), R00312 (Sun2024QDASQL) y R00480 (Teixeira2026SemPlan), y 0 para DC, lo que produce 1, mientras que en E3 se excluye el componente no aplicable de DC y se usa 2. <!-- matriz_decision.json: candidatos/DA/evidencia/C2; candidatos/DC/evidencia/C2; candidatos/DA+DC/p; candidatos/DA+DC/c2_E3; mapa_oe_contrastes.csv: OE4/principal_nivel2_umbral/Aclaración / interacción con el usuario (alternativa), estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** La regla de combinación toma el máximo de las puntuaciones de novedad de DA y DC, 1 y 1, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/DA/p; candidatos/DC/p; candidatos/DA+DC/p -->
- **C4:** La regla de combinación toma el mínimo de factibilidad entre DA, con SUSTITUTO y puntuación 2, y DC, sin requisitos y puntuación 3, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DA/evidencia/C4; candidatos/DC/evidencia/C4; candidatos/DA/p; candidatos/DC/p; candidatos/DA+DC/p -->
- **C5:** La regla de combinación toma el mínimo de las puntuaciones de riesgo nulo de DA y DC, 2 y 3, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DA/p; candidatos/DC/p; candidatos/DA+DC/p -->

### DB+DD — Datos en español y multilingües más contaminación de *benchmarks* y fecha de los modelos

- **C1:** La regla de combinación usa la media de las puntuaciones de DB y DD, 1 y 2, respectivamente, y produce 1,5. <!-- matriz_decision.json: candidatos/DB/p; candidatos/DD/p; candidatos/DB+DD/p -->
- **C2:** En E0–E2 se usa la media entre 0 para DB y 0 para DD, lo que produce 0, mientras que en E3 ambos componentes carecen de contrastes y el criterio completo se considera no aplicable. <!-- matriz_decision.json: candidatos/DB/p; candidatos/DD/p; candidatos/DB+DD/p; candidatos/DB+DD/c2_E3 -->
- **C3:** La regla de combinación toma el máximo de las puntuaciones de novedad de DB y DD, 3 y 2, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DB/p; candidatos/DD/p; candidatos/DB+DD/p -->
- **C4:** La regla de combinación toma el mínimo de factibilidad entre DB, con ANOTACION y puntuación 2, y DD, con INFO_NO_OBSERVABLE y puntuación 2, por lo que se asigna 2. <!-- matriz_decision.json: candidatos/DB/evidencia/C4; candidatos/DD/evidencia/C4; candidatos/DB/p; candidatos/DD/p; candidatos/DB+DD/p -->
- **C5:** La regla de combinación toma el mínimo de las puntuaciones de riesgo nulo de DB y DD, 3 y 3, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DB/p; candidatos/DD/p; candidatos/DB+DD/p -->

### DE+DF+DG — Líneas base simples fuertes más coste y eficiencia más esquemas grandes o empresariales

- **C1:** La regla de combinación usa la media de las puntuaciones de DE, DF y DG, 0, 3 y 1, respectivamente, y produce 1,33. <!-- matriz_decision.json: candidatos/DE/p; candidatos/DF/p; candidatos/DG/p; candidatos/DE+DF+DG/p -->
- **C2:** En E0–E2 se usa la media entre 3 para DE, 0 para DF y 0 para DG, que produce 1, mientras que en E3 se excluyen los componentes no aplicables y se usa 3 para DE; los contrastes de DE proceden de R00072 (Zhang2024CoESQL), R00079 (Ryu2024EHRSeqSQL), R00093 (Zheng2022HIESQL), R00120 (Wang2020PGGSQL), R00126 (Yu2019SParC), R00131 (Zhang2019EditSQL), R00148 (Urban2025Utilizing), R00435 (Tummalapenta2026Memory), R00453 (Lian2026CoeusBI), R00499 (Yang2026GitHarness), R00508 (Yang2026HarnessSQL), R00868 (Fu2023MIGA), R00078 (Li2024MultiSQL) y R00927 (Ascoli2025Advancing). <!-- matriz_decision.json: candidatos/DE/evidencia/C2; candidatos/DF/evidencia/C2; candidatos/DG/evidencia/C2; candidatos/DE+DF+DG/p; candidatos/DE+DF+DG/c2_E3; mapa_oe_contrastes.csv: OE2/principal_nivel2_umbral/SQL previo / edición / ventana (alternativa) y OE1/principal_nivel2_umbral/Concatenación / historial (alternativa), estudios; bib/claves_estudios.csv: clave_bib -->
- **C3:** La regla de combinación toma el máximo de las puntuaciones de novedad de DE, DF y DG, 0, 0 y 3, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DE/p; candidatos/DF/p; candidatos/DG/p; candidatos/DE+DF+DG/p -->
- **C4:** La regla de combinación toma el mínimo entre DE, sin requisitos y puntuación 3, DF, sin requisitos y puntuación 3, y DG, con SUSTITUTO y COSTE_API_ALTO y puntuación 1, por lo que se asigna 1. <!-- matriz_decision.json: candidatos/DE/evidencia/C4; candidatos/DF/evidencia/C4; candidatos/DG/evidencia/C4; candidatos/DE/p; candidatos/DF/p; candidatos/DG/p; candidatos/DE+DF+DG/p -->
- **C5:** La regla de combinación toma el mínimo de las puntuaciones de riesgo nulo de DE, DF y DG, todas de 3, por lo que se asigna 3. <!-- matriz_decision.json: candidatos/DE/p; candidatos/DF/p; candidatos/DG/p; candidatos/DE+DF+DG/p -->

## Robustez

Los escenarios no producen una primera posición estable: OE2 ocupa el rango 1 en E0 y E2, mientras DC ocupa el rango 1 en E1 y E3; sus intervalos globales son 1–8 y 1–2, respectivamente. <!-- matriz_decision.csv: OE2/DC, rango_E0_iguales/rango_E1_factibilidad/rango_E2_evidencia/rango_E3_iguales_C2_NA/rango_min/rango_max --> DB+DD se mantiene entre los rangos 2–9, DE+DF+DG entre 3–10 y OE3 entre 12–15, pero los demás candidatos también cambian de posición al variar los pesos o el tratamiento de C2. <!-- matriz_decision.csv: DB+DD/DE+DF+DG/OE3, rango_min/rango_max --> En particular, E3 eleva a los candidatos de evaluación sin contrastes al retirar C2 del denominador: DC pasa del rango 2 en E0 al 1 en E3, y DB pasa del 5 al 4. <!-- matriz_decision.csv: DC/DB, rango_E0_iguales/rango_E3_iguales_C2_NA --> Estos desplazamientos describen sensibilidad a la ponderación y a la asimetría de aplicabilidad, no evidencia de eficacia.

La dominancia de Pareto sí permanece fijada por las puntuaciones de criterios y no por los pesos: OE2 domina a OE4, DA y DA+DC; OE1 y OE4 también dominan a DA; DC domina a OE5 y DF; DB+DD domina a DB y DG; y DB y DE+DF+DG también dominan a DG. <!-- matriz_decision.csv: dominado_por --> Los candidatos sin una relación de dominancia registrada no quedan ordenados por Pareto entre sí, porque presentan compensaciones entre criterios.

Las posiciones también dependen de las entradas de juicio aprobadas por la autora, incluida D13, que conserva C2 en 0 para los candidatos de evaluación sin contrastes bajo E0–E2 y lo declara no aplicable bajo E3. <!-- revision_matriz.md: D13 --> Si la novedad de OE1 se midiera mediante clasificación de actos de discurso, su E0 cambiaría de 60,0 a 73,3 y su rango E0 de 5 a 1; si la de OE4 se midiera mediante reparación simbólica, su E0 cambiaría de 60,0 a 66,7 y su rango E0 de 5 a 2. <!-- matriz_alternativas.csv: D14/OE1; D15/OE4 --> Asignar a DE un problema cualitativo cambiaría su E0 de 60,0 a 66,7, mientras vincular DG con errores de *join* cambiaría su E0 de 53,3 a 60,0. <!-- matriz_alternativas.csv: D16/DE; D17/DG --> Retirar SUSTITUTO de OE5 cambiaría su E0 de 60,0 a 66,7, y añadir MULTICOMPONENTE a OE3 lo cambiaría de 53,3 a 46,7. <!-- matriz_alternativas.csv: D18a/OE5; D18b/OE3 --> Sustituir la media por el máximo para la evidencia de las combinaciones tendría su mayor cambio registrado en DE+DF+DG, de 62,2 a 86,7 en E0 y del rango 4 al 1, mientras reducir C5 de evaluación de 3 a 2 modificaría los totales y rangos de todos los candidatos de evaluación y de las combinaciones que los contienen. <!-- matriz_alternativas.csv: D19/DE+DF+DG; D20 --> La matriz conserva las opciones base aprobadas para esas decisiones; por tanto, estas alternativas se usan únicamente como análisis de sensibilidad y no reemplazan las puntuaciones presentadas.

## Limitaciones de la matriz

Las puntuaciones son ordinales, pero los totales las suman y normalizan como si las distancias entre 0, 1, 2 y 3 fueran intervalos equivalentes. <!-- reglas_matriz.md: escala; Escenarios de ponderación --> C2 usa el número de estudios, la dirección, la confianza y el alcance, pero omite la magnitud de los efectos porque los contrastes proceden de *benchmarks*, métricas y modelos heterogéneos; por ello una puntuación alta no demuestra eficacia. <!-- reglas_matriz.md: C2 --> Los candidatos de evaluación sin clases de contraste reciben 0 en C2 bajo E0–E2, aunque su aporte pueda ser informativo sin mejora, y esta asimetría se trata en E3 mediante la no aplicabilidad y en C5 mediante la puntuación 3 para evaluaciones. <!-- reglas_matriz.md: C2; C5; E3 --> Los umbrales de cobertura, dirección positiva, confianza y factibilidad son convenciones de esta matriz y pueden cambiar la posición de casos cercanos a sus cortes. Finalmente, los totales E0 se concentran en un intervalo de 53,3 a 73,3, con varios empates y diferencias pequeñas, de modo que el orden no debe interpretarse como una separación sustantiva entre candidatos. <!-- matriz_decision.csv: E0_iguales -->
