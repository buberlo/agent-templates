---
id: plattform-deploy-mcp-focus
title: "Platform Deploy: MCP/Skill-Fokus"
domain: devops-cloud
category: plattform-deploy
tags:
  - deploy
  - mcp
  - vercel
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "Actions, deployments API"
    version_notes: "Read deployments"
  - name: Vercel MCP
    install: "Marketplace / team MCP"
    version_notes: "Verify write policy"
  - name: gh
    install: "workflow_dispatch"
    version_notes: "When MCP write disabled"
inputs:
  - "Preview vs prod skill gates"
  - "Project/deployment IDs"
outputs:
  - "Deploy skill with MCP matrix"
  - "Audit trail summary"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Deploy-MCPs (GitHub Deployments, Vercel) in Skills mit **PROD_APPROVE**-Gate und CLI-Fallback wenn Writes in Policy aus sind.

## Wann nutzen

- Agent nutzt Vercel/GitHub MCP für Releases.
- Team dokumentiert MCP-minimierten Deploy-Skill.

**Wann nicht:** Nur kubectl/helm — siehe `k8s-*` und `plattform-deploy-workflow`.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub MCP | Deploy status | environments |
| Vercel MCP | Preview/prod | team policy |
| gh | Fallback | explicit CLI |

## System-Prompt / Instruktionen

```text
Platform deploy MCP/Skill focus (devops-cloud/plattform-deploy).

Skill steps: build verify (read) | preview deploy (write gated) | smoke | PROD_APPROVE | prod deploy | audit.
GitHub MCP: list deployments for environment; never approve deployment protection rules.
Vercel MCP: create preview deployment; prod promotion only step 5 after keyword.
If MCP write tools disabled in client, use gh workflow run or vercel CLI in skill text.

Single deploy MCP namespace; no duplicate hosting MCPs.
Record deployment_url from MCP response redacting tokens.
Rollback step must reference platform native command, not MCP delete guessing.
Hermes/OpenClaw: mark deploy tools needs approval true.
Post-deploy: MCP read deployment status until ready.
```

## Arbeitsablauf

1. Skill laden; Deploy-MCP-Whitelist.
2. GitHub MCP: letzte Deployment-Status production.
3. Preview via MCP oder `vercel deploy` Skill-Schritt.
4. Smoke URLs curl.
5. Block bis PROD_APPROVE.
6. Prod deploy MCP/gh; Deployment-ID speichern.
7. Matrix und Audit ins Ticket.

## Qualitätskriterien / Definition of Done

- [ ] Prod nur nach PROD_APPROVE
- [ ] Deployment-ID + SHA
- [ ] Rollback in Skill definiert

## Sicherheit & Freigaben

- high risk Prod remote deploy.
- MCP-Tokens scoped to project.

## Fallstricke

- Vercel MCP prod aus Versehen — Skill-Gate Pflicht.
- GitHub MCP sieht Fork — falsche Environment.
- Doppelter Deploy MCP Race.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Skill mit MCP preview only.
- **Input:** Projekt `web-shop`.
- **Prompt:**

```text
Steps 1-4 read/preview; block step 5 until PROD_APPROVE TICKET-1.
```

- **Erwartetes Ergebnis:**

```text
Vercel MCP preview url issued
Step 5 status: blocked
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** GitHub deployment audit.
- **Input:** Env `production`.
- **Prompt:**

```text
GitHub MCP list deployments; map to sha; no promote.
```

- **Erwartetes Ergebnis:**

```text
deployment id dpl_123 sha abc1234 status success
```