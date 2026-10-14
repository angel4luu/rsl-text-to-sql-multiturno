"""Phase 13, step 1b: review sheet for the author from the Codex claim-support verdicts (bib/afirmaciones/runs/).

Only non-obvious cases go to the sheet (memory: hojas-de-revision):
  A. wording where the sentence is stronger than the reference -> a proposed rewording (OK / M / free text);
  B. related-review descriptors the author took from her own reading of each review, which Codex could not see
     (it had the abstract only) -> one confirmation per review (OK / C + note);
  C. information only: flagged claims settled by repository records, and the count of supported claims.
Every flagged claim must fall in exactly one section (checked). Output: bib/afirmaciones/revision_afirmaciones.md.
Usage (from repo root): python3 bib/scripts/hoja_afirmaciones.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
A = RAIZ / "bib" / "afirmaciones"

# A: proposed rewordings (Spanish, as in the article); ids = claims they settle
PROPUESTAS = [
    {"ids": ["Li2020ContextSurvey#2", "Li2020ContextSurvey#3"], "archivo": "secciones/02-trabajos-relacionados.tex, secciones/05-discusion.tex",
     "actual": "«…una revisión narrativa, anterior a los LLM, …» / «…una visión narrativa anterior a los LLM…»",
     "propuesta": "«…anterior a la adopción generalizada de los LLM…» en ambas oraciones (en 2020 ya existían modelos como GPT-3)."},
    {"ids": ["Quamar2022NLI#1", "Shi2026SurveyLLM#1"], "archivo": "secciones/01-introduccion.tex",
     "actual": "«…y la tarea de traducir una pregunta a una consulta SQL (Text-to-SQL) es su formulación computacional más estudiada~[Quamar, Shi].»",
     "propuesta": "«…es una de sus formulaciones computacionales principales…» (ninguna de las dos fuentes afirma que sea la más estudiada)."},
    {"ids": ["Deng2022Recent#2"], "archivo": "tabla «Revisiones previas» (slr/sintesis/tablas/revisiones_previas.csv)",
     "actual": "Tipo = «Narrativa»",
     "propuesta": "Tipo = «Narrativa (se declara sistemática)»: su resumen dice «we … provide this systematic survey», sin protocolo. "
                  "Mantener «Narrativa» también es defendible si el criterio de la tabla es el método y no la autodenominación."},
]
# B: per review, descriptors from the author's own reading (column «Fuente leída»)
REVISIONES = {
    "Li2020ContextSurvey": "Resumen", "Yang2025Conversational": "Resumen", "Abbas2022NLIDB": "Resumen",
    "Katsogiannis2023Survey": "Resumen", "Liu2025SurveyLLMs": "Resumen", "Shi2026SurveyLLM": "Resumen",
    "Liu2026NLIDBReview": "Texto completo (arXiv v2)", "Bui2026Survey": "Texto completo (manuscrito)",
    "OrtizDelgado2026RAG": "Resumen y registro OSF",
}
# C: settled by repository records
REGISTROS = {
    "OSF2026Protocolo": "Registro OSF 2026-10-11 13:09 (commit 52b5042) y búsquedas oficiales confirmadas a las 17:08 "
                        "(commit 970cde1); los conteos de prueba anteriores figuran como «previo al registro» en "
                        "slr/busqueda/registro_busquedas.csv. La afirmación se sostiene con los registros del repositorio.",
}


def main():
    af = {x["id"]: x for x in json.loads((A / "afirmaciones.json").read_text(encoding="utf-8"))}
    juicios = {}
    for f in sorted((A / "runs").glob("*.json")):
        if not f.name.endswith(".error.json"):
            for j in json.loads(f.read_text(encoding="utf-8"))["juicios"]:
                juicios[j["id"]] = j
    assert set(juicios) == set(af), "missing verdicts: run run_afirmaciones_codex.py first"
    marcados = {i for i, j in juicios.items() if j["veredicto"] != "supported"}
    en_a = {i for p in PROPUESTAS for i in p["ids"]}
    en_b = {i for i in marcados - en_a if af[i]["clave"] in REVISIONES}
    en_c = {i for i in marcados if af[i]["clave"] in REGISTROS}
    sin = marcados - en_a - en_b - en_c
    assert not sin, f"flagged claims without a section: {sorted(sin)}"
    assert not (en_a & en_b) and not (en_b & en_c) and not (en_a & en_c)

    L = ["# Hoja de revisión — respaldo de las citas a referencias que no son estudios (fase 13, paso 1b)", "",
         f"Generada por `bib/scripts/hoja_afirmaciones.py`. Codex (`gpt-6.1-sol`, razonamiento medio, solo lectura) juzgó "
         f"{len(af)} oraciones que citan {len({x['clave'] for x in af.values()})} referencias, con el título y el resumen "
         f"de OpenAlex: {sum(j['veredicto'] == 'supported' for j in juicios.values())} respaldadas, "
         f"{sum(j['veredicto'] == 'partial' for j in juicios.values())} parciales y "
         f"{sum(j['veredicto'] == 'cannot_judge' for j in juicios.values())} no evaluables. "
         f"Aquí solo están los casos no obvios: A = {len(PROPUESTAS)}, B = {len({af[i]['clave'] for i in en_b})} revisiones "
         f"({len(en_b)} oraciones); C es informativa.", "",
         "## Cómo responder", "",
         "| Sección | Qué es | Respuestas válidas en `Decisión:` |", "|---|---|---|",
         "| **A** | La oración afirma más que la fuente; hay una redacción propuesta | **OK** = aplicar la propuesta · **M** = mantener el texto actual · o escriba la redacción que prefiera |",
         "| **B** | Descriptores de una revisión previa que usted tomó de su lectura (columna «Fuente leída»); Codex solo vio el resumen | **OK** = lo confirmo contra la fuente · **C** = corregir (añada la nota: `Decisión: C — …`) |",
         "| **C** | Informativa: resuelta con registros del repositorio | (no responder) |", "",
         "Veredictos de Codex: *supported* (respaldada), *partial* (la fuente respalda solo una parte o la oración es más fuerte), "
         "*unsupported* (no coincide), *cannot_judge* (el registro no basta). Las revisiones previas están en Mendeley, carpeta "
         "«9 · Revisiones previas (trabajos relacionados)».", "", "---", "", "## A · Redacción (3)", ""]
    for n, p in enumerate(PROPUESTAS, 1):
        L += [f"### A{n} · {', '.join(p['ids'])}", f"- Archivo: {p['archivo']}", f"- Texto actual: {p['actual']}",
              *[f"- Codex ({juicios[i]['veredicto']}), {i}: {juicios[i]['motivo']}" for i in p["ids"]],
              f"- **Propuesta:** {p['propuesta']}", "", "Decisión: ", ""]
    L += ["---", "", f"## B · Descriptores de revisiones previas ({len({af[i]['clave'] for i in en_b})})", ""]
    for n, clave in enumerate(k for k in REVISIONES if any(af[i]["clave"] == k for i in en_b)):
        L += [f"### B{n + 1} · {clave} — fuente leída: {REVISIONES[clave]}"]
        for i in sorted((i for i in en_b if af[i]["clave"] == clave), key=lambda x: int(x.split("#")[1])):
            L += [f"- **{i}** ({af[i]['archivo']}): {af[i]['oracion']}",
                  f"  - Codex ({juicios[i]['veredicto']}): {juicios[i]['motivo']}"]
        L += ["", "Decisión: ", ""]
    L += ["---", "", "## C · Informativa", ""]
    for clave, texto in REGISTROS.items():
        L += [f"- **{clave}** ({', '.join(sorted(i for i in en_c if af[i]['clave'] == clave))}): {texto}"]
    L += [f"- Respaldadas sin observaciones: {len(af) - len(marcados)} oraciones (detalle en `bib/afirmaciones/runs/`).", ""]
    (A / "revision_afirmaciones.md").write_text("\n".join(L), encoding="utf-8")
    print(f"sheet: A {len(PROPUESTAS)}, B {len({af[i]['clave'] for i in en_b})} reviews / {len(en_b)} claims, "
          f"C {len(en_c)}; lines {len(L)}")


if __name__ == "__main__":
    main()
