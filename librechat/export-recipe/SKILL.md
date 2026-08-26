---
name: export-recipe
description: "Use to render a Cooklang recipe as Markdown, JSON, YAML, or print-ready text; użyj do eksportu przepisu Cooklang do innego formatu."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, cooklang, export, structured-data, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/export-recipe"
  source-license: "MIT"
---

# Export a Cooklang Recipe

Convert Cooklang content supplied in the conversation or an accessible attachment into the requested text format. Return the result in chat; do not claim that a file was created unless a connected file or code tool actually produced one.

Respond in the user's language and preserve source attribution, ingredient meaning, quantities, units, ordering, optional markers, and notes.

## Workflow

1. Identify the source recipe or recipes and requested target: Markdown, JSON, YAML, plain text, or a print-friendly layout.
2. Parse frontmatter, ingredients, cookware, timers, sections, steps, and notes.
3. Ask only when ambiguity would make the exported data wrong. Otherwise retain uncertain source text and flag it.
4. Render the output in a fenced block labeled with the target format.
5. Validate structure before sending:
   - JSON must parse conceptually as one complete value with quoted keys and no comments;
   - YAML indentation and scalar types must be unambiguous;
   - Markdown must separate metadata, ingredients, equipment, and ordered instructions;
   - print-ready text must remain readable without hidden styling.

## JSON shape

```json
{
  "title": "Recipe name",
  "servings": 4,
  "times": {
    "prep": "15 minutes",
    "cook": "30 minutes"
  },
  "source": "https://example.org/original",
  "ingredients": [
    {"name": "flour", "quantity": 250, "unit": "g", "note": null}
  ],
  "cookware": ["large bowl"],
  "steps": ["Combine the ingredients."]
}
```

Use `null` for a genuinely absent structured value rather than inventing one. Keep original text when a quantity is a range or non-numeric phrase that should not be coerced.

## Final check

- No ingredient, step, attribution, or safety note was dropped.
- Quantities were not rescaled unless requested.
- The output language and units match the user's request.
- The answer clearly distinguishes chat output from an actually generated downloadable file.
