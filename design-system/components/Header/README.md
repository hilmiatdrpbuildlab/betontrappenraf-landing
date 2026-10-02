# Header

The site bar: the logo, four page links, the phone number in mono and one **Offerte aanvragen** button. Under 1024px the links and phone move into a full-width drawer.

## Use
- `header.rg-header` > `.rg-container` > `.rg-header__bar` with `.rg-header__logo`, `nav.rg-nav`, `.rg-header__actions`; then `.rg-drawer` for the phone menu. `js/rg.js` opens the drawer, swaps the menu and close icons, and closes it on Escape.
- On Light pages use `rg-logo.svg`. Inside the Dark hero add `.rg-header--transparent` and use `rg-logo-on-dark.svg`.
- Mark the current page with `aria-current="page"`: the 3px red riser bar sits under it. The same bar slides in on hover.
- The phone number is always visible on desktop: most of Raf's work starts with a call. Write it `0495 51 29 02`, link it `tel:+32495512902`.
- Proposed pages: **Realisaties**, **Werkwijze**, **Over Raf**, **Contact**. The current site is a single page, so confirm the menu with Raf before building.
- Logo height 44px (36px on phones).

## Avoid
- More than four links, or a dropdown menu.
- A sticky header taller than 64px once scrolled.
