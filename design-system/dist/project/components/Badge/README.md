# Badge

Small mono uppercase labels for project types and CMS states, plus the pressable filter tags that sort the Realisaties page.

## Use
- `span.rg-badge` on any ground. Variants: default (`surface-sunken`), `--outline`, `--solid` (ink), `--accent` (`red-500` with black text, for **Nieuw** only).
- Project types are a fixed list: **Binnentrap**, **Buitentrap**, **Keldertrap**, **Kwarttrap**, **Bordestrap**, **Bekistingswerk**. Add a type only when Raf adds one in the CMS.
- CMS status badges always carry `.rg-badge__dot` and the word, never colour alone: **Gepubliceerd** (`--success`), **Concept** (`--info`), **Gepland** (`--warning`), **Offline** (`--danger`).
- Filter tags: `button.rg-tag` with `aria-pressed`, inside `.rg-tags[data-rg-filter]` with a `role="group"` and an `aria-label`. `js/rg.js` keeps one pressed and fires an `rg:filter` event with the value. `.rg-tag__count` shows the number of projects; it must be the real count from the CMS.

## Avoid
- Badges as buttons. Anything clickable is a Tag or a Button.
- More than two badges on one project card.
