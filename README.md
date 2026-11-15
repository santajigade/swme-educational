# SWME Educational: auto publisher

Push articles to this repo and GitHub Actions publishes them to
**swme.ae/educational** through the website admin panel. No FTP needed.

## Structure

```
config/categories.json              Category pages (Flow, Pressure, Level ...)
assets/categories/*.webp            Category card images
articles/<category-slug>/<article-slug>/
    meta.json                       Title, SEO fields, status
    article.html                    Article body (HTML)
    thumbnail.webp                  Card image (optional)
scripts/publish.py                  Publisher
.github/workflows/publish.yml       Runs on every push to main
```

Page tree on the website:

```
/educational                         (Category template, created once in admin)
  /pressure-measurement-guides       (Category template, from config)
    /what-is-a-pressure-transmitter  (Standard page, from articles/)
```

## meta.json

```json
{
  "title": "What Is a Pressure Transmitter and How Does It Work?",
  "slug": "what-is-a-pressure-transmitter",
  "subtitle": "Working principle, types, output signals and selection tips",
  "meta_title": "Max 60 characters, brand is added by the site",
  "meta_description": "Max 160 characters",
  "summary": "Shown on the category card, max 200 characters",
  "status": "draft",
  "sort_order": 0,
  "thumbnail": "thumbnail.webp"
}
```

* `slug` must match the folder name and be unique across the whole website
  (URLs are flat: swme.ae/slug).
* `status`: `draft` or `published`.

## article.html rules

* Start with `<h2>`, never `<h1>` (the page title is the H1).
* Allowed: p, h2 to h4, ul, ol, table, img, a, blockquote, Bootstrap classes.
* Not allowed: `<script>`, `<style>` (the editor strips them).
* No em or en dashes. Minimum 150 words.

## One time setup

swme.ae blocks GitHub's servers, so publishing runs on a self-hosted runner
(a Windows PC that can open swme.ae). Validation still runs on GitHub.

0. On the PC: install Python 3.12 for all users with "Add to PATH" ticked, and
   Git for Windows. Then repo Settings > Actions > Runners > New self-hosted
   runner > Windows, run the commands shown, and answer Y to "run as service".
1. In swme.ae admin, Users: create a dedicated user for the publisher.
2. In this repo, Settings > Secrets and variables > Actions, add:
   * `SWME_EMAIL`
   * `SWME_PASSWORD`
3. Actions tab > "Publish to swme.ae Educational" > Run workflow > `dry-run`
   to confirm the login works.

## Daily use

* Add or edit an article folder and push to `main`. Only changed articles are published.
* Run the workflow manually with `all` for a full resync.
* Updating an existing slug updates that page instead of creating a duplicate.

## Local commands

```
pip install -r requirements.txt
python scripts/publish.py --validate
SWME_EMAIL=... SWME_PASSWORD=... python scripts/publish.py --dry-run
```
