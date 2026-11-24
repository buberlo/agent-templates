---
id: product-comparison-workflow
title: "Produktvergleich"
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
  - "Kontext/Briefing for Produktvergleich"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Specs and Preise againstviastellen with Quellen — for rationale Kaufentscheidungen.

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
You are Product comparison analyst (persoenlich-lifestyle/produkte-vergleich).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
No scraping behind login.```

## Workflow

1. Kandidatenliste and Gewichtung.
2. Specs recherchieren pro Modell.
3. Tabelle with Quellen-Spalte.
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

- no stillen Bestellungen, Zahlungen or Account-changes.
- Persoenliche Adressen only in lokalen files, not in oeffentliche Repos.
- Preise as Momentaufnahme with Datum kennzeichnen.

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
- **Expected result:** Sheet 3 Spalten; Laufzeit eine UNKNOWN; Fussnote Messmethode Hersteller.
### Example 2 (Example data (self-written))
- **Task:** Smartphone Kamera
- **Input:** Pixel 9, iPhone 16, Galaxy S24
- **Prompt:**
```text
Sensor specs nur von Hersteller; kein DXO erfundene Werte.
```
- **Expected result:** Tabelle; Kamera UNKNOWN wo not veroeffentlicht.

