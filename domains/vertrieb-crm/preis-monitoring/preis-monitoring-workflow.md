---
id: preis-monitoring-workflow
title: "Preis- & Wettbewerbsmonitoring"
domain: vertrieb-crm
category: preis-monitoring
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
    version_notes: "Stars hier nicht per API gezogen."
inputs:
  - "Watchlist (ASIN/SKU/URL) und Zielpreis oder Band"
  - "Historische Snapshots (CSV) optional"
  - "Alarm-Schwellen (%, absolut)"
outputs:
  - "Tages-Snapshot CSV"
  - "Alarmliste Über-/Unterschreitungen"
  - "Kurzinterpretation Wettbewerbsbewegung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Wiederholbares Preis-Monitoring** für Amazon und Shop-SKUs: Snapshots versionieren, Schwellen alarmieren—keine automatische Repricing-Engines ohne Freigabe.

## Wann nutzen

- MAP-Policy-Überwachung für Händlernetz.
- Buy-Box- oder Wettbewerberpreis täglich tracken.
- Eigenen Shopify-Preis gegen Amazon-Liste spiegeln.

**Wann nicht**

- Dynamisches Repricing in Echtzeit ohne Regelwerk.
- Preisfixierung mit Wettbewerbern (Kartellrisiko)—nur beobachten.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| HasData/amazon-mcp | ASIN-Preis | Read |
| Lokale CSV-Historie | Delta | DuckDB optional |
| Cron/n8n | Schedule | Nutzer-seitig |

## System-Prompt / Instruktionen

```text
Role: price monitoring operator (vertrieb-crm/preis-monitoring).
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
If no prior snapshot, report baseline only no delta.
```

## Arbeitsablauf

1. Watchlist und Schwellen bestätigen.
2. Vor-Snapshot laden oder Baseline markieren.
3. Preise lesen (MCP + Nutzer-Shop-Export).
4. Snapshot-Datei schreiben.
5. Deltas und MAP-Verletzungen berechnen.
6. Alarmtext für Nutzer (E-Mail manuell).
7. Kein Repricing-API-Call.

## Qualitätskriterien / Definition of Done

- [ ] Neues Snapshot-File, altes unangetastet
- [ ] VAT/Shipping dokumentiert
- [ ] Alerts mit delta_pct
- [ ] Keine Auto-Preisänderung

## Sicherheit & Freigaben

- Wettbewerbsbeobachtung legal abgrenzen—keine Preisabsprache.
- API-Keys geschützt.

## Fallstricke

- Tages-Deal ohne Ende-Datum als Dauerpreis.
- Versand separat → falscher Vergleich.
- Ein Snapshot ohne Trend-Story.
- MCP und Shop-Export unterschiedliche SKU-IDs.
- Sommerzeit in Cron falsch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Daily snapshot 10 ASINs
- **Input:** watchlist.csv
- **Prompt:**

```text
prices_2026-11-23.csv + alerts if >5% down vs yesterday.
```

- **Erwartetes Ergebnis:**

```text
10 rows | 2 alerts ASIN B0X dropped 6.1%
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** MAP check
- **Input:** map_price column
- **Prompt:**

```text
Flag below MAP any channel.
```

- **Erwartetes Ergebnis:**

```text
1 violation SKU-44 at 29.99 vs MAP 34.00 on Kaufland export
```