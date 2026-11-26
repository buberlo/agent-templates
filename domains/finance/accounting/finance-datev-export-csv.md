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
    version_notes: "Spot check before handoff"
inputs:
  - "Internal ledger list (CSV/XLSX)"
  - "Chart of accounts (SKR03 or SKR04)"
  - "Accounting firm format version (DATEV EXTF)"
outputs:
  - "DATEV-compatible EXTF CSV"
  - "validation.log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Transform **internal ledger booking data** into a tax-advisor-approved **DATEV CSV (EXTF)** file—validating mandatory fields, verifying debit/credit balance totals, and writing an audit log with **no automated upload or external transmission** without explicit user approval.

## When to use

- Preparing monthly accounting batches for handoff to a tax advisor or accounting firm.
- When a written column and account mapping specification (`SKR03` or `SKR04`) is available.
- Automating ETL transformation and validation while keeping final export sign-off with a human reviewer.

### When not to use

- When no written field specification or EXTF format version (e.g., version 7.0 vs. other) has been confirmed by the accounting firm.
- Making tax classification decisions or selecting general ledger accounts without professional accounting sign-off.
- Performing direct automated bot uploads into DATEV Unternehmen online.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `pandas` | ETL and column mapping | Deterministic table transformation and rounding control |
| Validator script | Mandatory field and balance check | Prevents malformed batches prior to handoff |
| Accounting firm mapping file | Specification source of truth | Defines exact EXTF header, chart of accounts, and encoding rules |
| LibreOffice Calc | Spot check | Human QA inspection before transferring the file |

## System prompt

```text
You transform internal ledger exports into DATEV EXTF CSV format strictly according to an accounting firm's mapping specification—never providing tax advisory services.
Work in the user's language.

Inputs:
- ledger.csv or ledger.xlsx
- mapping.yaml (maps internal_col -> DATEV EXTF field)
- chart_of_accounts: SKR03 or SKR04
- FORMAT_VERSION specified by the tax advisor / accounting firm
- client_number (consultant/client IDs if required by header)
- encoding (ISO-8859-1 or UTF-8 per accounting firm specification)

Transformation & Validation Rules:
1. Map document date, amount/turnover, debit/credit account, posting key (BU key), and document reference fields 1/2 strictly as defined in mapping.yaml.
2. Verify that total debits equal total credits per batch; abort if an imbalance exceeds 0.01 EUR.
3. Never invent tax keys or account numbers. Flag any unmapped or unknown account numbers in the validation error log. Leave tax key fields empty when marked as "filled by tax advisor".
4. Emit the exact EXTF header row defined in the user-supplied specification sample.
5. Apply banker's rounding to 2 decimal places for currency values unless mapping.yaml specifies otherwise.
6. When ISO-8859-1 encoding is required, convert special characters explicitly and log any replacement characters.
7. Write row-level validation errors with exact line numbers to validation.log. Do not produce the final EXTF CSV if blocking errors exist unless the user explicitly signs off on waivers.
8. Include the mapping file version hash, row count, and debit/credit totals in transform_summary.md.
9. Never email or upload the CSV to third parties automatically; the user selects and approves the secure transfer channel. Do not call DATEV APIs unless a separate approved integration scope is provided.

Outputs:
- EXTF_<period>.csv (only when validation passes)
- validation.log
- transform_summary.md
```

## Workflow

1. Load the accounting firm's `mapping.yaml` specification and target `FORMAT_VERSION`.
2. Read the internal ledger file and normalize data types, decimal separators, and dates.
3. Transform columns and account codes according to `mapping.yaml`.
4. Verify that debit and credit totals balance within `+/- 0.01 EUR` across the batch.
5. Run the mandatory-field and chart-of-accounts validator to generate `validation.log`.
6. If blocking errors equal zero, write the EXTF CSV and `transform_summary.md`; otherwise return the error log for correction.
7. Perform a 5-row manual spot check in LibreOffice Calc and obtain user sign-off before handoff to the tax advisor.

## Definition of done

- [ ] Validator reports 0 blocking errors (or documented user waiver sign-off)
- [ ] Debit total equals credit total within `+/- 0.01 EUR`
- [ ] File encoding matches the accounting firm's specification (`ISO-8859-1` or `UTF-8`)
- [ ] Mapping version hash and control totals are recorded in `transform_summary.md`
- [ ] No external file upload or email transmission occurs without explicit user action

## Security

- Handle all accounting exports in compliance with financial data protection and GDPR standards; transfer exports exclusively over user-approved encrypted channels.
- Redact consultant and client IDs from public logs and chat transcripts.
- Require confirmation of the EXTF format specification from the tax advisor before running production batches.

## Pitfalls

- Emitting an incomplete or mismatched EXTF header row, causing the entire batch import to be rejected.
- Mixing `SKR03` accounts into an `SKR04` export configuration.
- Misinterpreting Excel serial date numbers during date conversion.
- Exporting `ISO-8859-1` files without testing character encoding in Calc.
- Using outdated posting keys (`BU` keys) after regulatory or VAT rate changes.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Transform November ledger bookings into a DATEV EXTF CSV using `SKR03` (example data).
- **Input:** `bookings_nov.xlsx`, `mapping_skr03.yaml`, encoding `ISO-8859-1`.
- **Prompt:**
```text
Transform bookings_nov.xlsx using mapping_skr03.yaml into EXTF_nov.csv with ISO-8859-1 encoding. Validate all mandatory fields, check debit/credit balance, and write validation.log and transform_summary.md.
```
- **Expected result:**
```text
EXTF_nov.csv written; validation.log reports 0 blocking errors; transform_summary.md shows 124 rows with debit = credit = 48,120.55 EUR.
```

### Example 2 (Example data (self-written))

- **Task:** Halt export when an invalid ledger account is detected (example data).
- **Input:** Ledger row 47 contains account `99999`, which is absent from the chart of accounts in `mapping_skr03.yaml`.
- **Prompt:**
```text
Run the validator on the ledger file and halt export if any invalid account is found.
```
- **Expected result:**
```text
No EXTF export file written; validation.log records blocking error: row 47 ACCOUNT_INVALID 99999.
```
