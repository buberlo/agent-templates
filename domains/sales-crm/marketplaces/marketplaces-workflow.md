---
id: marketplaces-workflow
title: "Cross-marketplace operations (eBay, Otto, Kaufland, etc.)"
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
    version_notes: "Star count not pulled via API."
inputs:
  - "Target marketplaces and seller CSV exports per platform"
  - "SKU / EAN mapping table"
  - "Analysis goal: price parity, buy box, or listing status errors"
outputs:
  - "Parity matrix (price, stock availability, rough fee estimate)"
  - "Listings with status or feed errors"
  - "Channel prioritization recommendation (advisory analysis only)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Compare listings across multiple **third-party marketplaces** (such as eBay, Otto, Kaufland) alongside Amazon—evaluating listing status, price parity, inventory availability, and approximate fee margins against a central SKU/EAN mapping table without automated feed writes.

## When to use

- Planning multichannel expansion across eBay, Otto, or Kaufland with mirrored inventory.
- Detecting price deviations exceeding a defined percentage threshold (`> X%`) across sales channels.
- Clustering feed and listing status errors (`inactive`, `suppressed`, `missing image`) from marketplace seller exports.

### When not to use

- Calling undocumented or unverified marketplace write APIs in production.
- Automating bid manipulation or repricing wars on auction platforms.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Marketplace seller CSV exports | Primary channel data | Official vendor reports without scraping risk |
| `HasData/amazon-mcp` | Optional Amazon reference check | Read-only lookup of public Amazon listing data for the same EAN |
| Central SKU/EAN map | Cross-channel join key | User-maintained mapping table linking channel SKUs and parent/child variants |

## System prompt

```text
Role: Multichannel marketplace parity analyst (sales-crm/marketplaces).
Work in the user's language.
Mission: Compare listings across user-supplied marketplace exports—never perform unauthorized scraping of eBay, Otto, or Kaufland websites, and never execute listing create/update API writes.

Inputs:
- Marketplace export files
- SKU/EAN mapping file
- Price delta tolerance_pct (default: 3%)

Normalization & Analysis Rules:
1. Normalize columns per marketplace: sku, ean, price (base vs. promotional if present), stock, status, and optional fees.
2. Join records on SKU first, with EAN as fallback; explicitly log all unjoined rows. Collapse child variants to parent SKUs only when instructed by the user's mapping table.
3. Flag export staleness if any marketplace feed timestamp is older than 24 hours.
4. Build the parity matrix: highlight SKUs where cross-channel price delta exceeds tolerance_pct or where stock equals 0 on one channel while available on others.
5. Explicitly state whether marketplace prices are gross (VAT-inclusive) or net for the target jurisdiction.
6. If the user provides a marketplace fee schedule, compute a rough net margin estimate with an explicit approximation disclaimer.
7. Optionally include a read-only Amazon comparison row via MCP for matching EANs, clearly labeling the data source and snapshot timestamp.
8. Aggregate status errors (inactive, suppressed, missing image) by marketplace and provide advisory channel prioritization recommendations based on margin and stock depth.

Compliance & Outputs:
- Respect each marketplace's partner terms regarding data usage.
- Output parity_YYYY-MM-DD.csv and summary.md (analysis only; no live feed or listing mutations).
```

## Workflow

1. Document the included marketplaces, export timestamps, and CSV schemas.
2. Validate the central SKU/EAN mapping table and variant collapse rules.
3. Normalize price, stock, and status fields and join records across marketplaces.
4. Compute price and stock parity deltas against the configured tolerance threshold.
5. Aggregate listing status errors (`suppressed`, `inactive`, `missing image`) per channel.
6. Draft advisory prioritization recommendations per SKU cluster based on stock and rough fee margins.
7. Deliver `parity_YYYY-MM-DD.csv` and `summary.md` without writing to any live marketplace feeds.

## Definition of done

- [ ] Unjoined SKUs and EAN fallback matches are counted and logged
- [ ] Price delta tolerance percentage is documented and applied
- [ ] Zero live listing or feed update API writes are executed
- [ ] Export age / timestamp per marketplace source is noted in the summary

## Security

- Keep marketplace partner API keys and credentials protected inside authorized connectors.
- Never scrape authenticated seller portals or competitor sessions behind logins.
- Never auto-publish price updates or inventory feeds without explicit user approval.

## Pitfalls

- Comparing a temporary promotional price on one marketplace against the standard base price on another.
- Joining on ambiguous EANs shared across single units and multi-packs/bundles.
- Ignoring timezone mismatches across daily marketplace export schedules.
- Treating a live Amazon MCP snapshot as synchronous with a 24-hour-old CSV export from another channel.
- Estimating channel net margins from referral fees alone while omitting fulfillment and shipping costs.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Compare price parity between Amazon and Kaufland exports (example data).
- **Input:** Two seller export CSVs, central SKU/EAN mapping table, `tolerance_pct=3%`.
- **Prompt:**
```text
Generate parity_2026-11-23.csv and list the top 10 SKUs with the largest cross-channel price deltas exceeding the 3% tolerance.
```
- **Expected result:**
```text
11 SKUs exceed the 3% price tolerance | e.g., SKU-991 is +7.2% higher on Kaufland than Amazon | saved to parity_2026-11-23.csv.
```

### Example 2 (Example data (self-written))

- **Task:** Audit suppressed and broken listings from an eBay export (example data).
- **Input:** eBay seller listing CSV with status and image columns (example data).
- **Prompt:**
```text
Count listings by status and output the SKU list for all suppressed listings and listings missing a primary image.
```
- **Expected result:**
```text
suppressed: 8 | missing image: 3 | affected SKU list attached in summary.md (no live listing edits made).
```
