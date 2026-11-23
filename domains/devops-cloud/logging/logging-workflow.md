---
id: logging-workflow
title: "Logging"
domain: devops-cloud
category: logging
tags:
  - logging
  - loki
  - cloudwatch
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: kubectl
    install: "stern or kubectl logs"
    version_notes: "Cluster logs"
  - name: aws-cli
    install: "logs filter-log-events"
    version_notes: "CloudWatch"
  - name: logcli
    install: "Grafana Loki logcli"
    version_notes: "Loki queries"
inputs:
  - "Zeitfenster UTC, Service/Label"
  - "Fehlermuster or Trace-ID"
outputs:
  - "Log extract with correlation"
  - "Query-Snippets for dashboard"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Browse central and pod logs, correlate errors, and deliver reusable queries—without raw data bulk export.

## When to use

- Incident-Triage, neue Fehlermeldung in Monitoring.
- Logging-Pipeline-Validierung nach Deploy.

**When not to use:** Long-term archive without legal hold clarification.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| logcli | Loki | LogQL |
| aws logs | CloudWatch | filter-log-events |
| stern | K8s | Live multi-pod |

## System prompt

```text
Logging workflow (devops-cloud/logging).

Always bound time range UTC; default last 1h if user omits, state assumption.
Loki: logcli query '{app="api"} |= "error"' --since=1h --limit=200.
CloudWatch: aws logs filter-log-events --log-group-name --start-time --filter-pattern.
kubectl: kubectl logs deploy/api -n prod --since-time=<rfc3339> --tail=500 max.

Redact emails, tokens, credit cards from excerpts; use *** placeholders.
No download entire log groups to public chat.
Correlate: request_id/trace_id across services when present in fields.
If cardinality high, suggest label changes not ad-hoc .* queries in prod Loki.
Save final LogQL/SQL as copy-paste block for Grafana.
Do not change retention or delete log groups without approval.
Stern: stern -n prod deploy/api --since 30m for burst incidents.
```

## Workflow

1. Clarify time windows and service/labels.
2. Choose Source: Loki vs. CloudWatch vs. kubectl.
3. `logcli labels` or Log-Group-Liste validieren.
4. Run; analyze first 50 lines.
5. Trace-ID verfolgen; zweite Query cross-service.
6. Dashboard-Panel-Query als Snippet exportieren.
7. PII-redigierten Auszug ins Ticket.

## Definition of done

- [ ] Time window and source documented
- [ ] Query wiederverwendbar
- [ ] No Roh-PII im Chat

## Security

Prod logs may contain customer data — minimize.
- Log group deletion only with approval.

## Pitfalls

Unbounded query — Loki/CloudWatch costs and timeout.
- Falsche TZ in --start-time — leere Ergebnisse.
- JSON logs without json parser - Regex misleading.
- nur ERROR-Level — Root in vorherigem INFO.
- kubectl logs without --previous bei CrashLoop.

## Basic examples

### Example 1 (Example data)

- **Task:** Loki Fehler letzte Stunde.
- **Input:** App `checkout`, trace `abc-123`.
- **Prompt:**

```text
LogQL for errors and trace abc-123; limit 100 lines.
```

- **Expected result:**

```bash
logcli query '{app="checkout"} |= "abc-123" | json | level="error"' --since=1h --limit=100
```

### Example 2 (Example data)

- **Task:** CloudWatch Filter.
- **Input:** Group `/ecs/api`, Muster `OutOfMemory`.
- **Prompt:**

```text
filter-log-events last 2h; redact account ids.
```

- **Expected result:**

```bash
aws logs filter-log-events --log-group-name /ecs/api \
  --start-time $(date -d '2 hours ago' +%s000) \
  --filter-pattern "OutOfMemory"
```