# Modal

A confirm dialog on the native `dialog` element, used in the CMS before anything is deleted or taken offline.

## Use
- `dialog.rg-modal` with `aria-labelledby` > `.rg-modal__head` (`.rg-modal__icon` + a close button) + `.rg-modal__body` (`h2.t-h4` question, one paragraph naming exactly what will be lost) + `.rg-modal__foot` (ghost **Annuleren**, then the action).
- Open it with a button carrying `data-rg-open="<dialog id>"`; buttons with `data-rg-close` close it and pass their `value` as the dialog's `returnValue`. `showModal()` traps focus, Escape cancels, and focus returns to the opener.
- Put `autofocus` on **Annuleren**, so Enter never deletes by accident.
- The backdrop is `overlay`. Width 480px at most.
- `.rg-modal--inline` renders it in place for documentation only.

## Copy
Ask a question, name the item and the consequence: **Realisatie verwijderen?** "'Keldertrap in de ruwbouw' en de 6 foto's verdwijnen van de website. Dit kan niet ongedaan worden." The action button repeats the verb: **Verwijderen**, never **OK** or **Ja**.
