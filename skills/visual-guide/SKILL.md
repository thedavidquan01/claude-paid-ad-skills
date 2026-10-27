---
name: visual-guide
description: Turns brand screenshots or a Figma export into a DESIGN.md visual guide (colour, type, layout, photo style, logo rules, never-dos) plus a copy-paste prompt block for image tools such as Higgsfield, Midjourney, or ChatGPT images. Use when the user wants visual brand rules, wants AI images or ad mockups to look on-brand, shares brand screenshots or a Figma file, or before running visual-qa.
---

# Visual guide

Turn what the brand already looks like into rules an AI image tool can follow. The output is a `DESIGN.md` file and a prompt block to paste into any image tool.

## When to use

- The user wants visual brand rules for ads.
- The user shares screenshots of ads, a website, or a Figma export.
- AI-generated images or mockups look off-brand.
- The `visual-qa` skill needs a guide to check against.

## Inputs

Ask for as many of these as the user has:

- 5 to 10 screenshots of current ads, the homepage, and product pages.
- A Figma export (frames as PNG, or a page of styles and components).
- Any existing brand book or style guide.
- Exact hex codes and font names, if the user knows them.
- The brand guide from `brand-voice-guide`, if it exists.

## Evidence labels

Label every rule with where it came from. Use these four labels:

| Label | Meaning |
|---|---|
| `source-declared` | Stated in a brand book, Figma style, or by the user |
| `measured` | Read from pixels with code, such as a colour sampler |
| `visually-observed` | Seen in the screenshots, not measured |
| `inferred` | A reasonable guess. Needs confirmation |

Never present a hex code as exact unless it is `source-declared` or `measured`. A colour you only see in a screenshot is an approximation. Write it as "approx." and ask the user to confirm.

If code execution is available, sample colours from the screenshots with Python and Pillow, and label them `measured`. Note that screenshots and compression shift colours slightly.

## Steps

1. List the inputs you received and what each one shows.
2. Fill in `templates/DESIGN.md`:
   - Colour: each colour, its role (background, text, accent, CTA), hex, and evidence label.
   - Type: font families, weights, case style, and size hierarchy for headline, body, and CTA.
   - Layout: grid, margins, alignment, text density, and where the logo and CTA sit.
   - Photo and illustration style: subjects, lighting, framing, people or no people, product shots, and texture.
   - Logo rules: versions, clear space, minimum size, and placement.
   - Never do: 5 to 10 things that break the brand, each specific enough to check.
3. Write the prompt block (format below).
4. List open questions, such as missing hex codes, missing fonts, or conflicting examples.

## Prompt block for image tools

Fill this in and put it at the end of `DESIGN.md`. Paste it unchanged into every image prompt. Change only the scene description per asset.

```text
[BRAND LOCK: DO NOT DEVIATE]
Brand name spelling: [exact]
Logo: use the attached logo file only. Do not redraw, recolour, or stretch it.
Palette: [hex + role, for example #0B3D2E background, #F5F1E8 text, #E4572E CTA]
Typography: [font and style, for example bold geometric sans serif headline, sentence case]
Layout: [grid and spacing, for example left-aligned text, 10% margins, CTA bottom left]
Photo style: [subjects, lighting, framing]
Must keep: [fixed elements]
Never: [forbidden treatments]
Scene: [the only part that changes per asset]
```

Image tools often misrender text and logos. Tell the user to add final on-image text and the logo in a design tool, then run `visual-qa`.

## Output

- `DESIGN.md` with the six sections, evidence labels, the prompt block, and open questions.

## Next skills

- `ad-remix` and `creative-brief` use the visual rules.
- `visual-qa` checks finished ads against this guide.

## Credits

The evidence labels and the locked prompt block draw on the brandkit skill in higgsfield-ai/skills. The idea of extracting design tokens from a live brand draws on Dembrandt. This skill is an independent version and calls no paid tool.
