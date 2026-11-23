---
id: word-docx-mcp-focus
title: "Word DOCX: MCP- and Skill-Fokus"
domain: office-documents
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
    version_notes: "soffice headless for PDF/PNG"
  - name: pdftoppm
    install: "poppler-utils"
    version_notes: "Visuelle QA after Render"
inputs:
  - "Inhaltsbriefing or Vorlagen-path"
  - "Layout-Vorgaben (A4, Tabellenbreiten)"
  - "approval before Versand"
outputs:
  - "Valide .docx"
  - "Optional PDF/PNG for Sichtpruefung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**DOCX create and harden** with official docx-Skills: strukturiert write, **validate.py**, PDF-Render and image review—Layoutfehler (Tabellenbreiten) before delivery fangen.

## When to use

- reporte, Briefe or Briefings sollen as .docx with Corporate-Struktur entstehen.
- Agent waehlt zwischen Anthropic docx-Skill and Hermes microsoft-office.
- Qualitaetssicherung per Validator + visual Render-Pipeline verlangt will.

**When not to use**

- Serienbrief with CSV-Datenquelle (→ dokumente-libreoffice-mail-merge).
- Komplexe contract-Track-Changes with Anwaelten in Word Desktop only.
- Automatischer E-Mail-Versand the Dokuments without approval-Workflow.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic docx-Skill | generation + validate.py | Official Verify-path |
| Hermes microsoft-office | python-docx Skripte | Ohne Microsoft Office |
| LibreOffice soffice | PDF-Export | Visuelle QA |
| pdftoppm | PNG from PDF | Tabellen-Rand verify |

## System prompt

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

## Workflow

1. Briefing in Gliederung with Tabellen-Spaltenbreiten (DXA) festhalten.
2. docx-Skill or `docx_write.py` ausfuehren → `output.docx`.
3. `validate.py output.docx` — at FAIL Ursache beheben and neu bauen.
4. `soffice --headless --convert-to pdf output.docx`.
5. `pdftoppm` erste Seite with breiter Tabelle verify.
6. User approval for externe Weitergabe einholen.
7. Artefakte and Validator-Output im Thread document.

## Definition of done

- [ ] Validator: All validations PASSED
- [ ] Tabellen sichtbar innerhalb setspiegel on QA-PNG
- [ ] pagesformat A4 (or documented Abweichung)
- [ ] no Versand without Nutzerfreigabe
- [ ] PDF/PNG-QA-files at layoutkritischen Tabellen

## Security

- PII in Beispieltabellen only with synthetischen Daten.
- Write/Senden only after expliziter approval.
- Skills/MCP minimal halten (only docx-Scope).

## Pitfalls

- Validator gruen, aber Tabelle ragt visuell over the Rand (DXA-Summe).
- Default US Letter in Skill, User erwartet A4.
- LibreOffice-Render weicht minimal of Word ab—Kunden-Word-Stichprobe at Vertraegen.
- python-docx ersetzt no komplexen Vorlagen-Content-Controls.
- Grosse eingebettete Bilder blaehen file on without Kompression.

## Basic examples

### Example 1 (Real-world example)

- **Task:** Briefing-DOCX wie im Anthropic-Tutorial create and validieren.
- **Input:** Titel, zwei H1-Abschnitte, listn, Preistabelle with Spalten-DXA.
- **Prompt:**

```text
Create briefing.docx per outline; run validate.py; render PDF and pdftoppm; fix table width if Context column clipped.
```

- **Expected result:** `briefing.docx` (~10 KB), 25 Absaetze, All validations PASSED; after DXA-Korrektur sichtbare Context-Spalte.
- **Source:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/

### Example 2 (Example data)

- **Task:** Hermes microsoft-office path for internes Memo without Anthropic Plugin.
- **Input:** Gliederung 3 Abschnitte, no Tabelle.
- **Prompt:**

```text
Use Hermes docx CLI to write memo.docx; read back paragraph count; optional soffice pdf for archive.
```

- **Expected result:**

```text
memo.docx present; read script reports ≥3 Heading1 sections; memo.pdf optional in out/.
```