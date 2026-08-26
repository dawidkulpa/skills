---
name: shopping-list
description: "Use to consolidate recipe ingredients into a practical grocery checklist; użyj do tworzenia listy zakupów spożywczych z przepisów."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, groceries, shopping-list, cooklang, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/shopping-list"
  source-license: "MIT"
---

# Grocery Shopping List

Build a grocery list from recipes or a meal plan supplied in the conversation. This skill is for food and household ingredients, not durable-product comparison. Respond in the user's language; use metric units and common Polish grocery names for Polish output.

## Workflow

1. Identify the included recipes, meal slots, servings, and dates. Ask only when an omitted value changes quantities materially.
2. Scale each recipe before combining ingredients.
3. Normalize equivalent ingredient names and compatible units, then add quantities. Keep incompatible forms separate, such as fresh and dried herbs or whole and ground spices.
4. Subtract only pantry stock the user confirmed. Put uncertain staples in a `check at home` section.
5. Account for practical pack sizes without pretending to know current store inventory or price. Show both required amount and a reasonable buy amount when they differ.
6. Separate optional garnishes and substitutions. Preserve allergy-safe brands or variants as hard requirements.
7. Group the final checklist by a typical supermarket route. For Polish output prefer: warzywa i owoce, pieczywo, nabiał i jaja, mięso i ryby, produkty suche, konserwy i sosy, mrożonki, przyprawy, chemia/inne.

## Output format

```markdown
## Shopping list / Lista zakupów

### Produce / Warzywa i owoce
- [ ] onion / cebula — need 450 g; buy about 500 g

### Dairy / Nabiał
- [ ] milk / mleko — 1 l

### Check at home / Sprawdź w domu
- [ ] salt / sól — about 10 g needed

### Optional / Opcjonalne
- [ ] ...
```

If requested, also provide JSON, YAML, or a plain checklist in a fenced block. Do not claim that a list was saved, synced, ordered, or purchased.

## Final check

- All recipes and servings are included exactly once.
- Duplicate ingredients are merged only when interchangeable.
- Pantry deductions are traceable to user-provided stock.
- Quantities and units are usable in the user's market.
- Allergy-sensitive variants remain explicit.
