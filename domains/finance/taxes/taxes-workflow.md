---
id: taxes-workflow
title: "Organize tax data (not advice)"
domain: finance
category: taxes
tags:
  - tax
  - org
  - gobd
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Tables"
inputs:
  - "Receipt and document index list"
  - "Category mapping from tax advisor"
outputs:
  - "Structured handoff package index"
  - "Open questions list for tax advisor"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Structure receipts, invoices, and transaction lists for handoff to a tax advisor**—generating sorted package indexes, missing-receipt checklists, and open questions while providing **strictly zero tax advice, tax calculations, or automated tax filings**.

## When to use

- Preparing annual or quarterly document packages for an external tax advisor or accounting firm.
- Sorting and indexing expense receipts against a written category list supplied by the tax advisor.
- Preparing an immutable, GoBD-compliant document inventory with optional SHA-256 file hashes.

### When not to use

- Calculating substantive VAT returns or tax liabilities without a certified tax advisor.
- Requesting legal opinions or interpretations of tax statutes.
- Submitting automated tax filings (e.g., via ELSTER or government tax portals) through an agent.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `pandas` | Document inventory and gap checks | Matches ledger lines against receipt files and advisor categories |
| DATEV export workflow | Optional accounting handoff | Connects structured receipt lists with `finance-datev-export-csv` |
| PDF reader skill | Read receipt metadata | Extracts document dates, invoice totals, and merchant names in read-only mode |

## System prompt

```text
You organize tax-related documents and receipt inventories for handoff to a certified tax advisor—you NEVER provide tax advice, interpret tax law, or submit tax filings.
Work in the user's language (default to English).

Inputs:
- receipt_index.csv and file paths
- categories_map provided by the tax advisor
- fiscal period (FY / quarter)
Outputs:
- handoff.md
- package_index.csv
- open_questions.md

Strict Rules:
1. Mandatory Disclaimer: State clearly at the top of handoff.md that the output is purely organizational and that all tax liability, deductibility, and filing decisions rest with a certified tax advisor.
2. Classification: Assign category codes strictly from the user's tax-advisor mapping table. Never invent tax interpretations or suggest aggressive/unverified deductions.
3. Ambiguous Items: Place any unmapped merchant, unclear expense, or missing tax key into open_questions.md for human and tax advisor review.
4. Business vs. Private: Separate business and private expenses only if an explicit column is provided in the input—never guess.
5. Dates & Flags: Keep document_date (invoice date) and payment_date in distinct columns. Mark small-business VAT exemption status as UNKNOWN unless explicitly set by the user.
6. Missing Receipts & Integrity: Flag every expense row lacking a linked receipt file. Never delete or modify source PDF files. Optionally compute SHA-256 file hashes when requested for GoBD audit trail compliance.
7. VAT ID Check: Validate VAT ID string format (syntax) only; note that official authority verification must be performed separately.
8. Folder Structure & Transfer: Document the folder hierarchy required by the accounting firm. Never submit filings to tax authorities (such as ELSTER) or transmit archives externally without explicit user approval and selection of a secure transfer channel.
```

## Workflow

1. Validate the input receipt index CSV and verify that all referenced source PDFs exist without modifying or deleting any files.
2. Map transactions strictly to the category codes supplied by the tax advisor.
3. Identify and list all expense rows that are missing a corresponding receipt document.
4. Export `package_index.csv` keeping `document_date` and `payment_date` distinct and optionally including SHA-256 file hashes.
5. Generate `handoff.md` with the mandatory non-advisory disclaimer and folder structure overview.
6. Compile `open_questions.md` for unmapped merchants, missing receipts, or ambiguous items.
7. Hand off the local package to the user for transfer to their tax advisor over an approved secure channel.

## Definition of done

- [ ] Non-advisory tax disclaimer is prominently included in `handoff.md`
- [ ] Zero automated tax portal or ELSTER submissions are attempted
- [ ] Ambiguous items and missing receipts are listed in `open_questions.md`
- [ ] Categories are assigned exclusively from the user/advisor mapping table
- [ ] Source PDF receipts remain untouched and external transfer awaits explicit user action

## Security

- Treat tax records as high-risk confidential financial data; restrict the agent strictly to local document organization.
- Comply with statutory record-retention and non-deletion rules (such as GoBD); never delete or overwrite source receipt PDFs.
- Require explicit user action to transfer any archive to the tax advisor over an encrypted channel.

## Pitfalls

- Allowing the agent to act as a tax advisor or opine on tax deductibility.
- Inventing tax categories not present in the advisor's mapping file.
- Confusing document/invoice date with cash payment date across reporting period boundaries.
- Guessing whether an ambiguous transaction is business or private instead of routing it to `open_questions.md`.
- Failing to flag ledger expenses that lack a supporting receipt file.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Organize a Q3 receipt package for the tax advisor (example data).
- **Input:** `receipts_index.csv`, `categories_advisor.yaml` (example data).
- **Prompt:**
```text
Generate package_index.csv, handoff.md, and open_questions.md from receipts_index.csv and categories_advisor.yaml. Include the non-advisory disclaimer and provide no tax advice.
```
- **Expected result:**
```text
package_index.csv sorted with distinct document_date and payment_date columns; handoff.md includes the non-advisory disclaimer and missing-receipt count; open_questions.md lists unmapped merchants for the tax advisor.
```

### Example 2 (Example data (self-written))

- **Task:** Refuse a request to calculate a substantive VAT return and list data gaps instead (example data).
- **Input:** User prompt asks the agent to calculate and file the quarterly VAT return.
- **Prompt:**
```text
Refuse the VAT return calculation and filing; output only a list of missing receipt and data gaps for the tax advisor.
```
- **Expected result:**
```text
Refusal message stating the agent cannot calculate tax liability or file returns; open_questions.md updated with missing receipt and tax-code gaps for the tax advisor to review.
```
