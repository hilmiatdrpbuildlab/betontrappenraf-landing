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
/* GENERATED from tokens.json by src/build.py. Do not edit by hand. */

@font-face { font-family: "Archivo"; src: url("../fonts/Archivo-Variable.woff2") format("woff2"); font-weight: 100 900; font-style: normal; font-display: swap; }
@font-face { font-family: "IBM Plex Mono"; src: url("../fonts/IBMPlexMono-400.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }
@font-face { font-family: "IBM Plex Mono"; src: url("../fonts/IBMPlexMono-500.woff2") format("woff2"); font-weight: 500; font-style: normal; font-display: swap; }
@font-face { font-family: "IBM Plex Mono"; src: url("../fonts/IBMPlexMono-600.woff2") format("woff2"); font-weight: 600; font-style: normal; font-display: swap; }

:root, [data-theme="light"] {
  --red-300: #ff7a85;
  --red-400: #f0606c;
  --red-500: #e83e4d;
  --red-600: #cc2b3b;
  --red-700: #b5202f;
  --red-800: #a11b29;
  --white: #ffffff;
  --concrete-50: #f4f5f5;
  --concrete-100: #e9ebec;
  --concrete-200: #d6d9db;
  --concrete-300: #b8bcbf;
  --concrete-400: #8a8f94;
  --concrete-500: #63686d;
  --concrete-600: #4a4f54;
  --concrete-700: #33373b;
  --concrete-800: #232628;
  --concrete-900: #1a1c1e;
  --concrete-950: #0e0f10;
  --black: #000000;
  --teal-700: #0b6b5a;
  --teal-300: #4fd1b5;
  --teal-50: #e0f3ef;
  --amber-700: #9a5200;
  --amber-300: #f2b544;
  --amber-50: #fbefd9;
  --brick-700: #a8201a;
  --brick-300: #ff8e86;
  --brick-50: #fbe5e3;
  --blue-700: #1b4f91;
  --blue-300: #7fb2f0;
  --blue-50: #e3ecf7;
  --bg: var(--concrete-50);
  --surface: var(--white);
  --surface-sunken: var(--concrete-100);
  --surface-inverse: var(--concrete-950);
  --ink: var(--concrete-950);
  --ink-soft: var(--concrete-600);
  --ink-faint: var(--concrete-500);
  --ink-inverse: var(--concrete-50);
  --line: var(--concrete-200);
  --line-strong: var(--concrete-500);
  --accent: var(--red-600);
  --accent-hover: var(--red-700);
  --accent-press: var(--red-800);
  --on-accent: var(--white);
  --link: var(--red-700);
  --highlight: var(--red-500);
  --focus: var(--concrete-950);
  --success: var(--teal-700);
  --success-bg: var(--teal-50);
  --warning: var(--amber-700);
  --warning-bg: var(--amber-50);
  --danger: var(--brick-700);
  --danger-bg: var(--brick-50);
  --info: var(--blue-700);
  --info-bg: var(--blue-50);
  --scrim: rgba(14, 15, 16, 0.55);
  --overlay: rgba(14, 15, 16, 0.64);
  --shadow-sm: 0 1px 2px rgba(14, 15, 16, 0.08);
  --shadow-md: 0 2px 4px rgba(14, 15, 16, 0.06), 0 8px 24px rgba(14, 15, 16, 0.08);
  --shadow-lg: 0 16px 48px rgba(14, 15, 16, 0.22);
}
[data-theme="dark"] {
  --bg: var(--concrete-950);
  --surface: var(--concrete-900);
  --surface-sunken: var(--concrete-800);
  --surface-inverse: var(--concrete-50);
  --ink: var(--concrete-50);
  --ink-soft: var(--concrete-300);
  --ink-faint: #9a9fa4;
  --ink-inverse: var(--concrete-950);
  --line: rgba(244, 245, 245, 0.14);
  --line-strong: #7c8186;
  --accent: var(--red-500);
  --accent-hover: var(--red-400);
  --accent-press: var(--red-300);
  --on-accent: var(--black);
  --link: var(--red-400);
  --highlight: var(--red-500);
  --focus: var(--white);
  --success: var(--teal-300);
  --success-bg: #1f3532;
  --warning: var(--amber-300);
  --warning-bg: #383123;
  --danger: var(--brick-300);
  --danger-bg: #3a2c2d;
  --info: var(--blue-300);
  --info-bg: #28313b;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.5);
  --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.4), 0 8px 24px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.7);
}
[data-theme="red"] {
  --bg: var(--red-500);
  --surface: var(--red-500);
  --surface-sunken: var(--red-500);
  --surface-inverse: var(--black);
  --ink: var(--black);
  --ink-soft: #2b0a0e;
  --ink-faint: #2b0a0e;
  --ink-inverse: var(--white);
  --line: rgba(0, 0, 0, 0.22);
  --line-strong: var(--black);
  --accent: var(--black);
  --accent-hover: var(--concrete-700);
  --accent-press: var(--concrete-800);
  --on-accent: var(--white);
  --link: var(--black);
  --highlight: var(--black);
  --focus: var(--black);
}
:root {
  --space-3xs: 2px;
  --space-2xs: 4px;
  --space-xs: 8px;
  --space-sm: 12px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
  --space-4xl: 96px;
  --space-5xl: 128px;
  --radius-none: 0px;
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-full: 999px;
  --container-max: 1280px;
  --measure: 66ch;
  --grid-gutter: 24px;
  --page-margin: 48px;
  --header-height: 80px;
  --cms-sidebar: 264px;
  --cms-topbar: 64px;
  --control-height: 48px;
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
  --ease-out: cubic-bezier(0.2, 0, 0, 1);
  --dur-fast: 120ms;
  --dur-base: 200ms;
  --dur-slow: 320ms;
  --font-sans: "Archivo", "Arial Narrow", Arial, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
}
.t-display { font-family: var(--font-sans); font-size: 128px; line-height: 0.88; font-weight: 800; letter-spacing: -0.01em; }
.t-h1 { font-family: var(--font-sans); font-size: 80px; line-height: 0.92; font-weight: 800; letter-spacing: -0.005em; }
.t-h2 { font-family: var(--font-sans); font-size: 56px; line-height: 0.95; font-weight: 800; }
.t-h3 { font-family: var(--font-sans); font-size: 36px; line-height: 1; font-weight: 700; }
.t-h4 { font-family: var(--font-sans); font-size: 24px; line-height: 1.25; font-weight: 650; letter-spacing: -0.01em; }
.t-h5 { font-family: var(--font-sans); font-size: 20px; line-height: 1.3; font-weight: 650; letter-spacing: -0.005em; }
.t-h6 { font-family: var(--font-sans); font-size: 16px; line-height: 1.4; font-weight: 700; }
.t-lead { font-family: var(--font-sans); font-size: 20px; line-height: 1.5; font-weight: 400; }
.t-body { font-family: var(--font-sans); font-size: 16px; line-height: 1.6; font-weight: 400; }
.t-body-strong { font-family: var(--font-sans); font-size: 16px; line-height: 1.6; font-weight: 600; }
.t-small { font-family: var(--font-sans); font-size: 14px; line-height: 1.5; font-weight: 400; }
.t-caption { font-family: var(--font-sans); font-size: 12px; line-height: 1.4; font-weight: 400; }
.t-button { font-family: var(--font-sans); font-size: 15px; line-height: 1; font-weight: 700; letter-spacing: 0.04em; }
.t-label { font-family: var(--font-mono); font-size: 12px; line-height: 1.3; font-weight: 500; letter-spacing: 0.1em; }
.t-measure { font-family: var(--font-mono); font-size: 13px; line-height: 1.2; font-weight: 500; letter-spacing: 0.02em; }
.t-stat { font-family: var(--font-sans); font-size: 56px; line-height: 0.9; font-weight: 800; }
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
/** GENERATED from tokens.json by src/build.py. Do not edit by hand.
 *  Tailwind CSS v3 config for Raf Geerts Betontrappen. Every value points at a CSS variable from css/tokens.css,
 *  so load tokens.css first and the [data-theme] sections keep working: bg-surface, text-ink, bg-accent...
 *  Condensed headings: add the plugin rule below or use the .t-* classes from css/rg.css. */
module.exports = {
  content: [
    "./src/**/*.{html,js,ts,jsx,tsx,php,twig,blade.php}"
  ],
  darkMode: [
    "selector",
    "[data-theme=\"dark\"]"
  ],
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px"
    },
    colors: {
      transparent: "transparent",
      current: "currentColor",
      red: {
        "300": "var(--red-300)",
        "400": "var(--red-400)",
        "500": "var(--red-500)",
        "600": "var(--red-600)",
        "700": "var(--red-700)",
        "800": "var(--red-800)"
      },
      white: "var(--white)",
      concrete: {
        "50": "var(--concrete-50)",
        "100": "var(--concrete-100)",
        "200": "var(--concrete-200)",
        "300": "var(--concrete-300)",
        "400": "var(--concrete-400)",
        "500": "var(--concrete-500)",
        "600": "var(--concrete-600)",
        "700": "var(--concrete-700)",
        "800": "var(--concrete-800)",
        "900": "var(--concrete-900)",
        "950": "var(--concrete-950)"
      },
      black: "var(--black)",
      teal: {
        "700": "var(--teal-700)",
        "300": "var(--teal-300)",
        "50": "var(--teal-50)"
      },
      amber: {
        "700": "var(--amber-700)",
        "300": "var(--amber-300)",
        "50": "var(--amber-50)"
      },
      brick: {
        "700": "var(--brick-700)",
        "300": "var(--brick-300)",
        "50": "var(--brick-50)"
      },
      blue: {
        "700": "var(--blue-700)",
        "300": "var(--blue-300)",
        "50": "var(--blue-50)"
      },
      bg: "var(--bg)",
      surface: "var(--surface)",
      "surface-sunken": "var(--surface-sunken)",
      "surface-inverse": "var(--surface-inverse)",
      ink: "var(--ink)",
      "ink-soft": "var(--ink-soft)",
      "ink-faint": "var(--ink-faint)",
      "ink-inverse": "var(--ink-inverse)",
      line: "var(--line)",
      "line-strong": "var(--line-strong)",
      accent: "var(--accent)",
      "accent-hover": "var(--accent-hover)",
      "accent-press": "var(--accent-press)",
      "on-accent": "var(--on-accent)",
      link: "var(--link)",
      highlight: "var(--highlight)",
      focus: "var(--focus)",
      success: "var(--success)",
      "success-bg": "var(--success-bg)",
      warning: "var(--warning)",
      "warning-bg": "var(--warning-bg)",
      danger: "var(--danger)",
      "danger-bg": "var(--danger-bg)",
      info: "var(--info)",
      "info-bg": "var(--info-bg)",
      scrim: "var(--scrim)",
      overlay: "var(--overlay)"
    },
    fontFamily: {
      sans: [
        "Archivo",
        "Arial Narrow",
        "Arial",
        "sans-serif"
      ],
      mono: [
        "IBM Plex Mono",
        "ui-monospace",
        "Menlo",
        "Consolas",
        "monospace"
      ]
    },
    fontSize: {
      display: [
        "128px",
        {
          lineHeight: "0.88",
          fontWeight: "800",
          letterSpacing: "-0.01em"
        }
      ],
      h1: [
        "80px",
        {
          lineHeight: "0.92",
          fontWeight: "800",
          letterSpacing: "-0.005em"
        }
      ],
      h2: [
        "56px",
        {
          lineHeight: "0.95",
          fontWeight: "800"
        }
      ],
      h3: [
        "36px",
        {
          lineHeight: "1",
          fontWeight: "700"
        }
      ],
      h4: [
        "24px",
        {
          lineHeight: "1.25",
          fontWeight: "650",
          letterSpacing: "-0.01em"
        }
      ],
      h5: [
        "20px",
        {
          lineHeight: "1.3",
          fontWeight: "650",
          letterSpacing: "-0.005em"
        }
      ],
      h6: [
        "16px",
        {
          lineHeight: "1.4",
          fontWeight: "700"
        }
      ],
      lead: [
        "20px",
        {
          lineHeight: "1.5",
          fontWeight: "400"
        }
      ],
      body: [
        "16px",
        {
          lineHeight: "1.6",
          fontWeight: "400"
        }
      ],
      "body-strong": [
        "16px",
        {
          lineHeight: "1.6",
          fontWeight: "600"
        }
      ],
      small: [
        "14px",
        {
          lineHeight: "1.5",
          fontWeight: "400"
        }
      ],
      caption: [
        "12px",
        {
          lineHeight: "1.4",
          fontWeight: "400"
        }
      ],
      button: [
        "15px",
        {
          lineHeight: "1",
          fontWeight: "700",
          letterSpacing: "0.04em"
        }
      ],
      label: [
        "12px",
        {
          lineHeight: "1.3",
          fontWeight: "500",
          letterSpacing: "0.1em"
        }
      ],
      measure: [
        "13px",
        {
          lineHeight: "1.2",
          fontWeight: "500",
          letterSpacing: "0.02em"
        }
      ],
      stat: [
        "56px",
        {
          lineHeight: "0.9",
          fontWeight: "800"
        }
      ]
    },
    spacing: {
      "0": "0px",
      px: "1px",
      "3xs": "var(--space-3xs)",
      "2xs": "var(--space-2xs)",
      xs: "var(--space-xs)",
      sm: "var(--space-sm)",
      md: "var(--space-md)",
      lg: "var(--space-lg)",
      xl: "var(--space-xl)",
      "2xl": "var(--space-2xl)",
      "3xl": "var(--space-3xl)",
      "4xl": "var(--space-4xl)",
      "5xl": "var(--space-5xl)"
    },
    borderRadius: {
      none: "var(--radius-none)",
      xs: "var(--radius-xs)",
      sm: "var(--radius-sm)",
      full: "var(--radius-full)"
    },
    boxShadow: {
      none: "none",
      sm: "var(--shadow-sm)",
      md: "var(--shadow-md)",
      lg: "var(--shadow-lg)"
    },
    extend: {
      maxWidth: {
        container: "var(--container-max)",
        measure: "var(--measure)"
      },
      height: {
        header: "var(--header-height)",
        control: "var(--control-height)",
        topbar: "var(--cms-topbar)"
      },
      width: {
        sidebar: "var(--cms-sidebar)"
      },
      transitionTimingFunction: {
        out: "var(--ease-out)"
      },
      transitionDuration: {
        fast: "var(--dur-fast)",
        base: "var(--dur-base)",
        slow: "var(--dur-slow)"
      }
    }
  }
};

const plugin = require('tailwindcss/plugin');
module.exports.plugins = [
  plugin(({ addUtilities }) => addUtilities({
    '.condensed': { fontVariationSettings: '"wdth" 75', textTransform: 'uppercase' },
    '.semi-condensed': { fontVariationSettings: '"wdth" 85' },
    '.tabular': { fontVariantNumeric: 'tabular-nums' },
  })),
];
```

Example, the primary button in Tailwind:

```html
<a href="/offerte" class="inline-flex items-center gap-xs h-control px-[22px] rounded-xs bg-accent text-on-accent hover:bg-accent-hover active:bg-accent-press active:translate-y-px text-button semi-condensed uppercase transition-colors duration-fast ease-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-focus">
  Offerte aanvragen
</a>
```
