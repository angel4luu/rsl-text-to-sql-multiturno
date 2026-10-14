"""Full-text screening reviewers as isolated headless Claude Code sessions (instead of in-chat subagents).

Each call: `claude -p` with the sr-screener reviewer agent file as system prompt, Read as the only
tool (--restricted, no MCP servers, hooks or skills, no saved session), the model from index.json,
and the tool-generated prompt file (verbatim protocol + task). Every reviewer is a separate process
that sees only its own prompt and report: blinding as in the Agent-tool path.
Raw outputs go to sr_work/runs/cli_ft/<prompt>.json. Production runs are coordinated with the Codex runner
through scripts/ft_coord.py: A and B of a report always go to the same runner; Claude takes free reports
from the start of the priority order (sr_work/ft_order.json), Codex from the end; decided calls are skipped,
so the script can be stopped and resumed. Usage limits or errors are logged and the call is left for later.
Calibration (--calib): runs every prompt of sr_work/prompts_ft_calib into sr_work/runs/cli_calib_short.
Usage (from slr/cribado): python scripts/run_ft_cli.py [--jobs 8] [--limit N] [--calib]
"""
import argparse
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft_coord  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.abspath(os.path.join(HERE, ".."))
SLR = os.path.dirname(C)
AGENT = ("~/.claude/plugins/cache/academic-research-skills/academic-research-skills/3.23.0/"
         "agents/screening_reviewer_agent.md")


def system_prompt(out):
    text = open(AGENT, encoding="utf-8").read()
    body = text.split("---", 2)[2] if text.startswith("---") else text
    path = os.path.join(out, "_system_prompt.md")
    open(path, "w", encoding="utf-8").write(body.strip() + "\n")
    return path


def done_files(*dirs):
    have = set()
    for d in dirs:
        if os.path.isdir(d):
            for f in os.listdir(d):
                if not f.endswith(".json") or f.startswith("_"):
                    continue
                try:
                    j = json.load(open(os.path.join(d, f)))
                except Exception:
                    continue
                ok = "decisions" in j or (not j.get("is_error") and '"decisions"' in (j.get("result") or ""))
                if ok:
                    have.add(f[:-5])
    return have


def run_one(entry, sysprompt, out):
    fname = os.path.basename(entry["prompt_file"])
    stem = fname[:-4]
    msg = (f"Your complete task instructions are in the file {entry['prompt_file']} (prompt file {fname}). "
           "Read that file and follow it exactly. Return only the JSON object with \"decisions\" that it asks for.")
    cmd = ["claude", "-p", msg, "--model", entry["model"], "--system-prompt-file", sysprompt,
           "--tools", "Read", "--allowedTools", "Read", "--restricted", "--strict-mcp-config",
           "--disable-slash-commands", "--settings", '{"disableAllHooks":true}',
           "--no-session-persistence", "--output-format", "json"]
    t0 = time.time()
    p = subprocess.run(cmd, cwd=SLR, capture_output=True, text=True, timeout=900)
    try:
        res = json.loads(p.stdout)
    except Exception:
        res = {"is_error": True, "result": (p.stdout or "")[-500:], "stderr": (p.stderr or "")[-500:]}
    res["_label"] = entry["label"]
    res["_seconds"] = round(time.time() - t0, 1)
    ok = not res.get("is_error") and '"decisions"' in (res.get("result") or "")
    json.dump(res, open(os.path.join(out, stem + (".json" if ok else ".error.json")), "w"), ensure_ascii=False)
    return stem, ok, res.get("total_cost_usd") or 0, (res.get("result") or "")[:120]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0, help="max calls in this run (0 = all pending)")
    ap.add_argument("--calib", action="store_true", help="calibration of the excerpts (prompts_ft_calib)")
    ap.add_argument("--audit", action="store_true", help="audit of Codex decisions (prompts_ft_audit)")
    ap.add_argument("--adj", action="store_true", help="full-text adjudication of conflicts (prompts_ft_adj)")
    ap.add_argument("--qc", action="store_true", help="Opus second reading: unclear + multi-turn E6 (prompts_ft_qc)")
    a = ap.parse_args()
    if a.qc:
        a.calib = True  # independent blinded third reading with the tool's reviewer prompt; feeds the review sheet
        prompts, out = os.path.join(C, "sr_work", "prompts_ft_qc"), os.path.join(C, "sr_work", "runs", "cli_ft_qc")
    elif a.adj:
        a.calib = True  # run every prompt of the folder; decisions are merged with merge_decisions.py
        prompts, out = os.path.join(C, "sr_work", "prompts_ft_adj"), os.path.join(C, "sr_work", "runs", "cli_ft_adj")
    elif a.audit:
        a.calib = True  # same mechanics: run every prompt of the folder, never merged
        prompts, out = os.path.join(C, "sr_work", "prompts_ft_audit"), os.path.join(C, "sr_work", "runs", "cli_audit_codex")
    else:
        prompts = os.path.join(C, "sr_work", "prompts_ft_calib" if a.calib else "prompts_ft")
        out = os.path.join(C, "sr_work", "runs", "cli_calib_short" if a.calib else "cli_ft")
    os.makedirs(out, exist_ok=True)
    sysprompt = system_prompt(out)
    index = json.load(open(os.path.join(prompts, "index.json")))
    if a.calib:
        have = done_files(out)
        groups = [(None, [e for e in index if os.path.basename(e["prompt_file"])[:-4] not in have])]
    else:
        o = json.load(open(os.path.join(C, "sr_work", "ft_order.json")))
        groups = ft_coord.plan(index, o["multiturn"] + o["single"], "claude")
    if a.limit:
        groups, n = [g for g in groups], 0
        cut = []
        for g in groups:
            if n >= a.limit:
                break
            cut.append(g)
            n += len(g[1])
        groups = cut
    print(f"pending calls this run: {sum(len(e) for _, e in groups)}", flush=True)
    n_ok = n_err = 0
    cost = 0.0
    stop = False
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        futs, it = set(), iter(groups)

        def feed():
            # claim reports lazily (one at a time), so unstarted ones stay free for the Codex runner
            while len(futs) < a.jobs and not stop:
                try:
                    rid, entries = next(it)
                except StopIteration:
                    return
                if rid and not ft_coord.claim(rid, "claude"):
                    continue  # taken by the Codex runner meanwhile
                for e in entries:
                    futs.add(ex.submit(run_one, e, sysprompt, out))

        feed()
        i = 0
        while futs:
            done_f, _ = cf.wait(futs, return_when=cf.FIRST_COMPLETED)
            for f in done_f:
                futs.discard(f)
                stem, ok, c, snippet = f.result()
                i += 1
                cost += c
                n_ok += ok
                n_err += not ok
                print(f"[{i}] {stem} {'ok' if ok else 'ERROR ' + snippet}", flush=True)
            if not stop and n_err >= 10 and n_err > n_ok:
                stop = True
                print("too many errors (usage limit?) - stopping; rerun later to resume", flush=True)
            feed()
    if not a.calib:
        freed = ft_coord.release("claude")
        print(f"released {len(freed)} unstarted claims for the Codex runner", flush=True)
    print(f"done: ok {n_ok}, errors {n_err}, model usage reported ${cost:.2f}", flush=True)


if __name__ == "__main__":
    main()
