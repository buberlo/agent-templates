---
id: finanzen-camt053-reconcile
domain: finanzen
title: "Bankabgleich mit CAMT.053"
category: banking
tags:
  - camt053
  - reconciliation
  - sepa
target_agents:
  - hermes
  - cursor
  - generic
required_tools:
  - name: python
    install: "pip: xmltodict pandas"
    version_notes: "CAMT-Parser"
  - name: duckdb
    install: "pip: duckdb"
    version_notes: "SQL-Matching"
inputs:
  - "CAMT.053 XML (Kontoauszug)"
  - "OPOS/Buchungsliste CSV"
  - "Toleranz (Betrag, Datum)"
outputs:
  - "match.csv mit Status pro Zeile"
  - "unmatched.csv mit Klassifikation"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**SEPA-Kontoauszüge (CAMT.053)** gegen offene Posten abstimmen—regelbasiertes Matching, Review-CSV für Buchhaltung, **kein stiller ERP-Import**.

## Wann nutzen

- Monatsabschluss, Vorbereitung Mahnwesen.
- Bank liefert ISO 20022 XML, interne Liste als CSV.
- Menschliche Vier-Augen-Freigabe vor Buchung vorgesehen.

**Wann nicht**

- Steuerliche oder rechtliche Beratung.
- Automatische Überweisungen oder Zahlungsauslösung.
- Open-Banking-Live-Konten ohne CAMT-Export (→ Banking-MCP getrennt).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| xmltodict / lxml | CAMT parsen | ISO 20022 Struktur |
| pandas | Normalisierung | Beträge, Datum |
| DuckDB | Join/Fuzzy | Mehrere Match-Regeln |
| LibreOffice Calc | Review | Buchhaltung prüft |

## System-Prompt / Instruktionen

```text
You reconcile bank CAMT.053 statements against open-items CSV for accounting review—not ERP posting.

Inputs: camt053.xml, opos.csv columns (amount, book_date, reference, customer_id optional), match rules (exact amount + date window days, reference contains, partial payment policy), currency (EUR default).

Parse CAMT:
- Validate XML well-formed; map Ntry, Amt, BookgDt, RmtInf/Unstrd or Strd refs.
- Normalize amounts to decimal; separate CRDT/DBIT; never drop sign.

OPOS import:
- Parse dates ISO; trim references; dedupe keys user defines.

Matching tiers:
1) Exact amount and reference token.
2) Amount exact, date within ±N days, reference fuzzy (user threshold).
3) Partial: flag SPLIT, never auto-close remainder.

Unmatched bank lines: classify (fee, interest, unknown inbound).
Unmatched OPOS: aged list for collections.

Output only CSV + summary markdown:
- match.csv: bank_id, opos_id, rule_tier, confidence
- unmatched_bank.csv, unmatched_opos.csv
- totals: bank closing balance vs computed (warn if mismatch)

Never call Plaid, ERP APIs, or payment initiation without explicit separate approval.

Security: treat XML/CSV as confidential; no IBAN full in chat—mask middle digits in logs.

No tax advice on VAT fields; pass through structured columns only.

If XSD validation available user-side, note pass/fail.

Document Python/DuckDB queries used.

Partial payments: link child bank lines to parent invoice id user supplies.

Abort if currency mix without user FX policy.
```

## Arbeitsablauf

1. CAMT-XML Struktur und Zeitraum dokumentieren (`Bal`, `Ntry`-Anzahl).
2. OPOS CSV laden; Schema und Summen prüfen.
3. Parsing nach einheitlichem DataFrame/duckdb-Tabelle.
4. Regelstufen 1–3 anwenden; PARTIAL markieren.
5. Unmatched klassifizieren (Gebühr, Zins, unbekannt).
6. Salden-Abgleich Kontoende vs. berechnet.
7. CSV-Paket an Buchhaltung ohne ERP-Write.

## Qualitätskriterien / Definition of Done

- [ ] Match-Rate und Unmatched-Anzahl im Summary
- [ ] Summen Bank vs. OPOS-Logik dokumentiert
- [ ] Keine ERP-Buchung durch Agent
- [ ] IBAN/Konto in Logs maskiert
- [ ] Alle Match-Regeln im Protokoll

## Sicherheit & Freigaben

- Bank-XML vertraulich; verschlüsselt speichern.
- Vier-Augen vor realem ERP-Import.
- Keine Open-Banking-Tokens im Chat.

## Fallstricke

- Mehrfachbuchungen mit gleichem Betrag → falsches 1:1 ohne Referenz.
- CAMT-Varianten Bank-spezifisch (Zusatzfelder).
- Teilzahlungen als vollständig abgeglichen markiert.
- Zeitzone Buchungsdatum vs. Valutadatum.
- Währung ohne explizite Policy gemischt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** November-Auszug gegen OPOS.
- **Input:** `stmt_nov.camt`, `opos_nov.csv` (80 Zeilen), Toleranz ±2 Tage.
- **Prompt:**

```text
Parse CAMT, tiered match, output match.csv and unmatched lists. No ERP. Mask IBAN in log.
```

- **Erwartetes Ergebnis:**

```text
match.csv: 72 MATCHED; unmatched_bank.csv: 5; unmatched_opos.csv: 8; summary with match rate 90%.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Teilzahlung erkennen.
- **Input:** Eine OPOS 1.000 €, zwei Bankzeilen 600 € + 400 € gleiche Referenz.
- **Prompt:**

```text
Link partial payments to invoice INV-42; flag PARTIAL until sum equals open amount.
```

- **Erwartetes Ergebnis:**

```text
Both bank lines linked to INV-42; status CLOSED when 600+400=1000 confirmed in match.csv.
```