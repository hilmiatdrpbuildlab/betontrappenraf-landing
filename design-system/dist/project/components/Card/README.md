# Card

The generic container: a `surface` panel with a hairline border and `radius-sm` corners, for text blocks, form cards, CMS panels and anything that needs its own edge.

## Use
- `.rg-card` > optional `.rg-card__head`, content, optional `.rg-card__foot` (a hairline then a row). Padding is `space-lg`; `.rg-card--lg` uses `space-xl` for form cards.
- `--raised`: no border, `shadow-md`. Only for a card laid over a photo or a sticky panel.
- `--sunken`: `surface-sunken` fill and no border, for spec groups and read-only data.
- `--interactive`: the whole card is one link. Put `a.rg-card__link` on the title; its `::after` covers the card. Hover darkens the border to `line-strong` and adds `shadow-sm`.
- Elevation order: border (default), then `shadow-sm` (hover), `shadow-md` (raised, dropdowns), `shadow-lg` (modals, toasts). Never stack two.

## Avoid
- Cards inside cards. Use a sunken card or a hairline instead.
- A coloured stripe down one side of a card.
- Cards in Red sections: Red holds a title, a line and buttons only.
