#!/usr/bin/env python3
"""
SWME Educational auto publisher.

Logs in to the swme.ae admin panel and creates or updates pages:
  Educational (parent page, must already exist)
    -> category pages from config/categories.json
       -> article pages from articles/<category-slug>/<article-slug>/

Usage:
  python scripts/publish.py --validate          # check files only, no login
  python scripts/publish.py                     # sync everything
  python scripts/publish.py --changed a.txt     # only folders listed in a.txt
  python scripts/publish.py --dry-run           # login and plan, but do not save

Environment:
  SWME_BASE_URL   default https://swme.ae
  SWME_EMAIL      admin user email   (GitHub Secret)
  SWME_PASSWORD   admin user password (GitHub Secret)
"""
import argparse
import hashlib
import html as htmllib
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "categories.json"
ARTICLES = ROOT / "articles"

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_TAGS = re.compile(r"<\s*(script|style|iframe\s+[^>]*srcdoc)\b", re.I)
DASHES = re.compile("[–—]")
TEMPLATES = {"default", "category"}
STATUSES = {"published", "draft"}
IMG_TYPES = {".gif": "image/gif", ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}


class PublishError(Exception):
    pass


# ----------------------------------------------------------------- loading

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise PublishError(f"{path}: invalid JSON ({e})")


def check_text(label, value, errors, max_len=None, required=True):
    if not value:
        if required:
            errors.append(f"{label}: missing")
        return
    if DASHES.search(value):
        errors.append(f"{label}: contains an em or en dash")
    if max_len and len(value) > max_len:
        errors.append(f"{label}: {len(value)} chars, max {max_len}")


def load_plan():
    """Read config and article folders. Returns (parent_slug, parent, categories, articles, errors)."""
    errors = []
    cfg = load_json(CONFIG)
    parent_slug = cfg.get("parent_slug", "educational")
    parent = cfg.get("parent")
    if parent:
        parent["slug"] = parent_slug
        check_text("parent title", parent.get("title"), errors)
        check_text("parent meta_title", parent.get("meta_title"), errors, 60)
        check_text("parent meta_description", parent.get("meta_description"), errors, 160)
        check_text("parent summary", parent.get("summary"), errors, 200, required=False)
        check_text("parent intro", parent.get("intro"), errors, required=False)
        if parent.get("status", "draft") not in STATUSES:
            errors.append("parent: status must be published or draft")
        parent["_kind"] = "parent"
    categories = []
    cat_slugs = set()
    for c in cfg.get("categories", []):
        tag = f"category {c.get('slug', '?')}"
        if not SLUG_RE.match(c.get("slug", "")):
            errors.append(f"{tag}: bad slug")
        cat_slugs.add(c.get("slug"))
        check_text(f"{tag} title", c.get("title"), errors)
        check_text(f"{tag} meta_title", c.get("meta_title"), errors, 60)
        check_text(f"{tag} meta_description", c.get("meta_description"), errors, 160)
        check_text(f"{tag} summary", c.get("summary"), errors, 200)
        check_text(f"{tag} subtitle", c.get("subtitle"), errors, required=False)
        check_text(f"{tag} intro", c.get("intro"), errors, required=False)
        if c.get("status", "draft") not in STATUSES:
            errors.append(f"{tag}: status must be published or draft")
        thumb = c.get("thumbnail")
        c["_thumb_path"] = (ROOT / thumb) if thumb and (ROOT / thumb).is_file() else None
        c["_kind"] = "category"
        c["_dir"] = None
        categories.append(c)

    articles = []
    seen = set()
    if ARTICLES.is_dir():
        for meta_path in sorted(ARTICLES.glob("*/*/meta.json")):
            folder = meta_path.parent
            cat_slug = folder.parent.name
            tag = f"article {cat_slug}/{folder.name}"
            try:
                m = load_json(meta_path)
            except PublishError as e:
                errors.append(str(e))
                continue
            m.setdefault("slug", folder.name)
            if m["slug"] != folder.name:
                errors.append(f"{tag}: slug in meta.json must equal folder name")
            if not SLUG_RE.match(m["slug"]):
                errors.append(f"{tag}: bad slug")
            if m["slug"] in seen or m["slug"] in cat_slugs:
                errors.append(f"{tag}: duplicate slug")
            seen.add(m["slug"])
            if cat_slug not in cat_slugs:
                errors.append(f"{tag}: category folder not in config/categories.json")
            check_text(f"{tag} title", m.get("title"), errors)
            check_text(f"{tag} meta_title", m.get("meta_title"), errors, 60)
            check_text(f"{tag} meta_description", m.get("meta_description"), errors, 160)
            check_text(f"{tag} summary", m.get("summary"), errors, 200)
            check_text(f"{tag} subtitle", m.get("subtitle"), errors, required=False)
            if m.get("status", "draft") not in STATUSES:
                errors.append(f"{tag}: status must be published or draft")
            html_path = folder / "article.html"
            if not html_path.is_file():
                errors.append(f"{tag}: article.html missing")
                continue
            html = html_path.read_text(encoding="utf-8").strip()
            if FORBIDDEN_TAGS.search(html):
                errors.append(f"{tag}: <script>/<style> tags are stripped by the editor, remove them")
            if re.search(r"<\s*h1\b", html, re.I):
                errors.append(f"{tag}: do not use <h1>, the page title is the H1")
            if DASHES.search(html):
                errors.append(f"{tag}: article.html contains an em or en dash")
            text = htmllib.unescape(re.sub(r"<[^>]+>", " ", html))
            words = len(text.split())
            if words < 150:
                errors.append(f"{tag}: article is under 150 words")
            hy = sorted(set(re.findall(r"\b\w+-\w+\b", text)))
            if hy:
                errors.append(f"{tag}: hyphenated words in visible text: {', '.join(hy[:8])}")
            links = len(re.findall(r"<a\s[^>]*href=", html, re.I))
            if links < 10:
                errors.append(f"{tag}: only {links} links, need at least 10")
            kw = (m.get("keyword") or "").lower()
            if kw:
                heads = " ".join(re.findall(r"<h[234][^>]*>(.*?)</h[234]>", html, re.I | re.S)).lower()
                if kw not in heads:
                    errors.append(f"{tag}: keyword '{kw}' not in any H2 to H4")
                n = text.lower().count(kw)
                if n < max(5, words // 250):
                    errors.append(f"{tag}: keyword '{kw}' used {n} times, too few for {words} words")
            m["_words"] = words
            m["_html"] = html
            thumb = folder / m.get("thumbnail", "thumbnail.webp")
            m["_thumb_path"] = thumb if thumb.is_file() else None
            info = next((folder / f for f in ("infographic.gif", "infographic.webp") if (folder / f).is_file()), None)
            m["_info_path"] = info
            if m.get("infographic") and "{{infographic}}" not in html:
                errors.append(f"{tag}: meta has infographic but article.html lacks {{{{infographic}}}}")
            if m.get("published") and not re.match(r"^\d{4}-\d{2}-\d{2}$", m["published"]):
                errors.append(f"{tag}: published must be YYYY-MM-DD")
            m["_category"] = cat_slug
            m["_kind"] = "article"
            m["_dir"] = folder
            articles.append(m)

    for item in categories + articles:
        p = item.get("_thumb_path")
        if p and p.suffix.lower() not in IMG_TYPES:
            errors.append(f"{item['slug']}: thumbnail must be webp, jpg, png or gif")
        if p and p.stat().st_size > 10 * 1024 * 1024:
            errors.append(f"{item['slug']}: thumbnail over 10 MB")
    return parent_slug, parent, categories, articles, errors


# ----------------------------------------------------------------- admin client

class Admin:
    def __init__(self, base, email, password):
        import requests
        from bs4 import BeautifulSoup
        self.BS = BeautifulSoup
        self.base = base.rstrip("/")
        self.s = requests.Session()
        self.s.headers["User-Agent"] = "SWME-Educational-Publisher/1.0"
        orig = self.s.request

        def request_with_retry(method, url, **kw):
            import requests as rq
            for attempt in range(4):
                try:
                    return orig(method, url, **kw)
                except (rq.ConnectionError, rq.Timeout) as e:
                    if attempt == 3:
                        raise
                    wait = 5 * (attempt + 1)
                    print(f"    connection problem ({type(e).__name__}), retrying in {wait}s")
                    time.sleep(wait)
        self.s.request = request_with_retry
        self.email, self.password = email, password

    def url(self, path):
        return f"{self.base}/admin/{path.lstrip('/')}"

    def soup(self, resp):
        return self.BS(resp.text, "html.parser")

    def get(self, path, **kw):
        r = self.s.get(self.url(path), timeout=60, **kw)
        r.raise_for_status()
        if "/admin/login.php" in r.url and "login.php" not in path:
            raise PublishError("session expired or not logged in")
        return r

    @staticmethod
    def csrf(soup):
        el = soup.find("input", {"name": "_csrf"})
        if not el or not el.get("value"):
            raise PublishError("CSRF token not found, admin layout may have changed")
        return el["value"]

    def login(self):
        r = self.s.get(self.url("login.php"), timeout=60)
        token = self.csrf(self.soup(r))
        r = self.s.post(self.url("login.php"), timeout=60, data={
            "_csrf": token, "email": self.email, "password": self.password})
        r.raise_for_status()
        check = self.s.get(self.url(""), timeout=60)
        if "/admin/login.php" in check.url:
            raise PublishError("login failed, check SWME_EMAIL and SWME_PASSWORD")
        print("Logged in.")

    def pages(self):
        """Return {slug: {'id': int, 'title': str, 'status': str}} from the Pages list."""
        sp = self.soup(self.get("pages.php"))
        out = {}
        for row in sp.select("tbody tr"):
            a = row.find("a", href=re.compile(r"page-edit\.php\?id=\d+"))
            path = row.find("div", class_="text-muted")
            if not a or not path:
                continue
            pid = int(re.search(r"id=(\d+)", a["href"]).group(1))
            slug = path.get_text(strip=True).strip("/").split("/")[-1]
            badges = " ".join(b.get_text(strip=True).lower() for b in row.select(".badge"))
            out[slug] = {"id": pid, "title": a.get_text(strip=True),
                         "status": "draft" if "draft" in badges else "published"}
        if not out:
            raise PublishError("could not read the Pages list, admin layout may have changed")
        return out

    def current_form(self, path):
        sp = self.soup(self.get(path))
        form = None
        for f in sp.find_all("form"):
            if f.find(attrs={"name": "title"}):
                form = f
                break
        if form is None:
            raise PublishError(f"page form not found at {path}")
        values = {}
        for el in form.find_all(["input", "textarea", "select"]):
            name = el.get("name")
            if not name or el.get("type") == "file":
                continue
            if el.name == "textarea":
                values[name] = el.get_text()
            elif el.name == "select":
                opt = el.find("option", selected=True) or el.find("option")
                values[name] = opt.get("value", "") if opt else ""
            elif el.get("type") == "checkbox":
                if el.has_attr("checked"):
                    values[name] = el.get("value", "on")
            else:
                values[name] = el.get("value", "")
        return values

    def upload_image(self, path, name=None):
        """Upload an image through the editor's upload endpoint, return its URL or None."""
        if not hasattr(self, "_upload_url"):
            page = self.get("page-edit.php").text
            m = re.search(r'images_upload_url:"([^"]+)"', page)
            self._upload_url = m.group(1).replace("\\/", "/") if m else None
        if not self._upload_url:
            print("    warning: image upload endpoint not found")
            return None
        url = self.base + self._upload_url if self._upload_url.startswith("/") else self.url(self._upload_url)
        r = self.s.post(url, files={"file": (name or path.name, path.read_bytes(), IMG_TYPES[path.suffix.lower()])}, timeout=120)
        try:
            data = r.json()
        except ValueError:
            print(f"    warning: image upload failed for {path.name} (HTTP {r.status_code})")
            return None
        loc = data.get("location") or data.get("url") or data.get("path")
        if not loc:
            print(f"    warning: image upload returned no URL for {path.name}: {str(data)[:120]}")
        return loc

    def page_content(self, page_id):
        return self.current_form(f"page-edit.php?id={page_id}").get("content", "")

    def save(self, page_id, parent_id, fields, thumb_path, dry_run=False):
        path = f"page-edit.php?id={page_id}" if page_id else f"page-edit.php?parent_id={parent_id}"
        data = self.current_form(path)
        data.update({k: ("" if v is None else str(v)) for k, v in fields.items()})
        data["parent_id"] = str(parent_id)
        if dry_run:
            return None
        files = {}
        if thumb_path:
            files["card_image"] = (f"{fields.get('slug', 'image')}{thumb_path.suffix.lower()}", thumb_path.read_bytes(), IMG_TYPES[thumb_path.suffix.lower()])
        r = self.s.post(self.url(path), data=data, files=files or None, timeout=120)
        r.raise_for_status()
        if "/admin/login.php" in r.url:
            raise PublishError("session expired during save")
        err = self.soup(r).select_one(".alert-danger, .invalid-feedback.d-block")
        if err:
            raise PublishError(f"admin rejected save: {err.get_text(' ', strip=True)[:200]}")
        m = re.search(r"page-edit\.php\?id=(\d+)", r.url)
        return int(m.group(1)) if m else None


# ----------------------------------------------------------------- sync

def fields_for(item, content=None):
    if content is None:
        content = item["_html"] if item["_kind"] == "article" else item.get("intro", "")
    return {
        "title": item["title"],
        "slug": item["slug"],
        "subtitle": item.get("subtitle", ""),
        "content": content,
        "meta_title": item["meta_title"],
        "meta_description": item["meta_description"],
        "excerpt": item.get("summary", ""),
        "status": item.get("status", "draft"),
        "template": "default",
        "sort_order": item.get("sort_order", 0),
    }


SITE = os.environ.get("SWME_BASE_URL", "https://swme.ae").rstrip("/")


def nice_date(iso):
    import datetime
    try:
        return datetime.date.fromisoformat(iso).strftime("%d %B %Y").lstrip("0")
    except Exception:
        return iso or ""


def article_html(a, cat, images):
    """Article body with header (byline, share bar) and infographic."""
    color = cat.get("color", "#5f3dc4")
    url = f"{SITE}/{a['slug']}"
    from urllib.parse import quote
    u, t = quote(url, safe=""), quote(a["title"], safe="")
    mins = max(1, round(a.get("_words", 0) / 200))
    meta = (
        '<div class="d-flex flex-wrap align-items-center gap-3 small text-muted mb-3">'
        f'<span><i class="bi bi-person-circle me-1" style="color:{color};"></i>Written by <strong>{esc(a.get("author", "SWME Technical Staff"))}</strong></span>'
        f'<span><i class="bi bi-clock me-1" style="color:{color};"></i>{mins} min read</span>'
        + (f'<span><i class="bi bi-calendar3 me-1" style="color:{color};"></i>Published on {esc(nice_date(a.get("published")))}</span>' if a.get("published") else "")
        + '</div>'
    )
    shares = [
        ("LinkedIn", "bi-linkedin", "#0a66c2", f"https://www.linkedin.com/sharing/share-offsite/?url={u}"),
        ("Facebook", "bi-facebook", "#1877f2", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
        ("X", "bi-twitter-x", "#000000", f"https://twitter.com/intent/tweet?url={u}&text={t}"),
        ("WhatsApp", "bi-whatsapp", "#25d366", f"https://wa.me/?text={t}%20{u}"),
        ("Email", "bi-envelope-fill", "#6c757d", f"mailto:?subject={t}&body={u}"),
    ]
    share = ('<div class="d-flex flex-wrap align-items-center gap-2 pb-3 mb-4 border-bottom">'
             '<span class="small fw-semibold me-1">Share this guide:</span>'
             + "".join(f'<a class="d-inline-flex align-items-center justify-content-center rounded-circle text-white text-decoration-none" '
                       f'href="{esc(h)}" target="_blank" rel="noopener" title="Share on {n}" aria-label="Share on {n}" '
                       f'style="width:34px;height:34px;background:{c};"><i class="bi {i}"></i></a>' for n, i, c, h in shares)
             + '</div>')
    if a.get("_thumb_path"):
        a["_thumb_url"], _ = images.url(a["_thumb_path"], seo_name(a["slug"], a["_thumb_path"]))
    body = a["_html"]
    info = a.get("_info_path")
    if info and "{{infographic}}" in body:
        spec = a.get("infographic", {})
        iu, ih = images.url(info, seo_name(f'{spec.get("title") or a["slug"]} infographic', info))
        sz = img_size(info)
        dims = f' width="{sz[0]}" height="{sz[1]}"' if sz else ""
        a["_info_url"] = iu
        fig = (f'<figure class="my-5 text-center"><img class="img-fluid rounded-3 border" src="{esc(iu)}" data-hash="{ih}" '
               f'alt="{esc(spec.get("alt") or spec.get("title") or a["title"])}" title="{esc(spec.get("title", ""))}"{dims} loading="lazy">'
               f'<figcaption class="small text-muted mt-2">{esc(spec.get("title", ""))}</figcaption></figure>') if iu else ""
        body = body.replace("{{infographic}}", fig)
    else:
        body = body.replace("{{infographic}}", "")
    link_css = ('<style>article.prose:has(.edu-article) a:not([title^="Share"]):not(.card)'
                '{color:#0d6efd !important;text-decoration:underline;text-underline-offset:2px;}'
                'article.prose:has(.edu-article) a:not([title^="Share"]):not(.card):hover{color:#0a58ca !important;}</style>'
                '<div class="edu-article"></div>')
    host = SITE.split("://", 1)[-1]
    views = ('<div class="d-flex align-items-center gap-2 mt-5 pt-3 border-top small text-muted">'
             f'<i class="bi bi-eye" style="color:{color};"></i><span>Page views</span>'
             f'<img src="https://hits.sh/{esc(host)}/{esc(a["slug"])}.svg?label=views&amp;color={color.lstrip("#")}&amp;style=flat-square" '
             'alt="Page views" height="20" loading="eager" referrerpolicy="no-referrer"></div>')
    return link_css + meta + share + "\n" + body + "\n" + views + article_schema(a, cat, url)


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def breadcrumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}


def article_schema(a, cat, url):
    org = {"@type": "Organization", "name": "SWME Control Systems", "url": SITE,
           "logo": {"@type": "ImageObject", "url": f"{SITE}/uploads/brand/swme-logo.png"}}
    art = {"@context": "https://schema.org", "@type": "TechArticle", "headline": a["title"][:110],
           "description": a["meta_description"], "url": url, "mainEntityOfPage": url,
           "author": {"@type": "Organization", "name": a.get("author", "SWME Technical Staff"),
                      "url": f"{SITE}/about-us"},
           "publisher": org, "inLanguage": "en", "articleSection": cat["title"],
           "keywords": a.get("keyword", ""), "wordCount": a.get("_words", 0)}
    if a.get("published"):
        art["datePublished"] = art["dateModified"] = a["published"]
    if a.get("updated"):
        art["dateModified"] = a["updated"]
    full = lambda u: SITE + u if u.startswith("/") else u
    imgs = [full(u) for u in (a.get("_thumb_url"), a.get("_info_url")) if u and not u.startswith("#")]
    if imgs:
        art["image"] = imgs
    out = [art, breadcrumbs([("Home", SITE + "/"), ("Educational", f"{SITE}/educational"),
                             (cat["title"], f"{SITE}/{cat['slug']}"), (a["title"], url)])]
    faqs = re.findall(r"<summary[^>]*>(.*?)</summary>\s*(.*?)</details>", a["_html"], re.S)
    if faqs:
        clean = lambda h: re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", "", h))).strip()
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(ans)}}
            for q, ans in faqs]})
    return "".join(ld(o) for o in out)


def file_hash(path, name=""):
    return hashlib.sha1(path.read_bytes() + name.encode()).hexdigest()[:12]


def seo_name(stem, path):
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-") + path.suffix.lower()


def img_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


class ImageCache:
    """Maps image hash -> uploaded URL, seeded from data-hash attributes already on the site."""

    def __init__(self, admin, dry_run):
        self.admin, self.dry_run, self.map = admin, dry_run, {}

    def seed(self, html):
        for h, src in re.findall(r'<img[^>]*?data-hash="([0-9a-f]+)"[^>]*?src="([^"]+)"', html or ""):
            self.map.setdefault(h, src)
        for src, h in re.findall(r'<img[^>]*?src="([^"]+)"[^>]*?data-hash="([0-9a-f]+)"', html or ""):
            self.map.setdefault(h, src)

    def url(self, path, name=None):
        if not path:
            return None, None
        h = file_hash(path, name or "")
        if h not in self.map:
            self.map[h] = "#dry-run" if self.dry_run else self.admin.upload_image(path, name)
            if self.map[h] and not self.dry_run:
                print(f"    uploaded image {path.name}")
        return self.map[h], h


def esc(t):
    return htmllib.escape(t or "", quote=True)


def card_html(href, title, summary, img, h, cta, badge=None, color="#f5a623", icon=None):
    img_tag = (f'<img class="card-img-top" src="{esc(img)}" data-hash="{h}" alt="{esc(title)}" width="800" height="500" loading="lazy" '
               f'style="aspect-ratio:16/10;object-fit:cover;">') if img else ""
    icon_tag = (f'<span class="d-inline-flex align-items-center justify-content-center rounded-circle me-2" '
                f'style="width:36px;height:36px;background:{color};color:#fff;"><i class="bi {esc(icon)}"></i></span>') if icon else ""
    badge_tag = (f'<span class="small fw-semibold" style="color:{color};">{esc(badge)}</span>') if badge else ""
    head = (f'<div class="d-flex align-items-center mb-3">{icon_tag}{badge_tag}</div>') if (icon_tag or badge_tag) else ""
    return (
        '<div class="col-sm-6 col-lg-4">'
        f'<a class="card h-100 border-0 shadow-sm text-decoration-none overflow-hidden" href="{esc(href)}" '
        f'style="border-top:4px solid {color} !important;">'
        f'{img_tag}<div class="card-body p-4">{head}'
        f'<h3 class="h5 card-title text-dark mb-2">{esc(title)}</h3>'
        f'<p class="card-text text-muted small mb-3">{esc(summary)}</p>'
        f'<span class="fw-semibold" style="color:{color};">{esc(cta)} <i class="bi bi-arrow-right"></i></span>'
        '</div></a></div>'
    )


HIDE_SITE_LIST = ('<style>article.prose:has(.edu-marker) + .row.g-4.mt-2{display:none !important;}'
                  '.prose .edu-grid .card-title{margin-top:0;}</style>')


def grid_html(intro, heading, cards, empty_text):
    body = ('<div class="row g-4 edu-grid">' + "".join(cards) + "</div>") if cards else f'<p class="text-muted">{esc(empty_text)}</p>'
    return f'{HIDE_SITE_LIST}<div class="edu-marker" data-edu="listing"></div>{intro}\n<h2 class="mt-5 mb-4">{esc(heading)}</h2>\n{body}'


def visible(child, parent_status):
    return child.get("status", "draft") == "published" or parent_status == "draft"


def changed_filter(changed_file):
    if not changed_file:
        return None
    paths = [l.strip() for l in Path(changed_file).read_text().splitlines() if l.strip()]
    slugs, all_cats = set(), False
    for p in paths:
        parts = Path(p).parts
        if parts[:1] == ("articles",) and len(parts) >= 3:
            slugs.add(parts[2])
        elif p.startswith("config/") or p.startswith("assets/categories/"):
            all_cats = True
    return slugs, all_cats


def run(args):
    parent_slug, parent, categories, articles, errors = load_plan()
    print(f"Found {len(categories)} categories and {len(articles)} articles.")
    if errors:
        print("\nValidation errors:")
        for e in errors:
            print("  - " + e)
        return 1
    print("Validation passed.")
    if args.validate:
        return 0

    filt = changed_filter(args.changed)
    if filt is not None:
        slugs, all_cats = filt
        articles = [a for a in articles if a["slug"] in slugs]
        needed_cats = {a["_category"] for a in articles}
        if not all_cats:
            categories = [c for c in categories if c["slug"] in needed_cats]
            for c in categories:
                c["_only_if_missing"] = True
        print(f"Changed only: {len(categories)} categories, {len(articles)} articles.")

    email, password = os.environ.get("SWME_EMAIL"), os.environ.get("SWME_PASSWORD")
    if not email or not password:
        print("SWME_EMAIL and SWME_PASSWORD must be set.")
        return 1
    admin = Admin(os.environ.get("SWME_BASE_URL", "https://swme.ae"), email, password)
    admin.login()
    pages = admin.pages()
    if parent_slug not in pages:
        print(f"Parent page '/{parent_slug}' not found. Create it in the admin first.")
        return 1
    parent_id = pages[parent_slug]["id"]

    report, failed = [], 0
    all_cats = {c["slug"]: c for c in load_plan()[2]}
    all_articles = load_plan()[3]

    def do_save(item, p_id, content=None, label=None):
        nonlocal pages, failed
        slug = item["slug"]
        existing = pages.get(slug)
        action = "update" if existing else "create"
        try:
            admin.save(existing["id"] if existing else None, p_id, fields_for(item, content),
                       item.get("_thumb_path"), dry_run=args.dry_run)
            if not args.dry_run:
                time.sleep(1)
                pages = admin.pages()
                if slug not in pages:
                    raise PublishError("saved but page not found in list (slug may have been changed by the admin)")
            elif not existing:
                pages[slug] = {"id": 0, "title": item["title"], "status": "planned"}
            report.append(f"  {action:6} {label or item['_kind']:8} /{slug} [{item.get('status', 'draft')}]")
            print(report[-1] + (" (dry run)" if args.dry_run else ""))
            return True
        except Exception as e:
            failed += 1
            print(f"  ! {slug}: {e}")
            return False

    # 1. make sure category pages exist
    for c in categories:
        if c["slug"] not in pages:
            do_save(c, parent_id)

    images = ImageCache(admin, args.dry_run)
    seeded = set()

    # 2. articles
    for a in articles:
        cat = pages.get(a["_category"])
        if not cat:
            print(f"  ! {a['slug']}: category page '{a['_category']}' missing, skipped")
            failed += 1
            continue
        for seed_slug in (a["slug"], a["_category"]):
            if pages.get(seed_slug, {}).get("id") and seed_slug not in seeded:
                images.seed(admin.page_content(pages[seed_slug]["id"]))
                seeded.add(seed_slug)
        do_save(a, cat["id"], article_html(a, all_cats[a["_category"]], images))

    # 3. rebuild category listing pages
    touched = {c["slug"] for c in categories} | {a["_category"] for a in articles}
    for slug in sorted(touched, key=lambda s: all_cats[s].get("sort_order", 0)):
        c = all_cats[slug]
        if pages.get(slug, {}).get("id"):
            images.seed(admin.page_content(pages[slug]["id"]))
        kids = sorted([a for a in all_articles if a["_category"] == slug and visible(a, c.get("status"))],
                      key=lambda a: (a.get("sort_order", 0), a["title"]))
        cards = []
        for a in kids:
            img, h = images.url(a.get("_thumb_path"), seo_name(a["slug"], a["_thumb_path"]) if a.get("_thumb_path") else None)
            cards.append(card_html(f"/{a['slug']}", a["title"], a["summary"], img, h, "Read guide",
                                   color=c.get("color", "#f5a623"), icon=c.get("icon")))
        content = grid_html(c.get("intro", ""), c.get("grid_heading", "Guides in this section"), cards,
                            "New guides are coming soon.")
        content += ld(breadcrumbs([("Home", SITE + "/"), ("Educational", f"{SITE}/educational"),
                                   (c["title"], f"{SITE}/{c['slug']}")]))
        if kids:
            content += ld({"@context": "https://schema.org", "@type": "ItemList", "name": c["title"],
                           "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{k['slug']}",
                                                "name": k["title"]} for i, k in enumerate(kids)]})
        do_save(c, parent_id, content, "listing")

    # 4. rebuild the Educational landing page
    if parent and (touched or filt is None):
        p_status = parent.get("status", "draft")
        if pages.get(parent_slug, {}).get("id"):
            images.seed(admin.page_content(pages[parent_slug]["id"]))
        cards = []
        for c in sorted(all_cats.values(), key=lambda c: c.get("sort_order", 0)):
            if not visible(c, p_status):
                continue
            n = len([a for a in all_articles if a["_category"] == c["slug"] and visible(a, c.get("status"))])
            img, h = images.url(c.get("_thumb_path"), seo_name(c["slug"], c["_thumb_path"]) if c.get("_thumb_path") else None)
            badge = f"{n} guide{'s' if n != 1 else ''}" if n else "Coming soon"
            cards.append(card_html(f"/{c['slug']}", c["title"], c["summary"], img, h, "Explore guides", badge,
                                   color=c.get("color", "#f5a623"), icon=c.get("icon")))
        content = grid_html(parent.get("intro", ""), parent.get("grid_heading", "Browse by topic"), cards,
                            "Topics are coming soon.")
        content += ld(breadcrumbs([("Home", SITE + "/"), ("Educational", f"{SITE}/educational")]))
        do_save(parent, "", content, "landing")

    print(f"\nDone: {len(report)} ok, {failed} failed.")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="check files only")
    ap.add_argument("--dry-run", action="store_true", help="login and plan without saving")
    ap.add_argument("--changed", help="file listing changed paths (one per line)")
    args = ap.parse_args()
    try:
        sys.exit(run(args))
    except PublishError as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
