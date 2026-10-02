# ChoiceControls

Checkboxes, radios, switches and option tiles, all native inputs restyled: square checkboxes, round radios, a pill switch and tiles that draw each stair type as a profile.

## Use
- Checkbox and radio: `label.rg-check` > `input[type=checkbox|radio]` + text. Add `span.rg-check__hint` inside the text for a second line. Group them in `fieldset.rg-field` > `legend` + `.rg-choices`.
- Indeterminate (a "select all" with some rows chosen) is set from script: `input.indeterminate = true`.
- Switch: `label.rg-switch` > `input[type=checkbox][role=switch]` + text. CMS only, for settings that apply at once (**Toon op homepage**, **Uitgelicht**). In a form that is submitted, use a checkbox.
- Option tiles: `.rg-options` > `label.rg-option` > `input[type=radio]` + `svg.rg-option__shape` + `.rg-option__name` + `.rg-option__hint`. The selected tile gets a 2px `accent` border and a red profile. Use for the **Type trap** question of the quote form.
- The tile profiles are drawn from the step grid (8px treads): rechte trap, kwarttrap, bordestrap, buitentrap.
- Checked fills use `accent` with an `on-accent` mark, so all controls re-theme in Dark.

## Avoid
- A switch without a visible label.
- More than five option tiles; fall back to a select.
