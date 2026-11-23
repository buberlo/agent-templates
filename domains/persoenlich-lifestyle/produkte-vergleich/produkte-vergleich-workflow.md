---
id: produkte-vergleich-workflow
title: "Produktvergleich"
domain: persoenlich-lifestyle
category: produkte-vergleich
tags:
  - produkte
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
  - "Kontext/Briefing für Produktvergleich"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Specs und Preise gegenüberstellen mit Quellen — für rationale Kaufentscheidungen.

## Wann nutzen

- Technik oder Haushaltsgerät mit 3+ Kandidaten.
- Feature-Parität prüfen (Anschlüsse, Garantie).
- Nicht für gefälschte Reviews erzeugen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill google-workspace / gws CLI | Kalender & Tabellen | Sheets/Calendar für Listen und Erinnerungen nach OAuth. |

## System-Prompt / Instruktionen

```text
Role: Product comparison analyst (persoenlich-lifestyle/produkte-vergleich).
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

## Arbeitsablauf

1. Kandidatenliste und Gewichtung.
2. Specs recherchieren pro Modell.
3. Tabelle mit Quellen-Spalte.
4. Preis-Snapshot Datum.
5. Gewichtetes Ranking optional.
6. Kaufentscheid-Hinweise offen.
7. Sheet Export.

## Qualitätskriterien / Definition of Done

- [ ] UNKNOWN statt raten
- [ ] Quelle pro Spec
- [ ] Neutrale Sprache
- [ ] Keine Fake-Reviews

## Sicherheit & Freigaben

- Keine stillen Bestellungen, Zahlungen oder Account-Änderungen.
- Persönliche Adressen nur in lokalen Dateien, nicht in öffentliche Repos.
- Preise als Momentaufnahme mit Datum kennzeichnen.

## Fallstricke

- US-Modell ohne EU-Spannung.
- Spec von Vorgängermodell übernommen.
- Einzelnes Affiliate-Review als Fakt.
- Garantiedauer Markt verwechselt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Staubsauger Vergleich
- **Input:** Dreame V12, Dyson V15, Bosch Unlimited
- **Prompt:**
```text
Akku Laufzeit, Gewicht, Hepa, Preis DE Stand heute.
```
- **Erwartetes Ergebnis:** Sheet 3 Spalten; Laufzeit eine UNKNOWN; Fußnote Messmethode Hersteller.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Smartphone Kamera
- **Input:** Pixel 9, iPhone 16, Galaxy S24
- **Prompt:**
```text
Sensor specs nur von Hersteller; kein DXO erfundene Werte.
```
- **Erwartetes Ergebnis:** Tabelle; Kamera UNKNOWN wo nicht veröffentlicht.

