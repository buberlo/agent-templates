---
id: google-workspace-docs-workflow
title: "Google Docs and Sheets bearbeiten"
domain: office-documents
category: google-workspace-docs
tags:
  - google-docs
  - google-sheets
  - workspace
target_agents:
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Google Docs MCP
    install: "OAuth via Google connector"
    version_notes: "Read/write docs"
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "Export snapshot"
inputs:
  - "Doc/Sheet ID or URL"
  - "Aenderungsauftrag"
  - "approval Schreibzugriff"
outputs:
  - "Aktualisiertes Dokument"
  - "Aenderungsprotokoll"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Google Workspace-Dokumente** over MCP bearbeiten—read, strukturiert aendern, changes protokollieren—with OAuth, not with Passwort im Chat.

## When to use

- Team-Docs in Google Docs/Sheets bereits canonical.
- Agent has Google MCP with User-OAuth.
- Offline-DOCX not erforderlich.

**When not to use**

- Air-gapped without Google.
- Massenmigration to Microsoft 365 without Export-Spec.
- Oeffentliche Docs without Rechtepruefung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Google Docs MCP | Edit | Official Connector |
| Google Drive MCP | Discovery | files finden |
| MarkItDown | Snapshot | Backup before Edit |

## System prompt

```text
You edit Google Docs/Sheets via MCP with user OAuth—never ask for Google password in chat.

Inputs: document URL or id, change spec (section, table rows, cell range), mode read|suggest|apply, approval for apply.

Before write:
- Export read-only snapshot via MCP or MarkItDown to local backup path if user agrees.
- List current heading structure or sheet names.

Edits:
- Docs: prefer paragraph-level or table operations; preserve unrelated content; track what changed in changelog.md.
- Sheets: never overwrite entire sheet without backup; range-specific updates; formulas preserved unless user requests values-only.

Comments mode: if user wants suggestions only, use comment APIs or output diff for human paste—do not apply.

Sharing: never broaden sharing permissions unless explicit.

Approvals: apply edits, share link, or delete requires yes.

Output: changelog with timestamps, link to doc, sections touched.

Rate limits: batch edits; sleep if API errors.

Do not exfiltrate full doc to public paste sites.

If MCP unavailable, stop with setup instructions—not scraped login.

Redact PII in changelog excerpts.
Confirm document id matches user intent before write.
For Sheets: note if IMPORTRANGE external—do not break without user ok.
```

## Workflow

1. Doc/Sheet ID from URL parsen.
2. OAuth MCP Verbindung bestaetigen.
3. Lesen: Outline or Sheet-Inventory.
4. Snapshot-Backup when freigegeben.
5. changes anwenden or Diff liefern.
6. changelog.md write.
7. User Link zur Pruefung.

## Definition of done

- [ ] Korrektes Dokument bearbeitet (ID match)
- [ ] Changelog with Abschnitten/Zellen
- [ ] no Sharing-Aenderung without approval
- [ ] Backup when vereinbart
- [ ] no Passwort im Chat

## Security

- OAuth only; Tokens not loggen.
- Write after approval.
- DSGVO at PII in Docs.

## Pitfalls

- Falsches Tab in Sheet.
- Suggest-Modus vergessen → direkte Aenderung.
- IMPORTRANGE bricht at Loeschen.
- Concurrent edits of Menschen.
- MCP Scope to breit.

## Basic examples

### Example 1 (Example data)

- **Task:** FAQ-Abschnitt in Doc aktualisieren.
- **Input:** Doc URL, neuer Absatz unter „Support“.
- **Prompt:**

```text
Read outline, backup snapshot, insert paragraph under Support heading; changelog only.
```

- **Expected result:**

```text
Doc updated; changelog: +1 paragraph Support; backup/faq_snapshot.md.
```

### Example 2 (Example data)

- **Task:** Sheet-Zelle without Backup ablehnen.
- **Input:** Aenderung an ganze Sheet without backup flag.
- **Prompt:**

```text
Require backup=yes before overwriting range Budget!A1:Z500.
```

- **Expected result:**

```text
No write; message: set backup=yes or narrow range.
```