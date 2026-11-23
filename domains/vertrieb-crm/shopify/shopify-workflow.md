---
id: shopify-workflow
title: "Shopify Store Ops & Katalog"
domain: vertrieb-crm
category: shopify
tags:
  - shopify
  - ecommerce
  - vertrieb-crm
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: forgemeshlabs/shopscout-mcp
    install: "https://github.com/forgemeshlabs/shopscout-mcp"
    version_notes: "Stars hier nicht per API gezogen."
inputs:
  - "Shop-Domain (*.myshopify.com) und Auth (Admin API / MCP)"
  - "Scope: Produkte, Varianten, Bestand, Orders (Zeitraum)"
  - "Ob Draft-only oder Live-Änderungen erlaubt"
outputs:
  - "Katalog-Snapshot (SKU, Preis, Bestand, Status)"
  - "Abweichungsliste gegen Briefing"
  - "Optional: Shopify-Entwurf (Product/Inventory) zur Freigabe"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Shopify-Shops **lesen, überwachen und kontrolliert anpassen**: Varianten, Inventory, Metafelder und Order-Auswertungen—Live-Theme und Checkout nur mit expliziter Freigabe.

## Wann nutzen

- Bestandsabgleich nach ERP-Import oder Pop-up-Sale.
- Produkt-Drift finden (Preis, Compare-at, fehlende Bilder).
- Order-KPIs für eine Kampagne (AOV, Refunds) aus Admin API.

**Wann nicht**

- Theme/CSS produktiv anfassen ohne Staging und Review.
- Kunden-E-Mails oder Marketing-Automations ohne Legal/DSGVO-Check.
- Checkout-Zahlungskonfiguration ändern.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| shopscout-mcp | Admin-Read/limited Write | OAuth im Connector |
| Shopify Admin GraphQL | Detailqueries | Wenn MCP-Lücken |
| CSV Export lokal | Diff | ERP-Abgleich |

## System-Prompt / Instruktionen

```text
Role: Shopify operations assistant (vertrieb-crm/shopify).
Mission: Catalog health, inventory accuracy, order analytics—default read-only on live shop.
Tools: forgemeshlabs/shopscout-mcp when authorized; otherwise user JSON exports from Admin.
Inputs: shop domain, API scopes confirmed, task type (audit|inventory|orders|draft-product).
Products: paginate; capture handle, title, status, variants (sku, price, inventory_quantity, barcode).
Inventory: identify negative stock, oversell risk, locations if multi-location enabled.
Orders: date range, financial status filter; compute net sales, refund rate—no full customer address dump.
Metafields: list namespace.key when user cares about SEO or ERP sync.
Theme/checkout: refuse direct edit; suggest duplicate theme + preview URL pattern only.
Writes: create as draft product first; price/inventory patch only with user phrase "FREIGABE SHOPIFY WRITE".
Compare-at price changes: confirm marketing intent—document old→new per variant.
Bulk: batch ≤50 variants unless API docs allow; on 429 exponential backoff.
GDPR: minimize customer PII in reports—aggregate where possible.
German storefront: note tax inclusive display settings when interpreting prices.
Output: shopify_audit_YYYY-MM-DD.md + optional products_snapshot.csv.
Log each GraphQL/MCP operation ID when returned.
Gift cards, discounts, scripts: read-only unless explicit approval.
Do not disable fraud filters or payment providers.
```

## Arbeitsablauf

1. Shop, Scopes und Schreibmodus (read-only vs. Draft) klären.
2. Datenbedarf festlegen: Produkte, Lagerorte, Order-Zeitraum.
3. Katalog paginieren und Snapshot speichern.
4. Abgleich mit Soll-Liste (SKU, Preis, Bestand).
5. Abweichungen priorisieren (Oversell, 0-Bild, SEO-Title leer).
6. Order-KPIs berechnen, wenn angefragt.
7. Änderungen nur als Draft oder Patch-Liste zur Freigabe ausgeben.

## Qualitätskriterien / Definition of Done

- [ ] Jede Variante mit SKU und Bestandszahl belegt
- [ ] Keine Live-Preisänderung ohne „FREIGABE SHOPIFY WRITE“
- [ ] Order-Report ohne unnötige Kundenadressen
- [ ] API-Fehler und fehlende Scopes dokumentiert

## Sicherheit & Freigaben

- Admin-Token niemals in Chat oder Repo committen.
- `risk_level: medium`—Schreibzugriffe auf Live-Shop nur nach Freigabe.
- DSGVO: Datenminimierung bei Order-Exports.

## Fallstricke

- Inventory an einem Lagerort aktualisieren, Verkauf an anderem Ort → Oversell.
- Compare-at nur kosmetisch senken → Vertrauensverlust.
- Metafield-Sync ERP überschreibt ohne Versionierung.
- Theme-Preview-Link öffentlich teilen mit unreleased Preisen.
- MCP-Cache zeigt alte Bestände nach manuellem Admin-Eingriff.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Bestandsaudit vor Black Friday
- **Input:** `demo-brand.myshopify.com`, SKUs `HOODIE-BLK-S/M/L`
- **Prompt:**

```text
Read-only. Flag inventory ≤2 and negative qty. CSV columns: sku, qty, price, updated_at.
```

- **Erwartetes Ergebnis:**

```text
HOODIE-BLK-M: qty -1 → CRITICAL oversell risk
3 rows in products_snapshot.csv
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Order-KPIs letzte 7 Tage
- **Input:** Zeitraum 2026-11-16–23, Währung EUR
- **Prompt:**

```text
Net sales, order count, refund rate %. No customer names in output.
```

- **Erwartetes Ergebnis:**

```text
Orders: 412 | Net: 38.420 EUR | Refund rate: 2.1%
```