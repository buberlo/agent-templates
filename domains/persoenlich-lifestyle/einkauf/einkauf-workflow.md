---
id: einkauf-workflow
title: "Einkauf"
domain: persoenlich-lifestyle
category: einkauf
tags:
  - einkauf
  - persoenlich-lifestyle
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
inputs:
  - "Kontext/Briefing für Einkauf"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Produktrecherche, Preisziel und Bestellvorbereitung — Warenkorb setzt der Nutzer selbst.

## Wann nutzen

- Größere Anschaffung mit Must-haves und Budget-Deckel.
- Preisalarm-Vorbereitung mit Links und Stichtag.
- Nicht für automatischen Checkout oder Abo-Tricks ohne Zustimmung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Kalender & Tabellen | Sheets/Calendar für Listen und Erinnerungen nach OAuth. |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Bedarf und Budget festzurren.
2. Shortlist 5–8 Produkte recherchieren.
3. Vergleichsmatrix in Sheet.
4. Preisziel und Alternativen notieren.
5. Bestell-Checkliste (Adresse, Garantie).
6. Nutzer checkout selbst.
7. Optional Kalender Reminder für Sale via gws.

## Qualitätskriterien / Definition of Done

- [ ] Preise mit Abrufdatum
- [ ] Kein Checkout
- [ ] Quellenlinks
- [ ] Abo-Fallen markiert

## Sicherheit & Freigaben

- Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.
- Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.
- Preise als Momentaufnahme mit Datum kennzeichnen.

## Fallstricke

- Grauimport ohne Garantie-Hinweis.
- Refurb ohne Händlerbewertung.
- Falsche Steckertyp Version.
- Sheet mit voller Heimatadresse geteilt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** E-Bike bis 2500 EUR
- **Input:** Pendeln 15km, Bosch Motor, STORES DE
- **Prompt:**
```text
Matrix 4 Bikes mit Gewicht und Reichweite aus Herstellerseiten.
```
- **Erwartetes Ergebnis:** Sheet 4 Zeilen; ein UNKNOWN Reichweite; kein Kauf.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Black Friday Watchlist
- **Input:** Kopfhörer + Monitor, Ziel -20%
- **Prompt:**
```text
Links + Zielpreis, Calendar Reminder 28.11.
```
- **Erwartetes Ergebnis:** Sheet 2 Items; gws Event Entwurf ohne Versand.

