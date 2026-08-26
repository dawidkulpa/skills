---
name: grounded-citations
description: "Use for sourced research, fact-checking, and answers with verifiable citations; stosuj do researchu, weryfikacji faktów i odpowiedzi ze źródłami."
compatibility: "Current claims require a configured Web Search, Web Fetch, browser, or equivalent retrieval tool."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "research, citations, grounding, web, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/NousResearch/hermes-agent/tree/main/skills/research/grounded-citations"
  source-license: "MIT"
---

# Grounded Citations

Ground research in sources the reader can open and verify. Work in the user's language: answer Polish prompts in Polish and English prompts in English unless the user asks otherwise.

## Use this skill when

- the answer depends on current, external, disputed, medical, legal, financial, safety, travel, product, or scientific information;
- the user asks for research, source checking, a comparison, a fact-check, or links;
- a report or recommendation would be materially weaker without traceable evidence.

Do not add citations to casual conversation, creative writing, or facts derived only from user-provided material unless attribution would help.

## Web Search Prerequisite

Before the first Web Search or `web_search` call, load the `web-search-querying` skill and follow its query-design, localization, iterative follow-up, and coverage rules. Do not begin searching and load it only afterward.

## Retrieval rules

1. Use the retrieval capabilities actually available in the current LibreChat agent: Web Search, Web Fetch, browser tools, or a relevant MCP server. Never claim that a site, database, or document was checked when it was not accessible.
2. Search in the language and market relevant to the question. For Polish topics, include Polish queries and prefer Polish or EU primary sources where jurisdiction matters; broaden to English when it improves coverage.
3. Prefer primary and authoritative sources: official documentation, legislation, public authorities, standards, manufacturer specifications, original studies, and first-party announcements. Use reputable secondary analysis to interpret or cross-check, not to replace an accessible primary source.
4. Open the source behind a search result before relying on details that are not fully present in the snippet. A search snippet is evidence only for the text it literally contains.
5. Check publication and update dates. For changing facts, state the date or period to which the answer applies.
6. Cross-check consequential or disputed claims with an independent source when practical. If sources disagree, present the disagreement and explain which evidence is stronger.

## Citation workflow

1. Define the question and identify the claims that need external support.
2. Retrieve focused sources before drafting the conclusion.
3. Keep a simple source list in the order first used. Assign each source one stable number: `[1]`, `[2]`, and so on.
4. Place citations immediately after the sentence or compact paragraph they support. Reuse the same number for the same source. Do not invent an identifier, title, quotation, DOI, or URL.
5. Quote sparingly and verbatim. Clearly mark paraphrases as paraphrases, and never present translated wording as an exact quotation.
6. End with a `Sources` / `Źródła` section listing only cited sources as `number — title — direct URL`. Prefer canonical article or document URLs over search-result links.
7. Before sending, open-check every listed URL when the available tools permit it and confirm that each citation actually supports the nearby claim.

## Evidence calibration

- Distinguish verified fact, source-reported claim, estimate, interpretation, and unresolved uncertainty.
- Exact numbers, dates, product variants, legal requirements, and named findings need direct support.
- Do not hide evidence gaps with confident prose. Say `I could not verify...` / `Nie udało mi się potwierdzić...` and explain what was checked.
- For high-stakes topics, include the relevant limitations and avoid turning general information into individualized diagnosis, legal advice, or financial certainty.
- A long source list is not a quality signal. Use the smallest set that directly supports the answer.

## Output pattern

Use a natural answer rather than a research log. Lead with the conclusion, cite claims where they occur, then provide the source list.

```markdown
<Conclusion and explanation with inline citations.[1] A separate claim may use another source.[2]>

## Sources / Źródła
[1] Source title — https://example.org/source
[2] Source title — https://example.org/other
```

Adapt the heading to the response language. If the user requests another citation style, use it consistently while retaining direct, verifiable links.

## Final check

- Every external factual claim that materially affects the conclusion is supported.
- No citation points only to a search page when the underlying source was available.
- No inaccessible source is described as read.
- Source dates, jurisdiction, and product or document versions are not conflated.
- The answer and source labels match the user's language.
