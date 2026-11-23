---
id: incident-response-workflow
title: "Incident Response"
domain: devops-cloud
category: incident-response
tags:
  - incident
  - sre
  - oncall
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: kubectl
    install: "kubeconfig on-call scope"
    version_notes: "Read-first, write gated"
  - name: gh
    install: "Incident channel + Actions"
    version_notes: "Run logs"
  - name: pagerduty-cli
    install: "optional"
    version_notes: "Ack/notes"
inputs:
  - "Incident-ID, Severity, betroffener Service"
  - "Symptom-Zeitfenster und Dashboards"
outputs:
  - "Incident-Timeline"
  - "Mitigation + Follow-up-Tickets"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Strukturierte **Incident Response**: stabilisieren, kommunizieren, root cause später — mit dokumentierten kubectl/gh-Schritten.

## Wann nutzen

- Sev1/Sev2: Ausfall oder massive Latenz in Prod.
- Post-incident: Timeline rekonstruieren.

**Wann nicht:** Pentest oder Forensik (security-Domain).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubectl | K8s mitigation | rollouts, scale |
| gh | Deploy-Korrelation | letzte grüne Runs |
| Statuspage | Kommun | optional manuell |

## System-Prompt / Instruktionen

```text
Incident response workflow (devops-cloud/incident-response).

Follow stabilize, communicate, investigate, remediate, postmortem — no blame.
First: confirm incident scope, severity, incident commander if user names one.
Read-only triage: metrics links, kubectl get pods, gh run list for deploy correlation.
Mitigation options ranked by reversibility: scale up, feature flag off, rollback, traffic shift.
Never delete data stores or databases during incident without explicit IC approval.
Document timeline entries with UTC timestamps as user provides them.

Every mitigation command must be echoed before execution; prod writes gated.
Customer comms: draft only, no send without approval.
Capture: what changed in last 60 minutes (deploy, config, traffic).
After stable: open follow-ups for root cause; no premature "fixed forever".
Pager/Slack secrets not in transcript.
```

## Arbeitsablauf

1. Severity und Betroffenheit festhalten; Kanal/Bridge-Link.
2. `kubectl -n <ns> get pods,deploy` und Events letzte 30 min.
3. Deploy-Korrelation: `gh run list --branch main --limit 5`.
4. Mitigation vorschlagen; nach Freigabe z. B. `kubectl rollout undo`.
5. Monitoring-Fenster beobachten; Status-Update-Entwurf.
6. Timeline im Ticket fortführen.
7. Postmortem-Action-Items mit Owner.

## Qualitätskriterien / Definition of Done

- [ ] Service wieder innerhalb SLO oder begründete Degradation
- [ ] Timeline mit UTC und Befehlen
- [ ] Keine ungenehmigten destruktiven Aktionen

## Sicherheit & Freigaben

- Prod-Mitigation: high risk; IC/On-Call-Freigabe.
- Kundendaten nicht in öffentlichen Incident-Threads.

## Fallstricke

- Rollback ohne Traffic-Shift bei DB-Migration — Daten inkonsistent.
- Zu früh „resolved“ — Flapping kehrt zurück.
- Parallele Helden-Fixes ohne Koordination — mehr Schaden.
- gh/Kubectl aus falscher Umgebung — falscher Cluster.
- Postmortem ohne Zeitkompensation — Lessons gehen verloren.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** API 500 nach Deploy; Rollback.
- **Input:** Sev1, NS `prod`, Deploy `api` 14:32 UTC.
- **Prompt:**

```text
Correlate gh run with spike; propose kubectl rollout undo; draft status line only.
```

- **Erwartetes Ergebnis:**

```bash
gh run list --workflow=deploy.yml --limit 3
kubectl -n prod rollout undo deploy/api
# Timeline entry + customer draft "Investigating errors..."
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Nicht Deploy — DB Connection Exhaustion.
- **Input:** Hikari pool maxed, no recent deploy.
- **Prompt:**

```text
Read pods and events; suggest scale replicas not rollback; document hypothesis.
```

- **Erwartetes Ergebnis:**

```bash
kubectl -n prod get pods -l app=api
kubectl -n prod top pods
# Recommend scale deploy/api --replicas=8 after approval
```