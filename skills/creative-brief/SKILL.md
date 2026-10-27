---
name: creative-brief
description: Turns one grid cell (who x why) into one creative brief with four versions, V1 original, V2 new hook, V3 new creator, V4 new setting, each changing one thing. The brief holds the cell, awareness stage, page, first line in the customer's words, ask, and format, plus an ad name for each version. Use when the user wants an ad brief, creative concepts, or test ideas, has a cell from customer-grid, or asks what to make this week.
---

# Creative brief

One brief, four versions that each change one thing. A designer or creator can start on it today.

This is the BUILD step from Part 1. Week one is one cell, one brief, and four versions.

## When to use

- The user asks for an ad brief, concepts, or test ideas.
- The user has a cell from `customer-grid` or `next-cell`.
- Before `graded-ad-copy`, when there is no brief yet.

## Inputs

Ask for these. Do not start without the first two.

1. The cell: who x why, from `customer-grid`. No grid? Run `customer-grid` first, or ask for 3 to 10 customer quotes and build one cell from them.
2. Verbatim customer quotes for that cell, with sources.
3. The ask: the event you optimise for (for example trial started or purchase) and the offer.
4. The awareness stage. Not sure? Use Problem aware.
5. The page you will send people to, or "none yet".
6. The brand guide from `brand-voice-guide`, if it exists.
7. Constraints: formats you can make, creators you have, a regulated category, or words to avoid.

## Rules

- One brief covers one cell. A new idea is a new cell, not a new version.
- Each version changes one thing from V1 and keeps everything else:
  - V1 original.
  - V2 new hook. Only the hook or first line changes.
  - V3 new creator. Only the person on camera or the voice changes.
  - V4 new setting. Only the place or scene changes.
- Write the first line in their words. Lift it from a quote. Do not polish it.
- The page repeats what the ad promised. Match the page to the stage. If the page does not match, say so.
- Use only claims marked `sourced` in the brand guide. Mark anything else "needs proof".
- In health, finance, insurance, or legal categories, add "needs compliance review".
- Name every version with `references/naming-convention.md`.

## Steps

1. State the cell in one line: who x why.
2. Pick the stage and the matching page from the table in `templates/brief-template.md`.
3. Pick the first line. Choose the quote that names the problem most plainly. Write 3 first line options from real quotes. Mark the one for V1.
4. Write the ask and the format.
5. Write V1 in full. Then write V2, V3, and V4 as the single change from V1.
6. Name each version with the naming convention.
7. Check: does each version change exactly one thing? Does the page match the stage? Fix anything that fails.

## Output

- One brief in `templates/brief-template.md`.
- Four ad names, one per version, ready to paste into Ads Manager.
- One line on what next Monday's read will tell you.

Launch all four together on Monday in a new ad set. Never add ads to a live ad set.

## Next skills

- `graded-ad-copy` to write and score the first line and primary text for V1 and V2.
- `higgsfield-static-ads` or your designer for the statics.
- `visual-qa` before anything ships.
