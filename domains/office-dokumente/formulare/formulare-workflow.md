---
id: formulare-workflow
domain: office-dokumente
title: "PDF- und Office-Formulare ausfüllen"
category: formulare
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
  - "Formular-PDF oder DOCX"
  - "Feld-Werte (JSON/CSV)"
  - "Freigabe vor Einreichung"
outputs:
  - "Ausgefülltes Formular"
  - "Feld-Verifikationslog"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Behörden- und Vertragsformulare** programmatisch befüllen, Felder gegenlesen, visuell prüfen—**keine Einreichung** ohne Mensch.

## Wann nutzen

- Wiederkehrende PDF-AcroForms mit strukturierten Daten.
- Batch aus CRM/CSV mit gleichem Layout.
- Signatur und Versand in getrennten Schritten.

**Wann nicht**

- Formular ohne machine-readable fields (→ OCR).
- Rechtsverbindliche Signatur (→ e-signatur).
- Automatische Portal-Uploads ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pypdf | AcroForm | Feldliste |
| Hermes pdf | fill | Skill-Pfad |
| pdftoppm | QA | Sichtprüfung |
| DOCX path | Word forms | Nur wenn Felder existieren |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Feldinventar aus PDF extrahieren.
2. JSON/CSV gegen Inventar mappen.
3. Testzeile einfüllen.
4. verification.json Gegenlesen.
5. pdftoppm QA-Seite.
6. Batch oder Einzeldatei.
7. Nutzer-Freigabe vor Upload.

## Qualitätskriterien / Definition of Done

- [ ] verification.json = fields.json für alle Pflichtfelder
- [ ] QA-PNG ohne leere Pflichtfelder sichtbar
- [ ] Kein Portal-Submit durch Agent
- [ ] Batch-Fehlerzeilen im Log
- [ ] Keine erfundenen Ausweisnummern

## Sicherheit & Freigaben

- PII nur in geschützten Pfaden.
- Einreichung menschlich.
- Keine qualifizierte Signatur durch Agent.

## Fallstricke

- Feldnamen case-sensitive.
- Flatten zu früh → Korrektur unmöglich.
- Checkbox export value ≠ Anzeige.
- Mehrseitige Formulare: Felder auf Seite 2 übersehen.
- XFA-PDFs nicht von pypdf unterstützt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Antrag aus CRM-Export.
- **Input:** `antrag.pdf`, `row.json` mit name, address, case_id.
- **Prompt:**

```text
Fill required fields; verify.json; qa png page 1; no submit.
```

- **Erwartetes Ergebnis:**

```text
antrag_filled.pdf; verification diff empty; qa/antrag_p1.png.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlendes Pflichtfeld.
- **Input:** JSON ohne `case_id`.
- **Prompt:**

```text
Pre-flight abort if case_id missing.
```

- **Erwartetes Ergebnis:**

```text
No output pdf; error lists missing case_id in required set.
```