---
id: email-gmail-mcp-triage
title: "Posteingang triagieren mit Gmail MCP"
category: email-kommunikation
tags:
  - gmail
  - mcp
  - triage
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: gmail-mcp
    install: "MCP: Gmail"
    version_notes: "search_emails, drafts, labels"
  - name: google-calendar
    install: "MCP optional"
    version_notes: "Terminvorschläge"
inputs:
  - "Label/Query"
  - "Prioritätsregeln"
  - "Signatur"
outputs:
  - "Label-Struktur"
  - "Entwürfe Antworten"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

E-Mail-Flut strukturieren, Routineantworten als Entwurf vorbereiten und Follow-ups planen.

## Wann nutzen

- Support-Postfach, Führungskraft-Inbox.
- Nicht für Massenmail ohne Opt-in (Spam-Risiko).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Gmail MCP | Lesen/Schreiben | OAuth, auditierbar |
| Regelsatz YAML | Triage | Transparent |
| Tasks/Notion | Follow-up | SLA-Tracking |

## System-Prompt / Instruktionen

```text
Triage Gmail with MCP search_emails; never send without user send confirmation.
Apply labels: Action/Waiting/FYI per rules file.
Draft replies in user tone; cite ticket IDs.
Redact PII in summaries shared externally.
```

## Arbeitsablauf

1. Query der letzten 48 h analysieren.
2. Labels setzen; Newsletter archivieren.
3. Entwürfe für Top 10 Action-Mails.
4. Zusammenfassung an Nutzer.
5. Send nur nach explizitem OK.

## Qualitätskriterien / Definition of Done

- [ ] Inbox Zero oder vereinbarter Rückstand
- [ ] Keine ungesendeten Antworten ohne Review
- [ ] Regeln dokumentiert

## Sicherheit & Freigaben

- MCP-OAuth scoped minimal.
- Kein Auto-Forward sensibler Inhalte.

## Beispiele

**Eingabe:** Query `is:unread -category:promotions`
**Erwartetes Ergebnis:** 12 Action, 5 Entwürfe, Summary MD
