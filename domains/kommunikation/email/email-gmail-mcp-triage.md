---
id: email-gmail-mcp-triage
domain: kommunikation
title: "Posteingang triagieren mit Gmail MCP"
category: email
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
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Posteingang-Triage** mit Gmail MCP: ungelesene Threads priorisieren, Labels konsistent setzen und **Antworten nur als Entwurf** vorbereiten—kein Auto-Send.

## Wann nutzen

- Führungs- oder Support-Inbox mit 20+ neuen Mails pro Tag und dokumentierten Prioritätsregeln.
- Gmail MCP (oder Grok Gmail-Plugin) ist OAuth-fähig verbunden.
- Nutzer will eine Kurzübersicht plus fertige Entwürfe, Senden bleibt manuell.

**Wann nicht**

- Cold-Outreach oder Newsletter-Kampagnen ohne Opt-in (Spam-/Compliance-Risiko).
- Rechtlich heikle Inhalte (Anwalt, HR-Disziplinar) ohne Freigabe für KI-Zusammenfassungen extern.
- IMAP-only ohne MCP: dann Skill **email-inbox-triage** / Himalaya statt dieses Template.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Gmail MCP | Lesen, Labels, Entwürfe | OAuth, auditierbare API |
| YAML/MD Regelsatz | Priorisierung | Transparente Triage |
| Kalender MCP (optional) | Termin-Snippets | Meeting-Antworten |

## System-Prompt / Instruktionen

```text
You triage a Gmail inbox via MCP (search_emails, read_email, create_draft, update labels). Default: drafts only; never send_email without explicit user confirmation.

Inputs: time window (hours), base query, rules file path (Action / Waiting / FYI), user tone, signature block, max drafts to produce.

Steps:
1) search_emails with query e.g. is:unread newer_than:2d -category:promotions
2) Classify each thread: Action (needs reply), Waiting (awaiting others), FYI (archive after skim), Newsletter (archive).
3) Apply labels from rules; do not delete without approval.
4) For top Action threads: read full thread, create_draft reply referencing ticket/case IDs when present.
5) Redact PII in any summary posted outside Gmail (names → initials if policy says so).
6) Output markdown table: subject, from, label, draft_id or "no draft", one-line summary.

Constraints:
- No mass unsubscribe or filter creation without approval.
- If uncertain priority, label Review-Human.
- Cite message_id when suggesting follow-up calendar holds.

Deliver: label counts, list of draft IDs, triage-summary.md path.
```

## Arbeitsablauf

1. Regeln laden: `cat config/inbox-triage-rules.yaml`.
2. Gmail MCP: `search_emails` mit `is:unread newer_than:2d -category:promotions`.
3. Threads nach YAML priorisieren; Labels `Action`, `Waiting`, `FYI` setzen.
4. Top-10-`Action`: Thread lesen, `create_draft` mit Signatur und Ticket-Referenz.
5. Newsletter: Label `Newsletter` + archivieren (nur nach Policy).
6. `triage-summary.md` mit Counts und Draft-IDs schreiben.
7. Nutzer prüft Entwürfe; `send_email` nur nach explizitem OK pro Message.

## Qualitätskriterien / Definition of Done

- [ ] Alle ungelesenen Threads klassifiziert oder in `Review-Human`
- [ ] Keine gesendete Mail ohne dokumentierte Freigabe
- [ ] Entwürfe enthalten korrekte Thread-Referenz/Reply-To
- [ ] Zusammenfassung ohne unnötige PII im Agent-Log

## Sicherheit & Freigaben

- OAuth-Scopes minimal halten (kein Vault-Export sensibler Anhänge in öffentliche Channels).
- MCP-Logs und Chat: keine vollen Kundenadressen, wenn Policy Pseudonymisierung verlangt.
- Auto-Forward und Filteränderungen nur nach Freigabe.

## Fallstricke

- Reply-All auf interne Escalations → CC-Leak; Drafts auf Empfängerliste prüfen.
- Promotions-Query zu aggressiv → wichtige Receipts übersehen.
- Halluzinierte Fakten in Antworten → nur Zitate aus gelesenen Messages.
- Zeitzonen in Meeting-Vorschlägen falsch (immer IANA, z. B. Europe/Vienna).
- Doppelte Drafts bei erneutem Lauf ohne Idempotenz-Check auf `thread_id`.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Morgen-Triage Führungskraft-Inbox.
- **Input:** Query `is:unread -category:promotions`, Regeln `config/inbox-triage-rules.yaml`.
- **Prompt:**

```text
Triage last 48h unread, apply labels, draft replies for P1 Action (max 5), output triage-summary.md.
```

- **Erwartetes Ergebnis:**

```text
Action: 8 | Waiting: 3 | FYI: 14 | Archived promos: 22
Draft IDs: r-3849201, r-3849202 (customer escalation, board prep)
Review-Human: 1 (legal@...)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende Regeldatei.
- **Input:** Kein Pfad zu `inbox-triage-rules.yaml`.
- **Prompt:**

```text
Run inbox triage with defaults only.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: rules_file fehlt.
Nachfrage: Pfad zu Prioritätsregeln oder Inline-Kriterien (VIP-Domains, SLA-Stufen)?
Keine Label- oder Draft-Aktionen ausgeführt.
```