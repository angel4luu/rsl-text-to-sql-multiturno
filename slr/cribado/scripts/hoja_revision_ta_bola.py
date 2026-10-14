"""Builds the human review sheet for the non-obvious title/abstract cases (option B, amendment A3).

Cases sent to the reviewer (everything else is the AI decision, verified later at full text):
  A. Conflicts the adjudicator settled as EXCLUDE (one reviewer advanced): risk of losing a study.
  B. Joint exclusions the QC senior recheck proposes to ADVANCE.
  C. Conflicts the adjudicator settled as ADVANCE (low risk: they go to full text anyway).
Writes revision_ta.md. The reviewer writes OK (accept the AI suggestion) or I / U / E1..E6
on each "Decisión:" line; leer_revision_ta.py turns the answers into overrides.csv.
Usage (from slr/cribado): python scripts/hoja_revision_ta_bola.py (snowball workspace)
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "..")
W = os.path.join(C, "sr_work_bola")


def short(dec):
    return f"{dec['d']} {dec['code']} — {dec['why']}" if dec else "—"


def label(fin):
    return {"include": "I", "unclear": "U"}.get(fin["d"], fin["code"])


def main():
    dec = json.load(open(os.path.join(W, "decisions.json")))
    recs = {r["id"]: r for r in json.load(open(os.path.join(W, "records.json")))["unique"]}
    a, b, c = [], [], []
    for rid, d in sorted(dec.items()):
        if "ADJ" in d and d.get("final", {}).get("by") != "QC":
            (a if d["ADJ"]["d"] == "exclude" else c).append(rid)
        if d.get("final", {}).get("by") == "QC":
            b.append(rid)

    head = open(os.path.join(C, "etiquetado_muestra60.md"), encoding="utf-8").read()
    crit = head[head.index("## Criterios en una mirada"):head.index("---")]
    out = [
        "# Hoja de revisión — bola de nieve: cribado título/resumen (casos no obvios)",
        "",
        f"**Generada por** `scripts/hoja_revision_ta_bola.py` a partir de `sr_work_bola/decisions.json` (bola de nieve, fase 8). "
        f"Casos: A = {len(a)}, B = {len(b)}, C = {len(c)} (total {len(a) + len(b) + len(c)}).",
        "",
        "El resto de los registros (acuerdos claros entre los dos revisores IA y exclusiones confirmadas por el control de calidad) "
        "**no** requiere su revisión (opción B, enmienda A3).",
        "",
        "## Cómo responder",
        "En la línea `Decisión:` escriba **OK** si acepta la *Sugerencia IA*, o bien **I**, **U** o **E1…E6** para cambiarla. "
        "Puede añadir una nota: `Decisión: E6 — un turno, BI`.",
        "",
        "| Sección | Qué es | Riesgo |",
        "|---|---|---|",
        "| **A** | Un revisor IA lo pasaba y el otro lo excluía; el desempate (Opus) **excluyó** | Alto: se perdería el estudio. Revise con cuidado. |",
        "| **B** | Ambos revisores lo excluyeron; el control de calidad (Opus) propone **pasarlo** | Medio |",
        "| **C** | Conflicto; el desempate lo **pasó** a texto completo | Bajo: se revisará otra vez con el texto completo |",
        "",
        crit.strip(),
        "",
        "## Códigos de exclusión (use el PRIMERO que se cumpla, en este orden)",
        head[head.index("| Código |"):head.index("*E7–E9")].strip(),
        "",
    ]
    sections = [("A", "Desempate excluyó (revisar con cuidado)", a),
                ("B", "Control de calidad propone pasar", b),
                ("C", "Desempate pasó a texto completo (bajo riesgo)", c)]
    n = 0
    for key, title, ids in sections:
        out += ["---", "", f"## Sección {key} — {title} ({len(ids)})", ""]
        for rid in ids:
            n += 1
            r, d = recs[rid], dec[rid]
            out += [f"### {key}{n}. {rid} · {r.get('year') or '?'} · {r.get('type') or ''}",
                    f"**{r.get('title') or '(sin título)'}**"]
            if r.get("journal"):
                out.append(f"*{r['journal']}*")
            out += ["", r.get("abstract") or "*(sin resumen — decida por el título)*", "",
                    f"- Revisor A: {short(d.get('A'))}",
                    f"- Revisor B: {short(d.get('B'))}"]
            if "ADJ" in d:
                out.append(f"- Desempate: {short(d['ADJ'])}")
            if "QC" in d:
                out.append(f"- Control de calidad: {short(d['QC'])}")
            out += ["", f"**Sugerencia IA:** {label(d['final'])}", "", "**Decisión:** ", ""]
    open(os.path.join(C, "revision_ta_bola.md"), "w", encoding="utf-8").write("\n".join(out))
    print(f"revision_ta_bola.md: A={len(a)} B={len(b)} C={len(c)}")


if __name__ == "__main__":
    main()
