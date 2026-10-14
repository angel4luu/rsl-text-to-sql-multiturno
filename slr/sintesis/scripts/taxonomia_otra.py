"""Phase 10, step 4 — inductive consolidation of the OTRO/OTRA codes (plan_sintesis.md: "las categorías OTRA se
consolidan inductivamente y se reportan obligatoriamente").

Benchmarks and metrics written as OTRO:/OTRA: in resultados.csv / contrastes.csv get a canonical name (case, spacing,
version and sub-split variants merged) and a family. Registered codes (SPIDER, BIRD, SPARC, COSQL, CHASE, EX, QM, IM, ...)
keep their own family. The rules below are explicit and ordered (first match wins); anything unmatched -> "OTRAS".
Writes: tablas/taxonomia_otra.csv (original -> canonical, family, rows) and adds the columns benchmark_canonico,
benchmark_familia, metrica_canonica, metrica_familia to extraccion/resultados_taxonomia.csv and contrastes_taxonomia.csv
(the extraction files themselves are not modified). Usage (from slr/sintesis): python scripts/taxonomia_otra.py
"""
import collections
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.abspath(os.path.join(HERE, ".."))
EXT = os.path.join(os.path.dirname(S), "extraccion")

BENCH_REG = {"SPIDER": "Un turno estándar", "BIRD": "Un turno estándar", "WIKISQL": "Un turno estándar",
             "SPARC": "Multiturno conversacional", "COSQL": "Multiturno conversacional", "CHASE": "Multiturno conversacional"}
BENCH = [  # (family, regex on the name) — ordered
    ("Datos propios / industriales", r"baidu|production|produccion|propio|interno|fleet|business line|experience platform|^srd$|^mrd$|srd_bi|mrd_bi|srd-industry|mrd-industry|dataque|aep"),
    ("Interactivo / aclaración", r"interact|tide-bench|clarity|ambig|practiq|ehr-chatqa|splash|enterprisemem"),
    ("Diálogo orientado a tareas / estado del diálogo", r"multiwoz|airdialogue|restaurant|semplan"),
    ("QA conversacional / tabular híbrida", r"hybridqa|pacific|\bsqa\b|abg-coqa|coqa"),
    ("Multiturno conversacional", r"multisql|ar-sparc|mmsql|sparc|cosql|sesql|chase|spider2-mt|-mt\b|dysql|lost_in_conversation|followup|ehr-seqsql|mrd-bird|cqr"),
    ("Variantes de un turno (robustez, dominio, idioma)", r"spider|bird|cspider|dusql|livesql|mbpp|ehrsql|fiben|finscreen|adveta|kaggle|wikisql"),
]
MET_REG = {"EX": "Ejecución por pregunta", "EM": "Coincidencia exacta / lógica", "ESM": "Coincidencia exacta / lógica",
           "TS": "Ejecución por pregunta", "QM": "Coincidencia por pregunta (multiturno)", "IM": "Coincidencia por interacción (multiturno)",
           "VES": "Ejecución por pregunta", "LINKING_RECALL": "Vinculación de esquemas"}
MET = [
    ("Mejora / efecto de un componente", r"mejora|delta|corregidas|edit (de|in)creased|persistencia"),
    ("Ejecución por interacción (multiturno)", r"im[-_ ]?(ex|ts)|(ex|ts)\(im\)|\biex\b|^mts$|iaccs|sequence_state|em\(im\)"),
    ("Ejecución por pregunta", r"qm[-_ ]?(ex|ts)|(ex|ts)\(qm\)|\bqex\b|tdex|\bfx\b|executab|post-clarif\w* ex|database ?state ?match|databasestatematch|context-?aware ?match|contextawarematch|\buex\b|\bcea\b"),
    ("Coincidencia exacta / lógica", r"\blem\b|\bsem\b|lem_|sem_|\blx\b|em\(qm\)|qm-em|\betm\b|symbol accuracy|name acc|acccol|accop|accval|^accs$"),
    ("Éxito de tarea / agente", r"\bsr\b|sr[-_]|success|pass|progress|functional accuracy|episode"),
    ("Estado del diálogo / aclaración", r"\bjga\b|state acc|turn[_ ]accuracy|dialog_act|clarification|classification|clasificacion|slot|\blcr\b|crs@|trs@"),
    ("Generación de texto / respuesta", r"bleu|drop f1|post-clarify f1|answer_correct|^f1|grammar"),
    ("Recuperación / ordenamiento", r"kendall|recall@|avg\. (pre|rec|f1)|macro f1"),
    ("Ejecución por pregunta", r"^va$"),
    ("Estado del diálogo / aclaración", r"flight acc"),
    ("Calidad de la explicación (evaluación humana)", r"^ea_"),
    ("Exactitud no especificada", r"^acc\.?$|accuracy|wikisql acc"),
]


def fam(name, rules, default="Específicas del benchmark"):
    low = name.lower()
    for f, rx in rules:
        if re.search(rx, low):
            return f
    return default


def canon(name):
    n = re.sub(r"\s*\((propio|interno|private|spider-based|spider-derived|anclas de bird|tarea cqr|synthesized|adaptqa|"
               r"unspecified|lower is better|state-hash accuracy)[^)]*\)", "", name, flags=re.I)
    n = re.sub(r"[_\s]+", " ", n).strip()
    n = re.sub(r"\s*(\d+(\.\d+)?)$", "", n) if n.lower().startswith("multiwoz") else n
    n = re.sub(r"/.*$", "", n) if n.lower().startswith("dysql") else n
    return n.upper() if len(n) <= 6 else n


def clave(n):
    return re.sub(r"[^a-z0-9@^∧]", "", n.lower())


def main():
    # canonical metric name = the most frequent spelling among names with the same key (case/punctuation-insensitive)
    freq = collections.Counter()
    for name in ("resultados", "contrastes"):
        for r in csv.DictReader(open(os.path.join(EXT, f"{name}.csv"), encoding="utf-8")):
            m = (r.get("metrica") or "").strip()
            if re.match(r"OTR[OA]\s*:", m, re.I):
                freq[canon(re.sub(r"^OTR[OA]\s*:\s*", "", m, flags=re.I))] += 1
    best = {}
    for n, c in freq.most_common():
        best.setdefault(clave(n), n)
    stats = collections.defaultdict(lambda: [None, None, 0])
    for name in ("resultados", "contrastes"):
        rows = list(csv.DictReader(open(os.path.join(EXT, f"{name}.csv"), encoding="utf-8")))
        for r in rows:
            b, m = (r.get("benchmark") or "").strip(), (r.get("metrica") or "").strip()
            if re.match(r"OTR[OA]\s*:", b, re.I):
                raw = re.sub(r"^OTR[OA]\s*:\s*", "", b, flags=re.I)
                r["benchmark_canonico"], r["benchmark_familia"] = canon(raw), fam(raw, BENCH)
                stats[("benchmark", raw)] = [r["benchmark_canonico"], r["benchmark_familia"], stats[("benchmark", raw)][2] + 1]
            else:
                r["benchmark_canonico"], r["benchmark_familia"] = b.upper(), BENCH_REG.get(b.upper(), "OTRAS")
            if re.match(r"OTR[OA]\s*:", m, re.I):
                raw = re.sub(r"^OTR[OA]\s*:\s*", "", m, flags=re.I)
                r["metrica_canonica"], r["metrica_familia"] = best[clave(canon(raw))], fam(raw, MET)
                stats[("metrica", raw)] = [r["metrica_canonica"], r["metrica_familia"], stats[("metrica", raw)][2] + 1]
            else:
                r["metrica_canonica"], r["metrica_familia"] = m.upper(), MET_REG.get(m.upper(), "OTRAS")
        cols = list(rows[0].keys())
        with open(os.path.join(EXT, f"{name}_taxonomia.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)
    os.makedirs(os.path.join(S, "tablas"), exist_ok=True)
    with open(os.path.join(S, "tablas", "taxonomia_otra.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["tipo", "original", "canonico", "familia", "filas"])
        for (t, raw), (c, f, n) in sorted(stats.items(), key=lambda kv: (kv[0][0], kv[1][1], kv[1][0])):
            w.writerow([t, raw, c, f, n])
    for t in ("benchmark", "metrica"):
        fc = collections.Counter(v[1] for k, v in stats.items() if k[0] == t)
        cc = len({v[0] for k, v in stats.items() if k[0] == t})
        print(t, f"{sum(1 for k in stats if k[0] == t)} names -> {cc} canonical", dict(fc))


if __name__ == "__main__":
    main()
