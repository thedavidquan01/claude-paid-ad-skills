---
name: brand-voice-guide
description: Builds a one-page brand voice guide from real sources (best ads, website pages, sales call snippets, reviews, founder posts), then tests it with a blind test and a voice score. Use when the user wants a brand guide or tone of voice, says AI copy sounds generic or off-brand, or before writing any ad copy, brief, or remix if no brand guide exists yet. Run this first. Every other paid ads skill in this pack reads its output.
---

# Brand voice guide

Build a one-page brand guide from evidence, then prove it works. Every other skill in this pack reads the guide, so run this one first.

## When to use

- The user asks for a brand guide, voice guide, or tone of voice.
- The user says AI copy sounds generic, salesy, or "not us".
- Another skill in this pack needs a brand guide and none exists.
- Once a month, to refresh an existing guide with new sources.

## Step 1. Collect the inputs

Ask for these sources. Accept whatever the user has. Do not start until you have at least three of the six.

| Input | Why it matters |
|---|---|
| 3 to 5 best-performing ads, with the metric that made each one best | Proof of what buyers already respond to |
| Homepage and 2 product pages (text or screenshots) | Current positioning, claims, and CTAs (calls to action) |
| 5 to 10 sales call snippets in the buyer's own words | How buyers describe the problem |
| 10 reviews from G2, Capterra, or similar | Unprompted customer language |
| 2 to 3 founder posts or long-form pieces | The beliefs and stance behind the brand |
| An existing brand or style guide, if any | Rules already agreed |

Remind the user to remove customer names, emails, and private data before sharing.

## Step 2. Build the guide

Rules:

- Use only the sources provided. Quote exact lines and name the source of each.
- Mark anything you infer as "inference".
- If a section has no evidence, write "no evidence yet" and say what to collect.
- Never invent a number, customer, or claim.

Fill in `templates/brand-guide-template.md` in this order:

1. Positioning in one line: who it is for, what it does, why it is different.
2. Audience: buyer and user roles, their main problem as a quote, and what they fear about changing.
3. Voice traits: 3 to 5. For each, give the trait, a "this, not that" pair, and one real example line with its source.
4. Words to use and words to avoid. Give a reason for each word to avoid.
5. Claims table: every number, superlative, or comparison, its source, and a status of `sourced`, `needs source`, or `do not use`.
6. Offer: what the buyer gets and what they do next.
7. CTA style: the exact CTAs in use, their length, and their tone.
8. Never say: 10 lines that sound like a competitor or break the voice.

Keep it to one page. Use tables. Visual rules live in a separate file made by the `visual-guide` skill.

Save the result as `brand-guide.md`. In Claude.ai, tell the user to add it to their Claude Project files. In Claude Code or Cursor, write it to the project root.

## Step 3. Blind test

1. Write 5 short ad lines for the user's main offer. Each line is a hook plus one sentence. Do not reuse or lightly edit any line from the sources.
2. Ask the user to mix them with 5 real lines from their ads or site, then ask a teammate to pick the 5 real ones.
3. If the teammate spots the AI lines easily, ask the user which lines gave it away. Compare those lines to the real ones. Add what the real lines do to the guide as a sharper trait or example.

## Step 4. Voice score

Score any set of lines against every voice trait, from 1 to 5. A 5 means a customer would assume the brand wrote it. Give one line of reasoning per score.

Then flag:

- Any word from the words to avoid list.
- Any claim not marked `sourced` in the claims table.
- Any line that matches the never say list.

A trait that keeps scoring under 3 needs a sharper "this, not that" pair or a better example line. Update the guide.

## Step 5. Monthly refresh

When the user brings new sources (top ads, new reviews, new call snippets), propose changes only where the new sources give evidence. Show each change as: section | current | proposed | source. Flag any claim that is now out of date.

## Output

- `brand-guide.md`, one page, following the template.
- A blind test set of 5 lines.
- A voice score table when the user asks for one.

## Next skills

- `visual-guide` for colour, type, layout, and image rules.
- `competitor-ad-teardown` to see what competitors say.
- `creative-brief` and `graded-ad-copy` to write ads in this voice.

## Credits

The idea of turning scattered brand material into enforceable AI guidelines, with a "We are / We are not" anchor, comes from the Brand Voice plugin by Tribe AI in Anthropic's knowledge-work-plugins repo. This skill is an independent, simpler version. No text is copied.
