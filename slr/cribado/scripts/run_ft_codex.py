"""Run blinded full-text screening as isolated, headless Codex sessions.

Run from ``slr/cribado``. Calibration example::

    python scripts/run_ft_codex.py --calibration \
        --out sr_work/runs/codex_calib --jobs 4

Every prompt is handled by a fresh, ephemeral ``codex exec`` process. Successful
results are resumable; invalid or failed calls are retained as ``*.error.json``.
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ft_coord  # noqa: E402


HERE = Path(__file__).resolve().parent
C = HERE.parent
SLR = C.parent
PROMPTS = C / "sr_work" / "prompts_ft"
MANUAL = C / "sr_work" / "runs" / "manual_ft"
CLI = C / "sr_work" / "runs" / "cli_ft"
CALIB_OUT = C / "sr_work" / "runs" / "codex_calib"
CALIB_SHORT_OUT = C / "sr_work" / "runs" / "codex_calib_short"
PROMPTS_CALIB = C / "sr_work" / "prompts_ft_calib"
PROD_OUT = C / "sr_work" / "runs" / "codex_ft"
ORDER = C / "sr_work" / "ft_order.json"

MODEL = "gpt-6.1-sol"
REASONING = "medium"
SOURCE = f"codex:{MODEL}"
REPORT_RE = re.compile(r"^Use only the Read tool, on this file: (.+)$", re.MULTILINE)
STEM_RE = re.compile(r"^FT[AB]_(R\d+)$")
VALID_D = {"include", "exclude", "unclear"}
VALID_CODE = {"INC", "UNC", *(f"E{i}" for i in range(1, 10))}


def read_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def write_json_atomic(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False)
            handle.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def valid_decision_payload(payload, expected_id):
    if not isinstance(payload, dict) or set(payload) != {"decisions"}:
        return False, "top-level JSON must contain only decisions"
    decisions = payload.get("decisions")
    if not isinstance(decisions, list) or len(decisions) != 1:
        return False, "decisions must contain exactly one object"
    decision = decisions[0]
    required = {"id", "d", "code", "why", "where"}
    if not isinstance(decision, dict) or set(decision) != required:
        return False, "decision fields are invalid"
    if decision["id"] != expected_id:
        return False, f"decision id is not {expected_id}"
    if decision["d"] not in VALID_D or decision["code"] not in VALID_CODE:
        return False, "decision or code is outside the allowed vocabulary"
    expected_code = {"include": "INC", "unclear": "UNC"}.get(decision["d"])
    if expected_code and decision["code"] != expected_code:
        return False, "decision and code are inconsistent"
    if decision["d"] == "exclude" and not decision["code"].startswith("E"):
        return False, "exclude requires an E1-E9 code"
    if not isinstance(decision["why"], str) or not isinstance(decision["where"], str):
        return False, "why and where must be strings"
    return True, ""


def valid_result_file(path, expected_id=None):
    try:
        value = read_json(path)
        if expected_id is None:
            match = STEM_RE.match(Path(path).stem)
            expected_id = match.group(1) if match else None
        if not expected_id or not isinstance(value, dict):
            return False
        payload = {"decisions": value.get("decisions")}
        ok, _ = valid_decision_payload(payload, expected_id)
        return ok and isinstance(value.get("label"), str) and isinstance(value.get("source"), str)
    except (OSError, ValueError, TypeError):
        return False


def result_stems(directory):
    directory = Path(directory)
    if not directory.is_dir():
        return set()
    return {
        path.stem
        for path in directory.glob("FT[AB]_R*.json")
        if not path.name.endswith(".error.json") and valid_result_file(path)
    }


def reference_stems():
    stems = set()
    for directory in (MANUAL, CLI):
        if not directory.is_dir():
            continue
        for path in directory.glob("FT[AB]_R*.json"):
            if path.name.endswith(".error.json"):
                continue
            match = STEM_RE.match(path.stem)
            if not match:
                continue
            try:
                payload = reference_payload(path)
                ok, _ = valid_decision_payload(payload, match.group(1))
            except (OSError, ValueError, TypeError):
                ok = False
            if ok:
                stems.add(path.stem)
    return stems


def reference_payload(path):
    value = read_json(path)
    if isinstance(value.get("decisions"), list):
        return {"decisions": value["decisions"]}
    result = value.get("result")
    if isinstance(result, str):
        stripped = result.strip()
        if stripped.startswith("```json") and stripped.endswith("```"):
            result = stripped[7:-3].strip()
        return json.loads(result)
    raise ValueError(f"no decisions in reference file {path}")


def reference_path(stem):
    candidates = [MANUAL / f"{stem}.json", CLI / f"{stem}.json"]
    expected_id = STEM_RE.match(stem).group(1)
    found = []
    payloads = []
    for path in candidates:
        if not path.is_file():
            continue
        try:
            payload = reference_payload(path)
            ok, _ = valid_decision_payload(payload, expected_id)
        except (OSError, ValueError, TypeError):
            ok = False
        if ok:
            found.append(path)
            payloads.append(payload)
    if not found:
        return None
    first = payloads[0]
    for payload in payloads[1:]:
        if payload != first:
            raise RuntimeError(f"conflicting reference decisions for {stem}")
    return found[0]


def calibration_entries(index, single_ids):
    by_stem = {Path(entry["prompt_file"]).stem: entry for entry in index}
    selected = []
    report_ids = []
    for report_id in single_ids:
        stems = [f"FTA_{report_id}", f"FTB_{report_id}"]
        if all(stem in by_stem and reference_path(stem) for stem in stems):
            report_ids.append(report_id)
            selected.extend(by_stem[stem] for stem in stems)
    if len(report_ids) != 8 or len(selected) != 16:
        raise RuntimeError(
            f"expected 8 calibration reports/16 prompts, found {len(report_ids)}/{len(selected)}"
        )
    return selected, report_ids


def production_entries(index, single_ids, out):
    """Reports owned by (or free for) Codex, taken from the END of the priority order (ft_coord)."""
    selected = []
    for report_id, entries in ft_coord.plan(index, single_ids, "codex", from_end=True):
        for entry in entries:
            entry = dict(entry, _report=report_id)
            selected.append(entry)
    return [entry for entry in selected if _retry_ok(entry, out)]


def _retry_ok(entry, out):
    if True:
        stem = Path(entry["prompt_file"]).stem
        error_path = out / f"{stem}.error.json"
        attempts = 0
        if error_path.is_file():
            try:
                attempts = int(read_json(error_path).get("attempts", 1))
            except (OSError, ValueError, TypeError):
                attempts = 1
        return attempts < 2


def ordered(entries, rank):
    return sorted(
        entries,
        key=lambda entry: (
            rank.get(Path(entry["prompt_file"]).stem.split("_", 1)[1], 10**9),
            entry["prompt_file"],
        ),
    )


def report_path(prompt_path):
    text = Path(prompt_path).read_text(encoding="utf-8")
    match = REPORT_RE.search(text)
    if not match:
        raise ValueError(f"report path not found in {prompt_path}")
    path = Path(match.group(1).strip()).resolve()
    roots = {(SLR / "texto_completo" / "texto").resolve(), (SLR / "texto_completo" / "texto_calib").resolve()}
    if path.parent not in roots or not path.is_file():
        raise ValueError(f"invalid report path in {prompt_path}: {path}")
    return path


def run_one(entry, out):
    prompt = Path(entry["prompt_file"]).resolve()
    stem = prompt.stem
    match = STEM_RE.match(stem)
    if not match:
        return stem, False, 0.0, "invalid prompt stem"
    expected_id = match.group(1)
    started = time.monotonic()
    try:
        report = report_path(prompt)
        message = (
            f"Your complete task instructions are in the file {prompt} (prompt file {prompt.name}). "
            'Read that file and follow it exactly. Return only the JSON object with "decisions" '
            "that it asks for."
        )
        with tempfile.TemporaryDirectory(prefix=f"codex-ft-{stem}-") as work:
            last = Path(work) / "last-message.json"
            cmd = [
                "codex", "exec", "--model", MODEL,
                "-c", f'model_reasoning_effort="{REASONING}"',
                "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral",
                "--ignore-user-config", "--ignore-rules", "--cd", work,
                "--output-last-message", str(last), message,
            ]
            process = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
            raw = last.read_text(encoding="utf-8") if last.is_file() else ""
        if process.returncode != 0:
            raise RuntimeError(f"codex exit {process.returncode}: {(process.stderr or '')[-1000:]}")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid final JSON: {exc}; output: {raw[-1000:]}") from exc
        ok, reason = valid_decision_payload(payload, expected_id)
        if not ok:
            raise ValueError(reason)
        result = {
            "label": entry["label"],
            "decisions": payload["decisions"],
            "source": SOURCE,
        }
        write_json_atomic(out / f"{stem}.json", result)
        old_error = out / f"{stem}.error.json"
        if old_error.exists():
            old_error.unlink()
        return stem, True, time.monotonic() - started, ""
    except Exception as exc:  # Preserve every failed call for explicit retry.
        error_path = out / f"{stem}.error.json"
        attempts = 1
        if error_path.is_file():
            try:
                attempts = int(read_json(error_path).get("attempts", 1)) + 1
            except (OSError, ValueError, TypeError):
                attempts = 2
        error = {
            "label": entry.get("label"),
            "source": SOURCE,
            "is_error": True,
            "attempts": attempts,
            "error": str(exc),
            "seconds": round(time.monotonic() - started, 1),
        }
        write_json_atomic(error_path, error)
        return stem, False, time.monotonic() - started, str(exc)[:160]


def model_metadata(mode):
    return {
        "model": MODEL,
        "reasoning": REASONING,
        "source": SOURCE,
        "mode": mode,
        "sandbox": "read-only",
        "session": "ephemeral",
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompts", default=str(PROMPTS))
    parser.add_argument("--out", default=str(PROD_OUT))
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--limit", type=int, default=0, help="max calls (0 = all pending)")
    parser.add_argument("--calibration", action="store_true")
    parser.add_argument("--calib-short", action="store_true", help="excerpt calibration (prompts_ft_calib)")
    parser.add_argument("--dry-run", action="store_true", help="show selection without calls or writes")
    args = parser.parse_args()

    if args.jobs < 1 or args.limit < 0:
        parser.error("--jobs must be positive and --limit cannot be negative")
    out = Path(args.out).resolve()
    if args.calib_short and args.out == str(PROD_OUT):
        out = CALIB_SHORT_OUT.resolve()
    allowed_out = (CALIB_SHORT_OUT if args.calib_short else CALIB_OUT if args.calibration else PROD_OUT).resolve()
    if out != allowed_out:
        parser.error(f"output for this mode must be {allowed_out}")

    prompts = PROMPTS_CALIB.resolve() if args.calib_short else Path(args.prompts).resolve()
    if prompts not in (PROMPTS.resolve(), PROMPTS_CALIB.resolve()):
        parser.error(f"--prompts must be {PROMPTS.resolve()}")
    index = read_json(prompts / "index.json")
    order = read_json(ORDER)
    single_ids = order["single"]
    rank = {report_id: i for i, report_id in enumerate(order["multiturn"] + single_ids)}

    if args.calib_short:
        have = result_stems(out)
        todo = [entry for entry in index if Path(entry["prompt_file"]).stem not in have]
        mode_note = "excerpt calibration"
    elif args.calibration:
        candidates, report_ids = calibration_entries(index, single_ids)
        have = result_stems(out)
        todo = [entry for entry in candidates if Path(entry["prompt_file"]).stem not in have]
        mode_note = f"calibration reports: {','.join(report_ids)}"
    else:
        todo = production_entries(index, single_ids, out)
        mode_note = "production"
    if args.calibration:
        todo = ordered(todo, rank)
    if args.limit:
        todo = todo[:args.limit]

    print(f"{mode_note}; pending calls: {len(todo)}", flush=True)
    if args.dry_run:
        for entry in todo:
            print(Path(entry["prompt_file"]).stem)
        return

    out.mkdir(parents=True, exist_ok=True)
    mode = "calibration-excerpt" if args.calib_short else "calibration" if args.calibration else "production"
    write_json_atomic(out / "_model.json", model_metadata(mode))
    started = time.monotonic()
    ok_count = error_count = 0
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        def claimed(entries):
            for entry in entries:
                report_id = entry.get("_report")
                if report_id is None or ft_coord.claim(report_id, "codex"):
                    yield entry

        iterator = claimed(todo)
        futures = {}
        for entry in iterator:
            futures[executor.submit(run_one, entry, out)] = entry
            if len(futures) == args.jobs:
                break
        completed = consecutive_errors = 0
        halted = False
        while futures:
            done, _ = cf.wait(futures, return_when=cf.FIRST_COMPLETED)
            for future in done:
                futures.pop(future)
                stem, ok, seconds, detail = future.result()
                completed += 1
                ok_count += int(ok)
                error_count += int(not ok)
                consecutive_errors = 0 if ok else consecutive_errors + 1
                suffix = "ok" if ok else f"ERROR {detail}"
                print(f"[{completed}/{len(todo)}] {stem} {suffix} ({seconds:.1f}s)", flush=True)
            if not halted and consecutive_errors >= max(4, args.jobs):
                halted = True
                print("repeated errors detected; stopping new dispatch for a safe resume", flush=True)
            if not halted:
                while len(futures) < args.jobs:
                    try:
                        entry = next(iterator)
                    except StopIteration:
                        break
                    futures[executor.submit(run_one, entry, out)] = entry
    elapsed = time.monotonic() - started
    print(f"done: ok {ok_count}, errors {error_count}, elapsed {elapsed:.1f}s", flush=True)


if __name__ == "__main__":
    main()
