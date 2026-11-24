---
id: monitoring-observability-mcp-focus
title: "Monitoring and Observability: MCP/Skill Focus"
domain: devops-cloud
category: monitoring-observability
tags:
  - observability
  - mcp
  - grafana
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Grafana MCP
    install: "Community grafana-mcp variants"
    version_notes: "Dashboards read; verify unverified flag"
  - name: Sentry MCP
    install: "Error correlation"
    version_notes: "Links to releases"
  - name: promtool
    install: "Rule validation"
    version_notes: "Local verify before MCP write"
inputs:
  - "Alert name, dashboard UID"
  - "Skill verify steps"
outputs:
  - "MCP minimization for observability task"
  - "Validated rule change proposal"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Combine Observability (Grafana, Sentry) with **promtool/kubectl Verify** in the skill — no alert edits without local rule check.

## When to use

- Agent should read dashboards and work out alert suggestions.
- Team skill: MCP read → promtool test → optional MCP write.

**When not to use:** Reine CLI-Only — `monitoring-observability-workflow`.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Grafana MCP | Dashboards | UID panels |
| Sentry MCP | Errors | Release link |
| promtool | Gate | vor jeder Rule live |

## System prompt

```text
Observability MCP/Skill focus (devops-cloud/monitoring-observability).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Skill order: fetch context (MCP read) -> draft promql/rule -> promtool local -> approval -> apply kubectl/gh.
Grafana MCP: read dashboard by uid; never delete datasource without approval.
Sentry MCP: fetch issue stats; map release to github sha when possible.
Unverified MCP servers: mark in output; prefer CLI promtool over untrusted write MCP.
MCP writes disabled in prod until promtool test rules passes locally.
One observability MCP pair max (Grafana + Sentry) per session.
Document panel query extracted vs. modified.
Silence creation via MCP forbidden; silences manual with ticket id only.
Matrix column: Verify = promtool test rules file path.
After deploy skill step: suggest instant query to confirm metric moved.```

## Workflow

1. Alert/Dashboard UID aus Ticket.
2. Grafana MCP: Panel queries lesen.
3. Sentry MCP: Issues zur selben Zeitspanne.
4. Rule-Entwurf in Git; `promtool check rules`.
5. Perform Skill Verify step.
6. approval einholen; MCP/apply optional.
7. Post-check instant query dokumentieren.

## Definition of done

- [ ] promtool before any Prod-Rule change
- [ ] MCP-Write-Pfad dokumentiert or verweigert
- [ ] Dashboard UID + Panel id in Summary

## Security

- high risk: Prod alerts.
- Unverified Grafana MCP not for writes without review.

## Pitfalls

- MCP extrahiert veraltetes Panel — Git als Source of Truth.
- Sentry without Release-Tag — Korrelation schwach.
- promtool Test vergessen — broken rule paging.
- Zwei Grafana MCPs — Konflikt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Dashboard UID `api-slo` lesen, Rule anpassen.
- **Input:** Panel „Error budget burn“.
- **Prompt:**

```text
Grafana MCP read panel query; draft rule; promtool test before any write.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.MCP returned query sum(rate(...[5m]))
promtool test rules tests/slo_test.yaml OK
Write blocked pending APPROVE
```

### Example 2 (Example data (self-written))
- **Task:** Sentry+Grafana Korrelation.
- **Input:** Spike 09:00 UTC.
- **Prompt:**

```text
Minimize MCPs; timeline entry linking sentry release to dashboard spike.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Release api@3.1.0; Grafana panel request rate +80% 09:00-09:15 UTC
```