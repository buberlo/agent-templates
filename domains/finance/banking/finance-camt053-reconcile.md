---
id: finance-camt053-reconcile
title: "Bank reconciliation with CAMT.053"
domain: finance
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
    version_notes: "CAMT parser"
  - name: duckdb
    install: "pip: duckdb"
    version_notes: "SQL matching"
inputs:
  - "CAMT.053 XML (Kontoauszug)"
  - "OPOS/Buchungsliste CSV"
  - "Toleranz (Betrag, Datum)"
outputs:
  - "match.csv with Status per Zeile"
  - "unmatched.csv with Klassifikation"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**SEPA-Kontoauszuge (CAMT.053)** gegen offene Posten abstimmen—regelbasiertes Matching, Review-CSV for accounting, **no stiller ERP-import**.

## When to use

- Monatsabschluss, Vorbereitung Mahnwesen.
- Bank liefert ISO 20022 XML, interne Liste als CSV.
- Human four-eyes clearance provided before booking.

######################################################################## When not to use

- Steuerliche or rechtliche Beratung.
- Automatic transfers or Zahlungsauslosung.
- Open-Banking-Live-Konten without CAMT-Export (→ Banking-MCP getrennt).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| xmltodict / lxml | CAMT parsen | ISO 20022 Struktur |
| pandas | Normalisierung | Betrage, Datum |
| DuckDB | Join/Fuzzy | Mehrere Match-Regeln |
| LibreOffice Calc | Review | accounting pruft |

## System prompt

```text
You reconcile bank CAMT.053 statements against open-items CSV for accounting review—not ERP posting.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Abort if currency mix without user FX policy.```

## Workflow

1. CAMT-XML Struktur and Zeitraum dokumentieren (`Bal`, `Ntry`-Anzahl).
2. OPOS CSV laden; Schema and Summen prufen.
3. Parsing nach einheitlichem DataFrame/duckdb-Tabelle.
4. Regelstufen 1–3 anwenden; PARTIAL markieren.
5. Unmatched klassifizieren (Gebuhr, Zins, unbekannt).
6. Salden-Abgleich Kontoende vs. berechnet.
7. CSV-Paket an Buchhaltung without ERP-Write.

## Definition of done

- [ ] Match-Rate and Unmatched-Anzahl in Summary
- [ ] Summen Bank vs. OPOS-Logik dokumentiert
- [ ] No ERP-Buchung durch agent
- [ ] IBAN/Konto in Logs maskiert
- [ ] Alle Match-Regeln im Protokoll

## Security

- Bank-XML vertraulich; verschlusselt speichern.
- Vier-Augen vor realem ERP-Import.
- No Open-Banking-Tokens in Chat.

## Pitfalls

- Mehrfachbuchungen with gleichem Betrag → falsches 1:1 without Referenz.
- CAMT-Varianten Bank-spezifisch (Zusatzfelder).
- Teilzahlungen as vollstandig abgeglichen markiert.
- Zeitzone Buchungsdatum vs. Valutadatum.
- Wahrung without explizite Policy gemischt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** November-Auszug gegen OPOS.
- **Input:** `stmt_nov.camt`, `opos_nov.csv` (80 Zeilen), Toleranz ±2 Tage.
- **Prompt:**

```text
Parse CAMT, tiered match, output match.csv and unmatched lists. No ERP. Mask IBAN in log.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.match.csv: 72 MATCHED; unmatched_bank.csv: 5; unmatched_opos.csv: 8; summary with match rate 90%.
```

### Example 2 (Example data (self-written))
- **Task:** Teilzahlung erkennen.
- **Input:** Eine OPOS 1.000 €, zwei Bankzeilen 600 € + 400 € gleiche Referenz.
- **Prompt:**

```text
Link partial payments to invoice INV-42; flag PARTIAL until sum equals open amount.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Both bank lines linked to INV-42; status CLOSED when 600+400=1000 confirmed in match.csv.
```