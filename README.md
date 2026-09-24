# Bottleneck Calculator Website

## Structure

    /                    <- HTML pages live here (kept flat on purpose, see below)
    /css/style.css
    /js/app.js
    /images/*.webp       <- 11 blog/homepage illustrations
    /icons/              <- favicon.ico, favicon-16x16.png, favicon-32x32.png,
                            apple-touch-icon.png, icon-192.png, icon-512.png,
                            og-image.png (social share preview)

## Why the HTML pages themselves are NOT in subfolders

Two earlier uploads broke the live site because GitHub's web "Upload
files" tool does not reliably preserve folder structure unless you drag
actual folder ICONS onto it. The worst break happened because 5 files
were all named "index.html" (root + one per language folder) - when
folder structure got lost, only one of them survived and it silently
overwrote the real English homepage with the Portuguese one.

To avoid that ever happening again, every HTML page has a unique
filename and sits flat at the root: index.html, es.html, fr.html,
pt.html, zh.html, about.html, contact.html, privacy.html, terms.html,
blog.html, blog-*.html (6 guides), calculator.html (redirect stub).

Static assets (css/js/images/icons) ARE in subfolders for a cleaner,
more professional layout, since a lost/misplaced CSS or image file is
inconvenient but not destructive the way an overwritten homepage is.

## HOW TO UPLOAD WITHOUT LOSING THE FOLDERS (important)

GitHub's uploader preserves subfolders ONLY if you drag the folder
ICONS themselves from your file manager (Finder/Explorer) onto the
upload page - not if you open them and select files from inside.

1. Extract this zip locally into one folder.
2. Go to your repo on github.com -> select every existing file -> delete
   them all -> commit (clears out old/stale files from earlier uploads).
3. Click "Add file -> Upload files".
4. From your file manager, select ALL items at the top level of the
   extracted folder together: index.html, es.html, ... AND the css,
   js, images, icons folder icons themselves (not their contents).
5. Drag that whole selection - files and folder icons together - onto
   the GitHub upload box in one go. GitHub will show nested paths like
   "css/style.css" in the preview; if it instead shows a flat list of
   loose files with no folder names, STOP and try again with an actual
   drag from the file manager rather than a "choose files" dialog.
6. Commit directly to `main`.
7. Wait 1-2 minutes, then hard-refresh (Ctrl+Shift+R) the live site.

If you want to remove this risk entirely, using the free GitHub
Desktop app instead (point it at a local folder, it commits and
pushes the whole tree exactly as-is every time) avoids this class of
problem completely.

## Notes

- Only the homepage is translated so far (es/fr/pt/zh.html). Nav links
  from those to About/Contact/Blog/etc. fall back to the English
  versions until those get translated too.
- The calculator's live results text (after clicking "Analyze") is
  still generated in English by app.js regardless of page language -
  a separate localization task.
- Keep the AdSense script only if the publisher ID belongs to the
  correct AdSense account.
- Please also manually delete these leftover files sitting in the
  repo from earlier uploads, since they're unused clutter:
  favicon.svg, bottleneckcalculator-adsense-ready-v2.zip,
  README-GOOGLE-SITEMAP.txt (step 2 above already covers this if you
  delete everything before re-uploading).
