# ContactSection

The contact block: Raf's phone, e-mail, address and Facebook on a Dark photo panel, beside the quote request form. The form asks only what Raf needs to price a stair.

## Use
- `.rg-contact` > `.rg-contact__info[data-theme="dark"]` (a decorative `img` with `alt=""`, the title, `.rg-contact__rows` of `.rg-contact__row`) + a wrapper holding `form.rg-contact__form[data-rg-form]` and its `.rg-success[data-rg-success][hidden]`.
- The phone comes first: it is how most clients reach Raf. All rows link (`tel:`, `mailto:`, Facebook) except the address.
- Form fields, in this order: **Naam***, **Telefoon***, **E-mail***, **Gemeente van de werf**, **Type trap** (option tiles), **Verdiepingshoogte** (cm), **Plannen of foto's** (PDF or images), **Uw vraag**, the privacy consent*.
- `js/rg.js` validates on submit, shows each error under its field, focuses the first one, sets the button to loading and then swaps in the success panel. Replace that swap with the real endpoint; the form never claims a message was sent until the server says so.
- Under 960px the panel stacks above the form.

## Copy
- Success: **Bedankt voor uw aanvraag**, then what happens next and the phone number for anything urgent.
- No promised response time unless Raf commits to one.
