---
id: finanzen-camt053-reconcile
title: "Bankabgleich mit CAMT.053"
category: finanzen-buchhaltung
tags:
  - camt053
  - reconciliation
  - banking
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: xmltodict pandas"
    version_notes: "CAMT Parser"
  - name: duckdb
    install: "pip: duckdb"
    version_notes: "Matching-SQL"
inputs:
  - "CAMT.053 XML"
  - "Offene Posten CSV"
  - "Toleranzbetrag"
outputs:
  - "Abgleich-CSV"
  - "Unmatched-Liste"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Kontoauszüge (SEPA CAMT.053) mit Buchhaltungs-OPOS automatisch abgleichen.

## Wann nutzen

- Monatsabschluss, Mahnwesen-Vorbereitung.
- Nicht als steuerliche Beratung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| CAMT Parser | XML → Tabellen | ISO 20022 |
| DuckDB | Fuzzy match | Betrag+Datum+Referenz |
| Excel/LibreCalc | Review | Buchhaltung prüft |

## System-Prompt / Instruktionen

```text
Parse CAMT.053 and match open items by amount, date window, and remittance reference.
Mark partial payments and currency explicitly.
Never auto-post to ERP; output review CSV only.
```

## Arbeitsablauf

1. CAMT validieren (XSD).
2. OPOS importieren.
3. Matching-Regeln anwenden.
4. Unmatched klassifizieren.
5. CSV an Buchhaltung.

## Qualitätskriterien / Definition of Done

- [ ] Match-Rate > vereinbarter Schwellwert
- [ ] Alle Unmatched begründet
- [ ] Summen saldieren

## Sicherheit & Freigaben

- Bank-XML vertraulich; verschlüsselt speichern.
- Vier-Augen vor ERP-Import.

## Beispiele

**Eingabe:** `stmt.camt`, `opos_nov.csv`
**Erwartetes Ergebnis:** `match.csv`, 3 Unmatched
