"""Build the Raf Geerts Betontrappen design system.

    python src/build.py            -> css/tokens.css, tailwind.config.js, guide/6-implementation.md, styleguide.html
    python src/build.py artifact   -> also dist/project/... for the shared Design System artifact
                                      (needs src/_asset_ids.json from the asset upload)

Sources: tokens.json, css/rg.css, css/sg.css, js/rg.js, README.md, guide/*.md,
components/<Name>/{preview.html,README.md}, components/_partials/*.html, assets/, fonts/.
"""
import html, json, re, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text(encoding="utf8"))
THEMES = [t["id"] for t in TOKENS["color"]["themes"]]

# Display order and groups for the style guide.
COMPONENTS = [
    ("Actions", ["Button"]),
    ("Navigation", ["Header", "Footer", "Tabs"]),
    ("Sections", ["Hero", "CTABand", "ContactSection"]),
    ("Content", ["SectionHeader", "ProjectCard", "ProcessSteps", "SpecList", "Card", "Badge", "Accordion"]),
    ("Forms", ["FormField", "ChoiceControls"]),
    ("Feedback", ["Alert", "Toast", "Modal"]),
    ("CMS", ["AdminShell", "DataTable", "MediaUploader", "StatCard"]),
]
FAMILIES = ("spacing", "radius", "layout", "timing")


# ---------------------------------------------------------------- tokens.css
def color_value(v):
    m = re.fullmatch(r"\{([A-Za-z0-9_.-]+)\}", v)
    return f"var(--{m.group(1)})" if m else v


def per_theme(families):
    blocks = {t: [] for t in THEMES}
    for fam in families:
        for tok in TOKENS.get(fam, {}).get("tokens", []):
            val = tok["value"]
            if isinstance(val, str):
                blocks[THEMES[0]].append(f"  --{tok['name']}: {color_value(val)};")
            else:
                for t in THEMES:
                    v = val.get(t, val.get(THEMES[0])) if t == THEMES[0] else val.get(t)
                    if v is not None:
                        blocks[t].append(f"  --{tok['name']}: {color_value(v)};")
    return blocks


def tokens_css(font_prefix="../"):
    blocks = per_theme(["color", "shadow"])
    out = ["/* GENERATED from tokens.json by src/build.py. Do not edit by hand. */", ""]
    for f in TOKENS["type"]["fonts"]:
        out.append(f"@font-face {{ font-family: \"{f['family']}\"; src: url(\"{font_prefix}{f['file']}\") format(\"woff2\"); "
                   f"font-weight: {f['weight']}; font-style: {f.get('style', 'normal')}; font-display: swap; }}")
    out.append("")
    out.append(f':root, [data-theme="{THEMES[0]}"] {{\n' + "\n".join(blocks[THEMES[0]]) + "\n}")
    for t in THEMES[1:]:
        out.append(f'[data-theme="{t}"] {{\n' + "\n".join(blocks[t]) + "\n}")
    rest = []
    for fam in FAMILIES:
        for tok in TOKENS.get(fam, {}).get("tokens", []):
            rest.append(f"  --{tok['name']}: {tok['value']};")
    for key, stack in TOKENS["type"]["families"].items():
        rest.append(f"  --font-{key}: {stack};")
    out.append(":root {\n" + "\n".join(rest) + "\n}")
    for g in TOKENS["type"]["groups"]:
        for s in g["styles"]:
            fam = s.get("family", g["family"])
            props = [f"font-family: var(--font-{fam})", f"font-size: {s['fontSize']}", f"line-height: {s['lineHeight']}", f"font-weight: {s['fontWeight']}"]
            if "letterSpacing" in s:
                props.append(f"letter-spacing: {s['letterSpacing']}")
            out.append(f".{s['name']} {{ " + "; ".join(props) + "; }")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- tailwind.config.js
def tailwind_config():
    col = {t["name"]: t for t in TOKENS["color"]["tokens"]}
    palette, semantic = {}, {}
    for name in col:
        if isinstance(col[name]["value"], str) and col[name]["value"].startswith("#"):
            m = re.fullmatch(r"([a-z]+)-(\d+)", name)
            if m:
                palette.setdefault(m.group(1), {})[m.group(2)] = f"var(--{name})"
            else:
                palette[name] = f"var(--{name})"
        else:
            semantic[name] = f"var(--{name})"
    colors = {"transparent": "transparent", "current": "currentColor", **palette, **semantic}
    font_size = {}
    for g in TOKENS["type"]["groups"]:
        for s in g["styles"]:
            opts = {"lineHeight": str(s["lineHeight"]), "fontWeight": str(s["fontWeight"])}
            if "letterSpacing" in s:
                opts["letterSpacing"] = s["letterSpacing"]
            font_size[s["name"].replace("t-", "")] = [s["fontSize"], opts]
    tok = lambda fam: {t["name"]: f"var(--{t['name']})" for t in TOKENS[fam]["tokens"]}
    spacing = {t["name"].replace("space-", ""): f"var(--{t['name']})" for t in TOKENS["spacing"]["tokens"]}
    radius = {t["name"].replace("radius-", ""): f"var(--{t['name']})" for t in TOKENS["radius"]["tokens"]}
    shadow = {t["name"].replace("shadow-", ""): f"var(--{t['name']})" for t in TOKENS["shadow"]["tokens"]}
    layout = {t["name"]: t["value"] for t in TOKENS["layout"]["tokens"]}
    cfg = {
        "content": ["./src/**/*.{html,js,ts,jsx,tsx,php,twig,blade.php}"],
        "darkMode": ["selector", '[data-theme="dark"]'],
        "theme": {
            "screens": {"sm": layout["bp-sm"], "md": layout["bp-md"], "lg": layout["bp-lg"], "xl": layout["bp-xl"]},
            "colors": colors,
            "fontFamily": {"sans": ["Archivo", "Arial Narrow", "Arial", "sans-serif"], "mono": ["IBM Plex Mono", "ui-monospace", "Menlo", "Consolas", "monospace"]},
            "fontSize": font_size,
            "spacing": {"0": "0px", "px": "1px", **spacing},
            "borderRadius": radius,
            "boxShadow": {"none": "none", **shadow},
            "extend": {
                "maxWidth": {"container": "var(--container-max)", "measure": "var(--measure)"},
                "height": {"header": "var(--header-height)", "control": "var(--control-height)", "topbar": "var(--cms-topbar)"},
                "width": {"sidebar": "var(--cms-sidebar)"},
                "transitionTimingFunction": {"out": "var(--ease-out)"},
                "transitionDuration": {"fast": "var(--dur-fast)", "base": "var(--dur-base)", "slow": "var(--dur-slow)"},
            },
        },
    }
    body = json.dumps(cfg, indent=2, ensure_ascii=False)
    body = re.sub(r'^(\s*)"([A-Za-z_][A-Za-z0-9_]*)":', r"\1\2:", body, flags=re.M)
    head = ("/** GENERATED from tokens.json by src/build.py. Do not edit by hand.\n"
            " *  Tailwind CSS v3 config for Raf Geerts Betontrappen. Every value points at a CSS variable from css/tokens.css,\n"
            " *  so load tokens.css first and the [data-theme] sections keep working: bg-surface, text-ink, bg-accent...\n"
            " *  Condensed headings: add the plugin rule below or use the .t-* classes from css/rg.css. */\n")
    plugin = ("\nconst plugin = require('tailwindcss/plugin');\nmodule.exports.plugins = [\n"
              "  plugin(({ addUtilities }) => addUtilities({\n"
              "    '.condensed': { fontVariationSettings: '\"wdth\" 75', textTransform: 'uppercase' },\n"
              "    '.semi-condensed': { fontVariationSettings: '\"wdth\" 85' },\n"
              "    '.tabular': { fontVariantNumeric: 'tabular-nums' },\n"
              "  })),\n];\n")
    return head + "module.exports = " + body + ";\n" + plugin


# ---------------------------------------------------------------- snippets
ICON_DIR = ROOT / "assets" / "icons"
FILLED_ICONS = {"facebook"}


def icon(name, extra=""):
    svg = (ICON_DIR / f"{name}.svg").read_text(encoding="utf8")
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
    head, rest = svg.split(">", 1)
    head = re.sub(r'\s(class|width|height|role|stroke-linecap|stroke-linejoin)="[^"]*"', "", head)
    cls = ("rg-icon " + extra).strip()
    attrs = f' class="{cls}" aria-hidden="true" focusable="false"'
    attrs += ' fill="currentColor"' if name in FILLED_ICONS else ' stroke-linecap="square" stroke-linejoin="miter"'
    svg = head.replace("<svg", "<svg" + attrs, 1) + ">" + rest
    return re.sub(r">\s+<", "><", re.sub(r"\s+", " ", svg)).strip()


def expand(text, asset_url):
    def partial(m):
        parts = m.group(1).split("|")
        body = (ROOT / "components" / "_partials" / f"{parts[0]}.html").read_text(encoding="utf8")
        for kv in sorted(parts[1:], key=lambda kv: -len(kv.split("=", 1)[0])):
            k, v = kv.split("=", 1)
            body = body.replace("$" + k, v)
        return body.strip()
    for _ in range(3):
        text = re.sub(r"\{\{partial:([^}]+)\}\}", partial, text)
    text = re.sub(r"\{\{icon:([a-z0-9-]+)(?:\|([^}]*))?\}\}", lambda m: icon(m.group(1), m.group(2) or ""), text)
    text = re.sub(r"\{\{img:([^}]+)\}\}", lambda m: asset_url("assets/" + m.group(1)), text)
    text = re.sub(r"\{\{logo:([^}]+)\}\}", lambda m: asset_url("assets/logo/" + m.group(1)), text)
    return text


def read_component(name):
    d = ROOT / "components" / name
    marker, body = (d / "preview.html").read_text(encoding="utf8").split("\n", 1)
    return marker, body, (d / "README.md").read_text(encoding="utf8")


# ---------------------------------------------------------------- tiny markdown
def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md(text, skip_h1=True):
    out, para, items, rows, code = [], [], [], [], None
    def flush():
        nonlocal para, items, rows
        if para: out.append("<p>" + md_inline(" ".join(para)) + "</p>"); para = []
        if items: out.append("<ul>" + "".join(f"<li>{md_inline(i)}</li>" for i in items) + "</ul>"); items = []
        if rows:
            head, *body = [r for r in rows if not re.fullmatch(r"\|?[\s:|-]+\|?", r)]
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            t = '<div class="sg-table"><table><thead><tr>' + "".join(f"<th>{md_inline(c)}</th>" for c in cells(head)) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in cells(r)) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>"); rows = []
    for line in text.splitlines():
        if code is not None:
            if line.startswith("```"):
                out.append('<pre class="sg-code"><code>' + html.escape("\n".join(code)) + "</code></pre>"); code = None
            else:
                code.append(line)
            continue
        if line.startswith("```"):
            flush(); code = []
        elif line.startswith("# "):
            flush()
            if not skip_h1: out.append(f"<h2 class=\"t-h2\">{md_inline(line[2:])}</h2>")
        elif line.startswith("### "):
            flush(); out.append(f"<h5>{md_inline(line[4:])}</h5>")
        elif line.startswith("## "):
            flush(); out.append(f"<h4>{md_inline(line[3:])}</h4>")
        elif line.startswith("- "):
            if para: flush()
            items.append(line[2:])
        elif line.startswith("|"):
            if para or items: flush()
            rows.append(line)
        elif not line.strip():
            flush()
        else:
            if items: flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


# ---------------------------------------------------------------- style guide page
def local_url(path):
    return path


def resolve(name, theme):
    tok = next(t for t in TOKENS["color"]["tokens"] if t["name"] == name)
    v = tok["value"] if isinstance(tok["value"], str) else tok["value"].get(theme, tok["value"].get(THEMES[0]))
    m = re.fullmatch(r"\{(.+)\}", v)
    return resolve(m.group(1), theme) if m else v


def lum(h):
    h = h.lstrip("#"); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def swatches():
    pal = [t for t in TOKENS["color"]["tokens"] if isinstance(t["value"], str) and t["value"].startswith("#")]
    cells = []
    for t in pal:
        v = t["value"]
        on = "#0e0f10" if contrast(v, "#0e0f10") >= contrast(v, "#ffffff") else "#ffffff"
        cells.append(f'<figure class="sg-swatch"><div class="sg-swatch__chip" style="background:{v};color:{on}"><span>{v.upper()}</span><span>{contrast(v, "#ffffff"):.1f} / {contrast(v, "#0e0f10"):.1f}</span></div>'
                     f'<figcaption><strong>{t["name"]}</strong><span>{md_inline(t["usage"].replace("Palette. ", ""))}</span></figcaption></figure>')
    return '<p class="sg-hint">Ratios: against white / against concrete-950.</p><div class="sg-swatches">' + "".join(cells) + "</div>"


def semantic_table():
    head = "".join(f"<th>{t['name']}</th>" for t in TOKENS["color"]["themes"])
    rows = []
    for t in TOKENS["color"]["tokens"]:
        if isinstance(t["value"], str) and t["value"].startswith("#"):
            continue
        cells = "".join(f'<td><div data-theme="{th}" class="sg-chipcell"><span class="sg-chip" style="background:var(--{t["name"]})"></span></div></td>' for th in THEMES)
        rows.append(f'<tr><td><code>{t["name"]}</code><div class="sg-usage">{md_inline(t["usage"])}</div></td>{cells}</tr>')
    return f'<div class="sg-table"><table class="sg-semantic"><thead><tr><th>Token</th>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def type_specimens():
    out = []
    for g in TOKENS["type"]["groups"]:
        for s in g["styles"]:
            spec = f'{s["fontSize"]} / {s["lineHeight"]} · {s["fontWeight"]}' + (f' · {s["letterSpacing"]}' if "letterSpacing" in s else "")
            fam = "IBM Plex Mono" if s.get("family", g["family"]) == "mono" else "Archivo"
            out.append(f'<div class="sg-type"><div class="sg-type__meta"><code>.{s["name"]}</code><span>{fam} · {spec}</span><span>{md_inline(s["usage"])}</span></div>'
                       f'<div class="sg-type__sample {s["name"]}">{html.escape(s["sample"])}</div></div>')
    return "".join(out)


def spacing_radius():
    sp = "".join(f'<div class="sg-space"><code>{t["name"]}</code><span class="sg-space__bar" style="width:{t["value"]}"></span><span>{t["value"]}</span><span class="sg-usage">{md_inline(t["usage"])}</span></div>' for t in TOKENS["spacing"]["tokens"])
    rd = "".join(f'<figure class="sg-radius"><div style="border-radius:var(--{t["name"]})"></div><figcaption><code>{t["name"]}</code> {t["value"]}<span class="sg-usage">{md_inline(t["usage"])}</span></figcaption></figure>' for t in TOKENS["radius"]["tokens"])
    sh = "".join(f'<figure class="sg-shadow"><div style="box-shadow:var(--{t["name"]})"></div><figcaption><code>{t["name"]}</code><span class="sg-usage">{md_inline(t["usage"])}</span></figcaption></figure>' for t in TOKENS["shadow"]["tokens"])
    lay = "".join(f'<tr><td><code>{t["name"]}</code></td><td>{t["value"]}</td><td>{md_inline(t["usage"])}</td></tr>' for t in TOKENS["layout"]["tokens"] + TOKENS["timing"]["tokens"])
    return sp, rd, sh, f'<div class="sg-table"><table><thead><tr><th>Token</th><th>Value</th><th>Use</th></tr></thead><tbody>{lay}</tbody></table></div>'


def icon_grid():
    names = sorted(p.stem for p in ICON_DIR.glob("*.svg"))
    return '<div class="sg-icons">' + "".join(f'<figure>{icon(n)}<figcaption>{n}</figcaption></figure>' for n in names) + "</div>"


def photo_grid(url=local_url):
    credits = json.loads((ROOT / "assets" / "photos" / "credits.json").read_text(encoding="utf8"))
    return '<div class="sg-photos">' + "".join(
        f'<figure class="sg-photo"><img src="{url(c["path"])}" alt="{html.escape(c["alt"])}" loading="lazy"><figcaption><strong>{c["path"].split("/")[-1]}</strong><span>{html.escape(c["alt"])}</span></figcaption></figure>'
        for c in credits) + "</div>"


LOGOS = [
    ("rg-logo.svg", "light", "Primary, on white and concrete-50. Black RAF GEERTS, red-500 BETONTRAPPEN."),
    ("rg-logo-on-dark.svg", "dark", "On the Dark theme and dark photos. White RAF GEERTS, red-500 BETONTRAPPEN."),
    ("rg-logo-on-red.svg", "red", "On the Red theme: black RAF GEERTS, white BETONTRAPPEN, as on Raf's van."),
    ("rg-logo-mono-black.svg", "white", "One colour, black: print, stamps, forms, fax."),
    ("rg-logo-mono-white.svg", "black", "One colour, white: workwear, signage on black, photo overlays."),
]


def logo_grid(url=local_url):
    grounds = {"light": "var(--concrete-50)", "dark": "var(--concrete-950)", "red": "var(--red-500)", "white": "var(--white)", "black": "var(--black)"}
    return '<div class="sg-logos">' + "".join(
        f'<figure><div class="sg-logo" style="background:{grounds[g]}"><img src="{url("assets/logo/" + f)}" alt="Raf Geerts Betontrappen logo, {f}"></div><figcaption><code>{f}</code><span>{d}</span></figcaption></figure>'
        for f, g, d in LOGOS) + "</div>"


def guide_sections():
    return sorted((ROOT / "guide").glob("*.md"))


def build_implementation_md():
    tpl = (ROOT / "src" / "implementation.template.md").read_text(encoding="utf8")
    out = tpl.replace("{{TOKENS_CSS}}", tokens_css("../").rstrip()).replace("{{TAILWIND}}", tailwind_config().rstrip())
    (ROOT / "guide" / "6-implementation.md").write_text(out, encoding="utf8")


def build_styleguide():
    sp, rd, sh, lay = spacing_radius()
    nav, comps = [], []
    for group, names in COMPONENTS:
        nav.append(f'<li class="sg-nav__group">{group}</li>')
        for n in names:
            marker, body, readme = read_component(n)
            sub = re.search(r'subtitle="([^"]*)"', marker)
            nav.append(f'<li><a href="#c-{n}">{n}</a></li>')
            comps.append(f'<section class="sg-comp" id="c-{n}"><div class="sg-comp__head"><span class="t-label">{group}</span><h3 class="t-h2">{n}</h3>'
                         f'<p class="sg-sub">{html.escape(sub.group(1)) if sub else ""}</p></div><div class="sg-comp__doc">{md(readme)}</div>'
                         f'<div class="sg-demo">{expand(body, local_url)}</div></section>')
    guide_nav, guide_html = [], []
    for i, p in enumerate(guide_sections()):
        text = p.read_text(encoding="utf8")
        title = re.search(r"^# (.+)$", text, re.M).group(1)
        gid = "g-" + p.stem
        guide_nav.append(f'<li><a href="#{gid}">{html.escape(title)}</a></li>')
        guide_html.append(f'<section class="sg-block" id="{gid}"><header><span class="rg-eyebrow"><span class="rg-step-mark"></span>Guide</span><h2 class="t-h1">{html.escape(title)}</h2></header><div class="sg-doc">{md(text)}</div></section>')
    page = expand((ROOT / "src" / "styleguide.template.html").read_text(encoding="utf8"), local_url)
    repl = {
        "{{GUIDE}}": md((ROOT / "README.md").read_text(encoding="utf8")), "{{SECTIONS}}": "".join(guide_html), "{{NAV_GUIDE}}": "".join(guide_nav),
        "{{SWATCHES}}": swatches(), "{{SEMANTIC}}": semantic_table(), "{{TYPE}}": type_specimens(),
        "{{SPACING}}": sp, "{{RADIUS}}": rd, "{{SHADOW}}": sh, "{{LAYOUT}}": lay, "{{ICONS}}": icon_grid(), "{{PHOTOS}}": photo_grid(),
        "{{LOGOS}}": logo_grid(), "{{NAV_COMPONENTS}}": "".join(nav), "{{COMPONENTS}}": "".join(comps),
    }
    for k, v in repl.items():
        page = page.replace(k, v)
    (ROOT / "styleguide.html").write_text(page, encoding="utf8")


# ---------------------------------------------------------------- artifact tree
def build_artifact():
    ids = json.loads((ROOT / "src" / "_asset_ids.json").read_text(encoding="utf8"))
    blob = lambda p: "/_blob/" + ids[p]["id"]
    dist = ROOT / "dist" / "project"
    if dist.exists():
        shutil.rmtree(dist)
    (dist / "components").mkdir(parents=True)
    (dist / "fonts").mkdir()
    (dist / "guide").mkdir()
    (dist / "code").mkdir()
    shutil.copy(ROOT / "tokens.json", dist / "tokens.json")
    for f in TOKENS["type"]["fonts"]:
        shutil.copy(ROOT / f["file"], dist / f["file"])
    for lic in ("OFL-Archivo.txt", "OFL-IBMPlexMono.txt"):
        shutil.copy(ROOT / "fonts" / lic, dist / "fonts" / lic)
    shutil.copy(ROOT / "README.md", dist / "README.md")
    for p in guide_sections():
        shutil.copy(p, dist / "guide" / p.name)
    shutil.copy(ROOT / "CREDITS.md", dist / "CREDITS.md")
    shutil.copy(ROOT / "tailwind.config.js", dist / "code" / "tailwind.config.js")
    (dist / "code" / "tokens.css").write_text(tokens_css("../"), encoding="utf8")
    css = (ROOT / "css" / "rg.css").read_text(encoding="utf8") + "\n" + (ROOT / "css" / "sg.css").read_text(encoding="utf8")
    assert "</style" not in css
    (dist / "components" / "bundle.css").write_text(css, encoding="utf8")
    js = (ROOT / "js" / "rg.js").read_text(encoding="utf8")
    assert "</script" not in js and "<!--" not in js
    names = [n for _, ns in COMPONENTS for n in ns]
    header = '/* @ds-bundle: ' + json.dumps({"format": 4, "namespace": "RG", "components": [{"name": n} for n in names]}) + ' */\n'
    (dist / "components" / "bundle.js").write_text(header + js, encoding="utf8")
    for n in names:
        marker, body, readme = read_component(n)
        d = dist / "components" / n
        d.mkdir()
        (d / "preview.html").write_text(marker + "\n" + expand(body, blob), encoding="utf8")
        (d / "README.md").write_text(readme, encoding="utf8")
    (dist / "components" / "Cover").mkdir()
    (dist / "components" / "Cover" / "preview.html").write_text(expand((ROOT / "components" / "Cover" / "preview.html").read_text(encoding="utf8"), blob), encoding="utf8")
    for g, folder in (("Logos", "logo"), ("Photos", "photos"), ("Icons", "icons")):
        src = ROOT / "assets" / folder / "README.md"
        (dist / "assets" / g).mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dist / "assets" / g / "README.md")
    print("artifact tree:", sum(1 for _ in dist.rglob("*") if _.is_file()), "files")


if __name__ == "__main__":
    (ROOT / "css" / "tokens.css").write_text(tokens_css("../"), encoding="utf8")
    (ROOT / "tailwind.config.js").write_text(tailwind_config(), encoding="utf8")
    build_implementation_md()
    build_styleguide()
    print("built css/tokens.css, tailwind.config.js, guide/6-implementation.md and styleguide.html")
    if len(sys.argv) > 1 and sys.argv[1] == "artifact":
        build_artifact()
