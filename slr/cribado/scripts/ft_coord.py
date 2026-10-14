"""Shared coordination for the full-text reviewer runners (Claude: run_ft_cli.py, Codex: run_ft_codex.py).

Rule: both reviews (A and B) of a report are done by the SAME runner/model. A report belongs to
  1. the runner that already has a decision for it (any of A/B), else
  2. the runner holding its claim file sr_work/runs/claims/<id> (created atomically), else
  3. nobody: the next runner that dispatches it claims it.
Claude takes free reports from the start of the priority order, Codex from the end, so they meet
in the middle. A runner stopped by a usage limit keeps its claims and resumes them on the next run.
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.abspath(os.path.join(HERE, ".."))
RUNS = os.path.join(C, "sr_work", "runs")
CLAIMS = os.path.join(RUNS, "claims")
DIRS = {"claude": ["manual_ft", "cli_ft"], "codex": ["codex_ft"]}
STEM = re.compile(r"^(FT[AB])_(R\d{5})$")


def _valid(path):
    try:
        j = json.load(open(path, encoding="utf-8"))
    except Exception:
        return False
    if j.get("decisions"):
        return True
    return not j.get("is_error") and '"decisions"' in (j.get("result") or "")


def decided():
    """{stem: runner} for every valid decision file."""
    out = {}
    for runner, dirs in DIRS.items():
        for d in dirs:
            for f in glob.glob(os.path.join(RUNS, d, "FT[AB]_R*.json")):
                if f.endswith(".error.json"):
                    continue
                stem = os.path.basename(f)[:-5]
                if STEM.match(stem) and _valid(f):
                    out[stem] = runner
    return out


def owner(rid, done):
    for role in ("FTA", "FTB"):
        if f"{role}_{rid}" in done:
            return done[f"{role}_{rid}"]
    path = os.path.join(CLAIMS, rid)
    if os.path.exists(path):
        return open(path).read().strip() or None
    return None


def claim(rid, runner):
    """True if `runner` owns the report now (claimed before or claimed here)."""
    os.makedirs(CLAIMS, exist_ok=True)
    path = os.path.join(CLAIMS, rid)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, runner.encode())
        os.close(fd)
        return True
    except FileExistsError:
        return open(path).read().strip() == runner


def plan(index, order_ids, runner, from_end=False):
    """Prompt entries this runner should process now, grouped by report (A then B), in order."""
    done = decided()
    by_report = {}
    for e in index:
        m = STEM.match(os.path.basename(e["prompt_file"])[:-4])
        if m:
            by_report.setdefault(m.group(2), []).append(e)
    ids = list(reversed(order_ids)) if from_end else list(order_ids)
    todo = []
    for rid in ids:
        entries = [e for e in by_report.get(rid, []) if os.path.basename(e["prompt_file"])[:-4] not in done]
        if not entries:
            continue
        own = owner(rid, done)
        if own not in (None, runner):
            continue
        todo.append((rid, sorted(entries, key=lambda e: e["prompt_file"])))
    return todo


def release(runner):
    """Frees the claims of `runner` on reports it has not decided at all (A nor B), e.g. after a usage-limit
    stop, so the other runner can take them. Reports with a partial decision stay with their runner."""
    done = decided()
    freed = []
    if not os.path.isdir(CLAIMS):
        return freed
    for rid in os.listdir(CLAIMS):
        path = os.path.join(CLAIMS, rid)
        if open(path).read().strip() != runner:
            continue
        if not any(f"{r}_{rid}" in done for r in ("FTA", "FTB")):
            os.remove(path)
            freed.append(rid)
    return freed


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "release":
        print(f"released {len(release(sys.argv[2]))} claims of {sys.argv[2]}")
    else:
        print(f"{len(decided())} of 862 calls decided")
