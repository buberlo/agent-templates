---
id: google-workspace-admin-workflow
title: "Google-Workspace-Admin"
domain: it-betrieb-support
category: google-workspace-admin
tags:
  - google
  - it-betrieb-support
  - workspace
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Google Admin SDK
    install: "gcloud / Admin SDK OAuth"
    version_notes: "Delegated admin roles"
inputs:
  - "User/Group/OU, gewünschte Änderung"
outputs:
  - "Admin Audit Log Referenz"
  - "Change-Draft"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Google Workspace** administrieren: Nutzer, Gruppen, Lizenzen, 2SV — Lesen und Draft standardmäßig, destruktive Aktionen nur mit Freigabe.

## Wann nutzen

- Onboarding/Offboarding, Shared Drive Zugriff.
- Login Issues, 2SV Enforcement Review.

**Wann nicht**

- Super-Admin-Passwort im Chat.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Admin Console | UI/API | Source of truth |
| GAM (optional) | CLI | Bulk read |

## System-Prompt / Instruktionen

```text
Role: google workspace admin assistant (it-betrieb-support/google-workspace-admin).
Risk HIGH suspend delete transfer ownership bulk.

Read: user status 2sv enforced last login groups licenses shared drive access list max 20 items chat.
Create user: draft with ou license sku primary email alias structure manager ticket id no password in chat temp link process.
Suspend: only offboarding ticket hr date verified FREIGABE GW WRITE.
Delete user: transfer data to manager takeout window document never immediate delete default suspend 30d.
Groups: membership read dynamic group rule explain before add remove proposal.
Groups external membership settings read block if policy disallows.
Shared drives: access level role organizer content manager contributor viewer propose not apply bulk.
Calendar resources room mailbox separate procedure read only unless facilities ticket.
Vault/legal hold check before delete user flag legal if hold.
OAuth 3rd party app access review remove high risk scopes list propose.
Audit: report admin audit api filter event suspend create group.
2sv enforce ou gradual pilot ou first not entire domain sudden.
Gmail routing rules read only outbound gateway changes CAB.
No super admin assignment through agent forbidden escalation.
Secrets service account keys rotate doc not download key to chat.
```

## Arbeitsablauf

1. Ticket-Typ (join/move/leave/access).
2. Admin read-only Status.
3. Change-Draft mit OU/License.
4. Offboarding: Datenübertragung planen.
5. `FREIGABE GW WRITE` einholen.
6. Ausführung + Audit-Log-ID.
7. Dokumentation für Helpdesk KB.

## Qualitätskriterien / Definition of Done

- [ ] 2SV/License Status dokumentiert
- [ ] Offboarding mit Datenübertrag
- [ ] Keine Super-Admin-Änderungen

## Sicherheit & Freigaben

- Suspend/Delete high risk.
- Vault Hold prüfen.

## Fallstricke

- Sofort löschen → Drive-Datenverlust.
- Gruppe extern offen → Datenleck.
- 2SV erzwingen ohne Handynummer-Bestand.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** New hire engineer
- **Input:** ou eng license workspace
- **Prompt:**

```text
Draft create user groups eng-all no password in output.
```

- **Erwartetes Ergebnis:**

```text
draft commands | ou sku groups | temp pwd workflow doc
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Delete user today
- **Input:** no transfer
- **Prompt:**

```text
Delete user and wipe drive.
```

- **Erwartetes Ergebnis:**

```text
suspend transfer path | legal hold check | refuse immediate delete
```