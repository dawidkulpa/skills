---
name: convert-recipe
description: "Use to convert a recipe from a URL, image, file, or pasted text into Cooklang; użyj do konwersji przepisu do formatu Cooklang."
compatibility: "URLs and images require the corresponding retrieval or OCR capability; pasted text works without tools."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, cooklang, conversion, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/convert-recipe"
  source-license: "MIT"
---

# Convert a Recipe to Cooklang

Convert accessible recipe content in the conversation into a copy-ready Cooklang block. Respond in the user's language and preserve the original recipe's meaning, attribution, and source.

## Workflow

1. Identify the input: pasted text, attachment, photo or scan, or URL.
2. Use an available Web Fetch/browser capability for a URL and OCR or vision for an image. If the content is inaccessible, ask the user to paste it; never claim to have read a blocked page or unreadable image.
3. Extract title, yield, ingredients, steps, temperatures, times, equipment, notes, author, and source. Separate facts present in the source from your own inference.
4. Ask only about a missing value that blocks safe or useful conversion. Otherwise mark it as `not specified` in a note instead of inventing it.
5. Normalize Polish output to metric units and °C when conversion is unambiguous. Preserve the original amount in a note when rounding could affect baking or other precision-sensitive recipes.
6. Produce one fenced `cooklang` block and briefly list any uncertain OCR readings, conversions, or omitted page content.

## Cooklang rules

Use YAML frontmatter with `---` delimiters. Mark ingredients as `@name{quantity%unit}`, cookware as `#name{}`, and timers as `~{duration%unit}`. Put each step in its own paragraph. Multi-word names need braces even without a quantity, for example `@black pepper{}`.

Example:

```cooklang
---
title: Tomato soup
servings: 4
source: https://example.org/tomato-soup
---

Sauté @onion{1}(diced) in @olive oil{15%ml} in a #large pot{} for ~{5%minutes}.

Add @tomatoes{800%g} and simmer for ~{20%minutes}.
```

## Fidelity rules

- Do not silently improve, rewrite, or add ingredients to the source recipe.
- Preserve alternatives, optional ingredients, temperatures, resting times, and safety instructions.
- Do not remove attribution or replace the original URL with a search URL.
- For handwriting or OCR, mark uncertain characters rather than guessing.
- Do not claim the recipe was imported or saved; the deliverable is the chat content.

## Final check

Verify ingredient quantities against the steps, unit conversions, yield, source attribution, and every uncertain field before sending.
