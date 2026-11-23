---
id: etsy-workflow
title: "Etsy Shop & Listing-Ops"
domain: vertrieb-crm
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
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Shop-Name, Listing-IDs oder Export aus Etsy Seller"
  - "Ziel: SEO-Titel, Tags, Order-Auswertung"
  - "Schreibmodus: read-only | Draft-Vorschläge"
outputs:
  - "Listing-Audit (Tags, Titellänge, Fotos-Checkliste)"
  - "Order-/Umsatz-Kurzbericht"
  - "Tag- und Titel-Vorschläge ohne Auto-Publish"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Etsy-spezifische **Listing-Qualität und Shop-KPIs**—SEO-Titel, 13 Tags, saisonale Trends—ohne API-Massenänderungen ohne Seller-Freigabe.

## Wann nutzen

- Shop vor Weihnachts-/Saisonpeak optimieren.
- Underperforming Listings gegen Etsy-Richtlinien prüfen.
- Wiederkehrende Bestellmuster (Geschenk, Personalisierung) auswerten.

**Wann nicht**

- Digitale Downloads mit Lizenzstreitigkeiten.
- Verbotene Kategorien (Markenfälschung).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Etsy Seller Export | Datenbasis | Offiziell |
| attio MCP | Wholesale-B2B Leads | Optional wenn parallel B2B |

## System-Prompt / Instruktionen

```text
Role: Etsy seller optimization assistant (vertrieb-crm/etsy).
Mission: Listing audits and shop analytics from user exports—no Etsy API write unless user confirms Open API v3 with token in connector.
Inputs: listing export CSV or manual paste, shop niche, primary keyword language (DE/en).
Title: front-load primary keyword ≤140 chars Etsy limit; flag truncation risk.
Tags: exactly 13 slots recommendation; no duplicate tags; mix long-tail and Etsy search terms from public Etsy search autocomplete patterns user provides.
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

## Arbeitsablauf

1. Export oder Listing-URLs vom Nutzer holen.
2. Etsy-Limits (Titel, Tags, Fotos) gegen Bestand prüfen.
3. Keyword- und Tag-Lücken je Listing.
4. Order-KPIs wenn Orders-CSV vorhanden.
5. Saison- und Policy-Risiken notieren.
6. Vorschläge als Draft-Text ausgeben.
7. Freigabe vor Seller-Manager-Übernahme einholen.

## Qualitätskriterien / Definition of Done

- [ ] 13-Tag-Logik dokumentiert
- [ ] Kein Live-Listing-Update ohne Freigabe
- [ ] Policy-Flags bei Handmade/Digital
- [ ] Quellen nur öffentliche oder Nutzer-Export

## Sicherheit & Freigaben

- Etsy-ToS bei Dritttools beachten.
- Käuferdaten nicht für Marketing missbrauchen.

## Fallstricke

- Tag-Stuffing mit irrelevanten Begriffen → Ranking-Strafe.
- Titel in falscher Sprache für Zielmarkt.
- Personalisierungs-Optionen ohne Produktionskapazität.
- Konkurrenz-Fotos kopieren (rechtlich).
- Versandprofile nicht mit Produktionszeit abgestimmt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Tag-Audit Listing 884422
- **Input:** Export-Zeile, Nische „personalisierte Tassen“
- **Prompt:**

```text
13 tag slots filled; DE keywords. Suggest replacements for weak tags only.
```

- **Erwartetes Ergebnis:**

```text
Replace tags 7,11 (too generic) | keep 11 strong long-tail | no publish
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Q4 Order-KPIs
- **Input:** orders_oct_nov.csv
- **Prompt:**

```text
AOV, personalization %, top SKU. No buyer addresses.
```

- **Erwartetes Ergebnis:**

```text
AOV 34.20 EUR | personalization 62% | SKU MUG-GLD leading
```