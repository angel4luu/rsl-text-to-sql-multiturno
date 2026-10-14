"""Figure: records identified per source and included studies retrieved by each source (database arm).

Sources per record: cribado/sr_work/records.json (sources of each unique record after the tool's de-duplication)
plus busqueda/dedup_versiones_log.csv (the arXiv preprint versions and wrong-DOI Scopus records removed before the
tool: their source is added to the kept record). Included studies: extraccion/base_estudios.csv (origen = busqueda).
A study retrieved by several sources counts in each; «solo esta fuente» = retrieved by that source only.
Writes latex/slr/figuras/busqueda_fuentes.pdf and slr/sintesis/tablas/busqueda_fuentes.csv.
"""
import csv
import json

import matplotlib.pyplot as plt
import numpy as np

from comun import SLR
from estilo import ANCHO_COLUMNA, PALETA, aplicar_estilo, guardar

ORDEN = ["Scopus", "IEEE Xplore", "ACM DL", "ACL Anthology", "arXiv"]


def main():
    recs = json.load(open(SLR / "cribado" / "sr_work" / "records.json", encoding="utf-8"))["unique"]
    fuentes = {r["id"]: set(r["sources"]) for r in recs}
    por_doi = {(r.get("doi") or "").lower(): r["id"] for r in recs if r.get("doi")}
    for v in csv.DictReader(open(SLR / "busqueda" / "dedup_versiones_log.csv", encoding="utf-8")):
        if v["regla"] in ("preprint_de_version_publicada", "doi_erroneo_scopus"):
            rid = por_doi.get(v["doi_conservado"].lower())
            if rid:
                fuentes[rid].add(v["base_descartada"])
    ident = json.load(open(SLR / "cribado" / "prisma_identificacion.json", encoding="utf-8"))["registros_identificados"]
    incl = [r["id_cribado"] for r in csv.DictReader(open(SLR / "extraccion" / "base_estudios.csv", encoding="utf-8"))
            if r["origen"] == "busqueda"]
    assert all(i in fuentes for i in incl)
    filas = []
    for b in ORDEN:
        n_incl = sum(b in fuentes[i] for i in incl)
        solo = sum(fuentes[i] == {b} for i in incl)
        filas.append({"fuente": b, "identificados": ident[b], "incluidos": n_incl, "solo_esta_fuente": solo})
    with open(SLR / "sintesis" / "tablas" / "busqueda_fuentes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)

    aplicar_estilo()
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.6))
    y = np.arange(len(filas))[::-1]
    h = 0.38
    ax.barh(y + h / 2, [f["identificados"] for f in filas], h, color=PALETA[5], label="Registros identificados")
    ax.barh(y - h / 2, [f["incluidos"] for f in filas], h, color=PALETA[0], label="Estudios incluidos recuperados")
    ax.barh(y - h / 2, [f["solo_esta_fuente"] for f in filas], h, color=PALETA[1], label="… solo por esta fuente")
    for yi, f in zip(y, filas):
        ax.text(f["identificados"] + 6, yi + h / 2, str(f["identificados"]), va="center", fontsize=6.5)
        ax.text(f["incluidos"] + 6, yi - h / 2, f"{f['incluidos']} ({f['solo_esta_fuente']})", va="center", fontsize=6.5)
    ax.set_yticks(y, [f["fuente"] for f in filas])
    ax.set_xlabel("Registros o estudios")
    ax.set_xlim(0, max(f["identificados"] for f in filas) * 1.15)
    ax.legend(loc="lower left", bbox_to_anchor=(-0.02, 1.0), ncol=2, fontsize=6.5, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    guardar(fig, "busqueda_fuentes", leyenda=(
        "Registros identificados por fuente y estudios incluidos (brazo de bases) recuperados por cada fuente; entre "
        "paréntesis, los recuperados solo por esa fuente. Un estudio recuperado por varias fuentes cuenta en cada una; "
        "a cada registro conservado se le suman las fuentes de las versiones eliminadas antes del cribado."))
    print(filas)


if __name__ == "__main__":
    main()
