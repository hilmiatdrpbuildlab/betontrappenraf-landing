# Button

Square-cut action buttons in condensed uppercase: one red primary per view, an ink secondary, outline and ghost for the rest, and a danger button for deletes in the CMS.

## Use
- `a.rg-btn` for navigation, `button.rg-btn` for actions. Add `{{icon:arrow-right}}` with class `rg-btn__arrow` after the label when the button leads somewhere; the arrow slides 4px right on hover.
- Variants: default (primary, `accent`), `.rg-btn--secondary` (ink fill), `.rg-btn--outline`, `.rg-btn--ghost`, `.rg-btn--danger` (CMS only: deleting a project, a photo, a request).
- Sizes: `.rg-btn--sm` (40px, header and table toolbars), default (48px), `.rg-btn--lg` (56px, hero and the quote form submit). In the CMS the default is 40px.
- `.rg-btn--icon` makes a square icon-only button; it needs an `aria-label` in Dutch (**Bewerken**, **Verwijderen**).
- `.rg-btn--block` fills its container (mobile menu, narrow forms).
- `.rg-textlink` for tertiary links: uppercase with a red underline that turns ink on hover.

## States
- Hover: `accent-hover`. Pressed: `accent-press` and a 1px drop. Focus: 2px `focus` ring at 2px offset. Disabled: `disabled` attribute (or `aria-disabled="true"` on a link), 40% opacity, no pointer.
- Loading: add `.is-loading` and `aria-busy="true"`, put `{{icon:loader-circle}}` with class `rg-spin` before the label and wrap the label in `.rg-btn__label`. Keep the width; never swap the label for a spinner alone.

## Copy
Dutch, two or three words, saying what happens: **Offerte aanvragen**, **Bekijk realisaties**, **Contacteer ons**, **Aanvraag versturen**, **Opslaan**, **Publiceren**. Write the source in sentence case; CSS sets the capitals.

## Avoid
- Two primaries side by side. Pair the primary with an outline or a text link.
- White text on `red-500`: 4.0:1. The Light primary is `red-600` for that reason; on Dark, red buttons carry black text.
- Rounding the corners past `radius-xs`.
