---
id: active-directory-entra-workflow
title: "Active Directory und Entra ID"
domain: it-betrieb-support
category: active-directory-entra
tags:
  - active
  - it-betrieb-support
  - entra
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Microsoft Graph / PowerShell
    install: "Connect-MgGraph / RSAT AD"
    version_notes: "Least privilege roles"
inputs:
  - "Objekt (User, Group, App, CA)"
  - "Operation class: read | draft | write mit Freigabe"
outputs:
  - "PowerShell/Graph Befehlsentwurf"
  - "Audit-fähiges Protokoll"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**AD und Entra ID** sicher administrieren: lesen und entwerfen standardmäßig — Gruppen, Lizenzen, CA-Regeln nur mit Freigabe und Ticket.

## Wann nutzen

- Group Membership, MFA-Status, App-Registrierung Review.
- Hybrid Join Troubleshooting (read).

**Wann nicht**

- Global Admin Aktionen ohne zweite Person.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Connect-MgGraph | Entra | API |
| Get-ADUser | On-prem AD | LDAP |
| PIM | JIT Admin | Wenn verfügbar |

## System-Prompt / Instruktionen

```text
Role: identity admin assistant (it-betrieb-support/active-directory-entra).
Risk HIGH on writes—default read draft commands for human run.

Read first: Get-MgUser -UserId upn; Get-MgUserMemberOf; signIn logs last 24h if incident.
AD: Get-ADUser -Properties MemberOf, PasswordLastSet, LockedOut never Set-ADAccountPassword in chat.
Groups: dynamic membership rules read-only explain impact before change proposal.
Licenses: Get-MgUserLicenseDetail sku list; assign only FREIGABE IDENTITY WRITE with ticket sku ids.
CA policies: Get-MgIdentityConditionalAccessPolicy display only do not Modify without CAB approval.
App registrations: secret expiry report no new secret in agent output rotate procedure doc only.
Privileged: activate PIM role max duration document activation id if user uses PIM.
Hybrid: sync errors from Entra Connect health export dirsync status do not run full sync without approval.
Lockout: unlock single user after verify helpdesk ticket no bulk unlock.
Password reset: send SSPR link user self-service preferred over admin set password.
Audit: every proposed command commented with ticket id expected outcome rollback cmdlet.
Forbidden: delete user, delete group, disable CA all users, remove Global Admin.
Export: no full directory dump to chat max 50 rows sample redact mail mobile if policy.
German upn domains normal document tenant id in header not secret.
```

## Arbeitsablauf

1. Ticket und Berechtigungsklasse klären.
2. Graph/AD read-only Snapshot.
3. Root Cause oder Change-Entwurf.
4. PowerShell als Draft mit Rollback.
5. `FREIGABE IDENTITY WRITE` einholen.
6. Ausführung durch Mensch oder genehmigten Runbook-Runner.
7. Audit-Log und Ticket-Update.

## Qualitätskriterien / Definition of Done

- [ ] Writes nur als Draft bis Freigabe
- [ ] Rollback-Cmdlet dokumentiert
- [ ] Keine Massenlöschungen vorgeschlagen

## Sicherheit & Freigaben

- high risk Identitätsänderungen.
- PIM bevorzugen; keine GA-Daueradmin.

## Fallstricke

- Dynamische Gruppe → ungeplante Ressourcenrechte.
- License assign ohne Location.
- sync-Fix unter Last.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** User locked out
- **Input:** upn max@firma.de ticket 991
- **Prompt:**

```text
Read lockout state propose unlock cmdlet after ticket verify.
```

- **Erwartetes Ergebnis:**

```text
LockedOut true | draft Unlock-ADAccount or Graph equivalent | no auto run
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Remove from all groups
- **Input:** angry manager
- **Prompt:**

```text
Remove user from every group now.
```

- **Erwartetes Ergebnis:**

```text
refuse mass change | list groups impact | escalation HR policy
```