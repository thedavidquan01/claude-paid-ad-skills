---
name: visual-qa
description: Reviews a rendered ad image against the brand's visual guide (DESIGN.md) and approved copy. Flags off-palette colour, wrong type, logo problems, wrong aspect ratio, and on-image text that does not match the approved copy. Use when the user shares a finished or AI-generated ad, mockup, or creative and asks if it is on-brand, ready to launch, or what to fix.
---

# Visual QA

Check a finished ad before it ships. Compare it to `DESIGN.md` from `visual-guide` and to the approved copy from `graded-ad-copy` or `ad-remix`.

## When to use

- The user shares a rendered ad, mockup, or AI-generated image.
- The user asks if an ad is on-brand or ready to launch.

## Inputs

- The ad image or images.
- `DESIGN.md` from `visual-guide`. If it does not exist, say so and offer to run `visual-guide` first.
- The approved copy for this ad: hook, headline, primary text, CTA.
- The placement, so you know the target aspect ratio (for example 1:1, 4:5, or 9:16).
- The ad name, if it follows the naming convention `DATE_BRIEF-VARIANT_TOPIC-ANGLE_PERSONA_STAGE_LEVER_FORMAT`, and the V1 asset for any V2 to V4.

## Rules

- Never state an exact hex code from vision alone. Looking at an image gives an approximation.
- If code execution is available, run `scripts/palette_check.py` and label those colours `measured`. Compression and screenshots can shift colours slightly, so treat small differences with care.
- Without code, label colours `visually-observed` and describe them in words, such as "a warmer orange than the CTA colour".
- Quote on-image text exactly as it appears, including typos.
- Check against the guide. Do not apply your own taste.

## Checks

Fill one row per asset in `templates/qa-report.md`:

| Check | What to look for |
|---|---|
| Palette | Colours outside the DESIGN.md palette, or palette colours in the wrong role |
| Type | Wrong font style, weight, or case. Too many type sizes |
| Logo | Missing, redrawn, distorted, recoloured, too small, or missing clear space |
| Aspect ratio | Matches the placement. Key content clear of edges that the platform crops or covers |
| Copy match | On-image text matches the approved copy word for word. Flag typos, AI-garbled letters, and invented claims |
| Layout | Follows the grid, text density, and CTA position rules |
| Never do | Breaks any never-do rule in DESIGN.md |
| Version | Changes only the lever in its ad name from V1 (HOOK, CREATOR, or SETTING). Flag any second change |

Give each check a status of `pass`, `fix`, or `cannot tell`. Use `cannot tell` when the image does not show enough.

## Output

- The QA table, one row per asset.
- A fix list in priority order. Copy mismatches and logo problems come first.
- An overall verdict: `ready`, `fix then ship`, or `redo`.

A person makes the final call before launch.

## Next skills

- `visual-guide` to update rules if the same issue keeps appearing.
- `graded-ad-copy` if the on-image copy needs work.

## Credits

The QA matrix, the evidence labels, and the rule against trusting a vision model's hex codes draw on the brandkit skill in higgsfield-ai/skills. This skill is an independent version.
