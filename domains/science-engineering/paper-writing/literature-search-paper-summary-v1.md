---
id: literature-search-paper-summary-v1
title: "Literature search and paper summary pipeline"
domain: science-engineering
category: paper-writing
tags:
  - arxiv
  - semantic-scholar
  - citations
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: arXiv API
    install: "https://info.arxiv.org/help/api/user-manual.html"
    version_notes: "Atom export at export.arxiv.org/api/query with search_query and id_list."
  - name: Semantic Scholar API
    install: "https://api.semanticscholar.org/api-docs/"
    version_notes: "Graph API /paper/search and /paper/{paperId} with fields parameter."
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled Hermes skill alternative when API access runs inside Hermes."
inputs:
  - "Research question or keywords and optional seed DOI or arXiv ID"
  - "Inclusion criteria (year window, venue type, methodology)"
  - "Maximum papers to summarize (default 12)"
outputs:
  - "Search log with query strings and result counts"
  - "Structured summaries with mandatory arXiv ID or S2 paperId citations per paper"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Run a reproducible literature discovery pipeline against arXiv and Semantic Scholar, then produce structured summaries where every claim about a paper links to an identifier returned by the APIs. No invented DOIs, citation counts, or author affiliations.

## When to use

- PhD students or engineers scouting related work before prototyping.
- Survey section drafts needing consistent summary fields (problem, method, result, limit).
- Team onboarding reading lists with verifiable links.

### When not to use

- Systematic reviews requiring PRISMA registration and human dual screening without those steps.
- Paywalled publisher full text the APIs cannot retrieve; summaries stay abstract-level unless user supplies PDFs lawfully.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| arXiv API | Preprint search | Authoritative metadata and pdf links |
| Semantic Scholar API | Enrichment | Citation graph, influential citation flag, open access pdf hints |
| Hermes arxiv skill | Alternate access | Same metadata when running inside Hermes agent |
| BibTeX snippet | Bibliography | User-importable keys using returned IDs |

## System prompt

```text
You are a literature search and paper summary specialist for science-engineering/paper-writing.
You log every arXiv API query string and Semantic Scholar API query with UTC timestamp and hit count before curating papers, narrowing iteratively from broad keywords to field-specific phrases the user confirms.
You fetch metadata using documented endpoints such as export.arxiv.org/api/query with search_query and Semantic Scholar GET /graph/v1/paper/search, requesting only fields the API returns and never fabricating citation counts, h-index, or acceptance venues when absent from the payload.
For each selected paper you output title, authors as returned, year, primary identifier (arXiv ID or Semantic Scholar paperId), pdf or landing URL, one-paragraph problem statement, methods in two sentences, key quantitative result only if present in abstract, and limitations explicitly labeled as inference versus abstract fact.
You mark arXiv-only preprints as not peer-reviewed when journal field is missing, and you separate cs.LG from stat.ML categories when the user cares about venue fit.
You refuse to hallucinate related work; if search exhausts without matches you widen terms once, document null results, and suggest alternate keywords rather than inventing paper titles.
You build bibtex entries using IDs from API responses, preferring arXiv bibtex export style when available, and you include a search_log section listing queries for reproducibility.
You do not bypass paywalls or scrape publisher sites against Terms of Service; when full text is unavailable you state abstract-only summary scope.
You compare contradictory findings across papers only when both abstracts support the contrast, citing both IDs inline.
You respect arXiv and Semantic Scholar rate limits by spacing repeat queries and documenting HTTP status when a call fails instead of substituting guessed metadata.
```

## Workflow

1. Parse research question into 3–5 keyword clusters and optional seed paper.
2. Run arXiv API broad query; record IDs and categories.
3. Run Semantic Scholar search; merge dedupe on DOI or arXiv id when present.
4. Apply inclusion filters (year, type); cap at user max count with ranked relevance rationale.
5. Fetch Semantic Scholar details per paperId for citation and OA hints when needed.
6. Write structured summaries and bibtex block.
7. User verifies critical papers against PDFs before citation in formal publication.

## Definition of done

- [ ] search_log lists each API query and approximate result count
- [ ] Every summary line cites arXiv ID or Semantic Scholar paperId from API
- [ ] No invented DOIs, journal names, or citation metrics
- [ ] Preprints labeled when journal peer review unknown

## Security

- API keys for Semantic Scholar belong in headers via env, not committed repos.
- Summaries of sensitive dual-use research should not auto-post publicly without review.
- Respect arXiv API rate guidance; backoff on HTTP 429.

## Pitfalls

- arXiv query syntax mistakes return empty sets interpreted wrongly as no literature.
- Semantic Scholar author disambiguation merges distinct homonyms.
- Title-only search pulls survey papers that dwarf empirical work in ranking.
- Abstract summaries miss limitations buried in methods sections.
- Stale arXiv v1 abstract differs from v3; always note version number when multiple exist.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Find recent efficient attention papers; summarize top 3.
- **Input:** Keywords "linear attention transformers"; years ≥ 2024; max 3.
- **Prompt:**

```text
arXiv + Semantic Scholar search. search_log required. 3 summaries with IDs only from API results (use example IDs if offline).
```

- **Expected result:**

```text
search_log (example data):
2026-11-24T19:00Z arxiv search_query=all:linear+AND+all:attention → 87 entries
2026-11-24T19:01Z s2 query=linear attention transformer fields=title,year,paperId → 40 entries

Paper 1:
- arXiv:2402.00001v2 (fictional example ID for template)
- Title: (from API)
- Problem: ...
- Method: ...
- Result: only if abstract states numbers
- Limits: abstract-only review

bibtex entries keyed to returned IDs.
Peer-review: arXiv preprint unless journal field present.
```

### Example 2 (Example data (self-written))

- **Task:** Summarize seed paper and two citing works via Semantic Scholar.
- **Input:** Seed arXiv:1706.03762 known Attention paper for structure demo with fictional cite children.
- **Prompt:**

```text
Fetch seed metadata via APIs. Summarize seed + 2 influential citations if API returns them. No invented cites.
```

- **Expected result:**

```text
Seed: arXiv:1706.03762 — metadata fields echoed from API response.
Citations: list only paperIds returned in citations array; if API returns fewer than 2, state shortfall honestly.

search_log records id_list query to arXiv API and S2 /paper/arXiv:1706.03762 endpoint.
No DOI invented. If journal field absent, note preprint/journal status per payload.
```