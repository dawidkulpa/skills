---
name: meal-plan
description: "Use to plan meals around household needs, schedule, pantry, and waste reduction; użyj do planowania jadłospisu dla domu lub rodziny."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, meal-planning, family, pantry, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/meal-plan"
  source-license: "MIT"
---

# Meal Plan

Create a realistic meal plan in chat rather than an idealized menu that ignores time, leftovers, or household constraints. Respond in the user's language; for Polish, use familiar Polish product names, metric units, and locally realistic meals and seasonality.

## Gather only decision-changing inputs

Use what the user already said. Ask in one compact message only for missing essentials:

- number and ages of people, and which meals to plan;
- dates or number of days;
- allergies, medical dietary restrictions, preferences, and disliked foods;
- busy days, maximum active cooking time, equipment, and cooking skill;
- budget range when relevant;
- pantry, fridge, freezer, leftovers, or products that should be used first.

Never treat an allergy as a preference. If the user did not provide a recipe collection, work from named dishes or propose recipes rather than pretending to search one.

## Planning workflow

1. Put expiring products and existing leftovers into early slots where safe.
2. Match effort to the schedule: quick meals on busy days, batch cooking when it creates useful leftovers, and at least one flexible or leftovers slot.
3. Balance variety, nutrition, and household acceptance without claiming individualized medical nutrition advice.
4. Reuse ingredients deliberately, but avoid repetitive meals. Identify planned transformations, such as roast vegetables becoming soup or lunch filling.
5. Check storage life and cooling/reheating safety before carrying leftovers across days.
6. Scale each meal to the actual diners and call out child portions or separate mild seasoning when relevant.
7. Produce a consolidated shopping list only after subtracting confirmed pantry stock. Mark uncertain stock as `check before buying`.

## Output format

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Include, in order:

1. important assumptions;
2. a readable meal-plan table with day, meal, dish, active time, and prep or leftover notes;
3. a `Prep once, use twice` section when batch preparation helps;
4. a shopping list grouped by supermarket section;
5. `Use first and storage notes` for perishables and leftovers.

When the user asks for a recipe from the plan, expand it into a normal ingredient list and numbered cooking steps rather than machine-oriented notation. Do not claim the plan, pantry, or calendar was saved.

## Final check

- Every day fits the stated schedule and household size.
- Allergies and exclusions are respected in meals and substitutions.
- Leftovers have a clear origin, destination, and safe storage window.
- The shopping list is deduplicated and uses practical package-aware quantities where possible.
