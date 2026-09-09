---
name: export-recipe
description: "Use to format a recipe for easy reading, sharing, printing, or structured export; użyj do czytelnego formatowania i eksportu przepisu."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, recipes, export, structured-data, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/export-recipe"
  source-license: "MIT"
---

# Format or Export a Recipe

Format recipe content supplied in the conversation or an accessible attachment for reading, sharing, or printing. Return the result in chat; do not claim that a file was created unless a connected file or code tool actually produced one.

Respond in the user's language and preserve source attribution, ingredient meaning, quantities, units, ordering, optional ingredients, and notes.

## Workflow

1. Identify the source recipe or recipes and the requested use: easy reading in chat, sharing, printing, Markdown, plain text, JSON, or YAML.
2. Extract recipe metadata, ingredients, equipment, steps, timings, sections, and notes without exposing source-specific markup.
3. Ask only when ambiguity would make the result wrong. Otherwise retain uncertain source text and flag it.
4. Default to a polished, reader-facing recipe rendered directly in chat. Use a fenced code block only when the user explicitly requests a machine-readable or copy-exact format such as JSON, YAML, or raw Markdown.
5. Validate the chosen format before sending.

## Reader-facing default

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Use a clear title followed by servings and times, ingredients as bullet points, numbered instructions, notes or substitutions, storage guidance when relevant, and source attribution.

For a print-friendly result, remove conversational commentary and keep the complete recipe compact enough to follow on paper. For a sharing result, retain the source link and include only context that helps the recipient cook the dish.

## Structured formats

Use JSON or YAML only when the user asks for it. Represent missing structured values honestly rather than inventing them, and preserve ranges or non-numeric quantities as text when coercion would lose meaning. A structured export should include the title, servings, times, source, ingredients, equipment, steps, and notes that are available.

## Final check

- No ingredient, step, attribution, or safety note was dropped.
- Quantities were not rescaled unless requested.
- The output language and units match the user's request.
- Reader-facing output is directly readable rather than presented as code.
- The answer distinguishes chat output from an actually generated downloadable file.
