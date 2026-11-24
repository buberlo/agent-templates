---
id: rpa-workflow
title: "RPA"
domain: automation
category: rpa
tags:
  - rpa
  - automation
  - platform-mcp-catalog
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: RPA platform (UiPath / Power Automate / scripting)
    install: "Business License or OpenRPA"
    version_notes: "Check selector stability"
inputs:
  - "Process description (SOP) and applications"
  - "Exception treatment and audit requirements"
outputs:
  - "Prozessdiagramm"
  - "Bot design or pseudocode"
  - "Testdaten-Set"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Automate repeatable **GUI processes** in enterprise applications (RPA): structured design, intercept exceptions, audit trail — not as a replacement for missing APIs.

## When to use

- Legacy ERP without API, high manual click load.
- Regulatory process with screenshots per step.


####### When not to use


- If stable REST API available → Prefer integration.
Processes with frequent UI redesign without maintenance budget.

## Tool stack

| Tool | Role | Rationale |
|------------------------------------------------------------------------------------------------------
| OpenRPA / UiPath | Bot runtime | Enterprise Standard |
| Queue | Work items | Retry/DLQ |
| DB logging | Audit | Every step |

## System prompt

```text
You are RPA solution designer (automatisierung/rpa).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Map SOP to bot steps with exception paths; human-in-the-loop for low-confidence OCR.
Phase 1 discover: watch SOP list applications screens fields data sources pii.
Phase 2 design: flowchart decision diamonds for business rules not only happy path.
Selectors: prefer application accessibility ids over image matching document fallbacks.
Credentials: store in enterprise vault/credential asset never hardcode in xaml.
Exception: system down retry 3 backoff then queue item failed reason code.
Audit: log transaction id step timestamp screenshot hash optional.
Scaling: one bot one session per user profile—no shared desktop secrets.
Change management: UI update playbooks versioned with bot package version.
Testing: uat dataset with edge cases decimal comma german dates.
Compliance: GDPR retention on screenshots 30d default unless user policy.
Activation prod: USER_APPROVAL RPA PROD with owner signoff.
Maintenance: monthly selector health check calendar event.
API first: if screen scrape only because no API file ticket for api project parallel.```## Workflow

1. go through SOP with subject area; Mark exceptions.
2. Collect application list and selector candidates.
3. Drawing flowchart with decisions.
4. Pilot bot on UAT with test queue.
5. Implement exception and retry rules.
6. Audit logging and screenshot policy.
7. Prod rollout after `USER_APPROVAL RPA PROD`.

## Definition of done

Happy path and mind. 3 Exception paths
Credentials in the Vault
- [ ] UAT run logged
- [ ] Maintenance plan for UI changes

## Security

- high risk: production bots with financial or customer data.
Avoid shared RPA accounts.

## Pitfalls

- OCR in case of poor scanning quality → wrong bookings.
- Popup update interrupts Selector.
- Parallel running human users on the same account.

## Basic examples

Example 1 (Example data)

- **Task:** Export invoice from ERP
- **Input:** UAT, bills No. 10042
- **Prompt:**

```text
Design bot steps login navigate export pdf to queue folder log each step.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.flowchart + pilot run | PDF in queue | audit log 8 steps
```

### Example 2 (Example data (self-written))
- **Task:** Prod starten without UAT
- **Input:** go live Monday
- **Prompt:**

```text
Enable production bot schedule.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.blocked | require UAT evidence + USER_APPROVAL RPA PROD
```

### Example 1 (Example data (self-written))
- **Task:** Placeholder
- **Input:** example data
- **Prompt:**
```text
Draft only.
```
- **Expected result:** Draft artifact path.
