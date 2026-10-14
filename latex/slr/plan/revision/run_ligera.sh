#!/bin/sh
# Step 4f (light): methodology + devil's-advocate seats in parallel; the author's decision sheet is built from both.
cd "$(dirname "$0")/../../../.." || exit 1
D=latex/slr/plan/revision
run() {
  claude -p "Your complete task instructions are in $D/prompt_$1.md. Read it and follow it exactly." \
    --model sonnet --tools Read,Glob,Grep --allowedTools Read,Glob,Grep --disable-slash-commands \
    --settings '{"disableAllHooks":true}' --no-session-persistence --output-format json < /dev/null > "$D/run_$1.json"
  python3 -c "import json;d=json.load(open('$D/run_$1.json'));open('$D/informe_$1.md','w').write(d['result']);print('$1', d.get('total_cost_usd'), 'error', d.get('is_error'))"
}
run methodology & run devil & wait
