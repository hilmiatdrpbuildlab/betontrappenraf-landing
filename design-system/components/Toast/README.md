# Toast

Brief confirmations after an action in the CMS, on the inverse surface so they stand apart from every panel: what happened, an optional undo and a close button.

## Use
- A fixed `.rg-toasts` stack bottom-right (bottom-centre on phones) with `aria-live="polite"` > `.rg-toast` (`--success`, `--danger`, `--info` or plain) > icon + `p.rg-toast__text` + `.rg-toast__actions` (optional `button.rg-toast__action`, `button.rg-toast__close[data-rg-dismiss]`).
- `role="status"` for confirmations, `role="alert"` for failures.
- Success and info toasts close themselves after 6 seconds unless they hold an action; failures and anything with **Ongedaan maken** stay until closed. Pause the timer on hover and focus.
- Status icon colours flip with the theme (`teal-300` on the dark toast in Light, `teal-700` on the light toast in Dark), so they keep 3:1.
- Text: a bold verdict and one short sentence. **Opgeslagen.**, **Niet verstuurd.**

## Avoid
- Toasts for errors the user must fix in a form; show those at the field.
- More than three at once.
