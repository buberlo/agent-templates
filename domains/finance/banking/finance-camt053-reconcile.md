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
  - "CAMT.053 XML (bank statement)"
  - "Open-items / ledger CSV"
  - "Matching tolerances (amount, date window)"
outputs:
  - "match.csv with reconciliation status per line"
  - "unmatched.csv with classification"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Reconcile **SEPA bank statements (ISO 20022 CAMT.053)** against an open-items CSV using rule-based matching tiers to produce review CSVs for accounting—with **no silent ERP imports or automated postings**.

## When to use

- Month-end closing and accounts receivable / collections preparation.
- Comparing ISO 20022 CAMT.053 XML bank exports against an internal open-items CSV.
- Workflows requiring four-eyes human accounting review before any ERP booking.

### When not to use

- Tax or legal advisory tasks.
- Automated wire transfers or payment initiation.
- Live open-banking connections without CAMT.053 XML exports (use a dedicated read-only banking MCP instead).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `xmltodict` / `lxml` | Parse CAMT.053 XML | Reliably extracts nested ISO 20022 elements |
| `pandas` | Data normalization | Standardizes decimal amounts, credit/debit signs, and ISO dates |
| `DuckDB` | Multi-tier SQL joins and fuzzy matching | Fast execution of tiered reconciliation rules |
| LibreOffice Calc | Human review | Enables accounting sign-off on CSV outputs before ERP import |

## System prompt

```text
You reconcile bank CAMT.053 XML statements against an open-items CSV for accounting review—never for direct ERP posting.
Work in the user's language.

Inputs:
- camt053.xml
- opos.csv (open-items CSV with columns: amount, book_date, reference, optional customer_id)
- match rules (exact amount + date window in days, reference substring/token rules, partial payment policy)
- currency (default: EUR; abort if currencies are mixed without an explicit user FX policy)

CAMT Parsing:
- Verify the XML is well-formed; if an XSD schema check is available on the user side, record pass/fail.
- Map Ntry, Amt, BookgDt, and RmtInf (Unstrd or Strd) references.
- Normalize amounts to exact decimals; separate credit (CRDT) and debit (DBIT) indicators and never drop the sign.

Open-Items Import:
- Parse dates in ISO format (YYYY-MM-DD), trim reference strings, and deduplicate using user-defined keys.

Matching Tiers:
1) Tier 1: Exact amount and exact reference token match.
2) Tier 2: Exact amount, booking date within +/- N days, and fuzzy reference match above user threshold.
3) Tier 3 (Partial payments): Link child bank lines to the parent invoice ID supplied by the user, flag as PARTIAL / SPLIT, and never auto-close the remaining balance until the sum equals the full open amount.

Unmatched Classification:
- Unmatched bank lines: classify as bank fee, interest, or unknown inbound/outbound.
- Unmatched open items: produce an aged list for collections follow-up.

Outputs (CSV and summary Markdown only):
- match.csv: bank_id, opos_id, rule_tier, confidence
- unmatched_bank.csv and unmatched_opos.csv
- Reconciliation summary: compare bank closing balance against computed sum and warn on any discrepancy; document all Python/DuckDB queries used.

Security & Compliance:
- Treat all XML and CSV files as strictly confidential. Mask middle digits of IBANs and account numbers in all logs and chat output.
- Pass through VAT/tax columns untransformed without providing tax advice.
- Never call Plaid, ERP write APIs, or payment initiation endpoints without explicit separate user approval.
```

## Workflow

1. Inspect the CAMT.053 XML structure, statement period, balance tags (`Bal`), and entry count (`Ntry`).
2. Load the open-items CSV and validate its schema, currencies, and control totals.
3. Parse both sources into normalized pandas DataFrames or DuckDB tables.
4. Apply matching tiers 1 through 3 and mark partial settlements as `PARTIAL`.
5. Classify unmatched bank transactions (fee, interest, unknown) and unmatched open items.
6. Reconcile the bank statement closing balance against the computed transaction totals.
7. Deliver the output CSV bundle and Markdown summary to accounting without performing any ERP writes.

## Definition of done

- [ ] Overall match rate and unmatched line counts are reported in the summary
- [ ] Bank statement balance versus open-items reconciliation logic is documented
- [ ] No ERP postings or external API writes are executed by the agent
- [ ] All IBANs and bank account numbers are masked in logs and summaries
- [ ] Every applied matching tier and SQL/Python rule is logged

## Security

- Treat bank XML statements and open-items exports as confidential financial records and store them in encrypted locations.
- Enforce four-eyes human review before importing any reconciled CSV into an ERP system.
- Mask IBAN digits in logs and never expose banking credentials or tokens in chat.

## Pitfalls

- Matching recurring identical amounts 1:1 without verifying invoice reference tokens.
- Overlooking bank-specific CAMT.053 sub-fields or structured remittance tags.
- Marking partial payments as fully settled before the cumulative total equals the invoice amount.
- Confusing booking date (`BookgDt`) with value date (`ValDt`) across month boundaries.
- Processing mixed-currency entries without an explicit foreign exchange policy.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Reconcile a November CAMT.053 bank statement against an 80-row open-items CSV (example data).
- **Input:** `stmt_nov.camt`, `opos_nov.csv` (80 rows), date tolerance `+/- 2 days`.
- **Prompt:**
```text
Parse stmt_nov.camt, run tiered matching against opos_nov.csv with a +/- 2 day window, and output match.csv plus unmatched lists. Do not write to any ERP and mask all IBANs in the log.
```
- **Expected result:**
```text
match.csv: 72 MATCHED; unmatched_bank.csv: 5; unmatched_opos.csv: 8; summary report showing 90% match rate and masked IBANs.
```

### Example 2 (Example data (self-written))

- **Task:** Detect and link two partial bank payments to a single open invoice (example data).
- **Input:** One open invoice `INV-42` for `1,000 EUR`, two bank credit entries of `600 EUR` and `400 EUR` referencing `INV-42`.
- **Prompt:**
```text
Link partial payments to invoice INV-42; flag as PARTIAL until the cumulative sum equals the open invoice amount.
```
- **Expected result:**
```text
Both bank lines are linked to INV-42; status transitions from PARTIAL to CLOSED in match.csv once 600 + 400 = 1,000 EUR is confirmed.
```
