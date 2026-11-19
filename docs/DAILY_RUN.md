# Daily run: 4 new Educational guides for swme.ae

Santaji authorised on 15 November 2026 that 4 guides are written and published every
morning without his approval. Work unattended. Quality first: publish fewer rather than
publish something wrong.

## Setup
1. Clone this repo, set git user "SWME Educational" and email santajigade@users.noreply.github.com.
2. `pip install --break-system-packages requests beautifulsoup4 pillow` if missing.
   rsvg-convert is used to check SVG diagrams (apt or `pip install cairosvg` as fallback).
3. Read docs/ARTICLE-TEMPLATE.md, docs/LINKS.md, docs/TOPIC-QUEUE.md and two existing
   sources in tools/content/ (for example how-an-rtd-works.py and types-of-industrial-valves.py).

## Steps
1. **Pick 4 topics** from docs/TOPIC-QUEUE.md: the first unchecked topic in 4 different
   categories, rotating so categories that were used least recently go first.
   Skip any topic already covered by a published guide or an SWME blog post in docs/LINKS.md.
   If fewer than 12 unchecked topics remain, add 12 new ones (2 per category) with real
   search demand, checked with WebSearch.
2. **Research** each topic with WebSearch and WebFetch. Every number, standard and rule must
   come from a reliable source you read. Never invent figures.
3. **Write** tools/content/<slug>.py for each topic, following the approved template:
   * META: category, title, keyword, subtitle, meta_title (max 60), meta_description (max 160),
     summary, card_title, author "SWME Technical Staff", published = today (IST, YYYY-MM-DD),
     status "published", sort_order (next number in that category), thumbnail, infographic.
   * Infographic: pick a layout that differs from the other guides in the same category
     (steps, grid, flow, compare or levels) and from the other 3 guides of the day.
   * BODY: takeaways, intro (bold keyword, SWME product link), toc, sections with
     INFOGRAPHIC, at least one SVG diagram (svg() or svg_chain()) that is technically correct,
     rows or table, dyk (Did you know), twocol or checklist, mistakes, faq (3 questions).
   * 800 to 1,300 words, 10 or more links (SWME product pages, existing guides and blog posts,
     then instrumentationblog.in, zentacalculator.com, zentaengineering.com from docs/LINKS.md),
     keyword in an H2, plain professional tone, no em or en dashes and no hyphenated words in
     visible text (also inside SVG text), use "&amp;" for "&".
   * Link each new guide to 1 or 2 related existing guides (URL = /<slug>).
   * **Humanize the writing** (Santaji's instruction, 19 November 2026, applies from 20 November 2026):
     after drafting each guide, invoke the Skill tool with `humanize-writing:humanize-writing` and run
     every piece of visible prose through it (intro, paragraphs, rows, table cells, Did you know,
     checklist, mistakes, FAQ, infographic text). Keep every fact, number, source attribution, link,
     focus keyword and template component unchanged, and keep all writing rules above (no em or en
     dashes, no hyphenated words, keyword count). Then rebuild and validate again in step 4.
4. **Build and check**
   * `python tools/build_article.py <slug> ...`
   * `python tools/make_card_images.py --missing`
   * `python scripts/publish.py --validate` must pass.
   * Render every new SVG with rsvg-convert and look at it with the Read tool. Fix overlaps,
     clipped text or wrong technical content. Look at the last frame of every new infographic.gif
     and at every new thumbnail.webp.
   * Check that the slug is not used on swme.ae: WebFetch https://swme.ae/<slug> must not
     return a real page. If it exists, change the slug.
5. **Publish**: tick the topics in docs/TOPIC-QUEUE.md (move them to "Published" with today's
   date), commit everything (end the message with the attribution lines), `git pull --rebase`,
   `git push origin main`. The push starts the GitHub Actions workflow "Publish to swme.ae
   Educational", which publishes through the self hosted runner on Santaji's PC.
6. **Confirm**: dispatching is automatic. Check the newest run with
   `gh api repos/santajigade/swme-educational/actions/runs?per_page=1` and its jobs every
   60 seconds for up to 15 minutes. The publish log must end with "0 failed".
   * If the publish job stays "queued", the PC runner is offline. Nothing is lost: every publish
     run, and a catch up check every 3 hours, publishes all guides that are not yet live as soon
     as the PC is on and run.cmd is running. Say so in the report.
   * If it fails, read the job log and report the error. Never force anything on the live site.

## Report (one short SendUserMessage)
Titles with live URLs (https://swme.ae/<slug>), anything skipped and why, publish status,
how many topics are left in the queue, and a reminder to request indexing in Search Console.
