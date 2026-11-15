# SWME Educational: approved article template

Approved on 15 November 2026 (sample: what-is-a-pressure-transmitter).

## Added automatically by the publisher
1. No featured image on the article page (title shows in the site banner). Card images on listings stay.
2. Byline row: Written by SWME Technical Staff, reading time, Published on date.
3. Share bar: LinkedIn, Facebook, X, WhatsApp, Email.
4. Animated GIF infographic at `{{infographic}}` (steps from meta.json).
5. Site banner "Need help selecting the right product?" appears below every page,
   so articles have no closing CTA paragraph.

## Article body (article.html)
* Key takeaways box (category light tint, left border in category colour).
* Short intro, product link to the matching SWME product page.
* "In this guide" table of contents with jump links.
* Full width info rows as <div> blocks, never <ul>/<li> (the site adds tick icons to list items): light tint, coloured left border, bold label, for
  "At a glance" figures, concept definitions and common mistakes (orange).
* `{{infographic}}` inside the "How it works" section.
* At least one "Did you know?" box (light yellow, bulb icon).
* Tables: light category tint header, soft striped rows, light borders.
* Two column comparison boxes with light colour backgrounds (e.g. blue / green).
* Numbered selection checklist.
* FAQ: 3 short questions in a light box, first open, others closed.
* All text at normal article font size (no `small`).

## Writing rules
* No em or en dashes, no hyphenated words in visible text.
* At least 10 links. External links favour instrumentationblog.in,
  zentacalculator.com and zentaengineering.com, then official sites.
* Focus keyword in at least one H2 to H4 and used naturally throughout.
* Plain, professional whitepaper tone with "For example," and "In addition,".
* About 1,300 to 1,500 words.

## meta.json
title, slug, keyword, subtitle, meta_title (max 60), meta_description (max 160),
summary, card_title, author, published (YYYY-MM-DD), status, sort_order,
thumbnail, infographic {title, alt, steps: [[label, text], ...]}.
