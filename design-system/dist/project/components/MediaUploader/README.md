# MediaUploader

How photos get into the CMS: a dashed drop zone that turns red-edged when a file is dragged over it, and a list showing each file's progress, result and missing alt text.

## Use
- `.rg-drop` > the `upload` icon, a bold call (**Sleep foto's hierheen**), a hint with formats and size, and a full-cover `input[type=file][multiple]` labelled by a `label[for]` above the zone. `js/rg.js` adds `.is-over` during a drag.
- `ul.rg-files` > `li.rg-file` per file: a 56px thumbnail (or `.rg-file__ph` with an icon), `.rg-file__name`, `.rg-file__meta` and one action.
- States: uploading (meta shows size and percent, `.rg-progress` with `role="progressbar"` and its values), missing alt text (`.rg-file__meta.is-warn` and an **Aanvullen** button), done (size, **Omslagfoto** on the first), refused (`.rg-file--error`, `.rg-file__meta.is-error` with the reason and the fix).
- Every photo needs alt text before its project can be published; the Dashboard counts those still missing.
- Phone photos come in portrait; the site crops them with `object-fit`, so never ask Raf to crop.

## Copy
Errors name the file problem and the fix: "HEIC wordt niet ondersteund. Bewaar de foto als JPG en probeer opnieuw."
