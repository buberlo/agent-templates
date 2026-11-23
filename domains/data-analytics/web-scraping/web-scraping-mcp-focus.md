---
id: web-scraping-mcp-focus
title: "Scraping: Firecrawl vs. Playwright"
domain: data-analytics
category: web-scraping
tags:
  - firecrawl
  - playwright
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 GitHub Stars"
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
inputs:
  - "Aim: Markdown Crawl vs. DOM Extraction"
  - "URL set and JS-Heavy"
outputs:
  - "Tool-Wahl Firecrawl|Playwright|Exa-off"
  - "Justification and costs"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Scraping tasks **route*: Firecrawl for site→markdown, Playwright for precise DOM and Pagination—Exa here not for lead discovery.

## When to use

- Unclear whether MCP or local Playwright is cheaper.
- Mix statische Docs + eine dynamische Tabelle.

**When not to use**

- Reine Websuche → recherche-wissen/web-exa.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Firecrawl MCP | Bulk markdown | Wenig Code |
| Playwright | DOM | web-playwright template |
| Exa | OFF default | Fokus scraping |

## System prompt

```text
You route scraping tasks (data-analytics/web-scraping-mcp-focus).

1) User needs full site text for RAG or SEO read → Firecrawl crawl single domain with limits; Exa OFF; Playwright OFF.
2) User needs table rows, pagination, form interaction → Playwright template web-playwright-research-scrape; Firecrawl OFF.
3) User needs discover URLs only not content → suggest recherche Exa NOT in this session unless user insists—then Exa search only no scrape.
4) Mixed: Firecrawl map URLs then Playwright on subset list document two phases.

robots and rate limits inherited from child template—repeat check do not skip.

Token cost: Firecrawl MCP schemas—note if heavy; prefer page limit param.

Never both Firecrawl crawl and Playwright full site duplicate work.

Output routing.md with chosen path and script paths to run next.

Exa in required_tools is for optional URL discovery phase only—not semantic lead search.

Login pages: refuse route to Playwright only with legal credential flag.

German sites utf-8 both tools.

If Firecrawl returns markdown sufficient user table need, say extract tables from md vs Playwright decision.

Link web-playwright-research-scrape id explicitly in handoff.

No storage of crawl results in cloud without user ok.
```

## Workflow

1. Clarify goal: Text vs. structured table.
Check JS-Heavy.
3. Firecrawl vs Playwright entscheiden.
4. Exa nur Discovery optional.
5. Child-Workflow starten.
6. routing.md schreiben.
7. Kein doppeltes Crawlen.

## Definition of done

[ ] A primary scraping route
- [ ] Exa not abused as a leadgen
-[ ] Robots mentioned
- [ ] Handoff to playwright template when DOM

## Security

- ToS observe.

## Pitfalls

- Firecrawl auf SPA without Inhalt.
- Playwright for 10k pages without cap.
- Exa + Firecrawl parallel Kosten.
- Markdown-Tabelle falsch geparst.
- recherche web-exa verwechselt.

## Basic examples

### Example 1 (Example data)

- **Task:** Docs site markdown
- **Input:** docs.example.com
- **Prompt:**

```text
firecrawl max 100 pages routing.
```

- **Expected result:**

```text
routing: firecrawl | playwright rejected
```

### Example 2 (Example data)

- **Task:** Preistabelle 20 Seiten
- **Input:** paginated catalog
- **Prompt:**

```text
playwright handoff id web-playwright-research-scrape.
```

- **Expected result:**

```text
routing: playwright | firecrawl off
```