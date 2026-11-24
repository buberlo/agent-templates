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
  - "Symptom time windows and dashboards"
outputs:
  - "Incident-Timeline"
  - "Mitigation + Follow-up-Tickets"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Structured **Incident Response**: stabilize, communicate, root cause later — with documented kubectl/gh steps.

## When to use

- Sev1/Sev2: Ausfall or massive Latenz in Prod.
- Post-incident: Timeline rekonstruieren.

**When not to use:** Pentest or Forensik (security-Domain).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| kubectl | K8s mitigation | rollouts, scale |
| gh | Deploy correlation | last green runs |
| Statuspage | Kommun | optional manuell |

## System prompt

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

## Workflow

1. Record severity and concern; Channel/Bridge-Link.
2. `kubectl -n <ns> get pods,deploy` and events last 30 min.
3. Deploy-Korrelation: `gh run list --branch main --limit 5`.
4. Mitigation vorschlagen; nach approval e.g. `kubectl rollout undo`.
5. Monitoring-Fenster beobachten; Status-Update-Entwurf.
6. Continue timeline in the ticket.
7. Post-mortem action items with owner.

## Definition of done

- [ ] Service back within SLO or justified degradation
Timeline with UTC and commands
- [ ] No ungenehmigten destruktiven Aktionen

## Security

- Prod-Mitigation: high risk; IC/On-Call-approval.
And then, in fact, they are public.

## Pitfalls

- Rollback without Traffic-Shift bei DB-Migration — Daten inkonsistent.
- Too early "resolved" - Flapping returns.
- Parallele Helden-Fixes without Koordination — mehr Schaden.
- gh/Kubectl aus falscher Umgebung — falscher Cluster.
- Postmortem without Zeitkompensation — Lessons gehen verloren.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** API 500 nach Deploy; Rollback.
- **Input:** Sev1, NS `prod`, Deploy `api` 14:32 UTC.
- **Prompt:**

```text
Correlate gh run with spike; propose kubectl rollout undo; draft status line only.
```

- **Expected result:**

```bash
gh run list --workflow=deploy.yml --limit 3
kubectl -n prod rollout undo deploy/api
# Timeline entry + customer draft "Investigating errors..."
```

### Example 2 (Example data (self-written))
- **Task:** Not Deploy — DB Connection Exhaustion.
- **Input:** Hikari pool maxed, no recent deploy.
- **Prompt:**

```text
Read pods and events; suggest scale replicas not rollback; document hypothesis.
```

- **Expected result:**

```bash
kubectl -n prod get pods -l app=api
kubectl -n prod top pods
# Recommend scale deploy/api --replicas=8 after approval
```