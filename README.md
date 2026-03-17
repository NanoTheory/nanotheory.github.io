# Nanotheory Group Website

Static website for the [Nanotheory research group](https://nanotheory.github.io) at UC Davis.

## Build

```bash
npm install   # first time only
npm run build # outputs static HTML to _site/
```

The build copies HTML to the repo root. Commit and push to `master` to deploy via GitHub Pages.

## Editing content

| What | File to edit |
|------|-------------|
| People | `src/_data/people.json` |
| Alumni | `src/_data/alumni.json` |
| Undergrads | `src/_data/undergrads.json` |
| Press items | `src/_data/press.json` |
| Research topics | `src/_data/research.json` |
| Software/codes | `src/_data/codes.json` |
| Site metadata, email, min publication year | `src/_data/site.json` |

### Publications

Each publication is a Markdown file in `src/publications/` with frontmatter only:

```yaml
---
title: "Paper Title"
authors: "A Author, B Author"
journal: "Journal Name"
volume: "1 (2), 345"
year: 2025
url: "https://doi.org/..."
---
```

Add a new one with the helper script:

```bash
python scripts/add-publication.py --title "..." --authors "..." --journal "..." --year 2025 --url "..."
```

Only publications with `year >= publicationsMinYear` (set in `site.json`) are shown.

## Editing layout

| What | File |
|------|------|
| Page structure (head, nav, footer, scripts) | `src/_includes/base.njk` |
| Navigation menu | `src/_includes/partials/nav.njk` |
| Main page | `src/index.njk` |
| Alumni page | `src/alumni.njk` |
| Thank you page | `src/thankyou.njk` |
| Styles | `assets/css/main.css` |
| Images | `images/` |
