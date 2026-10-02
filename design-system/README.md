The design system for the new betontrappenraf.be and its CMS. Raf Geerts casts concrete stairs in place (betontrappen ter plaatse bekist) and does general formwork from Wiekevorst. The system is built on his own logo, the red, black and concrete grey of his current site and van, and his own site photos. It should feel the way a good stair is made: sturdy, reliable, precise.

Read this page first, then the guide sections: **Color system**, **Typography**, **Spacing and layout**, **Components and interaction**, **CMS** and **CSS and Tailwind**.

## Brand and design philosophy

Personality: industrial, modern, clean, robust, professional. Raf is a craftsman, not a corporation; the site speaks plainly and lets the stairs do the convincing.

- **Concrete ground, black type, one red.** Pages sit on `concrete-50` with `concrete-950` text. `red-500` is the brand and is used sparingly: the logo, the step mark, riser lines, one accent word, the primary button. Never fill large areas with red except the one Red band per page.
- **Built from treads and risers.** The signature shape is the stair profile: the three-tread step mark that leads every eyebrow (`.rg-step-mark`), the rising Werkwijze steps, the twelve red steps in the footer, the stair-type tiles in the quote form. Use those; do not invent other ornaments.
- **Square and measured.** Corners are `radius-none` to `radius-sm` (4px at most on the public site). Lines are 1px hairlines or 3–4px red risers. Measurements are set in mono with real units (`t-measure`).
- **Condensed and loud, then quiet.** Display and section titles are Archivo, uppercase, 75% width, weight 800. Everything else is Archivo at normal width in sentence case. One `t-display` per page.
- **His work is the imagery.** Every photo on the site is a stair Raf built, in formwork or finished. No stock photos of other people's work.
- **Light page, Dark and Red sections.** Build pages on the Light theme. Switch whole sections with `data-theme="dark"` (hero, Werkwijze, footer) or `data-theme="red"` (the call-to-action band). Never put two Dark sections back to back.

High-level rules for consistency:
- Components never use palette tokens directly; they use the semantic tokens (`bg`, `surface`, `surface-sunken`, `ink`, `ink-soft`, `ink-faint`, `line`, `line-strong`, `accent`, `on-accent`, `link`, `highlight`, `focus` and the status pairs), which change with the theme.
- One primary action per view. A second action is an outline button or a text link.
- Spacing comes from the 4px scale only (`space-3xs` to `space-5xl`).
- Every interactive element has a visible 2px `focus` ring at 2px offset. Never remove it.
- Everything that moves respects `prefers-reduced-motion`.

## Content and voice

- Dutch (Flemish), formal: the reader is **u / uw**. The company speaks as **wij** or by name, **Raf**: "Raf meet de trapopening op de werf."
- Short, concrete sentences in the trade's own words: **bekisten**, **wapenen**, **storten**, **ontkisten**, **optrede**, **aantrede**, **bordes**, **kwartdraaiend**, **ruwbouw**, **werf**.
- The company's own claims, used as written: **Betontrappen ter plaatse bekist** and **Algemeen bekistingswerk**. Never invent years of experience, project counts, guarantees, lead times or reviews; ask Raf.
- Sentence case in the source for every heading and button. CSS sets the capitals on display titles, buttons, nav and labels, so the CMS stores normal text.
- Buttons say what happens in two or three words: **Offerte aanvragen**, **Bekijk realisaties**, **Aanvraag versturen**, **Opslaan**.
- Phone `0495 51 29 02` (link `tel:+32495512902`), e-mail `info@betontrappenraf.be`, address `Wiekevorstsegoorweg 40, 2222 Wiekevorst`. Dates day first: **2 oktober 2026** in text, **02-10-2026** in CMS tables. Measurements with a comma and a space: **18,5 cm**, **2,78 m**.
- No emoji and no exclamation marks. Errors explain what went wrong and how to fix it, without apologising.

## Logo

- Five vector files in `assets/logo`, traced from Raf's own logo: `rg-logo.svg` (primary, Light), `rg-logo-on-dark.svg` (Dark and dark photos), `rg-logo-on-red.svg` (Red ground, as on his van), `rg-logo-mono-black.svg` and `rg-logo-mono-white.svg` (one colour).
- The lockup is two lines, **RAF GEERTS** over **BETONTRAPPEN**, in the logo's rounded heavy lettering. That lettering is artwork only; never set other text in a lookalike face.
- Minimum height 32px on screen (header 44px, 36px on phones; footer 240px wide). Clear space on every side equals the height of the letter E in BETONTRAPPEN.
- Never recolour it outside these five files, stretch it, outline it, add shadows or put the primary version on a photo. There is no separate mark yet; for avatars and favicons ask Raf before cutting one.

## Imagery

- Photos are Raf's own, in `assets/photos/client`: formwork in progress (bekisting), freshly stripped concrete, finished stairs, a stair plan and his van. Show the process as proudly as the result: the formwork is the craft.
- They are phone photos in portrait. Crop with `object-fit: cover`, 4:5 in grids and 4:3 in feature cards. Never stretch.
- Photos under text always get the hero gradient or `scrim`.
- Alt text in Dutch describes what is visible: "Bekisting van een keldertrap tussen snelbouwmuren". Photos that only decorate a panel take `alt=""`.
- The files in this system are screen captures at about 760px wide from the Facebook page. Replace them with Raf's originals before launch.

## Iconography

- Lucide icons, inlined as SVG so they take `currentColor`, stroke 2, with square caps and mitred joins for a sharper, measured look. 20px by default (`.rg-icon`), 16–18px inside buttons and badges, 28px in process steps.
- Fixed roles: `arrow-right` in leading buttons and text links, `phone`, `mail`, `map-pin` for contact, `ruler`, `hammer`, `layers`, `check` for the four Werkwijze steps, `info`, `circle-check`, `triangle-alert`, `circle-x` for status, `plus`/`minus` in the FAQ, `chevron-down` in selects.
- The Facebook mark (Simple Icons, filled) appears only in the footer and the contact block.
- Icons beside text get `aria-hidden="true"`; icon-only buttons get a Dutch `aria-label`.
- The step mark is not an icon; it is the `.rg-step-mark` shape in CSS.

## Motion and states

- Crisp and short, no bounce: colours `dur-fast` (120ms), arrows, accordions and switches `dur-base` (200ms), photo zoom and modal entry `dur-slow` (320ms), all on `ease-out`.
- Signature interactions: the arrow in a button slides 4px right; the red riser bar slides in under a nav link; a pressed button drops 1px; a project photo zooms 3%.
- Disabled is 40% opacity and no pointer. Loading keeps the button's width and puts a spinning `loader-circle` before the label.

## Accessibility

- Target WCAG 2.2 AA everywhere, AAA for body text: `ink` on every ground is 13.9:1 or more in Light and Dark.
- Every text colour's usage note names the grounds it passes on, with the ratio; `src/check_contrast.py` checks all of them in every theme.
- Brand traps: white on `red-500` is only 4.0:1, so the Light primary button is `red-600` (5.3:1) and Dark red buttons carry black text. `concrete-400`, the brand grey, is 3.0–3.3:1: decoration and 24px+ type only.
- Status never relies on colour: each badge, alert and toast has a word and an icon, and success is teal so it never depends on red-green hue.
- Touch targets are 40px or more (48px default on the website). Forms label every field above it, link hints and errors with `aria-describedby`, and move focus to the first error.

## Building with it

- Load `css/tokens.css`, then `css/rg.css`, then `js/rg.js`. Wrap the page in `body.rg`. Tailwind projects use `tailwind.config.js` on top of `tokens.css`.
- Each component's rules are in `components/<Name>/README.md`, its markup in `components/<Name>/preview.html` (copy the expanded markup from `styleguide.html`).
- `tokens.json` is the source of truth. After changing it run `python src/build.py` and `python src/check_contrast.py`.
