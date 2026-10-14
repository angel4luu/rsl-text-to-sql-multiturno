"""Calibration of the screening excerpts (option 2) — prompts and comparison.

  prompts : copies the tool-generated Reviewer A prompt (sr_work/prompts_ft/FTA_<id>.txt) of each
            calibration report, changing ONLY the report path from texto/<id>.txt to texto_calib/<id>.txt;
            writes sr_work/prompts_ft_calib/ + index.json (labels prefixed "CALIB-", never merged).
  compare : compares each runner's excerpt decision with the full-text decision of the same report
            (Reviewer A from cli_ft/manual_ft) and prints agreement on include-vs-not and on the code.
Usage (from slr/cribado): python scripts/calibracion_extractos.py prompts R00003,R00128,...
                          python scripts/calibracion_extractos.py compare
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.abspath(os.path.join(HERE, ".."))
W = os.path.join(C, "sr_work")
P_SRC, P_CAL = os.path.join(W, "prompts_ft"), os.path.join(W, "prompts_ft_calib")


def first_decision(path):
    j = json.load(open(path, encoding="utf-8"))
    if j.get("decisions"):
        return j["decisions"][0]
    m = re.search(r'\{\s*"decisions".*\}', j.get("result") or "", re.S)
    return json.loads(m.group(0))["decisions"][0] if m else None


def prompts(ids):
    os.makedirs(P_CAL, exist_ok=True)
    labels = {os.path.basename(e["prompt_file"]): e for e in json.load(open(os.path.join(P_SRC, "index.json")))}
    index = []
    for rid in ids:
        name = f"FTA_{rid}.txt"
        text = open(os.path.join(P_SRC, name), encoding="utf-8").read()
        new = text.replace(f"/texto/{rid}.txt", f"/texto_calib/{rid}.txt")
        if new == text:
            sys.exit(f"{rid}: report path not found in prompt (PDF fallback?)")
        dst = os.path.join(P_CAL, name)
        open(dst, "w", encoding="utf-8").write(new)
        e = dict(labels[name])
        e.update(prompt_file=dst, label="CALIB-" + e["label"])
        index.append(e)
    json.dump(index, open(os.path.join(P_CAL, "index.json"), "w"), indent=1)
    print(f"{len(index)} calibration prompts in {P_CAL}")


def compare():
    ref = {}
    for d in ("manual_ft", "cli_ft"):
        for f in glob.glob(os.path.join(W, "runs", d, "FTA_R*.json")):
            if not f.endswith(".error.json"):
                ref[os.path.basename(f)[4:-5]] = first_decision(f)
    for runner, d in (("Claude", "cli_calib_short"), ("Codex", "codex_calib_short")):
        rows = []
        for f in sorted(glob.glob(os.path.join(W, "runs", d, "FTA_R*.json"))):
            if f.endswith(".error.json"):
                continue
            rid, x = os.path.basename(f)[4:-5], first_decision(f)
            r = ref.get(rid)
            if x and r:
                rows.append((rid, r["code"], x["code"]))
        if not rows:
            print(f"{runner}: no calibration results yet")
            continue
        adv = sum((a == "INC" or a == "UNC") == (b == "INC" or b == "UNC") for _, a, b in rows)
        same = sum(a == b for _, a, b in rows)
        print(f"{runner}: n={len(rows)}  include-vs-not agree {adv}/{len(rows)}  same code {same}/{len(rows)}")
        for rid, a, b in rows:
            print(f"   {rid}: full text {a:4} | excerpt {b:4} {'' if a == b else '<-- differs'}")


if __name__ == "__main__":
    if sys.argv[1] == "prompts":
        prompts(sys.argv[2].split(","))
    else:
        compare()
