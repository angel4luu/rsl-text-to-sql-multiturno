# Screening protocol: title/abstract stage
Version 1.0, confirmed by Angela Lucia Jara Espinoza on 2026-10-11. Source: review protocol v1.2 (`protocolo_es.md`, §8) and eligibility criteria v1.1 (`03_criterios_elegibilidad.md`), translated from Spanish.

Review (systematic review in computer science, Kitchenham guidelines, PICOC): "Conversational Text-to-SQL: context restoration, dialogue state, schema linking and self-correction — a systematic literature review".
Question: which techniques do Text-to-SQL systems use to restore conversational context, represent dialogue state, link the database schema and infer joins, and correct their own SQL, especially in multi-turn settings, and what results do they report?

## Eligibility (full protocol)
- **Task (population):** primary studies that propose, adapt or evaluate a technique or a benchmark for translating natural language into SQL queries over **relational** databases (Text-to-SQL, NL2SQL, natural language interfaces to databases).
- **Scope (intervention), one of:**
  - (a) **Multi-turn** study addressing any of: context restoration (ellipsis, coreference, question rewriting with history), dialogue-state representation, schema linking / join inference, execution feedback / self-correction, or multi-turn benchmarks, metrics or per-turn performance; **or**
  - (b) **Single-turn** study whose **central contribution** is schema linking / join-path inference **or** execution feedback / self-correction.
- **Evaluation:** reports a quantitative empirical evaluation. Single-turn studies must evaluate on at least one public benchmark (e.g., Spider, BIRD, WikiSQL); multi-turn studies may use any data, including proprietary.
- **Dates:** published from 1 January 2019 onward.
- **Language:** article written in English or Spanish (the dataset may be in any language, e.g., the Chinese benchmark CHASE).
- **Publication type:** full peer-reviewed paper (journal, conference, workshop, including demo tracks) or an arXiv preprint.
- **Full-text-only criteria** — page length (at least 4 pages of content), presence and type of quantitative evaluation, use of a public benchmark, and whether a record is a secondary report of another included study — **must NOT be used to exclude at this title/abstract stage.**

## "Multi-turn" (interpret broadly at screening)
Counts: the **user** asks successive natural-language questions in a dialogue or session, and interpreting a later question depends on earlier user turns or system answers. Terms such as multi-turn, conversational, context-dependent, interactive dialogue, follow-up questions, SParC, CoSQL, CHASE usually signal this. Clarification exchanges **inside** a multi-turn dialogue (as in CoSQL) count.
Does not count on its own: internal rounds of a system on **one** user question (agent–database loops, self-refinement, multi-round reasoning, ReAct-style exploration), even if the paper calls them "multi-turn" or "multi-round"; a system asking for clarification of a single standalone question; using a log of earlier, independent queries as examples. These are **single-turn**.
Exception, treat as unclear: the abstract says "interactive" or "conversational" but does not make clear whether the user asks successive dependent questions.

## "Central contribution" (single-turn studies only)
Counts: schema linking, schema pruning/selection/retrieval, table or column selection, value linking, join-path or foreign-key inference, execution feedback, self-correction, self-debugging, refinement, verification or candidate selection is **stated as a contribution or novelty in the title or abstract**.
Does not count on its own: a general Text-to-SQL system that merely contains such a module, or mentions it in passing.
Exception, treat as unclear: the abstract lists several components and it is not clear whether the linking or correction component is a main contribution.

## Decisions
- "include" (code INC): the task criterion is clearly met **and** scope (a) or (b) is clearly met on the title/abstract.
- "unclear" (code UNC): the task criterion is plausibly met and the scope is plausibly met, but the title/abstract is insufficient, for example: (a) it is unclear whether the setting is multi-turn (see exception above); (b) single-turn study where it is unclear whether linking/correction is a central contribution; (c) unclear whether the target is SQL over a relational database or another formal language; (d) no abstract, but the title suggests Text-to-SQL with a multi-turn, linking or correction focus.
- **Uncertainty rule:** when in doubt about any criterion, choose "unclear"; exclude only when a criterion clearly fails.
- "exclude": give ONE code, the first criterion that clearly fails, checked in this order:
  - **E1 date:** published before 2019 (use the year in the record header).
  - **E2 language:** the record states that the article itself is written in a language other than English or Spanish. An English abstract of a non-English article counts only if the record states the article language.
  - **E3 publication type:** thesis or dissertation, poster, abstract-only or extended abstract, editorial, proceedings front matter or table of contents, complete book.
  - **E4 not a primary study:** survey, literature review, systematic review, tutorial, position or vision paper without its own evaluation.
  - **E5 not Text-to-SQL over relational databases:** knowledge-graph question answering, SPARQL, Cypher or property graphs, NoSQL (e.g., MongoDB), table question answering that does not generate SQL, general code generation, spreadsheets. *Exception: if the study also evaluates on relational SQL, do not use E5.*
  - **E6 single-turn without a central linking/correction contribution:** the study is clearly single-turn and neither schema linking/join inference nor execution feedback/self-correction is a stated contribution (e.g., a general fine-tuning method, prompt format, data augmentation, a new single-turn dataset not about linking or correction, an application or BI system description).
  - **E7 no quantitative evaluation** *(full text only)*.
  - **E8 single-turn without a public benchmark** *(full text only)*.
  - **E9 secondary report of an already included study** *(deduplication / full text only)*.

## Principles
- Sensitive: missing an eligible study is worse than an extra full-text check; when in doubt, "unclear".
- Decisive: most records are clearly irrelevant (e.g., SQL injection security, database tuning, general LLM papers that only mention SQL); "unclear" only when the task and scope criteria are plausibly met.
- Judge the record text only: no recalled knowledge of the paper, no lookups.
- Judge content, not language. Use the publication type and year in the record header for E1 and E3.
- A record that is a survey but relevant is still E4 (it will be used as related work, not as a primary study).

## Amendment log
| Date | Change | Reason | Records to re-screen |
|------|--------|--------|----------------------|
