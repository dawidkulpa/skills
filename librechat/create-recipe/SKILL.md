---
name: create-recipe
description: "Use to create a Cooklang recipe from an idea, notes, or family recipe; użyj do tworzenia przepisu Cooklang z opisu lub notatek."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, cooklang, recipes, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/create-recipe"
  source-license: "MIT"
---

# Create a Cooklang Recipe

Create a complete recipe as chat output. Do not assume that you can save it or access a recipe collection. Respond in the user's language; for Polish, prefer Polish ingredient names, metric units, and temperatures in °C.

## Workflow

1. Use information already present in the conversation. Ask only for missing details that materially affect the recipe: dish, servings, dietary restrictions or allergies, available equipment, and target time or difficulty.
2. If the user wants inspiration rather than documentation, propose a practical recipe and label assumptions. Never invent a family recipe's missing detail as if it were supplied by the user.
3. Check that quantities, steps, temperatures, and timings are internally consistent. Flag food-safety-sensitive steps such as cooking poultry, cooling, storage, or reheating.
4. Return the final recipe in one fenced `cooklang` block so the user can copy it into a `.cook` file. Add a short plain-language note only for important assumptions or substitutions.

## Cooklang format

Use YAML frontmatter and then one paragraph per step:

```cooklang
---
title: Recipe name
servings: 4
prep time: 15 minutes
cook time: 30 minutes
time: 45 minutes
tags: [dinner, quick]
source: https://example.org/original
---

Combine @flour{250%g} and @salt{1%tsp} in a #large bowl{}.

Bake in the #oven{} at 180°C for ~oven{25%minutes}.
```

Syntax:

- ingredient: `@ingredient{quantity%unit}`;
- ingredient without quantity: `@salt{}`;
- multi-word ingredient: `@olive oil{15%ml}`;
- preparation note: `@onion{1}(finely diced)`;
- fixed quantity that should not scale: `@salt{=1%pinch}`;
- cookware: `#pan{}` or `#large mixing bowl{}`;
- timer: `~{10%minutes}` or `~oven{25%minutes}`;
- section: `= Sauce`;
- tip or note: `> text`.

Keep the original source and author when supplied. Do not fabricate a source URL, nutrition values, or tested cooking times. If the user provided only a rough memory, mark estimated quantities or timing for confirmation.

## Quality check

- Servings and amounts agree.
- Metric units are the default for Polish output.
- All ingredients used in the steps are represented in Cooklang markup.
- Equipment and timers are marked where useful, not on every noun or time mention.
- The result is copy-ready and does not claim it was saved.
