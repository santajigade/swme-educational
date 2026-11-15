#!/usr/bin/env python3
"""Helpers that render the approved article components to HTML.

Article source files live in tools/content/<slug>.py and define META and BODY
(a list of component calls). Run: python tools/build_article.py <slug> [...]
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

THEME = {
    "flow-measurement-guides":        {"c": "#1971c2", "bg": "#eef5fd", "th": "#dbeafa", "tx": "#14508a"},
    "pressure-measurement-guides":    {"c": "#5f3dc4", "bg": "#f3f0ff", "th": "#ece8fb", "tx": "#3b2a8c"},
    "level-measurement-guides":       {"c": "#0c8599", "bg": "#e8f7f9", "th": "#d3f0f4", "tx": "#0a5f6d"},
    "temperature-measurement-guides": {"c": "#d9480f", "bg": "#fff1ea", "th": "#ffe3d5", "tx": "#a33608"},
    "gas-detection-guides":           {"c": "#2b8a3e", "bg": "#ecf8ee", "th": "#d8f1dd", "tx": "#1f6a2f"},
    "industrial-valve-guides":        {"c": "#e67700", "bg": "#fff4e6", "th": "#ffe8cc", "tx": "#a35400"},
}
T = THEME["pressure-measurement-guides"]


def ext(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


def link(url, text):
    return f'<a href="{url}">{text}</a>'


def p(*paras):
    return "\n".join(f"<p>{x}</p>" for x in paras)


def h2(id_, text):
    return f'<h2 id="{id_}">{text}</h2>'


def h3(text):
    return f'<h3 class="h5 fw-bold mt-4">{text}</h3>'


def takeaways(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return (f'<div class="p-4 rounded-3 mb-4" style="background:{T["bg"]};border-left:4px solid {T["c"]};">'
            f'<p class="fw-semibold mb-2" style="color:{T["c"]};">Key takeaways</p><ul class="mb-0">{lis}</ul></div>')


def toc(items):
    lis = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return f'<div class="border rounded-3 p-4 mb-4"><p class="fw-semibold mb-2">In this guide</p><ol class="mb-0">{lis}</ol></div>'


def rows(items, title=None):
    head = f'<p class="fw-semibold mb-2">{title}</p>' if title else ""
    body = "".join(f'<div class="p-3 mb-2 rounded-3" style="background:{T["bg"]};border-left:4px solid {T["c"]};">'
                   f'<strong style="color:{T["c"]};">{k}:</strong> {v}</div>' for k, v in items)
    return f'{head}<div class="my-3">{body}</div>'


def mistakes(items):
    body = "".join('<div class="p-3 mb-2 rounded-3" style="background:#fff4e6;border-left:4px solid #f08c00;">'
                   f'<strong style="color:#d9480f;">{k}</strong> {v}</div>' for k, v in items)
    return f'<div class="my-3">{body}</div>'


def table(headers, data):
    th = "".join(f'<th style="background:{T["th"]};color:{T["tx"]};">{h}</th>' for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in data)
    return ('<div class="table-responsive my-4"><table class="table table-bordered table-striped align-middle mb-0" '
            f'style="--bs-table-striped-bg:{T["bg"]};border-color:{T["th"]};"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')


def dyk(text):
    return ('<div class="d-flex gap-3 p-4 rounded-3 my-4" style="background:#fff9db;border:1px solid #ffe066;">'
            '<i class="bi bi-lightbulb-fill fs-3" style="color:#f59f00;"></i>'
            f'<div><p class="fw-bold mb-1">Did you know?</p><p class="mb-0">{text}</p></div></div>')


PALETTE = [("#e7f5ff", "#d0ebff", "#1864ab"), ("#ebfbee", "#d3f9d8", "#2b8a3e"),
           ("#fff4e6", "#ffe8cc", "#d9480f"), ("#f3f0ff", "#e5dbff", "#5f3dc4")]


def twocol(cols):
    out = []
    for n, (title, icon, items) in enumerate(cols):
        bg, bd, fg = PALETTE[n % len(PALETTE)]
        lis = "".join(f"<li>{i}</li>" for i in items)
        out.append(f'<div class="col-md-6"><div class="p-4 rounded-3 h-100" style="background:{bg};border:1px solid {bd};">'
                   f'<h3 class="h5 fw-bold" style="color:{fg};"><i class="bi {icon} me-2"></i>{title}</h3>'
                   f'<ul class="mb-0">{lis}</ul></div></div>')
    return '<div class="row g-3 my-4">' + "".join(out) + "</div>"


def checklist(items):
    lis = "".join(f'<li class="mb-2"><strong>{k}.</strong> {v}</li>' for k, v in items)
    return f'<ol class="my-4">{lis}</ol>'


def faq(items):
    out = []
    for n, (q, a) in enumerate(items):
        last = n == len(items) - 1
        out.append(f'<details{" open" if n == 0 else ""} class="py-2{"" if last else " border-bottom"}">'
                   f'<summary class="fw-semibold">{q}</summary><p class="mt-2 mb-1">{a}</p></details>')
    return f'<div class="border rounded-3 px-4 py-2 my-4" style="background:{T["bg"]};">' + "".join(out) + "</div>"


INFOGRAPHIC = "{{infographic}}"


def build(slug):
    global T
    src = ROOT / "tools" / "content" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), src)
    mod = importlib.util.module_from_spec(spec)
    T = THEME[mod_category(src)]
    mod.__dict__.update({k: v for k, v in globals().items() if not k.startswith("_")})
    spec.loader.exec_module(mod)
    meta = mod.META
    folder = ROOT / "articles" / meta["category"] / slug
    folder.mkdir(parents=True, exist_ok=True)
    html = "\n\n".join(mod.BODY) + "\n"
    (folder / "article.html").write_text(html, encoding="utf-8")
    out = {k: v for k, v in meta.items() if k != "category"}
    out["slug"] = slug
    (folder / "meta.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("built", meta["category"], slug)


def mod_category(src):
    for line in src.read_text(encoding="utf-8").splitlines():
        if '"category"' in line:
            return line.split(":", 1)[1].strip().strip(",").strip().strip('"')
    raise SystemExit(f"{src}: META needs a category line")




# ---------------------------------------------------------------- SVG diagrams
def svg(inner, caption, h=360, alt=None):
    """Wrap inline SVG in a responsive figure with caption (scales with column width)."""
    import html as _h
    label = _h.escape(alt or caption)
    caption = _h.escape(caption)
    return (f'<figure class="my-5 text-center"><div class="p-3 rounded-3 border" style="background:#fff;">'
            f'<svg viewBox="0 0 800 {h}" width="100%" role="img" aria-label="{label}" '
            f'style="max-width:800px;height:auto;font-family:Inter,Arial,sans-serif;" xmlns="http://www.w3.org/2000/svg">'
            f'<title>{label}</title>{inner}</svg></div>'
            f'<figcaption class="small text-muted mt-2">{caption}</figcaption></figure>')


def arrow_defs(c):
    return (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker></defs>')


def svg_chain(items, caption, sub=None):
    """Horizontal block diagram: boxes joined by arrows."""
    c, bg = T["c"], T["bg"]
    n = len(items); gap = 34; bw = (760 - (n - 1) * gap) / n; out = [arrow_defs(c)]
    for i, label in enumerate(items):
        x = 20 + i * (bw + gap)
        out.append(f'<rect x="{x:.0f}" y="40" width="{bw:.0f}" height="90" rx="12" fill="{bg}" stroke="{c}" stroke-width="2"/>')
        lines = label.split("|")
        for k, ln in enumerate(lines):
            y = 85 + (k - (len(lines) - 1) / 2) * 20
            out.append(f'<text x="{x + bw/2:.0f}" y="{y:.0f}" text-anchor="middle" font-size="15" font-weight="600" fill="{T["tx"]}">{ln}</text>')
        if sub and i < len(sub) and sub[i]:
            out.append(f'<text x="{x + bw/2:.0f}" y="160" text-anchor="middle" font-size="12" fill="#666">{sub[i]}</text>')
        if i < n - 1:
            out.append(f'<line x1="{x + bw + 3:.0f}" y1="85" x2="{x + bw + gap - 3:.0f}" y2="85" stroke="{c}" stroke-width="2.5" marker-end="url(#ah)"/>')
    return svg("".join(out), caption, 190)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        build(s)
