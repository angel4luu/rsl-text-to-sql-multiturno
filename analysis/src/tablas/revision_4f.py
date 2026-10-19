"""Phase 11, step 4f: reanalyses requested by the simulated peer review (decision sheet A1–A9, accepted 2026-10-14).

All computed from existing data; no new searches. Writes slr/sintesis/revision_4f.json and
slr/sintesis/tablas/pi34_tecnicas_central.csv (contrast restricted to PI3/PI4-central studies in both arms, with
«no reportado» rows). Rules reused from analysis/src/figs (pi0_mapeo.py, pi15_sintesis.py) so definitions match.
Usage: uv run --project analysis python analysis/src/tablas/revision_4f.py   (also run by make tablas)
"""
import collections
import csv
import glob
import json
import statistics as st
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "analysis" / "src" / "figs"))
from comun import KW_MT, SLR, estudios, leer_csv, lista, wilson  # noqa: E402
from pi0_mapeo import anio, central, cochran_armitage_exacta  # noqa: E402

SIN, TAB, C = SLR / "sintesis", SLR / "sintesis" / "tablas", SLR / "cribado"


def jl(p):
    return json.load(open(p, encoding="utf-8"))


def ic(k, n):
    lo, hi = wilson(k, n)
    return [round(lo, 4), round(hi, 4)]


def kappa(pares):
    n = len(pares)
    po = sum(a == b for a, b in pares) / n
    pa = sum(a for a, _ in pares) / n
    pb = sum(b for _, b in pares) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return round((po - pe) / (1 - pe), 3), round(po, 4), round(2 * po - 1, 3)  # kappa, observed, PABAK


def main():
    E = estudios()
    for r in E:
        r["_anio"], r["_mt"] = anio(r), str(r["nivel"]) == "2"
    out = {}

    # A1 — technique contrast restricted to PI3/PI4-central studies in both arms, with «no reportado» rows
    mt = [r for r in E if r["_mt"] and central(r)]
    ut = [r for r in E if not r["_mt"] and central(r)]
    filas = []
    for campo in ["pi3_tecnica_linking", "pi3_inferencia_joins", "pi4_mecanismo", "pi4_senal"]:
        cc = collections.defaultdict(lambda: [0, 0])
        for i, g in enumerate((mt, ut)):
            for r in g:
                vs = lista(r[campo])
                for v in vs:
                    cc[v][i] += 1
                if not vs:
                    cc["NR"][i] += 1
        for v, (m, u) in sorted(cc.items(), key=lambda x: (x[0] == "NR", -sum(x[1]))):
            filas.append({"campo": campo, "codigo": v, "multiturno": m, "un_turno": u,
                          "pct_multiturno": round(100 * m / len(mt), 1), "pct_un_turno": round(100 * u / len(ut), 1),
                          "no_trasladado": "SI" if v != "NR" and m == 0 and u >= 5 else ""})
    with open(TAB / "pi34_tecnicas_central.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    out["A1_contraste_central"] = {"n_multiturno": len(mt), "n_un_turno": len(ut)}

    # A2 — M8: expected pair counts under independence; lax (neural-graph) variant of (a)
    p15 = jl(SIN / "pi15_resultados.json")
    c = p15["brecha_M8"]["componentes"]
    n = c["base"]
    out["A2_M8_esperados"] = {"ab": round(c["a"] * c["b"] / n, 1), "ac": round(c["a"] * c["c"] / n, 1),
                              "bc": round(c["b"] * c["c"] / n, 1), "abc": round(c["a"] * c["b"] * c["c"] / n ** 2, 2)}

    # A3 — trend test including the partial year 2026 (sensitivity)
    pob = [r for r in E if central(r)]
    t0, pv = cochran_armitage_exacta([(r["_anio"], r["_mt"]) for r in pob if r["_anio"] and 2019 <= r["_anio"] <= 2026])
    out["A3_tendencia_2019_2026"] = {"estadistico": round(t0, 3), "p_exacta_bilateral": round(pv, 4), "replicas": 10000}

    # A4 — null threshold |Δ| < 0.5 pp on per-study medians; reporting-bias-penalized confidence (one level down)
    from pi15_sintesis import ACC, efectos  # noqa: E402
    cal = {r["id_estudio"]: r for r in leer_csv(SLR / "calidad" / "calidad.csv")}
    ids = {s for s, r in cal.items() if r["supera_umbral"] == "SI"}
    ef = efectos(leer_csv(SLR / "extraccion" / "contrastes_taxonomia.csv"), ids)
    nulos = []
    for e in ef:
        d = list(e["_deltas"].values())
        nulos.append({"pilar": e["pilar"], "clase": e["clase"], "n": len(d),
                      "nulos_umbral": sum(abs(x) < 0.5 for x in d), "positivos_umbral": sum(x >= 0.5 for x in d),
                      "negativos_umbral": sum(x <= -0.5 for x in d)})
    baja = {"alta": "moderada", "moderada": "baja", "baja": "muy baja", "muy baja": "muy baja"}
    conf = leer_csv(TAB / "confianza_hallazgos.csv")
    out["A4_nulos"] = {"umbral_pp": 0.5, "total_estudios_clase": sum(x["n"] for x in nulos),
                       "total_nulos": sum(x["nulos_umbral"] for x in nulos), "por_clase": nulos}
    out["A4_confianza_penalizada"] = {r["hallazgo"].split(":")[0]: baja.get(r["confianza"], r["confianza"]) for r in conf}
    out["A4_confianza_alta_registrada"] = sum(r["confianza"] == "alta" for r in conf)

    # A5 — joint exclusions not re-read; rescue rate in the random QC stratum extrapolated to them
    recs = {r["ID"]: r for r in csv.DictReader(open(C / "Screening_TA" / "TA_screening_log_All_Records.csv", encoding="utf-8-sig"))}
    ft = {r["ID"]: r for r in csv.DictReader(open(C / "Screening_FT" / "FT_screening_log_All_Records.csv", encoding="utf-8-sig"))}
    razones = jl(C / "sr_work" / "qc_reasons.json")
    qc = {}
    for f in glob.glob(str(C / "sr_work" / "runs" / "manual_qc" / "*.json")):
        for x in jl(f)["decisions"]:
            qc[x["id"]] = x["d"]
    conj = [i for i, r in recs.items() if r["Reviewer A"] == "exclude" and r["Reviewer B"] == "exclude"]
    no_releidas = [i for i in conj if i not in qc]
    aleat = [i for i in qc if razones.get(i) == "random" and i in conj]
    resc_inc = sum(ft.get(i, {}).get("Final decision") == "include" for i in aleat)
    tasa = resc_inc / len(aleat)
    lo, hi = wilson(resc_inc, len(aleat))
    out["A5_omisiones"] = {"exclusiones_conjuntas": len(conj), "releidas": len(conj) - len(no_releidas),
                           "no_releidas": len(no_releidas), "aleatorias_releidas": len(aleat),
                           "incluidas_tras_rescate_aleatorias": resc_inc, "tasa": round(tasa, 4), "tasa_ic95": [round(lo, 4), round(hi, 4)],
                           "omisiones_esperadas": round(tasa * len(no_releidas), 1),
                           "omisiones_esperadas_ic95": [round(lo * len(no_releidas), 1), round(hi * len(no_releidas), 1)]}
    # per-field agreement, Level 2 (A vs B, non-pilot studies)
    comp = jl(SLR / "extraccion" / "runs_nivel2_ab" / "_comparacion.json")
    campos = ["pilares_centrales", "pi1_tecnica", "pi2_representacion", "pi3_inferencia_joins", "pi4_mecanismo", "historial_eval"]
    out["A5_acuerdo_campo_nivel2"] = {c_: {"k": sum(c_ not in v["discrepancias"] for v in comp.values()), "n": len(comp)} for c_ in campos}

    # A6 — agreement on the field that defines the D4 population (PI3/PI4 central), Level 1 A vs B
    ab = jl(SLR / "extraccion" / "runs_nivel1" / "_ab.json")
    pares = [(central(ab["A"][s]), central(ab["B"][s])) for s in ab["A"] if s in ab["B"]]
    k, po, pabak = kappa(pares)
    out["A6_acuerdo_central_nivel1"] = {"n": len(pares), "kappa": k, "acuerdo": po, "pabak": pabak}

    # A7 — unretrieved reports: probabilistic bound for D4 with the rates observed among retrieved reports
    rr = jl(C / "sr_work" / "records.json")["unique"]
    senal = {r["id"]: any(kw in f"{r.get('title', '')} {r.get('abstract', '')}".lower() for kw in KW_MT) for r in rr}
    Eid = {r["id_estudio"]: r for r in E}
    tasas = {}
    for s_ in (True, False):
        evaluados = [i for i, r in ft.items() if senal.get(i) == s_ and r["Final decision"] in ("include", "exclude")]
        num_ = sum(1 for i in evaluados if i in Eid and central(Eid[i]) and Eid[i]["_mt"])
        den_ = sum(1 for i in evaluados if i in Eid and central(Eid[i]))
        tasas[s_] = (num_ / len(evaluados), den_ / len(evaluados), len(evaluados))
    p0 = jl(SIN / "pi0_resultados.json")
    nr = p0["no_recuperados_por_senal"]
    k0, n0 = p0["D4"]["estricto"]["k"], p0["D4"]["estricto"]["n"]
    kp = k0 + nr["multiturno"] * tasas[True][0] + nr["un_turno"] * tasas[False][0]
    np_ = n0 + nr["multiturno"] * tasas[True][1] + nr["un_turno"] * tasas[False][1]
    out["A7_cota_probabilistica"] = {"k_esperado": round(kp, 1), "n_esperado": round(np_, 1), "p": round(kp / np_, 4),
                                     "tasas_recuperados": {"multiturno": [round(tasas[True][0], 4), round(tasas[True][1], 4), tasas[True][2]],
                                                           "un_turno": [round(tasas[False][0], 4), round(tasas[False][1], 4), tasas[False][2]]}}
    ret = jl(C / "Screening_FT" / "FT_prisma_counts.json")
    out["A7_recuperacion"] = {"buscados": ret["reports_sought_for_retrieval"], "no_recuperados": ret["reports_not_retrieved"]}

    # A8 — CI of single-turn and multi-turn search sensitivity
    s = jl(SLR / "busqueda" / "sensibilidad_fase2.json")["arms"]
    out["A8_sensibilidad"] = {"un_turno": [s["un_turno"]["eligible"]["found"], s["un_turno"]["eligible"]["n"],
                                           ic(s["un_turno"]["eligible"]["found"], s["un_turno"]["eligible"]["n"])],
                              "multiturno": [s["multiturno"]["eligible"]["found"], s["multiturno"]["eligible"]["n"],
                                             ic(s["multiturno"]["eligible"]["found"], s["multiturno"]["eligible"]["n"])]}

    # A9 — degradation slopes per stratum (range, n) and curves exceeding turn 1
    pend = leer_csv(TAB / "pi5_pendientes.csv")
    a9 = {}
    for h in ("PREDICHO", "SOLO_PREGUNTAS"):
        v = [float(r["pendiente_pp_por_turno"]) for r in pend if r["historial_eval"] == h]
        if v:
            a9[h] = {"curvas": len(v), "mediana": round(st.median(v), 2), "min": min(v), "max": max(v),
                     "positivas": sum(x > 0 for x in v)}
    out["A9_degradacion"] = a9

    json.dump(out, open(SIN / "revision_4f.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in out.items() if k not in ("A4_nulos", "A4_confianza_penalizada")}, ensure_ascii=False, indent=1))
    print("A4 nulls:", out["A4_nulos"]["total_nulos"], "of", out["A4_nulos"]["total_estudios_clase"])


if __name__ == "__main__":
    main()
