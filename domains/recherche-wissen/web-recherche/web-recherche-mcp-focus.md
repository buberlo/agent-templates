---
id: web-recherche-mcp-focus
title: "Web-Recherche: MCP-Fokus"
domain: recherche-wissen
category: web-recherche
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
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Such-MCPs gezielt kombinieren**—Brave/Exa/Tavily für Discovery, Firecrawl für Inhalt—Playwright nicht als Default-Scraper.

## Wann nutzen

- Agenten-Setup für Web-Recherche.
- Token-Budget durch MCP-Minimalismus.
- Strategie vor Briefing-Lauf (web-exa-perplexity-briefing).

**Wann nicht**

- Login-walls oder JS-Apps (Playwright separat mit Freigabe).
- Vollständiges Briefing (eigene Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | Breite Suche | API-stabil |
| Exa MCP | Semantische Treffer | Tiefe |
| Firecrawl MCP | Extract | Volltext |
| Playwright MCP | Last resort | Teuer |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Frage in Suchstrings zerlegen.
2. Ein Search-MCP wählen.
3. Firecrawl für Top-URLs.
4. Playwright nur nach Freigabe.
5. MCP-Liste dokumentieren.
6. Quellen-Snippets strukturieren.
7. An Briefing-Template übergeben.

## Qualitätskriterien / Definition of Done

- [ ] ≤2 aktive Search-MCPs
- [ ] Firecrawl nur auf Kurzliste
- [ ] Queries geloggt
- [ ] Playwright begründet wenn genutzt
- [ ] Keine Credentials in Queries

## Sicherheit & Freigaben

- API-Keys nicht im Chat.
- Kein Login-Automation ohne Freigabe.
- Quellen-URLs öffentlich kennzeichnen.

## Fallstricke

- Alle MCPs an → Token-Explosion.
- Playwright als Default-Scraper.
- Duplicate Firecrawl Calls.
- Snippets ohne URL.
- Paywall-Volltext kopiert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Vendor-Vergleich EU Hosting.
- **Input:** 3 Vendor-Namen.
- **Prompt:**

```text
Plan: Brave search + Firecrawl top 3 each; no Playwright; minimal MCPs.
```

- **Erwartetes Ergebnis:**

```text
plan.md: MCPs brave+firecrawl; 9 fetches max; queries listed.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** SPA-Dashboard Recherche.
- **Input:** JS-only pricing page.
- **Prompt:**

```text
Firecrawl failed; request Playwright approval with scoped URL only.
```

- **Erwartetes Ergebnis:**

```text
Stopped at firecrawl error; Playwright pending user yes; single URL scope.
```