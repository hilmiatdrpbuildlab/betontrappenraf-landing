# AdminShell

The frame of the CMS where Raf manages realisations, quote requests, photos and pages: a fixed sidebar, a top bar with search and the light/dark toggle, and a content column of panels.

## Use
- `.rg-cms[data-theme]` > `aside.rg-cms__side` (brand, `nav.rg-cms__nav`, `.rg-cms__user`) + `.rg-cms__main` (`.rg-cms__top`, `main.rg-cms__content`).
- Content starts with `.rg-cms__pagehead`: breadcrumbs in mono, a `t-h3` page title and the one primary action of the page (**Nieuwe realisatie**). Below it, panels: `section.rg-panel` > `.rg-panel__head` (a `t-h6` title + a link or small buttons) + `.rg-panel__body` or a table.
- Sidebar items: icon + label, `aria-current="page"` on the active one (red bar on the left edge, red icon). Counts for new requests use `rg-badge--accent`. Items: **Dashboard**, **Realisaties**, **Aanvragen**, **Media**, **Pagina's**, **Gebruikers**, **Instellingen**.
- Inside `.rg-cms` the control height drops to 40px and body text to 14px; everything else is the website's tokens.
- When the CMS is narrower than 760px (a container query, so it also works inside a panel) the sidebar becomes an off-canvas drawer opened by `.rg-cms__burger`; Escape closes it.

## Light and dark mode
- The CMS follows the user's system setting on first load (`prefers-color-scheme`), then remembers the choice from the moon button (`[data-rg-theme-toggle]`, stored as `rg-cms-theme`). Set `data-theme` on `<html>` before first paint to avoid a flash.
- Dark is not an inverted Light: grounds are `concrete-950` and `concrete-900`, red text moves to `red-400`, the primary button turns `red-500` with black text.
- The public website stays Light with Dark sections; it does not switch with the visitor's system setting.

## Content
The dashboard figures, names and dates in the preview are examples. Show only live data, and leave a stat out rather than show a guess.
