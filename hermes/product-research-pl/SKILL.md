---
name: product-research-pl
description: "Use to compare products and offers for purchase in Poland, especially Allegro; użyj do wyboru produktu i oferty na polskim rynku."
compatibility: "Current prices, stock, seller terms, and offers require Web Search, browser, or shopping tools."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "shopping, product-research, allegro, poland, consumer, bilingual"
  version: "1.0.0"
---

# Product Research for Poland

Help the user choose a product and a concrete offer for delivery in Poland. Optimize for fit, total cost, seller reliability, and after-sales conditions—not rankings, novelty, sponsored content, or the largest specification number.

Respond in the user's language. Default to Poland, PLN, metric units, Polish/EU variants, and delivery to Poland unless the user states another market.

## Market and channel policy

Start offer discovery on Allegro whenever the requested product is normally sold there. Allegro is the preferred purchasing channel, not automatic evidence that an offer or seller is good.

For every serious Allegro candidate, verify:

- exact model, generation, configuration, color/size, EAN or manufacturer code when available;
- seller identity, rating pattern, business status, shipping origin, delivery date, invoice, return terms, warranty or conformity handling, and whether the listing is new, used, refurbished, outlet, import, or preorder;
- final payable price including delivery, mandatory accessories, coupons, subscriptions, bundles, installments, and other conditions.

Use the manufacturer's Polish/EU page for specifications, compatibility, supported variants, warranty information, and consumables. Use Ceneo or other reputable Polish comparison services to map prices and sellers, but never treat ranking position as proof of quality. Consider established Polish retailers or direct manufacturer stores when they provide a materially better price, safer seller, clearer warranty, faster delivery, or easier return.

## Decision workflow

1. **Clarify only what can change the choice.** Establish primary use, important secondary use, target budget and hard ceiling, hard requirements, unacceptable compromises, compatibility or size constraints, existing ecosystem, expected ownership time, and purchase timing. If details are unlikely to change the result, state reasonable assumptions and proceed.
2. **Define elimination criteria before scoring.** A hard requirement eliminates a candidate; it is not averaged away by unrelated strengths.
3. **Map the category.** Separate critical factors, user-dependent tradeoffs, and marketing-heavy features. Explain useful thresholds and diminishing returns.
4. **Build a focused shortlist.** Usually compare two to four genuinely competitive exact variants. Do not add weak options merely for variety.
5. **Match evidence to the claim.** Use official specifications for features and compatibility, transparent professional tests for measured performance, and repeated long-term owner reports for reliability and maintenance. Separate recurring patterns from isolated anecdotes.
6. **Verify live Polish offers.** Record the date checked. Never invent price, stock, historical low, promotion eligibility, delivery time, seller terms, or review count. If live access is unavailable, give selection guidance and a verification checklist instead of pretending to have checked offers.
7. **Calculate ownership cost when material.** Include consumables, replacement parts, subscriptions, energy, installation, accessories, maintenance, repairability, and switching cost over a stated period. Use ranges and explicit assumptions when exact values are unavailable.
8. **Run an anti-recommendation check.** For each finalist answer: `When should the user not buy it?` / `Kiedy nie warto go kupować?` and `What is the largest purchase risk?` / `Jakie jest największe ryzyko zakupu?`
9. **Recommend one option clearly.** Prefer the least expensive product that fully satisfies important requirements. Recommend a higher tier only when the extra cost materially improves this user's outcome.

## Output for a detailed comparison

```markdown
## Recommendation / Rekomendacja
<First choice, exact variant, decisive reason, confidence, date checked>

## Requirements and assumptions / Wymagania i założenia
- ...

## Shortlist / Krótka lista
| Product and exact variant | Fit | Main advantage | Main compromise | Verified offer price | Seller/channel |
|---|---|---|---|---:|---|

## Offer check / Weryfikacja oferty
- Allegro listing and seller: ...
- Manufacturer or authorized channel: ...
- Ceneo/market cross-check: ...
- Return, warranty/conformity, invoice, shipping origin: ...

## Total cost / Koszt całkowity
- ...

## Do not buy if / Kiedy nie kupować
- ...

## Evidence gaps / Braki w danych
- ...

## Purchase checklist / Lista przed zakupem
- [ ] Confirm exact model/EAN and seller
- [ ] Confirm final checkout price and delivery
- [ ] Save listing and terms applicable on purchase date
```

Use direct offer and source links when available. Distinguish a found price from an estimate and list conditional discounts separately.

## Transaction boundary

Research and recommend by default. Do not claim an item was added to a cart, ordered, reserved, or paid for. If connected tools can perform a transaction, do so only after an explicit user request and a final confirmation of the exact product, offer, seller, quantity, delivery address or pickup method, and total price.

## Final check

- The exact variant and Polish/EU compatibility are clear.
- Allegro was checked first when appropriate, but seller and terms were evaluated independently.
- All current facts include a check date and source.
- Hard requirements, total cost, return/warranty handling, and anti-recommendation risks are visible.
- Unavailable evidence lowers confidence instead of being simulated.
