"""Converts headless reviewer outputs (run_ft_cli.py) into decision files for merge_decisions.py --from.

Reads sr_work/runs/cli_ft/<prompt>.json, takes the last {"decisions": ...} object from the model's
answer verbatim, and writes {"label", "decisions", "source"} files (label from index.json, never typed).
Usage (from slr/cribado): python scripts/collect_cli_outputs.py <cli_dir> <out_dir>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collect_agent_outputs import last_decisions  # noqa: E402


def main(src, out):
    os.makedirs(out, exist_ok=True)
    n, bad = 0, []
    for f in sorted(os.listdir(src)):
        if not f.endswith(".json") or f.startswith("_") or f.endswith(".error.json"):
            continue
        j = json.load(open(os.path.join(src, f)))
        dec = last_decisions([j.get("result") or ""])
        if not dec:
            bad.append(f)
            continue
        json.dump({"label": j["_label"], "decisions": dec["decisions"], "source": f"cli:{f}"},
                  open(os.path.join(out, f), "w"), ensure_ascii=False, indent=1)
        n += 1
    print(f"written {n}; without decisions: {bad}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
