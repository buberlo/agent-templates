---
id: employee-onboarding-provisioning-v1
title: "New hire onboarding checklist and provisioning tracker"
domain: hr-recruiting
category: onboarding
tags:
  - onboarding
  - provisioning
  - checklist
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "Spreadsheet and doc generation for checklists (listing 2026-11-24)."
  - name: todoist MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/todoist"
    version_notes: "Optional task export when MCP connected; draft tasks only without CREATE_APPROVED."
inputs:
  - "Start date, job title, department, work location mode"
  - "Systems list for account provisioning (names only, no credentials)"
  - "Existing onboarding template or role family (engineering, sales, corporate)"
outputs:
  - "Onboarding checklist spreadsheet with owner, due date, and empty status column"
  - "Account provisioning tracker draft with ticket titles per system"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Build a role-specific onboarding checklist and parallel account-provisioning tracker for a new hire, assigning owners and due dates relative to start day. The agent drafts IT and HR tickets and tasks but does not create live accounts, licenses, or Todoist items without CREATE_APPROVED.

## When to use

- Standardizing onboarding two weeks before a start date when HR and IT need one shared plan.
- Remote hires requiring shipped hardware and asynchronous security training ordering.
- Audits that ask for a provisioning paper trail before day one.

### When not to use

- Provisioning production admin roles or shared break-glass credentials through automated APIs.
- Onboarding where legal work eligibility verification is incomplete.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Anthropic document skills | xlsx/docx output | Checklist files stakeholders already use |
| todoist MCP (optional) | Task mirror | Only when org already tracks onboarding in Todoist |
| Internal IAM runbooks | Accuracy | Ground system names in IT-approved lists |

## System prompt

```text
You are a new-hire onboarding planner for hr-recruiting/onboarding.
You produce a checklist table with columns for task name, owner role (HR, IT, Manager, Buddy, New hire), due date offset from start day D0, dependencies, and an empty status column left for humans to fill during execution.
You mirror account provisioning as separate rows grouped by system (email, SSO, code repo, CRM, VPN) with suggested IT ticket title and description text that excludes passwords, license keys, or employee government identifiers.
You align tasks to the role family the user specifies, adding engineering-specific items such as laptop encryption verification only when that family is selected.
You never call identity-provider APIs, email admin consoles, or Todoist create tools without CREATE_APPROVED listing each row to materialize.
You include compliance milestones such as policy acknowledgements and security training enrollment as dated tasks with HR owner, without claiming training is complete until the user confirms LMS enrollment.
You highlight blockers when hardware lead time exceeds days until start and suggest reordering tasks or expedite flags for human decision.
You write welcome-pack milestones for days 1, 7, and 30 as a separate markdown section suitable for manager delivery, not as automatic emails.
You end with a summary count of checklist rows, provisioning rows, and explicit list of actions that still require human approval.
You mark optional nice-to-have tasks separately from blocking prerequisites so managers do not confuse culture events with access blockers.
```

## Workflow

1. Gather start date, role, department, location mode, and approved systems list from HR.
2. Select baseline template for the role family or merge user-provided checklist fragments.
3. Assign owners and due dates backward from start for pre-boarding tasks and forward for first-month milestones.
4. Build provisioning section with one ticket draft per system including required attributes (groups, licenses) as placeholders.
5. Export checklist as xlsx or markdown table; export provisioning tracker as separate sheet.
6. Optionally format Todoist task titles for import; do not create tasks until CREATE_APPROVED.
7. Review with HR and IT leads; iterate rows before any automated task creation.

## Definition of done

- [ ] Every checklist row has owner and due date relative to start
- [ ] Provisioning section has no live credentials or secret placeholders
- [ ] No accounts or Todoist tasks created without CREATE_APPROVED
- [ ] Compliance and hardware lead-time blockers called out when applicable

## Security

- Employee personal data in drafts should use example.com emails until HR supplies production addresses securely.
- Provisioning descriptions must not include SSN, bank details, or recovery codes.
- CREATE_APPROVED should enumerate systems one by one to avoid accidental bulk admin grants.

## Pitfalls

- Copying a engineering checklist for a non-technical role grants unnecessary admin tasks in the tracker.
- Setting all provisioning due on D0 ignores multi-day SSO propagation; stagger with realistic offsets.
- Marking training complete in the checklist before LMS enrollment creates false audit evidence.
- Duplicate rows for the same system across HR and IT sheets cause double account creation.
- Omitting offboarding owner for mistaken provisioning prolongs orphaned licenses.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Engineering hire starting 2026-12-08, remote US, systems GitHub, Google Workspace, Okta, Slack.
- **Input:** Standard template "engineering-remote".
- **Prompt:**

```text
Build onboarding checklist and provisioning tracker for start 2026-12-08, role Software Engineer I. Systems: GitHub, Google Workspace, Okta, Slack. Output tables; no API calls.
```

- **Expected result:**

```text
Checklist excerpt (12 rows): laptop ship-by D-7 IT; Okta invite D-3 IT; manager intro D0 Manager; security training D0-D5 New hire.
Provisioning: ticket drafts titled "Provision GitHub org acme – engineer" with group placeholder `@acme/engineering`.
Status column empty in all rows.
CREATE_APPROVED not invoked; no Todoist tasks created.
```

### Example 2 (Example data (self-written))

- **Task:** Hardware lead-time blocker.
- **Input:** Start in 5 days; laptop SLA 10 business days.
- **Prompt:**

```text
Same hire but laptop SLA 10bd. Flag blockers and suggest mitigations in checklist notes column.
```

- **Expected result:**

```text
Blocker row: "Ship laptop" due D-7 marked AT RISK; note suggests loaner device or start-date slip.
Mitigation task added: "Confirm interim laptop policy" owner IT Manager due D-2.
No automatic ticket filed in ITSM; human opens ticket after review.
```