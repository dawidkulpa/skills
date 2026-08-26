---
name: scale-recipe
description: "Use to scale recipe quantities to a new yield and explain non-linear adjustments; użyj do przeliczenia przepisu na inną liczbę porcji."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, recipes, scaling, cooklang, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/scale-recipe"
  source-license: "MIT"
---

# Scale a Recipe

Scale a pasted or attached recipe in the chat. Respond in the user's language and use metric units by default for Polish output.

## Workflow

1. Establish the original yield and requested yield. If either is unknown, ask rather than infer.
2. Calculate `factor = requested yield / original yield`. Use an available calculator or code capability for many ingredients or awkward fractions; otherwise show the arithmetic explicitly.
3. Multiply scalable ingredient quantities by the factor. Keep Cooklang fixed quantities marked with `=` unchanged.
4. Apply practical judgment instead of blind multiplication:
   - round eggs and indivisible items to a usable plan and explain the choice;
   - scale salt, strong spices, extracts, and leavening cautiously;
   - do not scale cooking time linearly;
   - check pan volume, pot capacity, mixer load, batch count, heat transfer, and food-safe internal temperatures;
   - for baking or preserving, avoid speculative corrections and flag where a tested formula is needed.
5. Return a compact original-versus-scaled table and, when the input is Cooklang, a complete updated `cooklang` block.

## Output

State the factor and any rounding. Example:

```markdown
Scale factor: 6 / 4 = 1.5

| Ingredient | Original | Scaled | Note |
|---|---:|---:|---|
| flour | 400 g | 600 g | linear |
| eggs | 3 | 4.5 | use weighed egg or choose 4/5 and adjust |
| salt | 1 tsp | start with 1.25 tsp | adjust to taste |
```

For Cooklang, keep ingredient syntax such as `@flour{600%g}` and fixed quantities such as `@salt{=1%pinch}`.

## Final check

- The factor is correct and applied consistently.
- Rounding does not silently change the recipe.
- Timing and equipment advice are treated separately from ingredient scaling.
- The answer does not claim that a file was changed or saved.
