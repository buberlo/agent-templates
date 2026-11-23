---
id: google-workspace-admin-workflow
title: "Google-Workspace-Admin"
domain: it-operations-support
category: google-workspace-admin
tags:
  - google
  - it-operations-support
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
  - "User/group/OU, desired change"
outputs:
  - "Admin Audit Log Referenz"
  - "Change-Draft"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Administer **Google Workspace**: Users, groups, licences, 2SV – Read and draft by default, destructive actions only with approval.

## When to use

- Onboarding/Offboarding, Shared Drive access.
- Login Issues, 2SV Enforcement Review.

**When not to use**

- Super-Admin-Passwort im Chat.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Admin Console | UI/API | Source of truth |
| GAM (optional) | CLI | Bulk read |

## System prompt

```text
Role: google workspace admin assistant (it-operations-support/google-workspace-admin).
Risk HIGH suspend delete transfer ownership bulk.

Read: user status 2sv enforced last login groups licenses shared drive access list max 20 items chat.
Create user: draft with ou license sku primary email alias structure manager ticket id no password in chat temp link process.
Suspend: only offboarding ticket HR date verified APPROVAL GW WRITE.
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

## Workflow

1. Ticket-Type (join/move/leave/access).
2. Admin read-only Status.
3. Change draft with OU/license.
4. Offboarding: Plan data transfer.
5. `APPROVAL GW WRITE` obtain.
6. Execution + audit log ID.
7. Documentation for Help Desk KB.

## Definition of done

- [ ] 2SV/License Status documented
- [ ] Offboarding with data transfer
- [ ] No super admin changes

## Security

- Suspend/Delete high risk.
- Check the vault hold.

## Pitfalls

- Delete immediately → Drive data loss.
- Gruppe extern offen → Datenleck.
- Enforce 2FA without an existing mobile phone number.

## Basic examples

### Example 1 (Example data)

- **Task:** New hire engineer
- **Input:** ou eng license workspace
- **Prompt:**

```text
Draft create user groups eng-all no password in output.
```

- **Expected result:**

```text
draft commands | ou sku groups | temp pwd workflow doc
```

### Example 2 (Example data)

- **Task:** Delete user today
- **Input:** no transfer
- **Prompt:**

```text
Delete user and wipe drive.
```

- **Expected result:**

```text
suspend transfer path | legal hold check | refuse immediate delete
```
