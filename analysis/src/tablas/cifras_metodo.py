"""Phase 11, step 4b: figures of the Methods section, computed from the raw run data.

The sr-screener methods drafts (Screening_*/*_methods_selection.md) were written before some QC steps ran and are
not used as a source (e.g. the TA draft reports 360 re-screened / 0 advanced; the run data give the values below).
Output: slr/sintesis/cifras_metodo.json, read by numeros.py.
Usage (from repo root): uv run --project analysis python analysis/src/tablas/cifras_metodo.py   (or: make tablas)
"""
import collections
import csv
import glob
import json
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SLR = RAIZ / "slr"
C = SLR / "cribado"
W = C / "sr_work"


def jl(p):
    return json.load(open(p, encoding="utf-8"))


def log(carpeta, pref):
    return {r["ID"]: r for r in csv.DictReader(open(C / carpeta / f"{pref}_screening_log_All_Records.csv", encoding="utf-8-sig"))}


def decisiones(carpeta):
    out = {}
    for f in glob.glob(str(W / "runs" / carpeta / "*.json")):
        d = jl(f)
        txt = d["result"] if "result" in d else json.dumps(d)
        obj = json.loads(txt[txt.find("{"):txt.rfind("}") + 1]) if "result" in d else d
        for x in obj["decisions"]:
            out[x["id"]] = x.get("d") or x.get("decision")
    return out


def main():
    c = {}
    ident = jl(C / "prisma_identificacion.json")
    dup = ident["duplicados_eliminados"]
    c["dup_versiones"] = next(v for k, v in dup.items() if k.startswith("versiones"))
    c["dup_doi_erroneo"] = next(v for k, v in dup.items() if "DOI erróneo" in k)
    c["dup_srscreener"] = next(v for k, v in dup.items() if "sr-screener" in k)
    assert c["dup_versiones"] + c["dup_doi_erroneo"] + c["dup_srscreener"] == dup["total"]
    c["por_base"] = {k: v for k, v in ident["registros_identificados"].items() if k != "total"}

    # search sensitivity against the reference set (A1)
    s = jl(SLR / "busqueda" / "sensibilidad_fase2.json")["arms"]
    c["ref_mt_n"], c["ref_mt_found"] = s["multiturno"]["eligible"]["n"], s["multiturno"]["eligible"]["found"]
    c["ref_mt_ic_inf"] = s["multiturno"]["eligible"]["wilson95"][0]
    c["ref_ut_n"], c["ref_ut_found"] = s["un_turno"]["eligible"]["n"], s["un_turno"]["eligible"]["found"]

    # title/abstract: pilot (A3), agreement, author decisions, QC second reading of joint exclusions
    p = jl(W / "pilot_check.json")
    c["piloto_n"], c["piloto_avanza_autora"] = p["compared"], p["human_advanced"]
    c["piloto_omitidos_ia"], c["piloto_kappa"] = len(p["missed_advances"]), p["agreement"]["kappa"]
    ta = jl(C / "Screening_TA" / "TA_prisma_counts.json")
    c["ta_conflictos"], c["ta_autora"] = ta["agreement"]["conflicts"], ta["decided_by"]["AJE"]
    reasons = jl(W / "qc_reasons.json")
    qc = decisiones("manual_qc")
    assert set(qc) == set(reasons)
    c["qc_n"] = len(qc)
    c["qc_cercanos"] = sum(v == "near-miss" for v in reasons.values())
    c["qc_aleatorios"] = sum(v == "random" for v in reasons.values())
    avanzados = [i for i, d in qc.items() if d != "exclude"]
    c["qc_avanzados"] = len(avanzados)
    ft = log("Screening_FT", "FT")
    c["qc_incluidos_tc"] = sum(ft.get(i, {}).get("Final decision") == "include" for i in avanzados)

    # full text: retrieval, excerpt calibration, Codex audit, Opus second reading, adjudication
    ftc = jl(C / "Screening_FT" / "FT_prisma_counts.json")
    c["ft_conflictos"] = ftc["agreement"]["a_only_advance"] + ftc["agreement"]["b_only_advance"]
    c["ft_adj"], c["ft_autora"] = ftc["decided_by"].get("ADJ", 0), ftc["decided_by"].get("AJE", 0)
    out = subprocess.run(["python3", "scripts/calibracion_extractos.py", "compare"], cwd=C, capture_output=True,
                         text=True, timeout=300).stdout
    for quien in ("Claude", "Codex"):
        m = re.search(quien + r": n=(\d+)\s+include-vs-not agree (\d+)/\d+", out)
        c[f"calib_{quien.lower()}_n"], c[f"calib_{quien.lower()}_ok"] = int(m.group(1)), int(m.group(2))
    a = jl(W / "audit_codex_sample.json")
    aud = decisiones("cli_audit_codex")
    c["audit_pool"], c["audit_n"] = a["pool"], len(a["sample"])
    c["audit_ok"] = sum(aud.get(i) == "include" for i in a["sample"])
    qs = jl(W / "ft_qc_set.json")
    c["ftqc_e6_mt"], c["ftqc_dudosos"] = len(qs["e6_multiturn"]), len(qs["unclear"])

    # snowballing
    s1 = jl(SLR / "busqueda" / "exports" / "snowballing" / "snowball_log.json")["counts"]
    s2 = jl(SLR / "busqueda" / "exports" / "snowballing" / "snowball_log_s2.json")["counts"]
    c["bola_semillas"], c["bola_cand_openalex"] = s1["seeds"], s1["candidates"]
    c["bola_s2_semillas"], c["bola_s2_con_refs"] = s2["seeds_without_openalex_references"], s2["seeds_with_s2_references"]
    c["bola_cand_s2"] = s2["candidates"]
    tab = jl(C / "Screening_TA_bola" / "TA_prisma_counts.json")
    c["bola_ta_kappa"] = tab["agreement"]["kappa"]

    # quality checklist (protocol constants)
    chk = (SLR / "calidad" / "checklist_calidad.md").read_text(encoding="utf-8")
    c["cal_items"] = len(set(re.findall(r"\|\s*(CQ\d+)\s*\|", chk)))
    c["cal_items_validez"] = len(re.search(r"\(CQ2 \+ CQ4 \+ CQ5 \+ CQ6 \+ CQ7\)", chk).group(0).split("+"))
    c["cal_umbral"] = int(re.search(r"validez ≥ \*\*(\d+) %\*\*", chk).group(1))
    c["cal_calibracion_n"] = int(re.search(r"puntúan por separado \*\*(\d+) estudios\*\*", chk).group(1))

    json.dump(c, open(SLR / "sintesis" / "cifras_metodo.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(c, ensure_ascii=False))


if __name__ == "__main__":
    main()
