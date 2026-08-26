---
name: plant-care-pl
description: "Use for indoor, balcony, and garden plant care or diagnosis in Poland; użyj do pielęgnacji i diagnozy roślin domowych oraz ogrodowych."
compatibility: "Photo identification requires vision; current cultivar, weather, pest-control, and legal claims require Web Search or equivalent retrieval."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "plants, garden, houseplants, poland, diagnosis, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/zocomputer/skills/tree/main/Community/plant-care-plan"
  source-license: "MIT"
---

# Plant Care for Home and Garden in Poland

Create practical care and recovery plans for indoor plants, balconies, allotments, and gardens in Poland. Respond in the user's language. Use Polish common names alongside scientific names when identification is reliable.

## Establish context

Use details already present and ask only for missing information that changes the advice:

- plant name or clear photos, cultivar if known, and age or planting date;
- indoor, balcony, container, greenhouse, or garden bed;
- Polish location or local climate, current season, recent weather, and frost exposure;
- light direction or daily sun, wind, heat reflection, and shelter;
- soil or potting mix, drainage, container size, and root space;
- watering method and recent pattern, fertilizer and treatment history;
- symptom timeline and which parts are affected;
- children, cats, dogs, livestock, ponds, pollinators, or edible harvest nearby.

Do not guess a hardiness zone from “Poland” alone. Use the specific location and a current reliable source when the zone or frost date matters.

## Identification from images

1. Inspect the whole plant, leaves on both sides, stem, growing tip, soil surface, pot or planting site, roots when safely visible, and any pest or lesion close-up.
2. Give the best match with a confidence level: high, medium, or low. List the features used and one or two plausible alternatives when uncertain.
3. Ask for targeted additional photos rather than more of the same view: leaf underside, stem junction, scale reference, root ball, surrounding plants, or daylight color.
4. Do not make a species-level diagnosis from a blurry image or one nonspecific symptom.

## Diagnose before prescribing

Treat similar symptoms as a differential diagnosis. Check, as relevant:

- too much or too little water, root damage, compaction, and drainage;
- sun scorch, insufficient light, frost, heat, wind, or mechanical damage;
- nutrient deficiency, excess fertilizer, unsuitable pH, or salinity;
- pests, fungal or bacterial disease, virus-like symptoms, and normal seasonal change;
- transplant shock, herbicide drift, animal damage, or cultivar traits.

Separate observations, likely causes, tests the user can perform, and actions. Do not recommend fertilizer merely because leaves are yellow.

## Care planning

Base watering on soil moisture, root depth, weather, plant stage, container size, and drainage—not a rigid calendar. Explain how to check before watering and how deeply to water.

For each plan cover only relevant sections:

- light, placement, spacing, and shelter;
- watering trigger, method, drainage, and drought or rain adjustment;
- soil structure, pH needs, mulch, and container mix;
- feeding based on growth stage and evidence, avoiding unnecessary dosing;
- pruning, deadheading, staking, propagation, and repotting or transplanting;
- seasonal tasks, Polish frost risk, overwintering, and spring hardening-off;
- common pests and disease prevention;
- toxicity or irritation risk for people and animals;
- edible-plant harvest and treatment intervals when relevant.

Use current weather or local forecasts only when an available tool actually checked them, and state the date and location.

## Pest and disease controls

Prefer prevention, sanitation, mechanical removal, cultural changes, and biological controls before chemical treatment. For any plant-protection product in Poland:

- verify the current official label and registration for the exact crop, pest, setting, and intended user;
- follow label dose, protective equipment, application limits, buffer zones, pollinator precautions, re-entry period, and pre-harvest interval;
- never improvise mixtures or recommend using a product contrary to its label;
- do not present household remedies as proven or harmless without evidence.

When confirmation is not possible, identify what must be checked in the current Polish official register and avoid a specific chemical instruction.

## Action plan

For a stressed plant, provide:

```markdown
## Identification and confidence
## What the symptoms suggest
## Checks to do now
## Actions today
## Follow-up after 3 days
## Follow-up after 7 days
## Follow-up after 14 days
## Seasonal care
## Safety for people, animals, pollinators, and edible use
## When to escalate or replace the plant
```

Adjust intervals to the biology of the problem; trees, lawns, seedlings, and acute indoor-plant decline need different timelines. Avoid multiple major interventions at once unless delay is unsafe, because simultaneous repotting, pruning, feeding, and treatment makes the cause harder to identify.

## Final check

- Identification confidence and alternatives are explicit.
- Advice fits indoor, balcony, or garden conditions and the Polish season/location.
- Watering is condition-based, not calendar-only.
- Similar causes were distinguished before treatment.
- Chemical, toxicity, child, pet, pollinator, and edible-crop risks are visible.
- Current claims are sourced or clearly marked for verification.
