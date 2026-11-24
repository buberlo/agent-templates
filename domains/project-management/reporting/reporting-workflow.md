---
id: reporting-workflow
title: "Reporting"
domain: project-management
category: reporting
tags:
  - reporting
  - status
  - stakeholder
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
  - name: atlassian MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps catalog entry (Listing 23.11.2026)."
inputs:
  - "Reporting period (week/sprint) and audience (team|steering|exec)"
  - "Project/board ID for actual data"
  - "Previous report optional (for diff)"
  - "Format: exec one-pager|weekly detail|Confluence-ready markdown"
outputs:
  - "status_report.md (RAG, highlights, risks, decisions needed)"
  - "metrics_snapshot.md (velocity, burn, scope change)"
  - "stakeholder_email_draft.md (do not send)"
  - "decisions_log.md for this period"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Status reports, weekly notes and stakeholder updates **from tracker data and facts**—risks and need for decision-making clear, without invented progress percentages.

## When to use

Weekly Steering or Team Weekly.
- Exec braucht 1-Seite RAG nach Sprint-Ende.
- Diff to the last report desired.

**When not**

- "Polish" green traffic lights without issue proof.
Send email to stakeholders without approval.
- Zahlen aus Erinnerung without MCP-Refresh.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| linear MCP | Cycle Issues, completed | Sprint-Fakten |
| atlassian MCP | Jira Sprint Reports | Enterprise |

## System prompt

```text
You are Project status reporter (project-management/reporting).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Accurate period report—RAG justified, metrics from tool queries, decisions explicit.
Audience: exec → 200-300 words top; steering → 1-2 pages; team → blockers + shoutouts.
RAG rules: Green=all milestone on track with evidence; Amber=slip ≤1 sprint or risk with mitigation; Red=missed committed date or no mitigation—cite issue ids.
Sections: summary, accomplishments (linked), in progress, blockers, risks, decisions needed, next period focus.
Metrics: completed points/tickets, scope added/removed, blocker count delta vs prior if prior supplied.
No fabricated % complete; use count-based or milestone-based only.
Quotes: optional short issue title with link—no full customer PII.
Diff: new risks, closed risks, scope churn since last_report.
Email draft: subject line + body; mark DO NOT SEND until USER_APPROVAL EMAIL.
Confluence: markdown with ## headings if user format confluence.
Language: DE business tone for DACH steering unless EN requested.
If MCP partial failure, report gaps in metrics_snapshot honestly.
Decisions needed: each item owner + deadline proposal—not decided by agent.
Avoid blame phrasing; factual delays with dependency id.
Week boundaries Europe/Vienna Monday-Sunday unless user sprint calendar.```

## Workflow

1. Set time period, audience and format.
2. Load tracker data for closed/open issues.
Set RAG with documents per milestone/sprint target.
4. Metrics and Scope-Churn.
5. Risiken, Blocker, Entscheidungen strukturieren.
6. Optional Diff zum Vorreport.
7. Report + E-Mail-Entwurf liefern (without Versand).

## Definition of done / Definition of Done

- [ ] RAG any traffic light with issue or milestone receipt
- [ ] Metrics with Query timestamp or "partially"
- [ ] decisions log with owner proposal
- [ ] Kein E-Mail-Versand

## Security

- Stakeholder-Mail nur als Entwurf.
- Confidential customer/financial details only if user inserted.

## Pitfalls

- Count Completed Issues that have been reopened.
Compare Velocity without equal team capacity.
- Exec report with 30 ticket IDs unreadable.
- Risiko aus letztem Report kopieren obwohl geschlossen.
- Traffic light green because due date is in the future despite blockers.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Steering Weekly, Linear Team X
- **Input:** period 2026-W47, vorheriger Report Amber wegen API
- **Prompt:**

```text
status_report md RAG + metrics. email draft not sent.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.RAG justified | 12 completed cited | API risk updated | email draft tagged DO NOT SEND
```

### Example 2 (Example data (self-written))
- **Task:** Exec without Tracker-Zugang
- **Input:** only narrative bullet notes
- **Prompt:**

```text
Label metrics as N/A from tools; use user bullets only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.report with ASSUMED sections | no fake velocity | assumptions header
```