# Tabs

Switch between views of the same thing: underline tabs with the red marker for the CMS editor and request inbox, and a boxed segmented control for small view switches.

## Use
- `[data-rg-tabs]` > `.rg-tabs__list[role=tablist][aria-label]` of `button.rg-tabs__tab[role=tab]` (each with `aria-controls` and `aria-selected`; inactive ones `tabindex="-1"`) + one `.rg-tabs__panel[role=tabpanel]` per tab (`aria-labelledby`, `hidden` when inactive).
- `js/rg.js` handles click, Left/Right, Home and End.
- `.rg-tabs__count` adds a mono count (**Foto's 6**, **Nieuw 3**). Counts are live data.
- `.rg-tabs--boxed` for two or three view options (**Lijst**, **Raster**).
- Tab labels are one or two words, uppercase by CSS.

## Avoid
- Tabs as page navigation; that is the Header's job.
- Filter chips styled as tabs. Filters are Tags (see Badge).
