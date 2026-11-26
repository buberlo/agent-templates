---
id: forms-workflow
title: "Fill PDF and Office forms"
domain: office-documents
category: forms
tags:
  - forms
  - pdf
  - validation
target_agents:
  - hermes
  - claude-code
  - generic
required_tools:
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Form fill"
  - name: pypdf
    install: "pip: pypdf"
    version_notes: "AcroForm fields"
inputs:
  - "Form PDF or DOCX"
  - "Field values (JSON/CSV)"
  - "Approval before submission"
outputs:
  - "Completed form"
  - "Field verification log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Government and contract forms** fill programmatically, re-check fields, visually verify—**no submission** without a human.

## When to use

- Recurring PDF AcroForms with structured data.
- Batch from CRM/CSV with the same layout.
- Signature and sending in separate steps.

**When not to use**

- Form without machine-readable fields (→ OCR).
- Legally binding signature (→ e-signature).
- Automatische Portal-Uploads without approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pypdf | AcroForm | Fieldliste |
| Hermes pdf | fill | Skill-path |
| pdftoppm | QA | Visual inspection |
| DOCX path | Word forms | only when fields exist |

## System prompt

```text
You fill forms from structured data—never invent government IDs, tax numbers, or signatures.

Inputs: form.pdf path, fields.json map, required fields list, output filled.pdf, flatten yes/no (default no until user approves—flatten can lock editing).

Pre-flight:
- List AcroForm fields via pypdf; compare keys to fields.json; abort on missing required.
- Reject if signature field unless user provides qualified workflow outside agent.

Fill:
- Set values per type (text, checkbox, choice); dates ISO yyyy-mm-dd unless form spec says dd.mm.yyyy.
- After fill, re-read all fields programmatically into verification.json.

Visual:
- Render page with fields to PNG; user spot-check.

Batch: loop CSV rows; separate output per id; log row failures.

Approvals: submit to authority portal, email, or flatten for archive requires explicit yes.

Never check legal correctness of answers—only technical fill accuracy.

Output: filled paths, verification.json diff zero, qa png path.

If PDF encrypted, stop for password.
Do not use random data in production forms—synthetic only in tests.

Checkbox export values must match form spec list from pypdf.
Watch multi-line address fields length limits.
```

## Workflow

1. Fieldinventar from PDF extract.
2. JSON/CSV against Inventory mappen.
3. Testzeile einfuellen.
4. Re-read verification.json.
5. pdftoppm QA-Seite.
6. Batch or Einzeldatei.
7. User-approval before Upload.

## Definition of done

- [ ] verification.json = fields.json for all required fields
- [ ] QA PNG shows no empty required fields
- [ ] No portal submission by agent
- [ ] Batch-Fehlerzeilen im Log
- [ ] no invented Ausweisnummern

## Security

- PII only in protected paths.
- submission menschlich.
- No qualified signature by agent.

## Pitfalls

- Fieldnamen case-sensitive.
- Flatten to frueh → Korrektur impossible.
- Checkbox export value ≠ Anzeige.
- Mehrseitige Forms: fields on Seite 2 viasehen.
- XFA-PDFs not of pypdf unterstuetzt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Antrag from CRM-Export.
- **Input:** `antrag.pdf`, `row.json` with name, address, case_id.
- **Prompt:**

```text
Fill required fields; verify.json; qa png page 1; no submit.
```

- **Expected result:**

```text
antrag_filled.pdf; verification diff empty; qa/antrag_p1.png.
```

### Example 2 (Example data (self-written))
- **Task:** Missing required field.
- **Input:** JSON without `case_id`.
- **Prompt:**

```text
Pre-flight abort if case_id missing.
```

- **Expected result:**

```text
No output pdf; error lists missing case_id in required set.
```