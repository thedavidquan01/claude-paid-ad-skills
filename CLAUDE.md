# Paid ads workspace

Paste this into the instructions of a Claude Project called "Paid ads workspace". In Claude Code or Cursor, keep it as CLAUDE.md in your project root. Replace every [bracket].

## Our business

- What we sell: [one line]
- Who buys: [role, company size, region]
- Channels we run: [Meta / LinkedIn / Google]
- Regulated category: [no / yes: health, finance, insurance, or legal]

## Our numbers

- Target CAC (customer acquisition cost): [number]. The most we can pay to win one customer.
- Event we optimise for: [purchase / trial started / lead]. The earliest event we can afford 50 of a week.
- Event to customer rate: [for example 25% trial-to-paid, or "the event is the purchase"]
- Target cost per event: [target CAC x event to customer rate]
- Monthly budget: [number]. Weekly budget: [monthly / 4]
- Where conversions come from: [Meta / our own system]

## Our grid

Topic: [one problem area]

| Who \ Why | [why 1, their words] | [why 2, their words] | [why 3, their words] |
|---|---|---|---|
| [who 1] | [status] | [status] | [status] |
| [who 2] | [status] | [status] | [status] |

Status is `untested`, `testing`, `cut`, `winner`, or `scaling`. Week-one cell: [who] x [why].

## Files in this project

- `brand-guide.md`: our voice, words, claims, and never say list. Made with brand-voice-guide.
- `DESIGN.md`: our colours, type, layout, and image rules. Made with visual-guide.
- `grid.md`: our who x why grid with verbatim quotes and sources. Made with customer-grid.
- `customer-quotes.md`: real quotes from calls, reviews, and tickets, with names removed.
- `monday-read-log.md`: one Monday read per week. Made with ad-performance-readout.

## How to work

- Read `brand-guide.md` before writing any copy. Read `DESIGN.md` before any visual work. Read `grid.md` before any brief.
- If a file is missing, say so and offer the skill that makes it.
- Use the paid ads skills when they fit. BUILD: customer-grid, competitor-ad-teardown, creative-brief, graded-ad-copy, ad-remix, higgsfield-static-ads, visual-qa. MEASURE: ad-performance-readout. LEARN: next-cell. Setup: brand-voice-guide, visual-guide.
- Judge ads on CAC, not clicks. Read at 2x target CAC. Invest up to 5x. A winner is 10 conversions at or under target CAC.
- Each version changes one thing. Name every ad `DATE_BRIEF-VARIANT_TOPIC-ANGLE_PERSONA_STAGE_LEVER_FORMAT`.
- Use only numbers and claims from our files or this chat. Never invent a number, customer, or claim.
- Label anything you infer as "inference".
- Never copy a competitor's words, claims, or visuals.
- In a regulated category, mark claims "needs compliance review". Never give legal advice.

## How to write

- Lead with the conclusion.
- One idea per sentence.
- Sentence case for headings.
- Define every acronym the first time.
- No hype words from our never say list.

## Weekly loop

Monday you read and launch. Tuesday to Friday you build.

1. Monday, MEASURE: run ad-performance-readout. Count new winners.
2. Monday, LEARN: run next-cell. Scale winners and pick the next cell.
3. Monday: launch last week's versions together in a new ad set.
4. Tuesday to Friday, BUILD: creative-brief on the next cell, then graded-ad-copy, then design or higgsfield-static-ads, then visual-qa.

## Spending

- Never spend Higgsfield credits without a quote and my explicit yes.
- Credit cap per session: [number].
