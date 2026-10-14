# PI0 — Mapeo descriptivo (Nivel 1)

Pregunta: ¿cómo se distribuyen los estudios por año, tipo de publicación, paradigma técnico y escenario, y cómo evoluciona la proporción de estudios multiturno?

## Mapeo general

Se incluyeron 390 estudios, de los cuales 77 son multiturno [pi0_resultados.json]. Los 77 multiturno son el conjunto del Nivel 2 [pi15_resultados.json].

**Estudios por año y escenario** (Figura `pi0_anio_escenario`) [pi0_anio_escenario.csv]. 2026 es año parcial.

| Año | Multiturno | Un turno | Total |
|---|---|---|---|
| 2019 | 3 | 6 | 9 |
| 2020 | 7 | 12 | 19 |
| 2021 | 8 | 16 | 24 |
| 2022 | 9 | 10 | 19 |
| 2023 | 9 | 23 | 32 |
| 2024 | 10 | 37 | 47 |
| 2025 | 13 | 88 | 101 |
| 2026* | 18 | 121 | 139 |

**Tipo de publicación y *venue*** [pi0_foros.csv]: preprint 146; congreso A\* 90, A 8, B 16, C 1 y sin ranking 51; revista Q1 34, Q2 17, Q3 1, Q4 3 y sin ranking 1; taller 9; desconocido 12. Los *venues* más frecuentes son arXiv (125), *Annual Meeting of the Association for Computational Linguistics* (19), *Findings of the ACL: ACL 2026* (11) y *Proceedings of the ACM on Management of Data* (8) [pi0_venues_top.csv].

**Paradigma técnico principal por año** (Figura `pi0_paradigma_anio`) [pi0_paradigma_anio.csv]:

| Paradigma | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026* |
|---|---|---|---|---|---|---|---|---|
| LLM_PROMPTING | 0 | 0 | 0 | 1 | 8 | 20 | 33 | 54 |
| PLM_FINETUNING | 2 | 13 | 17 | 14 | 19 | 10 | 3 | 5 |
| AGENTES | 1 | 0 | 0 | 0 | 1 | 6 | 27 | 43 |
| LLM_FINETUNING | 0 | 0 | 0 | 0 | 0 | 8 | 31 | 25 |
| HIBRIDO_NEUROSIMBOLICO | 1 | 1 | 1 | 1 | 3 | 3 | 5 | 12 |
| NEURONAL_PRE_PLM | 4 | 3 | 5 | 1 | 1 | 0 | 0 | 0 |
| REGLAS_SIMBOLICO | 1 | 1 | 0 | 2 | 0 | 0 | 1 | 0 |

**Pilares centrales por escenario** [pi0_pilares_escenario.csv]: PI1 13 multiturno y 0 de un turno; PI2 26 y 0; PI3 13 y 156; PI4 22 y 140.

**Entrenamiento** [pi0_training_free.csv]: estudios con PI3 central y de ellos sin entrenamiento, por año: 2022, 9 y 1; 2023, 15 y 3; 2024, 21 y 10; 2025, 43 y 15; 2026, 60 y 34 (2019–2021: 0 sin entrenamiento). Para PI4: 2023, 11 y 6; 2024, 14 y 7; 2025, 50 y 20; 2026, 81 y 44 (2019–2022: 0 sin entrenamiento).

**Informes no recuperados por escenario (D6)**: 148 de señal de un turno y 43 de señal multiturno [pi0_no_recuperados_escenario.csv; pi0_resultados.json].

## Indicador D4

Regla registrada: la conclusión «considerablemente menos investigado» se emite solo si el límite superior del IC 95 % de Wilson es ≤ 30 %; si el IC contiene el 30 %, el resultado es no concluyente [01_preguntas_picoc.md].

| Versión | k / n | Proporción | IC 95 % de Wilson | Conclusión según la regla |
|---|---|---|---|---|
| Estricta | 34 / 302 | 11,26 % | 8,17–15,32 % | considerablemente menos investigado |
| Laxa (sensibilidad) | 49 / 317 | 15,46 % | 11,89–19,85 % | considerablemente menos investigado |

Fuente: [pi0_resultados.json].

**Tendencia 2019–2025** (Figura `d4_tendencia`): estadístico de Cochran–Armitage −0,6; p exacta bilateral 0,9499 (10 000 réplicas) [pi0_resultados.json]. Proporciones anuales [d4_tendencia.csv]:

| Año | k / n | p | IC 95 % |
|---|---|---|---|
| 2019 | 0 / 5 | 0,00 | 0,00–43,45 % |
| 2020 | 2 / 9 | 22,22 % | 6,32–54,74 % |
| 2021 | 1 / 12 | 8,33 % | 1,49–35,39 % |
| 2022 | 3 / 11 | 27,27 % | 9,75–56,57 % |
| 2023 | 4 / 24 | 16,67 % | 6,68–35,85 % |
| 2024 | 5 / 32 | 15,62 % | 6,86–31,75 % |
| 2025 | 12 / 87 | 13,79 % | 8,07–22,58 % |

2026 (año parcial, fuera de la prueba): 7 / 122, 5,74 % (IC 95 % 2,81–11,37 %) [pi0_resultados.json]. En los años 2019–2024 el límite superior del IC contiene el 30 % [d4_tendencia.csv].

## Técnicas de un turno no trasladadas al multiturno

Un único código aparece en un turno y no en multiturno: `pi4_mecanismo: AUTOCONSISTENCIA_VOTACION`, con 42 estudios de un turno y 0 multiturno [pi0_resultados.json; pi34_tecnicas_escenario.csv]. El resto de técnicas se detalla en PI3 y PI4.

## Bibliometría exploratoria (exploratorio, no pre-registrado (A6))

- OpenAlex (2026-10-13) resolvió 383 de 389 estudios; no se resolvieron R00005, R00039, R00061, R00065, R00935 y R00953 [bibliometria_resultados.json].
- Red de citas (Figura `bib_red_citas`): 389 nodos, 841 aristas, 205 aislados; citas por dirección: UT→UT 432, UT→MT 137, MT→MT 173, MT→UT 99 [bibliometria_resultados.json]. Mediana de citas por año: multiturno 1,0; un turno 0,5 [bibliometria_resultados.json].
- Afiliación: solo academia 196, academia + industria 79, solo industria 28, sin datos 80 [bibliometria_resultados.json].
- Países (Figura `bib_paises`): CN 170 estudios (35 multiturno, 135 un turno), US 91 (24; 67), HK 18, KR 12, CA 12 [bib_paises.csv].
- Comunidad del foro (Figura `bib_comunidad`), multiturno / un turno: PLN 34 / 65; Bases de datos 4 / 23; Aprendizaje automático / IA 7 / 19; Otra 14 / 77; Preprint 18 / 128 [bib_comunidad.csv].
- Estudios multiturno más citados por año de publicación: R00109 (PICARD), 321 citas; R00129 (CoSQL), 158; R00126 (SPARC), 141 [bib_mas_citados_multiturno.csv].
- Términos más frecuentes en títulos y resúmenes: *schema* (206 estudios; 30 multiturno), *execution* (178; 20), *spider* (155; 12), *user* (117; 37) [bib_terminos.csv].

## Sensibilidad

D4 [pi15_resultados.json, sensibilidad.json]:

| Análisis | k / n | p | IC 95 % | Conclusión |
|---|---|---|---|---|
| Sin preprints | 23 / 177 | 12,99 % | 8,82–18,74 % | considerablemente menos investigado |
| Versión laxa | 49 / 317 | 15,46 % | 11,89–19,85 % | considerablemente menos investigado |
| Solo búsquedas en bases | 34 / 273 | 12,45 % | 9,05–16,90 % | considerablemente menos investigado |
| Solo foros de primer nivel (A5) | 15 / 116 | 12,93 % | 8,00–20,24 % | considerablemente menos investigado |
| No recuperados según señal (A4)* | 77 / 493 | 15,62 % | 12,68–19,09 % | (sin conclusión registrada) |

\*Supuesto: todos los no recuperados cuentan en el denominador y los de señal multiturno también en el numerador (cota conservadora) [sensibilidad.json].

Contingencia del Nivel 1: «No aplica: la regla de contingencia por volumen no se activó (texto completo de un turno < 400)» [sensibilidad.json]. Ninguna de las variantes cambia la conclusión de la regla.

## Limitaciones

- El indicador depende del marco de elegibilidad (los estudios de un turno deben cumplir más requisitos), lo que tiende a aumentar la proporción multiturno; no se generaliza a todo el campo [01_preguntas_picoc.md].
- Los informes no recuperados son 148 de señal de un turno y 43 de señal multiturno [pi0_resultados.json].
- Acuerdo entre extractores en el Nivel 1: 4131/4755 campos (86,9 %; IC 95 % 85,9–87,8 %) [informe_acuerdo_extraccion.md].
- 2026 es año parcial (búsqueda del 11 de octubre de 2026) [leyendas.json].
- En el Nivel 1 solo se registraron los modelos citados en las páginas 1–2, por lo que el uso real de familias de modelos está subestimado [leyendas.json, `bib_modelos`].

## Para la discusión (no forma parte de los hallazgos)

- La regla registrada del D4 se cumple en todas las variantes de sensibilidad reportadas.
- La ausencia de tendencia detectable (p = 0,9499) convive con proporciones anuales de IC amplio en 2019–2024.
- La interpretación de la proporción 2026 debe considerar que el año es parcial.
