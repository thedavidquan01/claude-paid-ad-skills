# Budget table

Weekly budget = monthly budget / 4.

Reading one ad costs 2x target CAC. Proving a winner costs 10x target CAC. So the budget sets how many ads you can judge.

## Part 1 table, with a 100 target CAC

| Weekly budget | Ads you can read | Launch on Monday |
|---|---|---|
| 1,250 | 6 | 1 concept, 4 versions |
| 2,500 | 12 | 2 concepts, 8 ads (inference) |
| 3,750 | 18 | 3 concepts, 12 ads (inference) |

Ads you can read = weekly budget / (2 x target CAC), rounded down.

The 2 and 3 concept rows extend the Part 1 pattern of 6 readable ads per concept. The spare reads fund the versions that earn more spend.

## The event check

Under 50 a week, Meta is guessing. Optimise for the earliest event you can afford 50 of a week.

- Target cost per event = target CAC x event to customer rate.
- Budget for 50 events a week = 50 x target cost per event.

Made-up example: target CAC is 100 and 25% of trials become customers. Target cost per trial is 25. Fifty trials a week costs 1,250.

Run `scripts/budget.py` to do this math.
