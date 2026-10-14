"""Human review sheet for the non-obvious FULL-TEXT decisions (option B, amendment A3 logic).

Sections:
  A. Conflicts the adjudicator (Opus) settled as EXCLUDE although one reviewer advanced the report.
  B. Multi-turn-signal reports both reviewers excluded with E6 where the Opus second reading says advance.
  C. Reports both reviewers marked "unclear": Opus second reading (full text) gives a definite decision.
  D. Codex-reviewed reports where the Claude audit disagreed.
Writes revision_ft.md. Answers: OK (accept the suggestion) or I / U / E1..E9 on each "Decisión:" line;
leer_revision_ft.py turns them into overrides_ft.csv for merge_decisions.py --stage ft --overrides.
Usage (from slr/cribado): python scripts/hoja_revision_ft.py
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.abspath(os.path.join(HERE, ".."))
W = os.path.join(C, "sr_work")


def from_result(path):
    j = json.load(open(path, encoding="utf-8"))
    if j.get("decisions"):
        return j["decisions"][0]
    m = re.search(r'\{\s*"decisions".*\}', j.get("result") or "", re.S)
    return json.loads(m.group(0))["decisions"][0] if m else None


def runs(d, prefix):
    out = {}
    for f in glob.glob(os.path.join(W, "runs", d, f"{prefix}_R*.json")):
        if not f.endswith(".error.json"):
            x = from_result(f)
            if x:
                out[x["id"]] = x
    return out


def short(x):
    return f"{x['d']} {x['code']} — {x['why']}" + (f" *(p. {x['where']})*" if x.get("where") else "") if x else "—"


def label(code):
    return {"INC": "I", "UNC": "U"}.get(code, code)


def main():
    dec = json.load(open(os.path.join(W, "ft_decisions.json")))
    recs = {r["id"]: r for r in json.load(open(os.path.join(W, "records.json")))["unique"]}
    qc, audit = runs("cli_ft_qc", "FTQC"), runs("cli_audit_codex", "FTA")
    qset = json.load(open(os.path.join(W, "ft_qc_set.json")))
    sec = {"A": [], "B": [], "C": [], "D": []}
    for rid, x in sorted(dec.items()):
        if "ADJ" in x and x["final"]["d"] == "exclude":
            sec["A"].append((rid, x["final"]["code"]))
    for rid in qset["e6_multiturn"]:
        if qc.get(rid) and qc[rid]["code"] != "E6":
            sec["B"].append((rid, qc[rid]["code"]))
    for rid in qset["unclear"]:
        if qc.get(rid):
            sec["C"].append((rid, qc[rid]["code"]))
    for rid, a in sorted(audit.items()):
        if (a["d"] == "exclude") != (dec[rid]["final"]["d"] == "exclude"):
            sec["D"].append((rid, dec[rid]["final"]["code"]))
    cfg = json.load(open(os.path.join(C, "..", "protocolo", "screening_config.json")))
    codes = "\n".join(f"| **{c['code']}** | {c['label']} |" for c in cfg["exclusion_codes"])
    total = sum(len(v) for v in sec.values())
    out = [
        "# Hoja de revisión — cribado de texto completo (casos no obvios)", "",
        f"Generada por `scripts/hoja_revision_ft.py` desde `sr_work/ft_decisions.json` y las segundas lecturas de Opus. "
        f"Casos: A = {len(sec['A'])}, B = {len(sec['B'])}, C = {len(sec['C'])}, D = {len(sec['D'])} (total {total}).", "",
        "## Cómo responder",
        "En la línea `Decisión:` escriba **OK** para aceptar la *Sugerencia IA*, o **I** (incluir), **U** (dudoso) o **E1…E9**. "
        "Nota opcional: `Decisión: E6 — un turno`.", "",
        "| Sección | Qué es | Riesgo |", "|---|---|---|",
        "| **A** | Un revisor lo pasaba; el desempate (Opus) lo **excluyó** | Alto: se perdería el estudio |",
        "| **B** | Ambos revisores lo excluyeron con E6 (señal multiturno); Opus propone **pasarlo** | Alto (posible Nivel 2) |",
        "| **C** | Ambos revisores dijeron «dudoso»; Opus, con el texto completo, propone una decisión | Medio |",
        "| **D** | Revisado por Codex; la auditoría de Claude no coincidió | Medio |", "",
        "## Criterios de inclusión (texto completo)",
        "Pasa si es un estudio primario de **Text-to-SQL sobre BD relacionales** con **evaluación cuantitativa**, y además "
        "(a) **multiturno** (preguntas sucesivas del usuario dependientes del contexto) que aborde PI1–PI5, o "
        "(b) **un turno** cuya contribución central declarada sea vinculación de esquemas / inferencia de *joins* / "
        "retroalimentación de ejecución o autocorrección, evaluado en un *benchmark* público. Use el **primer** código que falle.", "",
        "| Código | Excluir si… |", "|---|---|", codes, "",
    ]
    titles = {"A": "Desempate excluyó (revisar con cuidado)", "B": "Opus propone rescatar una exclusión E6",
              "C": "Dudosos resueltos por Opus", "D": "Discrepancia en la auditoría de Codex"}
    n = 0
    for k in "ABCD":
        out += ["---", "", f"## Sección {k} — {titles[k]} ({len(sec[k])})", ""]
        for rid, sug in sec[k]:
            n += 1
            r, x = recs[rid], dec[rid]
            out += [f"### {k}{n}. {rid} · {r.get('year') or '?'} · {r.get('type') or ''}",
                    f"**{r.get('title') or '(sin título)'}**"]
            if r.get("journal"):
                out.append(f"*{r['journal']}*")
            out += ["", (r.get("abstract") or "*(sin resumen)*")[:1500], "",
                    f"- Revisor A: {short(x.get('A'))}", f"- Revisor B: {short(x.get('B'))}"]
            if "ADJ" in x:
                out.append(f"- Desempate (Opus): {short(x['ADJ'])}")
            if rid in qc:
                out.append(f"- Segunda lectura (Opus, texto completo): {short(qc[rid])}")
            if rid in audit:
                out.append(f"- Auditoría (Claude): {short(audit[rid])}")
            out += ["", f"**Sugerencia IA:** {label(sug)}", "", "**Decisión:** ", ""]
    open(os.path.join(C, "revision_ft.md"), "w", encoding="utf-8").write("\n".join(out))
    print("revision_ft.md:", {k: len(v) for k, v in sec.items()})


if __name__ == "__main__":
    main()
