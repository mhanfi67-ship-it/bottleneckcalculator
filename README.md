# Bottleneck Calculator Website — flat structure, no subfolders

Every single file lives at the repo root. There are NO subfolders anywhere
(not even for images or other languages) specifically to avoid GitHub's
web-upload tool silently dropping folder structure or overwriting
same-named files (this has happened twice already with this project).

## Deploying an update (IMPORTANT — do this every time)

1. Go to your repo on github.com.
2. Select ALL existing files and DELETE them first. Commit that deletion.
   (This prevents any stale file from a previous broken upload lingering
   around and causing confusing bugs, like the Portuguese homepage
   accidentally overwriting the English one last time.)
3. Extract this zip locally.
4. Select every file INSIDE the extracted folder (not the zip itself,
   not the folder itself) and drag them ALL into GitHub's
   "Add file -> Upload files" box in one single batch.
5. Commit directly to `main`.
6. Wait 1-2 minutes for GitHub Pages to rebuild, then hard-refresh
   (Ctrl+Shift+R) the live site.

## Pages

- / (index.html) - homepage / calculator, English
- /es.html, /fr.html, /pt.html, /zh.html - homepage translated into
  Spanish, French, Portuguese and Chinese
- /about.html, /contact.html, /privacy.html, /terms.html
- /blog.html - guides hub
- /blog-*.html - 6 individual guides (English only for now)
- /calculator.html - redirect stub to / (kept only for old links)

## Notes

- Only the homepage is translated so far. Nav links from the translated
  homepages to About/Contact/Blog/etc. fall back to the English versions
  until those are translated too.
- The calculator's live results text (after clicking "Analyze") is still
  generated in English by app.js regardless of page language - that is a
  separate, bigger localization job.
- Keep the AdSense script only if the publisher ID belongs to the correct
  AdSense account.
- og-image.png is the shared social-share preview image (1200x630),
  referenced by every page's og:image / twitter:image tags.
