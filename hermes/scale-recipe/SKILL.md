---
name: scale-recipe
description: "Use to scale recipe quantities to a new yield and explain practical adjustments; użyj do przeliczenia przepisu na inną liczbę porcji."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, recipes, scaling, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/scale-recipe"
  source-license: "MIT"
---

# Scale a Recipe

Scale a pasted or attached recipe in the chat. Respond in the user's language and use metric units by default for Polish output.

## Workflow

1. Establish the original yield and requested yield. If either is unknown, ask rather than infer.
2. Calculate `factor = requested yield / original yield`. Use an available calculator or code capability for many ingredients or awkward fractions.
3. Multiply scalable ingredient quantities by the factor. Keep explicitly non-scalable quantities unchanged and explain why.
4. Apply practical judgment instead of blind multiplication:
   - round eggs and indivisible items to a usable plan and explain the choice;
   - scale salt, strong spices, extracts, and leavening cautiously;
   - do not scale cooking time linearly;
   - check pan volume, pot capacity, mixer load, batch count, heat transfer, and food-safe internal temperatures;
   - for baking or preserving, avoid speculative corrections and flag where a tested formula is needed.
5. Return the complete scaled recipe, not just a conversion table, unless the user asked about only one ingredient.

## Default presentation

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Put the result in cooking order:

1. recipe title with the new serving count;
2. a short `Scaling notes` section for the factor, rounding, pan or batch changes, and timing caveats;
3. the full scaled ingredient list;
4. the complete numbered instructions with adjusted quantities where useful;
5. relevant safety, storage, or reheating notes.

Use practical kitchen quantities rather than awkward decimals when that does not compromise the recipe. If exact weight is important, show it alongside the practical measure. If the source uses machine-oriented markup, extract the cooking information and return clean reader-facing text unless the user explicitly requests a structured format.

## Final check

- The factor is correct and applied consistently.
- Rounding does not silently change the recipe.
- Timing and equipment advice are treated separately from ingredient scaling.
- The answer is directly readable while cooking and does not claim that a file was changed or saved.
