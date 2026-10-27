---
name: competitor-ad-teardown
description: Tears down a competitor's ads from pasted ad text or screenshots taken from the Meta Ad Library or LinkedIn Ad Library. Pulls hooks, angles, offers, formats, and awareness stage into a table, maps each ad to a who x why grid cell, then finds open cells to test. Use when the user shares competitor ads, asks what a competitor is running, asks how to find competitor ads, or wants ad ideas based on what others in their category do.
---

# Competitor ad teardown

Turn 10 to 20 competitor ads into a clear picture of what they say, who they say it to, and what they leave open.

## When to use

- The user pastes competitor ad copy or screenshots.
- The user asks what a competitor is running or how to find their ads.
- The user wants test ideas grounded in their category.

If the user has no ads yet, walk them through `references/finding-ads.md`.

## Inputs

- 10 to 20 ads from one competitor: screenshots, or copy and headline as text.
- For each ad, if visible: the "started running on" date, the format, and the landing page.
- The library each ad came from and the date it was captured.
- The user's brand guide from `brand-voice-guide`. If it does not exist, ask for three lines: what we sell, who we sell to, and our main message.

## Rules

- Describe only what is in the ads. Mark anything else as "inference".
- Quote exact words for every hook.
- Never claim an ad performs well. Public ad libraries do not show results. A long run time is a signal, not proof.
- Do not reuse a competitor's wording in any idea you suggest.

## Steps

1. Inventory. Fill one row per ad in this table:

   | # | Format | Hook (quoted) | Angle | Cell (who x why) | Offer and CTA | Stage | Days running | Landing page |
   |---|---|---|---|---|---|---|---|---|

   - Format: image, video, carousel, document, or text.
   - Hook: the first line, or the first 3 seconds of a video.
   - Angle: the reason to care, such as pain, outcome, proof, fear of missing out, comparison, or price.
   - Cell: the who the ad speaks to and the why it sells, in grid terms. Use the user's grid from `customer-grid` if it exists.
   - Stage: the awareness stage the ad speaks to, from Eugene Schwartz: Unaware, Problem aware, Solution aware, Product aware, or Most aware.

2. Patterns. The 3 to 5 angles they repeat most, the formats they favour, and their 3 longest-running ads with the cell each one sits in. `customer-grid` uses the longest-running ads to check the week-one cell.
3. Offers. Every offer and CTA, and how often each appears.
4. Stage coverage. Count ads per awareness stage. Note which stage is thin.
5. Open cells. 3 to 5 cells, stages, or objections they ignore that the user could own. This is the angle nobody runs yet. Tie each one to the user's customer quotes or brand guide.
6. Tests. 3 open cells for the user. For each, give the who x why, a first line in the customer's words, the stage, and the format.

## Output

- The inventory table.
- Short sections for patterns, offers, stage coverage, open cells, and tests.
- A line stating the capture date and library, so the user knows how fresh it is.

## Next skills

- `customer-grid` to mark cells as taken or open.
- `ad-remix` to borrow the structure of one strong competitor ad.
- `creative-brief` to turn an open cell into a brief.

## Credits

The idea of sorting competitor ads by message and funnel stage draws on the competitor-ads-analyst skill by Rebecca Rae Barton. This skill is an independent version. No text is copied.
