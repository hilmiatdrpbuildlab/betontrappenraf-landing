# CSS and Tailwind

Both are generated from `tokens.json` by `python src/build.py`, so they never drift from the tokens. Use one of them, not both side by side with different values.

## CSS variables
`css/tokens.css` (in this system also `code/tokens.css`) holds the font faces, every token as a custom property on `:root`, the theme overrides for `[data-theme="dark"]` and `[data-theme="red"]`, and one class per type style. Load it first, then `css/rg.css` for the components.

```html
<link rel="preload" href="/fonts/Archivo-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/tokens.css">
<link rel="stylesheet" href="/css/rg.css">
<script src="/js/rg.js" defer></script>
<body class="rg">
  <section data-theme="dark">…</section>
</body>
```

```css
{{TOKENS_CSS}}
```

Condensed titles are set by `css/rg.css`, because the width axis is not part of the token grammar:

```css
.t-display, .t-h1, .t-h2 { text-transform: uppercase; font-variation-settings: "wdth" 75; }
.t-h3 { text-transform: uppercase; font-variation-settings: "wdth" 80; }
.t-button { text-transform: uppercase; font-variation-settings: "wdth" 85; }
```

## Tailwind CSS
`tailwind.config.js` (in this system `code/tailwind.config.js`) maps every token to its CSS variable, so the themes keep working: `bg-surface text-ink`, `bg-accent text-on-accent hover:bg-accent-hover`, `border-line-strong`, `text-ink-soft`, `p-lg gap-md`, `rounded-xs`, `shadow-md`, `text-h1 condensed`, `font-mono text-measure tabular`. Load `tokens.css` before the Tailwind output. For Tailwind v4, load it with `@config "./tailwind.config.js";`.

```js
{{TAILWIND}}
```

Example, the primary button in Tailwind:

```html
<a href="/offerte" class="inline-flex items-center gap-xs h-control px-[22px] rounded-xs bg-accent text-on-accent hover:bg-accent-hover active:bg-accent-press active:translate-y-px text-button semi-condensed uppercase transition-colors duration-fast ease-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus">
  Offerte aanvragen
</a>
```
