# StatCard

A dashboard count for the CMS: a mono label with an icon, one big condensed number and a short note or link, optionally with a 12-week bar.

## Use
- `.rg-stats` (auto-fit grid, 200px minimum) > `.rg-stat` > `.rg-stat__label` (text + icon), `.rg-stat__value`, `.rg-stat__note`.
- `.rg-stat__bar` draws twelve weekly blocks; `.is-on` blocks are `highlight`, empty weeks keep a 6% stub in `surface-sunken`. Give it `role="img"` and an `aria-label` that lists the values.
- Each stat leads to a task: new requests to the inbox, missing alt text to the photos. Prefer counts Raf can act on over vanity numbers.

## Content
Only live figures from the CMS. The numbers in the preview are examples. The public website shows no statistics unless Raf supplies real ones.
