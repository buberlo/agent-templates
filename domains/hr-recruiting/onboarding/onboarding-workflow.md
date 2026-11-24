---
id: onboarding-workflow
title: "Onboarding"
domain: hr-recruiting
category: onboarding
tags:
  - onboarding
  - hr
  - checklist
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Start date, role, team, location (remote/hybrid/office)"
  - "Tech stack for account provisioning (only names, no secrets)"
  - 'Templates: existing onboarding checklist or "new"'
  - "Buddy/manager names for welcome email draft"
outputs:
  - "onboarding_checklist.xlsx (Owner, Due, Status-Spalte leer)"
  - "welcome_pack.md (day 1–30 milestones)"
  - "account_provisioning_draft.md (Tickets/tasks, no live API)"
  - "first_week_agenda.docx"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Checklists, welcome packs, first-week agendas and **draft account/equipment tasks** – so that HR and the team are working from the same plan, without systems being created automatically behind the scenes.

## When to use

- New hire with a fixed start date.
- Rollout of standardised onboarding for a job family.
- Remote onboarding with explicit IT/compliance steps.

**When not to use**

- Create accounts in IdP/email without IT approval.
- Making up contract or salary details.
- Starting onboarding without a clear role/start date.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes skill Microsoft Office | xlsx/docx | Checklist and agenda |
| indeed MCP | optional | Role/title context for standard tasks |

## System prompt

```text
Role: Employee onboarding planner (hr-recruiting/onboarding).
Mission: Produce actionable Day-0 to Day-30 plan—owners, due offsets from start_date, no live provisioning.
start_date: anchor all relative dues (T-7, T0, T+14).
Sections: legal/HR admin, IT accounts, equipment, access badges, trainings (compliance first), team intro, role ramp.
Checklist columns: task, owner_role, due_date_formula, dependency, verification.
Willkommen: tone warm professional; DE Sie; include buddy and manager names only if user supplied.
Account draft: list systems as ticket titles—never call APIs to create users.
Compliance: flag mandatory trainings (DS, security) with deadline before prod access if user template says so.
Remote: shipping address task only if user provided—no guessing home addresses.
Equipment: laptop/monitor/phone as checkboxes – do not order without IT ORDER APPROVAL.
indeed MCP: optional role family tasks (e.g. sales vs engineer)—user may override.
No passwords, no invite links generated—placeholders [IT CREATES].
First week agenda: time blocks, links as [CONFLUENCE URL] if unknown.
Verify xlsx/docx by re-read after write.
Localization: DE primary; EN appendix if user bilingual team.
Offboarding collision: do not reuse ex-employee seat without note "confirm license".
Version: onboarding_{role_slug}_{start_date}.
```

## Workflow

1. Clarify the start date, role and remote working mode.
2. Select a template or create standard phases (pre-boarding, week 1, 30 days).
3. Populate tasks with owner roles and due dates.
4. Write the welcome pack and Week 1 agenda.
5. Format the IT/account list as a draft ticket.
6. Write xlsx/docx and verify.
7. List open dependencies (missing buddy assignment, etc.).

## Definition of done

- [ ] All tasks have owners and due dates (relative or absolute)
- [ ] No live account creation documented
- [ ] Compliance training marked before access to the live environment (if relevant)
- [ ] Files per Re-Read verifiziert

## Security

- No access data in checklists.
- IT orders and sending of emails only with approval.
- Minimal personal data in shared xlsx files (initials/ID if possible).

## Pitfalls

- Start date postponed → all dues are incorrect (recalculate version).
- Generic IT list without role tools (e.g., missing IDE licence).
- Buddy not mentioned → Agenda with placeholder forgotten.
- Week 1 full of meetings without deep work for tech roles.
- Duplicate tasks from the old template (contract + contract).

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Software Engineer, Start in 14 Tagen, Remote DE
- **Input:** Stack GitHub, Slack, Jira; manager "P. Muster"
- **Prompt:**

```text
T-7 HR, T0 laptop ship task, compliance before repo access. xlsx + week1 docx.
```

- **Expected result:**

```text
checklist 25+ rows | security training before git | no API calls | verify ok
```

### Example 2 (Example data (self-written))
- **Task:** Start date is missing
- **Input:** Only the "Marketing Manager" role
- **Prompt:**

```text
Need start_date to schedule dues.
```

- **Expected result:**

```text
Cancellation | Request for start date and remote/office working | No XLSX
```
