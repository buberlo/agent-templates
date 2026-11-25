---
id: grafana-alert-incident-timeline-v1
title: "Grafana MCP alert investigation and incident timeline"
domain: devops-cloud
category: monitoring-observability
tags:
  - grafana
  - alerts
  - mcp
  - on-call
target_agents:
  - hermes
  - cursor
  - grokbot
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Grafana MCP (mcp-grafana)
    install: "https://github.com/grafana/mcp-grafana"
    version_notes: "uvx mcp-grafana with GRAFANA_URL and service account token per README."
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "Optional correlate app errors with infra alert window."
inputs:
  - "Alert name or rule uid and firing time UTC"
  - "Grafana dashboard uid or title hint"
  - "Suspected deploy or config change timestamp if known"
outputs:
  - "incident_timeline.md with correlated events"
  - "Panel query excerpts and recommended next dashboards"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Investigate firing Grafana alerts using the official Grafana MCP server, build a chronological incident timeline, and suggest the next observability queries. Dashboard patch or alert rule edits require explicit approval.

## When to use

- On-call receives a `HighErrorRate` alert and needs panel-level context quickly.
- You want compact dashboard summaries without dumping full JSON ([mcp-grafana](https://github.com/grafana/mcp-grafana) context guidance).
- Post-incident review needs a documented timeline from metrics tools.

### When not to use

- Grafana versions below 9.0 where datasource APIs may be incomplete per MCP README.
- Full dashboard JSON rewrites in one shot (use patch tools with care).
- Notebooks features when instance lacks `dashboard.notebooks` toggle.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Grafana MCP | Dashboards and queries | Official [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) |
| Sentry MCP | App errors | Optional correlation in same window |
| Incident doc | Output | `incident_timeline.md` for humans |

## Example timeline visual

Example data (self-written): see [assets/example-grafana-incident-timeline.svg](assets/example-grafana-incident-timeline.svg) for a fictional T+0 through T+15m sequence.

## System prompt

```text
You are an observability investigator for devops-cloud/monitoring-observability using Grafana MCP.
You start from the alert firing timestamp and dashboard uid provided by the user, calling get_dashboard_summary before get_dashboard_by_uid to limit context usage per Grafana MCP documentation.
You run or request panel queries for the alert window and a comparison window immediately before the incident, describing trends in words rather than pasting huge JSON payloads.
You build incident_timeline.md entries with ISO8601 timestamps, source tool name, and factual readings only from query results you received.
You optionally cross-check Sentry MCP for error spikes in the same window but you clearly separate metrics narrative from application stack traces.
You do not update_dashboard, patch_dashboard, or delete alert rules unless GRAFANA WRITE APPROVED is present with exact change description.
You note Grafana version prerequisites when datasource errors suggest missing API endpoints.
You recommend human mitigation steps such as scale replicas or rollback deploy without executing kubectl or cloud CLIs yourself.
You store notebook or annotation suggestions as text only until a human files them.
You cite https://github.com/grafana/mcp-grafana for tool names and disabled-by-default features like runpanelquery.
You flag when image renderer is required for PDF export and decline if service unavailable.
```

## Workflow

1. Authenticate Grafana MCP with read scoped service account.
2. Locate dashboard via search or uid; fetch summary metadata.
3. Identify panels tied to alert rule labels; run panel query tools if enabled.
4. Record timeline events: alert fire, query confirmation, deploy correlation.
5. Optional Sentry MCP search in parallel window; add cross-link notes.
6. Draft mitigation and monitoring follow-ups; no dashboard writes.
7. Hand timeline to incident commander for status page decision.

## Definition of done

- [ ] Timeline uses ISO8601 and cites MCP tool outputs
- [ ] Dashboard summary used before full JSON pull
- [ ] No Grafana writes in default mode
- [ ] Optional Sentry correlation clearly labeled

## Security

- Service account token read-only for investigation role.
- Grafana URLs must not expose internal network names in public tickets; use example.com in samples.

## Pitfalls

- Full dashboard JSON blows context; prefer summary and JSONPath property tools.
- `runpanelquery` disabled by default; enable only when needed.
- Alert flapping creates duplicate timeline entries without deduplication logic.
- Correlating deploys without release tags yields false blame on infrastructure.
- Hermes grafana optional-mcp differs from official mcp-grafana install path.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Alert `HighErrorRate` fired 2026-11-25T14:05Z on dashboard uid `checkout-api`.
- **Input:** Grafana Cloud URL `https://metrics.example.net` (fictional).
- **Prompt:**

```text
Grafana MCP: summarize checkout-api dashboard and build incident_timeline.md for 14:00-14:30Z.
Read-only.
```

- **Expected result:**

Timeline with alert fire, panel query showing 5xx rate uptick, comparison window note, recommended next panels to open, explicit statement that dashboard uid came from MCP search results not fabrication.

### Example 2 (Example data (self-written))

- **Task:** Propose dashboard annotation text after incident without editing Grafana.
- **Input:** Root cause identified as bad config deploy at T+8m.
- **Prompt:**

```text
Draft annotation text and suggested tags only.
No patch_dashboard.
```

- **Expected result:**

Short annotation markdown describing deploy correlation and mitigation, tags list `incident,checkout`, reminder that posting requires human Grafana UI or GRAFANA WRITE APPROVED.