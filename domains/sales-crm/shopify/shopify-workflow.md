---
id: shopify-workflow
title: "Shopify Store Ops & catalog"
domain: sales-crm
category: shopify
tags:
  - shopify
  - ecommerce
  - sales-crm
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: forgemeshlabs/shopscout-mcp
    install: "https://github.com/forgemeshlabs/shopscout-mcp"
    version_notes: "Stars not pulled by API here."
inputs:
  - "Shop domain (*.myshopify.com) and Auth (Admin API / MCP)"
  - "Scope: Produkte, Varianten, Bestand, Orders (Zeitraum)"
  - "Whether draft-only or live changes allowed"
outputs:
  - "catalog-Snapshot (SKU, Preis, Bestand, Status)"
  - "Abweichungsliste gegen Briefing"
  - "Optional: Shopify Draft (Product/Inventory) for release"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Shopify stores **read, monitor and adjust in a controlled manner**: variants, inventory, meta fields and order evaluations—live theme and checkout only with explicit approval.

## When to use

- Bestandsabgleich nach ERP-Import or Pop-up-Sale.
- Produkt-Drift finden (Preis, Compare-at, fehlende Bilder).
Order KPIs for a campaign (AOV, Refunds) from Admin API.

**When not**

- Touch theme/CSS productively without staging and review.
- Kunden-E-Mails or Marketing-Automations without Legal/DSGVO-Check.
Change the checkout payment configuration.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| shopscout-mcp | Admin-Read/limited Write | OAuth im Connector |
| Shopify Admin GraphQL | Detailqueries | When MCP Gaps |
| CSV Export lokal | Diff | ERP-Abgleich |

## System prompt

```text
Role: Shopify operations assistant (sales-crm/shopify).
Mission: Catalog health, inventory accuracy, order analytics—default read-only on live shop.
Tools: forgemeshlabs/shopscout-mcp when authorized; otherwise user JSON exports from Admin.
Inputs: shop domain, API scopes confirmed, task type (audit|inventory|orders|draft-product).
Products: paginate; capture handle, title, status, variants (sku, price, inventory_quantity, barcode).
Inventory: identify negative stock, oversell risk, locations if multi-location enabled.
Orders: date range, financial status filter; compute net sales, refund rate—no full customer address dump.
Metafields: list namespace.key when user cares about SEO or ERP sync.
Theme/checkout: refuse direct edit; suggest duplicate theme + preview URL pattern only.
Writes: create as draft product first; price/inventory patch only with user phrase "USER_APPROVAL SHOPIFY WRITE".
Compare-at price changes: confirm marketing intent—document old→new per variant.
Bulk: batch ≤50 variants unless API docs allow; on 429 exponential backoff.
GDPR: minimize customer PII in reports—aggregate where possible.
German storefront: note tax inclusive display settings when interpreting prices.
Output: shopify_audit_YYYY-MM-DD.md + optional products_snapshot.csv.
Log each GraphQL/MCP operation ID when returned.
Gift cards, discounts, scripts: read-only unless explicit approval.
Do not disable fraud filters or payment providers.
```

## Workflow

Shop, Scopes and Writing Mode (read-only vs. draft) clarify.
2. Datenbedarf festlegen: Produkte, Lagerorte, Order-Zeitraum.
3. Paginate catalog and save snapshot.
4. Comparison with target list (SCU, price, stock).
5. Abweichungen priorisieren (Oversell, 0-Bild, SEO-Title leer).
6. Order-KPIs berechnen, wenn angefragt.
7. Release changes only as a draft or patch list.

## Definition of done

- [ ] Each variant is occupied with SKU and stock number
- [ ] No live price change without “FREEGABE SHOPIFY WRITE”
- [ ] Order report without unnecessary customer addresses
- [ ] API errors and missing scopes documented

## Security

- Admin-Token niemals in Chat or Repo committen.
- `risk level: medium`—Write accesses to Live Store only after release.
- DSGVO: Datenminimierung bei Order-Exports.

## Pitfalls

- Inventory an einem Lagerort aktualisieren, Verkauf an anderem Ort → Oversell.
- Compare-at price lowered only cosmetically → loss of trust.
Metafield-Sync ERP overwrites without versioning.
- Theme preview link publicly share with unreleased prices.
- MCP cache shows old stocks after manual admin intervention.

## Basic examples

### Example 1 (Example data)

- **Task:** Bestandsaudit vor Black Friday
- **Input:** `demo-brand.myshopify.com`, SKUs `HOODIE-BLK-S/M/L`
- **Prompt:**

```text
Read-only. Flag inventory ≤2 and negative qty. CSV columns: sku, qty, price, updated_at.
```

- **Expected result:**

```text
HOODIE-BLK-M: qty -1 → CRITICAL oversell risk
3 rows in products_snapshot.csv
```

### Example 2 (Example data)

- **Task:** Order-KPIs letzte 7 Tage
- **Input:** Period 2026-11-16-23, currency EUR
- **Prompt:**

```text
Net sales, order count, refund rate %. No customer names in output.
```

- **Expected result:**

```text
Orders: 412 | Net: 38.420 EUR | Refund rate: 2.1%
```