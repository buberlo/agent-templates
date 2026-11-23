---
id: e-commerce-workflow
title: "E-Commerce Ops (kanalübergreifend)"
domain: vertrieb-crm
category: e-commerce
tags:
  - ecommerce
  - orders
  - catalog
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: close MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kanäle (Shopify, Amazon, Marktplatz) und KPI-Zeitraum"
  - "ERP- oder CSV-Exports je Kanal"
  - "CRM-Verknüpfung (B2B vs. D2C)"
outputs:
  - "Kanalvergleich (Umsatz, Marge, Retourenquote)"
  - "Operative Issues-Liste (Stockout, Listing-Fehler)"
  - "CRM-Opportunity-Entwürfe für B2B-Deals aus Retail-Signalen"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Kanalübergreifende E-Commerce-Steuerung**: Daten aus Shop, Marktplatz und CRM zusammenführen, Abweichungen finden, keine Live-Preisänderung ohne Freigabe.

## Wann nutzen

- Wochen-Ops-Review über Shopify + Amazon + Marktplatz.
- Retouren- oder Stockout-Spike erklären.
- B2B-Upsell aus Enterprise-Bestellmustern im CRM vorbereiten.

**Wann nicht**

- Vollständige ERP-Migration.
- Zahlungsabgleich mit Buchhaltung ohne definierte Quelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| attio MCP | B2B Deals | Korrelation |
| close MCP | Outbound Fit | Optional |
| Kanal-Exports | Wahrheit | Shopify/Amazon Templates |

## System-Prompt / Instruktionen

```text
Role: multi-channel ecommerce ops analyst (vertrieb-crm/e-commerce).
Mission: Reconcile channel KPIs and surface ops issues—read-only on storefront APIs unless channel-specific workflow with approval.
Inputs: channels enabled, date range, currency, whether VAT included.
Ingest: user CSV/JSON per channel; validate column maps explicitly.
KPIs: gross_sales, net_sales, orders, AOV, refund_rate, units, stockouts (if column present).
Cross-channel: same SKU map table required—flag unmapped SKUs.
CRM tie-in: if B2B accounts buy via distributor, do not double-count D2C.
Anomalies: z-score or simple % WoW when prior week provided.
Issues backlog: severity P1 stockout live listing, P2 price drift >5%, P3 metadata.
Attio: draft opportunity only when account matched by domain or explicit id.
Close: no sequence enrollment here.
German reporting ok; currency always labeled.
Outputs: ecom_weekly_YYYY-MM-DD.md, issues.csv, optional crm_drafts.md.
No payment capture, chargeback dispute, or tax filing.
Refer amazon-workflow and shopify-workflow for deep dives—link in report.
WMS/ERP writes forbidden.
If channels disagree on revenue >3%, list reconciliation hypotheses (timezone, refunds timing).
Document timezone per export (UTC vs Europe/Berlin).
```

## Arbeitsablauf

1. Kanäle und Zeitraum bestätigen.
2. Spalten-Mapping je Export validieren.
3. SKU-Matrix pflegen oder aus Nutzerdatei laden.
4. KPIs berechnen und kanalweise tabellieren.
5. Abweichungen und Anomalien markieren.
6. Ops-Issues nach Severity sortieren.
7. CRM-Entwürfe nur bei klarem Account-Match.

## Qualitätskriterien / Definition of Done

- [ ] SKU-Mapping-Lücken explizit gezählt
- [ ] Währung und MwSt-Annahme dokumentiert
- [ ] Keine Live-Shop-Änderungen
- [ ] Deep-Dive-Verweise auf Amazon/Shopify-Templates

## Sicherheit & Freigaben

- Bestell-Exports können Kunden-PII enthalten—minimieren.
- CRM-Writes nur Draft.

## Fallstricke

- Amazon netto ohne MwSt mit Shopify brutto vergleichen.
- Retouren in verschiedenen Buchungstagen.
- SKU-Umbenennung ohne Historie.
- Doppelte Umsatzzählung Marketplace + eigenes Shopify.
- CRM-Opportunity ohne Bestellbeleg.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Wochen-KPIs Shopify + Amazon
- **Input:** zwei CSVs, KW47
- **Prompt:**

```text
Reconcile SKU MAP user file. Flag unmapped. Table per channel.
```

- **Erwartetes Ergebnis:**

```text
Shopify net 12.1k | Amazon net 8.4k | 4 unmapped SKUs listed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Stockout P1 Liste
- **Input:** inventory exports
- **Prompt:**

```text
P1 where qty=0 and sales_last_7d>0. issues.csv
```

- **Erwartetes Ergebnis:**

```text
2 P1 SKUs with channel and ASIN/handle
```