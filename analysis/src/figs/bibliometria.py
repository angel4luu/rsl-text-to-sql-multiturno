"""Phase 10 — exploratory descriptive bibliometrics (amendment A6; not pre-registered, changes no conclusion).

1 citation network among included studies   2 citations per year since publication (+ percentile within year)
3 countries, institutions, industry vs academia   4 research community of the venue (NLP / databases / ML-AI / ...)
5 base-model families over time   6 co-occurrence of PI3/PI4 technique codes
Inputs: slr/extraccion/extraccion.csv, slr/sintesis/datos/openalex_estudios.jsonl (collection date inside).
Outputs: slr/sintesis/tablas/bib_*.csv, slr/sintesis/bibliometria_resultados.json, latex/slr/figuras/bib_*.pdf.
"""
import collections
import itertools
import json
import re

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from comun import SLR, escribir_tabla, estudios, lista
from estilo import ANCHO_COLUMNA, ANCHO_PAGINA, PALETA, aplicar_estilo, guardar

ANIOS = list(range(2019, 2027))
COMUNIDAD = [  # (label, regex on venue) — first match wins
    ("PLN", r"association for computational linguistics|\bacl\b|emnlp|empirical methods|naacl|eacl|coling|findings|tacl|conll|semeval|lrec|computational linguistics|\bacl anthology"),
    ("Bases de datos", r"sigmod|management of data|pacmmod|vldb|\bicde\b|data engineering|edbt|extending database|dasfaa|cikm|information and knowledge management|tkde|knowledge and data engineering|very large data"),
    ("Aprendizaje automático / IA", r"\biclr\b|learning representations|neurips|neural information processing|\bicml\b|machine learning|\baaai\b|artificial intelligence|ijcai|\bkdd\b|knowledge discovery"),
]
FAMILIAS = [("GPT", r"gpt|chatgpt|codex|o1|o3|o4-mini"), ("Claude", r"claude"), ("Gemini/PaLM", r"gemini|palm|bard"),
            ("LLaMA/CodeLlama", r"llama"), ("Qwen", r"qwen"), ("DeepSeek", r"deepseek"), ("Mistral", r"mistral|mixtral"),
            ("T5", r"\bt5|picard|flan"), ("BERT/RoBERTa/ELECTRA", r"bert|electra|grappa|tapas"), ("BART", r"bart"),
            ("Pre-PLM (LSTM/GloVe)", r"lstm|glove|gru\b|seq2seq")]


CORTOS = {"R00124": "RAT-SQL", "R00127": "IRNet", "R00109": "PICARD", "B00042": "BRIDGE", "R00131": "EditSQL",
          "B00012": "LGESQL", "R00126": "SParC", "R00129": "CoSQL", "R00117": "IGSQL", "R00110": "CHASE", "B00043": "Global-GNN"}
PAISES = {"CN": "China", "US": "EE. UU.", "HK": "Hong Kong", "KR": "Corea del Sur", "CA": "Canadá", "GB": "Reino Unido",
          "IN": "India", "SG": "Singapur", "DE": "Alemania", "JP": "Japón", "AU": "Australia", "FR": "Francia", "IT": "Italia",
          "TW": "Taiwán", "BR": "Brasil", "ES": "España", "NL": "Países Bajos", "CH": "Suiza", "IL": "Israel", "MO": "Macao"}
TEC = {"PODA_ESQUEMA": "Poda de esquema", "EMBEDDINGS_RECUPERACION": "Recuperación por embeddings",
       "LLM_PROMPTING": "Vinculación por prompting", "CLASIFICADOR_ENTRENADO": "Clasificador entrenado",
       "GRAFO_ESQUEMA": "Grafo de esquema", "COINCIDENCIA_CADENAS": "Coincidencia de cadenas",
       "NINGUNA_EXPLICITA": "Sin vinculación explícita", "EJECUCION_FEEDBACK_ERRORES": "Retroalimentación de ejecución",
       "AUTODEPURACION_LLM": "Autodepuración con LLM", "AUTOCONSISTENCIA_VOTACION": "Autoconsistencia / votación",
       "VERIFICADOR_CRITICO": "Verificador / crítico", "REPARACION_SIMBOLICA": "Reparación simbólica",
       "ACLARACION_USUARIO": "Aclaración al usuario", "ABSTENCION": "Abstención"}


def corto(sid, E):
    if sid in CORTOS:
        return CORTOS[sid]
    t = E[sid]["titulo"]
    return t.split(":")[0][:18] if ":" in t else " ".join(t.split()[:2])


def comunidad(r):
    v = (r["venue"] or "").lower()
    if r["foro_tipo"] == "PREPRINT":
        return "Preprint"
    for lab, rx in COMUNIDAD:
        if re.search(rx, v):
            return lab
    return "Otra"


def main():
    E = {r["id_estudio"]: r for r in estudios()}
    for r in E.values():
        r["_mt"] = str(r["nivel"]) == "2"
        r["_anio"] = int(str(r["anio"])[:4]) if str(r["anio"])[:4].isdigit() else None
    oa = {}
    fecha = None
    for line in open(SLR / "sintesis" / "datos" / "openalex_estudios.jsonl", encoding="utf-8"):
        j = json.loads(line)
        fecha = j["fecha"]
        if j["work"] and j["id_estudio"] in E:  # secondary reports (E9) are not studies
            oa[j["id_estudio"]] = j["work"]
    aplicar_estilo()
    res = {"fecha_openalex": fecha, "resueltos_openalex": len(oa), "no_resueltos": sorted(set(E) - set(oa)), "n_estudios": len(E)}

    # 1 citation network
    wid = {w["id"]: sid for sid, w in oa.items()}
    G = nx.DiGraph()
    G.add_nodes_from(E)
    for sid, w in oa.items():
        for ref in w.get("referenced_works") or []:
            if ref in wid and wid[ref] != sid:
                G.add_edge(sid, wid[ref])
    indeg = dict(G.in_degree())
    top = sorted(indeg.items(), key=lambda x: -x[1])[:10]
    escribir_tabla("bib_red_top", [{"id_estudio": s, "citas_en_red": c, "escenario": "MULTITURNO" if E[s]["_mt"] else "UN_TURNO",
                                    "anio": E[s]["anio"], "titulo": E[s]["titulo"][:100]} for s, c in top],
                   ["id_estudio", "citas_en_red", "escenario", "anio", "titulo"])
    cruz = collections.Counter(("MT" if E[a]["_mt"] else "UT") + "→" + ("MT" if E[b]["_mt"] else "UT") for a, b in G.edges())
    res["red"] = {"nodos": G.number_of_nodes(), "aristas": G.number_of_edges(), "aislados": sum(1 for n in G if G.degree(n) == 0),
                  "citas_por_direccion": dict(cruz)}
    H = G.subgraph([n for n in G if G.degree(n) > 0])
    pos = nx.spring_layout(H.to_undirected(), seed=2026, k=0.35)
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA, 4.6))
    nx.draw_networkx_edges(H, pos, ax=ax, alpha=0.10, width=0.3, arrows=False, edge_color="#555555")
    for mt, col, lab in ((False, PALETA[0], "Un turno"), (True, PALETA[1], "Multiturno")):
        ns = [n for n in H if E[n]["_mt"] == mt]
        nx.draw_networkx_nodes(H, pos, nodelist=ns, node_size=[8 + 5 * indeg[n] for n in ns], node_color=col, ax=ax, label=lab,
                               linewidths=0.4, edgecolors="white")
    xs = np.array([p[0] for p in pos.values()])
    ys_ = np.array([p[1] for p in pos.values()])
    cx = float(np.median([pos[t][0] for t, _ in top[:8]]))
    lados = {"izq": [], "der": []}
    for s, c in top[:8]:
        lados["izq" if pos[s][0] < cx else "der"].append((s, c))
    for lado, items in lados.items():
        items.sort(key=lambda t: -pos[t[0]][1])
        yl = np.linspace(ys_.max(), ys_.min(), len(items) + 2)[1:-1] if items else []
        xl = xs.min() - 0.15 if lado == "izq" else xs.max() + 0.15
        for (s, c), y in zip(items, yl):
            ax.annotate(f"{corto(s, E)} ({c})", pos[s], xytext=(xl, y), fontsize=6.5, va="center",
                        ha="right" if lado == "izq" else "left",
                        arrowprops=dict(arrowstyle="-", lw=0.4, color="#444444", shrinkA=0, shrinkB=2))
    ax.margins(x=0.32, y=0.05)
    leg = ax.legend(loc="lower left", markerscale=0.8, title="Escenario (tamaño = citas recibidas en la red)", title_fontsize=6.5)
    leg._legend_box.align = "left"
    ax.axis("off")
    guardar(fig, "bib_red_citas", leyenda="Red de citas entre los estudios incluidos con al menos un vínculo "
            f"({H.number_of_nodes()} de {G.number_of_nodes()} estudios; {G.number_of_edges()} citas; fuente: OpenAlex, {fecha}). "
            "Etiquetas: los ocho estudios más citados dentro de la red, con su número de citas. Análisis exploratorio (A6).")

    # 2 citations per year since publication + percentile within year
    filas = []
    for sid, w in oa.items():
        y = w.get("publication_year") or E[sid]["_anio"]
        edad = max(1, int(fecha[:4]) - y + 1) if y else 1
        filas.append({"id_estudio": sid, "escenario": "MULTITURNO" if E[sid]["_mt"] else "UN_TURNO", "anio": y,
                      "citas": w.get("cited_by_count", 0), "citas_por_anio": round(w.get("cited_by_count", 0) / edad, 1),
                      "titulo": E[sid]["titulo"][:100]})
    for y, grp in itertools.groupby(sorted(filas, key=lambda f: (f["anio"], f["citas"])), key=lambda f: f["anio"]):
        g = list(grp)
        for i, f in enumerate(g):
            f["percentil_en_anio"] = round(100 * (i + 1) / len(g))
    for esc in ("MULTITURNO", "UN_TURNO"):
        t = sorted([f for f in filas if f["escenario"] == esc], key=lambda f: -f["citas_por_anio"])[:10]
        escribir_tabla(f"bib_mas_citados_{esc.lower()}", t, ["id_estudio", "anio", "citas", "citas_por_anio", "percentil_en_anio", "titulo"])
    res["citas_mediana_por_anio"] = {esc: float(np.median([f["citas_por_anio"] for f in filas if f["escenario"] == esc])) for esc in ("MULTITURNO", "UN_TURNO")}

    # 3 countries, institutions, industry vs academia
    paises, inst, tipo = collections.Counter(), collections.Counter(), collections.Counter()
    pais_esc = collections.defaultdict(collections.Counter)
    for sid, w in oa.items():
        cs, tys, ins = set(), set(), set()
        for a in w.get("authorships") or []:
            for i in a.get("institutions") or []:
                if i.get("country_code"):
                    cs.add(i["country_code"])
                if i.get("type"):
                    tys.add(i["type"])
                if i.get("display_name"):
                    ins.add(i["display_name"])
        for c in cs:
            paises[c] += 1
            pais_esc["MULTITURNO" if E[sid]["_mt"] else "UN_TURNO"][c] += 1
        inst.update(ins)
        tipo["solo academia" if tys <= {"education", "facility", "government", "nonprofit", "archive", "healthcare"} and tys
             else "solo industria" if tys == {"company"} else "academia + industria" if "company" in tys else "sin datos"] += 1
    escribir_tabla("bib_paises", [{"pais": c, "estudios": n, "multiturno": pais_esc["MULTITURNO"][c], "un_turno": pais_esc["UN_TURNO"][c]}
                                  for c, n in paises.most_common(15)], ["pais", "estudios", "multiturno", "un_turno"])
    escribir_tabla("bib_instituciones", [{"institucion": k, "estudios": v} for k, v in inst.most_common(15)], ["institucion", "estudios"])
    res["tipo_afiliacion"] = dict(tipo)
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.6))
    pc = paises.most_common(10)[::-1]
    nombres = [PAISES.get(c, c) for c, _ in pc]
    ax.barh(nombres, [pais_esc["UN_TURNO"][c] for c, _ in pc], color=PALETA[0], label="Un turno", edgecolor="white", linewidth=0.5)
    ax.barh(nombres, [pais_esc["MULTITURNO"][c] for c, _ in pc], left=[pais_esc["UN_TURNO"][c] for c, _ in pc], color=PALETA[1],
            label="Multiturno", edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Número de estudios")
    ax.set_ylabel("País de afiliación")
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right")
    guardar(fig, "bib_paises", leyenda="Los diez países con más estudios incluidos, por escenario. Un estudio se cuenta en cada país "
            f"con al menos un autor afiliado (fuente: OpenAlex, {fecha}). Análisis exploratorio (A6).")

    # 4 research community by year and scenario
    com = collections.Counter((comunidad(r), "MULTITURNO" if r["_mt"] else "UN_TURNO") for r in E.values())
    labs = ["PLN", "Bases de datos", "Aprendizaje automático / IA", "Otra", "Preprint"]
    escribir_tabla("bib_comunidad", [{"comunidad": l, "multiturno": com[(l, "MULTITURNO")], "un_turno": com[(l, "UN_TURNO")]} for l in labs],
                   ["comunidad", "multiturno", "un_turno"])
    fig, axs = plt.subplots(1, 2, figsize=(ANCHO_PAGINA * 0.8, 2.6), sharey=True)
    for ax, esc, tit in ((axs[0], False, "(a) Un turno"), (axs[1], True, "(b) Multiturno")):
        bottom = np.zeros(len(ANIOS))
        for i, l in enumerate(labs):
            v = np.array([sum(1 for r in E.values() if r["_mt"] == esc and r["_anio"] == a and comunidad(r) == l) for a in ANIOS])
            ax.bar(range(len(ANIOS)), v, bottom=bottom, color=PALETA[i], label=l)
            bottom += v
        ax.set_xticks(range(len(ANIOS)), [str(a)[2:] if a < 2026 else "26*" for a in ANIOS])
        ax.set_title(tit)
        ax.set_xlabel("Año de publicación (20xx)")
        ax.grid(axis="x", visible=False)
    axs[0].set_ylabel("Número de estudios")
    fig.legend(*axs[0].get_legend_handles_labels(), loc="outside lower center", ncol=5, title="Comunidad del foro")
    guardar(fig, "bib_comunidad", leyenda="Comunidad de investigación del foro de publicación, por año: (a) estudios de un turno; "
            "(b) estudios multiturno. *2026: año parcial. Análisis exploratorio (A6).")

    # 5 base-model families over time
    fam_anio = collections.defaultdict(collections.Counter)
    for r in E.values():
        txt = (r["modelos_base"] or "").lower()
        for f, rx in FAMILIAS:
            if re.search(rx, txt):
                fam_anio[f][r["_anio"]] += 1
    escribir_tabla("bib_modelos_anio", [dict({"familia": f}, **{str(a): fam_anio[f][a] for a in ANIOS}) for f, _ in FAMILIAS],
                   ["familia"] + [str(a) for a in ANIOS])
    tot = {a: sum(1 for r in E.values() if r["_anio"] == a) for a in ANIOS}
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA * 0.62, 2.4))
    tops = sorted(FAMILIAS, key=lambda f: -sum(fam_anio[f[0]].values()))[:7]
    for i, (f, _) in enumerate(tops):
        ax.plot(range(len(ANIOS)), [100 * fam_anio[f][a] / tot[a] if tot[a] else 0 for a in ANIOS], marker="o", ms=2.5, lw=0.9, color=PALETA[i], label=f)
    ax.set_xticks(range(len(ANIOS)), [str(a) if a < 2026 else "2026*" for a in ANIOS], rotation=45)
    ax.set_xlabel("Año de publicación")
    ax.set_ylabel("Estudios que usan la familia (%)")
    fig.legend(*ax.get_legend_handles_labels(), loc="outside right center", title="Familia de modelo")
    guardar(fig, "bib_modelos", leyenda="Familias de modelos base por año (porcentaje de los estudios del año que mencionan la familia; "
            "un estudio puede usar varias). En el Nivel 1 solo se registraron los modelos citados en las páginas 1–2, por lo que el uso real "
            "está subestimado. *2026: año parcial. Análisis exploratorio (A6).")

    # 6 co-occurrence of technique codes (PI3 linking + PI4 mechanism), per scenario
    codes = [c for c, _ in collections.Counter(c for r in E.values() for c in lista(r["pi3_tecnica_linking"]) + lista(r["pi4_mecanismo"])).most_common(12)]
    fig, axs = plt.subplots(1, 2, figsize=(ANCHO_PAGINA, 4.4))
    vmax = 1
    mats = {}
    for ax, esc, tit in ((axs[0], False, "(a) Un turno"), (axs[1], True, "(b) Multiturno")):
        M = np.zeros((len(codes), len(codes)), dtype=int)
        for r in E.values():
            if r["_mt"] != esc:
                continue
            cs = [c for c in set(lista(r["pi3_tecnica_linking"]) + lista(r["pi4_mecanismo"])) if c in codes]
            for a, b in itertools.product(cs, cs):
                M[codes.index(a), codes.index(b)] += 1
        Mm = np.ma.masked_where(np.triu(np.ones_like(M, dtype=bool), k=1), M)  # symmetric: show lower triangle only
        im = ax.imshow(Mm, cmap="Blues")
        ax.grid(False)
        etiquetas = [TEC.get(c, c.replace("_", " ").capitalize()) for c in codes]
        ax.set_xticks(range(len(codes)), etiquetas, rotation=60, ha="right", rotation_mode="anchor", fontsize=6)
        ax.set_yticks(range(len(codes)), etiquetas if not esc else [""] * len(codes), fontsize=6)
        for i in range(len(codes)):
            for j in range(i + 1):
                if M[i, j]:
                    ax.text(j, i, M[i, j], ha="center", va="center", fontsize=5.5, color="white" if M[i, j] > M.max() / 2 else "black")
        ax.set_title(tit)
        fig.colorbar(im, ax=ax, fraction=0.04, label="Número de estudios")
        escribir_tabla(f"bib_coocurrencia_{'multiturno' if esc else 'un_turno'}",
                       [dict({"codigo": codes[i]}, **{codes[j]: int(M[i, j]) for j in range(len(codes))}) for i in range(len(codes))],
                       ["codigo"] + codes)
    guardar(fig, "bib_coocurrencia_tecnicas", leyenda="Coocurrencia de técnicas de vinculación de esquemas (PI3) y de "
            "autocorrección (PI4) en un mismo estudio: (a) un turno; (b) multiturno. Diagonal: estudios que usan la técnica; "
            "celdas bajo la diagonal: estudios que combinan ambas. Las doce técnicas más frecuentes. Análisis exploratorio (A6).")
    json.dump(res, open(SLR / "sintesis" / "bibliometria_resultados.json", "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
