---
id: finance-datev-export-csv
title: "DATEV export from ledger list"
domain: finance
category: accounting
tags:
  - datev
  - csv
  - skr03
target_agents:
  - hermes
  - cursor
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Transformation"
  - name: LibreOffice Calc
    install: "optional"
    version_notes: "Sample before handoff"
inputs:
  - "Interne Buchungsliste (CSV/XLSX)"
  - "SKR03 or SKR04"
  - "Kanzlei-Formatversion (EXTF)"
outputs:
  - "DATEV-kompatible CSV"
  - "validation.log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Internal Buchungsdaten** in a from the Steuerkanzlei bestatigtes **DATEV-CSV (EXTF)** uberfuhren—Pflichtfelder validieren, Summen prufen, **no Upload** without approval.

## When to use

- Monatsbatch vor tax advisor-handoff.
- Mapping SKR03/04 liegt schriftlich vor.
- Agent automatisiert Transform + Validator, Mensch gibt Export frei.

######################################################################## When not to use

- Ohne schriftliche Feldspezifikation the tax office (Version 7.0 vs. andere).
- Steuerliche Bewertung or Kontenwahl without Fachfreigabe.
- Direkter DATEV-Unternehmen-online-Import durch Bot.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pandas | ETL | Spaltenmapping |
| Validator (Script) | Pflichtfelder | Vor handoff |
| Kanzlei-Mapping-Tabelle | Spec | Source of truth |
| Calc | Stichprobe | Menschliche QA |

## System prompt

```text
You transform internal ledger exports to DATEV CSV per Kanzlei mapping—not tax advisory.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: ledger.csv/xlsx, mapping.yaml (internal_col → DATEV field), SKR (03|04), FORMAT_VERSION from Steuerberater, mandant_number if required, encoding (ISO-8859-1 vs UTF-8 per Kanzlei).
Rules:
- posting date, turnover, debit/credit-Konto, BU key, document field 1/2 as mapping defines.
- debit/credit sums must balance per batch; stop on imbalance > 0.01 EUR.
- No invented tax keys; UNKNOWN accounts → validation error list.
Transform steps in pandas; emit EXTF header row exactly as spec PDF states (user provides sample).
Validation log must list row-level errors with line numbers; zero blocking errors before export OR user sign-off on waivers.
Encoding: when Kanzlei demands ISO-8859-1, convert umlauts explicitly; log replacement chars.
Output files: EXTF_nov.csv, validation.log, transform_summary.md (row count, sum debit/credit).
Never email CSV to third parties; user chooses secure channel.
No DATEV API calls unless user provides separate integration scope.
Document mapping version hash in summary.
Round currency to 2 decimals banker's rounding unless mapping says else.
Keep Steuerschlussel empty when user marks "tax advisor fills".```

## Workflow

1. tax office-Mapping and FORMAT_VERSION laden.
2. Internal list einlesen; Datentypen and Datum normalisieren.
3. Spaltentransform gemass mapping.yaml.
4. Summen debit/credit per Batch prufen.
5. Validator-Script → validation.log.
6. Bei 0 Fehler: CSV schreiben; sonst Fehlerliste an Buchhaltung.
7. Sample 5 lines in Calc; release law firm contact.

## Definition of done

- [ ] Validator: 0 blockierende Fehler or dokumentierte approval
- [ ] Debit total equals credit total (±0.01 EUR)
- [ ] Encoding laut Kanzlei-Vorgabe
- [ ] Kein Versand without Nutzerkanal-Wahl
- [ ] Mapping-Version im Summary

## Security

- Finanzdaten GOdB/DSGVO; Export nur sicherer Kanal.
- No Mandantennummern in offentlichen Logs.
- tax advisor bestatigt Format vor Produktiv-Batch.

## Pitfalls

- Falsche EXTF-Kopfzeile → kompletter Import abgelehnt.
- SKR03-Konto in SKR04-Export.
- Excel-Datum als Serienzahl falsch konvertiert.
- ISO-8859-1 without Umlaut-Test in Calc.
- BU key veraltet nach Gesetzesanderung.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** November-Buchungen EXTF SKR03.
- **Input:** `buchungen_nov.xlsx`, `mapping_skr03.yaml`, Encoding ISO-8859-1.
- **Prompt:**

```text
Transform to EXTF_nov.csv, validate all mandatory fields, balance check, write validation.log.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.EXTF_nov.csv, validation.log (0 errors), transform_summary.md with 124 rows, debit=credit=48120.55.
```

### Example 2 (Example data (self-written))
- **Task:** Ungultiges Konto abbrechen.
- **Input:** Zeile with Konto `99999` not in Kontenplan.
- **Prompt:**

```text
Run validator only; expect blocking error on row 47 invalid account.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.No EXTF export written; validation.log line: row 47 ACCOUNT_INVALID 99999.
```