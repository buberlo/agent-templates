---
id: dokumente-libreoffice-mail-merge
domain: office-dokumente
title: "Serienbrief mit LibreOffice und CSV"
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
  - "ODT-Vorlage mit Platzhaltern"
  - "CSV mit Empfängerfeldern"
  - "Freigabe für Massen-PDF"
outputs:
  - "PDF pro Empfängerzeile"
  - "merge.log mit Fehlerzeilen"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Personalisierte Massenanschreiben** aus ODT + CSV headless erzeugen—PDF pro Zeile, protokollierte Fehler, keine stillen PII-Leaks.

## Wann nutzen

- Einladungen, Mahnungen, Zertifikate aus CRM-Export (CSV).
- LibreOffice auf Server/CI ohne GUI verfügbar.
- E-Mail-Versand erfolgt in separatem, freigegebenem Schritt.

**Wann nicht**

- Direkter SMTP-Massenversand ohne rechtliche Prüfung.
- Komplexe Word-ONLY-Felder (REVNUM, IF) ohne ODT-Migration.
- Echtzeit-Personalisierung während Live-Event ohne Batch-Window.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| LibreOffice Writer | Mail-Merge | Offen, automatisierbar |
| soffice | Headless CLI | PDF-Export |
| CSV | Datenquelle | Einfacher CRM-Export |
| python3 | Vorvalidierung | Spalten vs. Felder |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. CSV-Header mit ODT-Feldliste abgleichen (Mapping-Tabelle).
2. Testlauf 3 Zeilen → `out/test/` PDFs.
3. `pdftotext out/test/*.pdf` Stichprobe Platzhalter.
4. Vollbatch headless in `out/pdf/`.
5. Zeilenzählung: `wc -l kunden.csv` vs. `ls out/pdf | wc -l`.
6. `merge.log` auf ERROR-Zeilen prüfen.
7. Freigabe Fachabteilung vor physischem Versand.

## Qualitätskriterien / Definition of Done

- [ ] 100 % erfolgreicher Zeilen haben PDF (laut Log)
- [ ] Keine unersetzten Merge-Felder in Stichprobe
- [ ] Dateinamen eindeutig und sortierbar
- [ ] CSV/Log nicht öffentlich abgelegt
- [ ] Testlauf dokumentiert vor Vollbatch

## Sicherheit & Freigaben

- CSV enthält PII—Zugriff auf Output-Ordner beschränken.
- Textinhalt vor Massenversand von Fachseite freigegeben.
- Kein Versand ohne separaten Freigabe-Workflow.

## Fallstricke

- UTF-8 BOM in CSV verschiebt ersten Spaltennamen.
- LibreOffice-Makro-Pfad unter headless anders als GUI.
- Tausender-Zeilen-Batch ohne RAM-Limit killt soffice.
- ODT-Feld «City» vs. CSV «Ort» still leer.
- PDF-Namen mit Sonderzeichen auf Windows-Share problematisch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 200 Einladungen aus CRM-CSV.
- **Input:** `brief.odt` (Felder: id, lastname, event_date), `kunden.csv` (200 Zeilen).
- **Prompt:**

```text
Validate fields, test 3 rows, then full merge to out/pdf/{id}_{lastname}.pdf. Log failures per row.
```

- **Erwartetes Ergebnis:**

```text
out/pdf/: 200 PDFs (or 197 + merge.log with 3 ERROR rows); test/ with 3 PDFs documented first.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall fehlende Pflichtspalte.
- **Input:** `brief.odt`, CSV ohne Spalte `lastname`.
- **Prompt:**

```text
Pre-flight only: abort before merge and list missing columns.
```

- **Erwartetes Ergebnis:**

```text
No PDFs written; message: missing header lastname; mapping table diff shown.
```