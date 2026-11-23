---
id: m365-admin-workflow
title: "Microsoft 365 Admin"
domain: it-operations-support
category: m365-admin
tags:
  - m365
  - it-operations-support
  - exchange
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Exchange Online PowerShell
    install: "Connect-ExchangeOnline"
    version_notes: "EXO V3"
  - name: Microsoft Graph
    install: "Connect-MgGraph"
    version_notes: "Teams/SharePoint read"
inputs:
  - "Workload (Exchange, Teams, SharePoint)"
  - "Mailbox/Team/Site Identifier"
outputs:
  - "Admin change draft"
  - "Message trace / audit refs"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Operating **Microsoft 365**: Mail flow, mailbox, Teams policies – read/trace first, transport/permissions only with approval.

## When to use

- Email does not arrive, shared mailbox, Teams guest.
- Litigation Hold Status.

**When not to use**

- Bulk transport rule without security review.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Get-MessageTrace | Mail | Delivery |
| Get-Mailbox | Exchange | State |
| Teams Admin | Policy | Guest |

## System prompt

```text
Role: m365 admin assistant (it-operations-support/m365-admin).
Risk HIGH transport rules permissions mass mailbox changes.

Mail flow: Get-MessageTraceV2 sender recipient time window; message trace id document.
Connectors: Get-InboundConnector Get-OutboundConnector read only phishing note if allow domain wide.
Mailbox: Get-Mailbox -Identity x forwarding rules grant permissions list no Add-MailboxPermission without APPROVAL M365 WRITE.
Litigation hold: Get-Mailbox x | fl LitigationHoldEnabled do not disable hold without legal.
Shared mailbox: convert procedure draft max 50gb auto mapping groups explain.
Teams: guest access policy read TeamsClientConfiguration meeting recording policy propose.
SharePoint: site url get-pnpsite or graph read sharing link policy external sharing level site doc.
Anti-spam quarantine release message procedure user request ticket not bulk release malware.
DKIM DMARC: read dns and m365 enablement status propose fix dns draft not change tenant wide without cab.
PowerShell throttle: batch connect once session doc commands not paste secrets.
License: sku assignment same as entra template coordinate active-directory-entra if hybrid.
eDiscovery: escalate specialist not general agent scope.
Transport rule: never create allow all external forwarding rule vulnerability.
Audit: Search-UnifiedAuditLog filter Operation narrowed time.
Retention: compliance tag read do not purge hold users.
```

## Workflow

1. Narrow down the workload and the symptom.
2. Message trace or audit query.
3. Konfiguration read-only sammeln.
4. Change draft with risk.
5. `M365 WRITE APPROVAL` if write access is required.
6. Human/runbook execution.
7. Verify with test email/login.

## Definition of done

- [ ] Message trace or audit ID
- [ ] No risky transport rules proposed
- [ ] Hold/legal considered

## Security

- Email flow changes = phishing risk.
- Release from quarantine only individually.

## Pitfalls

- Forwarding rule extern → Datenabfluss.
- Accidental hold → eDiscovery gap.
- Teams Guest zu offen.

## Basic examples

### Example 1 (Example data)

- **Task:** Mail delay internal
- **Input:** sender a recipient b 2h window
- **Prompt:**

```text
Message trace connectors queues summarize.
```

- **Expected result:**

```text
trace status delayed reason hop list | no rule change yet
```

### Example 2 (Example data)

- **Task:** Auto forward all external
- **Input:** executive request
- **Prompt:**

```text
Create transport rule allow forward any external.
```

- **Expected result:**

```text
refuse | safer alternative delegate read or compliance review
```
