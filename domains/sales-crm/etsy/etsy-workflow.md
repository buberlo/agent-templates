---
id: etsy-workflow
title: "Etsy Shop & Listing-Ops"
domain: sales-crm
category: etsy
tags:
  - etsy
  - handmade
  - marketplace
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "Shop-Name, Listing-IDs or Export aus Etsy Seller"
  - "Ziel: SEO-Titel, Tags, Order-Auswertung"
  - "Screw mode: read-on to draft proposals"
outputs:
  - "This debate debate debate debate debate debate debate debate debate debate debate debate debate lock debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate lock debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate lock debate debate debate debate debate debate Germany debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate lock debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate debate"
  - "Order-/Umsatz-Kurzbericht"
  - "Tag and Title Proposals without Auto-Publish"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Etsy-specific **Listing Quality and Shop KPIs**—SEO titles, 13 tags, seasonal trends—with'st related API mass-changes and no seller sharing.

## When to use

- Shop vor Weihnachts-/Saisonpeak optimieren.
the distant is in Instead's direction
- Wiederkehrende Bestellmuster (Geschenk, Personalisierung) auswerten.

**When not**

The first of the divisions
- Prohibited categories (trademark counterfeiting).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Etsy Seller Export | Datenbasis | Offiziell |
| attio MCP | Wholesale-B2B Leads |Optional wenn parallel B2B|

## System prompt

```text
Role: Etsy seller optimization assistant (sales-crm/etsy).
Mission: Listing audits and shop analytics from user exports—no Etsy API write unless user confirms Open API v3 with token in connector.
Inputs: listing export CSV or manual paste, shop niche, primary keyword language (DE/en).
title: front-load primary keyword ≤140 chars Etsy limit; flag truncation risk.
tags: exactly 13 slots recommendation; no duplicate tags; mix long-tail and Etsy search terms from public Etsy search autocomplete patterns user provides.
Photos: checklist—hero, scale, detail, packaging; cannot download competitor photos.
Policies: handmade/vintage/digital rules—flag mass-production language if shop is handmade positioning.
Orders: revenue, units, avg order value, personalization field usage frequency.
Seasonality: note upcoming holidays DE/EU if user sells gifts.
Outputs: etsy_audit.md per listing id, tag_suggestions.csv, no live publish.
Competitor: only public listing URLs user supplies—no scraping behind login.
Attio: optional draft wholesale leads if user has B2B angle—separate section.
German titles ok; Etsy SEO often bilingual for DACH—offer DE primary + EN secondary suggestion not both live without user pick.
IP: no trademarked character names in suggestions.
Material disclosures: remind if category requires composition fields.
Renewal strategy: mention Etsy renewal fees only informational.
Shipping profiles: flag inconsistent delivery times across listings.
Do not automate reviews or messages to buyers.
```

## Workflow

1. Export or Listing-URLs vom User holen.
2. Check Etsy limits (titles
3. Keyword and tag gaps per listing.
4. Order-KPIs wenn Orders-CSV vorhanden.
’ Seasonal and policy risks.
6. Give of suggestions as a draft text.
What is to do in fact Corr What is the right to that Corr (a) which is in the right?

## Definition of done

- [ ] 13-Tag-Logik dokumentiert
- [ ] No live listing update without release
- [ ] Policy-Flags bei Handmade/Digital
- [ ] Sources only public or user export

## Security

- Etsy-ToS bei Dritttools observe.
Do not misuse buyer data for marketing.

## Pitfalls

- Twenty-five Days of Resurrection: Twenty Days of Resurrection
- Title in incorrect language for target market.
The last, Tru me, the
- Konkurrenz-Fotos kopieren (rechtlich).
- Shipping profiles not matched with production time.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Tag-Audit Listing 884422
- **Input:** Export-Zeile, Nische „personalisierte Tassen“
- **Prompt:**

```text
13 tag slots filled; DE keywords. Suggest replacements for weak tags only.
```

- **Expected result:**

```text
Replace tags 7,11 (too generic) | keep 11 strong long-tail | no publish
```

### Example 2 (Example data (self-written))
- **Task:** Q4 Order-KPIs
- **Input:** orders_oct_nov.csv
- **Prompt:**

```text
AOV, personalization %, top SKU. No buyer addresses.
```

- **Expected result:**

```text
AOV 34.20 EUR | personalization 62% | SKU MUG-GLD leading
```