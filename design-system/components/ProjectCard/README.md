# ProjectCard

One realisation per card: Raf's photo with a type badge, a short title and a mono line of specs. The grid card fills the Realisaties page; the wide card features one project on the homepage.

## Use
- Grid: `.rg-projects` (3 columns, 2 under 980px, 1 under 760px) of `article.rg-project` > `.rg-project__media` (`img`, `span.rg-badge.rg-badge--solid`, optional `span.rg-project__arrow`) + `.rg-project__body` (`h3.rg-project__title` with a link, `.rg-project__specs`).
- The title link's `::after` covers the card, so the whole card is clickable; the focus ring draws around the card.
- Wide: add `.rg-project--wide`. The title turns condensed uppercase; add a status line in `t-label`, one paragraph and a `.rg-textlink`.
- Photos are 4:5 portrait in the grid (Raf's phone photos are portrait) and 4:3 in the wide card, cropped by `object-fit`. Photo zoom on hover is 3% over `dur-slow`.
- Specs: two or three short facts in `t-measure` style: the type of run (**Rechte steekgang**, **Kwartdraaiend**), the number of treads, the finish (**Ruw beton**, **Bekleed**). Use real numbers from Raf only.
- In the CMS each project has: title, type (one of the Badge types), status, photos with alt text, up to three specs, an optional municipality (only with the client's consent) and a date.

## Content
The titles in this preview only describe what the photos show. Replace them with Raf's real project details. Alt text in Dutch says what is visible: "Bekisting van een keldertrap tussen snelbouwmuren".
