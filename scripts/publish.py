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
IMG_TYPES = {".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png"}


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
    """Read config and article folders. Returns (parent_slug, categories, articles, errors)."""
    errors = []
    cfg = load_json(CONFIG)
    parent_slug = cfg.get("parent_slug", "educational")
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
            if len(re.sub(r"<[^>]+>", " ", html).split()) < 150:
                errors.append(f"{tag}: article is under 150 words")
            m["_html"] = html
            thumb = folder / m.get("thumbnail", "thumbnail.webp")
            m["_thumb_path"] = thumb if thumb.is_file() else None
            m["_category"] = cat_slug
            m["_kind"] = "article"
            m["_dir"] = folder
            articles.append(m)

    for item in categories + articles:
        p = item.get("_thumb_path")
        if p and p.suffix.lower() not in IMG_TYPES:
            errors.append(f"{item['slug']}: thumbnail must be webp, jpg or png")
        if p and p.stat().st_size > 10 * 1024 * 1024:
            errors.append(f"{item['slug']}: thumbnail over 10 MB")
    return parent_slug, categories, articles, errors


# ----------------------------------------------------------------- admin client

class Admin:
    def __init__(self, base, email, password):
        import requests
        from bs4 import BeautifulSoup
        self.BS = BeautifulSoup
        self.base = base.rstrip("/")
        self.s = requests.Session()
        self.s.headers["User-Agent"] = "SWME-Educational-Publisher/1.0"
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

    def save(self, page_id, parent_id, fields, thumb_path, dry_run=False):
        path = f"page-edit.php?id={page_id}" if page_id else f"page-edit.php?parent_id={parent_id}"
        data = self.current_form(path)
        data.update({k: ("" if v is None else str(v)) for k, v in fields.items()})
        data["parent_id"] = str(parent_id)
        if dry_run:
            return None
        files = {}
        if thumb_path:
            files["card_image"] = (thumb_path.name, thumb_path.read_bytes(), IMG_TYPES[thumb_path.suffix.lower()])
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

def fields_for(item):
    if item["_kind"] == "category":
        content, template = item.get("intro", ""), "category"
    else:
        content, template = item["_html"], "default"
    return {
        "title": item["title"],
        "slug": item["slug"],
        "subtitle": item.get("subtitle", ""),
        "content": content,
        "meta_title": item["meta_title"],
        "meta_description": item["meta_description"],
        "excerpt": item["summary"],
        "status": item.get("status", "draft"),
        "template": template,
        "sort_order": item.get("sort_order", 0),
    }


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
    parent_slug, categories, articles, errors = load_plan()
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
    for item in categories + articles:
        slug = item["slug"]
        if item["_kind"] == "category":
            p_id = parent_id
        else:
            cat = pages.get(item["_category"])
            if not cat:
                print(f"  ! {slug}: category page '{item['_category']}' missing, skipped")
                failed += 1
                continue
            p_id = cat["id"]
        existing = pages.get(slug)
        if existing and item.get("_only_if_missing"):
            continue
        action = "update" if existing else "create"
        try:
            admin.save(existing["id"] if existing else None, p_id, fields_for(item),
                       item.get("_thumb_path"), dry_run=args.dry_run)
            if not args.dry_run:
                time.sleep(1)
                pages = admin.pages()
                if slug not in pages:
                    raise PublishError("saved but page not found in list (slug may have been changed by the admin)")
            report.append(f"  {action:6} {item['_kind']:8} /{slug} [{item.get('status', 'draft')}]")
            print(report[-1] + (" (dry run)" if args.dry_run else ""))
        except Exception as e:
            failed += 1
            print(f"  ! {slug}: {e}")

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
