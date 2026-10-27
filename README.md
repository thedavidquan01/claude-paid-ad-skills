# Claude paid ads skills

Eleven free Claude skills that put an AI layer on the CreativeOS from Part 1. They run the weekly loop of build, measure, and learn in your brand voice.

They work in Claude.ai, Claude Code, and Cursor. Each skill is a folder with a `SKILL.md` file in the Agent Skills format. Claude reads the description, then loads the skill when your request fits.

This repo is Part 2 of the Blackbird Signal Session on paid ads. Part 1 covered creative systems. Part 2 runs that system with Claude.

## Where Part 1 left off

The CreativeOS has two jobs and one loop.

- Job 1 is to find a winner. Does Meta work for us?
- Job 2 is to scale it. Can we spend more at the same cost per customer?
- Both jobs run the same weekly loop: BUILD a hypothesis, MEASURE by counting winners, LEARN by asking why and changing one thing.

Part 1 ended on slide 24, "Part 2: an AI layer on the OS". It promised three things. This repo ships them.

| Part 1 idea | Skill that runs it |
|---|---|
| Your customers already wrote the grid | `customer-grid` |
| Grid: who down the side, why they buy across, every cell one concept | `customer-grid` |
| Start where the money already is | `customer-grid` picks the week-one cell |
| Competitors: their ads, and the angle nobody runs yet | `competitor-ad-teardown` |
| Awareness stages, and the page repeats what the ad promised | `creative-brief` |
| One brief, four versions that each change one thing | `creative-brief` |
| First line in their words | `graded-ad-copy` |
| Make the statics | `higgsfield-static-ads`, then `visual-qa` |
| Count what you learn, not what you launch | `ad-performance-readout` |
| Judge on CAC, not clicks | `ad-performance-readout` |
| Fund only what you can judge | `ad-performance-readout` budget calculator |
| Under 50 a week, Meta is guessing | `ad-performance-readout` event check |
| Scale in steps | `ad-performance-readout` and `next-cell` |
| When one wins, change one thing | `next-cell` |
| Pick the next cell | `next-cell` |
| Naming convention | `references/naming-convention.md` in `creative-brief`, `ad-performance-readout`, and `next-cell` |

## The AI layer: build, measure, learn

Run the two setup skills once. Then run the loop every week.

| Step | Skill | What it does |
|---|---|---|
| Setup | `brand-voice-guide` | Builds a one-page voice guide from your real ads, pages, calls, and reviews. Ends with a blind test and a voice score. |
| Setup | `visual-guide` | Turns screenshots or a Figma export into a `DESIGN.md` plus a prompt block for image tools. |
| BUILD | `customer-grid` | Mines what buyers actually say into a who x why grid with verbatim quotes and sources. Picks the week-one cell. |
| BUILD | `competitor-ad-teardown` | Maps competitor ads to grid cells and awareness stages. Finds the open cells and the longest-running ads. |
| BUILD | `creative-brief` | Turns one cell into one brief with V1 original, V2 new hook, V3 new creator, and V4 new setting. Names every ad. |
| BUILD | `graded-ad-copy` | Writes 8 variants for the cell, scores them, checks claims, and gives you the V1 and V2 first lines. |
| BUILD | `ad-remix` | Optional. Rebuilds one competitor ad's structure in your brand, then checks it is not a copy. |
| BUILD | `higgsfield-static-ads` | Optional. Makes one static per version in Higgsfield Ads Studio. Quotes the credit cost and waits for your yes. Needs a paid Higgsfield plan. |
| BUILD | `visual-qa` | Checks each finished ad against `DESIGN.md`, the approved copy, and its version's one change. |
| MEASURE | `ad-performance-readout` | The Monday read. Judges every ad on CAC with the 2x, 5x, and 10x rules. Gives each ad a call and the one thing to change next. Includes a budget calculator. |
| LEARN | `next-cell` | Plans the scale step for winners and picks the next cell. Splits next week's launch between new cells and iterations. |

## The weekly loop

Monday you read and launch. Tuesday to Friday you build.

Monday:

1. MEASURE. Run `ad-performance-readout` on every live ad. Count new winners.
2. LEARN. Run `next-cell`. Scale the winners. Pick next week's cell.
3. Launch last week's build together in a new ad set. Never add ads to a live ad set.

Tuesday to Friday:

1. BUILD. Run `creative-brief` on the next cell.
2. Run `graded-ad-copy` for the V1 and V2 first lines.
3. Make the four versions, or run `higgsfield-static-ads`. Run `visual-qa` on each one.

Once a month, refresh `customer-grid` and `brand-guide.md` with new reviews, calls, and tickets.

## Before your first Monday

1. Write your target CAC in `CLAUDE.md`. Target CAC is the most you can pay to win one customer.
2. Pick the event. Optimise for the earliest event you can afford 50 of a week.
3. Install the pixel and check that the event fires.
4. Set the weekly budget. Run `budget.py` to see how many ads it can read.
5. Fill one grid row with `customer-grid`.
6. Write one brief with four versions with `creative-brief`.
7. Check that the page matches the stage.
8. Launch all four together on Monday.

## The numbers from Part 1

- Target CAC is the most you can pay to win one customer.
- A winner is 10 conversions at or under target CAC.
- Spend 2x target CAC to read an ad. Spend 10x target CAC to prove a winner.
- At 2x with no conversions, check tracking, then cut.
- At 2x and converting near target, keep investing up to 5x.
- Never judge on click rate or hook rate.
- Expect about 1 winner a week at best.
- Under 50 events a week, Meta is guessing.
- Scale a winner in its own campaign with about 20% budget bumps every 2 to 3 days. Step back if it leaves target CAC.
- Broad is the default. Your ad is the targeting.

## Naming convention

Name every ad so the Monday read can split it on underscores.

```text
DATE_BRIEF-VARIANT_TOPIC-ANGLE_PERSONA_STAGE_LEVER_FORMAT
261019_B01-V2_Rostering-SundayNights_SHIFTMGR_PROBLEM_HOOK_IMG
```

The full reference is in `skills/ad-performance-readout/references/naming-convention.md`.

## Budget table

Weekly budget is the monthly budget divided by 4. With a 100 target CAC:

| Weekly budget | Ads you can read | Launch |
|---|---|---|
| 1,250 | 6 | 1 concept, 4 versions |
| 2,500 | 12 | 2 concepts, 8 ads |
| 3,750 | 18 | 3 concepts, 12 ads |

Run it for your own numbers:

```bash
python3 skills/ad-performance-readout/scripts/budget.py --target-cac 100 --monthly 5000 --event-rate 0.25
```

## Install

### Claude.ai

1. Turn on code execution. On Free, Pro, and Max plans, open Settings, then Capabilities. On Team and Enterprise plans, an owner may need to turn on skills first.
2. Download the zips from the `dist/` folder. There is one zip per skill.
3. Open Customize, then Skills. Click +, then Create skill, then Upload a skill.
4. Upload each zip and switch the skill on.
5. Create a Claude Project called "Paid ads workspace". Paste `CLAUDE.md` into its instructions.

Skills you upload to Claude.ai are personal to you. Each teammate uploads their own.

### Claude Code

One line, from your terminal:

```bash
git clone https://github.com/thedavidquan01/claude-paid-ads-skills.git && cd claude-paid-ads-skills && ./install.sh
```

This copies every skill into `~/.claude/skills`. To install for one project only:

```bash
./install.sh --project /path/to/your/project
```

Or copy the folders by hand:

```bash
cp -R skills/* ~/.claude/skills/
```

Type `/skills` in Claude Code to check they loaded.

### Cursor

Cursor reads skills from `~/.claude/skills`, so the Claude Code install already works in Cursor. To keep a Cursor-only copy:

```bash
./install.sh --cursor
```

This also copies the skills into `~/.cursor/skills`. For one project, copy the folders into `.cursor/skills` in that project. Type `/` in Agent chat and search for a skill by name to check.

### Higgsfield connector (only for `higgsfield-static-ads`)

`higgsfield-static-ads` needs the Higgsfield MCP server. The other ten skills need nothing extra. You need a paid Higgsfield plan, and every generation spends credits.

In Claude.ai or Claude Desktop:

1. Open Customize, then Connectors. Click Add, then Add custom connector.
2. Name it Higgsfield and paste `https://mcp.higgsfield.ai/mcp`.
3. Click Connect, then sign in to Higgsfield and authorize.
4. In a chat, click +, open Connectors, and switch Higgsfield on.

In Claude Code, connectors from your claude.ai account show up on their own. Or add the server and sign in with `/mcp`:

```bash
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```

To check it works, ask: "What is my Higgsfield credit balance?" Full steps and sources are in `skills/higgsfield-static-ads/references/connect-higgsfield.md`.

### Safe to rerun

`install.sh` skips skills that are already up to date. If you changed a skill, it backs up your version before it copies the new one. Run `./install.sh --dry-run` to see what would happen first.

## Your first 30 minutes

| Minutes | Do this | Working looks like |
|---|---|---|
| 0 to 5 | Install the skills | All 11 show in your skills list or `/skills` |
| 5 to 15 | Run `customer-grid` on `examples/example-customer-sources.md` | A 2 x 3 grid with quotes and a week-one cell |
| 15 to 20 | Run `creative-brief` on the week-one cell | One brief with V1 to V4 and four ad names |
| 20 to 25 | Run `ad-performance-readout` on `examples/example-ads-export.csv` with a target CAC of 100 | A Monday read log with 1 winner, 1 scaling, 3 invest, and 2 cut |
| 25 to 30 | Run `next-cell` on that read | Next week's cell and launch split |

No data with you? Every skill works on the made-up files in `examples/`.

## Example prompts

```text
Use the customer-grid skill. Here are 40 reviews, 6 sales call notes, and 20 support tickets. Topic: rostering.
Use the competitor-ad-teardown skill on these 15 ads from [competitor], captured today from the Meta Ad Library. Map them to our grid.
Use the creative-brief skill on the week-one cell. Event: trial started. Stage: problem aware.
Use the graded-ad-copy skill on brief B01. We are not in a regulated category.
Use the higgsfield-static-ads skill on brief B01 and the final 3. One ad per version. Quote first.
Use the visual-qa skill on these four ads. The approved copy is below.
Use the ad-performance-readout skill for the Monday read. Target CAC is 100. Export attached.
Use the next-cell skill on this Monday read and our grid. We can launch 8 ads next week.
Use the brand-voice-guide skill. Here are our 5 best ads, our homepage, and 10 reviews.
Use the visual-guide skill on these 8 screenshots of our ads and site.
```

## Static ads with Higgsfield

Try it on the made-up files first. Attach `examples/example-approved-copy.md` and `examples/example-DESIGN.md`, switch on the Higgsfield connector, then send:

```text
Use the higgsfield-static-ads skill on the attached brief and final 3. Follow the attached DESIGN.md. This is a made-up brand with no website, so make prompt-only ads with no brand kit. Plan 3 square ads, one per copy variant, plus one 9:16 ad of variant 1. Get the quote, show it, and stop. I decide on spend after I see it.
```

Claude plans the batch, quotes it, and stops. Nothing spends credits until you reply yes. When the ads are ready, save them and run `visual-qa` on each one.

The Higgsfield MCP cannot edit an Ads Studio brand after it exists. Check the website URL before you create one. Fix brand details in Ads Studio on higgsfield.ai.

## Repo layout

```text
claude-paid-ads-skills/
  README.md
  CLAUDE.md            project instructions template
  LICENSE              MIT
  install.sh           installer for Claude Code and Cursor
  skills/              one folder per skill, each with SKILL.md
    customer-grid/       BUILD: who x why grid from buyer words
    creative-brief/      BUILD: one brief, V1 to V4
    ad-performance-readout/  MEASURE: the Monday read and budget.py
    next-cell/           LEARN: scale winners, pick the next cell
  dist/                one zip per skill, for Claude.ai upload
  examples/            made-up data for practice
  scripts/build-zips.sh  rebuilds dist/ after you edit a skill
```

## Rules the skills follow

- Use only your sources. Never invent a number, customer, or claim.
- Label inference as inference.
- Never copy a competitor's words, claims, or visuals.
- Flag "needs compliance review" in health, finance, insurance, and legal. A qualified person signs off.
- Remove customer names and private data before you upload anything.
- Judge on CAC, not clicks.
- Change one thing at a time.
- Read every skill before you install it, including these.

## Credits and further reading

These skills are original. Some ideas come from the work below. Each project has its own licence.

- David Quan, "How to make a lot of money on Meta", Blackbird Signal Session Part 1. The CreativeOS loop, the grid, the CAC rules, the brief, the naming convention, and the budget table.
- Eugene Schwartz, Breakthrough Advertising. The five awareness stages.
- [Corey Haines, marketingskills](https://github.com/coreyhaines31/marketingskills). A large library of marketing skills, including ads, copywriting, and product marketing context.
- [Rebecca Rae Barton, competitor-ads-analyst](https://github.com/thatrebeccarae/claude-marketing/tree/main/skills/competitor-ads-analyst). Sorting competitor ads by message and funnel stage. Inspired `competitor-ad-teardown`.
- [Anthropic knowledge-work-plugins, brand-voice by Tribe AI](https://github.com/anthropics/knowledge-work-plugins/tree/main/partner-built/brand-voice). Turning brand material into enforceable guidelines. Inspired `brand-voice-guide`.
- [Anthropic knowledge-work-plugins, brand-review](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing/skills/brand-review). Reviewing content against a brand, including claims. Inspired the claims table.
- [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) (MIT). The brandkit skill's locked prompt block, evidence labels, and QA matrix. Inspired `visual-guide` and `visual-qa`.
- [Higgsfield: connect to Claude, ChatGPT, or another agent](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent). The MCP server URL and sign-in steps used in `higgsfield-static-ads`.
- [Higgsfield Ads Studio](https://higgsfield.ai/blog/higgsfield-ads-studio). How Ads Studio builds a brand kit and static ads. `higgsfield-static-ads` follows the tool names and quote then approve flow in the Higgsfield MCP's own tool descriptions. It copies no Higgsfield code.
- [Dembrandt](https://github.com/dembrandt/dembrandt) and [dembrandt-skills](https://github.com/dembrandt/dembrandt-skills). Extracting design tokens from a live site. Inspired `visual-guide`.
- [Anthropic Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview). The skill format.
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude). Uploading skills to Claude.ai.
- [Use connectors in Claude](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) and [Claude Code MCP docs](https://code.claude.com/docs/en/mcp). Adding the Higgsfield connector.
- [Cursor Agent Skills](https://cursor.com/docs/skills). Where Cursor looks for skills.

## Licence

MIT. Copyright 2026 David Quan. See `LICENSE`.
