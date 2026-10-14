"""Manual retrieval sheet for the records the scripts could not retrieve (retrieval_log.csv).

Priority 1 = multi-turn signal in title/abstract (future Level 2: every one matters);
priority 2 = single-turn. Within each, records are grouped by source; open-access publishers that block
scripts (MDPI, PVLDB) and ACM come first, because a browser download is often enough.
Writes pendientes_recuperacion.md. Usage (from slr/texto_completo): python scripts/hoja_pendientes.py
"""
import argparse
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..")
KW = ["multi-turn", "multi turn", "conversational", "context-dependent", "sparc", "cosql", "dialogue", "dialog"]
ROUTE = {"10.3390": "Navegador (MDPI, acceso abierto)", "10.14778": "Navegador (PVLDB, acceso abierto: vldb.org)",
         "10.1145": "Navegador (ACM DL; muchos son de acceso abierto) o biblioteca UNMSM",
         "10.1109": "Biblioteca UNMSM (IEEE Xplore)", "10.1007": "Biblioteca UNMSM (Springer)",
         "10.1016": "Biblioteca UNMSM (Elsevier/ScienceDirect)"}
BROWSER = ("10.3390", "10.14778")
SOURCE = {"10.3390": "MDPI", "10.14778": "PVLDB", "10.1145": "ACM", "10.1109": "IEEE", "10.1007": "Springer",
          "10.1016": "Elsevier"}
ORDER = ["MDPI", "PVLDB", "ACM", "IEEE", "Springer", "Elsevier", "Otras editoriales", "Sin DOI"]


def local_path(value):
    return value if os.path.isabs(value) else os.path.abspath(os.path.join(T, value))


def source(pre):
    return SOURCE.get(pre) or ("Sin DOI" if not pre else "Otras editoriales")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default="../cribado/sr_work")
    ap.add_argument("--log", default="retrieval_log.csv")
    ap.add_argument("--out", default="pendientes_recuperacion.md")
    ap.add_argument("--pdf-dir", default="pdf")
    args = ap.parse_args()
    work, log, out_path, pdf_dir = map(local_path, (args.work, args.log, args.out, args.pdf_dir))
    recs = {r["id"]: r for r in json.load(open(os.path.join(work, "records.json")))["unique"]}
    rows = [r for r in csv.DictReader(open(log, encoding="utf-8"))
            if r["status"] != "recuperado"]

    def info(r):
        rec = recs[r["id"]]
        text = ((rec.get("title") or "") + " " + (rec.get("abstract") or "")).lower()
        pre = (r["doi"] or "").split("/")[0]
        return (0 if any(k in text for k in KW) else 1, ORDER.index(source(pre)), r["id"]), pre, rec

    items = sorted((info(r) + (r,) for r in rows), key=lambda x: x[0])
    p1 = sum(1 for k, *_ in items if k[0] == 0)
    out = ["# Textos completos pendientes de recuperar", "",
           f"Generado por `scripts/hoja_pendientes.py` desde `{os.path.basename(log)}`: {len(items)} registros "
           f"(prioridad 1, multiturno: {p1}; prioridad 2, un turno: {len(items) - p1}).", "",
           "## Cómo hacerlo",
           "1. Abra el enlace DOI y descargue el PDF (en un navegador o con el acceso de la biblioteca UNMSM).",
           f"2. Guárdelo en `slr/texto_completo/{os.path.basename(pdf_dir)}/` con el **ID del registro como nombre**: `R00123.pdf`.",
           "3. Si no lo consigue, marque la casilla y escriba el motivo (p. ej. `sin acceso`); no hace falta guardar nada.",
           "4. Avíseme: vuelvo a ejecutar `recuperar.py`, que registra los PDF manuales como «manual (autora)».", "",
           "Empiece por la **prioridad 1**: esos estudios forman el Nivel 2 (revisión en profundidad).", ""]
    cur, cur_src = None, None
    for key, pre, rec, r in items:
        if key[0] != cur:
            cur, cur_src = key[0], None
            out += ["", "## Prioridad 1 — señal multiturno" if cur == 0 else "## Prioridad 2 — un turno"]
        if key[1] != cur_src:
            cur_src = key[1]
            n_src = sum(1 for k, *_ in items if k[0] == cur and k[1] == cur_src)
            out += ["", f"### {ORDER[cur_src]} ({n_src})", "",
                    "| ✔ | ID | Año | Título | DOI | Ruta sugerida | Nota |", "|---|---|---|---|---|---|---|"]
        doi = f"[{r['doi']}](https://doi.org/{r['doi']})" if r["doi"] else "—"
        title = (rec.get("title") or "").replace("|", "/")
        route = ROUTE.get(pre, "Buscar el título en Google Scholar" if not r["doi"] else "Enlace DOI / biblioteca UNMSM")
        out.append(f"| ☐ | {r['id']} | {r['year']} | {title} | {doi} | {route} | |")
    open(out_path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"{os.path.basename(out_path)}: {len(items)} (priority 1: {p1})")


if __name__ == "__main__":
    main()
