---
name: graded-ad-copy
description: Writes 8 ad copy variants for one brief's grid cell, each opening a different way, scores them on a fixed 5-point rubric, runs a claims check that flags "needs compliance review" in health, finance, and other regulated categories, then rewrites the top 3. The top line becomes V1 and the runner-up becomes the V2 new hook. Use when the user asks for ad copy, ad variants, headlines, or hooks for Meta, LinkedIn, or Google ads, or wants existing copy graded.
---

# Graded ad copy

Write 8 variants, grade them hard, and keep the best 3. The grading is the point. It stops weak copy from reaching the ad account.

## When to use

- The user asks for ad copy, variants, hooks, or headlines.
- The user has a brief from `creative-brief`.
- The user wants existing copy scored and improved.

## Inputs

If there is no brief from `creative-brief`, ask for:

- Audience: who they are and the moment they are in.
- Problem in their words: 2 to 3 real customer quotes.
- Promise: the one outcome the product delivers.
- Proof: facts the user can back up, or "none".
- Offer and CTA (call to action).
- Channel: Meta feed, LinkedIn sponsored content, or Google search.
- Category: regulated (health, finance, legal, insurance) or not regulated.
- Words or claims to avoid.

Read the brand guide from `brand-voice-guide` if it exists. Use its voice traits, words to avoid, claims table, and never say list.

## Steps

1. Write 8 variants for the brief's cell. Keep the cell, stage, and ask fixed. Vary only how each one opens: pain, outcome, proof, objection, comparison, curiosity, specific use case, founder voice. A variant that needs a different who or why belongs in another cell. Build each first line from the customer's words in the brief. Each variant has:
   - Hook: up to 12 words.
   - Primary text: up to 60 words.
   - Headline: up to 8 words.
   - CTA.
   For Google search, follow the length limits in `references/rubric.md` instead.
2. Score each variant from 1 to 5 on the rubric in `references/rubric.md`. Give one line of reasoning per score and a total out of 25. Show the results as a table.
3. Claims check. List every factual claim in each variant. Mark each one `backed by brief`, `needs proof`, or `remove`. If the category is regulated, also flag:
   - guaranteed outcomes,
   - before-and-after promises,
   - anything that reads as medical, financial, or legal advice,
   - anything that may need a disclaimer.
   Write "needs compliance review" next to each flag. Never give legal advice.
4. Rewrite the top 3 variants to fix their lowest scores. Remove any claim marked `needs proof` or `remove`.
5. Show the final 3 as a table: hook | primary text | headline | CTA | new score.
6. Map to the brief. The top variant's first line is V1. The runner-up's first line is the V2 new hook. Keep V2's primary text, headline, and CTA the same as V1 so only the hook changes.

## Output

- The 8 variants.
- The score table.
- The claims check.
- The final 3, rewritten.
- The V1 and V2 first lines for the brief.

A person still approves every ad before it runs. In regulated categories, a qualified reviewer signs off.

## Next skills

- `brand-voice-guide` Step 4 to voice-score the finalists.
- `visual-qa` once the copy is on a design.
