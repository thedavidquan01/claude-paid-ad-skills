---
name: higgsfield-static-ads
description: Turns an approved creative brief and graded ad copy into a small batch of on-brand static ads in Higgsfield Ads Studio through the Higgsfield MCP connector. Reuses or creates the Ads Studio brand, plans 3 to 4 versions or frames from the DESIGN.md prompt block, gets a credit quote and waits for an explicit yes before generating, then runs visual-qa on the results. Use when the user wants static image ads, ad creatives, or Meta or LinkedIn image ads made with Higgsfield, or asks to turn approved copy into designed ads.
---

# Higgsfield static ads

Turn approved copy into 3 to 4 static ads in Higgsfield Ads Studio. Nothing spends credits until the user approves an exact quote.

## When to use

- The user has approved copy from `graded-ad-copy` and wants designed static ads.
- The user asks for Higgsfield ads, Ads Studio ads, or AI image ads in their brand.
- The user wants the same message in a few frames, such as feed and stories.

## Inputs

Ask for these. Do not start without the first three.

1. The brief from `creative-brief`.
2. The approved copy from `graded-ad-copy`: the final 3 variants with hook, headline, primary text, and CTA.
3. `DESIGN.md` from `visual-guide`, including its prompt block.
4. The brand's website URL, or "no website".
5. The placements. Ads Studio frames are 1:1 (square feed), 9:16 (stories and reels), 3:4 (portrait feed), and 16:9 (landscape). It has no 4:5 frame, so offer 3:4 instead.
6. A credit cap for this session.

If the copy or `DESIGN.md` is missing, say so and offer the skill that makes it.

## Connect Higgsfield

Check that the Higgsfield tools are available. Look for tools named `ads_studio_list_brands` and `ads_studio_quote`. Your client may show them with a prefix.

If they are missing, stop and give the user the setup steps in `references/connect-higgsfield.md`. Higgsfield needs a paid plan, and every generation through Claude spends credits.

To test the connection, ask Higgsfield for the credit balance. That calls the `balance` tool and spends nothing.

## Rules

- Quote before you generate. Show the exact ads, frames, and credits. Wait for an explicit yes in chat for that exact plan.
- A yes to a different plan is not a yes. If the plan or price changes, quote again and ask again.
- Stay under the user's credit cap. Higgsfield has no built-in cap, so this rule is the cap.
- Confirm the website URL before you create a brand. The Higgsfield MCP cannot edit a brand after it is created.
- Never create a second brand to fix the first one.
- Reuse one idempotency key per generation. A new key on a retry buys the same batch twice.
- Do not poll in a loop. Check a brand or a run when the user asks.
- Use only claims from the approved copy. In health, finance, insurance, and legal, mark the batch "needs compliance review".
- Remove customer names and private data from anything you send to Higgsfield.

## Steps

1. Load Higgsfield's own Ads Studio instructions before the first Ads Studio call. Call `get_workflow_instructions` with the workflow `ads-studio`. Some connections use `get_preset_instructions` with the preset `ads-studio` instead. Where those instructions are stricter than this skill, follow them.
2. Find or create the brand.
   - Call `ads_studio_list_brands`. If the brand is there, reuse its `brand_id`.
   - If it is not there and the user has a website, confirm the exact URL. Tell the user the brand cannot be edited from Claude once it exists. Then call `ads_studio_create_brand` with the URL. Research takes a few minutes. Check it with `ads_studio_get_brand` when the user asks.
   - If there is no website, skip the brand. Make prompt-only ads with no `brand_id`. Ads Studio then applies no logo, so add the logo in a design tool.
3. Compare the brand to `DESIGN.md`. Read it with `ads_studio_get_brand`. Fill the brand check table in `templates/batch-plan.md` for palette, logo, tone, and audience. If something differs, the user can fix it in Ads Studio on higgsfield.ai. Or set `brand_kit` to false and let the prompt block carry the look.
4. Pick what to advertise. Call `ads_studio_list_products` and pick the product the brief is about. If it is missing, add it with `ads_studio_add_product` from its page link or a description. For an ad about the brand itself, set `include_brand` to true.
5. Plan the batch in `templates/batch-plan.md`. If the brief has V1 to V4, plan one ad per version. Each version changes one thing from V1:
   - V1 original and V2 new hook use the approved first lines from `graded-ad-copy`.
   - V3 new creator changes only the person in the image.
   - V4 new setting changes only the scene.
   Without versions, the default is 4 ads: 3 square (1:1) ads, one per approved copy variant, plus 1 ad of the top variant in the second placement, such as 9:16. Name every ad with the naming convention `DATE_BRIEF-VARIANT_TOPIC-ANGLE_PERSONA_STAGE_LEVER_FORMAT`.
   One run has one frame. Each extra frame is its own run with its own quote.
6. Write the prompt for each run. Use up to 2,000 characters:
   - the `DESIGN.md` prompt block, unchanged,
   - the approved copy for each ad, marked "use these words exactly",
   - the cell (who x why) and the stage from the brief,
   - the objective, only when the brief makes it clear (sales, leads, traffic, awareness, or engagement).
   Add up to 4 style or product pictures as public https links, if the user has them.
7. Quote. Call `ads_studio_quote` with exactly the arguments you will generate with. Call `balance` too. Show a table of each run, its frame, its ad count, and its credits, then the total and the balance. Ask: "Generate these [n] ads for [total] credits? Reply yes to spend." Then stop.
8. Generate only after an explicit yes. Call `ads_studio_generate` with the unchanged arguments, `expected_credits` set to the approved cost of that run, and a stable `idempotency_key`. If the server refuses because the price changed, quote again and ask again. Report each run id and stop. Rendering takes a few minutes.
9. Collect the ads when the user asks. Call `ads_studio_get_run`. Its result has no image link. The pictures show in the generation card. Check `still_rendering` before you say the ads are ready. Ask the user to save the images and attach them.
10. Run `visual-qa` on every ad against `DESIGN.md`, the approved copy, and the placement. Ads Studio writes its own concepts, so check copy match closely. Fix garbled text and logos in a design tool, then check again.

## Fallback for a single image

Use `generate_image` when the user needs one exact layout that Ads Studio does not give. Higgsfield names `marketing_studio_image` as its default model for ads. Set `get_cost` to true first to get the quote without generating. The same approval rule applies.

## Output

- The brand check table.
- The batch plan with the quote and the user's approval.
- The run id of each run.
- A `visual-qa` report for each ad, with a verdict.

A person approves every ad before it runs.

## Next skills

- `visual-qa` for the check in step 10.
- `ad-performance-readout` for the Monday read once the ads have run.

## Credits

The tool names and the quote then approve flow follow Higgsfield's own MCP tool descriptions and help center. This skill is an independent version and copies no Higgsfield code.
