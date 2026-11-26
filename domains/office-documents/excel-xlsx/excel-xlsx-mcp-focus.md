---
id: excel-xlsx-mcp-focus
title: "Excel XLSX: Skill- and Tool-Fokus"
domain: office-documents
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
  - "xlsx-path"
outputs:
  - "Structure or validation report"
  - "Optional bearbeitete file"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Richtige XLSX-Skills and CLIs auswaehlen**, Token-Budget schonen, and jeden Schreibvorgang with **Read/Recalc** harden.

## When to use

- Agent should only xlsx-relevante Tools laden.
- Audit a bestehenden Arbeitsmappe before Weitergabe.
- Entscheidung Anthropic-Skill vs. Hermes-CLI.

**When not to use**

- Full BI pipeline (→ data-analytics).
- Live-Spreadsheet-API (Google Sheets → google-workspace-docs).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic xlsx-Skill | Write + validate | Verify in Skill-path |
| Hermes microsoft-office | read/recalc | Bundled CLIs |
| ClawHub Excel Skill | OpenClaw Alternative | Community |
| openpyxl | Fallback read | Struktur without Office |

## System prompt

```text
You are the xlsx tool router for office-documents/excel-xlsx—pick one primary skill path per task.

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

## Workflow

1. Nutzerumgebung clarify (Claude Code Skill vs. Hermes).
2. Set audit/write/validate mode.
3. Minimalen MCP/Skill-set enable.
4. Operation ausfuehren.
5. read/recalc or Validator.
6. report with Sheet-Inventory.
7. Empfehlung for episodeschritt (workflow template).

## Definition of done

- [ ] Tool-Wahl dokumentiert
- [ ] at write: read/recalc durchgefuehrt or PENDING begruendet
- [ ] Externe Links gemeldet
- [ ] no Overwrite without approval
- [ ] Audit table complete

## Security

- Finanz-Workbooks vertraulich behandeln.
- only freigegebene Skills from ClawHub.
- no Credentials in Zellen.

## Pitfalls

- all Office-MCPs aktiv → hoher Token-Overhead.
- Validator without Recalc gruen at leeren Summen.
- Hidden sheets with alten Daten.
- xlsx as ZIP manuell edit → Korruption.
- Makros in xlsx—Skill-path oft not unterstuetzt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Audit before Kundenversand.
- **Input:** `pricing.xlsx`.
- **Prompt:**

```text
Audit mode only: sheets, formula count, external links. Hermes read if available.
```

- **Expected result:**

```text
Markdown table: 3 sheets; Calc has 47 formulas; external_links: none; tool: Hermes xlsx_read.
```

### Example 2 (Example data (self-written))
- **Task:** Skill-Routing for Write.
- **Input:** User on Claude Code with document-skills installed.
- **Prompt:**

```text
Recommend Anthropic xlsx path for new model.xlsx; list post-write validate + recalc steps.
```

- **Expected result:**

```text
Plan: document-skills xlsx → validate → LibreOffice or xlsx_recalc; no Hermes unless user switches.
```