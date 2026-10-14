"""Phase 13, step 1b (no language model involved): claims that cite a non-study reference, for a claim-support check.

Non-study references = keys cited in the article (bib/verificacion_citas_fase13.csv, from step 1a) that are not
included studies (bib/claves_estudios.csv). For each one:
  - every sentence of latex/slr (sections, tables, appendices, figure captions) that cites it, with the previous
    sentence as context (comments removed, LaTeX kept as written);
  - the reference's title, type, venue and year from the .bib files, and its abstract from OpenAlex by DOI
    (cached in bib/afirmaciones/openalex_cache.json; no DOI or no abstract -> stated as such, never filled in).
Outputs (bib/afirmaciones/): afirmaciones.json (all claims, id = <key>#<n>) and prompts/<key>.md (one prompt per
reference for bib/scripts/run_afirmaciones_codex.py).
Usage (from repo root, after `make slr` and verificar_citas.py): python3 bib/scripts/extraer_afirmaciones.py
"""
import csv
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verificar_citas import BIB, SLR, leer_bib, openalex  # noqa: E402

OUT = BIB / "afirmaciones"
FUENTES_TEX = ["secciones", "tablas", "apendices", "figuras/tex"]
CITA = re.compile(r"\\(?:cite|citep|citet|parencite|textcite)\*?(?:\[[^\]]*\])*\{([^}]*)\}")
# abbreviations that end with a period but do not end a sentence
ABREV = [r"p\.\\,ej\.", r"p\. ej\.", r"et~al\.", r"et al\.", r"cf\.", r"vs\.", r"i\.\\,e\.", r"e\.\\,g\.", r"núm\.", r"Fig\.", r"pp\."]
PROMPT = """# Claim-support check (systematic review article, Spanish)

You check whether a cited reference supports the sentences of a published-style article that cite it.
You have no tools to use: judge only from the reference record below and your general knowledge of this
well-known reference, and say so when you rely on knowledge beyond the abstract.

## Reference `{clave}`
- Type: {tipo}
- Title: {titulo}
- Authors: {autores}
- Venue / year: {venue} ({anio})
- DOI / URL: {doi}
- Abstract (OpenAlex): {resumen}

## Sentences that cite it
Each item: id, file, the previous sentence (context only) and the citing sentence (LaTeX kept; `\\nX{{}}` macros are
generated numbers from the review's own data, not claims about the reference).

{items}

## Task
For each id decide what the citation is used for and whether the reference supports that use:
- `supported`: the reference states or clearly establishes what the sentence attributes to it (or it is cited as
  the source of a method, tool, dataset, guideline or statistic that the reference is);
- `partial`: the reference supports part of the attribution, or the sentence is stronger/more specific than the
  reference (e.g., a number, a generalisation, a causal claim);
- `unsupported`: the attribution does not match the reference;
- `cannot_judge`: the record and your knowledge are not enough to decide.
Judge only what the sentence attributes to this reference, not the review's own findings in the same sentence.

Return only this JSON object, one entry per id, nothing else:
{{"clave": "{clave}", "juicios": [{{"id": "<id>", "uso": "<what the citation is used for, <= 15 words>", "veredicto": "supported|partial|unsupported|cannot_judge", "motivo": "<one sentence, English>", "conocimiento_externo": true|false}}]}}
"""


def limpiar(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    return t


def oraciones(parrafo):
    s = parrafo
    for i, a in enumerate(ABREV):
        s = re.sub(a, f"@@ABR{i}@@", s)
    partes = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿\\])|\\item\s+", s)
    out = []
    for p in partes:
        for i, a in enumerate(ABREV):
            p = p.replace(f"@@ABR{i}@@", a.replace("\\\\", "\\").replace("\\.", "."))
        p = re.sub(r"\s+", " ", p).strip()
        if p:
            out.append(p)
    return out


def resumen_openalex(w):
    inv = (w or {}).get("abstract_inverted_index")
    if not inv:
        return None
    pos = sorted((i, pal) for pal, idx in inv.items() for i in idx)
    return " ".join(p for _, p in pos)


def main():
    estudios = {r["clave_bib"] for r in csv.DictReader(open(BIB / "claves_estudios.csv", encoding="utf-8"))}
    claves = [r["clave"] for r in csv.DictReader(open(BIB / "verificacion_citas_fase13.csv", encoding="utf-8"))
              if r["clave"] not in estudios]
    bib = leer_bib()
    # sentences citing each key
    usos = {k: [] for k in claves}
    for carpeta in FUENTES_TEX:
        for f in sorted((SLR / carpeta).glob("*.tex")):
            texto = limpiar(f.read_text(encoding="utf-8"))
            for parrafo in re.split(r"\n\s*\n", texto):
                if "&" in parrafo and "\\\\" in parrafo:  # table: one unit per row, context = caption + header row
                    filas = [re.sub(r"\s+", " ", x).strip() for x in re.split(r"\\\\", parrafo)]
                    cap = re.search(r"\\caption\{(.*?)\}\s*\n", parrafo, re.S)
                    cab = next((x.split("\\toprule")[-1].strip() for x in filas if "&" in x and not CITA.search(x)), "")
                    ors = [x for x in filas if CITA.search(x)]
                    ctx = [f"Table caption: {cap.group(1) if cap else '(none)'} Header: {cab}"] * len(ors)
                else:
                    ors = oraciones(parrafo)
                    ctx = [""] + ors[:-1]
                for o, c in zip(ors, ctx):
                    citadas = {c_.strip() for m in CITA.finditer(o) for c_ in m.group(1).split(",")}
                    for k in citadas & set(claves):
                        usos[k].append({"archivo": f"{carpeta}/{f.name}", "contexto": c, "oracion": o})
    OUT.mkdir(exist_ok=True)
    (OUT / "prompts").mkdir(exist_ok=True)
    cache_p = OUT / "openalex_cache.json"
    cache = json.loads(cache_p.read_text(encoding="utf-8")) if cache_p.exists() else {}
    todas, sin_uso = [], []
    for k in claves:
        e = bib[k][0]
        doi = (e.get("doi") or "").strip()
        if doi and doi not in cache:
            w = openalex(doi)
            cache[doi] = {"resumen": resumen_openalex(w), "titulo_openalex": (w or {}).get("display_name")}
            time.sleep(0.2)
        resumen = cache.get(doi, {}).get("resumen") if doi else None
        if not usos[k]:
            sin_uso.append(k)
            continue
        items = []
        for n, u in enumerate(usos[k], 1):
            u.update(id=f"{k}#{n}", clave=k)
            todas.append(u)
            items.append(f"- **{u['id']}** ({u['archivo']})\n  - context: {u['contexto'] or '(none)'}\n  - sentence: {u['oracion']}")
        (OUT / "prompts" / f"{k}.md").write_text(PROMPT.format(
            clave=k, tipo=e["tipo"], titulo=re.sub(r"[{}]", "", e.get("title", "")),
            autores=re.sub(r"\s+", " ", e.get("author", "(none)")), venue=e.get("journal") or e.get("booktitle")
            or e.get("institution") or e.get("publisher") or e.get("howpublished") or "(none)",
            anio=e.get("year") or e.get("date") or "?", doi=doi or e.get("url") or "(none)",
            resumen=resumen or ("(no DOI)" if not doi else "(OpenAlex has no abstract)"),
            items="\n".join(items)), encoding="utf-8")
    cache_p.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / "afirmaciones.json").write_text(json.dumps(todas, indent=1, ensure_ascii=False), encoding="utf-8")
    con_resumen = sum(1 for k in claves if (bib[k][0].get("doi") or "").strip() and cache.get(bib[k][0]["doi"].strip(), {}).get("resumen"))
    print(f"references: {len(claves)}; with OpenAlex abstract: {con_resumen}; claims: {len(todas)}; "
          f"prompts: {len(claves) - len(sin_uso)}")
    if sin_uso:
        print("cited only outside the scanned .tex (check by hand):", ", ".join(sin_uso))


if __name__ == "__main__":
    main()
