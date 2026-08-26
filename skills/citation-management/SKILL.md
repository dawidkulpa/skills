---
name: citation-management
description: "Use to find, verify, deduplicate, and format scholarly citations or BibTeX; użyj do wyszukiwania i weryfikacji cytowań naukowych."
compatibility: "Live metadata verification requires configured Web Search, Web Fetch, browser, or scholarly MCP tools; no separate API key is required by this skill."
metadata:
  author: "Dawid Kulpa, Hermes Agent"
  tags: "research, citations, bibtex, doi, pubmed, arxiv, bilingual"
  version: "1.0.0"
  adapted-from: "https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/citation-management"
  source-license: "MIT"
---

# Citation Management

Find and validate publication metadata inside the normal LibreChat workflow. Use the search, page retrieval, browser, or scholarly MCP capabilities that are currently configured. Do not require a separate credential or claim that an external index was queried when it was not.

Respond in the user's language, while preserving titles, author names, journal names, and identifiers exactly as published.

## Web Search Prerequisite

Before the first Web Search or `web_search` call, load the `web-search-querying` skill and follow its query-design, localization, iterative follow-up, and coverage rules. Do not begin searching and load it only afterward.

## Use cases

- find a known or relevant paper;
- resolve a DOI, PMID, PMCID, arXiv identifier, ISBN, or publication URL;
- verify a reference list;
- convert verified metadata to BibTeX or a requested citation style;
- deduplicate references and identify preprint/published-version pairs;
- find missing metadata without inventing it.

## Source hierarchy

Match each field to an authoritative record:

1. publisher or journal article page and DOI landing page;
2. domain record such as PubMed/PMC or arXiv for its own identifier and version history;
3. Crossref, DataCite, OpenAlex, library catalog, or another reputable metadata record available through current retrieval tools;
4. the publication PDF or repository copy for details absent from metadata;
5. search results only for discovery, never as the final authority when an underlying record can be opened.

When records disagree, report the conflict and prefer the source responsible for that field. Do not “correct” author spelling, capitalization, page range, issue, or year from memory.

## Workflow

1. Identify the desired output style and whether the user needs discovery, verification, conversion, or cleanup.
2. Search by exact title, identifier, author, or a focused topic query. For discovery, use more than one relevant index when available and label the coverage.
3. Open the publication or authoritative metadata record. Confirm title, complete author list and order, publication year, venue, volume, issue, pages or article number, publisher, publication type, and stable identifier.
4. Test that the DOI or other persistent link resolves to the same work. Never infer a DOI from a URL pattern.
5. Check whether a preprint has a later peer-reviewed version. Keep both only when the distinction matters, and label versions clearly.
6. Deduplicate by DOI or other stable identifier first, then normalized title, authors, and year. Do not merge corrigenda, editorials, conference abstracts, protocols, datasets, and full papers merely because titles are similar.
7. Format only verified fields. If an expected field is genuinely absent, omit it or add a clear note; do not fabricate volume, pages, DOI, or publisher.
8. For a manuscript bibliography, check that every in-text citation has one reference and every listed reference is used when the manuscript is available.

## BibTeX guidance

Choose the correct entry type and retain Unicode unless the user's toolchain requires LaTeX escaping.

```bibtex
@article{Kowalski2026Example,
  author  = {Kowalski, Anna and Smith, John},
  title   = {Exact Published Title},
  journal = {Journal Name},
  year    = {2026},
  volume  = {12},
  number  = {3},
  pages   = {101--115},
  doi     = {10.0000/example},
  url     = {https://doi.org/10.0000/example}
}
```

Use stable, unique citation keys. Do not silently change existing keys when cleaning a bibliography unless the user requests rekeying; if keys change, provide an old-to-new map.

## Output

For a small request, lead with the verified citation and direct source links. For a batch, use a table:

```markdown
| Input | Status | Verified work | Identifier | Problems or conflicts |
|---|---|---|---|---|
```

Then provide the requested BibTeX or formatted bibliography in one copy-ready fenced block. Add a short verification log naming the records actually checked and the check date.

## Final check

- Every returned identifier resolves to the cited work.
- Author order, title, venue, year, and version match an authoritative record.
- Missing fields are visible rather than guessed.
- Duplicates and preprint/published pairs were handled intentionally.
- Formatting is consistent and direct links are included where useful.
