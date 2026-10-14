"""Phase 10, step 1 — PRISMA 2020 counts (from the screening tools' outputs) and flow diagram.

Every number is read from: cribado/prisma_identificacion.json (database identification and pre-screening
de-duplication), Screening_TA / Screening_FT (main search) and Screening_TA_bola / Screening_FT_bola (other
methods: snowballing), plus dedup_bola_post_ta.csv. Writes slr/sintesis/prisma_conteos.json and
latex/slr/figuras/prisma_flujo.pdf.
"""
import csv
import json

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from comun import SLR, leer_json
from estilo import ANCHO_PAGINA, aplicar_estilo, guardar

C = SLR / "cribado"


def conteos():
    ident = leer_json(C / "prisma_identificacion.json")
    ta = leer_json(C / "Screening_TA" / "TA_prisma_counts.json")
    ft = leer_json(C / "Screening_FT" / "FT_prisma_counts.json")
    tab = leer_json(C / "Screening_TA_bola" / "TA_prisma_counts.json")
    ftb = leer_json(C / "Screening_FT_bola" / "FT_prisma_counts.json")
    dedup_post = list(csv.DictReader(open(C / "dedup_bola_post_ta.csv", encoding="utf-8")))
    snow = leer_json(SLR / "busqueda" / "exports" / "snowballing" / "snowball_log.json")["counts"]
    snow2 = leer_json(SLR / "busqueda" / "exports" / "snowballing" / "snowball_log_s2.json")["counts"]
    ta_excl_bola = {k: v for k, v in tab["excluded_by_code"].items()}
    return {
        "bases": {
            "identificados": ident["registros_identificados"],
            "duplicados_eliminados": ident["duplicados_eliminados"]["total"],
            "cribados": ta["records_screened"],
            "excluidos_cribado": ta["records_excluded"],
            "excluidos_cribado_por_codigo": ta["excluded_by_code"],
            "buscados": ft["reports_sought_for_retrieval"],
            "no_recuperados": ft["reports_not_retrieved"],
            "evaluados": ft["reports_assessed"],
            "excluidos_texto_completo": ft["reports_excluded"],
            "excluidos_texto_completo_por_motivo": ft["excluded_by_reason"],
            "incluidos": ft["studies_included_reports"],
        },
        "otros_metodos": {
            "estudios_de_inicio": snow["seeds"],
            "registros_identificados_openalex": snow["candidates"],
            "registros_identificados_semantic_scholar": snow2["candidates"],
            "duplicados_eliminados": tab["identified_total"] - tab["records_screened"] if "identified_total" in tab else 1,
            "cribados": tab["records_screened"],
            "excluidos_cribado": tab["records_excluded"] - len(dedup_post),
            "duplicados_tras_cribado_E9": len(dedup_post),
            "buscados": ftb["reports_sought_for_retrieval"],
            "no_recuperados": ftb["reports_not_retrieved"],
            "evaluados": ftb["reports_assessed"],
            "excluidos_texto_completo": ftb["reports_excluded"],
            "excluidos_texto_completo_por_motivo": ftb["excluded_by_reason"],
            "incluidos": ftb["studies_included_reports"],
            "excluidos_cribado_por_codigo": ta_excl_bola,
        },
    }


def en_lineas(items, por_linea=3):
    items = list(items)
    return "\n".join(" · ".join(items[i:i + por_linea]) for i in range(0, len(items), por_linea))


def caja(ax, x, y, w, h, texto, color="#FFFFFF"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.01",
                                linewidth=0.6, edgecolor="black", facecolor=color))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=6.2, wrap=True)


def flecha(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", lw=0.6, color="black"))


def main():
    c = conteos()
    (SLR / "sintesis").mkdir(exist_ok=True)
    json.dump(c, open(SLR / "sintesis" / "prisma_conteos.json", "w"), indent=1, ensure_ascii=False)
    b, o = c["bases"], c["otros_metodos"]
    ident = b["identificados"]
    aplicar_estilo()
    fig, ax = plt.subplots(figsize=(ANCHO_PAGINA, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    W, H = 0.27, 0.11
    xL, xR, xO, xOR = 0.02, 0.31, 0.62, 0.84
    ys = [0.86, 0.66, 0.46, 0.26, 0.04]
    ax.text(0.30, 0.985, "Identificación de estudios mediante bases de datos", ha="center", fontsize=7, weight="bold")
    ax.text(0.80, 0.985, "Identificación mediante otros métodos", ha="center", fontsize=7, weight="bold")
    caja(ax, xL, ys[0], W, H, "Registros identificados (n = {}):\n".format(ident["total"]) +
         "\n".join(f"{k}: {v}" for k, v in ident.items() if k != "total"))
    caja(ax, xR, ys[0], 0.25, H, f"Registros eliminados antes del cribado:\nduplicados y versiones\ndel mismo estudio (n = {b['duplicados_eliminados']})")
    caja(ax, xL, ys[1], W, H, f"Registros cribados\n(título y resumen)\n(n = {b['cribados']})")
    caja(ax, xR, ys[1], 0.25, H, "Registros excluidos (n = {})\n".format(b["excluidos_cribado"]) +
         en_lineas(f"{k}: {v}" for k, v in b["excluidos_cribado_por_codigo"].items()))
    caja(ax, xL, ys[2], W, H, f"Informes buscados para\nrecuperación (n = {b['buscados']})")
    caja(ax, xR, ys[2], 0.25, H, f"Informes no recuperados\n(n = {b['no_recuperados']})")
    caja(ax, xL, ys[3], W, H, f"Informes evaluados\n(texto completo)\n(n = {b['evaluados']})")
    caja(ax, xR, ys[3], 0.25, H, "Informes excluidos (n = {})\n".format(b["excluidos_texto_completo"]) +
         en_lineas(f"{k.split(' ')[0]}: {v}" for k, v in b["excluidos_texto_completo_por_motivo"].items()))
    caja(ax, 0.20, ys[4], 0.40, 0.12, f"Estudios incluidos en la revisión (n = {b['incluidos'] + o['incluidos']})\n"
         f"bases: {b['incluidos']} · otros métodos: {o['incluidos']}", color="#EAF2FA")
    caja(ax, xO, ys[0], 0.20, H, f"Bola de nieve desde {o['estudios_de_inicio']}\nestudios multiturno:\nOpenAlex n = {o['registros_identificados_openalex']}\nSemantic Scholar n = {o['registros_identificados_semantic_scholar']}")
    caja(ax, xO, ys[1], 0.20, H, f"Registros cribados\n(n = {o['cribados']})")
    caja(ax, xOR, ys[1], 0.15, H, f"Excluidos (n = {o['excluidos_cribado']});\nduplicados de\nregistros previos (E9)\n(n = {o['duplicados_tras_cribado_E9']})")
    caja(ax, xO, ys[2], 0.20, H, f"Informes buscados\n(n = {o['buscados']})")
    caja(ax, xOR, ys[2], 0.15, H, f"No recuperados\n(n = {o['no_recuperados']})")
    caja(ax, xO, ys[3], 0.20, H, f"Informes evaluados\n(n = {o['evaluados']})")
    caja(ax, xOR, ys[3], 0.15, H, "Excluidos (n = {})\n".format(o["excluidos_texto_completo"]) +
         "\n".join(f"{k.split(' ')[0]}: {v}" for k, v in o["excluidos_texto_completo_por_motivo"].items()))
    for y0, y1 in zip(ys[:3], ys[1:4]):
        flecha(ax, xL + W / 2, y0, xL + W / 2, y1 + H)
        flecha(ax, xO + 0.10, y0, xO + 0.10, y1 + H)
    for y in ys[:4]:
        flecha(ax, xL + W, y + H / 2, xR, y + H / 2)
        if y != ys[0]:
            flecha(ax, xO + 0.20, y + H / 2, xOR, y + H / 2)
    flecha(ax, xL + W / 2, ys[3], 0.30, ys[4] + 0.12)
    flecha(ax, xO + 0.10, ys[3], 0.50, ys[4] + 0.12)
    guardar(fig, "prisma_flujo", leyenda="Diagrama de flujo PRISMA 2020 de la selección de estudios. E1–E9: códigos de exclusión "
            "del protocolo; E9 = informe secundario de un estudio ya incluido (versiones preprint/publicada o doble indexación), "
            "cuyo identificador se conserva en el informe primario.")
    print(json.dumps(c, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
