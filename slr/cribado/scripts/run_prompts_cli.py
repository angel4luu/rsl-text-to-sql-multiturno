"""Generic headless runner: runs every prompt of a sr-screener prompt folder (index.json) that has no valid
result yet, as isolated `claude -p` sessions (same settings as run_ft_cli.py). Used for the snowball screening.
Usage (from slr/cribado): python scripts/run_prompts_cli.py <prompts_dir> <out_dir> [--jobs 8]
"""
import argparse
import concurrent.futures as cf
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_ft_cli import done_files, run_one, system_prompt  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompts")
    ap.add_argument("out")
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    a.prompts, a.out = os.path.abspath(a.prompts), os.path.abspath(a.out)
    os.makedirs(a.out, exist_ok=True)
    sp = system_prompt(a.out)
    have = done_files(a.out)
    todo = [e for e in json.load(open(os.path.join(a.prompts, "index.json")))
            if os.path.basename(e["prompt_file"])[:-4] not in have]
    print(f"pending calls: {len(todo)}", flush=True)
    ok = err = 0
    cost = 0.0
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for f in cf.as_completed([ex.submit(run_one, e, sp, a.out) for e in todo]):
            stem, good, c, snip = f.result()
            ok, err, cost = ok + good, err + (not good), cost + c
            print(f"{stem} {'ok' if good else 'ERROR ' + snip}", flush=True)
    print(f"done: ok {ok}, errors {err}, model usage reported ${cost:.2f}", flush=True)


if __name__ == "__main__":
    main()
