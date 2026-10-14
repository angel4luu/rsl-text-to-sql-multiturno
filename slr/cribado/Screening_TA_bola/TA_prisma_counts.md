# PRISMA 2020 counts - title/abstract stage

```mermaid
flowchart TD
  I["Records identified from databases (n = 293)<br/>OpenAlex (snowballing) n = 266; Semantic Scholar (snowballing) n = 27"]
  R["Records removed before screening:<br/>duplicate records (n = 1)"]
  S["Records screened (n = 292)"]
  X["Records excluded (n = 207)<br/>E3 Thesis, poster, abstract-only or extended abstract, <4 pages of content, editorial, proceedings front matter, complete book: 3<br/>E4 Not a primary study (survey, review, tutorial, position paper): 21<br/>E5 Not Text-to-SQL over relational databases (KGQA/SPARQL, Cypher, NoSQL, table QA without SQL, general code generation): 7<br/>E6 Single-turn and schema linking / join inference / execution feedback / self-correction is not a stated central contribution: 173<br/>E9 Secondary report of an already included study (deduplication / full text only): 3"]
  F["Reports sought for retrieval (n = 85)"]
  I --> R
  I --> S
  S --> X
  S --> F
```

```json
{
 "stage": "ta",
 "tool": "sr-screener 1.0.0",
 "complete": true,
 "pending_records": 0,
 "state_problems": [],
 "identified_by_database": {
  "OpenAlex (snowballing)": 266,
  "Semantic Scholar (snowballing)": 27
 },
 "identified_total": 293,
 "duplicates_removed": 1,
 "records_screened": 292,
 "records_to_screen": 292,
 "records_excluded": 207,
 "excluded_by_code": {
  "E3": 3,
  "E4": 21,
  "E5": 7,
  "E6": 173,
  "E9": 3
 },
 "reports_sought_for_retrieval": 85,
 "advanced_include": 23,
 "advanced_unclear": 62,
 "advanced_outside_allowed_languages": 0,
 "agreement": {
  "n": 292,
  "both_advance": 63,
  "both_exclude": 212,
  "a_only_advance": 6,
  "b_only_advance": 11,
  "observed_agreement": 0.9418,
  "kappa": 0.843,
  "pabak": 0.884,
  "conflicts": 17,
  "resolved_by": {
   "A+B": 260,
   "AJE": 29,
   "dedup": 3
  }
 },
 "decided_by": {
  "A+B": 260,
  "AJE": 29,
  "dedup": 3
 }
}
```
