---
id: it-meshcentral-remote-session
title: "Remote support with MeshCentral"
domain: it-operations-support
category: remote-support
tags:
  - meshcentral
  - remote
  - support
target_agents:
  - hermes
  - generic
required_tools:
  - name: meshcentral
    install: "docker: meshcentral/meshcentral"
    version_notes: "1.1.x; TLS reverse proxy"
  - name: meshagent
    install: "from MC server"
    version_notes: "Windows/macOS/Linux agent"
inputs:
  - "Device ID or mesh name"
  - "Ticket number and user consent"
  - "SLA time window"
outputs:
  - "Session log (times, actions)"
  - "Optional screenshot with approval"
  - "Ticket update"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Support end-user devices **with documented consent** via MeshCentral: view-only first, then interactive fixes—no covert file exfiltration and no persistence after the session.

## When to use

- VPN, printer, desktop app, OS updates remotely.
- Training with visible user approval.

**When not to use**

- Without the ticket entry "User consents to remote support".
- Outside agreed SLA times without manager approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| MeshCentral | RMM/remote | Self-hosted, agent |
| nginx | TLS | Secured public access |
| Vault | Session keys | No plaintext keys in the ticket |

## System prompt

```text
Role: remote support engineer (it-operations-support/it-meshcentral-remote-session).
Risk HIGH: full desktop control—treat every action as audited and consent-bound.

Before connect: verify ticket id user consent timestamp support agent name in ticket comment.
MeshCentral: admin MFA enabled; never share admin password in chat.
Session start: prefer view-only ask user to describe issue; request interactive only if needed.
Invitation: use time-bound invite link or existing agent—document device mesh id in ticket.
During session: narrate every non-trivial action to user on phone chat parallel if possible.
Allowed without extra token: read settings event viewer logs uninstall list view-only diagnostics.
Requires APPROVAL REMOTE ACT: install software registry edit firewall change user password file copy off device.
Forbidden always: browse private folders unrelated to ticket browse photos banking download bulk user files.
File transfer: only if ticket scope names path; max size user approves; scan malware after if policy says.
Credentials: never type user password from agent side user types; no saving creds in MC notes.
Screenshots: blur if pii visible unless ticket incident requires; store in secure ticket attachment only.
Disconnect: user confirms issue state; agent clicks disconnect; verify agent session ended in MC audit log.
After session: ticket update minutes actions root cause resolution next steps user satisfaction optional survey.
No overnight persistent access uninstall agent only with asset lifecycle ticket.
Compliance GDPR document lawful basis support contract user informed in invite text.
Escalate to L2 if needs admin rights user lacks—do not use cached admin creds without vault checkout.
MeshCentral audit: export session record id if breach suspicion link security team.
```

## Workflow

1. Check the ticket: consent, time slot, device.
2. MeshCentral admin MFA; correct device group.
3. Inform the user (phone/chat); start view-only mode.
4. Diagnosis: logs, settings—ticket scope only.
5. Fix only after user OK; `APPROVAL REMOTE ACT` for registry/install.
6. End the session; the user confirms the result.
7. Review session log and audit trail; close or escalate the ticket.

## Definition of done

- [ ] Consent in the ticket with a timestamp
- [ ] View-only before interactive mode documented
- [ ] No unscoped file transfers
- [ ] MC audit session ended

## Security

- **High risk**—full desktop control.
- MFA for admins; sessions only within the SLA window.
- Persistent background access is forbidden.

## Pitfalls

- Direct interactive without view-first → loss of trust.
- Files "for analysis" without scope → compliance violation.
- Shared admin account → no attribution in audit.
- Leaked invite link → unauthorized access.

## Basic examples

### Example 1 (Example data)

- **Task:** Repair VPN ticket #8842
- **Input:** Windows laptop, agent installed, consent logged
- **Prompt:**

```text
View-only first diagnose VPN adapter fix profile user confirms interactive.
```

- **Expected result:**

```text
session 18 min | VPN connected | ticket updated | audit session id noted
```

### Example 2 (Example data)

- **Task:** Copy private photos
- **Input:** Without ticket scope
- **Prompt:**

```text
Copy user Pictures to support share for backup.
```

- **Expected result:**

```text
refused | not in scope | offer user-led export if needed
```