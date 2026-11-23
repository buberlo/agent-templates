---
id: excel-xlsx-mcp-focus
title: "Excel XLSX: Skill- und Tool-Fokus"
domain: office-dokumente
category: excel-xlsx
tags:
  - xlsx
  - skill
  - validate
target_agents:
  - hermes
  - claude-code
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (xlsx)
    install: "https://github.com/anthropics/skills"
    version_notes: "Official xlsx skill"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "xlsx_read, xlsx_recalc"
inputs:
  - "Aufgabenmodus (read|write|validate)"
  - "xlsx-Pfad"
outputs:
  - "Struktur- oder Validierungsbericht"
  - "Optional bearbeitete Datei"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Richtige XLSX-Skills und CLIs auswählen**, Token-Budget schonen, und jeden Schreibvorgang mit **Read/Recalc** absichern.

## Wann nutzen

- Agent soll nur xlsx-relevante Tools laden.
- Audit einer bestehenden Arbeitsmappe vor Weitergabe.
- Entscheidung Anthropic-Skill vs. Hermes-CLI.

**Wann nicht**

- Vollständige BI-Pipeline (→ daten-analytics).
- Live-Spreadsheet-API (Google Sheets → google-workspace-docs).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic xlsx-Skill | Write + validate | Verify in Skill-Pfad |
| Hermes microsoft-office | read/recalc | Bundled CLIs |
| ClawHub Excel Skill | OpenClaw Alternative | Community |
| openpyxl | Fallback read | Struktur ohne Office |

## System-Prompt / Instruktionen

```text
You are the xlsx tool router for office-dokumente/excel-xlsx—pick one primary skill path per task.

Modes:
- audit: read only, list sheets, dimensions, formula cells count, external links flagged
- write: Anthropic xlsx skill OR Hermes write CLI per user environment
- validate: run skill validator; never skip on financial sheets

Enable only xlsx tools; disable unrelated document MCPs to save context.

Audit output table: sheet | rows | cols | has_formulas | external_links

Write handoff: after generation always run read/recalc per Hermes docs—formulas may be unevaluated in file.

For OpenClaw: install verified ClawHub Excel skill only if user names openclaw.

Approvals: overwrite production xlsx, email attachment, or delete backup requires yes.

Security: no API keys in cells; warn on hidden sheets with formulas.

Output: recommended tool path, commands, and audit markdown.

Do not claim SOX compliance—technical checks only.

If external workbook links found, list target paths and stop until user confirms.
Log skill version when validate fails.
Prefer copying source to work/ before mutate.
```

## Arbeitsablauf

1. Nutzerumgebung klären (Claude Code Skill vs. Hermes).
2. Modus audit/write/validate festlegen.
3. Minimalen MCP/Skill-Satz aktivieren.
4. Operation ausführen.
5. read/recalc oder Validator.
6. Bericht mit Sheet-Inventar.
7. Empfehlung für Folgeschritt (workflow template).

## Qualitätskriterien / Definition of Done

- [ ] Tool-Wahl dokumentiert
- [ ] Bei write: read/recalc durchgeführt oder PENDING begründet
- [ ] Externe Links gemeldet
- [ ] Kein Overwrite ohne Freigabe
- [ ] Audit-Tabelle vollständig

## Sicherheit & Freigaben

- Finanz-Workbooks vertraulich behandeln.
- Nur freigegebene Skills aus ClawHub.
- Keine Credentials in Zellen.

## Fallstricke

- Alle Office-MCPs aktiv → hoher Token-Overhead.
- Validator ohne Recalc grün bei leeren Summen.
- Hidden sheets mit alten Daten.
- xlsx als ZIP manuell editieren → Korruption.
- Makros in xlsx—Skill-Pfad oft nicht unterstützt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Audit vor Kundenversand.
- **Input:** `pricing.xlsx`.
- **Prompt:**

```text
Audit mode only: sheets, formula count, external links. Hermes read if available.
```

- **Erwartetes Ergebnis:**

```text
Markdown table: 3 sheets; Calc has 47 formulas; external_links: none; tool: Hermes xlsx_read.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Skill-Routing für Write.
- **Input:** User on Claude Code with document-skills installed.
- **Prompt:**

```text
Recommend Anthropic xlsx path for new model.xlsx; list post-write validate + recalc steps.
```

- **Erwartetes Ergebnis:**

```text
Plan: document-skills xlsx → validate → LibreOffice or xlsx_recalc; no Hermes unless user switches.
```