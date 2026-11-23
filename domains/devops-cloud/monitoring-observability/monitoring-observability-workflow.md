---
id: monitoring-observability-workflow
title: "Monitoring and Observability"
domain: devops-cloud
category: monitoring-observability
tags:
  - prometheus
  - grafana
  - alerts
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: promtool
    install: "Teil von Prometheus"
    version_notes: "rules test"
  - name: curl
    install: "Prometheus HTTP API"
    version_notes: "instant query"
  - name: kubectl
    install: "ServiceMonitors CR"
    version_notes: "Operator stacks"
inputs:
  - "Metric/Alert-Name, Cluster or VM"
  - "SLO or Schwellwert"
outputs:
  - "Validierte Rule or Dashboard-JSON-Snippet"
  - "Runbook link for Alert"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Maintain metrics, alerts and SLOs — check PromQL, test rules, do not silently deactivate Prod alerts.

## When to use

- New alert, flaky firing, dashboard for on-call.
- Nach Deploy: SLI-Verifikation.

**When not to use:** Full observability vendor migration in a sprint.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| promtool | Rules | check rules |
| Prometheus API | Query | instant/range |
| Grafana | Dashboards | Export/Import JSON |

## System prompt

```text
Observability workflow (devops-cloud/monitoring-observability).

Validate recording and alerting rules with promtool check rules and promtool test rules.
Query live: curl -G <prometheus>/api/v1/query --data-urlencode 'query=up{job="api"}'.
SLO alerts: for duration must match error budget policy user provides.
Never silence all alerts in prod without incident id and expiry.
Label sets: consistent job, service, env labels on new rules.
Dashboard changes: export JSON diff summary, not full paste if huge.
kubectl apply ServiceMonitor only after promtool pass and approval.
Recording rules before complex dashboards to avoid expensive queries.
Document alert runbook URL in annotation runbook_url.
No cardinality explosion from high-cardinality labels in user suggestions.
```

## Workflow

1. Alert symptom and current rule file load.
2. `promtool check rules alerts/api.yaml`.
3. Test vectors: `promtool test rules tests/api_alerts_test.yaml`.
4. Live: `curl -G 'http://prom:9090/api/v1/query' --data-urlencode 'query=rate(http_requests_total{status=~"5.."}[5m])'`.
5. Rule change as PR; Grafana Panel supplement.
6. Nach approval: `kubectl apply -f servicemonitor-api.yaml`.
7. Ampeco firing test in staging (`amtool alert add` nur staging).

## Definition of done

- [ ] promtool check + test green
- [ ] Runbook-Annotation gesetzt
- [ ] Kein prod silence without Ticket

## Security

- Prod-Alert-Config: high risk.
- Metrics can reveal internal hostnames - edit in public tickets.

## Pitfalls

- `rate()` without `[5m]` minimum sinnvoll — spike noise.
- Alert without `for:` — flapping pager.
- Recording rule cyclic dependency.
- Grafana Variable without datasource — broken dashboard.
- kube-state-metrics fehlt — Pods unknown aber App „up“.

## Basic examples

### Example 1 (Example data)

- **Task:** Check 5xx rate alert.
- **Input:** `alerts/api.yaml` rule `HighErrorRate`.
- **Prompt:**

```text
promtool check and test; show instant query for current 5xx rate.
```

- **Expected result:**

```bash
promtool check rules alerts/api.yaml
promtool test rules tests/api_alerts_test.yaml
curl -G 'http://localhost:9090/api/v1/query' \
  --data-urlencode 'query=sum(rate(http_requests_total{status=~"5.."}[5m]))'
```

### Example 2 (Example data)

- **Task:** ServiceMonitor for new deployment.
- **Input:** NS `prod`, port metrics 8080.
- **Prompt:**

```text
Draft ServiceMonitor yaml; apply only after approval note.
```

- **Expected result:**

```bash
kubectl apply -f servicemonitor-api.yaml   # after APPROVE
kubectl get servicemonitor -n prod
```