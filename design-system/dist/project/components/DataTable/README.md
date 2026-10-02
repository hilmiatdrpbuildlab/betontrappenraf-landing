# DataTable

The CMS list view for realisations, requests and media: a toolbar with search and filter, a table with selection, sortable columns, status badges and row actions, and a pager.

## Use
- `section.rg-panel[data-rg-table]` > `.rg-toolbar` (search `.rg-input-wrap`, filter `.rg-select-wrap`, `.rg-toolbar__bulk` with `[data-rg-count]`) + `.rg-table-wrap` > `table.rg-table` + `.rg-pager`.
- Selection: a header checkbox with `data-rg-all` and one per row. `js/rg.js` sets `aria-selected` on rows (red edge and tint), the header's indeterminate state, and shows the bulk bar with the count.
- Sortable columns: a `button` inside `th`, with `aria-sort` on the `th` (`ascending`, `descending`, `none`) and the matching icon (`chevron-up`, `chevron-down`, `arrow-up-down`).
- First column: `.rg-table__item` with a 48px `img.rg-table__thumb` (`alt=""`, the title says it), the title in bold and the slug in mono.
- Dates in mono, day first with leading zeros: **02-10-2026**. Status is always a Badge with dot and word.
- Row actions are ghost icon buttons with a Dutch `aria-label` that names the row: "Bewerk Kwartdraaiende trap". The destructive action lives in the overflow menu or the bulk bar and always goes through a Modal.
- The table scrolls sideways inside `.rg-table-wrap` on narrow screens; the page never does.

## Content
Rows in the preview are examples built from the photos.
