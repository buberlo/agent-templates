---
id: google-workspace-docs-workflow
domain: office-dokumente
title: "Google Docs und Sheets bearbeiten"
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
  - "Doc/Sheet ID oder URL"
  - "Änderungsauftrag"
  - "Freigabe Schreibzugriff"
outputs:
  - "Aktualisiertes Dokument"
  - "Änderungsprotokoll"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Google Workspace-Dokumente** über MCP bearbeiten—lesen, strukturiert ändern, Änderungen protokollieren—mit OAuth, nicht mit Passwort im Chat.

## Wann nutzen

- Team-Docs in Google Docs/Sheets bereits canonical.
- Agent hat Google MCP mit Nutzer-OAuth.
- Offline-DOCX nicht erforderlich.

**Wann nicht**

- Air-gapped ohne Google.
- Massenmigration zu Microsoft 365 ohne Export-Spec.
- Öffentliche Docs ohne Rechteprüfung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Google Docs MCP | Edit | Offizieller Connector |
| Google Drive MCP | Discovery | Dateien finden |
| MarkItDown | Snapshot | Backup vor Edit |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Doc/Sheet ID aus URL parsen.
2. OAuth MCP Verbindung bestätigen.
3. Lesen: Outline oder Sheet-Inventar.
4. Snapshot-Backup wenn freigegeben.
5. Änderungen anwenden oder Diff liefern.
6. changelog.md schreiben.
7. Nutzer Link zur Prüfung.

## Qualitätskriterien / Definition of Done

- [ ] Korrektes Dokument bearbeitet (ID match)
- [ ] Changelog mit Abschnitten/Zellen
- [ ] Keine Sharing-Änderung ohne Freigabe
- [ ] Backup wenn vereinbart
- [ ] Kein Passwort im Chat

## Sicherheit & Freigaben

- OAuth only; Tokens nicht loggen.
- Schreiben nach Freigabe.
- DSGVO bei PII in Docs.

## Fallstricke

- Falsches Tab in Sheet.
- Suggest-Modus vergessen → direkte Änderung.
- IMPORTRANGE bricht bei Löschen.
- Concurrent edits von Menschen.
- MCP Scope zu breit.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** FAQ-Abschnitt in Doc aktualisieren.
- **Input:** Doc URL, neuer Absatz unter „Support“.
- **Prompt:**

```text
Read outline, backup snapshot, insert paragraph under Support heading; changelog only.
```

- **Erwartetes Ergebnis:**

```text
Doc updated; changelog: +1 paragraph Support; backup/faq_snapshot.md.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Sheet-Zelle ohne Backup ablehnen.
- **Input:** Änderung an ganze Sheet without backup flag.
- **Prompt:**

```text
Require backup=yes before overwriting range Budget!A1:Z500.
```

- **Erwartetes Ergebnis:**

```text
No write; message: set backup=yes or narrow range.
```