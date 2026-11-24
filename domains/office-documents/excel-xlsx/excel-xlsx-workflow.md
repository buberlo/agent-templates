---
id: excel-xlsx-workflow
title: "Excel-Arbeitsmappen erstellen and verify"
domain: office-documents
category: excel-xlsx
tags:
  - xlsx
  - openpyxl
  - formulas
target_agents:
  - hermes
  - claude-code
  - generic
required_tools:
  - name: Anthropic document skills (xlsx)
    install: "https://github.com/anthropics/skills"
    version_notes: "xlsx validate path"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "openpyxl / xlsx_recalc"
inputs:
  - "Datenquelle or Spezifikation"
  - "Sheet-Layout and Formeln"
outputs:
  - "Valide .xlsx"
  - "Recalc- or Read-Log"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Tabellen, Formeln and Charts** in XLSX zuverlaessig create—Daten and Berechnungslogik trennen, values after Recalc re-checked.

## When to use

- KPI-Reports, Preislisten or Datenbereinigung as Arbeitsmappe.
- Agent schreibt file; User oeffnet in Excel/LibreOffice zur Endkontrolle.
- no Live-ERP-Connector required.

**When not to use**

- Echtzeit-DWH or Millionenzeilen without dediziertes BI-Tool.
- Makros/VBA-Produktion without Sandbox-approval.
- Finanzielles Reporting without 4-Augen (→ finanzen-Templates).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic xlsx-Skill | Write + Validate | Official path |
| Hermes xlsx CLIs | read/recalc | Formeln verify |
| LibreOffice Calc | Optional Recalc | when xlsx_recalc fehlt |
| pandas | Daten-ETL | before the Write |

## System prompt

```text
You build Excel .xlsx workbooks with clear separation: Data sheets vs Calculation sheets vs Presentation.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: schema (sheet names, columns, types), formulas as explicit text (=SUM(Data!B2:B100)), chart spec optional, output path, locale (de-DE: semicolon formulas only if user opens in DE Excel—prefer comma in file for openpyxl unless user says DE Excel).
Write rules:
- Named ranges for formula inputs when >3 references.
- No volatile INDIRECT unless user requests.
- Format numbers as number not text (watch leading zeros in IDs).
After write:
- Run xlsx_read.py or skill read: dump calculated values if available.
- Run xlsx_recalc.py or instruct user to open in Excel when formulas show None.
- Spot-check 3 cells: total row, edge case, empty input.
Charts: data range must match table size; no chart on blank headers.
Approvals: email workbook, connect live APIs, or delete source data only with user yes.
Never embed credentials in connection strings.
Output: path, sheet list, formula cells sampled, recalc status (OK|PENDING_USER).
Validate table boundaries: no merged cells in data region unless template requires.
Document openpyxl vs skill path used.
If CSV import sheet: freeze header row and apply autofilter.
Watch Excel serial dates: convert ISO in pandas before write.```

## Workflow

1. Daten in pandas normalisieren (Datum, Dezimal).
2. Skill/CLI: Struktur Sheets `Data`, `Calc`, `Report` anlegen.
3. Formeln eintragen; no hartcodierten Summen in Report.
4. `xlsx_read.py` or Skill-Read: Stichprobe values.
5. `xlsx_recalc.py` or Calc-Oeffnung anfordern when #NAME? droht.
6. Validator/Skill-Check falls verfuegbar.
7. path + Recalc-Status an User.

## Definition of done

- [ ] Formelzellen liefern erwartete Stichproben (or PENDING_USER dokumentiert)
- [ ] no Text-Zahlen in Summen-Spalten
- [ ] Sheet-Namen and Bereiche wie Spezifikation
- [ ] no Versand without approval
- [ ] Read/Recalc-Log vorhanden

## Security

- no PII in Test-Workbooks im Repo.
- Finanz-Sheets only after approval versenden.
- MCP/Skills minimal (office only).

## Pitfalls

- openpyxl speichert Formeln without berechneten Wert.
- DE Excel trennt Argumente with `;` when Oeffnen—Quelldatei konsistent halten.
- Charts on leeren Bereich → leere Grafik.
- Grosse files without Kompression langsam.
- Filter verstecken Zeilen the Summen brauchen.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Umsatzreport Q4 from CSV.
- **Input:** `sales_q4.csv`, Report with SUM and Pivot-light.
- **Prompt:**

```text
Build report.xlsx: Data sheet from CSV, Report with =SUM(Data!amount) and monthly subtotals. Recalc and read back total cell.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.report.xlsx; read log shows Report!B20 matches manual sum of CSV; recalc OK or PENDING_USER noted.
```

### Example 2 (Example data (self-written))
- **Task:** Fehlerhafte Formel before delivery stoppen.
- **Input:** Spec verlangt =VLOOKUP aber Schluesselspalte fehlt.
- **Prompt:**

```text
Pre-flight schema; abort if lookup key column missing in Data sheet.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.No xlsx written; error lists missing column product_id.
```