---
name: ad-remix
description: Remixes the structure of a competitor ad into the user's own brand, using their brand guide. Keeps only the skeleton (hook type, tension, proof type, offer, CTA, format, length) and replaces every word, claim, and visual, then runs a similarity check. Use when the user shares a competitor ad they like and wants their own version, or asks to "remix", "adapt", or "do our version of" an ad.
---

# Ad remix

Borrow the skeleton of an ad that works. Leave the competitor's words, claims, and visuals behind.

## When to use

- The user shares one competitor ad and wants their own version.
- The user asks to remix, adapt, or rework an ad from the `competitor-ad-teardown` output.

## Inputs

- The competitor ad: copy, or a screenshot, plus the advertiser name and capture date.
- The brand guide from `brand-voice-guide`. If it does not exist, run that skill first or ask for positioning, audience pain in their words, voice traits, and sourced claims.
- The visual guide from `visual-guide`, if the user wants visual direction.

## Rules

- Never reuse the competitor's words, claims, offers, characters, or visuals.
- Use only claims marked `sourced` in the brand guide.
- Write in the voice traits from the brand guide.

## Steps

1. Skeleton. Describe each part of the ad by the job it does, not its content:

   | Part | Job it does |
   |---|---|
   | Hook type | for example, a question that names a daily frustration |
   | Tension | for example, cost of doing nothing |
   | Proof type | for example, one customer quote |
   | Offer | for example, free trial |
   | CTA | for example, short imperative |
   | Format | for example, single image, 1:1 |
   | Length | for example, 40 words of primary text |

2. Drop all of their wording. Only the skeleton carries over.
3. Rebuild each part with the user's positioning, the audience's pain in their own words, the voice traits, and sourced claims only.
4. Write 3 variants. For each, give hook, primary text, headline, CTA, and a visual direction that follows `DESIGN.md`.
5. Score each variant against the voice traits from 1 to 5, with one line of reasoning per score.
6. Similarity check. Compare each variant to the original ad. List any phrase of 3 or more words in common, any shared claim, any shared visual idea, and any signature device (a mascot, a catchphrase, a distinctive layout). Replace each one. Then state "similarity check passed" or list what remains.

## Output

- The skeleton table.
- 3 variants with voice scores and visual direction.
- The similarity check result.

## Next skills

- `graded-ad-copy` to score the variants on the full rubric.
- `visual-qa` once the ad is designed.
