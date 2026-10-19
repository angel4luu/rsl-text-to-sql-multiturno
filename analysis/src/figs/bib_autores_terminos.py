"""Phase 10 — exploratory bibliometrics, part 2 (amendment A6): authorship and terms.

1 author productivity (top 15 authors by number of included studies, by scenario)
2 co-authorship network of the authors with >= 3 included studies (edge = co-authored study)
3 terms in titles and abstracts: word cloud (illustrative) + frequency bars (the readable version)
Inputs: slr/extraccion/extraccion.csv, slr/sintesis/datos/openalex_estudios.jsonl, screening records (abstracts).
Outputs: slr/sintesis/tablas/bib_autores.csv, bib_terminos.csv; latex/slr/figuras/bib_autores*.pdf, bib_terminos*.pdf.
"""
import collections
import itertools
import json
import re

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from wordcloud import STOPWORDS, WordCloud

from comun import SLR, escribir_tabla, estudios, leer_json
from estilo import ANCHO_COLUMNA, ANCHO_PAGINA, PALETA, aplicar_estilo, guardar

STOP = set("""a an the of for and or in on to with from by via as at into over under is are be been being this that these those
we our us it its their they them which what when where how than then also can may more most such both each other using use used
based towards toward through between across within without new novel approach approaches method methods model models paper study
propose proposed present results show shows achieve achieves achieving state art performance task tasks large language llm llms
text sql text-to-sql nl2sql natural queries query question questions database databases framework system systems data set via
however while existing previous first two one three experiments experimental demonstrate significantly improve improves improving
improvement accuracy benchmark benchmarks work works make making effective effectively compared introduce introduces address
addresses learning dataset datasets complex various different key challenge challenges evaluate evaluated evaluation outperforms
outperform demonstrates leverage leverages leveraging high recent real-world world well generate generates generating generation
semantic specific multiple single provide provides including enables enable ability given correct correctly significant
substantial develop developed critical important often across have has had state-of-the-art computational linguistics
association copyright licensed rights reserved information code available publicly github open-source source https
specifically current yet due still better relevant strong challenging effectiveness enabling designed extensive practical rely
relies struggle potential time enhance enhances enhanced research test problem process settings scenarios diverse robust accurate
understanding limitations analysis strategy strategies capabilities generated problem problems design remains remain particularly
enables significantly furthermore thus therefore moreover effective consistently overall""".split()) | set(STOPWORDS)


def main():
    E = {r["id_estudio"]: r for r in estudios()}
    for r in E.values():
        r["_mt"] = str(r["nivel"]) == "2"
    oa, fecha = {}, None
    for line in open(SLR / "sintesis" / "datos" / "openalex_estudios.jsonl", encoding="utf-8"):
        j = json.loads(line)
        fecha = j["fecha"]
        if j["work"] and j["id_estudio"] in E:
            oa[j["id_estudio"]] = j["work"]
    aplicar_estilo()

    # 1 author productivity
    autores = collections.defaultdict(lambda: {"nombre": "", "MT": 0, "UT": 0, "estudios": []})
    for sid, w in oa.items():
        for a in w.get("authorships") or []:
            au = a.get("author") or {}
            if not au.get("id"):
                continue
            d = autores[au["id"]]
            d["nombre"] = au.get("display_name") or au["id"]
            d["MT" if E[sid]["_mt"] else "UT"] += 1
            d["estudios"].append(sid)
    top = sorted(autores.items(), key=lambda kv: -(kv[1]["MT"] + kv[1]["UT"]))[:15]
    escribir_tabla("bib_autores", [{"autor": d["nombre"], "estudios": d["MT"] + d["UT"], "multiturno": d["MT"], "un_turno": d["UT"]}
                                   for _, d in top], ["autor", "estudios", "multiturno", "un_turno"])
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 3.0))
    tt = top[::-1]
    nombres = [d["nombre"] for _, d in tt]
    ax.barh(nombres, [d["UT"] for _, d in tt], color=PALETA[0], label="Un turno", edgecolor="white", linewidth=0.5)
    ax.barh(nombres, [d["MT"] for _, d in tt], left=[d["UT"] for _, d in tt], color=PALETA[1], label="Multiturno",
            edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Número de estudios incluidos")
    ax.set_ylabel("Autor")
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right")
    guardar(fig, "bib_autores", leyenda="Los quince autores con más estudios incluidos, por escenario (fuente: OpenAlex, "
            f"{fecha}; autores identificados por su identificador de OpenAlex). Análisis exploratorio.")

    # 2 co-authorship network (authors with >= 3 studies)
    fuertes = {k for k, d in autores.items() if d["MT"] + d["UT"] >= 3}
    G = nx.Graph()
    for k in fuertes:
        G.add_node(k)
    for sid, w in oa.items():
        ids = [a["author"]["id"] for a in w.get("authorships") or [] if (a.get("author") or {}).get("id") in fuertes]
        for a, b in itertools.combinations(sorted(set(ids)), 2):
            G.add_edge(a, b, weight=G.get_edge_data(a, b, {"weight": 0})["weight"] + 1)
    G.remove_nodes_from([n for n in list(G) if G.degree(n) == 0])
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    pos = nx.spring_layout(G, seed=2026, k=0.6, weight="weight")
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA, 4.4))
    nx.draw_networkx_edges(G, pos, ax=ax, width=[0.4 + 0.5 * G[a][b]["weight"] for a, b in G.edges()], alpha=0.35, edge_color="#666666")
    share = {n: autores[n]["MT"] / (autores[n]["MT"] + autores[n]["UT"]) for n in G}
    for grupo, col, lab in ((lambda n: share[n] >= 0.5, PALETA[1], "Mayoría multiturno"), (lambda n: share[n] < 0.5, PALETA[0], "Mayoría un turno")):
        ns = [n for n in G if grupo(n)]
        nx.draw_networkx_nodes(G, pos, nodelist=ns, ax=ax, node_color=col, label=lab, linewidths=0.4, edgecolors="white",
                               node_size=[25 + 18 * (autores[n]["MT"] + autores[n]["UT"]) for n in ns])
    etiquetar = [max(c, key=lambda n: autores[n]["MT"] + autores[n]["UT"]) for c in comps if len(c) >= 3]
    for n in etiquetar:
        x, y = pos[n]
        ax.text(x, y + 0.045, autores[n]["nombre"], fontsize=6, ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.8))
    ax.legend(loc="lower left", title="Autor (tamaño = estudios incluidos)", title_fontsize=6.5, markerscale=0.6)
    ax.axis("off")
    ax.margins(0.08)
    guardar(fig, "bib_autores_red", leyenda=f"Red de coautoría de los autores con al menos tres estudios incluidos ({G.number_of_nodes()} "
            f"autores, {G.number_of_edges()} vínculos, {len(comps)} grupos; el mayor reúne {len(comps[0]) if comps else 0} autores). "
            "El grosor de la arista indica el número de estudios en coautoría; se rotula el autor más productivo de cada grupo de tres o más "
            "autores (lista completa en la tabla bib_autores). "
            f"Fuente: OpenAlex, {fecha}. Análisis exploratorio.")

    # 3 terms (unigrams + bigrams) in titles and abstracts
    recs = {}
    for w_, p in (("sr_work", "R"), ("sr_work_bola", "B")):
        for r in leer_json(SLR / "cribado" / w_ / "records.json")["unique"]:
            recs[p + r["id"][1:]] = r
    frec = collections.Counter()
    frec_esc = {True: collections.Counter(), False: collections.Counter()}
    for sid, r in E.items():
        rr = recs.get(sid, {})
        toks = [t for t in re.findall(r"[a-z][a-z0-9\-]+", ((rr.get("title") or r["titulo"]) + " " + (rr.get("abstract") or "")).lower())
                if t not in STOP and len(t) > 2]
        toks = [t[:-1] if t.endswith("s") and not t.endswith("ss") and len(t) > 4 else t for t in toks]  # schema(s), table(s)
        terms = set(toks) | {f"{a} {b}" for a, b in zip(toks, toks[1:])}
        frec.update(terms)              # document frequency: a term counts once per study
        frec_esc[r["_mt"]].update(terms)
    top_t = [t for t, _ in frec.most_common(80)]
    escribir_tabla("bib_terminos", [{"termino": t, "estudios": frec[t], "multiturno": frec_esc[True][t], "un_turno": frec_esc[False][t]}
                                    for t in top_t[:40]], ["termino", "estudios", "multiturno", "un_turno"])
    fmax, fmin = frec[top_t[0]], frec[top_t[-1]]

    def color(word, **_):  # sequential single hue: darker = more studies (readable on white)
        k = (frec[word] - fmin) / max(1, fmax - fmin)
        r, g, b, _a = plt.get_cmap("Blues")(0.55 + 0.45 * k)
        return f"rgb({int(255 * r)},{int(255 * g)},{int(255 * b)})"

    wc = WordCloud(width=1600, height=800, background_color="white", color_func=color, prefer_horizontal=1.0,
                   font_path="/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", relative_scaling=0.5,
                   min_font_size=10, random_state=2026).generate_from_frequencies({t: frec[t] for t in top_t})
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA * 0.8, ANCHO_PAGINA * 0.4))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    guardar(fig, "bib_terminos_nube", leyenda="Nube de los 80 términos (palabras y bigramas) más frecuentes en títulos y resúmenes de los "
            "390 estudios incluidos; el tamaño es proporcional al número de estudios que los mencionan. Figura ilustrativa: "
            "las frecuencias exactas están en la figura de barras y en la tabla bib_terminos. Análisis exploratorio.")
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 3.6))
    t20 = top_t[:20][::-1]
    ax.barh(t20, [frec_esc[False][t] for t in t20], color=PALETA[0], label="Un turno", edgecolor="white", linewidth=0.5)
    ax.barh(t20, [frec_esc[True][t] for t in t20], left=[frec_esc[False][t] for t in t20], color=PALETA[1], label="Multiturno",
            edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Estudios que mencionan el término")
    ax.set_ylabel("Término")
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right")
    guardar(fig, "bib_terminos_barras", leyenda="Los veinte términos más frecuentes en títulos y resúmenes (número de estudios que los "
            "mencionan, por escenario), excluidas palabras vacías y términos genéricos del dominio (p. ej., «text-to-SQL», «LLM»). "
            "Análisis exploratorio (A6).")
    print(json.dumps({"autores_top": [(d["nombre"], d["MT"] + d["UT"]) for _, d in top[:8]], "red_coautoria": {
        "autores": G.number_of_nodes(), "vinculos": G.number_of_edges(), "grupos": len(comps)},
        "terminos_top": [(t, frec[t]) for t in top_t[:15]]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
