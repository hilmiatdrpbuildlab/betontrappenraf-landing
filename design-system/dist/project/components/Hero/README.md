# Hero

The homepage opener: one of Raf's own stair photos full-bleed under a dark gradient, the header laid over it, one condensed display statement bottom-left and a row of the three stair types.

## Use
- `section.rg-hero[data-theme="dark"]` > `img.rg-hero__media`, the Header (with `.rg-header--transparent` and `rg-logo-on-dark.svg`), then `.rg-container.rg-hero__body` with `.rg-hero__copy` and `.rg-hero__specs`.
- The statement is the company's own promise, **Ter plaatse bekist.**, in `t-display`. Wrap one word in `.rg-accent-word` to set it in `red-500`; never more than one.
- One `rg-btn--lg` primary (**Offerte aanvragen**) and one outline (**Bekijk realisaties**).
- `.rg-hero__specs` lists the stair types Raf builds, each with a step mark. Three cells; link them to the filtered Realisaties page when it exists.
- Photo: a finished stair or a clean formwork shot, with the calm part on the left. The gradient keeps text at 4.5:1 or more over any photo; check a new photo by eye anyway.
- Interior pages reuse the frame at about 420px tall with a `t-h1` instead of `t-display`.

## Avoid
- Stock photos. Every hero photo is Raf's own work.
- Centred copy, a carousel or an autoplay video.
