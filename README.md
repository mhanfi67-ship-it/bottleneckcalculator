# Bottleneck Calculator (bottleneckcalculator.cc)

Static site hosted on GitHub Pages with the custom domain in `CNAME`.

## Folder structure

```
/
├── index.html              English homepage (calculator)
├── about.html  contact.html  privacy.html  terms.html
├── 404.html                Not-found page, also forwards old URLs to new ones
├── blog/
│   ├── index.html          Guides hub  (/blog/)
│   └── *.html              Individual guides (/blog/<slug>.html)
├── es/  fr/  pt/  zh/      Translated homepages (/es/, /fr/, /pt/, /zh/)
├── assets/
│   ├── css/style.css
│   ├── js/app.js
│   ├── images/             Article images (.webp) and og-image.png
│   └── icons/              apple-touch-icon + PWA icons (192, 512)
├── favicon.ico             Must stay in the root (browsers request /favicon.ico)
├── manifest.json  robots.txt  sitemap.xml  ads.txt  CNAME  .nojekyll
```

All internal links use root paths (`/assets/...`, `/blog/`), so every page works
no matter which folder it sits in.

## Deploying

1. In the GitHub repo, delete all old files and commit.
2. Extract the zip. Open the extracted folder.
3. Select everything inside it (files AND folders) and drag it into
   "Add file > Upload files". Dragging keeps the folders. Do not use the
   "choose your files" button, because it flattens folders.
4. Commit to `main`, wait 1 to 2 minutes, then hard refresh (Ctrl+Shift+R).
5. In Google Search Console, resubmit `https://bottleneckcalculator.cc/sitemap.xml`.

## Local preview

Paths start with `/`, so open the site through a local server instead of
double-clicking files:

```
python -m http.server 8000
```

Then visit http://localhost:8000
