---
id: web-research-mcp-focus
title: "Web research: MCP-Fokus"
domain: research-knowledge
category: web-research
tags:
  - brave
  - exa
  - firecrawl
  - search
target_agents:
  - grokbot
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Websuche API"
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "Neural search"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Fetch/extract"
inputs:
  - "Recherchefrage"
  - "Erlaubte MCPs"
outputs:
  - "Minimaler MCP-Satz"
  - "Suchstrategie"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Search MCPs Targeted**—Brave/Exa/Tavily for Discovery, Firecrawl for Content—Playwright not as a default scraper.

## When to use

- Agent setup for web research.
- Token-Budget durch MCP-Minimalismus.
- Strategie vor Briefing-Lauf (web-exa-perplexity-briefing).

**When not**

- Login walls or JS apps (Playwright separately with sharing).
- Full briefing (own templates).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Breite Suche | API-stabil |
| Exa MCP | Semantische Treffer | Tiefe |
| Firecrawl MCP | Extract | Volltext |
| Playwright MCP | Last resort | Teuer |

## System prompt

```text
You configure web research MCPs with minimal active set per task.

Default stack: ONE search MCP + Firecrawl extract—not Playwright unless user proves need (login, SPA).

Flow:
1) Search: brave or exa with tight query; max 8 results first pass.
2) Fetch: firecrawl on top 3-5 URLs; never fetch all results.
3) Cite: title, url, accessed date in notes.

Disable unused MCPs to reduce context overhead (known 60k+ token issue with full catalogs).

Playwright: only when firecrawl returns empty and user approves browser session.

Rate limits: backoff; log failures.

No credentials in search queries.

Output: enabled MCP list, search plan, estimated calls.

Never paste paywalled full text without license.

Regional: DE queries add site: or language hint when user asks.

Do not enable Tavily+Brave+Exa all at once unless comparison study requested.

Log query strings for reproducibility.

Refuse scraping disallowed by robots.txt when firecrawl reports block.
Cache fetch results in thread to avoid duplicate firecrawl on same url.
```

## Workflow

1. Frage in Suchstrings zerlegen.
2. Choose a search MCP.
3. Firecrawl for top URLs.
4. Playwright only after release.
5. MCP-Liste dokumentieren.
6. Quellen-Snippets strukturieren.
7. Presented to briefing template.

## Definition of done

- [ ] ≤2 aktive Search-MCPs
- [ ] Firecrawl nur auf Kurzliste
- [ ] Queries geloggt
- [ ] Playwright justified when used
- [ ] No Credentials in Queries

## Security

- API keys not in chat.
No login automation without approval.
- publicly label source URLs.

## Pitfalls

- Alle MCPs an → Token-Explosion.
- Playwright als Default-Scraper.
- Duplicate Firecrawl Calls.
- Snippets without URL.
- Paywall-Volltext kopiert.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Vendor-Vergleich EU Hosting.
- **Input:** 3 Vendor-Namen.
- **Prompt:**

```text
Plan: Brave search + Firecrawl top 3 each; no Playwright; minimal MCPs.
```

- **Expected result:**

```text
plan.md: MCPs brave+firecrawl; 9 fetches max; queries listed.
```

### Example 2 (Example data (self-written))
- **Task:** SPA-Dashboard Recherche.
- **Input:** JS-only pricing page.
- **Prompt:**

```text
Firecrawl failed; request Playwright approval with scoped URL only.
```

- **Expected result:**

```text
Stopped at firecrawl error; Playwright pending user yes; single URL scope.
```