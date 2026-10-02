"""Write the five logo SVGs from the traced paths in src/_logo_paths.json.
The paths are a potrace trace of the client's own Logo.png (betontrappenraf.be)."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d = json.loads((ROOT / "src" / "_logo_paths.json").read_text())
nums = [float(x) for x in re.findall(r"-?\d+\.?\d*", d["black"] + d["red"])]
xs, ys = nums[0::2], nums[1::2]
x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
vb = f"{x0:.1f} {y0:.1f} {x1 - x0:.1f} {y1 - y0:.1f}"
VARIANTS = {
    "rg-logo":            ("#000000", "#E83E4D"),
    "rg-logo-on-dark":    ("#FFFFFF", "#E83E4D"),
    "rg-logo-on-red":     ("#000000", "#FFFFFF"),
    "rg-logo-mono-black": ("#000000", "#000000"),
    "rg-logo-mono-white": ("#FFFFFF", "#FFFFFF"),
}
for name, (top, bottom) in VARIANTS.items():
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="Raf Geerts Betontrappen">'
           f'<title>Raf Geerts Betontrappen</title><path fill="{top}" d="{d["black"]}"/><path fill="{bottom}" d="{d["red"]}"/></svg>\n')
    (ROOT / "assets" / "logo" / f"{name}.svg").write_text(svg)
print("viewBox", vb)
