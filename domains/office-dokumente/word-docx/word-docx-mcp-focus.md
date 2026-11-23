---
id: word-docx-mcp-focus
title: "Word DOCX: MCP- und Skill-Fokus"
domain: office-dokumente
category: word-docx
tags:
  - docx
  - validate
  - libreoffice
target_agents:
  - hermes
  - claude-code
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (docx)
    install: "https://github.com/anthropics/skills"
    version_notes: "validate.py, npm docx"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "python-docx CLIs"
  - name: LibreOffice
    install: "apt/brew: libreoffice"
    version_notes: "soffice headless für PDF/PNG"
  - name: pdftoppm
    install: "poppler-utils"
    version_notes: "Visuelle QA nach Render"
inputs:
  - "Inhaltsbriefing oder Vorlagen-Pfad"
  - "Layout-Vorgaben (A4, Tabellenbreiten)"
  - "Freigabe vor Versand"
outputs:
  - "Valide .docx"
  - "Optional PDF/PNG für Sichtprüfung"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**DOCX erzeugen und absichern** mit offiziellen docx-Skills: strukturiert schreiben, **validate.py**, PDF-Render und Bildprüfung—Layoutfehler (Tabellenbreiten) vor Auslieferung fangen.

## Wann nutzen

- Berichte, Briefe oder Briefings sollen als .docx mit Corporate-Struktur entstehen.
- Agent wählt zwischen Anthropic docx-Skill und Hermes microsoft-office.
- Qualitätssicherung per Validator + visueller Render-Pipeline verlangt wird.

**Wann nicht**

- Serienbrief mit CSV-Datenquelle (→ dokumente-libreoffice-mail-merge).
- Komplexe Vertrags-Track-Changes mit Anwälten in Word Desktop only.
- Automatischer E-Mail-Versand des Dokuments ohne Freigabe-Workflow.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic docx-Skill | Erzeugung + validate.py | Offizieller Verify-Pfad |
| Hermes microsoft-office | python-docx Skripte | Ohne Microsoft Office |
| LibreOffice soffice | PDF-Export | Visuelle QA |
| pdftoppm | PNG aus PDF | Tabellen-Rand prüfen |

## System-Prompt / Instruktionen

```text
You produce Word .docx files using Anthropic docx skill or Hermes microsoft-office CLIs—never raw ZIP hacking unless emergency and user approves.

Inputs: content outline (title, H1 sections, lists, tables with column widths in DXA), page size (A4 default per skill docs), output path, whether to render PDF/PNG for QA.

Structure:
- One clear H1 per major section unless user template specifies else.
- Tables: total table width must not exceed printable text width (A4 ~9026 DXA content area typical); sum of column DXA must match table width—tutorial case fixed 11520→9360 DXA when Context column clipped.

After generation:
- Run validate.py / docx_validate.py from skill; all checks PASS required before calling done.
- soffice --headless --convert-to pdf output.docx
- pdftoppm -png output.pdf qa/page
- Inspect qa PNG for table overflow, heading orphans, footer page numbers.

Edits: prefer regenerating sections over manual OOXML unless user demands track changes.

Approvals: email, share drive, or delete drafts only after user confirms content and layout.

Security: no credentials in document body; redact sample data.

Output: docx path, validator summary (paragraph count), render paths, known layout warnings.

Do not change contractual legal text without lawyer review flag from user.

German typography: use proper quotes and hyphenation settings if template provides.
Keep styles semantic (Heading1, List Paragraph) not ad-hoc bold runs.
If Hermes path: run bundled read script and echo sheet/section inventory.
```

## Arbeitsablauf

1. Briefing in Gliederung mit Tabellen-Spaltenbreiten (DXA) festhalten.
2. docx-Skill oder `docx_write.py` ausführen → `output.docx`.
3. `validate.py output.docx` — bei FAIL Ursache beheben und neu bauen.
4. `soffice --headless --convert-to pdf output.docx`.
5. `pdftoppm` erste Seite mit breiter Tabelle prüfen.
6. Nutzer Freigabe für externe Weitergabe einholen.
7. Artefakte und Validator-Output im Thread dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Validator: All validations PASSED
- [ ] Tabellen sichtbar innerhalb Satzspiegel auf QA-PNG
- [ ] Seitenformat A4 (oder dokumentierte Abweichung)
- [ ] Kein Versand ohne Nutzerfreigabe
- [ ] PDF/PNG-QA-Dateien bei layoutkritischen Tabellen

## Sicherheit & Freigaben

- PII in Beispieltabellen nur mit synthetischen Daten.
- Schreiben/Senden nur nach expliziter Freigabe.
- Skills/MCP minimal halten (nur docx-Scope).

## Fallstricke

- Validator grün, aber Tabelle ragt visuell über den Rand (DXA-Summe).
- Default US Letter in Skill, Nutzer erwartet A4.
- LibreOffice-Render weicht minimal von Word ab—Kunden-Word-Stichprobe bei Verträgen.
- python-docx ersetzt keine komplexen Vorlagen-Content-Controls.
- Große eingebettete Bilder blähen Datei auf ohne Kompression.

## Grundbeispiele

### Beispiel 1 (Praxisbeispiel)

- **Aufgabe:** Briefing-DOCX wie im Anthropic-Tutorial erzeugen und validieren.
- **Input:** Titel, zwei H1-Abschnitte, Listen, Preistabelle mit Spalten-DXA.
- **Prompt:**

```text
Create briefing.docx per outline; run validate.py; render PDF and pdftoppm; fix table width if Context column clipped.
```

- **Erwartetes Ergebnis:** `briefing.docx` (~10 KB), 25 Absätze, All validations PASSED; nach DXA-Korrektur sichtbare Context-Spalte.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Hermes microsoft-office Pfad für internes Memo ohne Anthropic Plugin.
- **Input:** Gliederung 3 Abschnitte, keine Tabelle.
- **Prompt:**

```text
Use Hermes docx CLI to write memo.docx; read back paragraph count; optional soffice pdf for archive.
```

- **Erwartetes Ergebnis:**

```text
memo.docx present; read script reports ≥3 Heading1 sections; memo.pdf optional in out/.
```