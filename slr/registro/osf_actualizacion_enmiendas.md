# Actualización del registro OSF — enmiendas A1–A3 (texto para pegar)

Registro: https://osf.io/5usf3/ · DOI 10.17605/OSF.IO/5USF3 · fuente: `slr/protocolo/enmiendas.md`.

**Procedimiento:** abra la página del **registro** → **Update** → pegue la justificación (sección 1) → en cada campo de la sección 2, **deje el texto existente** y **añada al final** el bloque indicado (con una línea en blanco antes) → *Review* → *Submit*. Compruebe después que el registro muestra una versión nueva.

---

## 1. Justificación de la actualización (*justification*)

Se registran tres enmiendas al protocolo v1.2, documentadas con fecha y motivo en `enmiendas.md` del repositorio del proyecto. A1 (2026-10-11): la elegibilidad del conjunto de referencia la determina la IA aplicando los criterios registrados; el conjunto se usa solo para medir la sensibilidad de la búsqueda y se elimina la prueba de positivos conocidos de los revisores IA, que sería circular. A2 (2026-10-11): la exportación de citas de ACM DL solo está disponible para cuentas premium, por lo que los resultados de ACM se capturan guardando las páginas de resultados como HTML sin editar y completando los metadatos desde OpenAlex/Crossref por DOI; las cadenas y el motor de búsqueda no cambian. A3 (2026-10-11): diseño reducido de verificación humana del cribado (una muestra ciega de 60 registros que sirve de piloto y de validación, más la revisión por la autora de todos los conflictos y de las exclusiones que la recomprobación QC propone avanzar). Motivo común: revisión realizada por una autora única con tiempo limitado. Las tres enmiendas se adoptaron antes del cribado título/resumen; las limitaciones que introducen se declararán en el artículo. Los demás campos no cambian.

---

## 2. Bloques para añadir a cada campo

### Campo *Interfaces* (A2)

[Enmienda A2, 2026-10-11] ACM DL: la exportación de citas solo está disponible para cuentas premium. Las consultas ACM-1 y ACM-2 se ejecutaron sin cambios en el sitio web de ACM; los resultados se capturaron guardando las páginas de resultados (50 por página) como HTML sin editar. Un script versionado (`acm_html2ris.py`) extrae el DOI y el título de cada resultado y completa los metadatos (autores, año, fuente, resumen) desde OpenAlex o Crossref por DOI. Se verificó que el número de ítems extraídos coincide con el número de resultados mostrados en pantalla para ambas consultas. Las cadenas y el motor de búsqueda no cambian.

### Campo *Search validation procedure* (A1)

[Enmienda A1, 2026-10-11] La elegibilidad de los 57 candidatos del conjunto de referencia la determinó la IA (Claude Opus 5.5) aplicando los criterios registrados sobre título y resumen, en lugar de la autora; los candidatos clasificados como dudosos quedan para revisión humana cuando sea posible. El conjunto se usa solo para medir la sensibilidad de la búsqueda, que se reporta con los candidatos «elegibles» y, como análisis de sensibilidad, con «elegibles + probables». Limitación: el juicio de la IA se hizo cuando ya se conocían los resultados de arXiv y ACL Anthology (no los de Scopus, IEEE Xplore ni ACM DL).

### Campo *Screened fields / masking* (A3)

[Enmienda A3, 2026-10-11] La auditoría humana ciega de exclusiones se suprime. La autora etiquetó a ciegas una única muestra aleatoria de 60 registros antes de cualquier decisión de la IA (véase *Sampling and sample size*). En la revisión de casos no evidentes, la autora ve las decisiones y los motivos de los revisores IA.

### Campo *Screening reliability* (A1 + A3)

[Enmiendas A1 y A3, 2026-10-11] (A1) Se elimina la prueba de sensibilidad de los revisores IA con el conjunto de referencia: ese conjunto lo clasificó la IA, por lo que la prueba sería circular. (A3) La fiabilidad se mide con una única muestra aleatoria de 60 registros, extraída con semilla fija de los lotes del piloto (excluidos los estudios semilla) y etiquetada por la autora a ciegas, que sirve a la vez de piloto y de muestra de validación: acuerdo humano–IA (acuerdo observado, kappa de Cohen, PABAK) y sensibilidad y especificidad con IC 95 %. Se reportan tanto el acuerdo con las etiquetas ciegas como el acuerdo tras la conciliación documentada de las discrepancias. Limitación declarada: con 60 registros las estimaciones son poco precisas y la muestra no es independiente del piloto (no hay muestra reservada); se reportan los IC y se discute.

### Campo *Screening reconciliation procedure* (A3)

[Enmienda A3, 2026-10-11] Sustituye a la auditoría humana de máx(10 %, 150) exclusiones. La autora revisa todos los casos no evidentes en los que una decisión de la IA podría excluir un estudio: todos los conflictos entre los revisores A y B (resueltos o no por el tercer revisor) y todas las exclusiones conjuntas que la recomprobación QC por un revisor sénior IA propone avanzar; sus decisiones se registran como anulaciones (`overrides.csv`). Las decisiones «unclear» no se revisan en título/resumen porque avanzan automáticamente a texto completo, donde la autora las verifica según la regla de contingencia por volumen. Las exclusiones evidentes (ambos revisores IA excluyen) quedan cubiertas por la recomprobación QC automática (muestra de 150 más casos cercanos por palabras clave) y por la tasa de error estimada en la muestra de 60. Control del piloto: la IA no puede excluir ningún registro que la autora avance; las discrepancias se concilian por escrito conservando las etiquetas ciegas.

### Campo *Sampling and sample size* (A3)

[Enmienda A3, 2026-10-11] Piloto y validación: una única muestra aleatoria de 60 registros (semilla fija, lotes del piloto, sin estudios semilla), etiquetada a ciegas por la autora. Sustituye al piloto de 50–100 registros, a la validación reservada de 100 registros y a la auditoría de máx(10 %, 150) exclusiones. La recomprobación QC por IA (muestra de 150 exclusiones conjuntas más casos cercanos) y la regla de contingencia por volumen no cambian.

### Campo *Screening procedure justification* (A3)

[Enmienda A3, 2026-10-11] Por limitación de tiempo de la autora única, la validación humana reservada y la auditoría de exclusiones se sustituyen por la muestra ciega de 60 registros y por la revisión de todos los casos no evidentes en los que la IA podría excluir un estudio. La limitación se declara en el artículo.

---

# Segunda actualización — enmienda A4 (2026-10-11)

## Justificación (*justification*)

Enmienda A4 (2026-10-11), documentada en `enmiendas.md`: no se contacta a los autores de los informes cuyo texto completo no se pudo obtener. Motivo: revisión realizada por una autora única con tiempo limitado. Los informes no obtenidos se reportan como «no recuperados» en el diagrama PRISMA, con su motivo, y se añade un análisis de sensibilidad del indicador principal. Los demás campos no cambian.

## Campo *Procedures to contact authors* (A4) — añadir al final

[Enmienda A4, 2026-10-11] No se contacta a los autores. La recuperación de textos completos se limita a rutas de acceso abierto automáticas (ACL Anthology, arXiv, OpenAlex, Semantic Scholar → arXiv, búsqueda en arXiv por título exacto) y a la búsqueda manual de la autora (navegador y acceso de la biblioteca de la UNMSM). Cada informe se registra con su ruta o su motivo de no recuperación (sin acceso, retirado, no encontrado).

## Campo *Results of contacting authors* (A4) — añadir al final

[Enmienda A4, 2026-10-11] No aplica: no se contactó a los autores. Los informes no recuperados se reportan en el diagrama PRISMA («informes no recuperados»), y el indicador principal (proporción multiturno, D4) se calcula además con las decisiones de título/resumen como análisis de sensibilidad. Limitación declarada: posible sesgo de disponibilidad hacia editoriales de acceso abierto.
