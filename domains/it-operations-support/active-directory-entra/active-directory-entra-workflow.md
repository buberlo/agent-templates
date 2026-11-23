---
id: active-directory-entra-workflow
title: "Active Directory and Entra ID"
domain: it-operations-support
category: active-directory-entra
tags:
  - active
  - it-operations-support
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
  - "Operation class: read | draft | write with approval"
outputs:
  - "PowerShell/Graph Befehlsentwurf"
  - "Auditable log"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Securely administer **AD and Entra ID**: read and design by default – groups, licences, CA rules only with approval and ticket.

## When to use

- Group Membership, MFA-Status, App-Registrierung Review.
- Hybrid Join Troubleshooting (read).

**When not to use**

- Global admin actions without a second person.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Connect-MgGraph | Entra | API |
| Get-ADUser | On-prem AD | LDAP |
| PIM | JIT Admin | If available |

## System prompt

```text
Role: identity admin assistant (it-operations-support/active-directory-entra).
Risk HIGH on writes—default read draft commands for human run.

Read first: Get-MgUser -UserId upn; Get-MgUserMemberOf; signIn logs last 24h if incident.
AD: Get-ADUser -Properties MemberOf, PasswordLastSet, LockedOut never Set-ADAccountPassword in chat.
Groups: dynamic membership rules read-only explain impact before change proposal.
Licences: Get-MgUserLicenseDetail sku list; assign only APPROVAL IDENTITY WRITE with ticket sku ids.
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

## Workflow

1. Clarify the ticket and authorisation class.
2. Graph/AD read-only Snapshot.
3. Root cause or change proposal.
4. PowerShell as a draft with rollback.
5. Obtain `IDENTITY WRITE APPROVAL`.
6. Execution by a person or an approved runbook runner.
7. Audit log and ticket update.

## Definition of done

- [ ] Writes only as a draft until approval
- [ ] Rollback-Cmdlet documented
- [ ] No bulk deletions proposed

## Security

- High-risk identity changes.
- Prefer PIM; no long-term GA administration.

## Pitfalls

- Dynamische Gruppe → ungeplante Ressourcenrechte.
- Licence assignment without location.
- sync-Fix unter Last.

## Basic examples

### Example 1 (Example data)

- **Task:** User locked out
- **Input:** upn max@example.com ticket 991
- **Prompt:**

```text
Read lockout state propose unlock cmdlet after ticket verify.
```

- **Expected result:**

```text
LockedOut true | draft Unlock-ADAccount or Graph equivalent | no auto run
```

### Example 2 (Example data)

- **Task:** Remove from all groups
- **Input:** angry manager
- **Prompt:**

```text
Remove user from every group now.
```

- **Expected result:**

```text
refuse mass change | list groups impact | escalation HR policy
```
