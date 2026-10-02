# Footer

The site footer on Dark: the logo with the company's own line, the page links, the contact details, the Facebook link and a strip of twelve red steps that rises to the legal line.

## Use
- `footer.rg-footer[data-theme="dark"]` > `.rg-container` > `.rg-footer__top` (`.rg-footer__brand` + `.rg-footer__cols`), `.rg-footer__steps`, `.rg-footer__bottom`.
- Logo: `rg-logo-on-dark.svg` at 240px wide.
- The brand line is the company's own wording: **Betontrappen ter plaatse bekist. Algemeen bekistingswerk.**
- Contact exactly as on the Contact page: **Wiekevorstsegoorweg 40, 2222 Wiekevorst**, **0495 51 29 02**, **info@betontrappenraf.be**.
- Facebook is where the realisations live today; keep the link until the CMS gallery replaces it, then keep it as a social link.
- `.rg-footer__steps` is decorative (`aria-hidden="true"`): twelve `span`s whose heights rise evenly, in `red-500`.
- The bottom line needs the ondernemingsnummer, which Belgian law requires on a business website. The one in the preview is a placeholder.
