---
name: imagegen
description: "Use to generate or edit images with clear prompts and controlled visual changes; użyj do generowania lub edycji obrazów."
compatibility: "Requires configured Image Tools MCP or equivalent image generation and editing tools in LibreChat."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "images, generation, editing, prompting, librechat, bilingual"
  version: "1.0.0"
---

# Image Generation and Editing

Use the image capabilities configured in LibreChat, preferably Image Tools MCP, to create or edit raster images. This skill defines quality and control rules; it does not assume a provider, model, command line, local path, or separate API credential.

Respond in the user's language. Preserve any exact text the user supplies in its original spelling unless translation is explicitly requested.

## Choose the intent

- **Generate:** create a new image from text, optionally using references for subject, style, composition, palette, or mood.
- **Edit:** modify an existing image while preserving everything outside the requested change.
- **Clarify roles:** for every input image, identify it as the edit target, identity/subject reference, style reference, composition reference, or element to composite. Never silently treat a style reference as the image to edit.

Use another medium only when it better matches the request, such as SVG for deterministic vector graphics or Mermaid for a technical diagram. Do not replace an explicitly requested photo, illustration, texture, or raster edit with a textual mockup.

## Ask only what blocks a good result

Infer ordinary creative details when the user gives a broad brief, but ask one compact question when the answer materially changes the output: target use and aspect ratio, which image is the edit target, exact text, identity-preservation requirement, or a missing must-keep constraint.

Do not turn a simple image request into a long questionnaire. State reasonable assumptions and proceed.

## Build the working prompt

Translate the request into a concise production brief. Include only relevant fields:

```text
Goal and use: <where and why the image will be used>
Primary request: <the user's intent>
Input images: <Image 1 role; Image 2 role>
Subject: <main subject and essential attributes>
Scene/background: <setting>
Style/medium: <photo, illustration, 3D, collage, etc.>
Composition: <framing, viewpoint, subject placement, negative space>
Lighting/mood: <lighting and atmosphere>
Palette/materials: <only when useful>
Text (verbatim): "<exact text>"
Must keep: <invariants>
Must avoid: <unwanted elements or changes>
```

If the user's prompt is already specific, normalize it without adding new creative requirements. If it is broad, add only details that support the stated use. Do not invent brands, logos, slogans, extra people, or narrative elements.

## Generation rules

1. Use the available Image Tools MCP generation capability and pass the strongest supported inputs from the brief.
2. Specify intended use and composition, not just a list of objects. For layouts with copy, reserve deliberate negative space.
3. Put required text in quotation marks and repeat that it must be rendered verbatim. Keep text short when possible; image models can misspell. Verify every visible character before accepting the result.
4. For multiple requested assets or variants, keep shared constraints stable and vary one purposeful dimension at a time.
5. Do not claim success merely because the tool returned an image. Inspect subject, count, anatomy, perspective, text, crop, artifacts, and forbidden elements.

## Edit rules

1. Treat the supplied image as immutable outside the requested region or property. Restate invariants in every edit call.
2. Preserve face, identity, body proportions, pose, age presentation, skin tone, distinctive features, product geometry, logos, text, camera angle, crop, lighting, and background unless the user explicitly asks to change a specific item.
3. For face or body retouching, confirm the requested scope when it is not explicit. Do not expand a local correction into beautification or reshaping.
4. Say `change only X; keep Y and Z unchanged` rather than describing only the desired result.
5. Never overwrite or imply destruction of the original. Return the edit as a new result.
6. For compositing, specify which image supplies each element and require matched scale, perspective, light direction, shadows, color temperature, and edge quality.

## Review and iteration

After each result:

- compare it against the brief and every `must keep` / `must avoid` item;
- verify exact text character by character;
- for edits, compare unaffected regions for drift;
- identify the single most important defect;
- make one targeted correction while repeating all invariants.

Do not repeatedly regenerate without explaining what is being corrected. If a configured tool cannot perform the requested edit mode, mask, reference handling, or output size, state that limitation and offer the closest honest alternative.

## Delivery

Show the selected result in the chat and briefly report:

- whether it was generated or edited;
- the final prompt or edit instruction;
- important assumptions and any unresolved limitation;
- which variant is recommended if several were produced.

Do not claim a local file was saved or an image was attached unless LibreChat actually returned that artifact.
