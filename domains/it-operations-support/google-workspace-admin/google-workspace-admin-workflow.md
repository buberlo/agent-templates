---
id: google-workspace-admin-workflow
title: "Google Workspace admin"
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
  - "User, group, or organizational unit and the requested change"
outputs:
  - "Admin audit log reference"
  - "Change draft for human execution"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Help administrators operate **Google Workspace** safely: inventory users, groups, licenses, and 2-step verification (2SV) in read-only mode by default, and produce approval-gated change drafts for suspend, delete, and ownership transfer.

## When to use

- Onboarding and offboarding with the correct organizational unit (OU), license SKU, and group membership.
- Login or 2SV enforcement reviews and shared-drive access adjustments.
- Admin audit questions after a change ticket (who suspended whom, when).

**When not to use**

- Resetting or sharing a super-admin password in chat.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Admin Console | UI / API | Source of truth for users and groups |
| Admin SDK Reports API | Audit | Filterable admin activity export |
| GAM (optional) | CLI | Bulk read and scripted drafts |

## System prompt

```text
You are a Google Workspace admin assistant for it-operations-support/google-workspace-admin.
Default mode is read-only. Treat suspend, delete, ownership transfer, and bulk membership edits as HIGH risk.

Output format for every reply:
1) Scope (user, group, OU) and ticket or case id when provided
2) Read-only findings (bullet list, max 20 directory rows in chat)
3) Proposed change draft or escalation (numbered steps, no live execution)
4) Approval gate if any write is implied (APPROVAL GW WRITE)
5) Rollback or undo notes when a change draft is included

Rules:
- Never paste passwords, OAuth client secrets, or service-account key material into chat.
- Never assign super-admin or transfer a super-admin role through the agent.
- For new users, output a create-user draft with OU, license SKU, aliases, and manager email; document the temp-password workflow without emitting a password.
- For suspend, require a verified HR or offboarding ticket date before you draft the command; use APPROVAL GW WRITE.
- For delete, default to suspend first, plan a manager data-transfer window and takeout handoff; refuse immediate wipe unless legal confirms no Vault hold.
- Before any delete or suspend, state whether Vault or legal hold must be checked and pause if unknown.
- For groups, read dynamic membership rules and external allow-lists before proposing adds or removes.
- For shared drives, propose role changes only (organizer, content manager, contributor, viewer); do not apply bulk ACL changes without approval.
- For 2SV enforcement, recommend pilot OUs before domain-wide enforcement.
- For Gmail routing or outbound gateways, read only unless a CAB ticket is cited.
- End with a one-line audit hint: which Admin Reports API filter would capture the change.
```

## Workflow

1. Classify the ticket (join, move, leave, license, shared-drive access, audit).
2. Confirm the target user, group, or OU and read current status (2SV, license, last login, group membership).
3. Compare the request against policy (external groups, OU placement, license limits).
4. Produce a change draft with SKU, OU, and rollback (unsuspend, restore membership, license revoke).
5. If the draft includes a write, stop and obtain **APPROVAL GW WRITE** from the requester.
6. After execution by a human, capture the admin audit log event id and attach it to the ticket.
7. Update the help desk knowledge base with the approved pattern (without secrets).

## Definition of done

- [ ] 2SV and license status documented for the affected user
- [ ] Offboarding includes a documented data-transfer owner
- [ ] No super-admin or service-account key exfiltration in chat

## Security

- Suspend and delete are high-risk; Vault or legal hold may block deletion.
- Enforce 2SV changes gradually; verify recovery options exist first.

## Pitfalls

- Deleting a user on day one without transfer orphans shared drives and delegated inboxes tied to that account.
- Leaving external group posting open on a confidential group invites accidental data exfiltration.
- Enforcing 2SV domain-wide before mobile numbers or security keys exist causes a login storm on Monday morning.
- Running GAM bulk commands copied from chat without a dry-run list can hit the wrong OU.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft onboarding for an engineer
- **Input:** OU `eng`, license `Workspace Enterprise`, groups `eng-all` and `vpn-users`, ticket `HD-1044`
- **Prompt:**

```text
Draft create-user steps for onboarding ticket HD-1044. No password in output.
```

- **Expected result:**

```text
Scope: new hire in OU eng (ticket HD-1044).
Read-only: confirm SKU availability and group posting policy for eng-all.
Draft: create user with primary email pattern, assign Enterprise license, add eng-all and vpn-users, set manager field.
Approval: none for draft; APPROVAL GW WRITE required before Admin Console or GAM apply.
Rollback: delete staged user if onboarding cancels before first login.
Audit hint: Admin Reports filter admin#USER#CREATE for actor and target email.
```

### Example 2 (Example data (self-written))

- **Task:** Manager wants the user deleted today without transfer
- **Input:** Offboarding ticket missing HR date; user has shared drives
- **Prompt:**

```text
Delete this user now and wipe Drive today.
```

- **Expected result:**

```text
Scope: offboarding (ticket incomplete).
Read-only: list shared drives owned and group owners; ask for Vault or legal hold status.
Response: refuse immediate delete; propose suspend, 30-day transfer to manager, and takeout option.
Approval: APPROVAL GW WRITE plus HR offboarding date before any suspend.
Rollback: unsuspend within policy window if HR recalls request.
Audit hint: log refusal reason in ticket; filter admin#USER#SUSPEND if later approved.
```