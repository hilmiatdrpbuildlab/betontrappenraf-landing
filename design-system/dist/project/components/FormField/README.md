# FormField

Labelled text inputs, unit inputs, selects and textareas with hints, errors and success messages. Square, 48px tall, with a `line-strong` border that passes 3:1 on every ground.

## Use
- `.rg-field` > `label[for]` + the control + optional `p.rg-field__hint`, `p.rg-field__error` or `p.rg-field__ok`, linked with `aria-describedby`.
- Controls: `input.rg-input`; `.rg-select-wrap` > `select.rg-select` + the `chevron-down` icon; `textarea.rg-textarea`; `.rg-input-wrap` > a leading icon + input (search); `.rg-input-group` > input + `span.rg-input-group__unit` for measurements (**cm**, **m**). Unit inputs switch to mono numerals.
- Required: `required` on the control and `span.rg-field__req` (`*`, `aria-hidden`) in the label. Optional fields say **(optioneel)** in `.rg-field__opt`. Mark whichever is rarer.
- States: hover darkens the border to ink; focus adds the 2px `focus` ring; `.rg-field--error` + `aria-invalid="true"` turns the border `danger` (2px) and shows the error; `.rg-field--success` shows the `ok` line; `disabled` sinks the fill; `readonly` sinks it with a dashed border.
- Lay fields out in `.rg-form`: two columns, one under 640px; `.rg-field--full` spans both.
- `js/rg.js` validates `[data-rg-form]` on submit, focuses the first wrong field and clears an error as soon as the value is valid.

## Copy
- Labels above the field, short nouns: **Naam**, **E-mail**, **Telefoon**, **Gemeente van de werf**, **Verdiepingshoogte**.
- Placeholders give an example, never the label.
- Errors say how to fix it: "Vul een geldig e-mailadres in, bijvoorbeeld naam@voorbeeld.be."
