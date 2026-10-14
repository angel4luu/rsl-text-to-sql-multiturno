"""Phase 13, step 1a: deterministic citation-integrity check of the SLR article (no language model involved).

For every key cited in latex/slr/main.pdf (read from main.aux, so the appendices are included):
  A. the key exists in exactly one bib file, and biber/LaTeX report no missing or undefined citation;
  B. the entry is verified: by an earlier record (claves_estudios.csv for included studies, verificacion_citas.csv for
     methods references), by an author decision recorded in revision_citas.md (entries without DOI), or, if neither,
     live now against OpenAlex by DOI (title similarity >= 0.90 and year within one year);
  C. the fields IEEE style needs for its entry type are present (a missing DOI/URL is only noted);
  D. no two entries in the bib files share a DOI or a normalised title;
  E. no two included studies map to the same entry.
Outputs: bib/verificacion_citas_fase13.csv (one row per cited key) and bib/verificacion_citas_fase13.md (report).
Usage (from repo root, after `make slr`): python3 bib/scripts/verificar_citas.py
"""
import csv
import difflib
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BIB = RAIZ / "bib"
SLR = RAIZ / "latex" / "slr"
ARCHIVOS = ["referencias.bib", "referencias_metodo.bib", "estudios_incluidos.bib"]
MANUALES = {"Kitchenham2007Guidelines": "C1 (revision_citas.md): @techreport verificado por la autora contra su copia",
            "TCS2026": "C4 (revision_citas.md): URL verificada por HTTP 200 el 2026-10-13",
            "ARS2026": "Software: repositorio público de la suite (URL)"}
REQUERIDOS = {"article": ["author", "title", "journal|journaltitle", "year|date"],
              "inproceedings": ["author", "title", "booktitle", "year|date"],
              "incollection": ["author", "title", "booktitle", "year|date"],
              "techreport": ["author", "title", "institution", "year|date"],
              "misc": ["author|title", "year|date"], "online": ["title", "url"], "software": ["title", "url"],
              "book": ["author|editor", "title", "publisher", "year|date"]}
CORREO = "mailto=angela.jara@unmsm.edu.pe"  # OpenAlex polite pool (author's institutional address, as in the article)


def campos(cuerpo):
    """BibTeX fields with nested braces."""
    out, i = {}, 0
    for m in re.finditer(r"(\w+)\s*=\s*", cuerpo):
        if m.start() < i:
            continue
        j = m.end()
        if j < len(cuerpo) and cuerpo[j] == "{":
            d, k = 0, j
            while k < len(cuerpo):
                d += {"{": 1, "}": -1}.get(cuerpo[k], 0)
                if d == 0:
                    break
                k += 1
            out[m.group(1).lower()] = cuerpo[j + 1:k]
            i = k
        else:
            v = re.match(r'"([^"]*)"|([^,\n]+)', cuerpo[j:])
            out[m.group(1).lower()] = (v.group(1) or v.group(2) or "").strip()
            i = j + v.end()
    return out


def leer_bib():
    entradas = defaultdict(list)
    for f in ARCHIVOS:
        t = (BIB / f).read_text(encoding="utf-8")
        for m in re.finditer(r"^@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)(?=^@|\Z)", t, re.M | re.S):
            entradas[m.group(2)].append({"tipo": m.group(1).lower(), "archivo": f, **campos(m.group(3))})
    return entradas


def norm(s):
    s = unicodedata.normalize("NFKD", re.sub(r"\\[a-zA-Z]+|[{}\\'`^\"~]", "", s or ""))
    s = re.sub(r"[^a-z0-9 ]", "", s.encode("ascii", "ignore").decode().lower())
    return re.sub(r"\s+", " ", s).strip()


def openalex(doi):
    url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi.lower())}?{CORREO}"
    for intento in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(2 * (intento + 1))
        except OSError:
            time.sleep(2 * (intento + 1))
    return None


def main():
    aux = (SLR / "main.aux").read_text(encoding="utf-8", errors="replace")
    citadas = sorted(set(re.findall(r"\\abx@aux@cite\{0\}\{([^}]+)\}", aux)))
    entradas = leer_bib()
    estudios = {r["clave_bib"]: r for r in csv.DictReader(open(BIB / "claves_estudios.csv", encoding="utf-8"))}
    metodo = {r["clave"]: r for r in csv.DictReader(open(BIB / "verificacion_citas.csv", encoding="utf-8"))}
    blg = (SLR / "main.blg").read_text(encoding="utf-8", errors="replace")
    log = (SLR / "main.log").read_text(encoding="utf-8", errors="replace")
    avisos_biber = [l for l in blg.splitlines() if re.search(r"WARN|ERROR", l)]
    indefinidas = re.findall(r"Citation `([^']+)' .*undefined", log)

    filas, problemas, notas = [], [], []
    for k in citadas:
        e = entradas.get(k, [])
        fila = {"clave": k, "archivo": "", "tipo": "", "verificacion": "", "detalle": "", "campos_faltantes": ""}
        if len(e) != 1:
            problemas.append(f"A · `{k}`: {'no existe' if not e else 'duplicada en ' + ', '.join(x['archivo'] for x in e)}")
            fila["verificacion"] = "FALLA"
            filas.append(fila)
            continue
        e = e[0]
        fila.update(archivo=e["archivo"], tipo=e["tipo"])
        # B. verification
        if k in estudios and estudios[k]["estado"] == "ok":  # "existente" = entry in referencias.bib, checked live below
            fila.update(verificacion="registro previo", detalle=f"claves_estudios.csv ({estudios[k]['fuente']})")
        elif k in metodo and metodo[k]["estado"] == "ok":
            fila.update(verificacion="registro previo", detalle=f"verificacion_citas.csv ({metodo[k]['fuente']})")
        elif k in MANUALES:
            fila.update(verificacion="decisión de la autora", detalle=MANUALES[k])
        elif e.get("doi"):
            doi = e["doi"].replace("\\_", "_")
            w = openalex(doi)
            time.sleep(0.2)
            if not w:
                fila.update(verificacion="FALLA", detalle=f"DOI {doi} no encontrado en OpenAlex")
                problemas.append(f"B · `{k}`: DOI {doi} no encontrado en OpenAlex")
            else:
                sim = difflib.SequenceMatcher(None, norm(e.get("title")), norm(w.get("title"))).ratio()
                anio_bib = re.search(r"\d{4}", e.get("year") or e.get("date") or "")
                dif = abs(int(anio_bib.group()) - (w.get("publication_year") or 0)) if anio_bib else 99
                ok = sim >= 0.90 and dif <= 1
                fila.update(verificacion="OpenAlex por DOI" if ok else "FALLA",
                            detalle=f"similitud del título {sim:.2f}; año bib {anio_bib.group() if anio_bib else '?'} / "
                                    f"OpenAlex {w.get('publication_year')}")
                if not ok:
                    problemas.append(f"B · `{k}`: {fila['detalle']} (OpenAlex: «{w.get('title')}»)")
        else:
            fila.update(verificacion="FALLA", detalle="sin registro de verificación ni DOI")
            problemas.append(f"B · `{k}`: sin registro de verificación ni DOI")
        # C. fields
        falt = [r for r in REQUERIDOS.get(e["tipo"], ["title"]) if not any(e.get(c) for c in r.split("|"))]
        if not (e.get("doi") or e.get("url")):
            notas.append(f"`{k}` (@{e['tipo']}): sin DOI ni URL; se identifica por título y foro ({fila['detalle']})")
        if falt:
            fila["campos_faltantes"] = "; ".join(falt)
            problemas.append(f"C · `{k}` (@{e['tipo']}): faltan {', '.join(falt)}")
        filas.append(fila)

    # D. duplicates across all bib entries (cited or not)
    por_doi, por_titulo = defaultdict(set), defaultdict(set)
    for k, es in entradas.items():
        for e in es:
            if e.get("doi"):
                por_doi[e["doi"].lower().replace("\\_", "_")].add(k)
            if len(norm(e.get("title"))) > 20:
                por_titulo[norm(e.get("title"))].add(k)
    duplicados = [f"D · DOI {d}: {', '.join(sorted(ks))}" for d, ks in por_doi.items() if len(ks) > 1]
    duplicados += [f"D · título «{t[:60]}…»: {', '.join(sorted(ks))}" for t, ks in por_titulo.items() if len(ks) > 1]
    problemas += duplicados
    # E. two included-study IDs mapped to one entry = the same paper counted twice
    por_clave = defaultdict(list)
    incluidos = {r["id_estudio"] for r in csv.DictReader(open(BIB.parent / "slr" / "extraccion" / "extraccion.csv", encoding="utf-8"))}
    for r in csv.DictReader(open(BIB / "claves_estudios.csv", encoding="utf-8")):
        if r["id_estudio"] in incluidos:  # E9 secondary reports keep their key row but are not studies
            por_clave[r["clave_bib"]].append(r["id_estudio"])
    problemas += [f"E · `{k}`: un mismo informe para los estudios incluidos {', '.join(v)} (posible duplicado no "
                  "eliminado)" for k, v in por_clave.items() if len(v) > 1]
    problemas += [f"A · biber: {l.strip()}" for l in avisos_biber] + [f"A · LaTeX: cita indefinida `{k}`" for k in indefinidas]

    with open(BIB / "verificacion_citas_fase13.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    cuenta = defaultdict(int)
    for f in filas:
        cuenta[f["verificacion"]] += 1
    n_estudios = sum(1 for k in citadas if k in estudios)
    informe = [
        "# Verificación de citas — fase 13, paso 1a (determinista)", "",
        "Generado por `bib/scripts/verificar_citas.py` sobre `latex/slr/main.aux` (artículo y apéndices).", "",
        f"- Claves citadas: {len(citadas)} (estudios incluidos: {n_estudios} de {len(estudios)}; otras referencias: "
        f"{len(citadas) - n_estudios}).",
        "- Verificación: " + "; ".join(f"{k}: {v}" for k, v in sorted(cuenta.items())) + ".",
        f"- Avisos de biber: {len(avisos_biber)}; citas indefinidas en LaTeX: {len(indefinidas)}.",
        f"- Entradas de los archivos .bib: {sum(len(v) for v in entradas.values())}; duplicados por DOI o título: "
        f"{len(duplicados)}.", "",
        f"## Problemas ({len(problemas)})", ""] + ([f"- {p}" for p in problemas] or ["Ninguno."]) + [
        "", f"## Notas informativas ({len(notas)})", ""] + [f"- {n}" for n in notas] + [
        "", "Detalle por clave: `bib/verificacion_citas_fase13.csv`."]
    (BIB / "verificacion_citas_fase13.md").write_text("\n".join(informe) + "\n", encoding="utf-8")
    print("\n".join(informe[4:]))


if __name__ == "__main__":
    main()
