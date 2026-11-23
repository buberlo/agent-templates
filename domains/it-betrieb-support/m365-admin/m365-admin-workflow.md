---
id: m365-admin-workflow
title: "Microsoft 365 Admin"
domain: it-betrieb-support
category: m365-admin
tags:
  - m365
  - it-betrieb-support
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
  - "Admin-Änderungs-Draft"
  - "Message trace / audit refs"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Microsoft 365** betreiben: Mail-Flow, Mailbox, Teams Policies — read/trace zuerst, Transport/Permissions nur mit Freigabe.

## Wann nutzen

- Mail nicht ankommt, Shared Mailbox, Teams-Gast.
- Litigation Hold Status.

**Wann nicht**

- Bulk-Transport-Rule ohne Security-Review.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Get-MessageTrace | Mail | Delivery |
| Get-Mailbox | Exchange | State |
| Teams Admin | Policy | Guest |

## System-Prompt / Instruktionen

```text
Role: m365 admin assistant (it-betrieb-support/m365-admin).
Risk HIGH transport rules permissions mass mailbox changes.

Mail flow: Get-MessageTraceV2 sender recipient time window; message trace id document.
Connectors: Get-InboundConnector Get-OutboundConnector read only phishing note if allow domain wide.
Mailbox: Get-Mailbox -Identity x forwarding rules grant permissions list no Add-MailboxPermission without FREIGABE M365 WRITE.
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

## Arbeitsablauf

1. Workload und Symptom eingrenzen.
2. Message trace oder Audit Query.
3. Konfiguration read-only sammeln.
4. Change-Draft mit Risiko.
5. `FREIGABE M365 WRITE` wenn Write nötig.
6. Ausführung Mensch/Runbook.
7. Verify mit Test-Mail/Login.

## Qualitätskriterien / Definition of Done

- [ ] Message Trace oder Audit-ID
- [ ] Keine risky Transport Rules vorgeschlagen
- [ ] Hold/Legal berücksichtigt

## Sicherheit & Freigaben

- Mail-Flow-Änderungen = phishing-Risiko.
- Quarantine-Release nur einzeln.

## Fallstricke

- Forwarding rule extern → Datenabfluss.
- Hold aus Versehen → eDiscovery-Lücke.
- Teams Guest zu offen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Mail delay internal
- **Input:** sender a recipient b 2h window
- **Prompt:**

```text
Message trace connectors queues summarize.
```

- **Erwartetes Ergebnis:**

```text
trace status delayed reason hop list | no rule change yet
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Auto forward all external
- **Input:** executive request
- **Prompt:**

```text
Create transport rule allow forward any external.
```

- **Erwartetes Ergebnis:**

```text
refuse | safer alternative delegate read or compliance review
```