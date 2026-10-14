"""Phase 11: LaTeX macros for every number quoted in the article text (CLAUDE.md: no hand-typed numbers).

Sections use only these macros for counts, percentages and intervals; verificar_numeros.py rejects literal
numbers in latex/slr/secciones/*.tex. Output: latex/slr/numeros.tex (generated, never edited by hand).
Usage (from repo root): uv run --project analysis python analysis/src/tablas/numeros.py   (or: make tablas)
"""
import csv
import json
import re
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SLR = RAIZ / "slr"
SIN = SLR / "sintesis"


def jl(p):
    return json.load(open(p, encoding="utf-8"))


def num(x, d=1):
    return r"\num{%s}" % Decimal(str(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)


def main():
    pr, p0, p15 = jl(SIN / "prisma_conteos.json"), jl(SIN / "pi0_resultados.json"), jl(SIN / "pi15_resultados.json")
    ident = jl(SLR / "cribado" / "prisma_identificacion.json")
    cal = jl(SLR / "calidad" / "calidad_resultados.json")
    b, o, d4 = pr["bases"], pr["otros_metodos"], p0["D4"]["estricto"]
    assert b["incluidos"] + o["incluidos"] == p0["n_estudios"]
    m = {
        # search and selection (PRISMA)
        "nBases": len([k for k in b["identificados"] if k != "total"]),
        "fechaBusqueda": ident["fecha"],
        "nIdentificados": b["identificados"]["total"], "nDuplicados": b["duplicados_eliminados"],
        "nCribados": b["cribados"], "nExcluidosCribado": b["excluidos_cribado"], "nBuscados": b["buscados"],
        "nNoRecuperados": b["no_recuperados"], "nEvaluados": b["evaluados"],
        "nExcluidosTexto": b["excluidos_texto_completo"], "nIncluidosBases": b["incluidos"],
        "nIncluidosBola": o["incluidos"], "nEstudios": p0["n_estudios"],
        # two-level design and quality
        "nMultiturno": p0["n_multiturno"], "nUnTurno": p0["n_estudios"] - p0["n_multiturno"],
        "nUmbral": p15["nivel2_umbral"], "nBajoUmbral": len(cal["bajo_umbral"]),
        "validezMediana": num(cal["validez_mediana"]),
        # D4 (primary indicator of PI0)
        "DcuatroK": d4["k"], "DcuatroN": d4["n"], "DcuatroPct": num(100 * d4["k"] / d4["n"]),
        "DcuatroICinf": num(100 * d4["ic95"][0]), "DcuatroICsup": num(100 * d4["ic95"][1]),
        "DcuatroConclusion": d4["conclusion"],
        "DcuatroTendenciaP": num(p0["D4"]["tendencia_2019_2025"]["p_exacta_bilateral"], 2),
        # M8 gap criterion (+ marginal and pairwise counts over the Level 2 studies)
        "nBrechaMocho": p15["brecha_M8"]["n"],
        **{f"nMocho{k.upper()}": v for k, v in p15["brecha_M8"]["componentes"].items() if k != "base"},
        # related work
        "fechaBusquedaExploratoria": re.search(r"Fecha de búsqueda exploratoria:\s*(\S+)",
                                               (SLR / "protocolo" / "00_analisis_brecha.md").read_text(encoding="utf-8")).group(1),
        "nRevisionesPrevias": len(list(csv.DictReader(open(SIN / "tablas" / "revisiones_previas.csv", encoding="utf-8")))),
    }
    # Methods (step 4b): raw-data figures (cifras_metodo.py) and extraction agreement (informe_acuerdo.json)
    cm = jl(SIN / "cifras_metodo.json")
    ac = jl(SLR / "extraccion" / "informe_acuerdo.json")
    nombres_base = {"Scopus": "Scopus", "IEEE Xplore": "IEEE", "ACM DL": "ACM", "ACL Anthology": "ACL", "arXiv": "Arxiv"}
    m.update({f"nBase{nombres_base[k]}": v for k, v in cm["por_base"].items()})
    m.update({
        "nDupVersiones": cm["dup_versiones"], "nDupDOI": cm["dup_doi_erroneo"], "nDupHerramienta": cm["dup_srscreener"],
        "nRefMT": cm["ref_mt_n"], "nRefMTHallados": cm["ref_mt_found"], "refMTICinf": num(100 * cm["ref_mt_ic_inf"]),
        "nRefUT": cm["ref_ut_n"], "nRefUTHallados": cm["ref_ut_found"],
        "nPiloto": cm["piloto_n"], "nPilotoAvanzaAutora": cm["piloto_avanza_autora"],
        "nPilotoOmitidosIA": cm["piloto_omitidos_ia"], "pilotoKappa": num(cm["piloto_kappa"], 2),
        "nConflictosTR": cm["ta_conflictos"], "nAutoraTR": cm["ta_autora"],
        "nQC": cm["qc_n"], "nQCCercanos": cm["qc_cercanos"], "nQCAleatorios": cm["qc_aleatorios"],
        "nQCAvanzados": cm["qc_avanzados"], "nQCIncluidos": cm["qc_incluidos_tc"],
        "nConflictosTC": cm["ft_conflictos"], "nAdjTC": cm["ft_adj"], "nAutoraTC": cm["ft_autora"],
        "nCalibN": cm["calib_claude_n"], "nCalibClaude": cm["calib_claude_ok"], "nCalibCodex": cm["calib_codex_ok"],
        "nAuditPool": cm["audit_pool"], "nAuditN": cm["audit_n"], "nAuditOK": cm["audit_ok"],
        "nQCTCmt": cm["ftqc_e6_mt"], "nQCTCdudosos": cm["ftqc_dudosos"],
        "nBolaSemillas": cm["bola_semillas"], "nBolaCandOA": cm["bola_cand_openalex"],
        "nBolaSemillasSS": cm["bola_s2_semillas"], "nBolaSemillasSSrefs": cm["bola_s2_con_refs"],
        "nBolaCandSS": cm["bola_cand_s2"],
        "nItemsCalidad": cm["cal_items"], "nItemsValidez": cm["cal_items_validez"], "umbralValidez": cm["cal_umbral"],
        "nCalibCalidad": cm["cal_calibracion_n"], "umbralDcuatro": cm["d4_umbral"],
        "replicasTendencia": num(p0["D4"]["tendencia_2019_2025"]["replicas"], 0),
        "nExtrNivelUno": ac["n1_estudios"], "nExtrNivelDos": ac["n2_estudios"],
        "acuerdoNivelUno": num(100 * ac["n1_ab"][0] / ac["n1_ab"][1]),
        "acuerdoNivelDos": num(100 * ac["n2_campos_ab"][0] / ac["n2_campos_ab"][1]),
        "acuerdoCalidad": num(100 * ac["n2_calidad_ab"][0] / ac["n2_calidad_ab"][1]),
        "verifC": f"{ac['verif_C'][0]}/{ac['verif_C'][1]}", "verifD": f"{ac['verif_D'][0]}/{ac['verif_D'][1]}",
        "verifB": f"{ac['verif_B'][0]}/{ac['verif_B'][1]}", "nMuestraCiega": ac["ciega_n"],
        "ciegaCalidad": f"{ac['ciega_calidad_identico'][0]}/{ac['ciega_calidad_identico'][1]}",
        "ciegaCalidadMedio": f"{ac['ciega_calidad_medio_punto'][0]}/{ac['ciega_calidad_medio_punto'][1]}",
    })
    # plan de tesis: dataset language of the included studies (extraccion.csv, field idioma_dataset)
    idiomas = [set(t.strip() for t in r["idioma_dataset"].upper().split(";"))
               for r in csv.DictReader(open(SLR / "extraccion" / "extraccion.csv", encoding="utf-8"))]
    m.update({"nDatasetES": sum("ES" in i for i in idiomas), "nDatasetEN": sum("EN" in i for i in idiomas),
              "nDatasetZH": sum("ZH" in i for i in idiomas)})
    # step 4f reanalyses (revision_4f.py)
    rv = jl(SIN / "revision_4f.json")
    a5, a8, a9, a7 = rv["A5_omisiones"], rv["A8_sensibilidad"], rv["A9_degradacion"], rv["A7_cota_probabilistica"]
    m.update({
        "umbralNulo": num(rv["A4_nulos"]["umbral_pp"]),
        "nCentralMT": rv["A1_contraste_central"]["n_multiturno"], "nCentralUT": rv["A1_contraste_central"]["n_un_turno"],
        "espMochoAB": num(rv["A2_M8_esperados"]["ab"]), "espMochoAC": num(rv["A2_M8_esperados"]["ac"]),
        "espMochoBC": num(rv["A2_M8_esperados"]["bc"]), "espMochoABC": num(rv["A2_M8_esperados"]["abc"]),
        "tendenciaConP": num(rv["A3_tendencia_2019_2026"]["p_exacta_bilateral"], 2),
        "nulosUmbral": rv["A4_nulos"]["total_nulos"], "nEstClase": rv["A4_nulos"]["total_estudios_clase"],
        "nConfAlta": rv["A4_confianza_alta_registrada"],
        "nConjuntas": a5["exclusiones_conjuntas"], "nNoReleidas": a5["no_releidas"], "nAleatRel": a5["aleatorias_releidas"],
        "nRescAleat": a5["incluidas_tras_rescate_aleatorias"], "tasaRescate": num(100 * a5["tasa"]),
        "tasaRescateInf": num(100 * a5["tasa_ic95"][0]), "tasaRescateSup": num(100 * a5["tasa_ic95"][1]),
        "omisEsp": num(a5["omisiones_esperadas"]), "omisEspInf": num(a5["omisiones_esperadas_ic95"][0]),
        "omisEspSup": num(a5["omisiones_esperadas_ic95"][1]),
        "kappaCentral": num(rv["A6_acuerdo_central_nivel1"]["kappa"], 2), "pabakCentral": num(rv["A6_acuerdo_central_nivel1"]["pabak"], 2),
        "nKappaCentral": rv["A6_acuerdo_central_nivel1"]["n"],
        "DcuatroProbPct": num(100 * a7["p"]),
        "sensUTInf": num(100 * a8["un_turno"][2][0]), "sensUTSup": num(100 * a8["un_turno"][2][1]),
        "degPredMin": num(a9["PREDICHO"]["min"]), "degPredMax": num(a9["PREDICHO"]["max"]),
        "degSoloMin": num(a9["SOLO_PREGUNTAS"]["min"]), "degSoloMax": num(a9["SOLO_PREGUNTAS"]["max"]),
    })
    # extraction runs vs studies: \nExtrNivelUno + \nExtrNivelDos - secondary reports - studies in both + L2->L1 = \nEstudios
    ext = SLR / "extraccion"
    run1 = set(jl(ext / "runs_nivel1" / "_ab.json")["A"])
    run2 = set(jl(ext / "l2_final.json"))
    incl = {r["id_estudio"] for r in csv.DictReader(open(ext / "extraccion.csv", encoding="utf-8"))}
    sec, ambos, l2_l1 = (run1 | run2) - incl, run1 & run2 & incl, incl - run1 - run2
    assert len(run1) + len(run2) - len(sec) - len(ambos) + len(l2_l1) == p0["n_estudios"]
    e9 = list(csv.DictReader(open(SLR / "cribado" / "e9_duplicados_post_ft.csv", encoding="utf-8")))
    m.update({"nSecundariosExtraidos": len(sec), "nAmbosNiveles": len(ambos), "nNivelDosAUno": len(l2_l1),
              "nDupVerifCitas": sum(r["detectado"] == "verificacion_citas" for r in e9)})
    # PI3/PI4 contrast restricted to central studies (pi34_tecnicas_central.csv): \ct<field><code><MT|UT> (%), \nct... (n)
    corto = {"pi3_tecnica_linking": "Link", "pi3_inferencia_joins": "Joins", "pi4_mecanismo": "Mec", "pi4_senal": "Senal"}
    for r in csv.DictReader(open(SIN / "tablas" / "pi34_tecnicas_central.csv", encoding="utf-8")):
        c_ = corto[r["campo"]] + "".join(x.capitalize() for x in r["codigo"].split("_"))
        m.update({f"ct{c_}MT": num(r["pct_multiturno"]), f"ct{c_}UT": num(r["pct_un_turno"]),
                  f"nct{c_}MT": int(r["multiturno"]), f"nct{c_}UT": int(r["un_turno"])})
    # central pillars by scenario (pi0_pilares_escenario.csv): \nPilar<Uno..Cuatro><MT|UT>
    ordinal = {"PI1": "Uno", "PI2": "Dos", "PI3": "Tres", "PI4": "Cuatro"}
    for r in csv.DictReader(open(SIN / "tablas" / "pi0_pilares_escenario.csv", encoding="utf-8")):
        m.update({f"nPilar{ordinal[r['pilar']]}MT": int(r["multiturno"]), f"nPilar{ordinal[r['pilar']]}UT": int(r["un_turno"])})
    # exclusions by code and arm (prisma_conteos.json): \nExcl<TR|TC><Bases|Otros>E<Uno..Nueve>
    palabra = dict(zip("123456789", ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]))
    for brazo, nombre in ((b, "Bases"), (o, "Otros")):
        for codigo, n_ in brazo["excluidos_cribado_por_codigo"].items():
            m[f"nExclTR{nombre}E{palabra[codigo[1]]}"] = n_
        for motivo, n_ in brazo["excluidos_texto_completo_por_motivo"].items():
            m[f"nExclTC{nombre}E{palabra[motivo[1]]}"] = n_
    # D4 sensitivity variants quoted in the text (sensibilidad.json): lax version and extreme bound with non-retrieved
    sens = jl(SIN / "sensibilidad.json")
    for nombre, clave in (("Laxo", "3_D4_laxo"), ("Cota", "A4_D4_con_no_recuperados_segun_senal")):
        v = sens[clave]
        m.update({f"Dcuatro{nombre}K": v["k"], f"Dcuatro{nombre}N": v["n"], f"Dcuatro{nombre}Pct": num(100 * v["k"] / v["n"]),
                  f"Dcuatro{nombre}ICinf": num(100 * v["ic95"][0]), f"Dcuatro{nombre}ICsup": num(100 * v["ic95"][1])})
    # publication type and venue (pi0_foros.csv, pi0_venues_top.csv) and venue community (bib_comunidad.csv)
    nivel = {"A*": "Aestrella", "A": "A", "B": "B", "C": "C", "Q1": "QUno", "Q2": "QDos", "Q3": "QTres", "Q4": "QCuatro",
             "SIN_RANKING": "SinRanking", "SIN_DATOS": "", "PREPRINT": ""}
    for r in csv.DictReader(open(SIN / "tablas" / "pi0_foros.csv", encoding="utf-8")):
        m["nForo" + r["foro_tipo"].capitalize() + nivel[r["foro_nivel"]]] = int(r["estudios"])
    for n, r in enumerate(csv.DictReader(open(SIN / "tablas" / "pi0_venues_top.csv", encoding="utf-8"))):
        if n < 4:
            m["nVenue" + ["Uno", "Dos", "Tres", "Cuatro"][n]] = int(r["estudios"])
    comunidad = {"PLN": "Pln", "Bases de datos": "BasesDatos", "Aprendizaje automático / IA": "Aprendizaje",
                 "Otra": "Otra", "Preprint": "Preprint"}
    for r in csv.DictReader(open(SIN / "tablas" / "bib_comunidad.csv", encoding="utf-8")):
        m.update({f"nComunidad{comunidad[r['comunidad']]}MT": int(r["multiturno"]),
                  f"nComunidad{comunidad[r['comunidad']]}UT": int(r["un_turno"])})
    # bibliometric overview (bibliometria_resultados.json) and contribution of each source (busqueda_fuentes.csv)
    bm = jl(SIN / "bibliometria_resultados.json")
    red, dir_, af = bm["red"], bm["red"]["citas_por_direccion"], bm["tipo_afiliacion"]
    m.update({"fechaOpenalex": bm["fecha_openalex"], "nResueltosOA": bm["resueltos_openalex"],
              "nNoResueltosOA": len(bm["no_resueltos"]), "nCitasRed": red["aristas"],
              "nConVinculo": red["nodos"] - red["aislados"], "nAislados": red["aislados"],
              "nCitasUTUT": dir_["UT→UT"], "nCitasUTMT": dir_["UT→MT"], "nCitasMTMT": dir_["MT→MT"], "nCitasMTUT": dir_["MT→UT"],
              "citasMedMT": num(bm["citas_mediana_por_anio"]["MULTITURNO"]), "citasMedUT": num(bm["citas_mediana_por_anio"]["UN_TURNO"]),
              "nAfilAcademia": af["solo academia"], "nAfilMixta": af["academia + industria"],
              "nAfilIndustria": af["solo industria"], "nAfilSinDatos": af["sin datos"]})
    bf = {r["fuente"]: r for r in csv.DictReader(open(SIN / "tablas" / "busqueda_fuentes.csv", encoding="utf-8"))}
    m.update({"nInclIEEE": int(bf["IEEE Xplore"]["incluidos"]), "nInclArxiv": int(bf["arXiv"]["incluidos"]),
              "nSoloArxiv": int(bf["arXiv"]["solo_esta_fuente"])})
    nombres = {"pilares_centrales": "PilaresCentrales", "pi1_tecnica": "TecnicaContexto", "pi2_representacion": "Representacion",
               "pi3_inferencia_joins": "InferenciaJoins", "pi4_mecanismo": "Mecanismo", "historial_eval": "Historial"}
    for c_, v in rv["A5_acuerdo_campo_nivel2"].items():  # LaTeX macro names cannot contain digits
        m["acuerdoCampo" + nombres[c_]] = f"{v['k']}/{v['n']}"
    lineas = ["% Generado por analysis/src/tablas/numeros.py — no editar a mano.",
              "% Cifras del texto del artículo; cada una proviene de un archivo de resultados de la síntesis."]
    # numbers get \xspace; text values (e.g. the D4 conclusion) do not, so closing quotes stay tight
    lineas += [f"\\newcommand{{\\{k}}}{{{v}" + ("\\xspace" if re.search(r"\d", str(v)) else "") + "}" for k, v in m.items()]
    (RAIZ / "latex" / "slr" / "numeros.tex").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"{len(m)} macros → latex/slr/numeros.tex")


if __name__ == "__main__":
    main()
