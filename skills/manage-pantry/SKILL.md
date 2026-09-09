---
name: manage-pantry
description: "Use to review pantry stock, expiring food, low supplies, and cook-now options; użyj do zarządzania zapasami kuchennymi i terminami ważności."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "cooking, pantry, food-waste, inventory, bilingual"
  version: "1.1.0"
  adapted-from: "https://github.com/cooklang/cooklang-skills/tree/main/skills/manage-pantry"
  source-license: "MIT"
---

# Manage Pantry

Help the user reason about an inventory snapshot supplied in chat or an attachment. LibreChat chat context is not a guaranteed inventory database: never claim stock was persisted, decremented, or synchronized unless an actual connected tool confirms it.

Respond in the user's language. For Polish, use metric units and Polish product names.

## Workflow

1. Ask for or read the current pantry, fridge, and freezer snapshot. Preserve reported quantities, opened dates, use-by dates, best-before dates, and storage locations.
2. Normalize names and units without merging distinct products. Mark uncertain OCR or missing quantities.
3. Classify items:
   - use immediately because of food safety or a near use-by date;
   - use soon for quality or best-before reasons;
   - low stock;
   - stable stock;
   - unknown because date or quantity is missing.
4. Distinguish `use by` from `best before`. Do not recommend eating food with spoilage signs or overriding official storage guidance. When safety is uncertain, advise discarding or checking authoritative guidance rather than relying on smell alone.
5. Suggest meals that use the most urgent items. Separate `can make now` from `missing one or two items`, and respect allergies and dietary restrictions.
6. Return an updated snapshot for the user to copy after shopping or cooking. Subtract only amounts the user confirms were used.

## Default presentation

Render the default answer as normal Markdown in the chat, never as a fenced code block.

Add a small number of familiar food emojis to aid scanning—typically 3–6 across a full answer. An emoji may prefix a key ingredient (for example, `🍅 tomatoes — 800 g`) or a section heading. Never add one to every line, use an ambiguous emoji, or replace the ingredient name with an emoji.

Use readable tables or bullet lists for pantry, fridge, and freezer items. Include quantity, storage location, relevant date, status, and a short action where known.

Use ISO dates (`YYYY-MM-DD`) to avoid ambiguity. Provide a copyable YAML or JSON snapshot only when the user explicitly requests a structured inventory format.

## Output

Provide:

1. urgent items and why;
2. meal ideas ranked by what they use up;
3. missing items for each idea;
4. low-stock checklist;
5. corrected inventory snapshot if requested.

Do not fabricate expiry dates, quantities, storage conditions, or persistence.
