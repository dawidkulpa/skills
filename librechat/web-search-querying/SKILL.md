---
name: web-search-querying
description: "Use when forming focused queries with web_search."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "research, web-search, retrieval, query-design"
  version: "0.9.0"
---

# web_search Querying Skill

Use `web_search` for focused, iterative research. It uses SearXNG under the hood, but always refer to the tool as `web_search`.

## Guidelines

1. **Use multiple narrow searches for multi-fact tasks.** Break the request into 2–4 concrete sub-questions and issue a separate `web_search` call for each. Run independent calls in parallel. Loading this skill for a multi-fact task is explicit instruction to use more than the tool's default one-call recommendation.

2. **Keep one intent per query.** A query should discover candidates, verify a specification, check suitability, find pricing, or answer another single facet—not combine the full request.

3. **Keep queries concise.** Start with roughly 2–5 meaningful concepts. Exact multi-word names may make a query longer. Prefer keywords and source vocabulary over conversational sentences.

4. **Start simple, then refine.** Begin with plain terms. If a required facet remains unanswered, make one narrower follow-up query for that facet. Do not stop after the first batch merely because some relevant results appeared.

5. **Use separate calls for alternatives.** Search important aliases, spellings, products, or viewpoints separately instead of joining them into one query.

6. **Use `country` for localization.** Pass a two-letter country code when results should be local. Do not append a country name merely to localize results; keep it in query text only when the country is part of the subject.

7. **Use tool parameters instead of query stuffing.** Apply `date`, `news`, `images`, or `videos` when needed rather than duplicating their purpose in query text.

8. **Use operators sparingly.** Start without `site:`, Boolean expressions, or multiple quoted phrases because support varies across the configured engines. Use quotes mainly for exact errors, identifiers, or phrases known to occur verbatim.

9. **Ground follow-up entities.** Search a specific product, company, person, or document only when the user supplied it or it appeared in a retrieved title or snippet. Do not invent candidates from model memory.

10. **Inspect results before searching again.** Scan all titles, domains, and snippets. Ignore unrelated results. Rephrase a failed query with fewer or clearer terms instead of adding many constraints.

11. **Finish the requested coverage.** Before answering, compare the results with every fact the user requested. Continue with a focused follow-up if an exact candidate, requested value, suitability condition, or other required facet is still missing. Normally stop after 2–4 total calls and state any unresolved limitation.

12. **Verify decisive claims from appropriate sources.** Prefer manufacturer pages, labels, technical sheets, official documentation, standards, repositories, or regulators for exact facts. Once a useful URL is known, inspect it directly when another tool permits.

## Query Shapes

```text
<topic> <facet>
<category> <use-case>
<entity> <requested-field>
<topic> <decisive-condition>
```

Avoid:

```text
<full request copied into one query>
<candidate-A> <candidate-B> <candidate-C>
site:<domain> "<entity>" "<suspected-value>"
```

## Quick Check

- [ ] Multi-fact request: 2–4 separate calls, parallel where independent.
- [ ] One intent per query.
- [ ] Country localization uses `country`.
- [ ] Specific entities came from the user or results.
- [ ] Missing requested facts received a focused follow-up.
- [ ] Irrelevant results were ignored.
- [ ] Exact claims use suitable authoritative sources.
