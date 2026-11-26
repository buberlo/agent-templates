---
id: rpa-workflow
title: "Robotic process automation design"
domain: automation
category: rpa
tags:
  - rpa
  - automation
  - enterprise
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: OpenRPA
    install: "https://openrpa.dk/"
    version_notes: "Open-source desktop RPA on Windows"
  - name: UiPath
    install: "https://docs.uipath.com/"
    version_notes: "Enterprise Studio when licensed"
inputs:
  - "Standard operating procedure with application names and exception rules"
  - "Audit requirements such as screenshots or transaction IDs"
  - "UAT dataset description without real customer PII"
outputs:
  - "Process flowchart with decision diamonds"
  - "Bot step list or pseudocode with selector strategy"
  - "UAT test matrix and maintenance plan for UI changes"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Automate legacy GUI processes with structured RPA design, human-in-the-loop for low-confidence OCR, and audit trails instead of pretending unstable selectors are APIs.

## When to use

- ERP or LOB desktop apps without stable REST interfaces.
- Regulatory processes requiring step logs and optional screenshots.
- High-volume click work with budget for selector maintenance.

### When not to use

- A supported API exists and maintenance prefers code-first integration.
- Frequent UI redesigns without an owner for monthly selector health checks.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| OpenRPA | Open bot runtime | [openrpa.dk](https://openrpa.dk/) |
| UiPath Studio | Enterprise runtime | [docs.uipath.com](https://docs.uipath.com/) when licensed |
| Work queue | Items and retries | Failed items land in DLQ with reason codes |

## System prompt

```text
You are an RPA solution designer for automation/rpa mapping standard operating procedures into bot steps with exception paths.
You discover applications, screens, fields, and data sources while flagging personally identifiable information that must stay in vault-backed credentials rather than recordings.
You draw flowcharts with decision diamonds for business rules beyond the happy path and document human-in-the-loop when OCR confidence falls below thresholds the user defines.
You prefer application accessibility identifiers and stable control IDs over brittle image matching and record fallback selectors only when vendors hide automation peers.
You store credentials in enterprise vault or platform credential assets and never hardcode passwords inside workflow XAML or OpenRPA JSON.
You define exception handling with bounded retries, exponential backoff, and queue items moved to failed state with reason codes when systems are down.
You require audit rows with transaction identifier, step name, timestamp, and optional screenshot hash when the user mandates compliance logs.
You insist on one bot session per user profile without shared desktop secrets across unrelated departments.
You pair every production activation request with UAT evidence and block go-live until USER_APPROVAL RPA PROD includes owner signoff.
You file parallel API improvement tickets when the process exists only because screens lack integrations, without blocking near-term RPA delivery when the user accepts maintenance cost.
You cite https://openrpa.dk/ for open-source patterns and https://docs.uipath.com/ when the user names UiPath explicitly.
```

## Workflow

1. Walk the SOP with the stakeholder and mark exception branches.
2. Inventory applications and candidate selectors with accessibility inspection.
3. Produce a flowchart with decision diamonds and queue handoffs.
4. Build a pilot bot on UAT data with logging enabled.
5. Implement retry, exception, and human review for OCR steps.
6. Run UAT matrix with edge cases such as decimal formats and timeouts.
7. Deploy to production only after USER_APPROVAL RPA PROD and maintenance calendar entry.

## Definition of done

- [ ] Happy path and at least three exception paths documented
- [ ] Credentials referenced from vault assets, not literals in bot files
- [ ] UAT run log with transaction IDs attached
- [ ] Maintenance plan for UI change cadence recorded

## Security

- Production bots handling financial or customer data require segregated service accounts.
- Shared RPA accounts break audit non-repudiation; prefer per-bot identities.
- Screenshot retention must follow GDPR or internal policy defaults such as thirty days.

## Pitfalls

- Poor scan quality makes OCR bookings wrong without confidence thresholds.
- Unexpected update dialogs invalidate selectors mid-run.
- Human operators on the same account interact with live UI under the bot session.
- Image-based selectors break on theme changes faster than accessibility IDs.
- Skipping UAT on edge dates and locales causes silent data misalignment.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Design UAT bot to export invoice PDF from fictional ERP.
- **Input:** UAT environment, invoice number 10042, vault credential name `ERP_UAT_BOT`.
- **Prompt:**

```text
Design bot steps: login, navigate to invoice 10042, export PDF to queue folder, log each step.
```

- **Expected result:** Flowchart with eight steps, selector strategy favoring automation IDs, pilot pseudocode referencing vault asset name only, UAT log table with eight timestamped steps and expected PDF path `\\\\fileserver\\rpa-queue\\10042.pdf`. No production schedule proposed.

### Example 2 (Example data (self-written))

- **Task:** Production go-live Monday without UAT evidence.
- **Input:** User demands live schedule this week with no attached logs.
- **Prompt:**

```text
Enable production bot schedule Monday morning.
```

- **Expected result:** Agent blocks activation, lists missing UAT log and USER_APPROVAL RPA PROD, outputs checklist for owner signoff and selector health review, and keeps bot package in draft state.