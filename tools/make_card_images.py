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

def icon(d, kind, cx, cy, r, ink, accent, needle=300):
    lw = int(r*0.09)
    if kind == "gauge":
        d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=ink, width=lw)
        for i in range(11):
            a = math.radians(135 + i*27)
            d.line((cx+math.cos(a)*r*0.72, cy+math.sin(a)*r*0.72, cx+math.cos(a)*r*0.88, cy+math.sin(a)*r*0.88), fill=ink, width=lw//2)
        a = math.radians(needle)
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

def make(theme, title, out, text_only=False):
    base = hex2rgb(theme["color"])
    img = Image.new("RGB", (W*S, H*S), base)
    grad = Image.new("RGB", (W*S, H*S), mix(base, (0, 0, 0), 0.35))
    mask = Image.linear_gradient("L").rotate(-60, expand=False).resize((W*S, H*S))
    img = Image.composite(grad, img, mask)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    background(ImageDraw.Draw(ov), theme["icon"], base)
    img = Image.alpha_composite(img.convert("RGBA"), ov)
    if text_only:
        d = ImageDraw.Draw(img)
        maxw, size = W*S*0.84, 64
        while True:
            fnt = font(size*S)
            lines = wrap(d, title, fnt, maxw)
            if (len(lines) <= 3 and all(d.textlength(l, font=fnt) <= maxw for l in lines)) or size <= 30:
                break
            size -= 2
        lh = fnt.size*1.2
        y = H*S/2 - lh*len(lines)/2 - 10*S
        for ln in lines:
            d.text(((W*S - d.textlength(ln, font=fnt))/2, y), ln, font=fnt, fill="white"); y += lh
        d.rectangle((W*S/2 - 50*S, y + 22*S, W*S/2 + 50*S, y + 30*S), fill=(255, 196, 64))
        img.convert("RGB").resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=85)
        return
    if title:
        cx, cy, r = int(W*S*0.5), int(H*S*0.37), int(H*S*0.15)
    else:
        cx, cy, r = int(W*S*0.5), int(H*S*0.5), int(H*S*0.3)
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse((cx-r*1.75, cy-r*1.75, cx+r*1.75, cy+r*1.75), fill=(255, 255, 255, 34))
    img = Image.alpha_composite(img, halo)
    d = ImageDraw.Draw(img)
    icon(d, theme["icon"], cx, cy, r, (255, 255, 255), (255, 196, 64))
    if not title:
        img.convert("RGB").resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=85)
        return
    maxw = W*S*0.6
    size = 50
    while True:
        fnt = font(size*S)
        lines = wrap(d, title, fnt, maxw)
        if (len(lines) <= 1 and d.textlength(lines[0], font=fnt) <= maxw) or size <= 30:
            break
        size -= 2
    lh = fnt.size*1.18
    y = H*S*0.66
    for ln in lines:
        d.text(((W*S - d.textlength(ln, font=fnt))/2, y), ln, font=fnt, fill="white"); y += lh
    d.rectangle((W*S/2 - 40*S, y + 12*S, W*S/2 + 40*S, y + 19*S), fill=(255, 196, 64))
    img.convert("RGB").resize((W, H), Image.LANCZOS).save(out, "WEBP", quality=85)

def render_infographic(theme, spec, shown=None, active=None, needle=300):
    """Vertical step infographic: title band, numbered steps with arrows, footer."""
    base = hex2rgb(theme["color"])
    light = mix(base, (255, 255, 255), 0.9)
    Wd = 1200 * S
    steps = spec["steps"]
    tf, lf, bf, sf = font(54*S), font(36*S), font(28*S) if False else None, font(24*S)
    try:
        bf = ImageFont.truetype(glob.glob("/usr/share/fonts/**/DejaVuSans.ttf", recursive=True)[0], 28*S)
    except Exception:
        bf = font(28*S)
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    rows = []
    for label, text in steps:
        lines = wrap(tmp, text, bf, Wd - 420*S)
        rows.append((label, lines, max(150*S, int(70*S + len(lines) * 40*S))))
    head_h, gap, foot_h = 260*S, 50*S, 110*S
    Ht = head_h + 60*S + sum(r[2] for r in rows) + gap*(len(rows)-1) + 60*S + foot_h
    img = Image.new("RGB", (Wd, Ht), "white")
    d = ImageDraw.Draw(img)
    # header
    d.rectangle((0, 0, Wd, head_h), fill=base)
    ov = Image.new("RGBA", (Wd, head_h), (0, 0, 0, 0))
    background(ImageDraw.Draw(ov), theme["icon"], base)
    img.paste(Image.alpha_composite(Image.new("RGBA", (Wd, head_h), base + (255,)), ov).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)
    icon(d, theme["icon"], Wd - 170*S, head_h//2, 75*S, (255, 255, 255), (255, 196, 64), needle)
    tl = wrap(d, spec["title"], tf, Wd - 420*S)
    y = head_h/2 - len(tl)*66*S/2
    for ln in tl:
        d.text((70*S, y), ln, font=tf, fill="white"); y += 66*S
    # steps
    y = head_h + 60*S
    n_shown = len(rows) if shown is None else shown
    for i, (label, lines, h) in enumerate(rows):
        if i >= n_shown:
            d.rounded_rectangle((60*S, y, Wd - 60*S, y + h), radius=24*S, outline=mix(base, (255, 255, 255), 0.85), width=3*S)
            y += h + gap
            continue
        fill = mix(base, (255, 255, 255), 0.78) if i == active else light
        d.rounded_rectangle((60*S, y, Wd - 60*S, y + h), radius=24*S, fill=fill)
        if i == active:
            d.rounded_rectangle((60*S, y, 72*S, y + h), radius=6*S, fill=(255, 196, 64))
        cx, cy, r = 150*S, y + h//2, 52*S
        d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=base)
        num = str(i + 1)
        d.text((cx - d.textlength(num, font=lf)/2, cy - 24*S), num, font=lf, fill="white")
        ty = y + (h - (46*S + len(lines)*40*S)) / 2
        d.text((250*S, ty), label, font=lf, fill=mix(base, (0, 0, 0), 0.35))
        ty += 52*S
        for ln in lines:
            d.text((250*S, ty), ln, font=bf, fill=(60, 60, 70)); ty += 40*S
        if i < n_shown - 1:
            ay = y + h + 8*S
            d.polygon([(cx - 22*S, ay), (cx + 22*S, ay), (cx, ay + gap - 16*S)], fill=base)
        y += h + gap
    # footer
    d.rectangle((0, Ht - foot_h, Wd, Ht), fill=mix(base, (0, 0, 0), 0.3))
    ft = spec.get("footer", "swme.ae  |  Educational Guides")
    d.text((70*S, Ht - foot_h/2 - 14*S), ft, font=sf, fill="white")
    return img.resize((Wd//S * 2 // 3, Ht//S * 2 // 3), Image.LANCZOS)


# ---------------------------------------------------------------- extra layouts
def _regular(sz):
    try:
        return ImageFont.truetype(glob.glob("/usr/share/fonts/**/DejaVuSans.ttf", recursive=True)[0], sz)
    except Exception:
        return font(sz)


def _canvas(theme, title, body_h, needle=300):
    """Header band + white body + footer. Returns (img, draw, top_y, Wd, base, light)."""
    base = hex2rgb(theme["color"]); light = mix(base, (255, 255, 255), 0.9)
    Wd, head_h, foot_h = 1200 * S, 230 * S, 100 * S
    Ht = head_h + body_h + foot_h
    img = Image.new("RGB", (Wd, Ht), "white")
    band = Image.new("RGBA", (Wd, head_h), base + (255,))
    ov = Image.new("RGBA", (Wd, head_h), (0, 0, 0, 0)); background(ImageDraw.Draw(ov), theme["icon"], base)
    img.paste(Image.alpha_composite(band, ov).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)
    icon(d, theme["icon"], Wd - 160*S, head_h // 2, 70*S, (255, 255, 255), (255, 196, 64), needle)
    tf = font(52*S); tl = wrap(d, title, tf, Wd - 400*S); y = head_h/2 - len(tl)*62*S/2
    for ln in tl:
        d.text((70*S, y), ln, font=tf, fill="white"); y += 62*S
    d.rectangle((0, Ht - foot_h, Wd, Ht), fill=mix(base, (0, 0, 0), 0.3))
    d.text((70*S, Ht - foot_h/2 - 14*S), "swme.ae  |  Educational Guides", font=font(24*S), fill="white")
    return img, d, head_h, Wd, base, light


def _text_block(d, x, y, w, label, text, base, lf=34, bf=26, color=(60, 60, 70), center=False):
    lfnt, bfnt = font(lf*S), _regular(bf*S)
    for ln in wrap(d, label, lfnt, w):
        tx = x + (w - d.textlength(ln, font=lfnt))/2 if center else x
        d.text((tx, y), ln, font=lfnt, fill=mix(base, (0, 0, 0), 0.35)); y += lf*1.3*S
    y += 6*S
    for ln in wrap(d, text, bfnt, w):
        tx = x + (w - d.textlength(ln, font=bfnt))/2 if center else x
        d.text((tx, y), ln, font=bfnt, fill=color); y += bf*1.45*S
    return y


def render_grid(theme, spec, shown=None, active=None, needle=300):
    items = spec["steps"]; n = len(items); cols = 2; rows_ = (n + 1) // 2
    cw, ch, gap = 520*S, 300*S, 40*S
    img, d, top, Wd, base, light = _canvas(theme, spec["title"], 60*S + rows_*(ch + gap) + 20*S, needle)
    shown = n if shown is None else shown
    for i, (label, text) in enumerate(items):
        r, c = divmod(i, cols); x = 60*S + c*(cw + gap); y = top + 60*S + r*(ch + gap)
        if i >= shown:
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=28*S, outline=mix(base, (255, 255, 255), 0.85), width=3*S); continue
        d.rounded_rectangle((x, y, x + cw, y + ch), radius=28*S, fill=mix(base, (255, 255, 255), 0.78) if i == active else light)
        d.rounded_rectangle((x, y, x + cw, y + 14*S), radius=7*S, fill=base)
        d.ellipse((x + 30*S, y + 40*S, x + 100*S, y + 110*S), fill=base)
        num = str(i + 1); nf = font(36*S)
        d.text((x + 65*S - d.textlength(num, font=nf)/2, y + 54*S), num, font=nf, fill="white")
        _text_block(d, x + 30*S, y + 130*S, cw - 60*S, label, text, base, lf=30, bf=24)
    return img.resize((Wd//S * 2 // 3, img.height//S * 2 // 3), Image.LANCZOS)


def render_flow(theme, spec, shown=None, active=None, needle=300):
    items = spec["steps"]; n = len(items)
    bw, gap = (1080*S - (n - 1)*60*S) // n, 60*S
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    th_ = max(len(wrap(tmp, l, font(26*S), bw - 36*S))*34*S + 8*S + len(wrap(tmp, t, _regular(21*S), bw - 36*S))*31*S for l, t in items)
    box_h = 140*S + th_ + 30*S
    img, d, top, Wd, base, light = _canvas(theme, spec["title"], box_h + 120*S, needle)
    shown = n if shown is None else shown
    for i, (label, text) in enumerate(items):
        x = 60*S + i*(bw + gap); y = top + 60*S
        if i >= shown:
            d.rounded_rectangle((x, y, x + bw, y + box_h), radius=24*S, outline=mix(base, (255, 255, 255), 0.85), width=3*S); continue
        d.rounded_rectangle((x, y, x + bw, y + box_h), radius=24*S, fill=mix(base, (255, 255, 255), 0.78) if i == active else light)
        d.rounded_rectangle((x, y, x + bw, y + 90*S), radius=24*S, fill=base)
        d.rectangle((x, y + 60*S, x + bw, y + 90*S), fill=base)
        nf = font(40*S); num = str(i + 1)
        d.text((x + bw/2 - d.textlength(num, font=nf)/2, y + 22*S), num, font=nf, fill="white")
        _text_block(d, x + 18*S, y + 115*S, bw - 36*S, label, text, base, lf=26, bf=21, center=True)
        if i < shown - 1 and i < n - 1:
            ax = x + bw + 8*S; ay = y + box_h/2
            d.polygon([(ax, ay - 20*S), (ax + gap - 16*S, ay), (ax, ay + 20*S)], fill=base)
    return img.resize((Wd//S * 2 // 3, img.height//S * 2 // 3), Image.LANCZOS)


def render_compare(theme, spec, shown=None, active=None, needle=300):
    colsd = spec["columns"]; n = len(colsd); gap = 40*S
    cw = (1080*S - (n - 1)*gap) // n
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10))); bf = _regular(24*S)
    hmax = max(sum(len(wrap(tmp, ln, bf, cw - 70*S)) * 36*S + 18*S for ln in lines) for _, lines in colsd)
    body = 60*S + 110*S + hmax + 60*S
    img, d, top, Wd, base, light = _canvas(theme, spec["title"], body, needle)
    shown = n if shown is None else shown
    tints = [base, mix(base, (0, 0, 0), 0.35), mix(base, (255, 255, 255), 0.3)]
    for i, (title, lines) in enumerate(colsd):
        x = 60*S + i*(cw + gap); y = top + 60*S; h = 110*S + hmax + 30*S
        if i >= shown:
            d.rounded_rectangle((x, y, x + cw, y + h), radius=24*S, outline=mix(base, (255, 255, 255), 0.85), width=3*S); continue
        d.rounded_rectangle((x, y, x + cw, y + h), radius=24*S, fill=light)
        col = tints[i % len(tints)]
        d.rounded_rectangle((x, y, x + cw, y + 100*S), radius=24*S, fill=col); d.rectangle((x, y + 70*S, x + cw, y + 100*S), fill=col)
        tf = font(30*S); tl = wrap(d, title, tf, cw - 40*S)[:2]; ty = y + 50*S - len(tl)*19*S
        for ln in tl:
            d.text((x + cw/2 - d.textlength(ln, font=tf)/2, ty), ln, font=tf, fill="white"); ty += 38*S
        ly = y + 130*S
        for line in lines:
            d.ellipse((x + 28*S, ly + 10*S, x + 44*S, ly + 26*S), fill=col)
            for wl in wrap(d, line, bf, cw - 70*S):
                d.text((x + 56*S, ly), wl, font=bf, fill=(60, 60, 70)); ly += 36*S
            ly += 18*S
    return img.resize((Wd//S * 2 // 3, img.height//S * 2 // 3), Image.LANCZOS)


def render_levels(theme, spec, shown=None, active=None, needle=300):
    items = spec["levels"]; n = len(items); H_ = 700*S
    img, d, top, Wd, base, light = _canvas(theme, spec["title"], H_ + 120*S, needle)
    shown = n if shown is None else shown
    x0, y0, y1 = 220*S, top + 60*S, top + 60*S + H_
    d.rounded_rectangle((x0 - 40*S, y0, x0 + 40*S, y1), radius=40*S, fill=light, outline=mix(base, (255, 255, 255), 0.6), width=3*S)
    lf = _regular(22*S)
    d.text((x0 - 60*S - d.textlength(spec.get("top_label", "High"), font=lf), y0), spec.get("top_label", "High"), font=lf, fill=(110, 110, 120))
    d.text((x0 - 60*S - d.textlength(spec.get("bottom_label", "Low"), font=lf), y1 - 30*S), spec.get("bottom_label", "Low"), font=lf, fill=(110, 110, 120))
    for i, (label, text, pos) in enumerate(items):
        if i >= shown: continue
        y = y1 - pos * H_
        c = mix(base, (255, 196, 64), 0.6) if i == active else base
        d.ellipse((x0 - 26*S, y - 26*S, x0 + 26*S, y + 26*S), fill=c)
        d.line((x0 + 30*S, y, x0 + 130*S, y), fill=c, width=5*S)
        bx = x0 + 140*S; bw = Wd - bx - 60*S
        bfnt = _regular(24*S); tl = wrap(d, text, bfnt, bw - 40*S)
        bh = 60*S + len(tl)*34*S
        by = max(y0, min(y - bh/2, y1 - bh))
        d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=20*S, fill=mix(base, (255, 255, 255), 0.78) if i == active else light)
        _text_block(d, bx + 20*S, by + 12*S, bw - 40*S, label, text, base, lf=28, bf=24)
    return img.resize((Wd//S * 2 // 3, img.height//S * 2 // 3), Image.LANCZOS)


RENDERERS = {"steps": None, "grid": render_grid, "flow": render_flow, "compare": render_compare, "levels": render_levels}


def make_infographic(theme, spec, out):
    """Animated GIF: steps appear one by one, then the full graphic holds."""
    layout = spec.get("layout", "steps")
    render = RENDERERS.get(layout) or render_infographic
    n = len(spec.get("steps") or spec.get("columns") or spec.get("levels"))
    frames, durations = [], []
    frames.append(render(theme, spec, shown=0, needle=150)); durations.append(700)
    for k in range(1, n + 1):
        frames.append(render(theme, spec, shown=k, active=k - 1, needle=150 + 150 * k / n))
        durations.append(1300 if layout == "compare" else 1100)
    frames.append(render(theme, spec, shown=n, needle=300)); durations.append(3500)
    pal = [f.convert("P", palette=Image.ADAPTIVE, colors=128) for f in frames]
    pal[0].save(out, save_all=True, append_images=pal[1:], duration=durations, loop=0, optimize=True, disposal=2)


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
            if only_missing and t.exists() and (not m.get("infographic") or (meta.parent / "infographic.gif").exists()):
                continue
            short = m.get("card_title") or m["title"].split("?")[0].split(":")[0]
            make(th, short, t, text_only=True); print("article ", t.parent.name)
            if m.get("infographic"):
                make_infographic(th, m["infographic"], meta.parent / "infographic.gif")
                print("infographic", t.parent.name)

if __name__ == "__main__":
    main()
