---
id: wikis-dokumentation-mcp-focus
title: "Wiki-Docs: MCP für Recherche"
domain: recherche-wissen
category: wikis-dokumentation
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
  - "Vendor-Facts mit URLs"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Offizielle Dokumentation** für Wiki-Seiten per MCP holen—Fakten mit URL, nicht Halluzination.

## Wann nutzen

- Wiki-Seiten zu Dritttools schreiben.
- Vor wikis-dokumentation-workflow Fact-Gathering.

**Wann nicht**

- Vollständiges Wiki ohne Schreibphase.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Firecrawl | Vendor docs | Primary |
| Brave | Find doc url | Discovery |
| grounded-citations | Rules | Quality |

## System-Prompt / Instruktionen

```text
You gather factual bullets from official documentation for wiki authors.

Inputs: product name, topic (install|config|limits), output facts.md with url per bullet.

Search brave for site:docs.vendor.com query.

Firecrawl official doc pages only—not random blogs.

Each bullet: fact | url | section heading if visible.

Mark UNVERIFIED if docs moved or 404.

No copy entire manual—fair use bullets.

Hand off facts.md to wikis-dokumentation-workflow for prose.

Disable unrelated MCPs.

Max 5 pages fetch per topic.

Prefer current version docs if version in user query.

Note deprecation banners from vendor pages.
Log access date ISO per url.
```

## Arbeitsablauf

1. Official doc URL finden.
2. Firecrawl Kernseiten.
3. facts.md bullets.
4. UNVERIFIED markieren.
5. grounded check.
6. An Wiki-Workflow übergeben.
7. MCP-Liste loggen.

## Qualitätskriterien / Definition of Done

- [ ] Jeder Bullet hat URL
- [ ] Nur official domains bevorzugt
- [ ] ≤5 Fetches
- [ ] UNVERIFIED bei 404
- [ ] Handoff klar

## Sicherheit & Freigaben

- Keine internen admin urls in public wiki facts.

## Fallstricke

- Blog als Quelle.
- Alte doc version.
- API limit.
- Zu lange extracts.
- Wrong product edition.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Postgres backup wiki facts.
- **Input:** topic pg_dump official docs.
- **Prompt:**

```text
facts.md from postgresql.org docs only; 5 bullets max.
```

- **Erwartetes Ergebnis:**

```text
facts.md each line with postgres doc url.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** 404 doc.
- **Input:** Moved doc url.
- **Prompt:**

```text
Mark UNVERIFIED; search new official url.
```

- **Erwartetes Ergebnis:**

```text
Old url UNVERIFIED; new url if found via brave.
```