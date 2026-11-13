#!/usr/bin/env python3
"""AI 关注动态：读 briefs/watchlist.md，拉取其中的订阅源，生成单文件 HTML（可选 JSON）。

只用标准库，零 CDN、零构建。订阅源条目只是线索，进 wiki 前须追到原文（见 AGENTS.md）。

用法：
  python3 tools/ai_watch.py                          # 写 output/personal/ai-watch.html
  python3 tools/ai_watch.py --days 3 --json /tmp/w.json
  python3 tools/ai_watch.py --artifact --out /tmp/w.html   # 输出 Artifact 用的页面片段
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TZ = dt.timezone(dt.timedelta(hours=8))  # 与每日简报一致（Asia/Singapore，UTC+8）
UA = "kb-ai-watch/1.0 (personal reading list)"
ATOM = "{http://www.w3.org/2005/Atom}"
DC = "{http://purl.org/dc/elements/1.1/}"
GROUPS = {"A": "Claude / Anthropic", "B": "工程实践", "C": "研究与行业"}
WEEKDAYS = "一二三四五六日"
XNEWS_ACCOUNT = "https://xnews.xgrowing.ai/accounts/{}"


# ---------- 名单解析 ----------

def parse_tables(md: str) -> dict[str, list[dict[str, str]]]:
    """按「## 节标题」收集该节下表格的行，每行是 {表头: 单元格}。"""
    sections: dict[str, list[dict[str, str]]] = {}
    current, header = None, None
    for line in md.splitlines():
        if line.startswith("## "):
            current, header = line[3:].strip(), None
            sections.setdefault(current, [])
            continue
        if current is None or not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
        elif not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            sections[current].append(dict(zip(header, cells)))
    return sections


def blank(v: str | None) -> bool:
    return not v or v.strip() in {"—", "-", ""}


# ---------- 抓取与解析 ----------

def fetch(url: str, limit: int = 4_000_000) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.read(limit)


def parse_date(s: str) -> dt.datetime | None:
    s = (s or "").strip()
    if not s:
        return None
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def text_of(el) -> str:
    return "".join(el.itertext()).strip() if el is not None else ""


def plain(s: str, n: int = 160) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n].rstrip() + "…"


def safe_url(u: str) -> str:
    u = (u or "").strip()
    return u if u.startswith(("https://", "http://")) else ""


def parse_feed(data: bytes) -> list[dict]:
    root = ET.fromstring(data)
    items = []
    if root.tag == ATOM + "feed":
        for e in root.findall(ATOM + "entry"):
            link = next((l.get("href", "") for l in e.findall(ATOM + "link")
                         if l.get("rel", "alternate") == "alternate"), "")
            items.append({
                "title": plain(text_of(e.find(ATOM + "title")), 200),
                "url": safe_url(link),
                "published": parse_date(text_of(e.find(ATOM + "published"))
                                        or text_of(e.find(ATOM + "updated"))),
                "excerpt": plain(text_of(e.find(ATOM + "summary"))
                                 or text_of(e.find(ATOM + "content"))),
            })
    else:
        for it in root.iter("item"):
            items.append({
                "title": plain(text_of(it.find("title")), 200),
                "url": safe_url(text_of(it.find("link"))),
                "published": parse_date(text_of(it.find("pubDate")) or text_of(it.find(DC + "date"))),
                "excerpt": plain(text_of(it.find("description"))),
            })
    return items


def parse_changelog(md: str, n: int = 2) -> list[dict]:
    versions: list[dict] = []
    for line in md.splitlines():
        m = re.match(r"^##\s+(\S+)", line)
        if m:
            if len(versions) == n:
                break
            versions.append({"version": m.group(1), "bullets": []})
        elif versions and line.startswith("- "):
            versions[-1]["bullets"].append(line[2:].strip())
    return versions


def collect(sources: list[dict], days: int, per_feed: int, now: dt.datetime):
    cutoff = now - dt.timedelta(days=days)

    def work(src: dict):
        st = {"name": src.get("名称", ""), "group": src.get("组", ""), "type": src.get("类型", "feed"),
              "url": safe_url(src.get("URL", "")), "ok": False, "latest": None,
              "recent": 0, "error": "", "versions": []}
        try:
            if not st["url"]:
                raise ValueError("URL 无效")
            if st["type"] == "changelog":
                st["versions"] = parse_changelog(fetch(st["url"], 200_000).decode("utf-8", "replace"))
                st["ok"] = bool(st["versions"])
                return st, []
            items = [i for i in parse_feed(fetch(st["url"])) if i["published"]]
            st["latest"] = max((i["published"] for i in items), default=None)
            recent = sorted((i for i in items if i["published"] >= cutoff),
                            key=lambda i: i["published"], reverse=True)
            st["ok"], st["recent"] = True, len(recent)
            for i in recent:
                i.update(source=st["name"], group=st["group"])
            return st, recent[:per_feed]
        except Exception as exc:  # 单个源失败不影响整页
            st["error"] = f"{type(exc).__name__}: {exc}"[:160]
            return st, []

    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(work, sources))
    statuses = [r[0] for r in results]
    seen, items = set(), []
    for _, recent in results:
        for i in recent:
            key = i["url"] or i["title"]
            if key not in seen:
                seen.add(key)
                items.append(i)
    items.sort(key=lambda i: i["published"], reverse=True)
    return statuses, items


# ---------- 渲染 ----------

E = lambda s: html.escape(str(s or ""), quote=True)  # noqa: E731


def link(url: str, label: str, cls: str = "") -> str:
    url = safe_url(url)
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{E(url)}" target="_blank" rel="noopener">{E(label)}</a>' if url else E(label)


def code_spans(s: str) -> str:
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", E(s))


def fmt_day(d: dt.datetime) -> str:
    d = d.astimezone(TZ)
    return f"{d.month} 月 {d.day} 日 · 周{WEEKDAYS[d.weekday()]}"


CSS = """
:root {
  /* 单栏阅读流：页眉摘要 → 分组筛选 → 按天时间线 → 版本 / X / 渠道 / 名单附录 */
  --paper: #ECEEE9; --sheet: #F7F8F5; --ink: #14181C; --ink-2: #4A545B; --ink-3: #6C767C;
  --rule: #BDC4C0; --rule-soft: #D7DCD8; --signal: #2447D6;
  --g-a: #2447D6; --g-a-tint: rgba(36, 71, 214, 0.09);
  --g-b: #0F716D; --g-b-tint: rgba(15, 113, 109, 0.10);
  --g-c: #7B45A3; --g-c-tint: rgba(123, 69, 163, 0.10);
  --ok: #2B7449; --bad: #B8392A; --bad-tint: rgba(184, 57, 42, 0.09); --new: #94650F;
  --head: "Barlow Condensed", "PingFang SC", "Noto Sans SC", "Microsoft YaHei", system-ui, sans-serif;
  --sans: system-ui, -apple-system, "PingFang SC", "Noto Sans SC", "Microsoft YaHei", "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #0E1114; --sheet: #151A1E; --ink: #E3E7E4; --ink-2: #AEB6BA; --ink-3: #858E93;
  --rule: #313A40; --rule-soft: #232A30; --signal: #8CA3FF;
  --g-a: #8CA3FF; --g-a-tint: rgba(140, 163, 255, 0.12);
  --g-b: #5CC8C3; --g-b-tint: rgba(92, 200, 195, 0.12);
  --g-c: #C79BEA; --g-c-tint: rgba(199, 155, 234, 0.12);
  --ok: #6DC593; --bad: #F08A7C; --bad-tint: rgba(240, 138, 124, 0.12); --new: #E2B04A;
  color-scheme: dark; } }
:root[data-theme="dark"] {
  --paper: #0E1114; --sheet: #151A1E; --ink: #E3E7E4; --ink-2: #AEB6BA; --ink-3: #858E93;
  --rule: #313A40; --rule-soft: #232A30; --signal: #8CA3FF;
  --g-a: #8CA3FF; --g-a-tint: rgba(140, 163, 255, 0.12);
  --g-b: #5CC8C3; --g-b-tint: rgba(92, 200, 195, 0.12);
  --g-c: #C79BEA; --g-c-tint: rgba(199, 155, 234, 0.12);
  --ok: #6DC593; --bad: #F08A7C; --bad-tint: rgba(240, 138, 124, 0.12); --new: #E2B04A;
  color-scheme: dark; }
[hidden] { display: none !important; }
body { background: var(--paper); color: var(--ink); font: 15px/1.6 var(--sans); }
.wrap { max-width: 46rem; margin: 0 auto; padding-block: 28px 56px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
a { color: inherit; text-underline-offset: 2px; }
a:focus-visible, button:focus-visible, summary:focus-visible { outline: 2px solid var(--signal); outline-offset: 2px; border-radius: 3px; }
h1 { font: 700 2.1rem/1.15 var(--head); letter-spacing: 0.01em; margin: 0; text-wrap: balance; }
.meta { color: var(--ink-2); font-size: 0.86rem; margin: 6px 0 0; font-variant-numeric: tabular-nums; }
.stats { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0 0; padding: 0; list-style: none; }
.stats li { background: var(--sheet); border: 1px solid var(--rule-soft); border-radius: 6px; padding: 5px 10px;
  font-size: 0.84rem; color: var(--ink-2); font-variant-numeric: tabular-nums; }
.stats b { color: var(--ink); font-weight: 650; }
.stats .warn b { color: var(--bad); }
.filters { display: flex; flex-wrap: wrap; gap: 6px; margin: 22px 0 4px; }
.filters button { font: inherit; font-size: 0.84rem; color: var(--ink-2); background: transparent; cursor: pointer;
  border: 1px solid var(--rule); border-radius: 999px; padding: 3px 12px; font-variant-numeric: tabular-nums; }
.filters button[aria-pressed="true"] { background: var(--ink); border-color: var(--ink); color: var(--paper); }
h2 { font: 650 1.2rem/1.3 var(--head); letter-spacing: 0.02em; margin: 36px 0 4px; padding-top: 18px;
  border-top: 1px solid var(--rule); text-wrap: balance; }
.lede { color: var(--ink-2); font-size: 0.88rem; margin: 0 0 8px; }
.day h3 { font: 600 0.78rem/1 var(--sans); letter-spacing: 0.08em; color: var(--ink-3); margin: 20px 0 2px; }
.item { display: grid; grid-template-columns: 3.2rem minmax(0, 1fr); gap: 12px; padding: 11px 0;
  border-bottom: 1px solid var(--rule-soft); }
.time { font: 0.78rem/1.9 var(--mono); color: var(--ink-3); font-variant-numeric: tabular-nums; }
.src { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; font-size: 0.78rem; color: var(--ink-2); }
.g { font: 600 0.68rem/1.6 var(--mono); padding: 0 6px; border-radius: 4px; }
.g-A { color: var(--g-a); background: var(--g-a-tint); }
.g-B { color: var(--g-b); background: var(--g-b-tint); }
.g-C { color: var(--g-c); background: var(--g-c-tint); }
.new { font-size: 0.68rem; line-height: 1.5; color: var(--new); border: 1px solid currentColor; border-radius: 3px; padding: 0 4px; }
.title { margin: 2px 0 0; font-size: 1rem; line-height: 1.45; font-weight: 600; }
.title a { text-decoration: none; }
.title a:hover { text-decoration: underline; }
.ex { margin: 3px 0 0; color: var(--ink-2); font-size: 0.87rem; line-height: 1.55;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.empty { color: var(--ink-3); font-size: 0.9rem; padding: 14px 0; }
.panel { background: var(--sheet); border: 1px solid var(--rule-soft); border-radius: 8px; padding: 12px 16px; min-width: 0; }
.panel h3 { font: 600 0.95rem/1.4 var(--sans); margin: 0 0 6px; }
.panel ul { margin: 0; padding-left: 1.1rem; font-size: 0.88rem; }
.panel li { margin: 3px 0; }
.panel .muted { color: var(--ink-3); font-size: 0.82rem; margin: 0; }
code { font: 0.85em var(--mono); background: var(--rule-soft); border-radius: 3px; padding: 0 3px; overflow-wrap: anywhere; }
details { margin-top: 8px; }
summary { cursor: pointer; color: var(--ink-2); font-size: 0.88rem; }
.cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: 10px; margin-top: 8px; }
.acct { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 2px 10px; padding: 5px 0;
  border-bottom: 1px solid var(--rule-soft); font-size: 0.88rem; }
.acct:last-child { border-bottom: 0; }
.acct span { color: var(--ink-3); }
.links { margin: 6px 0 0; padding-left: 1.1rem; font-size: 0.9rem; }
.links li { margin: 4px 0; }
.links span { color: var(--ink-3); }
.tbl { overflow-x: auto; margin-top: 8px; }
table { border-collapse: collapse; width: 100%; font-size: 0.84rem; font-variant-numeric: tabular-nums; }
th, td { text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--rule-soft); vertical-align: top; }
th { color: var(--ink-3); font-weight: 600; white-space: nowrap; }
.st-ok { color: var(--ok); }
.st-bad { color: var(--bad); background: var(--bad-tint); border-radius: 3px; padding: 0 4px; }
footer { margin-top: 40px; padding-top: 14px; border-top: 1px solid var(--rule); color: var(--ink-3); font-size: 0.8rem; }
footer p { margin: 4px 0; }
"""

JS = """
(function () {
  var buttons = document.querySelectorAll('.filters button');
  var empty = document.getElementById('filter-empty');
  function apply(g) {
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.g === g)); });
    var shown = 0;
    document.querySelectorAll('.item[data-group]').forEach(function (el) {
      el.hidden = !(g === 'all' || el.dataset.group === g);
      if (!el.hidden) shown++;
    });
    document.querySelectorAll('.day').forEach(function (d) { d.hidden = !d.querySelector('.item:not([hidden])'); });
    if (empty) empty.hidden = shown > 0;
  }
  buttons.forEach(function (b) { b.addEventListener('click', function () { apply(b.dataset.g); }); });
})();
"""


def render(people, sources_status, items, manual, days, now, artifact: bool) -> str:
    gen = now.astimezone(TZ)
    new_cut = now - dt.timedelta(hours=24)
    feeds = [s for s in sources_status if s["type"] != "changelog"]
    ok_feeds = sum(1 for s in feeds if s["ok"])
    gaps = [p for p in people if p.get("状态") == "缺口"]
    on_xnews = [p for p in people if not blank(p.get("XNews"))]
    n_new = sum(1 for i in items if i["published"] >= new_cut)
    out: list[str] = []
    w = out.append

    if artifact:
        w('<title>AI 关注动态</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
    w(f'<meta name="canonical-source" content="briefs/watchlist.md">'
      f'<meta name="generated" content="{gen.isoformat(timespec="minutes")}">')
    w(f"<style>{CSS}</style>")
    w('<main class="wrap" lang="zh-CN">')
    w("<header><h1>AI 关注动态</h1>")
    w(f'<p class="meta">生成于 {gen:%Y-%m-%d %H:%M}（UTC+8）· 时间窗：近 {days} 天 · '
      f"名单 {len(people)} 个对象 · {len(feeds)} 个订阅源</p>")
    bad = len(feeds) - ok_feeds
    w('<ul class="stats">'
      f"<li><b>{len(items)}</b> 条更新</li>"
      f"<li>24 小时内 <b>{n_new}</b> 条</li>"
      f'<li{" class=\"warn\"" if bad else ""}>订阅源正常 <b>{ok_feeds}/{len(feeds)}</b></li>'
      f"<li>只在 X 发言 <b>{len(gaps)}</b> 人</li></ul></header>")

    # 分组筛选
    counts = {g: sum(1 for i in items if i["group"] == g) for g in GROUPS}
    w('<nav class="filters" aria-label="按分组筛选">'
      f'<button type="button" data-g="all" aria-pressed="true">全部 {len(items)}</button>')
    for g, label in GROUPS.items():
        w(f'<button type="button" data-g="{g}" aria-pressed="false">{g} · {E(label)} {counts[g]}</button>')
    w("</nav>")

    # 时间线
    w(f'<section aria-labelledby="h-feed"><h2 id="h-feed">最近更新</h2>'
      f'<p class="lede">名单内博客、周报与官方页面的新文章，按发布时间倒序；每个源最多显示若干条。</p>')
    if not items:
        w(f'<p class="empty">近 {days} 天名单内没有新文章。</p>')
    day_key = None
    for i in items:
        d = i["published"].astimezone(TZ)
        if d.date() != day_key:
            if day_key is not None:
                w("</div>")
            day_key = d.date()
            w(f'<div class="day"><h3>{E(fmt_day(d))}</h3>')
        badge = '<span class="new">24h 内</span>' if i["published"] >= new_cut else ""
        title = link(i["url"], i["title"] or i["url"] or "（无标题）")
        ex = f'<p class="ex">{E(i["excerpt"])}</p>' if i["excerpt"] else ""
        w(f'<article class="item" data-group="{E(i["group"])}"><div class="time">{d:%H:%M}</div><div>'
          f'<div class="src"><span class="g g-{E(i["group"])}">{E(i["group"])}</span>{E(i["source"])}{badge}</div>'
          f'<p class="title">{title}</p>{ex}</div></article>')
    if day_key is not None:
        w("</div>")
    w('<p class="empty" id="filter-empty" hidden>这个分组在时间窗内没有更新。</p></section>')

    # Claude Code 版本
    cl = next((s for s in sources_status if s["type"] == "changelog"), None)
    if cl:
        w('<section aria-labelledby="h-cc"><h2 id="h-cc">Claude Code 最新版本</h2>')
        if cl["versions"]:
            w('<p class="lede">取自 CHANGELOG.md 顶部，按版本号排列，没有发布日期。</p>')
            for k, v in enumerate(cl["versions"]):
                kinds: dict[str, list[str]] = {"新增": [], "改进": [], "修复": [], "其他": []}
                for b in v["bullets"]:
                    word = b.split(" ", 1)[0]
                    kind = ("新增" if word == "Added" else "修复" if word == "Fixed"
                            else "改进" if word in {"Improved", "Changed", "Updated", "Made", "Reduced"} else "其他")
                    kinds[kind].append(f"<li>{code_spans(b)}</li>")
                summary = " · ".join(f"{name} {len(xs)}" for name, xs in kinds.items() if xs)
                body = f'<p class="muted">{summary or "（无条目）"}</p>'
                for name, xs in kinds.items():
                    if not xs:
                        continue
                    if name == "新增" and len(xs) <= 30:
                        body += f"<ul>{''.join(xs)}</ul>"
                    else:
                        body += f"<details><summary>{name}（{len(xs)}）</summary><ul>{''.join(xs)}</ul></details>"
                if k == 0:
                    w(f'<div class="panel"><h3>{E(v["version"])}</h3>{body}</div>')
                else:
                    w(f"<details><summary>上一版 {E(v['version'])}</summary><div class=\"panel\">{body}</div></details>")
            w(f'<p class="lede" style="margin-top:8px">{link(cl["url"], "查看完整 CHANGELOG")}</p>')
        else:
            w(f'<p class="empty">CHANGELOG 读取失败：{E(cl["error"])}</p>')
        w("</section>")

    # X 账号
    def acct_row(p, via_xnews: bool):
        h = p.get("X 账号", "")
        handle = h.lstrip("@")
        xlink = link(f"https://x.com/{handle}", h) if h.startswith("@") else E(h)
        extra = f' · {link(XNEWS_ACCOUNT.format(p["XNews"].strip()), "XNews")}' if via_xnews else ""
        return f'<div class="acct"><div>{E(p.get("对象"))}</div><span>{xlink}{extra}</span></div>'

    w('<section aria-labelledby="h-x"><h2 id="h-x">X 上的动态</h2>'
      '<p class="lede">本页不直接读取 X。收进 XNews 的账号可以在它的账号页看最近推文的中文整理；'
      "只在 X 发言的人只能去 X 看。</p><div class=\"cols\">")
    w(f'<div class="panel"><h3>XNews 收录（{len(on_xnews)}）</h3>'
      + "".join(acct_row(p, True) for p in on_xnews) + "</div>")
    w(f'<div class="panel"><h3>只在 X 发言（{len(gaps)}）</h3>'
      + ("".join(acct_row(p, False) for p in gaps) or '<p class="muted">无</p>') + "</div>")
    w("</div></section>")

    # 手动查看
    if manual:
        w('<section aria-labelledby="h-manual"><h2 id="h-manual">手动查看</h2>'
          '<p class="lede">没有可用订阅源的入口。</p><ul class="links">')
        for m in manual:
            note = f' <span>— {E(m.get("说明"))}</span>' if not blank(m.get("说明")) else ""
            w(f'<li>{link(m.get("URL", ""), m.get("名称", ""))}{note}</li>')
        w("</ul></section>")

    # 订阅源状态
    w('<section aria-labelledby="h-status"><h2 id="h-status">订阅源状态</h2>'
      '<div class="tbl"><table><thead><tr><th>订阅源</th><th>组</th><th>状态</th><th>最近一篇</th>'
      f"<th>近 {days} 天</th></tr></thead><tbody>")
    for s in sorted(feeds, key=lambda s: (s["ok"], s["group"])):
        st = '<span class="st-ok">正常</span>' if s["ok"] else f'<span class="st-bad" title="{E(s["error"])}">失败</span>'
        latest = s["latest"].astimezone(TZ).strftime("%Y-%m-%d") if s["latest"] else "—"
        w(f'<tr><td>{link(s["url"], s["name"])}</td><td>{E(s["group"])}</td><td>{st}</td>'
          f'<td>{latest}</td><td>{s["recent"] if s["ok"] else "—"}</td></tr>')
    w("</tbody></table></div></section>")

    # 名单
    w('<section aria-labelledby="h-list"><h2 id="h-list">关注名单</h2>'
      '<details><summary>展开全部 '
      f'{len(people)} 个对象（来源：briefs/watchlist.md）</summary><div class="tbl"><table><thead><tr>'
      "<th>对象</th><th>组</th><th>X 账号</th><th>免费渠道</th><th>状态</th><th>备注</th></tr></thead><tbody>")
    for p in people:
        h = p.get("X 账号", "")
        xh = link(f"https://x.com/{h.lstrip('@')}", h) if h.startswith("@") else E(h)
        w(f'<tr><td>{E(p.get("对象"))}</td><td>{E(p.get("组"))}</td><td>{xh}</td>'
          f'<td>{E(p.get("免费渠道"))}</td><td>{E(p.get("状态"))}</td><td>{E(p.get("备注"))}</td></tr>')
    w("</tbody></table></div></details></section>")

    w("<footer><p>名单：briefs/watchlist.md · 生成：tools/ai_watch.py · 本页数据来自各订阅源，"
      "社区生成的 Anthropic / Claude 订阅源来自 Olshansk/rss-feeds。</p>"
      "<p>条目只是线索：引用或沉淀前，打开原文核对。</p></footer></main>")
    w(f"<script>{JS}</script>")
    page = "\n".join(out)
    if artifact:
        return page
    return ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f"<title>AI 关注动态</title>\n</head>\n<body>\n{page}\n</body>\n</html>\n")


def to_json(sources_status, items, people, days, now) -> dict:
    iso = lambda d: d.astimezone(TZ).isoformat(timespec="minutes") if d else None  # noqa: E731
    return {
        "generated_at": iso(now), "window_days": days,
        "items": [{**{k: i[k] for k in ("title", "url", "excerpt", "source", "group")},
                   "published": iso(i["published"])} for i in items],
        "sources": [{"name": s["name"], "group": s["group"], "type": s["type"], "ok": s["ok"],
                     "latest": iso(s["latest"]), "recent": s["recent"], "error": s["error"],
                     "versions": s["versions"]} for s in sources_status],
        "x_only": [{"name": p.get("对象"), "handle": p.get("X 账号")} for p in people if p.get("状态") == "缺口"],
        "on_xnews": [{"name": p.get("对象"), "handle": p.get("X 账号"), "xnews_id": p.get("XNews")}
                     for p in people if not blank(p.get("XNews"))],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--watchlist", default=str(ROOT / "briefs" / "watchlist.md"))
    ap.add_argument("--out", default=str(ROOT / "output" / "personal" / "ai-watch.html"))
    ap.add_argument("--json", help="另存结构化结果，供每日简报 Routine 使用")
    ap.add_argument("--days", type=int, default=3, help="时间窗（天），默认 3")
    ap.add_argument("--per-feed", type=int, default=6, help="每个源最多显示几条，默认 6")
    ap.add_argument("--artifact", action="store_true", help="输出不带 <html>/<head> 的页面片段（发布 Artifact 用）")
    args = ap.parse_args()

    tables = parse_tables(Path(args.watchlist).read_text(encoding="utf-8"))
    people = tables.get("人物与机构", [])
    sources = tables.get("订阅源", [])
    manual = tables.get("手动查看", [])
    if not people or not sources:
        print("名单解析失败：缺少「人物与机构」或「订阅源」表", file=sys.stderr)
        return 2

    now = dt.datetime.now(dt.timezone.utc)
    statuses, items = collect(sources, args.days, args.per_feed, now)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(render(people, statuses, items, manual, args.days, now, args.artifact), encoding="utf-8")
    if args.json:
        Path(args.json).write_text(json.dumps(to_json(statuses, items, people, args.days, now),
                                              ensure_ascii=False, indent=1), encoding="utf-8")
    failed = [s["name"] for s in statuses if not s["ok"]]
    print(f"写入 {args.out}：{len(items)} 条更新；订阅源失败 {len(failed)} 个{('：' + '、'.join(failed)) if failed else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
