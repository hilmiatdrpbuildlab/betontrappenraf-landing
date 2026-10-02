# CMS

The CMS is where Raf publishes realisations, answers quote requests and manages photos and pages. It uses the same tokens and components as the website, tuned for work: denser, calmer, with full light and dark modes.

## Principles
- **Same brand, quieter.** The CMS keeps the concrete grounds, the black type and the red accent, but drops display type: page titles are `t-h3`, panel titles `t-h6`. Red marks the primary action, the active nav item and selected rows only.
- **Denser.** Inside `.rg-cms` controls are 40px and body text 14px. Tables pad cells 10×16px.
- **Status in words.** Every state is a badge with a dot and a word: **Gepubliceerd**, **Concept**, **Gepland**, **Offline**.
- **Nothing destructive without a question.** Deleting goes through a Modal with **Annuleren** focused; bulk actions repeat the count.
- **Photos need words.** A project cannot be published while a photo lacks alt text; the dashboard and the uploader both say how many are missing.

## Structure
- `AdminShell`: 264px sidebar (brand, nav, user) + top bar (search, light/dark toggle, notifications, **Bekijk website**) + content column.
- Navigation: **Dashboard**, **Realisaties**, **Aanvragen** (with a live count), **Media**, **Pagina's**, **Gebruikers**, **Instellingen**.
- Page pattern: breadcrumbs, `t-h3` title and the page's one primary action, then panels.

## Core screens
- **Dashboard**: StatCards (new requests, realisations online, photos missing alt text), latest requests table.
- **Realisaties**: DataTable with search, status filter, bulk publish and delete, sort on title and date, thumbnails, slugs.
- **Realisatie bewerken**: Tabs **Inhoud** (title, slug, type, status, description), **Foto's** (MediaUploader, cover photo, alt text per photo), **Maatvoering** (type of run, number of treads, rise, going, floor height in unit inputs), **SEO** (page title, description); a sticky bar with **Opslaan** and **Publiceren**.
- **Aanvragen**: Tabs **Nieuw**, **Beantwoord**, **Archief**; each request shows the quote form fields and any attached plans.

## Feedback
- Inline Alerts for page-level states (unsaved changes, missing alt text, failed save).
- Toasts bottom-right for completed actions, with **Ongedaan maken** where it is possible.
- Field errors at the field, never only in a toast.

## Modes
- Light and Dark follow `prefers-color-scheme` on first load; the top bar toggle overrides and is remembered per browser.
- Both modes pass the same contrast floors; check new colours with `src/check_contrast.py`.
