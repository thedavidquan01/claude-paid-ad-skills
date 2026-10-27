---
name: ad-performance-readout
description: Runs the Monday read. Judges every ad on CAC against your target CAC with Part 1's rules (read at 2x, invest up to 5x, prove a winner at 10 conversions at or under target by 10x), never on CTR or hook rate. Parses the ad naming convention, gives each ad a call of cut, invest, winner, or scaling, and the one thing to change next. Works from Zernio or Creative Strategist MCP data, Ads Manager screenshots, or any export. Includes a budget calculator. Use when the user asks for the Monday read, what to cut or scale, how last week went, or how much budget they need.
---

# Ad performance readout: the Monday read

Monday you read and launch. Tuesday to Friday you build. This skill is the read.

This is the MEASURE step from Part 1: count winners. Count what you learn, not what you launch.

## When to use

- It is Monday, or the user asks how last week went.
- The user asks what to cut, keep, or scale.
- The user asks how much budget they need, or how many ads they can test.

## Inputs

1. Target CAC: the most you can pay to win one customer. Read it from `CLAUDE.md`. If it is missing, stop and ask. Nothing can be judged without it.
2. Per ad, since it launched: ad name, campaign name, spend, and conversions.
3. The event you optimise for, and the event to customer rate if the event is not the purchase.

Get the data in this order:

- A connected Zernio MCP or Creative Strategist MCP. Pull ad-level spend and conversions since launch for every live ad. Check the tool list first. Use whatever ad insights tool the connector offers. Never guess a tool name. Some connections only cover organic posts. If yours has no ad-level spend and conversions, say so and ask for an export.
- A CSV or spreadsheet export from Ads Manager. If code execution is available, run `scripts/monday_read.py`.
- Screenshots or numbers typed into chat. Read the numbers, list what you read, and ask the user to confirm before you judge.

## Rules

- Judge on CAC, not clicks. Never judge on click rate or hook rate, even if the data has them.
- CAC = spend / conversions.
- Spend multiple = spend / target CAC.
- Use these calls, in this order:

| Situation | Call | Change one thing next |
|---|---|---|
| In a SCALE campaign, still at target CAC | scaling | Raise the budget about 20%. Check again in 2 to 3 days |
| In a SCALE campaign, above target CAC | scaling | Step back to the last budget that held target |
| 10 or more conversions at or under target CAC | winner | Copy it into its own SCALE campaign. Change one thing, such as only the first line |
| Under 2x target CAC | invest | Still reading. Let it reach 2x |
| 2x or more, no conversions | cut | Check tracking first. If tracking works, cut it |
| 2x to 5x, converting near target | invest | Keep investing up to 5x |
| 5x to 10x, at or under target | invest | Keep going to prove it by 10x |
| Anything else | cut | Take the next version or the next cell |

- "Near target" defaults to a CAC within 1.25x of target. That number is a setting, not a Part 1 rule. Ask the user if they want a different one.
- Scaling is a second test. A winner that misses target in its SCALE campaign steps back. It does not lose its winner status.
- Never add ads to a live ad set. New versions launch together in a new ad set on Monday.
- Use only the numbers provided. Say which source the conversions came from, Meta or the user's own system.
- Label anything you infer as "inference".

## Steps

1. Data check. List the source, the date range, and the columns found. Confirm the target CAC. Stop and ask if spend or conversions are missing.
2. Parse names. Split each ad name on underscores with `references/naming-convention.md`. List any name that does not fit.
3. Judge each ad with the table above. Run `scripts/monday_read.py` when you have a CSV.
4. Count new winners this week.
5. Fill the Monday read log in `templates/monday-read-log.md`.
6. Check the budget. Run `scripts/budget.py` with the target CAC and the budget. Say how many ads next week's budget can read and how many to launch. Flag it if the event falls under 50 a week. See `references/budget-table.md`.

## Output

- Headline: new winners this week, in one sentence.
- The Monday read log, one row per ad, with a call and the one thing to change next.
- Budget line: weekly budget, ads you can read, ads to launch, and the event check.
- Questions for you, only where data is missing.
- Under 300 words outside the table.

## Next skills

- `next-cell` to pick next week's cell and the one change.
- `creative-brief` for the new versions.
