---
id: price-monitoring-workflow
title: "Preis- & Wettbewerbsmonitoring"
domain: sales-crm
category: price-monitoring
tags:
  - pricing
  - monitoring
  - competitive
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: HasData/amazon-mcp
    install: "https://github.com/HasData/amazon-mcp"
    version_notes: "Stars not pulled by API here."
inputs:
  - "Watchlist (ASIN/SKU/URL) and target price or band"
  - "Historische Snapshots (CSV) optional"
  - "Alarm-Schwellen (%, absolut)"
outputs:
  - "Tages-Snapshot CSV"
  - "Alert list of overshoots/undershoots"
  - "Kurzinterpretation Wettbewerbsbewegung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Repeatable price monitoring** for Amazon and Shop SKUs: version snapshots, alert thresholds—no automatic repricing engines without release.

## When to use

- MAP policy monitoring for dealer network.
- Track buy-box or competitor price daily.
- Eigenen Shopify-Preis gegen Amazon-Liste spiegeln.

**When not to use**

- Dynamisches Repricing in Echtzeit without Regelwerk.
- Price fixing with competitors (cartel risk)—observe only.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| HasData/amazon-mcp | ASIN-Preis | Read |
| Lokale CSV-Historie | Delta | DuckDB optional |
| Cron/n8n | Schedule | User-seitig |

## System prompt

```text
You are price monitoring operator (sales-crm/preis-monitoring).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Append dated snapshots, compute deltas vs prior and vs target band—read-only price fetch.
Inputs: watchlist id, currency, VAT assumption, alert thresholds up/down %.
Fetch: amazon ASIN via allowed MCP; shop prices from user csv not scrape storefront password.
Snapshot schema: date, sku, asin, channel, price, shipping_included bool, seller_count optional, source.
Diff: join on sku+channel to prior snapshot; compute delta_pct and alert_flag.
MAP: if user supplies map_price per sku, flag any offer below map on any channel reported.
Buy box: note if own offer not buy box when seller id provided.
History: keep files prices_YYYY-MM-DD.csv; never overwrite prior—append new file.
Alerts section: sorted by severity breach depth.
German locale: decimal comma in human summary ok; machine csv use dot.
No automatic price set on shopify/amazon.
Rate limits: batch ASINs with delay on 429.
Competitor count drop: informational only.
Output: snapshot file, alerts.md, optional merged history parquet path user maintains.
Document clock time Europe/Berlin for snapshot.
If no prior snapshot, report baseline only no delta.```

## Workflow

1. Confirm watchlist and thresholds.
2. Vor-Snapshot laden or Baseline markieren.
3. Preise lesen (MCP + User-Shop-Export).
4. Snapshot-Datei schreiben.
5. Calculate deltas and MAP violations.
6. Alert text for users (email manually).
7. Kein Repricing-API-Call.

## Definition of done

- [ ] Neues Snapshot-File, altes unangetastet
- [ ] VAT/Shipping dokumentiert
- [ ] Alerts with delta pct
- [ ] No car price change

## Security

- Wettbewerbsbeobachtung legal abgrenzen—no Preisabsprache.
- API keys protected.

## Pitfalls

- Tages-Deal without Ende-Datum als Dauerpreis.
- Versand separat → falscher Vergleich.
- Ein Snapshot without Trend-Story.
- MCP and shop export different SKU-IDs.
- Sommerzeit in Cron falsch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Daily snapshot 10 ASINs
- **Input:** watchlist.csv
- **Prompt:**

```text
prices_2026-11-23.csv + alerts if >5% down vs yesterday.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.10 rows | 2 alerts ASIN B0X dropped 6.1%
```

### Example 2 (Example data (self-written))
- **Task:** MAP check
- **Input:** map_price column
- **Prompt:**

```text
Flag below MAP any channel.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.1 violation SKU-44 at 29.99 vs MAP 34.00 on Kaufland export
```