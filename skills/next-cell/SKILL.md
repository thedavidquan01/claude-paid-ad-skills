---
name: next-cell
description: Picks what to build next after the Monday read. If an ad won, it plans the scale step and the one thing to change. If nothing won, it picks the next grid cell to test and says why. Updates the status of every cell in the grid and hands one cell to creative-brief. Use after the Monday read, when the user asks what to test next, what to change on a winner, or how to split next week's ads between new ideas and iterations.
---

# Next cell

Ask why, then change one thing. This skill closes the weekly loop.

This is the LEARN step from Part 1. It turns the Monday read into next week's build.

## When to use

- Right after `ad-performance-readout`.
- The user asks what to test next or what to do with a winner.
- The user asks how many new ideas and how many iterations to make.

## Inputs

1. The Monday read log from `ad-performance-readout`.
2. The grid from `customer-grid`, saved as `grid.md`. If it is missing, run `customer-grid` first.
3. Next week's launch count from `scripts/budget.py` in `ad-performance-readout`, or the weekly budget and target CAC.

## Rules

- Change one thing at a time. A winner keeps everything except the one lever you test.
- A new idea is a new cell. A new version of the same idea is an iteration.
- Start where the money already is. Prefer cells that share a who or a why with a winner.
- Use the grid's verbatim quotes. Do not invent new reasons to buy.
- Never add ads to a live ad set. Next week's ads launch together in a new ad set.
- Label anything you infer as "inference".

## Steps

1. Update the grid. Set each tested cell to `testing`, `cut`, `winner`, or `scaling` from the Monday read.
2. Ask why. For each winner and each cut, write one line on why, in the buyer's words where you can. Label it "inference".
3. Plan winners first. For each new winner:
   - copy it into its own SCALE campaign and raise the budget about 20% every 2 to 3 days while it holds target CAC,
   - pick the one thing to change for its next iteration, such as only the first line,
   - name the iteration with the naming convention, keeping every part except the lever.
4. Pick the next cell. Use this order:
   - the same who as a winner, with the next why,
   - the same why as a winner, with the other who,
   - the cell with the most quotes that is still `untested`,
   - an `open` cell where no competitor runs ads yet.
   Give a two-line reason. If a competitor's longest-running ad sits in that cell, say so.
5. Split next week's launch. Most of the launch goes to new cells and a small share to iterations on winners. Part 1 showed about 8 net new to 2 iterations in a 10-ad week. Match the launch count from the budget.
6. Hand off. Pass the next cell to `creative-brief` for one brief with V1 to V4.

## Output

- The grid with every cell's status updated.
- Why each winner won and each cut lost, one line each.
- The scale plan for winners.
- The next cell, with its reason.
- Next week's launch split in `templates/next-week.md`.

## Next skills

- `creative-brief` for the next cell.
- `customer-grid` when every cell in the grid is tested. Pick a new topic or refresh the quotes.
