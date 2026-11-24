---
id: documents-libreoffice-mail-merge
title: "Serienbrief with LibreOffice and CSV"
domain: office-documents
category: word-docx
tags:
  - libreoffice
  - mail-merge
  - odt
  - csv
target_agents:
  - hermes
  - cursor
  - generic
required_tools:
  - name: libreoffice
    install: "apt: libreoffice-writer"
    version_notes: "24.x headless"
  - name: python3
    install: "system"
    version_notes: "Optional UNO-Bridge"
inputs:
  - "ODT-Vorlage with Platzhaltern"
  - "CSV with Empfaengerfieldern"
  - "approval for Massen-PDF"
outputs:
  - "PDF pro Empfaengerzeile"
  - "merge.log with Fehlerzeilen"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Personalisierte Massenanwrite** from ODT + CSV headless create—PDF pro Zeile, protokollierte Fehler, no stillen PII-Leaks.

## When to use

- Einladungen, Mahnungen, Zertifikate from CRM-Export (CSV).
- LibreOffice on Server/CI without GUI verfuegbar.
- E-Mail-Versand erfolgt in separatem, freigegebenem step.

**When not to use**

- Direkter SMTP-Massenversand without rechtliche Pruefung.
- Komplexe Word-ONLY-fields (REVNUM, IF) without ODT-Migration.
- Echtzeit-Personalisierung waehrend Live-Event without Batch-Window.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| LibreOffice Writer | Mail-Merge | Offen, automatisierbar |
| soffice | Headless CLI | PDF-Export |
| CSV | Datenquelle | Einfacher CRM-Export |
| python3 | Vorvalidierung | Spalten vs. fields |

## System prompt

```text
You run LibreOffice Writer mail merge in headless mode on Linux.

Inputs: template.odt with merge fields matching CSV headers, recipients.csv (UTF-8), output directory, filename pattern (default {id}_{lastname}.pdf), test_rows (default 3 before full batch).

Pre-flight:
- Parse CSV header row; compare to template field list from ODT metadata or user mapping table; stop on mismatch.
- Reject rows with empty required fields (configurable list).
- PII: never log full CSV contents in chat—only row counts and error row ids.

Test merge:
- Run first N rows only; open one PDF via pdftotext or user confirmation.
- Verify placeholders replaced (no literal «Field» or «MERGEFIELD» left).

Full batch:
- soffice --headless with mail merge macro or documented CLI path user provides.
- On row failure: log row id and continue unless user requested abort-on-error.
- Export PDF per row; unique filenames.

Post-check: count PDFs vs successful CSV rows minus skips; report delta.

Approvals: mass email send, upload to portal, or delete CSV requires explicit user yes.

Security: chmod output dir; no world-readable merge.log with addresses.

Output: pdf count, merge.log path, sample pdftotext excerpt row 1.

Do not embed secrets in ODT fields.

If UNO bridge used, document Python entrypoint and LO version.

Validate encoding: latin-1 CSV on DE umlauts needs utf-8-sig or iconv first.
```

## Workflow

1. CSV-Header with ODT-Fieldliste abgleichen (Mapping-Tabelle).
2. Testlauf 3 Zeilen → `out/test/` PDFs.
3. `pdftotext out/test/*.pdf` Stichprobe Platzhalter.
4. Vollbatch headless in `out/pdf/`.
5. Zeilenzaehlung: `wc -l kunden.csv` vs. `ls out/pdf | wc -l`.
6. `merge.log` on ERROR-Zeilen verify.
7. approval Fachabteilung before physischem Versand.

## Definition of done

- [ ] 100 % erfolgreicher Zeilen have PDF (according to Log)
- [ ] no unersetzten Merge-fields in Stichprobe
- [ ] filenamen eindeutig and sortierbar
- [ ] CSV/Log not oeffentlich abgelegt
- [ ] Testlauf dokumentiert before Vollbatch

## Security

- CSV enthaelt PII—Zugriff on Output-Ordner beschraenken.
- Textinhalt before Massenversand of Fachseite freigegeben.
- no Versand without separaten approval-Workflow.

## Pitfalls

- UTF-8 BOM in CSV verschiebt ersten Spaltennamen.
- LibreOffice-Makro-path unter headless anders as GUI.
- Tausender-Zeilen-Batch without RAM-Limit killt soffice.
- ODT-Field «City» vs. CSV «Ort» still leer.
- PDF-Namen with Sonderzeichen on Windows-Share problematisch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 200 Einladungen from CRM-CSV.
- **Input:** `brief.odt` (fields: id, lastname, event_date), `kunden.csv` (200 Zeilen).
- **Prompt:**

```text
Validate fields, test 3 rows, then full merge to out/pdf/{id}_{lastname}.pdf. Log failures per row.
```

- **Expected result:**

```text
out/pdf/: 200 PDFs (or 197 + merge.log with 3 ERROR rows); test/ with 3 PDFs documented first.
```

### Example 2 (Example data (self-written))
- **Task:** Fehlerfall fehlende Pflichtspalte.
- **Input:** `brief.odt`, CSV without Spalte `lastname`.
- **Prompt:**

```text
Pre-flight only: abort before merge and list missing columns.
```

- **Expected result:**

```text
No PDFs written; message: missing header lastname; mapping table diff shown.
```