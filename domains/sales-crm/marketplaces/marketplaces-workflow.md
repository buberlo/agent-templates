---
id: marketplaces-workflow
title: "cross-marketplace (eBay, Otto, Kaufland ...)"
domain: sales-crm
category: marketplaces
tags:
  - marketplace
  - multichannel
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: HasData/amazon-mcp
    install: "https://github.com/HasData/amazon-mcp"
    version_notes: "Stars here not pulled by API."
inputs:
  - "Marketplaces and seller exports per platform"
  - "SKU/ EAN Mapping-Tabelle"
  - "Question: Price Parity, Buybox, Listing Status"
outputs:
  - "Parity matrix (price, availability, gross fees)"
  - "Listings with status errors"
  - "Empfehlung welcher Kanal priorisiert wird (nur Analyse)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Multiple **third party marketplaces** besides Amazon compare: listing status, price parity, fee approximation—assuming central SKU truth.

## When to use

- Planning expansion on eBay/Otto/Kaufland with inventory mirroring.
- Find price deviation >X % between channels.
- Feed-Fehler aus Marktplatz-Reports clustern.

**When not**

- Unbekannte Marktplatz-API without Dokumentation live ansteuern.
- Gebotsmanipulation auf Auktionsplattformen.

## Tool stack

| Tool | Role | Explanation |
|------|-------|------------|
| Plattform-Exports | Ground truth | Vendor-CSV |
| HasData/amazon-mcp | Amazon-Referenz | Optional Vergleich |
| SKU-Map | Join-Key | Nutzerpflege |

## System prompt

```text
Role: marketplace parity analyst (sales-crm/marketplaces).
Mission: Compare listings across user-supplied marketplace exports—no unauthorized scraping of eBay/Otto sites.
Inputs: marketplace list, SKU map file, tolerance % for price delta default 3.
Per marketplace columns normalize: sku, ean, price, stock, status, fees_optional.
Join on sku then ean fallback—log unjoined rows.
Parity table: highlight where price diff > tolerance or stock 0 on one channel only.
Fees: if user provides fee sheet, compute margin estimate disclaimer rough.
Amazon row optional via MCP read-only for same EAN—label source.
Status errors: inactive, suppressed, missing image—aggregate count by marketplace.
Recommendations: prioritize channel by margin and stock—advisory only.
German marketplaces: note VAT included price assumption.
Output: parity_YYYY-MM-DD.csv, summary_de.md.
No listing create/update API calls.
Legal: respect each marketplace partner terms on data use.
Feed schedules: note if export stale >24h.
Promotional prices: compare base vs promo columns if present.
Variant explosion: collapse to parent SKU when user map says so.
```

## Workflow

1 To document marketplaces and export format.
2. SKU/EAN-Map validieren.
3. Normalize fields and join.
4. calculating price and stock parity.
5. Status-Fehler aggregieren.
6. Kurz-Empfehlung je SKU-Cluster.
7. Report without Feed-Schreiben ausliefern.

## Definition of done

- [ ] Unjoined SKUs counted
- [ ] Toleranz % dokumentiert
- [ ] No Listing-API-Writes
It is an a (e an olet, OR, OR, OR, OR, OR, OR, OR, OR.

## Security

Thezing that can be a collaborator of the ?
- should not scrap in login sessions.

## Pitfalls

Compare the promo price with the base price.
- EAN-Mehrdeutigkeit bei Bundles.
- Zeitzone bei Tages-Exporten.
- Amazon MCP Momentaufnahme vs. gestern Feed.
Fees without shipping model.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Parity Amazon vs Buying Country
- **Input:** zwei CSVs, MAP, 3% tolerance
- **Prompt:**

```text
parity csv + top 10 worst deltas.
```

- **Expected result:**

```text
11 SKUs over 3% | example SKU-991 +7.2% Kaufland higher
```

### Example 2 (Example data (self-written))
- **Task:** Repressed Listings
- **Input:** eBay export status column
- **Prompt:**

```text
Count by status, list sku for suppressed.
```

- **Expected result:**

```text
suppressed: 8 | missing image: 3 | sku list attached
```