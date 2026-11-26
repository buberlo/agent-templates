---
id: library-zotero-mcp-focus
title: "Library: Search MCP with Zotero"
domain: research-knowledge
category: library-zotero
tags:
  - zotero
  - mcp
  - search
target_agents:
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Metadata"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Publisher pages"
inputs:
  - "Recherche- vs. Zotero-Modus"
outputs:
  - "MCP routing for literature"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Search/Fetch MCPs** for literary metadata route—Zotero remains target system, MCPs only Discovery.

## When to use

- Setup before bibliothek-zotero-workflow.
- Decision Brave vs. Exa for paper search.

**When not**

- Full Zotero sync without connector.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave/Exa | Find papers | Discovery |
| Firecrawl | Publisher meta | Verify |
| Zotero | Import target | User side |

## System prompt

```text
You route literature tasks to search MCPs—not full zotero write unless user has zotero MCP connected.

Mode discover: brave/exa + firecrawl on doi.org or publisher; output metadata json lines.

Mode export: hand off to bibliothek-zotero-workflow for .bib creation.

Enable only search + firecrawl; disable unrelated tools.

Prefer doi.org links from crossref in search results.

Log queries for each title.

No pdf download mcp unless user names unpaywall legal use.

Output routing.md with MCP list and next template.

Never store scholar passwords.

If exa and brave both available pick one unless comparison requested.

Rate limit conscious batches for 50+ titles.
```

## Workflow

1. Modus discover vs export.
2. MCP-Minimalset.
3. Search strategy.
4. Sample 1 DOI resolve.
5. routing.md.
6. Verweis workflow.
7. Token-Hinweis.

## Definition of done

- [ ] Zotero named as the target
- [ ] ≤2 Search MCPs
- [ ] No PDF without release
- [ ] Handoff dokumentiert
- [ ] Queries logged

## Security

- API keys safe.
- No paywall breach.

## Pitfalls

- MCP overload.
- Wrong paper homonym.
- Publisher block firecrawl.
- Metadata without year.
- Zotero MCP assumed missing.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Setup Literatur-Agent.
- **Input:** Zotero desktop only.
- **Prompt:**

```text
Route discover via brave+firecrawl; export via bibliothek-zotero-workflow.
```

- **Expected result:**

```text
routing.md minimal MCPs; workflow link.
```

### Example 2 (Example data (self-written))
- **Task:** DOI sample.
- **Input:** Title „Attention Is All You Need“.
- **Prompt:**

```text
Discover doi metadata json one line.
```

- **Expected result:**

```text
metadata line with doi 10.48550/arXiv.1706.03762 or publisher doi.
```