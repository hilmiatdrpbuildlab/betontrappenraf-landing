# SpecList

Maatvoering: the technical details of a stair as a ruled list of label and value, plus a dimension line in the style of a stair plan. This is where the site shows precision instead of claiming it.

## Use
- `dl.rg-specs` > `.rg-specs__row` > `dt` (label, `ink-soft`) + `dd` (value, mono, right-aligned, tabular numerals). The list opens with a 1px ink rule; rows are separated by `line`.
- `.rg-dim` draws a dimension line with end ticks in `highlight` and the value centred: `<div class="rg-dim"><span class="rg-dim__line"></span><span class="rg-dim__label">1,00 m</span><span class="rg-dim__line"></span></div>`. Add `.rg-dim--v` for a vertical one (floor height next to a photo). Give it an `aria-label` that reads the measurement in words.
- Use it on project detail pages and next to plans.

## Units and numbers
- The vocabulary of the trade: **Optrede** (rise), **Aantrede** (going), **Aantal treden**, **Verdiepingshoogte**, **Breedte**, **Kwartdraaiend**, **Halfdraaiend**, **Bordes**.
- Belgian notation: comma decimals, a space before the unit: **18,5 cm**, **2,78 m**. Centimetres for treads, metres for heights and widths.
- Only real measurements from Raf's plans. The preview's values are read off his plan photo and are examples.
