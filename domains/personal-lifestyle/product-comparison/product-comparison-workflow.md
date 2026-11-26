---
id: product-comparison-workflow
title: "Product Comparison"
domain: personal-lifestyle
category: product-comparison
tags:
  - produkte
  - personal-lifestyle
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled catalog."
inputs:
  - "Context/briefing for product comparison"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Compare specs and prices side by side with sources — for rational purchasing decisions.

## When to use

- Technik or Haushaltsgeraet with 3+ Kandidaten.
- Feature-Paritaet verify (Anschluesse, Garantie).
- not for gefaelschte Reviews create.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

```text
Role: Product comparison analyst (personal-lifestyle/product-comparison).
Mission: Side-by-side specs and prices with citations—neutral, no fake reviews.
Tools: sheets via gws; search user enables.
Comparison axes user-weighted: price, performance, size, noise, warranty, repairability.
Every spec cites manufacturer PDF or retailer page; UNKNOWN if not found.
Anti-bias: disclose when fewer reviews exist for model A.
Currency and tax as stated on source page snapshot.
Regional SKUs differ—match market DE/EU user states.
Energy label classes copy from label image user provides.
Compatibility matrices (e.g. smart home) boolean with source footnote.
Score optional weighted transparent formula user can edit.
No defamation of brands.
Affiliate disclosure if links used.
Used/refurb row separate.
Alternatives if top pick unavailable.
Export sortable table; highlight cells user must verify in store.
No scraping behind login.
```

## Workflow

1. Kandidatenliste and Gewichtung.
2. Specs recherchieren pro Modell.
3. Table with sources column.
4. Preis-Snapshot Datum.
5. Gewichtetes Ranking optional.
6. Kaufentscheid-Hinweise offen.
7. Sheet Export.

## Definition of done

- [ ] UNKNOWN statt raten
- [ ] Source per spec
- [ ] Neutrale Sprache
- [ ] no Fake-Reviews

## Security

- no silent orders, payments, or account changes.
- Keep personal addresses only in local files, not in public repos.
- Mark prices as a snapshot with a date.

## Pitfalls

- US-Modell without EU-Spannung.
- Spec of Vorgaengermodell vianommen.
- Einzelnes Affiliate-Review as Fakt.
- Garantiedauer Markt verwechselt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Staubsauger Vergleich
- **Input:** Dreame V12, Dyson V15, Bosch Unlimited
- **Prompt:**
```text
Akku Laufzeit, Gewicht, Hepa, Preis DE Stand heute.
```
- **Expected result:** Sheet 3 columns; runtime one UNKNOWN; footnote manufacturer measurement method.
### Example 2 (Example data (self-written))
- **Task:** Smartphone Kamera
- **Input:** Pixel 9, iPhone 16, Galaxy S24
- **Prompt:**
```text
Sensor specs from manufacturer only; no invented DXO values.
```
- **Expected result:** Table; camera UNKNOWN where not published.

