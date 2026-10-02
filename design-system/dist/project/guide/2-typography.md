# Typography

## Families
- **Archivo** (Omnibus-Type, SIL OFL, free on Google Fonts), self-hosted as one variable file with a weight axis (100–900) and a width axis (62–125%). A grotesque with the sturdy, engineered feel of signage and technical documents. Titles use it condensed: `font-variation-settings: "wdth" 75`; buttons and nav at 85%; text at 100%.
- **IBM Plex Mono** (SIL OFL) at 400, 500 and 600 for eyebrows, labels, table headers, dates and every measurement. It reads like the numbers on a construction drawing.
- Fallbacks: `"Arial Narrow", Arial, sans-serif` and `ui-monospace, Menlo, Consolas, monospace`. Both families are in `fonts/`; load them with `font-display: swap`.
- The logo's rounded heavy lettering is artwork. Never imitate it in text.

## Scale
Desktop sizes; the four display styles and the lead step down under 720px.

| Style | Size / line height | Weight | Tracking | Case, width | Phone | Use |
| --- | --- | --- | --- | --- | --- | --- |
| `t-display` | 128 / 0.88 | 800 | −0.01em | Upper, 75% | 56 | Hero statement, once per page |
| `t-h1` | 80 / 0.92 | 800 | −0.005em | Upper, 75% | 44 | Section titles |
| `t-h2` | 56 / 0.95 | 800 | 0 | Upper, 75% | 34 | Sub-sections, CTA band |
| `t-h3` | 36 / 1.0 | 700 | 0 | Upper, 80% | 26 | Card and step titles, CMS page titles |
| `t-h4` | 24 / 1.25 | 650 | −0.01em | Sentence | 24 | Project titles, modal titles |
| `t-h5` | 20 / 1.3 | 650 | −0.005em | Sentence | 20 | FAQ questions, panel titles |
| `t-h6` | 16 / 1.4 | 700 | 0 | Sentence | 16 | Footer columns, form groups |
| `t-lead` | 20 / 1.5 | 400 | 0 | Sentence | 18 | Intro paragraphs in `ink-soft` |
| `t-body` | 16 / 1.6 | 400 | 0 | Sentence | 16 | Running text |
| `t-body-strong` | 16 / 1.6 | 600 | 0 | Sentence | 16 | Emphasis, key values |
| `t-small` | 14 / 1.5 | 400 | 0 | Sentence | 14 | Descriptions, hints, CMS tables |
| `t-caption` | 12 / 1.4 | 400 | 0 | Sentence | 12 | Captions, legal lines |
| `t-button` | 15 / 1 | 700 | 0.04em | Upper, 85% | 15 | Buttons (13 small, 16 large), tabs, nav |
| `t-label` | 12 / 1.3 mono | 500 | 0.1em | Upper | 12 | Eyebrows, badges, table headers |
| `t-measure` | 13 / 1.2 mono | 500 | 0.02em | As written | 13 | Dimensions and specs |
| `t-stat` | 56 / 0.9 | 800 | 0 | 75% | 44 | CMS dashboard counts |

## Rules
- Weights in use: 400, 600/650, 700, 800. No italics; emphasis is weight.
- Titles get `text-wrap: balance`, leads `text-wrap: pretty`. Running text stays within `measure` (66ch).
- Numbers that line up (specs, tables, phone numbers, stats) use tabular numerals; the `.t-measure` and `.t-stat` classes set them.
- Write headings in sentence case; uppercase comes from CSS. Never type all caps in content.
- One `.rg-accent-word` (red) per title at most, and only in 24px+ titles.
