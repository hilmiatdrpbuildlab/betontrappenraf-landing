# Components and interaction

Twenty-three components, each with its own card, live preview and rules. This section is the summary spec of the core set. Class prefix `rg-`; every colour is a semantic token, so each component works in Light, Dark and Red.

## Buttons

| Variant | Fill / text | Hover | Active (pressed) | Focus | Disabled |
| --- | --- | --- | --- | --- | --- |
| Primary `.rg-btn` | `accent` / `on-accent` | `accent-hover` | `accent-press`, 1px drop | 2px `focus` ring, 2px offset | 40% opacity, no pointer |
| Secondary `--secondary` | `ink` / `ink-inverse` | ink 82% | ink 72%, 1px drop | same | same |
| Outline `--outline` | transparent, 1px `ink` border / `ink` | fills `ink`, text `ink-inverse` | ink 82% | same | same |
| Ghost `--ghost` | transparent / `ink` | 8% ink wash | 14% ink wash | same | same |
| Danger `--danger` (CMS) | `danger` / `bg` | danger 86% | same | same | same |

- Sizes: small 40px (13px text), default 48px (15px), large 56px (16px); the CMS default is 40px. Horizontal padding 16 / 22 / 28px. Corners `radius-xs`.
- Label: Archivo 700, uppercase, 85% width, 0.04em tracking. Icon 18px, 8px gap.
- Micro-interactions: the trailing `arrow-right` slides 4px right on hover (`dur-base`); colours change in `dur-fast`; press drops 1px. Loading keeps the width, dims the label and spins `loader-circle`.

## Cards and containers
- `.rg-card`: `surface`, 1px `line` border, `radius-sm`, padding `space-lg` (`space-xl` for `--lg`), internal gap `space-md`.
- `--raised` swaps the border for `shadow-md`; `--sunken` uses `surface-sunken` and no border; `--interactive` makes the whole card one link, hover border `line-strong` + `shadow-sm`.
- Project cards have no frame at all: a square-cut photo (4:5) with a solid badge, then the title and mono specs. Hover zooms the photo 3% over `dur-slow` and nudges the red arrow block.
- Panels in the CMS (`.rg-panel`) are cards with a ruled head row.

## Form controls
- Inputs, selects and textareas: 48px tall (40px in CMS), `radius-xs`, 1px `line-strong` border on `surface`, 14px side padding, 16px text (prevents zoom on iOS).
- States: hover border `ink`; focus 2px `focus` ring at 2px offset plus `ink` border; error 2px `danger` border, `aria-invalid="true"` and a message with `circle-x`; success `success` border with a `check` line; disabled `surface-sunken`, `ink-faint` text; read-only `surface-sunken` with a dashed border.
- Labels sit above the field (14px, 600). Hints in 13px `ink-faint`. Required `*` in `link` red; optional fields marked **(optioneel)**.
- Unit inputs (`.rg-input-group`) append a mono unit cell: **cm**, **m**.
- Checkbox 20px square, radio 20px round, both fill with `accent` and an `on-accent` mark. Switch 44×24 pill, CMS only. Option tiles show each stair type as a profile and take a 2px `accent` border when chosen.
- Validation runs on submit, focuses the first error and clears each error as soon as the value is valid; no red before the user has tried.

## Navigation header and footer
- Header: 80px (64px on phones) on `surface` with a bottom hairline, or transparent over the Dark hero. Logo 44px, four links in Archivo 700 uppercase 14px, phone in mono with a red phone icon, one small primary button. The current page and hovered link get a 3px `highlight` riser bar that slides in from the left. Under 1024px: menu button and a full-width drawer with 28px condensed links and a call button; Escape closes it.
- Footer: Dark, `space-4xl` top padding. Brand column (logo 240px, the company's one line, a small button), three link columns with mono titles, the rising strip of twelve red steps, then the legal line with the ondernemingsnummer.

## Badge and tag
- Badge: 24px tall, 8px padding, `radius-xs`, IBM Plex Mono 500 11px uppercase with 0.08em tracking. Variants default (`surface-sunken`), outline, solid (ink), accent (`red-500` with black text), and the four status badges with a 6px dot.
- Project categories: **Binnentrap**, **Buitentrap**, **Keldertrap**, **Kwarttrap**, **Bordestrap**, **Bekistingswerk**.
- Filter tags (`.rg-tag`): 40px pressable buttons with `aria-pressed`; pressed fills with `ink`. Optional live count in mono.

## The rest
- **Hero** (Dark photo, display statement, stair types), **CTABand** (Red, black type, phone), **ContactSection** (photo panel + quote form), **SectionHeader** (step-mark eyebrow), **ProcessSteps** (rising flight), **SpecList** (mono specs and dimension lines), **Accordion** (FAQ), **Tabs**, **Alert**, **Toast**, **Modal**, and the CMS set: **AdminShell**, **DataTable**, **MediaUploader**, **StatCard**.
