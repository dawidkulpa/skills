---
name: convert-recipe
description: "Use to turn a recipe from a URL, image, file, or pasted text into a clear recipe; użyj do przepisania przepisu do czytelnej postaci."
compatibility: "URLs and images require the corresponding retrieval or OCR capability; pasted text works without tools."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, recipes, conversion, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/convert-recipe"
  source-license: "MIT"
---

# Convert a Recipe

Turn accessible recipe content into a clean recipe that a person can read and cook from directly in chat. Respond in the user's language and preserve the original recipe's meaning, attribution, and source.

## Workflow

1. Identify the input: pasted text, attachment, photo or scan, or URL.
2. Use an available Web Fetch/browser capability for a URL and OCR or vision for an image. If the content is inaccessible, ask the user to paste it; never claim to have read a blocked page or unreadable image.
3. Extract title, yield, ingredients, steps, temperatures, times, equipment, notes, author, and source. Separate facts present in the source from your own inference.
4. Ask only about a missing value that blocks safe or useful conversion. Otherwise label it as not specified instead of inventing it.
5. Normalize Polish output to metric units and °C when conversion is unambiguous. Preserve the original amount in a note when rounding could affect baking or another precision-sensitive recipe.
6. Remove website clutter, duplicated prose, and machine-oriented markup while retaining all cooking information. Briefly list uncertain OCR readings, conversions, or inaccessible sections.

## Default presentation

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Present:

- the recipe title and source attribution;
- servings and available preparation, cooking, and total times;
- a readable bullet list of ingredients, grouped by component if needed;
- numbered cooking instructions;
- notes, substitutions, storage guidance, and safety instructions from the source;
- a short `Uncertainties` section only when something could not be read or verified.

Use ordinary ingredient and timing language. Do not expose source markup, metadata delimiters, scraping artifacts, or machine notation in the reader-facing recipe. Produce JSON, YAML, or another structured representation only when the user explicitly requests it.

## Fidelity rules

- Do not silently improve, rewrite, or add ingredients to the source recipe.
- Preserve alternatives, optional ingredients, temperatures, resting times, and safety instructions.
- Do not remove attribution or replace the original URL with a search URL.
- For handwriting or OCR, mark uncertain characters rather than guessing.
- Do not claim the recipe was imported or saved; the deliverable is the chat content.

## Final check

Verify ingredient quantities against the steps, unit conversions, yield, source attribution, and every uncertain field before sending. Confirm that the recipe renders as readable chat content rather than a code snippet.
