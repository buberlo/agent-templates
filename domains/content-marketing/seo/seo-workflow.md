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
  - "Domain oder URLs"
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

## Zweck

Technisches und inhaltliches SEO mit Crawl und priorisierten Fixes.

## Wann nutzen

- Passende Anfrage in **SEO Audits & On-Page**.
- Mit klaren Freigaben bei Publish/Send.

**Wann nicht**

- Boilerplate ohne Briefing oder ohne Datenquelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Siehe required_tools | Kern | Domänenspezifisch |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Scope und Budget
2. Crawl starten
3. Technik clustern
4. On-Page je Template
5. SERP-Stichprobe
6. Priorisieren
7. Meta-CSV

## Qualitätskriterien / Definition of Done

- [ ] System-Prompt befolgt
- [ ] Kein Live-Publish ohne Freigabe
- [ ] Quellen dokumentiert
- [ ] Outputs wie spezifiziert

## Sicherheit & Freigaben

- Tokens/Credentials nicht im Chat.
- Schreib-/Send-Aktionen nur mit Freigabe.

## Fallstricke

- Staging noindex crawlen
- hreflang falsch
- Title-Stuffing
- Crawl-Limit
- SERP-Snapshot als Dauerzustand

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Audit Homepage+Produkt
- **Input:** example.de 80 URLs
- **Prompt:**

```text
P1/P2 summary
```

- **Erwartetes Ergebnis:**

```text
12 P1 in report
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Meta 5 URLs
- **Input:** money pages
- **Prompt:**

```text
DE meta csv
```

- **Erwartetes Ergebnis:**

```text
titles under 60 chars
```
