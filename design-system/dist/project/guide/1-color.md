# Color system

Four brand colours from the current site and the van, extended into scales: `red-500` #E83E4D, black, `concrete-400` #8A8F94 and white. Components use only the semantic tokens below; the palette exists to define them.

## Brand and primary
- `red-500` is the brand red: the logo, the step mark, riser lines, the Red ground, one accent word per title. It is a mark colour, not a text colour on Light (3.7:1 on `concrete-50`).
- `accent` is the primary action colour: `red-600` in Light (white text 5.3:1), `red-500` in Dark (black text 5.2:1), black in Red (white text 21:1). Hover is `accent-hover`, pressed `accent-press`.
- `link` is red text: `red-700` in Light (6.0:1 on `concrete-50`), `red-400` in Dark (5.4:1 on `concrete-900`). Links in running text are always underlined.
- `highlight` is for non-text marks (step marks, risers, active bars, dimension ticks): 3:1 or more on every ground.

## Neutrals, surfaces and backgrounds
The concrete scale is cool grey with the slight blue bias of fresh concrete.

| Token | Light | Dark | Red | Use |
| --- | --- | --- | --- | --- |
| `bg` | concrete-50 | concrete-950 | red-500 | Page and section ground |
| `surface` | white | concrete-900 | red-500 | Cards, panels, inputs, CMS chrome |
| `surface-sunken` | concrete-100 | concrete-800 | red-500 | Table headers, tab rails, read-only fields |
| `surface-inverse` | concrete-950 | concrete-50 | black | Toasts, tooltips |
| `line` | concrete-200 | 14% white | 22% black | Decorative hairlines |
| `line-strong` | concrete-500 | #7C8186 | black | Control borders (3:1 or more) |

## Text and hierarchy

| Token | Light | Dark | Red | Lowest ratio on bg / surface / sunken |
| --- | --- | --- | --- | --- |
| `ink` | concrete-950 | concrete-50 | black | 16.0 · 13.9 · 5.2 |
| `ink-soft` | concrete-600 | concrete-300 | #2B0A0E | 6.9 · 8.0 · 4.5 |
| `ink-faint` | concrete-500 | #9A9FA4 | #2B0A0E | 4.7 · 5.7 · 4.5 |
| `ink-inverse` | concrete-50 | concrete-950 | white | 17.6 on surface-inverse |

Hierarchy: headings and body in `ink`; leads, descriptions and meta in `ink-soft`; placeholders, captions and timestamps in `ink-faint`. Do not go lighter.

## Feedback and status
Each status has a text/icon colour and a tint. Every pair passes 4.5:1 for text, including `ink` on the tint.

| Status | Light text / tint | Dark text / tint | Used for |
| --- | --- | --- | --- |
| Success | teal-700 / teal-50 | teal-300 / #1F3532 | Gepubliceerd, saved, sent |
| Warning | amber-700 / amber-50 | amber-300 / #383123 | Gepland, missing alt text |
| Error | brick-700 / brick-50 | brick-300 / #3A2C2D | Form errors, failed saves, destructive buttons |
| Info | blue-700 / blue-50 | blue-300 / #28313B | Concept, tips |

- Success is teal, so it is never told from error by red-green hue alone.
- Error (`danger`) sits close to the brand red by nature. An error therefore always carries the `circle-x` icon and a sentence, and the brand red never appears on form controls.

## Light and dark mode
- Website: Light is the page; Dark and Red are section themes set with `data-theme` on a section. The site does not follow the visitor's system setting; the dark hero and footer already give it contrast.
- CMS: full light and dark modes. Follow `prefers-color-scheme` on first load, then the user's choice from the top bar toggle, by setting `data-theme` on `<html>`.
- Dark is designed, not inverted: grounds `concrete-950` / `concrete-900`, red text moves up to `red-400`, buttons keep `red-500` with black text, shadows deepen.

## Accessibility and contrast rules
- Body text and anything under 24px (or 19px bold): 4.5:1 minimum (AA). The system's body text reaches 7:1+ (AAA) on every Light and Dark ground.
- Large display type (24px+): 3:1 minimum, which is why `red-500` may set one accent word in a `t-display` or `t-h1`.
- Control borders, focus rings, icons that carry meaning: 3:1 minimum (WCAG 1.4.11). `line-strong` is 4.7:1 or more in Light.
- Never put white text on `red-500` (4.0:1) or body text in `concrete-400` (3.0–3.3:1).
- Run `python src/check_contrast.py` after any colour change; it fails on a pair below its floor in any theme.
