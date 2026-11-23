---
id: bibliothek-zotero-mcp-focus
title: "Bibliothek: Such-MCP mit Zotero"
domain: recherche-wissen
category: bibliothek-zotero
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
  - "MCP-Routing für Literatur"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Search/Fetch-MCPs** für Literaturmetadaten routen—Zotero bleibt Zielsystem, MCPs nur Discovery.

## Wann nutzen

- Setup vor bibliothek-zotero-workflow.
- Entscheidung Brave vs. Exa für Paper-Suche.

**Wann nicht**

- Vollständiger Zotero-Sync ohne Connector.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave/Exa | Find papers | Discovery |
| Firecrawl | Publisher meta | Verify |
| Zotero | Import target | User side |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Modus discover vs export.
2. MCP-Minimalset.
3. Suchstrategie.
4. Sample 1 DOI resolve.
5. routing.md.
6. Verweis workflow.
7. Token-Hinweis.

## Qualitätskriterien / Definition of Done

- [ ] Zotero als Ziel benannt
- [ ] ≤2 Search MCPs
- [ ] Kein PDF ohne Freigabe
- [ ] Handoff dokumentiert
- [ ] Queries geloggt

## Sicherheit & Freigaben

- API keys safe.
- No paywall breach.

## Fallstricke

- MCP overload.
- Wrong paper homonym.
- Publisher block firecrawl.
- Metadata ohne year.
- Zotero MCP assumed missing.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Setup Literatur-Agent.
- **Input:** Zotero desktop only.
- **Prompt:**

```text
Route discover via brave+firecrawl; export via bibliothek-zotero-workflow.
```

- **Erwartetes Ergebnis:**

```text
routing.md minimal MCPs; workflow link.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** DOI sample.
- **Input:** Title „Attention Is All You Need“.
- **Prompt:**

```text
Discover doi metadata json one line.
```

- **Erwartetes Ergebnis:**

```text
metadata line with doi 10.48550/arXiv.1706.03762 or publisher doi.
```