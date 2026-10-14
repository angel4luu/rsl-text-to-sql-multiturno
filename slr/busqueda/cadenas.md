# Cadenas de búsqueda — versión v4 (revisada tras el Checkpoint 1, 2026-10-11)

Diseño: **A (tarea) AND (B1 (multiturno) OR B2 (pilares 3–4))**, campos título + resumen + palabras clave, 2019–2026.
Historial de versiones, pruebas y conteos marginales: `pruebas_cadenas.md`.
**Al ejecutar cada búsqueda oficial (Fase 2):** registrar fecha, cadena exacta pegada, filtros y número de resultados en `registro_busquedas.csv`, y guardar la exportación sin editar en `exports/<base>/`.

## Bloques conceptuales (forma canónica)
**A — tarea:** "text-to-SQL" · "text to SQL" · text2sql · NL2SQL · "NL-to-SQL" · "natural language to SQL" · "natural language interface(s) to (relational) database(s)" · NLIDB(s) · "SQL generation" · "SQL query generation" · "SQL synthesis" · "question(s) to SQL" · "database question answering" · "question answering over (relational) databases" · ("semantic parsing" AND (SQL OR database(s) OR SParC OR CoSQL OR Spider OR CHASE))

**B1 — multiturno:** "multi-turn" · multiturn · "multi-round" · multiround · conversational · "context-dependent" · "context dependent" · "context-aware" · dialog/dialogue · "dialogue state tracking" · "follow-up" · interactive · session · chat · chatbot(s) · "chat-based" · coreference · ellipsis · anaphora · "query/question/utterance rewriting" · SParC · CoSQL

**B2 — pilares 3–4:** "schema linking" · "schema pruning" · "schema selection" · "schema retrieval" · "schema grounding" · "schema filtering" · "schema routing" · "keyword mapping" · "table selection" · "column selection" · "table retrieval" · "value linking" · "value retrieval" · "join path(s)" · "join inference" · "multi-hop join" · "foreign key(s)" · Steiner · self-correct(ion/ing) · self-debug(ging) · debugging · self-refine/self-refinement · refinement · "self-consistency" · reflection · verifier/verification · "candidate selection" · "execution feedback" · "execution-guided" · "error correction" · "SQL correction" · "SQL repair" · "query repair"

## Tabla de equivalencia entre bases
| Concepto | Scopus | IEEE | ACM | arXiv / ACL (script) |
|---|---|---|---|---|
| Bloque A completo | ✓ | ✓ (variantes sin comodín); «semantic parsing ∧ (…)» en IEEE-4 | ✓ | ✓ |
| B1 completo | ✓ | ✓ (IEEE-1) | ✓ | ✓ |
| B2 vinculación / *joins* | ✓ | ✓ (IEEE-2) | ✓ | ✓ |
| B2 autocorrección | ✓ | ✓ (IEEE-3) | ✓ | ✓ |
| Comodines | sí (`*`) | no: variantes escritas | sí (`*`) | no: variantes escritas |
Ningún término se omite por límite de longitud sin dividir la consulta; toda división se documenta.

---

## 1. Scopus (Advanced search)
```
TITLE-ABS-KEY("text-to-SQL" OR "text to SQL" OR text2sql OR nl2sql OR "NL-to-SQL" OR "natural language to SQL" OR "natural language interface* to database*" OR "natural language interface* to relational database*" OR nlidb* OR "SQL generation" OR "SQL query generation" OR "SQL synthesis" OR "question* to SQL" OR "database question answering" OR "question answering over database*" OR "question answering over relational database*" OR ("semantic pars*" AND (sql OR database* OR sparc OR cosql OR spider OR chase)))
AND ( TITLE-ABS-KEY("multi-turn" OR multiturn OR "multi-round" OR multiround OR conversational OR "context-dependent" OR "context dependent" OR "context-aware" OR dialog* OR "follow-up" OR interactive OR session* OR chat OR chatbot* OR "chat-based" OR coreference OR ellipsis OR anaphor* OR "query rewriting" OR "question rewriting" OR "utterance rewriting" OR sparc OR cosql)
   OR TITLE-ABS-KEY("schema linking" OR "schema pruning" OR "schema selection" OR "schema retrieval" OR "schema grounding" OR "schema filtering" OR "schema routing" OR "keyword mapping" OR "table selection" OR "column selection" OR "table retrieval" OR "value linking" OR "value retrieval" OR "join path*" OR "join inference" OR "multi-hop join*" OR "foreign key*" OR steiner OR "self-correct*" OR "self-debug*" OR debugging OR "self-refin*" OR refinement OR "self-consistency" OR reflection OR verifier* OR verification OR "candidate selection" OR "execution feedback" OR "execution-guided" OR "error correction" OR "SQL correction" OR "SQL repair" OR "query repair") )
AND PUBYEAR > 2018 AND PUBYEAR < 2027
```
Exportar: RIS o CSV con resumen y palabras clave. Sin otros filtros.

## 2. IEEE Xplore (Command Search, *All Metadata*)
Para no exceder los límites de términos, se ejecutan **cuatro consultas** y se unen en la Fase 3. `AM` abrevia `"All Metadata"` y debe escribirse completo al pegar.

**A (común a IEEE-1, -2 y -3):**
```
(AM:"text-to-SQL" OR AM:"text to SQL" OR AM:text2sql OR AM:NL2SQL OR AM:"NL-to-SQL" OR AM:"natural language to SQL" OR AM:"natural language interface to database" OR AM:"natural language interfaces to databases" OR AM:"natural language interface to relational database" OR AM:"natural language interfaces to relational databases" OR AM:NLIDB OR AM:NLIDBs OR AM:"SQL generation" OR AM:"SQL query generation" OR AM:"SQL synthesis" OR AM:"question to SQL" OR AM:"questions to SQL" OR AM:"database question answering" OR AM:"question answering over databases" OR AM:"question answering over relational databases")
```
**IEEE-1 = A AND B1**
```
AND (AM:"multi-turn" OR AM:multiturn OR AM:"multi-round" OR AM:multiround OR AM:conversational OR AM:"context-dependent" OR AM:"context dependent" OR AM:"context-aware" OR AM:dialogue OR AM:dialog OR AM:"dialogue state tracking" OR AM:"follow-up" OR AM:interactive OR AM:session OR AM:chat OR AM:chatbot OR AM:"chat-based" OR AM:coreference OR AM:ellipsis OR AM:anaphora OR AM:"query rewriting" OR AM:"question rewriting" OR AM:"utterance rewriting" OR AM:SParC OR AM:CoSQL)
```
**IEEE-2 = A AND B2a (vinculación / *joins*)**
```
AND (AM:"schema linking" OR AM:"schema pruning" OR AM:"schema selection" OR AM:"schema retrieval" OR AM:"schema grounding" OR AM:"schema filtering" OR AM:"schema routing" OR AM:"keyword mapping" OR AM:"table selection" OR AM:"column selection" OR AM:"table retrieval" OR AM:"value linking" OR AM:"value retrieval" OR AM:"join path" OR AM:"join inference" OR AM:"multi-hop join" OR AM:"foreign key" OR AM:Steiner)
```
**IEEE-3 = A AND B2b (autocorrección)**
```
AND (AM:"self-correction" OR AM:"self-correcting" OR AM:"self-debugging" OR AM:debugging OR AM:"self-refine" OR AM:"self-refinement" OR AM:refinement OR AM:"self-consistency" OR AM:reflection OR AM:verifier OR AM:verification OR AM:"execution feedback" OR AM:"execution-guided" OR AM:"candidate selection" OR AM:"error correction" OR AM:"SQL correction" OR AM:"SQL repair" OR AM:"query repair")
```
**IEEE-4 = análisis semántico + bases de datos (sin bloque B, porque ya es muy específico)**
```
(AM:"semantic parsing") AND (AM:SQL OR AM:database OR AM:databases OR AM:SParC OR AM:CoSQL OR AM:Spider)
```
Filtros: 2019–2026. Exportar CSV con resumen.

## 3. ACM Digital Library (Advanced Search → editar consulta)
Colección: **ACM Full-Text Collection.** Justificación: la *ACM Guide to Computing Literature* reindexa registros de terceros (IEEE, Springer) ya cubiertos por Scopus/IEEE y multiplicaría los duplicados; la Full-Text Collection aporta lo que solo está en ACM (p. ej., PACMMOD, SIGMOD, CIKM, KDD).
**Regla de sintaxis ACM (corregida tras el conteo previo, 2026-10-11):** ACM no admite comodines **dentro de frases entre comillas**; las variantes se escriben completas. Los comodines solo se usan en palabras sueltas.

Consulta **ACM-1** (tarea ∧ (multiturno ∨ pilares)):
```
(Title:("text-to-SQL" OR "text to SQL" OR text2sql OR nl2sql OR "NL-to-SQL" OR "natural language to SQL" OR "natural language interface to database" OR "natural language interfaces to databases" OR "natural language interface to relational database" OR "natural language interfaces to relational databases" OR nlidb OR nlidbs OR "SQL generation" OR "SQL query generation" OR "SQL synthesis" OR "question to SQL" OR "questions to SQL" OR "database question answering" OR "question answering over databases" OR "question answering over relational databases") OR Abstract:("text-to-SQL" OR "text to SQL" OR text2sql OR nl2sql OR "NL-to-SQL" OR "natural language to SQL" OR "natural language interface to database" OR "natural language interfaces to databases" OR "natural language interface to relational database" OR "natural language interfaces to relational databases" OR nlidb OR nlidbs OR "SQL generation" OR "SQL query generation" OR "SQL synthesis" OR "question to SQL" OR "questions to SQL" OR "database question answering" OR "question answering over databases" OR "question answering over relational databases") OR Keyword:("text-to-SQL" OR "text to SQL" OR text2sql OR nl2sql OR "NL-to-SQL" OR "natural language to SQL" OR "natural language interface to database" OR "natural language interfaces to databases" OR "natural language interface to relational database" OR "natural language interfaces to relational databases" OR nlidb OR nlidbs OR "SQL generation" OR "SQL query generation" OR "SQL synthesis" OR "question to SQL" OR "questions to SQL" OR "database question answering" OR "question answering over databases" OR "question answering over relational databases"))
AND
(Title:("multi-turn" OR multiturn OR "multi-round" OR multiround OR conversational OR "context-dependent" OR "context dependent" OR "context-aware" OR dialog* OR "follow-up" OR interactive OR session* OR chat OR chatbot* OR "chat-based" OR coreference OR ellipsis OR anaphor* OR "query rewriting" OR "question rewriting" OR "utterance rewriting" OR sparc OR cosql OR "schema linking" OR "schema pruning" OR "schema selection" OR "schema retrieval" OR "schema grounding" OR "schema filtering" OR "schema routing" OR "keyword mapping" OR "table selection" OR "column selection" OR "table retrieval" OR "value linking" OR "value retrieval" OR "join path" OR "join paths" OR "join inference" OR "multi-hop join" OR "multi-hop joins" OR "foreign key" OR "foreign keys" OR steiner OR "self-correction" OR "self-correcting" OR "self-debugging" OR debugging OR "self-refine" OR "self-refinement" OR refinement OR "self-consistency" OR reflection OR verifier* OR verification OR "candidate selection" OR "execution feedback" OR "execution-guided" OR "error correction" OR "SQL correction" OR "SQL repair" OR "query repair") OR Abstract:("multi-turn" OR multiturn OR "multi-round" OR multiround OR conversational OR "context-dependent" OR "context dependent" OR "context-aware" OR dialog* OR "follow-up" OR interactive OR session* OR chat OR chatbot* OR "chat-based" OR coreference OR ellipsis OR anaphor* OR "query rewriting" OR "question rewriting" OR "utterance rewriting" OR sparc OR cosql OR "schema linking" OR "schema pruning" OR "schema selection" OR "schema retrieval" OR "schema grounding" OR "schema filtering" OR "schema routing" OR "keyword mapping" OR "table selection" OR "column selection" OR "table retrieval" OR "value linking" OR "value retrieval" OR "join path" OR "join paths" OR "join inference" OR "multi-hop join" OR "multi-hop joins" OR "foreign key" OR "foreign keys" OR steiner OR "self-correction" OR "self-correcting" OR "self-debugging" OR debugging OR "self-refine" OR "self-refinement" OR refinement OR "self-consistency" OR reflection OR verifier* OR verification OR "candidate selection" OR "execution feedback" OR "execution-guided" OR "error correction" OR "SQL correction" OR "SQL repair" OR "query repair") OR Keyword:("multi-turn" OR multiturn OR "multi-round" OR multiround OR conversational OR "context-dependent" OR "context dependent" OR "context-aware" OR dialog* OR "follow-up" OR interactive OR session* OR chat OR chatbot* OR "chat-based" OR coreference OR ellipsis OR anaphor* OR "query rewriting" OR "question rewriting" OR "utterance rewriting" OR sparc OR cosql OR "schema linking" OR "schema pruning" OR "schema selection" OR "schema retrieval" OR "schema grounding" OR "schema filtering" OR "schema routing" OR "keyword mapping" OR "table selection" OR "column selection" OR "table retrieval" OR "value linking" OR "value retrieval" OR "join path" OR "join paths" OR "join inference" OR "multi-hop join" OR "multi-hop joins" OR "foreign key" OR "foreign keys" OR steiner OR "self-correction" OR "self-correcting" OR "self-debugging" OR debugging OR "self-refine" OR "self-refinement" OR refinement OR "self-consistency" OR reflection OR verifier* OR verification OR "candidate selection" OR "execution feedback" OR "execution-guided" OR "error correction" OR "SQL correction" OR "SQL repair" OR "query repair"))
```
Consulta **ACM-2** (análisis semántico + bases de datos, equivalente a IEEE-4):
```
(Title:("semantic parsing" OR "semantic parser" OR "semantic parsers") OR Abstract:("semantic parsing" OR "semantic parser" OR "semantic parsers")) AND (Title:(sql OR database* OR sparc OR cosql OR spider OR chase) OR Abstract:(sql OR database* OR sparc OR cosql OR spider OR chase))
```
Si el sitio rechaza la longitud de ACM-1, se divide B en multiturno / vinculación / autocorrección (como en IEEE) y se documenta.
**Filtro de fecha:** la cuenta de la autora no permite filtrar por año en ACM; los registros anteriores a 2019 se eliminan en la Fase 3 por metadatos (EX1) y se cuentan en el diagrama PRISMA.
Filtros: 2019–2026. Exportar BibTeX/RIS con resumen.
**Comprobación obligatoria (aprobado/fallido en `registro_busquedas.csv`):** S5 (Chen et al. 2025) y S6 (Xie et al. 2025) deben aparecer. Si alguna no aparece, se analiza la causa antes de continuar y se registra.

## 4. arXiv (API, script reproducible)
API oficial `export.arxiv.org/api/query` con un script versionado (Fase 2): `(ti:<A> OR abs:<A>) AND (ti:<B> OR abs:<B>)`, términos expandidos sin comodines, categorías `cs.*`, 2019-01-01 → fecha de búsqueda. Se registran fecha, consulta y número de resultados.

## 5. ACL Anthology (volcado oficial + script)
1. Descargar `anthology+abstracts.bib.gz`; registrar fecha y SHA-256.
2. Aplicar la **misma lógica v4** sobre título + resumen, 2019–2026.
3. **Registros sin resumen (M4e):** aplicar solo el bloque A al título; los que coincidan pasan al cribado.
4. Guardar el subconjunto en `exports/acl/` sin editar.

## Fuente complementaria eliminada
La «comprobación en DBLP» de versiones anteriores se elimina (M4f): no tenía procedimiento ni contabilidad PRISMA. La cobertura de *venues* se verifica con el conjunto de referencia independiente (`pruebas_cadenas.md`).
