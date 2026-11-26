---
id: wikis-documentation-mcp-focus
title: "Wiki-Docs: MCP for Research"
domain: research-knowledge
category: wikis-documentation
tags:
  - wiki
  - mcp
  - firecrawl
target_agents:
  - generic-mcp-agents
  - grokbot
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Official docs fetch"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Find docs"
inputs:
  - "Doc-Thema"
outputs:
  - "Vendor facts with URLs"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Official documentation** for getting wiki pages via MCP—facts with URL, not hallucination.

## When to use

- Write wiki pages for third-party tools.
- Fact-gathering before wikis-documentation-workflow.

**When not**

- Full wiki without writing phase.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Firecrawl | Vendor docs | Primary |
| Brave | Find doc url | Discovery |
| grounded-citations | Rules | Quality |

## System prompt

```text
You gather factual bullets from official documentation for wiki authors.

Inputs: product name, topic (install|config|limits), output facts.md with url per bullet.

Search brave for site:docs.vendor.com query.

Firecrawl official doc pages only—not random blogs.

Each bullet: fact | url | section heading if visible.

Mark UNVERIFIED if docs moved or 404.

No copy entire manual—fair use bullets.

Hand off facts.md to wikis-documentation-workflow for prose.

Disable unrelated MCPs.

Max 5 pages fetch per topic.

Prefer current version docs if version in user query.

Note deprecation banners from vendor pages.
Log access date ISO per url.
```

## Workflow

1. Official doc URL finden.
2. Firecrawl Kernseiten.
3. facts.md bullets.
4. UNVERIFIED markieren.
5. grounded check.
6. Handed over to wiki workflow.
7. Log the MCP list.

## Definition of done

- [ ] Jeder Bullet hat URL
- [ ] Prefer official domains only
- [ ] ≤5 Fetches
- [ ] UNVERIFIED on 404
- [ ] Handoff klar

## Security

- No internen admin urls in public wiki facts.

## Pitfalls

Blog as a source.
- Alte doc version.
- API limit.
- Zu lange extracts.
- Wrong product edition.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Postgres backup wiki facts.
- **Input:** topic pg_dump official docs.
- **Prompt:**

```text
facts.md from postgresql.org docs only; 5 bullets max.
```

- **Expected result:**

```text
facts.md each line with postgres doc url.
```

### Example 2 (Example data (self-written))
- **Task:** 404 doc.
- **Input:** Moved doc url.
- **Prompt:**

```text
Mark UNVERIFIED; search new official url.
```

- **Expected result:**

```text
Old url UNVERIFIED; new url if found via brave.
```