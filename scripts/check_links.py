"""japan-exhibitions.json 안의 모든 링크(url, venueUrl)를 열어 보고 결과를 표로 남긴다."""
import json, sys, urllib.request, urllib.error, concurrent.futures, ssl

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
items = json.load(open("japan-exhibitions.json", encoding="utf-8"))["exhibitions"]
links = {}
for e in items:
    for key in ("url", "venueUrl"):
        if e.get(key):
            links.setdefault(e[key], []).append(f'{e["id"]}.{key}')

def check(url):
    req = urllib.request.Request(url.split("#")[0], headers={"User-Agent": UA, "Accept-Language": "ja,ko;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, url
    except Exception as e:
        return f"ERR {type(e).__name__}: {str(e)[:80]}", url

with concurrent.futures.ThreadPoolExecutor(8) as pool:
    results = dict(zip(links, pool.map(check, links)))

bad = [(u, s) for u, (s, f) in results.items() if s != 200]
moved = [(u, f) for u, (s, f) in results.items() if s == 200 and f.rstrip('/') != u.split('#')[0].rstrip('/')]
lines = ["# 링크 검사 결과", "", f"검사한 링크 {len(links)}개 · 열리지 않은 링크 {len(bad)}개 · 다른 주소로 넘어간 링크 {len(moved)}개", ""]
if bad:
    lines += ["## 열리지 않은 링크", "", "| 상태 | 주소 | 쓰인 곳 |", "|---|---|---|"]
    lines += [f"| {s} | {u} | {', '.join(links[u])} |" for u, s in bad]
    lines.append("")
if moved:
    lines += ["## 다른 주소로 넘어간 링크", "", "| 원래 주소 | 넘어간 주소 |", "|---|---|"]
    lines += [f"| {u} | {f} |" for u, f in moved]
report = "\n".join(lines) + "\n"
open("link-report.md", "w", encoding="utf-8").write(report)
print(report)
