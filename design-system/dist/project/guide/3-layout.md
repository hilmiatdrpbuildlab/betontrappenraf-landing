# Spacing and layout

## Base grid
A 4px base with an 8px rhythm. Every margin, padding and gap is a spacing token; component internals may use the 2px `space-3xs` for hairline offsets only.

## Spacing scale

| Token | Value | Typical use |
| --- | --- | --- |
| `space-3xs` | 2px | Hairline offsets |
| `space-2xs` | 4px | Icon to text in badges |
| `space-xs` | 8px | Eyebrow to title, label to input, icon to text in buttons |
| `space-sm` | 12px | Compact control gaps, table cell padding |
| `space-md` | 16px | Input padding, form field gaps, phone gutter |
| `space-lg` | 24px | Card padding, grid gutter, CMS content padding |
| `space-xl` | 32px | Large card padding, tablet margin |
| `space-2xl` | 48px | Section title to content, desktop margin |
| `space-3xl` | 64px | Blocks inside a section, section padding on phones |
| `space-4xl` | 96px | Section padding on tablets |
| `space-5xl` | 128px | Section padding on desktop |

## Containers and columns

| Range | Columns | Gutter | Page margin | Section padding |
| --- | --- | --- | --- | --- |
| Phone, under 720px | 4 | 16px | 16px (`space-md`) | 64px |
| Tablet, 720–1023px | 8 | 24px | 32px (`space-xl`) | 96px |
| Desktop, 1024px and up | 12 | 24px (`grid-gutter`) | 48px (`page-margin`) | 128px |
| Max width | 12 | 24px | 48px | 128px |

- `.rg-container` caps content at `container-max` (1280px) plus the page margins, so the widest layout is 1376px. Full-bleed photos and bands run edge to edge; their content sits in a container.
- `.rg-grid` gives the column grid; most sections use simpler splits built on it: 7/5 (feature project), 5/7 (contact, footer), 3 equal (project grid), 4 rising steps (Werkwijze).
- Breakpoints: `bp-sm` 640, `bp-md` 768, `bp-lg` 1024, `bp-xl` 1280. The header folds at 1024px, project grids at 980px and 760px, forms at 640px.
- The CMS is a 264px sidebar plus a fluid content column with 24px padding; it collapses through a container query when narrower than 760px.

## Shape and depth
- Radius: `radius-none` for photos, hero, bands and project cards; `radius-xs` (2px) for buttons, inputs, badges, tabs; `radius-sm` (4px) for cards, panels, toasts, modals; `radius-full` only for avatars, status dots and the switch.
- Elevation goes border first: a 1px `line` outline for cards; `shadow-sm` on hover; `shadow-md` for dropdowns and a form card over a photo; `shadow-lg` for modals and toasts. Dark sections use the darker Dark shadow values automatically.
