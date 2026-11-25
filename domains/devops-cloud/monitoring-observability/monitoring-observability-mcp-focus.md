---
id: monitoring-observability-mcp-focus
title: "Monitoring and observability: MCP focus"
domain: devops-cloud
category: monitoring-observability
tags:
  - observability
  - mcp
  - grafana
target_agents:
  - hermes
  - cursor
  - claude-code
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Grafana MCP (community)
    install: "Verify package against org allow list"
    version_notes: "Dashboard read; unverified flag in catalog"
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "Release-linked errors"
  - name: promtool
    install: "https://prometheus.io/docs/prometheus/latest/command-line/promtool/"
    version_notes: "Local rule check before any prod change"
inputs:
  - "Alert name or dashboard UID"
  - "Skill verify steps for rule changes"
outputs:
  - "MCP minimization plan for observability task"
  - "Validated rule change proposal"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Combine observability reads (Grafana, Sentry) with **promtool verification** in the skill — no production alert rule edits without a local rule test pass.

## When to use

- An agent reads dashboards and drafts alert or recording rule changes.
- Team skill pattern: MCP read, promtool test, optional apply after approval.

### When not to use

- Pure CLI-only observability without MCP hosts.
- Exploratory ad hoc queries with no change proposal.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Grafana MCP | Dashboards | Panel queries by UID |
| Sentry MCP | Errors | Release to SHA correlation |
| promtool | Gate | `promtool check rules` before live |

## System prompt

```text
You are an observability MCP focus assistant for devops-cloud/monitoring-observability.
You order work as fetch context via MCP read, draft PromQL or rule YAML, run promtool locally, obtain approval, then apply via kubectl or gh.
You read Grafana dashboards by UID via MCP and never delete datasources without approval.
You use Sentry MCP for issue stats and map releases to GitHub SHAs when tags allow.
You mark unverified MCP servers in output and prefer CLI promtool over untrusted write MCP.
You disable MCP writes in production until promtool test rules passes on the changed file.
You enable at most one observability MCP pair per session, typically Grafana plus Sentry.
You document extracted panel queries separately from proposed modifications.
You forbid silence creation via MCP; silences stay manual with ticket ids.
You map skill Verify step to promtool test rules with file path.
You after deploy suggest instant queries to confirm metric movement.
You keep Git as source of truth when MCP panel text looks stale.
```

## Workflow

1. Parse alert name or dashboard UID from ticket.
2. Grafana MCP: read panel queries for target UID.
3. Sentry MCP: issues in the same UTC window.
4. Draft rule change in git; run `promtool check rules`.
5. Execute skill Verify step with promtool output archived.
6. Obtain approval; apply via GitOps or documented MCP write path.
7. Post-check instant query and attach result to ticket.

## Definition of done

- [ ] promtool passed before any production rule change
- [ ] MCP write path documented or explicitly refused
- [ ] Dashboard UID and panel id in summary

## Security

- **High risk** for production alerting paths.
- Unverified Grafana MCP must not perform writes without security review.
- Do not paste internal-only dashboard URLs with tokens into public tickets.

## Pitfalls

- MCP returns stale panel text — diff against git.
- Sentry without release tags weakens deploy correlation.
- Skipping promtool ships broken rules that page falsely.
- Two Grafana MCP servers with conflicting configs.
- MCP write enabled before promtool gate in skill order.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Read dashboard UID `api-slo` and tune burn rule.
- **Input:** Panel “Error budget burn”.
- **Prompt:**

```text
Grafana MCP read panel query; draft rule; promtool test before any write.
```

- **Expected result:**

```text
MCP returns query sum(rate(http_requests_total{status=~"5.."}[5m]))
Rule draft in rules/slo_burn.yaml
promtool test rules rules/slo_burn_test.yaml reports SUCCESS
Write blocked pending APPROVE; git commit hash noted
```

### Example 2 (Example data (self-written))

- **Task:** Correlate Sentry and Grafana spike.
- **Input:** Spike 09:00 UTC.
- **Prompt:**

```text
Minimize MCPs; timeline entry linking sentry release to dashboard spike.
```

- **Expected result:**

```text
Active MCPs: Sentry plus Grafana only
Release api@3.1.0; Grafana panel request rate +80 percent 09:00–09:15 UTC
Timeline entry for incident bridge; SHA from GitHub tag when available
No alert silences created via MCP
```