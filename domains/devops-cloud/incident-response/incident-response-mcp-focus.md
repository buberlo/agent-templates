---
id: incident-response-mcp-focus
title: "Incident Response: MCP/Skill-Fokus"
domain: devops-cloud
category: incident-response
tags:
  - incident
  - mcp
  - observability
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "Runs, Deploys"
    version_notes: "Read during incident"
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "Error spikes"
  - name: kubernetes-mcp-server
    install: "https://github.com/containers/kubernetes-mcp-server"
    version_notes: "readonly default"
inputs:
  - "Incident bridge context"
  - "Maps: Skill step → MCP tool"
outputs:
  - "Minimized MCP set for incident"
  - "Correlation notes"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Unter Incident-Zeitdruck nur **notwendige MCPs** aktiv lassen: GitHub Runs, Sentry-Spikes, Kubernetes readonly — Skill steuert Freigaben.

## Wann nutzen

- Agent unterstützt Incident Commander mit Lesen/Korrelation.
- Team will Incident-Skill mit MCP-Matrix pflegen.

**Wann nicht:** Erste Hilfe ohne Skill — erst `incident-response-workflow`.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Sentry MCP | Errors | Release + fingerprint |
| GitHub MCP | Deploys | Run ↔ commit |
| K8s MCP | Pods | readonly diagnose |

## System-Prompt / Instruktionen

```text
Incident MCP/Skill focus (devops-cloud/incident-response).

Minimize MCP count: three servers max during active incident.
Skill gates: correlate (read) -> propose mitigation -> await APPROVE -> execute kubectl/gh write tools.
Sentry MCP: fetch issue stats for release version user names; no PII paste.
GitHub MCP: list workflow runs around incident start timestamp.
Kubernetes MCP: access-level readonly; never admin without IC sign-off.

Disable unrelated MCPs (Notion, email send) for session duration.
Document tool provenance in timeline bullets.
MCP write tools off by default in Cursor/Hermes policy.
If MCP auth fails, fall back to gh/kubectl CLI in skill without disabling incident bridge.
Post-incident: restore normal MCP profile.
```

## Arbeitsablauf

1. Incident-Skill laden; MCP-Whitelist anwenden.
2. Matrix: correlate deploy | correlate errors | pod status.
3. Sentry + GitHub MCP parallel reads; Zeitfenster UTC.
4. K8s MCP describe failing workload.
5. Vorschlag ins Bridge-Dokument; keine Auto-Mitigation.
6. Nach APPROVE: Skill-Schritt mit kubectl/gh (nicht MCP write unless configured).
7. Post-incident: Matrix und MCP-Liste zurücksetzen.

## Qualitätskriterien / Definition of Done

- [ ] ≤3 MCPs aktiv während Incident
- [ ] Korrelation Deploy↔Error dokumentiert
- [ ] Writes nur nach explizitem APPROVE

## Sicherheit & Freigaben

- high risk in Prod; IC-Freigabe für Writes.
- Sentry/K8s-Daten können PII enthalten — redigieren.

## Fallstricke

- Alle MCPs an — langsamer Agent, falsche Tool-Wahl.
- Sentry MCP Rate Limits unter Last.
- K8s MCP mit admin aus Versehen — Gefahr.
- GitHub MCP ohne Zeitfilter — zu viele Runs.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** MCP-Minimierung bei Sev1.
- **Input:** 12 MCPs aktiv, Incident API down.
- **Prompt:**

```text
Whitelist Sentry, GitHub, k8s readonly; map skill steps; disable others.
```

- **Erwartetes Ergebnis:**

```text
Active: sentry-mcp, github-mcp, kubernetes-mcp (readonly)
Steps 1-3 read-only; step 4 blocked until APPROVE
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Deploy-Korrelation zu Sentry Release.
- **Input:** Release `api@2.4.0`, spike 15:10 UTC.
- **Prompt:**

```text
Use MCPs only to link gh run id to sentry issue count; timeline bullet.
```

- **Erwartetes Ergebnis:**

```text
Run 20155678 finished 15:08 UTC; Sentry events +340% for release api@2.4.0
```