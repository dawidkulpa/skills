# Third-party notices

The canonical skills in this repository include substantially rewritten adaptations of ideas or formats from the projects listed below. The source links and reviewed revisions are recorded for attribution and reproducibility.

## MIT-licensed sources

- `grounded-citations`: NousResearch/hermes-agent, `skills/research/grounded-citations`, revision `cddb908aab2542eec9b4480a3738e9ea0ae3a8f5`; Copyright (c) 2025 Nous Research.
- Cooklang recipe skills: cooklang/cooklang-skills, revision `88aca3b7be2dac550cb92b9488cefb44132cae4b`; Copyright (c) 2026 Cooklang.
- `literature-review` and `citation-management`: K-Dense-AI/scientific-agent-skills, revision `36d8f13a1e754618794bf42f417884940077b4ae`; Copyright (c) 2025 K-Dense Inc.
- `plant-care-pl`: zocomputer/skills `Community/plant-care-plan`, revision `a86c4b112e108e0d1938f5e61ee3a1de59e37f1d`; Copyright (c) 2026 Zo Computer.
- `task-prioritizer`: Cogaid/agent-skills, revision `9b6521253962171c50ccc594306385ab8c9aabb3`; Copyright (c) 2025 Cogaid Solutions Private Limited.

These sources are used under the MIT License:

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## Apache-2.0 source

- `skill-creator`: anthropics/skills, `skills/skill-creator`, revision `3b3fad96af16a10759d930941b4520ba0c40edae`; Copyright 2026 Anthropic, PBC. The Apache License 2.0 text is included at `skills/skill-creator/LICENSE.txt`. The adapted `SKILL.md` carries a prominent source and change notice in its metadata.

## Design references not redistributed

The following repositories were reviewed as design references, but their text or executable resources are not redistributed here. The corresponding skills were written as independent LibreChat-first implementations because the reviewed source either had no applicable license in the selected path or used terms that are not compatible with this repository's general MIT distribution:

- SHIELD-SKY/china-shopping-research, revision `b1063ed06071786a4d5890f4a635fdc63c7499d1` — no license file found; `product-research-pl` is an original Polish-market workflow.
- openai/skills `skills/.system/imagegen`, revision `49f948faa9258a0c61caceaf225e179651397431` — no license file found for the selected system skill; `imagegen` is an original provider-neutral Image Tools MCP workflow.
- apljacob/travel-agent, revision `6ac21feb3f39bac3a1cf15d31cf5d53b665aa6f8` — CC BY-NC 4.0; `travel-agent` is an original chat-first travel-planning workflow and does not reproduce the source's fixed process or deliverable text.
