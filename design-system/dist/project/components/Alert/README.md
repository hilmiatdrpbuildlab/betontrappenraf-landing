# Alert

Inline messages that stay in the page: a tinted panel with a status icon, a short title and one sentence on what happened or what to do.

## Use
- `.rg-alert` (info) or `--success`, `--warning`, `--danger` > the status icon + a `div` with `p.rg-alert__title` and optional `p.rg-alert__text` + an optional `button.rg-alert__close[data-rg-dismiss]` with `aria-label="Melding sluiten"`.
- Icons are fixed: `info`, `circle-check`, `triangle-alert`, `circle-x`. The icon and the title carry the meaning; the tint only supports it, so the message survives colour blindness and greyscale.
- `role="status"` for info, success and warning; `role="alert"` for errors that block the task.
- Errors say what went wrong and how to fix it, without apologising: "De verbinding viel weg. Uw wijzigingen staan nog in het formulier; probeer opnieuw."
- Transient confirmations after an action belong in a Toast, not an Alert.

## Avoid
- The brand `accent` for errors, or `danger` for decoration.
- A coloured side stripe instead of a full tint.
