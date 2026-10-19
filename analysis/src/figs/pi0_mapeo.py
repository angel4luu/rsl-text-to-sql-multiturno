"""Phase 10, steps 2-3 — PI0 mapping (Level 1, all included studies), D4 indicator with Wilson CI and exact
Cochran-Armitage trend (permutation, 10,000 replicates, 2019-2025; 2026 reported apart), and the single-turn vs
multi-turn contrast of PI3/PI4 technique codes. Rules as registered (01_preguntas_picoc.md, plan_sintesis.md).

Multi-turn = final level 2 (author-confirmed); PI3/PI4 central = pilares_centrales contains PI3 or PI4.
Outputs: slr/sintesis/tablas/*.csv, slr/sintesis/pi0_resultados.json, latex/slr/figuras/*.pdf.
"""
import collections
import csv
import json
import random

import matplotlib.pyplot as plt
import numpy as np

from comun import KW_MT, SLR, TABLAS, escribir_tabla, estudios, leer_csv, leer_json, lista, wilson
from estilo import ANCHO_COLUMNA, ANCHO_PAGINA, PALETA, aplicar_estilo, guardar

ANIOS = list(range(2019, 2027))


def anio(r):
    try:
        return int(str(r["anio"])[:4])
    except ValueError:
        return None


def central(r, pis=("PI3", "PI4")):
    return any(p in lista(r["pilares_centrales"]) for p in pis)


def contenido(r, pis=("PI3", "PI4")):
    return any(p in lista(r["pilares_contenidos"]) for p in pis)


def cochran_armitage_exacta(rows, reps=10000, semilla=2026):
    """rows: [(year, is_multiturn)]; statistic = sum x_i*(s_i - mean s); two-sided permutation p-value."""
    s = np.array([y for y, _ in rows], dtype=float)
    x = np.array([m for _, m in rows], dtype=float)
    sc = s - s.mean()
    t0 = float((x * sc).sum())
    rng = random.Random(semilla)
    xs = list(x)
    extremo = 0
    for _ in range(reps):
        rng.shuffle(xs)
        if abs(float((np.array(xs) * sc).sum())) >= abs(t0) - 1e-12:
            extremo += 1
    return t0, (extremo + 1) / (reps + 1)


def main():
    E = estudios()
    for r in E:
        r["_anio"] = anio(r)
        r["_mt"] = str(r["nivel"]) == "2"
    aplicar_estilo()
    res = {"n_estudios": len(E), "n_multiturno": sum(r["_mt"] for r in E)}

    # 1. studies per year and scenario
    filas = []
    for a in ANIOS:
        mt = sum(1 for r in E if r["_anio"] == a and r["_mt"])
        ut = sum(1 for r in E if r["_anio"] == a and not r["_mt"])
        filas.append({"anio": a, "multiturno": mt, "un_turno": ut, "total": mt + ut})
    escribir_tabla("pi0_anio_escenario", filas, ["anio", "multiturno", "un_turno", "total"])
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.2))
    x = np.arange(len(ANIOS))
    ax.bar(x, [f["un_turno"] for f in filas], color=PALETA[0], label="Un turno")
    ax.bar(x, [f["multiturno"] for f in filas], bottom=[f["un_turno"] for f in filas], color=PALETA[1], label="Multiturno")
    ax.set_xticks(x, [str(a) if a < 2026 else "2026*" for a in ANIOS])
    ax.set_xlabel("Año de publicación")
    ax.set_ylabel("Número de estudios")
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left")
    guardar(fig, "pi0_anio_escenario", leyenda=f"Estudios incluidos por año de publicación y escenario (n = {len(E)}). "
            "*2026: año parcial (búsqueda del 11 de octubre de 2026).")

    # 2. venue type and tier
    c = collections.Counter((r["foro_tipo"], r["foro_nivel"]) for r in E)
    escribir_tabla("pi0_foros", [{"foro_tipo": k[0], "foro_nivel": k[1], "estudios": v} for k, v in sorted(c.items())],
                   ["foro_tipo", "foro_nivel", "estudios"])
    vc = collections.Counter(r["venue"] for r in E if r["venue"])
    escribir_tabla("pi0_venues_top", [{"venue": k, "estudios": v} for k, v in vc.most_common(15)], ["venue", "estudios"])

    # 3. paradigm x year heatmap
    pars = [p for p, _ in collections.Counter(r["paradigma_principal"] for r in E).most_common() if p not in ("", "NR")]
    M = np.array([[sum(1 for r in E if r["paradigma_principal"] == p and r["_anio"] == a) for a in ANIOS] for p in pars])
    escribir_tabla("pi0_paradigma_anio", [dict({"paradigma": p}, **{str(a): int(M[i, j]) for j, a in enumerate(ANIOS)}) for i, p in enumerate(pars)],
                   ["paradigma"] + [str(a) for a in ANIOS])
    NOMBRES = {"AGENTES": "Agentes", "HIBRIDO_NEUROSIMBOLICO": "Híbrido neurosimbólico", "LLM_FINETUNING": "LLM con ajuste fino",
               "LLM_PROMPTING": "LLM con prompting", "PLM_FINETUNING": "PLM con ajuste fino", "NEURONAL_PRE_PLM": "Neuronal pre-PLM",
               "REGLAS_SIMBOLICO": "Reglas / simbólico"}
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA * 0.62, 0.3 * len(pars) + 1.0))
    im = ax.imshow(M, cmap="Blues", aspect="auto")
    ax.grid(False)
    ax.set_xticks(range(len(ANIOS)), [str(a) if a < 2026 else "2026*" for a in ANIOS])
    ax.set_yticks(range(len(pars)), [NOMBRES.get(p, p.replace("_", " ").capitalize()) for p in pars])
    ax.set_xlabel("Año de publicación")
    ax.set_ylabel("Paradigma principal")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i, j]:
                ax.text(j, i, int(M[i, j]), ha="center", va="center", fontsize=6,
                        color="white" if M[i, j] > M.max() / 2 else "black")
    fig.colorbar(im, ax=ax, fraction=0.03, label="Número de estudios")
    guardar(fig, "pi0_paradigma_anio", leyenda=f"Paradigma técnico principal de los estudios incluidos por año (n = {len(E)}; "
            "un código por estudio con la precedencia del formulario). *2026: año parcial.")

    # 4. pillars x scenario ; training-free by year and pillar
    pil = []
    for p in ["PI1", "PI2", "PI3", "PI4"]:
        pil.append({"pilar": p, "multiturno": sum(1 for r in E if r["_mt"] and p in lista(r["pilares_centrales"])),
                    "un_turno": sum(1 for r in E if not r["_mt"] and p in lista(r["pilares_centrales"]))})
    escribir_tabla("pi0_pilares_escenario", pil, ["pilar", "multiturno", "un_turno"])
    tf = []
    for a in ANIOS:
        for p in ["PI3", "PI4"]:
            g = [r for r in E if r["_anio"] == a and p in lista(r["pilares_centrales"])]
            tf.append({"anio": a, "pilar": p, "n": len(g), "sin_entrenamiento": sum(1 for r in g if r["requiere_entrenamiento"].upper() == "NO")})
    escribir_tabla("pi0_training_free", tf, ["anio", "pilar", "n", "sin_entrenamiento"])

    # 5. not-retrieved reports by scenario signal (D6), main search + snowballing
    nr = []
    for work, log in (("sr_work", "retrieval_log.csv"), ("sr_work_bola", "retrieval_log_bola.csv")):
        recs = {x["id"]: x for x in leer_json(SLR / "cribado" / work / "records.json")["unique"]}
        dec = leer_json(SLR / "cribado" / work / "decisions.json")
        for x in leer_csv(SLR / "texto_completo" / log):
            if x["status"] == "recuperado" or dec.get(x["id"], {}).get("final", {}).get("d") == "exclude":
                continue
            t = ((recs[x["id"]].get("title") or "") + " " + (recs[x["id"]].get("abstract") or "")).lower()
            nr.append("multiturno" if any(k in t for k in KW_MT) else "un_turno")
    cn = collections.Counter(nr)
    escribir_tabla("pi0_no_recuperados_escenario", [{"senal_escenario": k, "informes": v} for k, v in cn.items()], ["senal_escenario", "informes"])
    res["no_recuperados_por_senal"] = dict(cn)

    # 6. D4 (strict and lax) + trend
    pob = [r for r in E if central(r)]
    k = sum(r["_mt"] for r in pob)
    lo, hi = wilson(k, len(pob))
    pob_l = [r for r in E if central(r) or (r["_mt"] and contenido(r))]
    kl = sum(r["_mt"] for r in pob_l)
    lol, hil = wilson(kl, len(pob_l))
    # majority reading (post-close-out revision 2026-10-19; replaces the former 30 % threshold)
    regla = lambda h, l: "minoritario" if h < 0.50 else ("no concluyente" if l <= 0.50 else "mayoritario")
    res["D4"] = {"estricto": {"k": k, "n": len(pob), "p": round(k / len(pob), 4), "ic95": [round(lo, 4), round(hi, 4)], "conclusion": regla(hi, lo)},
                 "laxo": {"k": kl, "n": len(pob_l), "p": round(kl / len(pob_l), 4), "ic95": [round(lol, 4), round(hil, 4)], "conclusion": regla(hil, lol)}}
    tend = []
    for a in ANIOS:
        g = [r for r in pob if r["_anio"] == a]
        kk = sum(r["_mt"] for r in g)
        l2, h2 = wilson(kk, len(g)) if g else (float("nan"), float("nan"))
        tend.append({"anio": a, "k": kk, "n": len(g), "p": round(kk / len(g), 4) if g else "", "ic_inf": round(l2, 4) if g else "", "ic_sup": round(h2, 4) if g else ""})
    escribir_tabla("d4_tendencia", tend, ["anio", "k", "n", "p", "ic_inf", "ic_sup"])
    t0, pval = cochran_armitage_exacta([(r["_anio"], r["_mt"]) for r in pob if r["_anio"] and 2019 <= r["_anio"] <= 2025])
    res["D4"]["tendencia_2019_2025"] = {"estadistico": round(t0, 3), "p_exacta_bilateral": round(pval, 4), "replicas": 10000}
    res["D4"]["anio_2026_parcial"] = next(t for t in tend if t["anio"] == 2026)
    # post hoc complement (2026-10-19): share of multi-turn studies whose central contribution is PI3/PI4
    mts = [r for r in E if r["_mt"]]
    kc = sum(central(r) for r in mts)
    loc, hic = wilson(kc, len(mts))
    res["D4"]["complemento_multiturno"] = {"k": kc, "n": len(mts), "p": round(kc / len(mts), 4), "ic95": [round(loc, 4), round(hic, 4)],
                                         "resto_pi12": sum(1 for r in mts if not central(r) and central(r, ("PI1", "PI2"))),
                                         "resto_sin_pilar": sum(1 for r in mts if not central(r) and not central(r, ("PI1", "PI2", "PI5")))}
    fig, ax = plt.subplots(figsize=(ANCHO_COLUMNA, 2.2))
    tt = [t for t in tend if t["n"]]
    xs = [t["anio"] for t in tt]
    ax.errorbar(xs, [t["p"] * 100 for t in tt], yerr=[[100 * (t["p"] - t["ic_inf"]) for t in tt], [100 * (t["ic_sup"] - t["p"]) for t in tt]],
                fmt="o-", color=PALETA[1], capsize=2, lw=0.8, ms=3)
    ax.set_ylabel("Estudios multiturno (%)")
    ax.set_xlabel("Año de publicación")
    ax.set_xticks(xs, [str(a) if a < 2026 else "2026*" for a in xs])
    ax.set_ylim(0, 100)
    guardar(fig, "d4_tendencia", leyenda="Indicador D4 por año: proporción de estudios multiturno entre los estudios con "
            "vinculación de esquemas o autocorrección (PI3/PI4) como contribución central, con IC 95 % de Wilson. "
            "*2026: año parcial, excluido de la prueba de tendencia.")

    # 7. step 3: technique codes by scenario (single-turn vs multi-turn)
    tec = []
    for campo in ["pi3_tecnica_linking", "pi3_inferencia_joins", "pi4_mecanismo", "pi4_senal"]:
        cc = collections.defaultdict(lambda: [0, 0])
        for r in E:
            for v in lista(r[campo]):
                cc[v][0 if r["_mt"] else 1] += 1
        nmt, nut = res["n_multiturno"], len(E) - res["n_multiturno"]
        for v, (m, u) in sorted(cc.items(), key=lambda x: -sum(x[1])):
            tec.append({"campo": campo, "codigo": v, "multiturno": m, "un_turno": u,
                        "pct_multiturno": round(100 * m / nmt, 1), "pct_un_turno": round(100 * u / nut, 1),
                        "no_trasladado": "SI" if m == 0 and u >= 5 else ""})
    escribir_tabla("pi34_tecnicas_escenario", tec, ["campo", "codigo", "multiturno", "un_turno", "pct_multiturno", "pct_un_turno", "no_trasladado"])
    res["tecnicas_un_turno_no_trasladadas"] = [f"{t['campo']}:{t['codigo']} ({t['un_turno']})" for t in tec if t["no_trasladado"]]
    json.dump(res, open(SLR / "sintesis" / "pi0_resultados.json", "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
