---
id: monitoring-observability-mcp-focus
title: "Monitoring und Observability: MCP/Skill-Fokus"
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
  - "MCP minimization für observability task"
  - "Validated rule change proposal"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Observability-MCPs (Grafana, Sentry) mit **promtool/kubectl Verify** im Skill kombinieren — keine Alert-Edits ohne lokale Rule-Prüfung.

## Wann nutzen

- Agent soll Dashboards lesen und Alert-Vorschläge ausarbeiten.
- Team skill: MCP read → promtool test → optional MCP write.

**Wann nicht:** Reine CLI-Only — `monitoring-observability-workflow`.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Grafana MCP | Dashboards | UID panels |
| Sentry MCP | Errors | Release link |
| promtool | Gate | vor jeder Rule live |

## System-Prompt / Instruktionen

```text
Observability MCP/Skill focus (devops-cloud/monitoring-observability).

Skill order: fetch context (MCP read) -> draft promql/rule -> promtool local -> approval -> apply kubectl/gh.
Grafana MCP: read dashboard by uid; never delete datasource without approval.
Sentry MCP: fetch issue stats; map release to github sha when possible.
Unverified MCP servers: mark in output; prefer CLI promtool over untrusted write MCP.

MCP writes disabled in prod until promtool test rules passes locally.
One observability MCP pair max (Grafana + Sentry) per session.
Document panel query extracted vs. modified.
Silence creation via MCP forbidden; silences manual with ticket id only.
Matrix column: Verify = promtool test rules file path.
After deploy skill step: suggest instant query to confirm metric moved.
```

## Arbeitsablauf

1. Alert/Dashboard UID aus Ticket.
2. Grafana MCP: Panel queries lesen.
3. Sentry MCP: Issues zur selben Zeitspanne.
4. Rule-Entwurf in Git; `promtool check rules`.
5. Skill Verify-Schritt ausführen.
6. Freigabe einholen; MCP/apply optional.
7. Post-check instant query dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] promtool vor jeder Prod-Rule-Änderung
- [ ] MCP-Write-Pfad dokumentiert oder verweigert
- [ ] Dashboard UID + Panel id in Summary

## Sicherheit & Freigaben

- high risk: Prod alerts.
- Unverified Grafana MCP nicht für Writes ohne Review.

## Fallstricke

- MCP extrahiert veraltetes Panel — Git als Source of Truth.
- Sentry ohne Release-Tag — Korrelation schwach.
- promtool Test vergessen — broken rule paging.
- Zwei Grafana MCPs — Konflikt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Dashboard UID `api-slo` lesen, Rule anpassen.
- **Input:** Panel „Error budget burn“.
- **Prompt:**

```text
Grafana MCP read panel query; draft rule; promtool test before any write.
```

- **Erwartetes Ergebnis:**

```text
MCP returned query sum(rate(...[5m]))
promtool test rules tests/slo_test.yaml OK
Write blocked pending APPROVE
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Sentry+Grafana Korrelation.
- **Input:** Spike 09:00 UTC.
- **Prompt:**

```text
Minimize MCPs; timeline entry linking sentry release to dashboard spike.
```

- **Erwartetes Ergebnis:**

```text
Release api@3.1.0; Grafana panel request rate +80% 09:00-09:15 UTC
```