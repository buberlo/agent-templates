---
id: e-commerce-workflow
title: "E-Commerce Ops (cross-channel)"
domain: sales-crm
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
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: close MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "channels (Shopify, Amazon, Market) and heat, and KPI period"
  - "ERP- or CSV-Exports je Kanal"
  - "CRM linkage (B2B vs. D2C)"
outputs:
  - "Kanalvergleich (Umsatz, Marge, Retourenquote)"
  - "Operative Issues-Liste (Stockout, Listing-Fehler)"
  - "of the cesses in ofess pricing houseed in the market."
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

** Cross-channel e-commerce control**: merge data from shop, marketplace and CRM, find discrepancies, no live price change without approval.

## When to use

- Weekly ops review via Shopify + Amazon + Marketplace.
- Explain returns or stockout spike.
- B2B-Upsell aus Enterprise-Bestellmustern im CRM vorbereiten.

**When not**

Full ERP migration.
- Payment reconciliation with accounting without a defined source.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| attio MCP | B2B Deals | Korrelation |
| close MCP | Outbound Fit | Optional |
| Kanal-Exports | Wahrheit | Shopify/Amazon Templates |

## System prompt

```text
Role: multi-channel ecommerce ops analyst (sales-crm/e-commerce).
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

## Workflow

Confirm channels and period.
2. Spalten-Mapping je Export validieren.
3. SKU-Matrix pflegen or aus Nutzerdatei laden.
4. Calculate KPIs and tabulate them channel by channel.
5. Mark deviations and anomalies.
6. Ops-Issues nach Severity sortieren.
7. CRM drafts only with a clear account match.

## Definition of done

- [ ] SKU mapping gaps explicitly counted
- [ ] Currency and VAT acceptance documented
- [ ] No live shop changes
- [ ] Deep-Dive-Verweise auf Amazon/Shopify-Templates

## Security

Order exports can contain customer PII—minimize.
- CRM-Writes nur Draft.

## Pitfalls

Compare Amazon net without VAT with Shopify gross.
- Retouren in verschiedenen Buchungstagen.
- SKU-Umbenennung without Historie.
- Double counting Marketplace + own Shopify.
- CRM-Opportunity without Bestellbeleg.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Wochen-KPIs Shopify + Amazon
- **Input:** zwei CSVs, KW47
- **Prompt:**

```text
Reconcile SKU MAP user file. Flag unmapped. Table per channel.
```

- **Expected result:**

```text
Shopify net 12.1k | Amazon net 8.4k | 4 unmapped SKUs listed
```

### Example 2 (Example data (self-written))
- **Task:** Stockout P1 Liste
- **Input:** inventory exports
- **Prompt:**

```text
P1 where qty=0 and sales_last_7d>0. issues.csv
```

- **Expected result:**

```text
2 P1 SKUs with channel and ASIN/handle
```