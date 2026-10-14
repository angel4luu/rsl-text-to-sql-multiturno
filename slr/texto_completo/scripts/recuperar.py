"""Phase 6 — full-text retrieval of the records advanced at title/abstract (include + unclear).

Free, legal routes only, tried in this order for each record:
  1. ACL Anthology  (DOI 10.18653/v1/<id> or aclanthology.org URL in the export) -> <id>.pdf
  2. arXiv          (DOI 10.48550/arXiv.<id> or arxiv.org URL in the export)      -> arxiv.org/pdf/<id>
  3. OpenAlex       (by DOI, or by exact title when there is no DOI): every location with a
                    pdf_url, best open-access location first (publisher, repository, arXiv copy).
A download counts only if the file starts with %PDF. PDFs are saved as pdf/<record id>.pdf
(gitignored) and every record gets one row in retrieval_log.csv. Resumable: records whose PDF
already exists are logged again without downloading.
Usage (from slr/texto_completo): python scripts/recuperar.py
"""
import argparse
import csv
import datetime
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..")
UA = {"User-Agent": "SLR-thesis-UNMSM (mailto:angela.jara@unmsm.edu.pe)"}
TODAY = datetime.date.today().isoformat()


def local_path(value):
    return value if os.path.isabs(value) else os.path.abspath(os.path.join(T, value))


def get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.geturl()


def get_json(url):
    try:
        return json.loads(get(url)[0])
    except Exception:
        return None


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def candidates(rec, raws):
    """(route, url, version) in order of preference."""
    out = []
    doi = (rec.get("doi") or "").lower()
    urls = [u for r in raws for u in r.get("UR", [])]
    acl = set()
    if doi.startswith("10.18653/v1/"):
        acl.add(doi.split("10.18653/v1/")[1])
    for u in urls:
        m = re.search(r"aclanthology\.org/([^/?#]+?)/?$", u)
        if m and not m.group(1).endswith(".pdf"):
            acl.add(m.group(1))
    out += [("ACL Anthology", f"https://aclanthology.org/{a}.pdf", "publishedVersion") for a in sorted(acl)]
    arx = set()
    m = re.match(r"10\.48550/arxiv\.(.+)", doi)
    if m:
        arx.add(m.group(1))
    for u in urls:
        m = re.search(r"arxiv\.org/(?:abs|pdf)/([^?#]+?)(?:\.pdf)?/?$", u)
        if m:
            arx.add(re.sub(r"v\d+$", "", m.group(1)))
    out += [("arXiv", f"https://arxiv.org/pdf/{a}", "submittedVersion") for a in sorted(arx)]
    work = None
    if doi:
        work = get_json("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
    if not work and rec.get("title"):
        q = urllib.parse.quote(re.sub(r"[^\w\s-]", " ", rec["title"])[:200])
        res = get_json(f"https://api.openalex.org/works?filter=title.search:{q}&per-page=5")
        for w in (res or {}).get("results", []):
            if norm(w.get("title")) == norm(rec["title"]):
                work = w
                break
    if work:
        locs = []
        if work.get("best_oa_location"):
            locs.append(work["best_oa_location"])
        locs += work.get("locations") or []
        seen = {u for _, u, _ in out}
        for loc in locs:
            u = loc.get("pdf_url")
            if u and u not in seen:
                seen.add(u)
                src = ((loc.get("source") or {}).get("display_name")) or urllib.parse.urlparse(u).netloc
                out.append((f"OpenAlex: {src}", u, loc.get("version") or ""))
    return out, (work or {}).get("open_access", {}).get("oa_status", "")


def fallbacks(rec):
    """Tried only when the routes above fail: arXiv copies of published papers.
    4. Semantic Scholar by DOI (externalIds.ArXiv, openAccessPdf)  5. arXiv API, exact title match."""
    out = []
    doi = rec.get("doi") or ""
    if doi:
        for attempt in range(3):
            try:
                p = json.loads(get("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi)
                                   + "?fields=externalIds,openAccessPdf")[0])
                break
            except urllib.error.HTTPError as e:
                p = None
                if e.code != 429:
                    break
                time.sleep(5 * (attempt + 1))
            except Exception:
                p = None
                break
        if p:
            ax = (p.get("externalIds") or {}).get("ArXiv")
            if ax:
                out.append(("Semantic Scholar → arXiv", f"https://arxiv.org/pdf/{ax}", "submittedVersion"))
            u = (p.get("openAccessPdf") or {}).get("url")
            if u:
                out.append(("Semantic Scholar", u, ""))
        time.sleep(1.1)
    if rec.get("title"):
        clean = re.sub(r"[^\w\s-]", " ", rec["title"])
        q = urllib.parse.quote('ti:"' + clean + '"')
        try:
            xml = get(f"http://export.arxiv.org/api/query?search_query={q}&max_results=5")[0].decode("utf-8", "replace")
        except Exception:
            xml = ""
        for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
            t = re.search(r"<title>(.*?)</title>", entry, re.S)
            i = re.search(r"<id>http://arxiv\.org/abs/(.*?)</id>", entry)
            if t and i and norm(t.group(1)) == norm(rec["title"]):
                axid = re.sub(r"v\d+$", "", i.group(1))
                out.append(("arXiv (título exacto)", "https://arxiv.org/pdf/" + axid, "submittedVersion"))
                break
        time.sleep(3.0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default="../cribado/sr_work")
    ap.add_argument("--pdf-dir", default="pdf")
    ap.add_argument("--log", default="retrieval_log.csv")
    args = ap.parse_args()
    work, pdf_dir, log = map(local_path, (args.work, args.pdf_dir, args.log))
    dec = json.load(open(os.path.join(work, "decisions.json")))
    recs = {r["id"]: r for r in json.load(open(os.path.join(work, "records.json")))["unique"]}
    raw = json.load(open(os.path.join(work, "raw_records.json")))
    ids = sorted(k for k, v in dec.items() if v["final"]["d"] != "exclude")
    os.makedirs(pdf_dir, exist_ok=True)
    old = {}
    if os.path.exists(log):
        old = {r["id"]: r for r in csv.DictReader(open(log, encoding="utf-8"))}
    rows = []
    for n, rid in enumerate(ids, 1):
        rec = recs[rid]
        row = {"id": rid, "ta": dec[rid]["final"]["d"], "doi": rec.get("doi") or "", "year": rec.get("year") or "",
               "title": rec.get("title") or "", "route": "", "version": "", "url": "", "oa_status": "",
               "status": "no_recuperado", "reason": "", "date": TODAY, "bytes": ""}
        path = os.path.join(pdf_dir, f"{rid}.pdf")
        cands, row["oa_status"] = candidates(rec, [raw[i] for i in rec.get("members", [])])
        if os.path.exists(path):
            prev = old.get(rid, {})
            if prev.get("status") == "recuperado":
                row.update({k: prev[k] for k in ("route", "url", "version", "date")})
            else:  # placed by hand after a run that could not retrieve it
                row.update(route="manual (autora)", version="por verificar")
            row.update(status="recuperado", reason="", bytes=os.path.getsize(path))
        else:
            errors = []
            tried = {u for _, u, _ in cands}
            more = [c for c in fallbacks(rec) if c[1] not in tried]
            for route, url, version in cands + more:
                try:
                    data, final = get(url, timeout=90)
                except Exception as e:
                    errors.append(f"{route}: {type(e).__name__}")
                    continue
                if not data.startswith(b"%PDF"):
                    errors.append(f"{route}: no es PDF")
                    continue
                open(path, "wb").write(data)
                row.update(route=route, url=final, version=version, status="recuperado", bytes=len(data))
                break
            if row["status"] != "recuperado":
                row["reason"] = "sin ruta de acceso abierto" if not cands + more else "; ".join(errors)[:300]
            time.sleep(1.0)
        rows.append(row)
        print(f"[{n}/{len(ids)}] {rid} {row['status']} {row['route']}", flush=True)
    with open(log, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    got = sum(r["status"] == "recuperado" for r in rows)
    print(f"retrieved {got}/{len(rows)}; not retrieved {len(rows) - got}")


if __name__ == "__main__":
    main()
