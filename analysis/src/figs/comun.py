"""Shared paths and loaders for the synthesis scripts (Phase 10). Not a figure script."""
import csv
import json
import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SLR = RAIZ / "slr"
EXT = SLR / "extraccion"
TABLAS = SLR / "sintesis" / "tablas"
TABLAS.mkdir(parents=True, exist_ok=True)
KW_MT = ["multi-turn", "multi turn", "conversational", "context-dependent", "sparc", "cosql", "dialogue", "dialog"]


def leer_csv(path):
    return list(csv.DictReader(open(path, encoding="utf-8")))


def leer_json(path):
    return json.load(open(path, encoding="utf-8"))


def estudios():
    return leer_csv(EXT / "extraccion.csv")


def lista(v):
    v = (v or "").strip()
    return [x.strip().upper() for x in v.split(";") if x.strip() and x.strip().upper() not in ("NR", "NA")]


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def escribir_tabla(nombre, filas, columnas):
    with open(TABLAS / f"{nombre}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columnas, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
