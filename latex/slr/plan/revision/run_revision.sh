#!/bin/sh
# Step 4f: five independent reviewer seats in parallel, then the editorial synthesis. Outputs informe_*.md here.
cd "$(dirname "$0")/../../../.." || exit 1
D=latex/slr/plan/revision
run() {  # $1 = name, $2 = model
  claude -p "Your complete task instructions are in $D/prompt_$1.md. Read it and follow it exactly." \
    --model "$2" --tools Read,Glob,Grep --allowedTools Read,Glob,Grep --disable-slash-commands \
    --settings '{"disableAllHooks":true}' --no-session-persistence --output-format json < /dev/null > "$D/run_$1.json"
  python3 -c "import json,sys;d=json.load(open('$D/run_$1.json'));open('$D/informe_$1.md','w').write(d['result']);print('$1', d.get('total_cost_usd'), 'error', d.get('is_error'))"
}
for s in eic methodology domain perspective devil; do run "$s" sonnet & done
wait
run sintesis sonnet
