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
