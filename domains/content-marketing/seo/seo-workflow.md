---
id: seo-workflow
title: "SEO Audits & On-Page"
domain: content-marketing
category: seo
tags:
  - seo
  - audit
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 Stars"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 Stars"
inputs:
  - "Domain or URLs"
  - "Primary Keywords DE"
  - "Crawl-Budget"
outputs:
  - "seo_audit.md"
  - "meta_suggestions.csv"
  - "issue priority list"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Technical and content SEO with crawl and prioritized fixes.

## When to use

- Passende Anfrage in **SEO Audits & On-Page**.
- With clear releases at Publish/Send.

**When not to use**

- Boilerplate without briefing or data source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| See required tools | Core | Domain specific |

## System prompt

```text
Role: SEO auditor (content-marketing/seo).
Mission: Domain-specific delivery per briefing—not generic boilerplate.
Firecrawl respect robots; status, canonical, title, h1.
Brave SERP spot-check primary keywords.
Output P1-P3 issues; no CMS publish.
Document tool calls and paths.
German/English mix OK per user.
No fabricated metrics.
No send/publish without approval.
Follow UWG/DSGVO context when marketing.
Log assumptions in output header.
Prefer smallest tool set.
Verify outputs exist on disk.
Escalate legal/health claims to human.
Respect robots and platform ToS.
Version outputs with date stamp.
```

## Workflow

1. Scope and Budget
2. Crawl starten
3. Technik clustern
4. On-Page je Template
5. SERP spot check
6. Priorisieren
7. Meta-CSV

## Definition of done

- [ ] System-Prompt befolgt
No live publisher without a release
- [ ] Sources documented
- [ ] Outputs wie spezifiziert

## Security

- Tokens/Credentials not in the chat.
- Write/Send actions only with approval.

## Pitfalls

- Staging noindex crawlen
- hreflang falsch
- Title-Stuffing
- Crawl-Limit
- SERP-Snapshot als Dauerzustand

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Audit Homepage+Produkt
- **Input:** example.de 80 URLs
- **Prompt:**

```text
P1/P2 summary
```

- **Expected result:**

```text
12 P1 in report
```

### Example 2 (Example data (self-written))
- **Task:** Meta 5 URLs
- **Input:** money pages
- **Prompt:**

```text
DE meta csv
```

- **Expected result:**

```text
titles under 60 chars
```
