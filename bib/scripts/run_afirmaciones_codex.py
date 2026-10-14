"""Phase 13, step 1b: runs the claim-support prompts (bib/afirmaciones/prompts/<key>.md) with Codex.

One fresh, ephemeral, read-only `codex exec` per reference (same model and reasoning for every call). A result is
kept only if it is valid JSON with exactly one judgement per claim id of that prompt and an allowed verdict;
otherwise the call is saved as <key>.error.json for an explicit retry (re-running the script retries only the
missing or failed keys). Outputs: bib/afirmaciones/runs/<key>.json.
Usage (from repo root): python3 bib/scripts/run_afirmaciones_codex.py [--jobs 4] [--only KEY ...]
"""
import argparse
import json
import re
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
A = RAIZ / "bib" / "afirmaciones"
RUNS = A / "runs"
MODEL, REASONING = "gpt-6.1-sol", "medium"
VEREDICTOS = {"supported", "partial", "unsupported", "cannot_judge"}


def validar(payload, clave, ids):
    if not isinstance(payload, dict) or payload.get("clave") != clave:
        return "wrong or missing 'clave'"
    js = payload.get("juicios")
    if not isinstance(js, list) or sorted(j.get("id") for j in js if isinstance(j, dict)) != sorted(ids):
        return "judgement ids do not match the prompt"
    for j in js:
        if j.get("veredicto") not in VEREDICTOS or not str(j.get("motivo", "")).strip():
            return f"invalid verdict or empty reason in {j.get('id')}"
    return ""


def correr(clave, ids):
    prompt = (A / "prompts" / f"{clave}.md").read_text(encoding="utf-8")
    t0 = time.monotonic()
    try:
        with tempfile.TemporaryDirectory(prefix=f"codex-af-{clave}-") as work:
            last = Path(work) / "last.json"
            cmd = ["codex", "exec", "--model", MODEL, "-c", f'model_reasoning_effort="{REASONING}"',
                   "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral", "--ignore-user-config",
                   "--ignore-rules", "--cd", work, "--output-last-message", str(last), prompt]
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
            raw = last.read_text(encoding="utf-8") if last.is_file() else ""
        if p.returncode != 0:
            raise RuntimeError(f"codex exit {p.returncode}: {(p.stderr or '')[-800:]}")
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip())
        payload = json.loads(raw)
        error = validar(payload, clave, ids)
        if error:
            raise ValueError(error)
        payload.update(modelo=f"codex:{MODEL}", razonamiento=REASONING)
        (RUNS / f"{clave}.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
        (RUNS / f"{clave}.error.json").unlink(missing_ok=True)
        return clave, True, time.monotonic() - t0, ""
    except Exception as e:  # kept for explicit retry, never filled in
        (RUNS / f"{clave}.error.json").write_text(json.dumps({"clave": clave, "error": str(e)}, ensure_ascii=False),
                                                 encoding="utf-8")
        return clave, False, time.monotonic() - t0, str(e)[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    RUNS.mkdir(exist_ok=True)
    afs = json.loads((A / "afirmaciones.json").read_text(encoding="utf-8"))
    ids = {}
    for x in afs:
        ids.setdefault(x["clave"], []).append(x["id"])
    pendientes = [k for k in sorted(ids) if (a.only is None or k in a.only) and not (RUNS / f"{k}.json").exists()]
    print(f"references: {len(ids)}; pending: {len(pendientes)}; model {MODEL} ({REASONING})")
    with ThreadPoolExecutor(a.jobs) as ex:
        for clave, ok, s, err in ex.map(lambda k: correr(k, ids[k]), pendientes):
            print(f"{'ok ' if ok else 'ERR'} {clave} ({s:.0f} s) {err}")
    hechos = sum((RUNS / f"{k}.json").exists() for k in ids)
    print(f"done: {hechos}/{len(ids)}; errors: {len(list(RUNS.glob('*.error.json')))}")


if __name__ == "__main__":
    main()
