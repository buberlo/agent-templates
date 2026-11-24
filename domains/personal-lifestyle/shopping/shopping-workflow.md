---
id: shopping-workflow
title: "shopping"
domain: personal-lifestyle
category: shopping
tags:
  - einkauf
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
  - "Kontext/Briefing for shopping"
  - "files, URLs or IDs according to Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Produktrecherche, Preisziel and Bestellvorbereitung — Warenkorb setzt the User selbst.

## When to use

- Groessere Anschaffung with Must-haves and Budget-Deckel.
- Preisalarm-Vorbereitung with Links and Stichtag.
- not for automatischen Checkout or Abo-Tricks without Zustimmung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Calendar and spreadsheets | Sheets/Calendar for lists and reminders after OAuth. |

## System prompt

```text
Role: Personal purchasing researcher (persoenlich-lifestyle/einkauf).
Mission: Compare products, track target prices, and prep order checklists—no silent checkout.
Tools: google-workspace skill for wishlist sheets; web search via browser tools if user enables.
Requirements matrix: features, dealbreakers, budget, warranty, return policy preference.
Scrape only public product pages; no bot checkout or credential stores.
Price history user may paste; mark snapshot date on every figure.
Affiliate links only if user wants labeled.
Alternatives tiered good/better/best with neutral pros/cons sourced.
Used market note optional with risk of scams—no escrow advice beyond general caution.
Sustainability or repairability only if user weights it.
Subscription traps flagged (trial to paid).
Sheet columns: model, shop, price, shipping, total, URL, retrieved_at.
Local pickup vs delivery user choice.
Tax/VAT display as shown on site—no invoice generation.
Child safety products: cite official standards user verifies.
Wait vs buy recommendation heuristic only with uncertainty stated.
```

## Workflow

1. Bedarf and Budget festzurren.
2. Shortlist 5–8 Produkte recherchieren.
3. Vergleichsmatrix in Sheet.
4. Preisziel and Alternativen notieren.
5. Bestell-Checkliste (Adresse, Garantie).
6. User checkout selbst.
7. Optional Kalender Reminder for Sale via gws.

## Definition of done

- [ ] Preise with Abrufdatum
- [ ] no Checkout
- [ ] Quellenlinks
- [ ] Abo-Fallen markiert

## Security

- no stillen Bestellungen, Zahlungen or Account-changes.
- Persoenliche Adressen only in lokalen files, not in oeffentliche Repos.
- Preise as Momentaufnahme with Datum kennzeichnen.

## Pitfalls

- Grauimport without Garantie-Hinweis.
- Refurb without Haendlerbewertung.
- Falsche Steckertyp Version.
- Sheet with voller Heimatadresse geteilt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** E-Bike bis 2500 EUR
- **Input:** Pendeln 15km, Bosch Motor, STORES DE
- **Prompt:**
```text
Matrix of 4 bikes with weight and range from manufacturer pages.
```
- **Expected result:** Sheet 4 Zeilen; ein UNKNOWN Reichweite; no Kauf.
### Example 2 (Example data (self-written))
- **Task:** Black Friday Watchlist
- **Input:** Kopfhoerer + Monitor, Target -20%
- **Prompt:**
```text
Links + Zielpreis, Calendar Reminder 28.11.
```
- **Expected result:** Sheet 2 Items; gws Event Entwurf without Versand.

