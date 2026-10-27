---
name: customer-grid
description: Mines what buyers actually say (reviews, sales call notes, support tickets) and what competitors run, then builds a who x why grid for one topic. Every cell is one concept, backed by verbatim quotes with sources. Picks the week-one cell where the money already is. Use when the user wants ad concepts, angles, or a testing plan, asks what to test first, shares reviews or call notes, or before creative-brief when no grid exists yet.
---

# Customer grid

Your customers already wrote the grid. This skill finds it in their words and picks the cell to test first.

This is the BUILD step from Part 1: generate your hypothesis. Each cell is one hypothesis.

## When to use

- The user asks what to test, which angle to run, or where to start on Meta.
- The user shares reviews, sales call notes, support tickets, or competitor ads.
- `creative-brief` needs a cell and no grid exists yet.
- `next-cell` needs the grid to pick next week's cell.

## How this differs from other skills

- `customer-grid` decides who to talk to and why they buy. It outputs cells, not copy.
- `brand-voice-guide` decides how the brand sounds. It does not pick concepts.
- `graded-ad-copy` writes the lines. It reads the quotes this grid collects.
- `competitor-ad-teardown` goes deep on one competitor. This skill uses competitor ads only to mark cells as taken or open.

## Inputs

Ask for these. Do not start without at least two customer sources.

1. Reviews: app store, G2, Trustpilot, Google, or your own site.
2. Sales call notes or transcripts.
3. Support tickets or onboarding chats.
4. Competitor ads from the Meta Ad Library, with the "started running on" date. Use `competitor-ad-teardown` output if it exists.
5. The topic, if the user has one. A topic is one problem area, such as weight, sleep, or rostering.
6. Which customer you sell most to today, and the reason they give most often, if the user knows.

Remove customer names and private data before you work. Refer to sources by type and number, such as "review 7" or "sales call 3".

## Rules

- Quote verbatim. Never paraphrase a customer into marketing speak.
- Every quote has a source. A cell with no quote is "inference" and says so.
- WHY THEY BUY uses the words buyers used before they bought. Ignore what they say about features after they bought.
- Keep customer quotes and competitor ad lines apart. Competitor lines show taken ground. They are never a source for your copy.
- Every cell must be a different idea. Two cells that differ only in wording are one cell.
- Never claim an ad performs well. A long run time in the Ad Library is a signal, not proof.

## Steps

1. Pick the topic. Use the user's topic, or the problem that shows up in the most sources. One grid covers one topic.
2. Collect quotes. Pull 15 to 30 verbatim quotes about the topic. Tag each one with its source, the who it comes from, and the why it points to.
3. Find WHO. Group quotes by the kind of person speaking. Keep the two groups with the most quotes. Name each one the way they describe themselves.
4. Find WHY THEY BUY. Group quotes by the reason to act. Keep the three reasons with the most quotes. Name each one in the buyer's words.
5. Build the grid with `templates/grid-template.md`. Who goes down the side. Why they buy goes across. That gives six cells.
6. Fill each cell. Write the concept in one line, the best quote with its source, and a starting awareness stage. Not sure of the stage? Use Problem aware.
7. Mark competitors. For each cell, note whether a competitor ad already runs it and how many days it has run. Mark the cell `taken`, `open`, or `unknown`.
8. Pick the week-one cell. Start where the money already is:
   - the who you already sell most to,
   - crossed with the why they give most often.
   - If a competitor's longest-running ad sits in the same cell, say so. That suggests you are on to something.
   - If the user gave no sales data, pick the cell with the most quotes and label the pick "inference".
9. Hand off. Week one is one cell, one brief, and four versions. Pass the cell to `creative-brief`.

## Output

- The quote bank: quote | source | who | why.
- The grid, filled in `templates/grid-template.md`, saved as `grid.md`.
- The week-one cell, with a two-line reason.
- Gaps: any who or why with fewer than 3 quotes, and the source that would fill it.

## Next skills

- `creative-brief` to turn the week-one cell into one brief with V1 to V4.
- `competitor-ad-teardown` if most cells are `unknown`.
- `next-cell` each Monday to pick the following cell.
