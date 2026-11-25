---
id: incident-response-workflow
title: "Incident response"
domain: devops-cloud
category: incident-response
tags:
  - incident
  - sre
  - oncall
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: kubectl
    install: "kubeconfig scoped to on-call RBAC"
    version_notes: "Read-first; writes gated"
  - name: GitHub CLI
    install: "https://cli.github.com/manual/gh"
    version_notes: "Run logs and deploy correlation"
inputs:
  - "Incident id, severity, and affected service"
  - "Symptom time window and dashboard links"
outputs:
  - "Incident timeline with UTC stamps"
  - "Mitigation commands and follow-up tickets"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Run **structured incident response**: stabilize first, communicate clearly, investigate root cause later — with documented kubectl and GitHub CLI steps and no blame.

## When to use

- Sev1 or Sev2 outages or severe latency in production.
- Post-incident timeline reconstruction from chat and logs.

### When not to use

- Penetration tests or forensic investigations owned by the security domain.
- Planned maintenance without customer impact.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| kubectl | Kubernetes mitigation | rollouts, scale, events |
| gh | Deploy correlation | workflow runs around incident start |
| Statuspage (manual) | Customer comms | drafts only unless approved |

## System prompt

```text
You are an incident response assistant for devops-cloud/incident-response.
You follow stabilize, communicate, investigate, remediate, and postmortem without assigning blame.
You first confirm incident scope, severity, and incident commander when the user names one.
You perform read-only triage: metrics links, kubectl get pods, and gh run list for deploy correlation.
You rank mitigation options by reversibility: scale up, feature flag off, rollout undo, traffic shift.
You never delete data stores or databases during an incident without explicit incident commander approval.
You document timeline entries with UTC timestamps as the user provides them.
You echo every mitigation command before execution and gate production writes behind approval tokens.
You draft customer communications only and never send without explicit approval.
You capture what changed in the last 60 minutes: deploy, config, traffic, or feature flags.
You after stability open follow-up tickets for root cause instead of claiming permanent fix.
You keep PagerDuty and Slack webhook secrets out of the transcript.
```

## Workflow

1. Record severity, scope, and bridge channel link.
2. `kubectl -n <ns> get pods,deploy` and events for the last 30 minutes.
3. Correlate deploy: `gh run list --workflow deploy.yml --limit 5`.
4. Propose mitigations; execute only after APPROVE with echoed command.
5. Watch metrics window; draft status update for humans.
6. Append timeline entries with command outputs redacted for PII.
7. List postmortem actions with owners and due dates.

## Definition of done

- [ ] Service within SLO or degradation documented and accepted
- [ ] Timeline with UTC timestamps and command list
- [ ] No unapproved destructive actions executed

## Security

- Production mitigation is **high risk**; incident commander approval for writes.
- Do not paste customer data from logs into public tickets.
- kubeconfig and tokens stay out of chat.

## Pitfalls

- Rollback without traffic shift when a DB migration already ran — data inconsistency.
- Marking resolved too early while error rates flap.
- Parallel uncoordinated fixes from multiple responders.
- kubectl against wrong context or cluster.
- Postmortem skipped because on-call fatigue.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** API 500 after deploy; propose rollback.
- **Input:** Sev1, namespace `prod`, deploy `api` at 14:32 UTC.
- **Prompt:**

```text
Correlate gh run with spike; propose kubectl rollout undo; draft status line only.
```

- **Expected result:**

```text
gh run list shows workflow finished 14:30 UTC on commit abc1234
kubectl -n prod rollout undo deploy/api proposed; blocked until APPROVE
Timeline bullet: spike at 14:33 UTC correlates with deploy
Customer draft: "We are investigating elevated error rates on API" — not sent
```

### Example 2 (Example data (self-written))

- **Task:** Connection pool exhaustion without recent deploy.
- **Input:** Hikari pool maxed; no green deploy in window.
- **Prompt:**

```text
Read pods and events; suggest scale replicas not rollback; document hypothesis.
```

- **Expected result:**

```text
kubectl -n prod get pods shows Ready but throttled; events show probe timeouts
kubectl top pods suggests CPU headroom; scale to 8 replicas proposed after APPROVE
Rollback not recommended; hypothesis documented as DB pool wait not bad release
Follow-up ticket: pool sizing and connection leak investigation
```