"""Phase 12, step 1: generated content of the article appendices A–G (single PDF, decision of 2026-10-14).

A search strings (PRISMA-S) · B full-text exclusions · C extraction form · D quality rubric and per-study profile ·
E characteristics of the multi-turn studies · F moved figures · G AI models, settings, verification and prompt templates.
Every value is read from the SLR files (CSV/JSON/Markdown); counts are checked against prisma_conteos.json (assert).
Prompt templates are quoted verbatim except: the embedded protocol/form/checklist blocks (shown in appendices B–D),
the page text of the papers (copyright) and absolute paths (made relative to the repository).

Output: latex/slr/apendices/*.tex (never edited by hand). Usage: make tablas
"""
import csv
import glob
import json
import re
import textwrap
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SLR = RAIZ / "slr"
OUT = RAIZ / "latex" / "slr" / "apendices"
CAB = "% Generado por analysis/src/tablas/apendices.py — no editar a mano.\n"

# Non-ASCII characters inside verbatim listings (listings does not handle multibyte UTF-8)
TRANSLIT = {"—": "--", "–": "-", "≤": "<=", "≥": ">=", "·": ".", "«": '"', "»": '"', "’": "'", "“": '"', "”": '"',
            "…": "...", "→": "->", "×": "x", "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n", "Δ": "Delta"}
# Markdown/plain text -> LaTeX (prose cells)
SIMBOLOS = {"≥": r"$\geq$", "≤": r"$\leq$", "×": r"$\times$", "→": r"$\rightarrow$", "Δ": r"$\Delta$", "∧": r"$\wedge$",
            "∨": r"$\vee$", "<": r"$<$", ">": r"$>$", "≈": r"$\approx$"}


def leer(p, enc="utf-8"):
    return list(csv.DictReader(open(p, encoding=enc)))


def jl(p):
    return json.load(open(p, encoding="utf-8"))


def esc(s):
    s = s.replace("\\", r"\textbackslash{}")
    s = re.sub(r"([&%#_$^{}])", r"\\\1", s)
    s = s.replace("~", r"\textasciitilde{}")
    for a, b in SIMBOLOS.items():
        s = s.replace(a, b)
    return s


def md(s):
    """Markdown cell -> LaTeX: `code`, **bold**, *italics*; everything else escaped."""
    partes = re.split(r"(`[^`]*`)", s)
    out = []
    for p in partes:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append(r"\texttt{" + esc(p[1:-1]).replace(r"\_", r"\_\allowbreak{}") + "}")
        else:
            t = esc(p)
            t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
            t = re.sub(r"\*(.+?)\*", r"\\textit{\1}", t)
            out.append(t)
    return "".join(out)


def verbatim(texto):
    for a, b in TRANSLIT.items():
        texto = texto.replace(a, b)
    raros = sorted({c for c in texto if ord(c) > 127})
    assert not raros, raros
    # line breaks at whitespace only, for layout (listings cannot measure lines of several thousand characters)
    return "\n".join(textwrap.fill(l, 112, break_long_words=False, break_on_hyphens=False,
                                    subsequent_indent="  ") if len(l) > 112 else l for l in texto.split("\n"))


def escribir(nombre, tex):
    (OUT / f"{nombre}.tex").write_text(CAB + tex, encoding="utf-8")


def larga(cols, cabecera, filas, leyenda, etiqueta, tam=r"\footnotesize"):
    """longtable with repeated header (one-column appendix pages)."""
    n = cabecera.count("&") + 1
    return (f"{{{tam}\n\\setlength{{\\tabcolsep}}{{3.5pt}}\n\\begin{{longtable}}{{{cols}}}\n"
            f"\\caption{{{leyenda}}}\\label{{{etiqueta}}}\\\\\n\\toprule\n{cabecera} \\\\\n\\midrule\n\\endfirsthead\n"
            f"\\multicolumn{{{n}}}{{@{{}}l}}{{\\textit{{(continuación)}}}} \\\\\n\\toprule\n{cabecera} \\\\\n\\midrule\n\\endhead\n"
            f"\\bottomrule\n\\endfoot\n" + "\n".join(filas) + "\n\\end{longtable}\n}\n")


# ----------------------------------------------------------------------------------------------------------
def a_busqueda():
    """A: official searches (log rows B01–B09) and the exact strings (PRISMA-S)."""
    filas_log = [r for r in leer(SLR / "busqueda" / "registro_busquedas.csv") if r["id"].startswith("B")]
    prisma = jl(SLR / "sintesis" / "prisma_conteos.json")["bases"]["identificados"]
    por_base = Counter()
    for r in filas_log:
        por_base[r["base_datos"]] += int(r["resultados"])
    assert sum(por_base.values()) == prisma["total"], (por_base, prisma)
    for b, n in por_base.items():
        assert prisma[b] == n, (b, n, prisma[b])
    consulta = {"B01": "Volcado oficial + filtro local v4", "B02": "API (bloque A) + filtro local v4", "B03": "Scopus",
                "B04": "IEEE-1", "B05": "IEEE-2", "B06": "IEEE-3", "B07": "IEEE-4", "B08": "ACM-1", "B09": "ACM-2"}
    filas = [f"{r['id']} & {esc(r['base_datos'])} & {consulta[r['id']]} & {r['fecha_busqueda']} & {esc(r['campos'])} & "
             f"{esc(r['filtros'])} & {r['resultados']} \\\\" for r in filas_log]
    filas.append(r"\midrule" + f"\n\\multicolumn{{6}}{{@{{}}l}}{{Total identificado en las bases}} & {prisma['total']} \\\\")
    tabla = larga(r"@{}l l l l p{3.1cm} p{4.6cm} r@{}", "Id. & Base & Consulta & Fecha & Campos & Filtros & Registros",
                  filas, "Búsquedas oficiales registradas (\\texttt{registro\\_busquedas.csv}). En IEEE~Xplore y ACM~DL las "
                  "consultas se unieron y deduplicaron en la fase de cribado; los registros de ACM anteriores a 2019 se "
                  "excluyeron por EX1.", "tab:ap-busquedas")
    # exact strings: paste-ready file (registered v4) + arXiv API query from the run log
    texto = (SLR / "busqueda" / "consultas_para_pegar.md").read_text(encoding="utf-8")
    bloques = re.findall(r"^## (.+?)\n```\n(.*?)\n```", texto, re.M | re.S)
    assert len(bloques) == 7, len(bloques)
    log = jl(SLR / "busqueda" / "exports" / "arxiv" / "2026-10-11_arxiv_log.json")
    bloques.append(("arXiv — API export.arxiv.org (paso 1; el paso 2 aplica v4 en local, scripts/v4.py)",
                    log["query_block_A"]))
    partes = []
    for titulo, cadena in bloques:
        titulo = titulo.replace("Advanced Search → «Edit query»", "Advanced Search, editar consulta")
        partes.append(f"\\par\\medskip\\noindent\\textit{{{esc(titulo)}}}\\par\\nopagebreak\n\\begin{{lstlisting}}\n{verbatim(cadena)}\n\\end{{lstlisting}}\n")
    escribir("a_busqueda", tabla + "\n" + "\n".join(partes))


def b_excluidos():
    """B: reports excluded at full text with their code (PRISMA item 16b)."""
    prisma = jl(SLR / "sintesis" / "prisma_conteos.json")
    filas, total = [], 0
    for carpeta, rama, clave in (("Screening_FT", "Búsqueda en bases", "bases"),
                                 ("Screening_FT_bola", "Bola de nieve", "otros_metodos")):
        rs = leer(SLR / "cribado" / carpeta / "FT_screening_log_Excluded_with_reasons.csv", "utf-8-sig")
        assert len(rs) == prisma[clave]["excluidos_texto_completo"], (carpeta, len(rs))
        esperado = {k.split(" ")[0]: v for k, v in prisma[clave]["excluidos_texto_completo_por_motivo"].items()}
        assert dict(Counter(r["Final code"] for r in rs)) == esperado, carpeta
        total += len(rs)
        filas.append(f"\\multicolumn{{5}}{{@{{}}l}}{{\\textit{{{rama} (n = {len(rs)})}}}} \\\\")
        for r in sorted(rs, key=lambda r: (int(r["Final code"][1:]), r["Year"], r["First author"])):
            autor = r["First author"].strip() or "---"
            filas.append(f"{r['ID']} & {esc(autor)} & {r['Year']} & {esc(r['Title'].strip())} & EX{r['Final code'][1:]} \\\\")
    tabla = larga(r"@{}l p{3.0cm} l p{11.2cm} l@{}", "Id. & Primer autor & Año & Título & Motivo", filas,
                  f"Informes excluidos en la evaluación a texto completo con su motivo (n = {total}). Los códigos EX$n$ "
                  "son los criterios de exclusión de la \\cref{tab:criterios}; se asigna el primer criterio que falla.",
                  "tab:ap-excluidos", r"\scriptsize")
    escribir("b_excluidos", tabla)


def c_formulario():
    """C: extraction form, blocks 0–7, parsed from formulario_extraccion.md."""
    texto = (SLR / "extraccion" / "formulario_extraccion.md").read_text(encoding="utf-8")
    secciones = re.split(r"^## ", texto, flags=re.M)
    filas = []
    for s in secciones:
        titulo, _, cuerpo = s.partition("\n")
        if not titulo.startswith("Bloque"):
            continue
        filas.append(f"\\multicolumn{{2}}{{@{{}}l}}{{\\textit{{{md(titulo.strip())}}}}} \\\\")
        for linea in cuerpo.splitlines():
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")] if linea.startswith("|") else []
            if len(celdas) != 2 or set(celdas[0]) <= set("-") or celdas[0] == "Campo":
                continue
            filas.append(f"{md(celdas[0])} & {md(celdas[1])} \\\\")
    n_campos = sum(1 for f in filas if not f.startswith("\\multicolumn"))
    tabla = larga(r"@{}p{4.3cm} p{12.6cm}@{}", "Campo & Vocabulario o contenido", filas,
                  f"Formulario de extracción de datos (bloques 0--7; {n_campos} filas de campos). Los bloques 2, 3 y 5b, "
                  "y los campos marcados como Nivel 2, se extraen solo en los estudios multiturno. "
                  "\\texttt{NR}: no reportado; \\texttt{NA}: no aplica.", "tab:ap-formulario", r"\scriptsize")
    escribir("c_formulario", tabla)


def d_calidad():
    """D: quality rubric (checklist_calidad.md) and the per-study profile (calidad.csv)."""
    texto = (SLR / "calidad" / "checklist_calidad.md").read_text(encoding="utf-8")
    filas = []
    for grupo, cuerpo in re.findall(r"^### (.+?)\n(.*?)(?=^##)", texto, re.M | re.S):
        filas.append(f"\\multicolumn{{5}}{{@{{}}l}}{{\\textit{{{md(grupo.strip())}}}}} \\\\")
        for linea in cuerpo.splitlines():
            c = [x.strip() for x in linea.strip().strip("|").split("|")]
            if len(c) == 5 and c[0].startswith("CQ"):
                filas.append(" & ".join(md(x) for x in c) + " \\\\")
    rubrica = larga(r"@{}l p{7.2cm} p{2.6cm} p{2.6cm} p{2.6cm}@{}", "Ítem & Pregunta & 1 & 0,5 & 0", filas,
                    "Lista de verificación de calidad (adaptada de Kitchenham y Charters). La puntuación de validez es la "
                    "media de CQ2 y CQ4--CQ7; los ítems de reporte y apertura se informan por separado.",
                    "tab:ap-rubrica", r"\scriptsize")
    claves = {r["id_estudio"]: r["clave_bib"] for r in leer(RAIZ / "bib" / "claves_estudios.csv")}
    anio = {r["id_estudio"]: r["anio"] for r in leer(SLR / "extraccion" / "extraccion.csv")}
    cal = leer(SLR / "calidad" / "calidad.csv")
    items = ["CQ2", "CQ4", "CQ5", "CQ6", "CQ7", "CQ1", "CQ3", "CQ8", "CQ9", "CQ10"]
    sim = {"1.0": "1", "0.5": r"\textonehalf", "0.0": "0"}
    filas = []
    for r in sorted(cal, key=lambda r: (-float(r["validez_pct"]), anio[r["id_estudio"]], r["id_estudio"])):
        v = sum(float(r[i]) for i in items[:5]) / 5 * 100
        assert abs(v - float(r["validez_pct"])) < 0.05, r["id_estudio"]
        assert (v >= 50) == (r["supera_umbral"] == "SI"), r["id_estudio"]
        filas.append(f"{r['id_estudio']} & \\cite{{{claves[r['id_estudio']]}}} & {anio[r['id_estudio']]} & "
                     + " & ".join(sim[r[i]] for i in items) + f" & {float(r['validez_pct']):.0f} \\\\")
    n_sup = sum(r["supera_umbral"] == "SI" for r in cal)
    perfil = larga(r"@{}l l l *{5}{c} | *{5}{c} r@{}",
                   "Id. & Ref. & Año & " + " & ".join(items) + r" & Validez (\%)", filas,
                   f"Perfil de calidad por estudio del Nivel 2 (n = {len(cal)}; {n_sup} alcanzan el umbral de validez del "
                   "50 \\%). 1: sí; \\textonehalf: parcial; 0: no. A la izquierda de la barra, ítems de validez; a la "
                   "derecha, ítems de reporte y apertura. Orden: validez descendente.", "tab:ap-calidad")
    escribir("d_calidad", rubrica + "\n\\input{tablas/calidad}\n\n" + perfil)


ABREV = {
    "paradigma": {"AGENTES": "AG", "HIBRIDO_NEUROSIMBOLICO": "HNS", "LLM_FINETUNING": "LLM-A", "LLM_PROMPTING": "LLM-P",
                  "NEURONAL_PRE_PLM": "NPP", "PLM_FINETUNING": "PLM-A", "REGLAS_SIMBOLICO": "RS"},
    "pi1": {"CONCATENACION": "CON", "REESCRITURA": "REE", "RESOLUCION_EXPLICITA": "RES", "CLASIFICACION_DISCURSO": "CLD"},
    "pi2": {"HISTORIAL_PLANO": "HP", "ESTRUCTURA_EXPLICITA": "EE", "SQL_PREVIO_EDICION": "SQL", "GRAFO": "GR",
            "MEMORIA_EXTERNA": "ME", "VENTANA_DESLIZANTE": "VD", "RESUMEN": "RSM", "ARBOL_AST": "AST"},
    "pi3_joins": {"IMPLICITA_MODELO": "IMP", "GRAFO_FK_RESTRICCIONES": "GFK", "ALGORITMICA_CAMINOS": "ALG"},
    "pi4": {"EJECUCION_FEEDBACK_ERRORES": "EJE", "AUTODEPURACION_LLM": "ADP", "AUTOCONSISTENCIA_VOTACION": "ACV",
            "VERIFICADOR_CRITICO": "VER", "REPARACION_SIMBOLICA": "REP", "ACLARACION_USUARIO": "ACL", "ABSTENCION": "ABS"},
    "historial_eval": {"GOLD": "G", "PREDICHO": "P", "SOLO_PREGUNTAS": "SP"},
}
NOMBRE = {"paradigma": "paradigma", "pi1": "PI1", "pi2": "PI2", "pi3_joins": r"PI3 (\en{joins})", "pi4": "PI4",
          "historial_eval": "historial en la evaluación"}


PARADIGMA = {"AGENTES": "agentes", "HIBRIDO_NEUROSIMBOLICO": "híbrido neurosimbólico",
             "LLM_FINETUNING": "ajuste fino de LLM", "LLM_PROMPTING": r"LLM con \en{prompting}",
             "NEURONAL_PRE_PLM": "neuronal anterior a los PLM", "PLM_FINETUNING": "ajuste fino de PLM",
             "REGLAS_SIMBOLICO": "reglas o simbólico"}


def e_caracteristicas():
    """E: characteristics of the multi-turn studies above the validity threshold (pi_tabla_comparativa.csv)."""
    from tablas import ETIQUETA  # labels of the main-text tables (same vocabulary)
    claves = {r["id_estudio"]: r["clave_bib"] for r in leer(RAIZ / "bib" / "claves_estudios.csv")}
    rs = leer(SLR / "sintesis" / "tablas" / "pi_tabla_comparativa.csv")
    cal = {r["id_estudio"]: r for r in leer(SLR / "calidad" / "calidad.csv")}
    assert len(rs) == sum(r["supera_umbral"] == "SI" for r in cal.values())

    def cod(campo, v):
        vals = [x.strip() for x in v.split(";") if x.strip()]
        return "; ".join(ABREV[campo].get(x, x) for x in vals) or "---"

    filas = []
    for r in sorted(rs, key=lambda r: (r["anio"], r["id_estudio"])):
        res = "---"
        if r["benchmark"]:
            res = f"{esc(r['benchmark'])}, {esc(r['metrica'])}: {r['resultado']}"
            if r["delta_pp"]:
                res += f" ($\\Delta$ {r['delta_pp']})"
        filas.append(f"\\cite{{{claves[r['id_estudio']]}}} & {r['anio']} & {esc(r['pilares'])} & "
                     f"{cod('paradigma', r['paradigma'])} & {r['sin_entrenamiento']} & {cod('pi1', r['pi1'])} & "
                     f"{cod('pi2', r['pi2'])} & {cod('pi3_joins', r['pi3_joins'])} & {cod('pi4', r['pi4'])} & "
                     f"{cod('historial_eval', r['historial_eval'])} & {res} & {float(r['validez']):.0f} \\\\")
    usados = {c: {x.strip() for r in rs for x in r[c].split(";")} - {"NR", "NA", ""} for c in ABREV}
    for c, s in usados.items():
        assert s <= set(ABREV[c]), (c, s - set(ABREV[c]))
    leyenda_codigos = "; ".join(
        f"{NOMBRE[c]}: " + ", ".join(f"{ABREV[c][k]} = {(PARADIGMA.get(k) or ETIQUETA[k].lower())}"
                                     for k in ABREV[c] if k in usados[c]) for c in ABREV)
    leyenda_codigos = leyenda_codigos.replace("llm", "LLM").replace("sql", "SQL").replace("\\en{gold}", "\\en{gold}")
    tabla = larga(r"@{}l l l l l l l l l l p{4.4cm} r@{}",
                  r"Ref. & Año & Pilar & Parad. & SE & PI1 & PI2 & PI3 & PI4 & Hist. & Resultado principal & Val.",
                  filas,
                  f"Características de los estudios multiturno que alcanzan el umbral de validez (n = {len(rs)}). "
                  "Pilar: contribución central declarada; SE: sin entrenamiento; Hist.: historial usado en la evaluación; "
                  "Resultado principal: \\en{benchmark}, métrica y valor reportado (\\%), con $\\Delta$ en puntos "
                  "porcentuales frente a la línea base de referencia (regla M7e) cuando existe; Val.: puntuación de "
                  "validez (\\%). NR: no reportado; NA: no aplica. Códigos: " + leyenda_codigos + ".",
                  "tab:ap-caracteristicas", r"\scriptsize")
    escribir("e_caracteristicas", tabla)


def f_figuras():
    """F: figures moved from the main text (decision of 2026-10-14)."""
    ley = jl(RAIZ / "latex" / "slr" / "figuras" / "leyendas.json")
    tex = ""
    for n in ("pi0_paradigma_anio", "bib_coocurrencia_tecnicas"):
        cap = esc(ley[n]).replace(r"\$", "$")
        tex += (f"\\begin{{figure}}[!htbp]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{{{n}}}\n"
                f"\\caption{{{cap}}}\n\\label{{fig:{n}}}\n\\end{{figure}}\n\n")
    escribir("f_figuras", tex)


# --- G: AI use -------------------------------------------------------------------------------------------
OMITIDO = {"SCREENING PROTOCOL": "criteria in the eligibility table of the main text", "FORM EXCERPT": "see appendix C",
           "EXTRACTION FORM": "see appendix C", "QUALITY CHECKLIST": "see appendix D"}
ALIAS = {"sonnet": "claude-sonnet-5-5", "opus": "claude-opus-5-5"}
ETAPAS = [  # (stage, role, prompt folder(s)); runner settings below
    ("Cribado T/R, piloto", "Revisores A y B", ["slr/cribado/sr_work/prompts_pilot"]),
    ("Cribado T/R, piloto", "Desempate", ["slr/cribado/sr_work/prompts_pilot_adj"]),
    ("Cribado T/R", "Revisores A y B", ["slr/cribado/sr_work/prompts_ta", "slr/cribado/sr_work_bola/prompts_ta"]),
    ("Cribado T/R", "Desempate", ["slr/cribado/sr_work/prompts_ta_adj", "slr/cribado/sr_work_bola/prompts_ta_adj"]),
    ("Cribado T/R", "Control de calidad", ["slr/cribado/sr_work/prompts_qc", "slr/cribado/sr_work_bola/prompts_ta_qc"]),
    ("Texto completo", "Calibración", ["slr/cribado/sr_work/prompts_ft_calib"]),
    ("Texto completo", "Revisores A y B", ["slr/cribado/sr_work/prompts_ft", "slr/cribado/sr_work_bola/prompts_ft"]),
    ("Texto completo", "Desempate", ["slr/cribado/sr_work/prompts_ft_adj", "slr/cribado/sr_work_bola/prompts_ft_adj"]),
    ("Texto completo", "Control de calidad", ["slr/cribado/sr_work/prompts_ft_qc", "slr/cribado/sr_work_bola/prompts_ft_qc"]),
    ("Texto completo", "Auditoría de exclusiones", ["slr/cribado/sr_work/prompts_ft_audit"]),
    ("Extracción, piloto", "Extractores A y B", ["slr/extraccion/prompts_piloto"]),
    ("Extracción, Nivel 1", "Extractores A y B", ["slr/extraccion/prompts_nivel1"]),
    ("Extracción, Nivel 1", "Desempate", ["slr/extraccion/prompts_l1_desempate"]),
    ("Extracción y calidad, Nivel 2", "Extractor A", ["slr/extraccion/prompts_nivel2_A",
                                                      "slr/extraccion/prompts_nivel2_extra_A"]),
    ("Extracción y calidad, Nivel 2", "Extractor B", ["slr/extraccion/prompts_nivel2",
                                                      "slr/extraccion/prompts_nivel2_extra_B"]),
    ("Extracción y calidad, Nivel 2", "Desempate", ["slr/extraccion/prompts_l2_desempate"]),
    ("Extracción por turno, Nivel 2", "Extractor", ["slr/extraccion/prompts_turnos"]),
]


def modelos_carpeta(carpetas):
    c = Counter()
    for d in carpetas:
        idx = jl(RAIZ / d / "index.json")
        for e in (idx if isinstance(idx, list) else idx.get("entries", [])):
            c[e["model"]] += 1
    return c


def g_ia():
    # model IDs: Claude aliases resolved as reported by sr-screener (methods drafts); Codex model from the run metadata
    metodos = (SLR / "cribado" / "Screening_FT" / "FT_methods_selection.md").read_text(encoding="utf-8")
    for alias in ALIAS.values():
        assert alias in metodos, alias
    meta = [jl(p) for p in glob.glob(str(SLR / "**" / "_model.json"), recursive=True)]
    codex = {(m["model"], m["reasoning"], m["sandbox"]) for m in meta}
    assert len(codex) == 1, codex
    cmodel, crazon, csandbox = codex.pop()
    ajustes = {"claude": r"\texttt{claude -p}; solo herramienta Read; sin \en{hooks}, MCP ni sesión persistente; salida JSON",
               "codex": rf"\texttt{{codex exec}}; razonamiento \texttt{{{crazon}}}; \en{{sandbox}} de solo lectura; sesión efímera"}
    filas = []
    for fase, rol, carpetas in ETAPAS:
        c = modelos_carpeta(carpetas)
        assert c, carpetas
        for m, n in sorted(c.items()):
            mid = ALIAS.get(m, cmodel if m == "codex" else None)
            assert mid, m
            filas.append(f"{fase} & {rol} & \\texttt{{{mid}}} & {ajustes['codex' if m == 'codex' else 'claude']} & {n} \\\\")
    tabla = larga(r"@{}p{3.6cm} p{2.9cm} l p{6.0cm} r@{}", r"Fase & Rol & Modelo (ID) & Ejecución & \en{Prompts}", filas,
                  "Modelos, roles y ajustes de ejecución por etapa. Cada \\en{prompt} se ejecutó como una sesión aislada; "
                  "un \\en{prompt} de cribado T/R cubre un lote de registros. No se fijó la temperatura: las herramientas "
                  "de línea de órdenes usan el valor por defecto del proveedor. Fuente: \\texttt{index.json} de cada "
                  "carpeta de \\en{prompts} y metadatos de ejecución (\\texttt{\\_model.json}).", "tab:ap-modelos",
                  r"\scriptsize")
    # verification by the author (Wilson 95 % CI), from informe_acuerdo.json
    ia = jl(SLR / "extraccion" / "informe_acuerdo.json")
    from tablas import pct, num  # same rounding as the main text

    def wilson(k, n, z=1.96):
        p, d = k / n, 1 + z * z / n
        c, h = (p + z * z / (2 * n)) / d, z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
        return num(100 * (c - h)), num(100 * (c + h))

    verif = [("Valores concordantes A--B del Nivel 2 (muestra del 10 \\%)", "verif_C", "Confirmados sin cambios"),
             ("Estudios del Nivel 1 (muestra del 10 \\%)", "verif_D", "Confirmados sin cambios"),
             ("Ítems de validez con puntuación entre 40 y 60 \\%", "verif_B", "Confirmados sin cambios"),
             ("Muestra ciega: escenario", "ciega_escenario", "Coincide con la IA"),
             ("Muestra ciega: historial en la evaluación", "ciega_historial_eval", "Coincide con la IA"),
             ("Muestra ciega: ítems de calidad", "ciega_calidad_identico", "Puntuación idéntica"),
             ("Muestra ciega: ítems de calidad", "ciega_calidad_medio_punto", "Diferencia $\\leq$ 0,5"),
             ("Muestra ciega: resultados principales", "ciega_resultados", "Presentes en \\texttt{resultados.csv}")]
    fv = []
    for desc, k, crit in verif:
        a, n = ia[k]
        lo, hi = wilson(a, n)
        fv.append(f"{desc} & {crit} & {a}/{n} & {pct(a, n)} & {lo}--{hi} \\\\")
    tv = larga(r"@{}p{6.2cm} p{4.2cm} r r r@{}", r"Verificación & Criterio & $k/n$ & \% & IC 95 \% (Wilson)", fv,
               f"Verificación humana de la extracción y la calidad asistidas por IA. Muestra ciega: {ia['ciega_n']} "
               "estudios del Nivel 2 extraídos por la autora sin ver la propuesta de la IA (semilla fija). "
               "Fuente: \\texttt{informe\\_acuerdo\\_extraccion.md}.", "tab:ap-verificacion")
    escribir("g_ia", tabla + "\n" + tv)
    # prompt templates
    plantillas = [
        ("Cribado título-resumen, revisor A (lote)", "slr/cribado/sr_work/prompts_ta/A_b005.txt"),
        ("Cribado a texto completo, revisor A", "slr/cribado/sr_work/prompts_ft/FTA_R00003.txt"),
        ("Cribado a texto completo, desempate", "slr/cribado/sr_work/prompts_ft_adj/FTADJ_R00098.txt"),
        ("Extracción, Nivel 1, extractor A (lote)", "slr/extraccion/prompts_nivel1/A_L1_001.txt"),
        ("Extracción y calidad, Nivel 2, extractor A", "slr/extraccion/prompts_nivel2/A_R00019.txt"),
    ]
    raiz_abs = str(RAIZ) + "/"
    partes = []
    for titulo, ruta in plantillas:
        t = (RAIZ / ruta).read_text(encoding="utf-8")
        t = re.sub(r"^=== ((?!END)[^=\n]+?) ===\n.*?^=== END[^=\n]* ===$",
                   lambda m: f"[{m.group(1).split(' (')[0]}: omitted here; {OMITIDO[m.group(1).split(' (')[0]]}]", t, flags=re.S | re.M)
        corte = re.search(r"^(PAGES\n)?=== p.gina \d+ ===", t, re.M)
        if corte:
            t = t[:corte.start()] + "[PAGE TEXT OF THE PAPERS: omitted (copyright)]\n"
        t = t.replace(raiz_abs, "").rstrip()
        assert "/home/" not in t, ruta
        partes.append(f"\\par\\medskip\\noindent\\textit{{{titulo}}} (\\texttt{{{esc(ruta)}}})\\par\\nopagebreak\n\\begin{{lstlisting}}\n{verbatim(t)}\n"
                      "\\end{lstlisting}\n")
    escribir("g_prompts", "\n".join(partes))


def main():
    OUT.mkdir(exist_ok=True)
    a_busqueda()
    b_excluidos()
    c_formulario()
    d_calidad()
    e_caracteristicas()
    f_figuras()
    g_ia()
    print("apéndices A–G → latex/slr/apendices/")


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    main()
