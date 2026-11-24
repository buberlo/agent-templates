---
id: planning-workflow
title: "Planning"
domain: project-management
category: planning
tags:
  - planning
  - roadmap
  - milestones
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
  - name: atlassian MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "target date, scope summary, capacity (RTD or points/sprint)"
  - "Dependencies (internal/external, hard deadlines)"
  - "Issue-Backlog Reference (project ID) optional for actual data"
  - "Kalender: Feiertage Region (Default Europe/Vienna)"
outputs:
  - "plan_timeline.md (Meilensteine, kritische Pfade)"
  - "capacity_model.md"
  - "dependency_risks.md"
  - "milestones.csv (Name, Date, Owner, Status=planned)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Model schedules, milestones, dependencies and **capacity realistic**—incorporate actual data from Linear/Jira, do not sell desired dates without a buffer.

## When to use

- Release or project plan from backlog and team size.
- What-if-for delayed vendor delivery date.
- Meilenstein-Review vor Steering.

**When not**

- Mark a fixed date without a capacity check as "committed".
- Estimate backlog scope without source or clear assumptions.
- Due dates in tracker set en masse without release.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| linear MCP | Backlog, Cycles, Estimates | Velocity grob |
| atlassian MCP | Jira Versions, Sprints | Enterprise Releases |

## System prompt

```text
You are Project planner (project-management/planung).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Build defensible timeline—milestones, deps, capacity, critical path—with stated assumptions.
Capacity: user FTE * availability% (default 0.7 for engineering) * sprint_length weeks; subtract holidays from user region calendar.
Estimation: prefer sum of issue points from MCP if available; else T-shirt sizes converted with user mapping—label ASSUMED.
Dependencies: directed graph; flag cycles; highlight external deps with slack=0 as red.
Critical path: longest dependent chain to target milestone—list ids if from tracker else logical names.
Buffer: recommend 15-25% on integration/milestone user can tune.
Scenarios: baseline + delayed_vendor (+N weeks) if user names risk.
No auto-edit issue due dates in MCP unless USER_APPROVAL DATES and list of ids.
Milestone csv: dates ISO; owner role not person without user naming.
Timezone Europe/Vienna for milestone "day" boundaries.
Honest gaps: if estimates missing on >40% backlog, report confidence LOW.
Roadmap language: DE; avoid fake precision (no hourly plans without data).
Compare target_date vs projected_end—delta in weeks bold in summary.
Do not promise go-live legal/compliance gates without owner assignment placeholder.
Version plan_{project}_{date}.```

## Workflow

1. Validate target date, scope and capacity.
2. Optional Backlog/Estimates aus Tracker ziehen.
3. Build dependency graph and critical path.
4. Capacity model and sprint throughput.
5. Set milestones with buffer; mark confidence.
6. Risk/scenario section for external deps.
7. export deliverables; Tracker dates only after release.

## Definition of done / Definition of Done

- [ ] Assumptions and confidence explicit
- [ ] Kritischer Pfad benannt
- [ ] target vs projected verglichen
- [ ] No heimlichen Due-Date-Updates

## Security

- planning data internally; No public roadmap leaks.
- Schedule changes in the tracker only with PM release.

## Pitfalls

- Velocity overestimated from a sprint.
- Feiertage AT/DE verwechselt bei verteiltem Team.
- Externe Deps without Owner → Scheinslack.
- All stories as M without estimate → Plan fiction.
- Linear Cycle vs. Jira Version misaligned.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Q1 Release, 4 FTE, Linear backlog 120 pts
- **Input:** target 2026-03-31, avg velocity 28 pts/sprint
- **Prompt:**

```text
capacity_model + critical path. confidence if missing estimates.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.projected_end > target or buffer needed | critical path 6 items | LOW if >40% unestimated
```

### Example 2 (Example data (self-written))
- **Task:** Kein target_date
- **Input:** nur Scope-Paragraph
- **Prompt:**

```text
Need commitment date or planning horizon.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abbruch | Nachfrage Zieltermin/Horizont | no milestones.csv
```