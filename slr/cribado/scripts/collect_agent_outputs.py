"""Collect reviewer-agent decisions verbatim from Claude Code subagent transcripts.

sr-screener's fallback path (no Workflow tool): one Agent call per prompt file, each returned
JSON saved as {"label": ..., "decisions": [...]} in a folder that merge_decisions.py --from reads.
This script reads the subagent transcripts (*.jsonl), identifies which prompt file each agent was
given (so the label comes from index.json, never typed by hand), extracts the final JSON object
with "decisions" and writes one file per label. Agents whose prompt is not in the index are ignored.

Usage: python collect_agent_outputs.py <subagents_dir> <prompts_dir_with_index.json> <out_dir>
"""
import glob
import json
import os
import re
import sys


def texts(obj):
    """Yield every text fragment and tool-input JSON inside a transcript line."""
    if isinstance(obj, dict):
        if obj.get("type") == "text" and isinstance(obj.get("text"), str):
            yield obj["text"]
        if obj.get("type") == "tool_use" and isinstance(obj.get("input"), dict):
            yield json.dumps(obj["input"])
        for v in obj.values():
            yield from texts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from texts(v)
    elif isinstance(obj, str):
        yield obj


def last_decisions(fragments):
    found = None
    for t in fragments:
        for m in re.finditer(r'\{\s*"decisions"\s*:', t):
            depth, j = 0, m.start()
            for k in range(m.start(), len(t)):
                if t[k] == "{":
                    depth += 1
                elif t[k] == "}":
                    depth -= 1
                    if depth == 0:
                        j = k + 1
                        break
            try:
                found = json.loads(t[m.start():j])
            except json.JSONDecodeError:
                pass
    return found


def main(sub_dir, prompts_dir, out_dir):
    index = json.load(open(os.path.join(prompts_dir, "index.json")))
    by_file = {os.path.basename(e["prompt_file"]): e["label"] for e in index}
    os.makedirs(out_dir, exist_ok=True)
    written, missing = 0, []
    for path in sorted(glob.glob(os.path.join(sub_dir, "agent-*.jsonl"))):
        lines = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
        frags = [t for l in lines for t in texts(l)]
        prompt = next((f for f in by_file if any(f in t for t in frags[:20])), None)
        if not prompt:
            continue
        dec = last_decisions(frags)
        label = by_file[prompt]
        if not dec:
            missing.append(prompt)
            continue
        name = label.split("@")[0].replace(":", "_")
        json.dump({"label": label, "decisions": dec["decisions"], "source_transcript": os.path.basename(path)},
                  open(os.path.join(out_dir, f"{name}.json"), "w"), ensure_ascii=False, indent=1)
        written += 1
        print(f"{name}: {len(dec['decisions'])} decisions  <- {os.path.basename(path)}")
    print(f"written {written}; without decisions: {missing}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
