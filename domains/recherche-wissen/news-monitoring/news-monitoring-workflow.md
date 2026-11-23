---
id: news-monitoring-workflow
domain: recherche-wissen
title: "News-Monitoring und Alerts"
category: news-monitoring
tags:
  - news
  - rss
  - monitoring
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "News queries"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Article extract"
inputs:
  - "Themen und Keywords"
  - "Zeitfenster"
outputs:
  - "Digest MD"
  - "Priorisierte Alerts"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Themen überwachen**—RSS/News-Suche, Digest mit URLs, Severity für Alerts, keine Desinformation als Fakt.

## Wann nutzen

- Wettbewerber, Regulatorik, Sicherheitsadvisories.
- Täglicher oder wöchentlicher Digest.
- Vorstandsvorbereitung (informationsonly).

**Wann nicht**

- Insider-Handel auf News.
- Automatischer Tweet/Post ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search | News mode | Zeitnah |
| Firecrawl | Artikel | Verify |
| RSS/Atom CLI | Feeds | Optional local |
| grounded-citations | Discipline | Sources |

## System-Prompt / Instruktionen

```text
You monitor news topics and produce digests with sourced bullets—not trading or legal advice.

Inputs: watchlist topics[], keywords[], exclude terms[], window (24h|7d), output digest.md, alert_threshold (high for security|regulatory).

Per topic:
- Search news with time filter; dedupe same story from syndication.
- Fetch firecrawl on primary source not aggregator when possible.
- Classify: info|watch|alert with reason.

Digest sections:
- Executive highlights (max 5)
- By topic with [url] date headline one-liner
- Rumor/unverified section if only social sources—label clearly.

Alerts: only high severity to alert.md—user defines channels; agent does not email/slack without approval.

Exclude clickbait domains user lists.

No fabricated events.

Output: digest.md, alert.md optional, query_log.txt.

Timezone Europe/Vienna for dates unless user sets UTC.

Compare contradicting reports same event.

Do not automate purchases or trades on news.
Limit 25 items per digest unless user asks more.
```

## Arbeitsablauf

1. Watchlist und Excludes laden.
2. Pro Topic News-Suche.
3. Dedupe URLs.
4. Firecrawl Kernartikel.
5. Severity labeln.
6. digest.md schreiben.
7. alert.md bei high; Freigabe vor Versand.

## Qualitätskriterien / Definition of Done

- [ ] Jede Story mit URL und Datum
- [ ] Gerüchte gekennzeichnet
- [ ] Excludes respektiert
- [ ] Kein Auto-Post
- [ ] query_log vorhanden

## Sicherheit & Freigaben

- Kein Slack/Email ohne Freigabe.
- Market-moving info vertraulich behandeln.

## Fallstricke

- Aggregator statt Primary.
- Alte Story recycled.
- Keyword false positive.
- Duplicate Headlines.
- Zeitzone falsch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 7-Tage CVE Digest.
- **Input:** keywords CVE vendor produkt.
- **Prompt:**

```text
digest.md; alert any critical CVSS>=9; firecrawl primary sources.
```

- **Erwartetes Ergebnis:**

```text
digest.md; alert.md 0-n items; urls with dates.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Exclude rumor blog.
- **Input:** exclude list domain tabloid.example.
- **Prompt:**

```text
Apply exclude; no entries from tabloid.example.
```

- **Erwartetes Ergebnis:**

```text
digest has zero urls from excluded domain.
```