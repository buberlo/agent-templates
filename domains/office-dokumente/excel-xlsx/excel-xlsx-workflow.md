---
id: excel-xlsx-workflow
domain: office-dokumente
title: "Excel-Arbeitsmappen erstellen und prüfen"
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
  - "Datenquelle oder Spezifikation"
  - "Sheet-Layout und Formeln"
outputs:
  - "Valide .xlsx"
  - "Recalc- oder Read-Log"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Tabellen, Formeln und Charts** in XLSX zuverlässig erzeugen—Daten und Berechnungslogik trennen, Werte nach Recalc gegenlesen.

## Wann nutzen

- KPI-Reports, Preislisten oder Datenbereinigung als Arbeitsmappe.
- Agent schreibt Datei; Nutzer öffnet in Excel/LibreOffice zur Endkontrolle.
- Kein Live-ERP-Connector nötig.

**Wann nicht**

- Echtzeit-DWH oder Millionenzeilen ohne dediziertes BI-Tool.
- Makros/VBA-Produktion ohne Sandbox-Freigabe.
- Finanzielles Reporting ohne 4-Augen (→ finanzen-Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic xlsx-Skill | Schreiben + Validate | Offizieller Pfad |
| Hermes xlsx CLIs | read/recalc | Formeln prüfen |
| LibreOffice Calc | Optional Recalc | Wenn xlsx_recalc fehlt |
| pandas | Daten-ETL | Vor dem Schreiben |

## System-Prompt / Instruktionen

```text
You build Excel .xlsx workbooks with clear separation: Data sheets vs Calculation sheets vs Presentation.

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
Watch Excel serial dates: convert ISO in pandas before write.
```

## Arbeitsablauf

1. Daten in pandas normalisieren (Datum, Dezimal).
2. Skill/CLI: Struktur Sheets `Data`, `Calc`, `Report` anlegen.
3. Formeln eintragen; keine hartcodierten Summen in Report.
4. `xlsx_read.py` oder Skill-Read: Stichprobe Werte.
5. `xlsx_recalc.py` oder Calc-Öffnung anfordern wenn #NAME? droht.
6. Validator/Skill-Check falls verfügbar.
7. Pfad + Recalc-Status an Nutzer.

## Qualitätskriterien / Definition of Done

- [ ] Formelzellen liefern erwartete Stichproben (oder PENDING_USER dokumentiert)
- [ ] Keine Text-Zahlen in Summen-Spalten
- [ ] Sheet-Namen und Bereiche wie Spezifikation
- [ ] Kein Versand ohne Freigabe
- [ ] Read/Recalc-Log vorhanden

## Sicherheit & Freigaben

- Keine PII in Test-Workbooks im Repo.
- Finanz-Sheets nur nach Freigabe versenden.
- MCP/Skills minimal (office only).

## Fallstricke

- openpyxl speichert Formeln ohne berechneten Wert.
- DE Excel trennt Argumente mit `;` beim Öffnen—Quelldatei konsistent halten.
- Charts auf leeren Bereich → leere Grafik.
- Große Dateien ohne Kompression langsam.
- Filter verstecken Zeilen die Summen brauchen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Umsatzreport Q4 aus CSV.
- **Input:** `sales_q4.csv`, Report mit SUM und Pivot-light.
- **Prompt:**

```text
Build report.xlsx: Data sheet from CSV, Report with =SUM(Data!amount) and monthly subtotals. Recalc and read back total cell.
```

- **Erwartetes Ergebnis:**

```text
report.xlsx; read log shows Report!B20 matches manual sum of CSV; recalc OK or PENDING_USER noted.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerhafte Formel vor Auslieferung stoppen.
- **Input:** Spec verlangt =VLOOKUP aber Schlüsselspalte fehlt.
- **Prompt:**

```text
Pre-flight schema; abort if lookup key column missing in Data sheet.
```

- **Erwartetes Ergebnis:**

```text
No xlsx written; error lists missing column product_id.
```