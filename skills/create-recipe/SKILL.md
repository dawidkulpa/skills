---
name: create-recipe
description: "Use to create a clear, practical recipe from an idea, notes, or a family recipe; użyj do tworzenia czytelnego przepisu z opisu lub notatek."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, recipes, family, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/create-recipe"
  source-license: "MIT"
---

# Create a Recipe

Create a complete, easy-to-follow recipe as reader-facing chat output. Do not assume that you can save it or access a recipe collection. Respond in the user's language; for Polish, prefer familiar Polish ingredient names, metric units, and temperatures in °C.

## Workflow

1. Use information already present in the conversation. Ask only for missing details that materially affect the recipe: dish, servings, dietary restrictions or allergies, available equipment, and target time or difficulty.
2. If the user wants inspiration rather than documentation, propose a practical recipe and state any important assumptions. Never invent a family recipe's missing detail as if the user supplied it.
3. Check that quantities, steps, temperatures, and timings are internally consistent. Flag food-safety-sensitive steps such as cooking poultry, cooling, storage, or reheating.
4. Make the instructions usable while cooking: keep steps short, number them, and repeat an ingredient quantity in a step when the cook would otherwise need to scroll back or guess.

## Default presentation

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Use this order:

1. recipe title;
2. one-sentence description when useful;
3. servings, preparation time, cooking time, and total time;
4. ingredients as readable bullet points, grouped by component when needed;
5. numbered instructions;
6. optional substitutions or serving suggestions;
7. storage, reheating, and food-safety notes when relevant;
8. source or family attribution when supplied.

Use ordinary text such as `250 g flour` and `bake for 25 minutes at 180°C`. Do not add programming-style ingredient markers, metadata headers, or machine-oriented notation unless the user explicitly asks for a structured data format.

Keep the answer friendly and practical. Avoid long prefatory explanations, repeated disclaimers, and unnecessary culinary terminology.

Keep the original source and author when supplied. Do not fabricate a source URL, nutrition values, or claims that estimated cooking times were tested. If the user supplied only a rough memory, clearly mark estimated quantities or timing for confirmation.

## Quality check

- Servings and ingredient amounts agree.
- Every listed ingredient is used, and every ingredient introduced in the steps is listed.
- Metric units are the default for Polish output.
- Equipment, temperatures, and timings are stated where the cook needs them.
- Important assumptions, substitutions, and food-safety constraints are visible.
- The result is readable directly in chat and does not claim it was saved.
