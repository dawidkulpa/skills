---
name: literature-review
description: "Use for rigorous rapid, narrative, scoping, or systematic literature reviews; użyj do przeglądu i syntezy literatury naukowej."
compatibility: "Live discovery and verification require configured Web Search, Web Fetch, browser, or scholarly MCP tools; no separate model or API key is assumed."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "research, literature-review, science, evidence, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review"
  source-license: "MIT"
---

# Literature Review

Conduct the review inside the normal LibreChat conversation using the retrieval capabilities currently available. Do not delegate the intellectual work to an external model, require a separate credential, or imply access to a database that was not searched.

Respond in the user's language. Preserve publication titles in their original language and translate only explanatory prose unless requested otherwise.

## Web Search Prerequisite

Before the first Web Search or `web_search` call, load the `web-search-querying` skill and follow its query-design, localization, iterative follow-up, and coverage rules. Do not begin searching and load it only afterward.

## Classify the review honestly

Choose the lightest method that meets the request:

- **Rapid review:** focused question, limited sources or dates, explicit shortcuts.
- **Narrative review:** interpretive overview without claims of exhaustive retrieval.
- **Scoping review:** maps concepts, evidence types, and gaps with documented inclusion rules.
- **Systematic review:** predefined protocol, reproducible multi-database search, explicit screening and exclusions, quality assessment, and complete reporting.
- **Meta-analysis:** only when comparable quantitative outcome data and an appropriate statistical method are available; never use the label for a prose synthesis.

If the user asks for a “systematic” review but the accessible tools, time, dual screening, or full texts are insufficient, explain the limitation and deliver a rapid or scoping review instead of overstating rigor.

## Workflow

1. **Frame the question.** Define population/problem, intervention or exposure, comparator, outcomes, context, date range, languages, publication types, and intended use as relevant. Ask only for choices that materially change scope.
2. **Write inclusion and exclusion criteria before searching.** Record protocol changes rather than silently moving criteria to fit discovered papers.
3. **Build search concepts.** Combine controlled vocabulary when known with synonyms, spelling variants, acronyms, and translated terms. Keep the exact query for each source.
4. **Search broadly but honestly.** Use available Web Search, Web Fetch, browser, or scholarly MCP tools. Aim for multiple independent scholarly indexes or domain databases when accessible. Record source/database, exact query, filters, search date, and result count when the interface provides it. A general web search does not become PubMed, Scopus, or Web of Science merely because it finds papers hosted there.
5. **Expand deliberately.** Use backward references, forward citations, related-article links, author searches, trial registries, guidelines, and preprint servers when relevant. Check whether important preprints have peer-reviewed versions.
6. **Screen consistently.** Review title/abstract, then accessible full text. Keep inclusion decisions and exclusion reasons. Do not infer full-text eligibility from a snippet.
7. **Extract structured evidence.** Capture citation, design, setting, sample, intervention/exposure, comparator, outcomes, effect estimates, uncertainty, follow-up, limitations, funding, and conflicts of interest as relevant.
8. **Assess quality with a method appropriate to the study design.** Do not collapse all designs into a single pseudo-precise score. Separate risk of bias, applicability, and certainty of the body of evidence.
9. **Synthesize across studies.** Organize by question or theme, compare agreements and conflicts, explain heterogeneity, and weight evidence by design and quality. Avoid one paragraph per paper with no synthesis.
10. **Verify before writing.** Open-check every cited publication or authoritative record, confirm identifiers and metadata, and ensure the citation supports the claim.

## Capability and evidence rules

- Distinguish abstract-only assessment from full-text review.
- Treat publication metadata, abstracts, and search snippets as different evidence levels.
- Do not invent result counts, excluded-study counts, quotations, effect sizes, confidence intervals, DOI values, or inaccessible methods.
- Current health or policy questions should also check recent guidelines and official evidence summaries, but guidelines do not replace primary-study review when the question requires it.
- Note publication bias, selective reporting, conflicts of interest, language restrictions, date limits, unavailable paywalled text, and search-platform coverage.

## Output

Adapt depth to the request, but for a substantial review include:

```markdown
# Review title

## Review type and scope
## Question and eligibility criteria
## Search methods
| Source | Query | Filters | Search date | Results available |
|---|---|---|---|---:|

## Selection summary and limitations
## Evidence table
| Study | Design/sample | Exposure/intervention | Outcome | Main finding | Key limitation |
|---|---|---|---|---|---|

## Thematic synthesis
## Quality, bias, and certainty
## Evidence gaps
## Conclusions and practical implications
## References
```

For systematic work, include a text selection flow only from recorded counts. Do not fabricate a diagram. Provide Markdown in chat by default; create another document format only when the user asks and the current agent can actually produce it.

## Final check

- The review label matches the method actually completed.
- Search sources, queries, dates, filters, and tool limitations are explicit.
- Included studies meet the stated criteria.
- Synthesis separates evidence from interpretation.
- Every citation and identifier was verified against an accessible source.
