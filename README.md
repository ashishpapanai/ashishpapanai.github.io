# ashishpapanai.github.io

Personal academic website — a minimal, single-page Jekyll site hosted on GitHub Pages.

## Structure

- `_pages/about.md` — the homepage (bio, news, publications, writing, notes, experience, education).
- `_pages/cv.md`, `_pages/awards.md` — secondary content pages.
- `_layouts/home.html` — standalone layout for the homepage.
- `_layouts/page.html` — layout for CV / awards / 404.
- `assets/css/minimal.css` — the entire theme (light + dark, responsive).
- `images/profile.jpg` — profile photo.

## Editing

- **News / publications / notes:** edit the corresponding `<section>` in `_pages/about.md`.
- **Writing:** posts are pulled live from Medium via RSS (client-side); no edits needed.
- **Visitor counter:** the footer badge in `_layouts/home.html` (hits.sh).

## Local development

```bash
bundle install
bundle exec jekyll serve   # http://127.0.0.1:4000
```

On GitHub Pages the site builds automatically on push to `main`.
