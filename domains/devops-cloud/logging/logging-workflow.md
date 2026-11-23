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
  - "Fehlermuster oder Trace-ID"
outputs:
  - "Log-Auszug mit Korrelation"
  - "Query-Snippets für Dashboard"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Zentrale und Pod-Logs durchsuchen, Fehler korrelieren und **wiederverwendbare Queries** liefern — ohne Rohdaten-Massenexport.

## Wann nutzen

- Incident-Triage, neue Fehlermeldung in Monitoring.
- Logging-Pipeline-Validierung nach Deploy.

**Wann nicht:** Langzeit-Archiv ohne Legal Hold Klärung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| logcli | Loki | LogQL |
| aws logs | CloudWatch | filter-log-events |
| stern | K8s | Live multi-pod |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Zeitfenster und Service/Labels klären.
2. Quelle wählen: Loki vs. CloudWatch vs. kubectl.
3. `logcli labels` oder Log-Group-Liste validieren.
4. Query ausführen; erste 50 Zeilen analysieren.
5. Trace-ID verfolgen; zweite Query cross-service.
6. Dashboard-Panel-Query als Snippet exportieren.
7. PII-redigierten Auszug ins Ticket.

## Qualitätskriterien / Definition of Done

- [ ] Zeitfenster und Quelle dokumentiert
- [ ] Query wiederverwendbar
- [ ] Keine Roh-PII im Chat

## Sicherheit & Freigaben

- Prod-Logs können Kundendaten enthalten — Minimierung.
- Log-Group-Löschung nur mit Freigabe.

## Fallstricke

- Unbounded query — Loki/CloudWatch Kosten und Timeout.
- Falsche TZ in --start-time — leere Ergebnisse.
- JSON-Logs ohne json parser — Regex irreführend.
- nur ERROR-Level — Root in vorherigem INFO.
- kubectl logs ohne --previous bei CrashLoop.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Loki Fehler letzte Stunde.
- **Input:** App `checkout`, trace `abc-123`.
- **Prompt:**

```text
LogQL for errors and trace abc-123; limit 100 lines.
```

- **Erwartetes Ergebnis:**

```bash
logcli query '{app="checkout"} |= "abc-123" | json | level="error"' --since=1h --limit=100
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** CloudWatch Filter.
- **Input:** Group `/ecs/api`, Muster `OutOfMemory`.
- **Prompt:**

```text
filter-log-events last 2h; redact account ids.
```

- **Erwartetes Ergebnis:**

```bash
aws logs filter-log-events --log-group-name /ecs/api \
  --start-time $(date -d '2 hours ago' +%s000) \
  --filter-pattern "OutOfMemory"
```