"""PI5 — verifies the per-turn rows extracted by Codex (runs_turnos_codex/) against the cited pages of each study's
text (same rule as for the results tables: the number must appear on the cited page, else anywhere in the text,
else the row is flagged and not used). Writes resultados_turnos.csv (all rows + `verificacion`).
Usage (from slr/extraccion): python scripts/verificar_turnos.py
"""
import csv
import glob
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
E = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(E)
sys.path.insert(0, HERE)
from l2_resolver import pages_text, verify  # noqa: E402

base = {r["id_estudio"]: r for r in csv.DictReader(open(os.path.join(E, "base_estudios.csv"), encoding="utf-8"))}
cols = ["id_estudio", "benchmark", "version", "particion", "metrica", "turno", "n_turno", "historial_eval", "sistema",
        "modelo_base", "valor", "ubicacion", "verificacion"]
out = []
for f in sorted(glob.glob(os.path.join(E, "runs_turnos_codex", "T_*.json"))):
    if f.endswith(".error.json"):
        continue
    j = json.load(open(f, encoding="utf-8"))
    d = json.loads(re.search(r'\{\s*"decisions".*\}', j["result"], re.S).group(0))["decisions"][0]
    sid = d["id_estudio"]
    full, pages = pages_text(os.path.join(SLR, base[sid]["texto"]))
    for r in d["extraccion"].get("resultados_turno") or []:
        r = dict(r, id_estudio=sid)
        r["verificacion"] = verify(r, ["valor"], full, pages)
        out.append(r)
with open(os.path.join(E, "resultados_turnos.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    w.writerows(out)
print(len(out), Counter(r["verificacion"] for r in out), "studies", len({r["id_estudio"] for r in out}))
