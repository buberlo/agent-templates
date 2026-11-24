---
id: news-monitoring-workflow
title: "News Monitoring and Alerts"
domain: research-knowledge
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
  - "Themes and Keywords"
  - "Zeitfenster"
outputs:
  - "Digest MD"
  - "Priorisierte Alerts"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Monitor topics—RSS/News search, digest with URLs, severity for alerts, no disinformation as fact.

## When to use

- Wettbewerber, Regulatorik, Sicherheitsadvisories.
Daily or weekly digest.
- Vorstandsvorbereitung (informationsonly).

**When not**

- Insider-Handel auf News.
- Automatic tweet/post without release.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search | News mode | Zeitnah |
| Firecrawl | Artikel | Verify |
| RSS/Atom CLI | Feeds | Optional local |
| grounded-citations | Discipline | Sources |

## System prompt

```text
You monitor news topics and produce digests with sourced bullets—not trading or legal advice.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Limit 25 items per digest unless user asks more.```

## Workflow

1. Watchlist and Excludes.
2. Pro Topic News-Suche.
3. Dedupe URLs.
4. Firecrawl Kernartikel.
5. Severity labeln.
6. digest.md schreiben.
7. alert.md at high; Release before shipment.

## Definition of done

- [ ] Every story with URL and date
- [ ] Rumors marked
- [ ] Excludes respektiert
- [ ] Kein Auto-Post
- [ ] query_log vorhanden

## Security

- No Slack/Email without release.
- Market-moving info vertraulich behandeln.

## Pitfalls

- Aggregator statt Primary.
- Alte Story recycled.
- Keyword false positive.
- Duplicate Headlines.
- Zeitzone falsch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 7-Tage CVE Digest.
- **Input:** keywords CVE vendor produkt.
- **Prompt:**

```text
digest.md; alert any critical CVSS>=9; firecrawl primary sources.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.digest.md; alert.md 0-n items; urls with dates.
```

### Example 2 (Example data (self-written))
- **Task:** Exclude rumor blog.
- **Input:** exclude list domain tabloid.example.
- **Prompt:**

```text
Apply exclude; no entries from tabloid.example.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.digest has zero urls from excluded domain.
```