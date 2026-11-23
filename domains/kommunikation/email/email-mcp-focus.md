---
id: email-mcp-focus
title: "E-Mail: MCP/Skill-Fokus"
domain: kommunikation
category: email
tags:
  - email
  - kommunikation
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skills email-inbox-triage und himalaya
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub-Zahlen: Leaderboard 23.11.2026."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
inputs:
  - "Kontext/Briefing für E-Mail"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**E-Mail-Stacks gezielt auswählen**: Hermes Triage + Himalaya (IMAP) oder **gws** / Gmail-MCP—Skills für Workflow, MCP für OAuth-Anbindung; Standard bleibt **Entwurf, kein Senden**.

## Wann nutzen

- Agent soll nur die passenden E-Mail-Tools aktivieren (include/exclude, Tool-Policy).
- Mix aus Workspace (gws) und Drittanbieter-IMAP.
- Dokumentation, welcher Pfad Gmail MCP vs. Himalaya ist.

**Wann nicht**

- Ein einzelnes, wiederkehrendes Triage-Szenario mit festen Queries → Template `email-gmail-mcp-triage`.
- Kein eingerichtetes OAuth oder IMAP-Passwort-Handling.
- Hochriskante Massenkommunikation.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| email-inbox-triage | Priorisierung, Entwürfe | Bundled Hermes-Workflow |
| Himalaya / imap-smtp-email | IMAP/SMTP CLI | OpenClaw/ClawHub, kein Google-only |
| gws CLI | Gmail, Calendar, Drive | Workspace-Inbox in einem CLI |
| Grok Gmail-Plugin | Chat-gebundenes Lesen/Schreiben | Offizieller OAuth-Connector |

## System-Prompt / Instruktionen

```text
You configure and use email tools for kommunikation/email: Hermes email-inbox-triage, himalaya CLI, gws, or Gmail MCP—pick the minimum set for the task.

Inputs: mailbox type (gmail_oauth | imap | workspace_gws), allowed actions (read | draft | label | send), credential location (never paste secrets).

Decision:
- Gmail with MCP available → MCP search + create_draft.
- Generic IMAP → himalaya envelope list + folder sync; draft via SMTP only after approval.
- Workspace admin tasks → gws gmail users.messages.list.

Always:
1) List which tools you enable and why.
2) Read before write; summarize in German if user writes German.
3) create_draft / save to Drafts; send only on explicit "SEND message_id".

Output: tool-choice.md (one page), command log redacted, artifact paths.
Disable unused MCPs to reduce prompt injection surface.
Verify: re-fetch draft or list folder after write.
```

## Arbeitsablauf

1. Anforderung klären: Gmail-OAuth, IMAP oder gws.
2. Hermes MCP-Filter setzen: nur `gmail` oder `himalaya` inkludieren.
3. `gws gmail users.messages.list --user me --query "is:unread"` oder `himalaya envelope list`.
4. Skill **email-inbox-triage** für Priorisierung und Entwurfstexte.
5. Entwurf anlegen (MCP `create_draft` oder Himalaya Draft-Ordner).
6. Ergebnisliste `output/email-session.md` mit Tool-Pfad dokumentieren.
7. Send-Schritt nur nach Nutzerfreigabe mit Message-ID.

## Qualitätskriterien / Definition of Done

- [ ] Aktivierte Tools dokumentiert und begründet
- [ ] Keine Credentials in Chat oder Skill-Dateien
- [ ] Mindestens ein verifizierter Lesezugriff (Message-Count oder Snippet)
- [ ] Schreibaktionen nur als Entwurf oder mit Freigabe

## Sicherheit & Freigaben

- IMAP-App-Passwörter nur in Secret Store, nicht in argv.
- Grok/OAuth-Tokens bleiben auf Connector-Backend.
- PII in Agent-Logs minimieren; Himalaya-Logs rotieren.

## Fallstricke

- Skill und MCP parallel für dasselbe Konto → doppelte Aktionen.
- Himalaya ohne TLS → Credentials im Klartext.
- gws ohne richtiges `GOOGLE_APPLICATION_CREDENTIALS` → scheinbar leere Inbox.
- OpenClaw-ClawHub-Skills ohne `skills verify` laden.
- Senden aus Versehen, wenn MCP-Send-Tool nicht aus Policy entfernt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** IMAP-Firmenpostfach triagieren.
- **Input:** Server `mail.firma.example`, Skill Himalaya aktiv.
- **Prompt:**

```text
Enable only himalaya + email-inbox-triage. List unread INBOX, classify, save reply drafts locally as .eml for review.
```

- **Erwartetes Ergebnis:**

```text
Tools: himalaya, email-inbox-triage (gmail MCP disabled)
Unread: 17 | Drafts saved: output/drafts/re-28401.eml, re-28402.eml
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Workspace-Inbox lesen ohne Send-Tool.
- **Input:** gws installiert, Policy: read+draft only.
- **Prompt:**

```text
gws list 5 newest unread, summarize subjects in German, no send tools in session.
```

- **Erwartetes Ergebnis:**

```text
1) Onboarding docs — Alice
2) Invoice #8821 — finance@
...
Send tools: none bound this session
```