#!/bin/sh
# Headless run of one Phase 11 drafting step. Usage: latex/slr/plan/run_paso.sh <paso> <model>
#   e.g. run_paso.sh 4a sonnet  -> prompt plan/prompt_4a.md, output plan/run/4a.json + section files (FILE markers)
cd "$(dirname "$0")/../../.." || exit 1
P=$1; M=${2:-sonnet}
claude -p "Your complete task instructions are in latex/slr/plan/prompt_$P.md. Read it and follow it exactly." \
  --model "$M" --tools Read,Glob,Grep --allowedTools Read,Glob,Grep \
  --disable-slash-commands --settings '{"disableAllHooks":true}' --no-session-persistence \
  --output-format json > "latex/slr/plan/run/$P.json"
python3 - "$P" <<'PY'
import json, re, sys
d = json.load(open(f"latex/slr/plan/run/{sys.argv[1]}.json"))
print("cost", d.get("total_cost_usd"), "error", d.get("is_error"))
parts = re.split(r"^%%%% FILE: (\S+)\s*$", re.sub(r"^```\w*\s*$", "", d["result"], flags=re.M), flags=re.M)
for name, body in zip(parts[1::2], parts[2::2]):
    open(f"latex/slr/secciones/{name}", "w", encoding="utf-8").write(body.strip() + "\n")
    print("wrote", name, len(body.split()), "words")
PY
