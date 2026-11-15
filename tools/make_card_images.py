#!/usr/bin/env python3
"""Generate category card images and article thumbnails (colour, icon, themed background)."""
import json, math, glob, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
W, H, S = 800, 500, 2  # supersample

THEMES = {
    "flow-measurement-guides":        {"color": "#1971c2", "icon": "flow",  "label": "Flow"},
    "pressure-measurement-guides":    {"color": "#5f3dc4", "icon": "gauge", "label": "Pressure"},
    "level-measurement-guides":       {"color": "#0c8599", "icon": "tank",  "label": "Level"},
    "temperature-measurement-guides": {"color": "#d9480f", "icon": "therm", "label": "Temperature"},
    "gas-detection-guides":           {"color": "#2b8a3e", "icon": "gas",   "label": "Gas Detection"},
    "industrial-valve-guides":        {"color": "#e67700", "icon": "valve", "label": "Valves"},
}

def font(sz):
    for f in glob.glob("/usr/share/fonts/**/DejaVuSans-Bold.ttf", recursive=True) + \
             glob.glob("C:/Windows/Fonts/arialbd.ttf"):
        return ImageFont.truetype(f, sz)
    return ImageFont.load_default()

def hex2rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def mix(c, t, k): return tuple(int(a + (b - a) * k) for a, b in zip(c, t))

def background(d, kind, base):
    w, h = W*S, H*S
    faint = mix(base, (255, 255, 255), 0.18) + (70,)
    lw = 3*S
    if kind == "gauge":
        for r in range(60, 1400, 70):
            d.ellipse((w*0.78-r*S/2, h*0.5-r*S/2, w*0.78+r*S/2, h*0.5+r*S/2), outline=faint, width=lw)
    elif kind == "therm":
        for y in range(0, h+200, 90*S//2):
            pts = [(x, y + 18*S*math.sin(x/(60*S))) for x in range(0, w, 10)]
            d.line(pts, fill=faint, width=lw)
    elif kind == "tank":
        for y in range(h//3, h+100, 50*S//2):
            pts = [(x, y + 10*S*math.sin(x/(40*S) + y)) for x in range(0, w, 10)]
            d.line(pts, fill=faint, width=lw)
    elif kind == "flow":
        for y in range(40*S, h, 70*S//2):
            pts = [(x, y + 25*S*math.sin(x/(120*S))) for x in range(0, w, 10)]
            d.line(pts, fill=faint, width=lw)
    elif kind == "gas":
        import random
        rnd = random.Random(7)
        for _ in range(160):
            x, y, r = rnd.randint(0, w), rnd.randint(0, h), rnd.randint(4, 22)*S
            d.ellipse((x-r, y-r, x+r, y+r), outline=faint, width=2*S)
    elif kind == "valve":
        for x in range(0, w, 120*S):
            d.rectangle((x, 0, x+22*S, h), fill=faint)
        for y in range(60*S, h, 160*S):
            d.rectangle((0, y, w, y+22*S), fill=faint)

def icon(d, kind, cx, cy, r, ink, accent):
    lw = int(r*0.09)
    if kind == "gauge":
        d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=ink, width=lw)
        for i in range(11):
            a = math.radians(135 + i*27)
            d.line((cx+math.cos(a)*r*0.72, cy+math.sin(a)*r*0.72, cx+math.cos(a)*r*0.88, cy+math.sin(a)*r*0.88), fill=ink, width=lw//2)
        a = math.radians(300)
        d.line((cx, cy, cx+math.cos(a)*r*0.7, cy+math.sin(a)*r*0.7), fill=accent, width=lw)
        d.ellipse((cx-r*0.1, cy-r*0.1, cx+r*0.1, cy+r*0.1), fill=ink)
        d.rectangle((cx-r*0.15, cy+r, cx+r*0.15, cy+r*1.3), fill=ink)
    elif kind == "therm":
        bw = r*0.32
        d.rounded_rectangle((cx-bw/2, cy-r*1.1, cx+bw/2, cy+r*0.5), radius=bw/2, outline=ink, width=lw)
        d.ellipse((cx-r*0.38, cy+r*0.3, cx+r*0.38, cy+r*1.06), fill=accent, outline=ink, width=lw)
        d.rectangle((cx-bw*0.18, cy-r*0.4, cx+bw*0.18, cy+r*0.5), fill=accent)
        for i in range(5):
            y = cy - r*0.9 + i*r*0.28
            d.line((cx+bw/2+r*0.08, y, cx+bw/2+r*0.3, y), fill=ink, width=lw//2)
    elif kind == "tank":
        x0, x1, y0, y1 = cx-r*0.8, cx+r*0.8, cy-r*1.0, cy+r*1.0
        lvl = cy - r*0.1
        d.rectangle((x0, lvl, x1, y1), fill=accent)
        pts = [(x, lvl + r*0.06*math.sin((x-x0)/(r*0.18))) for x in range(int(x0), int(x1), 4)]
        d.line(pts, fill=ink, width=lw//2)
        d.rounded_rectangle((x0, y0, x1, y1), radius=r*0.12, outline=ink, width=lw)
        d.polygon([(x1+r*0.15, lvl), (x1+r*0.4, lvl-r*0.15), (x1+r*0.4, lvl+r*0.15)], fill=ink)
    elif kind == "flow":
        d.rounded_rectangle((cx-r*1.3, cy-r*0.35, cx+r*1.3, cy+r*0.35), radius=r*0.1, outline=ink, width=lw)
        for dx in (-0.8, 0, 0.8):
            x = cx + dx*r
            d.line((x-r*0.3, cy, x+r*0.2, cy), fill=accent, width=lw)
            d.polygon([(x+r*0.35, cy), (x+r*0.12, cy-r*0.16), (x+r*0.12, cy+r*0.16)], fill=accent)
        d.rectangle((cx-r*1.5, cy-r*0.5, cx-r*1.3, cy+r*0.5), fill=ink)
        d.rectangle((cx+r*1.3, cy-r*0.5, cx+r*1.5, cy+r*0.5), fill=ink)
    elif kind == "gas":
        d.rounded_rectangle((cx-r*0.55, cy-r*0.6, cx+r*0.55, cy+r*1.1), radius=r*0.15, outline=ink, width=lw)
        d.ellipse((cx-r*0.28, cy-r*0.35, cx+r*0.28, cy+r*0.21), outline=ink, width=lw//2)
        d.rectangle((cx-r*0.3, cy+r*0.45, cx+r*0.3, cy+r*0.8), fill=accent)
        t = [(cx+r*0.6, cy-r*1.2), (cx+r*1.25, cy-r*0.1), (cx-r*0.05, cy-r*0.1)]
        d.polygon(t, fill=accent, outline=ink)
        d.line((cx+r*0.6, cy-r*0.9, cx+r*0.6, cy-r*0.45), fill=ink, width=lw//2)
        d.ellipse((cx+r*0.56, cy-r*0.33, cx+r*0.64, cy-r*0.25), fill=ink)
    elif kind == "valve":
        d.polygon([(cx-r*1.0, cy-r*0.5), (cx, cy), (cx-r*1.0, cy+r*0.5)], outline=ink, width=lw)
        d.polygon([(cx+r*1.0, cy-r*0.5), (cx, cy), (cx+r*1.0, cy+r*0.5)], outline=ink, width=lw)
        d.line((cx, cy, cx, cy-r*0.9), fill=ink, width=lw)
        d.ellipse((cx-r*0.55, cy-r*1.15, cx+r*0.55, cy-r*0.85), outline=ink, width=lw)
        d.rectangle((cx-r*1.3, cy-r*0.55, cx-r*1.05, cy+r*0.55), fill=ink)
        d.rectangle((cx+r*1.05, cy-r*0.55, cx+r*1.3, cy+r*0.55), fill=ink)

def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=fnt) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur)
    return lines

def make(theme, title, out):
    base = hex2rgb(theme["color"])
    img = Image.new("RGB", (W*S, H*S), base)
    grad = Image.new("RGB", (W*S, H*S), mix(base, (0, 0, 0), 0.35))
    mask = Image.linear_gradient("L").rotate(-60, expand=False).resize((W*S, H*S))
    img = Image.composite(grad, img, mask)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    background(ImageDraw.Draw(ov), theme["icon"], base)
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    cx, cy, r = int(W*S*0.76), int(H*S*0.5), int(H*S*0.25)
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse((cx-r*1.6, cy-r*1.6, cx+r*1.6, cy+r*1.6), fill=(255, 255, 255, 34))
    img = Image.alpha_composite(img, halo)
    d = ImageDraw.Draw(img)
    icon(d, theme["icon"], cx, cy, r, (255, 255, 255), (255, 196, 64))
    maxw = W*S*0.46
    size = 58
    while True:
        fnt = font(size*S)
        lines = wrap(d, title, fnt, maxw)
        if (len(lines) <= 3 and all(d.textlength(l, font=fnt) <= maxw for l in lines)) or size <= 28:
            break
        size -= 2
    lh = fnt.size*1.18
    y = H*S/2 - lh*len(lines)/2
    for ln in lines:
        d.text((56*S, y), ln, font=fnt, fill="white"); y += lh
    d.rectangle((56*S, y + 18*S, 156*S, y + 26*S), fill=(255, 196, 64))
    img.convert("RGB").resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=85)

def main():
    cfg = json.loads((ROOT / "config/categories.json").read_text(encoding="utf-8"))
    only_missing = "--missing" in sys.argv
    for c in cfg["categories"]:
        th = THEMES.get(c["slug"])
        if not th:
            print(f"no theme for {c['slug']}, skipped"); continue
        out = ROOT / c["thumbnail"]
        if not (only_missing and out.exists()):
            make(th, th["label"], out); print("category", out.name)
        for meta in sorted((ROOT / "articles" / c["slug"]).glob("*/meta.json")):
            m = json.loads(meta.read_text(encoding="utf-8"))
            t = meta.parent / m.get("thumbnail", "thumbnail.webp")
            if only_missing and t.exists(): continue
            short = m.get("card_title") or m["title"].split("?")[0].split(":")[0]
            make(th, short, t); print("article ", t.parent.name)

if __name__ == "__main__":
    main()
