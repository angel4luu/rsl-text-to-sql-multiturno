#!/bin/sh
# Headless Sonnet run of ARS outline mode (Phase 11, step 1). Output: run/esquema.json (+ esquema_articulo.md).
cd "$(dirname "$0")/../../.." || exit 1
claude -p "Your complete task instructions are in latex/slr/plan/prompt_esquema.md. Read it and follow it exactly." \
  --model sonnet --tools Read,Glob,Grep --allowedTools Read,Glob,Grep \
  --disable-slash-commands --settings '{"disableAllHooks":true}' --no-session-persistence \
  --output-format json > latex/slr/plan/run/esquema.json
python3 -c "import json;d=json.load(open('latex/slr/plan/run/esquema.json'));open('latex/slr/plan/esquema_articulo.md','w').write(d['result']);print('cost', d.get('total_cost_usd'), 'error', d.get('is_error'))"
