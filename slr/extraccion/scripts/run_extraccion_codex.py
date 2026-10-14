"""Run extraction prompts in fresh, isolated Codex CLI sessions."""

import argparse
import concurrent.futures as futures
import datetime as datetime
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
E = HERE.parent
TIE_PROMPTS = (E / "prompts_l1_desempate").resolve()
TIE_RUNS = (E / "runs_l1_desempate").resolve()
N2_PROMPTS = (E / "prompts_nivel2").resolve()
N2_RUNS = (E / "runs_nivel2_codex").resolve()
TURN_PROMPTS = (E / "prompts_turnos").resolve()
TURN_RUNS = (E / "runs_turnos_codex").resolve()
MODEL = "gpt-6.1-sol"
REASONING = "medium"


def read_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def write_json_atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def decode_result(raw):
    text = raw.strip()
    if text.startswith("```json") and text.endswith("```"):
        text = text[7:-3].strip()
    return json.loads(text)


def validate(raw, expected_ids):
    try:
        payload = decode_result(raw)
    except (json.JSONDecodeError, TypeError) as exc:
        return False, f"invalid final JSON: {exc}"
    if not isinstance(payload, dict) or set(payload) != {"decisions"}:
        return False, "top-level JSON must contain only decisions"
    decisions = payload["decisions"]
    if not isinstance(decisions, list) or len(decisions) != len(expected_ids):
        return False, f"expected {len(expected_ids)} decisions"
    found = []
    for decision in decisions:
        if not isinstance(decision, dict) or not isinstance(decision.get("extraccion"), dict):
            return False, "each decision needs id_estudio and extraccion"
        found.append(decision.get("id_estudio"))
    if set(found) != set(expected_ids) or len(found) != len(set(found)):
        return False, "decision IDs do not match the prompt"
    return True, ""


def valid_result(path, entry):
    try:
        wrapper = read_json(path)
        if wrapper.get("_label") != entry["label"] or not isinstance(wrapper.get("result"), str):
            return False
        return validate(wrapper["result"], entry["_ids"])[0]
    except (OSError, ValueError, TypeError):
        return False


def attempts_for(path):
    try:
        return int(read_json(path).get("attempts", 1))
    except (OSError, ValueError, TypeError):
        return 0


def run_one(entry, output, mode):
    prompt = Path(entry["prompt_file"]).resolve()
    stem = prompt.stem
    started = time.monotonic()
    try:
        if mode == "per-turn":
            message = (
                f"Your complete task instructions are in the file {prompt} (prompt file {prompt.name}). "
                'Read that file and follow it exactly. Return only the JSON object with "decisions" requested there.'
            )
        else:
            message = (
                f"Your complete task instructions are in {prompt}. Read that file and follow it exactly. "
                'Return only the JSON object with "decisions" requested there.'
            )
        with tempfile.TemporaryDirectory(prefix=f"codex-extraction-{stem}-") as work:
            last = Path(work) / "last-message.json"
            command = [
                "codex", "exec", "--model", MODEL,
                "-c", f'model_reasoning_effort="{REASONING}"',
                "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral",
                "--ignore-user-config", "--ignore-rules", "--cd", work,
                "--output-last-message", str(last), message,
            ]
            process = subprocess.run(command, capture_output=True, text=True, timeout=1800)
            raw = last.read_text(encoding="utf-8") if last.is_file() else ""
        if process.returncode:
            raise RuntimeError(f"codex exit {process.returncode}: {(process.stderr or '')[-1200:]}")
        valid, reason = validate(raw, entry["_ids"])
        if not valid:
            raise ValueError(reason)
        write_json_atomic(output / f"{stem}.json", {"result": raw, "_label": entry["label"]})
        error_path = output / f"{stem}.error.json"
        if error_path.exists():
            error_path.unlink()
        return stem, True, time.monotonic() - started, ""
    except Exception as exc:
        error_path = output / f"{stem}.error.json"
        attempt = attempts_for(error_path) + 1
        write_json_atomic(error_path, {
            "_label": entry.get("label"), "model": MODEL, "reasoning": REASONING,
            "is_error": True, "attempts": attempt, "error": str(exc),
            "seconds": round(time.monotonic() - started, 1),
        })
        return stem, False, time.monotonic() - started, str(exc)[:180]


def model_metadata(mode):
    return {
        "model": MODEL, "reasoning": REASONING, "mode": mode,
        "sandbox": "read-only", "session": "ephemeral",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompts", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--role", choices=("all", "B"), default="all")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.jobs < 1 or args.limit < 0:
        parser.error("--jobs must be positive and --limit cannot be negative")
    prompts, output = Path(args.prompts).resolve(), Path(args.out).resolve()
    allowed = {
        (TIE_PROMPTS, TIE_RUNS): "l1-tie-break",
        (N2_PROMPTS, N2_RUNS): "level2-B",
        (TURN_PROMPTS, TURN_RUNS): "per-turn",
    }
    mode = allowed.get((prompts, output))
    if mode is None:
        parser.error("prompt/output paths are outside the handoff allowlist")
    if mode == "level2-B" and args.role != "B":
        parser.error("Level-2 Codex runs must use --role B")
    index = read_json(prompts / "index.json")
    selected = []
    for raw_entry in index:
        entry = dict(raw_entry)
        stem = Path(entry["prompt_file"]).stem
        if args.role == "B" and not stem.startswith("B_"):
            continue
        entry["_ids"] = entry.get("ids") or [stem.removeprefix("B_").removeprefix("A_")]
        result_path = output / f"{stem}.json"
        error_path = output / f"{stem}.error.json"
        if not valid_result(result_path, entry) and attempts_for(error_path) < 2:
            selected.append(entry)
    if args.limit:
        selected = selected[:args.limit]
    print(f"{mode}; pending calls: {len(selected)}", flush=True)
    if args.dry_run:
        for entry in selected:
            print(Path(entry["prompt_file"]).stem)
        return
    output.mkdir(parents=True, exist_ok=True)
    write_json_atomic(output / "_model.json", model_metadata(mode))
    started = time.monotonic()
    ok_count = error_count = completed = 0
    with futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        iterator = iter(selected)
        active = {}
        for _ in range(min(args.jobs, len(selected))):
            entry = next(iterator)
            active[executor.submit(run_one, entry, output, mode)] = entry
        consecutive_errors = 0
        halted = False
        while active:
            done, _ = futures.wait(active, return_when=futures.FIRST_COMPLETED)
            for future in done:
                active.pop(future)
                stem, ok, seconds, detail = future.result()
                completed += 1
                ok_count += int(ok)
                error_count += int(not ok)
                consecutive_errors = 0 if ok else consecutive_errors + 1
                status = "ok" if ok else f"ERROR {detail}"
                print(f"[{completed}/{len(selected)}] {stem} {status} ({seconds:.1f}s)", flush=True)
            if consecutive_errors >= max(4, args.jobs):
                halted = True
                print("repeated errors detected; stopping new dispatch for a safe resume", flush=True)
            if not halted:
                while len(active) < args.jobs:
                    try:
                        entry = next(iterator)
                    except StopIteration:
                        break
                    active[executor.submit(run_one, entry, output, mode)] = entry
    print(f"done: ok {ok_count}, errors {error_count}, elapsed {time.monotonic() - started:.1f}s", flush=True)


if __name__ == "__main__":
    main()
