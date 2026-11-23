---
id: monitoring-observability-workflow
title: "Monitoring und Observability"
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
  - "Metric/Alert-Name, Cluster oder VM"
  - "SLO oder Schwellwert"
outputs:
  - "Validierte Rule oder Dashboard-JSON-Snippet"
  - "Runbook-Link für Alert"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Metriken, Alerts und SLOs pflegen — PromQL prüfen, Rules testen, Prod-Alerts nicht stillschweigend deaktivieren.

## Wann nutzen

- Neuer Alert, flaky firing, Dashboard für on-call.
- Nach Deploy: SLI-Verifikation.

**Wann nicht:** Vollständiges Observability-Vendor-Migration in einem Sprint.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| promtool | Rules | check rules |
| Prometheus API | Query | instant/range |
| Grafana | Dashboards | Export/Import JSON |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Alert symptom und aktuelle Rule-Datei laden.
2. `promtool check rules alerts/api.yaml`.
3. Test vectors: `promtool test rules tests/api_alerts_test.yaml`.
4. Live: `curl -G 'http://prom:9090/api/v1/query' --data-urlencode 'query=rate(http_requests_total{status=~"5.."}[5m])'`.
5. Rule-Änderung als PR; Grafana Panel ergänzen.
6. Nach Freigabe: `kubectl apply -f servicemonitor-api.yaml`.
7. Ampeco firing test in staging (`amtool alert add` nur staging).

## Qualitätskriterien / Definition of Done

- [ ] promtool check + test grün
- [ ] Runbook-Annotation gesetzt
- [ ] Kein prod silence ohne Ticket

## Sicherheit & Freigaben

- Prod-Alert-Config: high risk.
- Metrics können interne Hostnamen enthüllen — redigieren in öffentlichen Tickets.

## Fallstricke

- `rate()` ohne `[5m]` minimum sinnvoll — spike noise.
- Alert ohne `for:` — flapping pager.
- Recording rule cyclic dependency.
- Grafana Variable ohne datasource — broken dashboard.
- kube-state-metrics fehlt — Pods unknown aber App „up“.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 5xx-Rate-Alert prüfen.
- **Input:** `alerts/api.yaml` rule `HighErrorRate`.
- **Prompt:**

```text
promtool check and test; show instant query for current 5xx rate.
```

- **Erwartetes Ergebnis:**

```bash
promtool check rules alerts/api.yaml
promtool test rules tests/api_alerts_test.yaml
curl -G 'http://localhost:9090/api/v1/query' \
  --data-urlencode 'query=sum(rate(http_requests_total{status=~"5.."}[5m]))'
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** ServiceMonitor für neues Deployment.
- **Input:** NS `prod`, port metrics 8080.
- **Prompt:**

```text
Draft ServiceMonitor yaml; apply only after approval note.
```

- **Erwartetes Ergebnis:**

```bash
kubectl apply -f servicemonitor-api.yaml   # after APPROVE
kubectl get servicemonitor -n prod
```