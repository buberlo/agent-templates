---
id: platform-deploy-mcp-focus
title: "Platform Deploy: MCP/Skill focus"
domain: devops-cloud
category: platform-deploy
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

## Purpose

Deploy MCPs (GitHub Deployments, Vercel) in Skills with **PROD APPROVE** gate and CLI fallback when Writes in Policy are off.

## When to use

Agent uses Vercel/GitHub MCP for releases.
- Team documents MCP-minimized deploy skill.

**When not to use: therefore only kubectl/helm — see `k8s-*` and `platform-deploy-workflow`.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| GitHub MCP | Deploy status | environments |
| Vercel MCP | Preview/prod | team policy |
| gh | Fallback | explicit CLI |

## System prompt

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

## Workflow

1. Skill laden; Deploy-MCP-Whitelist.
2. GitHub MCP: letzte Deployment-Status production.
3. Preview via MCP or `vercel deploy` Skill-Schritt.
4. Smoke URLs curl.
5. Block bis PROD_APPROVE.
6. Prod deploy MCP/gh; save deployment ID.
7. Matrix and audit into the ticket.

## Definition of done

- [ ] Prod only after PROD_APPROVE
- [ ] Deployment-ID + SHA
- [ ] Rollback in Skill definiert

## Security

- high risk Prod remote deploy.
- MCP-Tokens scoped to project.

## Pitfalls

- Accidental prod deploy via Vercel MCP — skill gate required.
- GitHub MCP sieht Fork — falsche Environment.
- Duplicate deploy MCP race.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Skill with MCP preview only.
- **Input:** Projekt `web-shop`.
- **Prompt:**

```text
Steps 1-4 read/preview; block step 5 until PROD_APPROVE TICKET-1.
```

- **Expected result:**

```text
Vercel MCP preview url issued
Step 5 status: blocked
```

### Example 2 (Example data (self-written))
- **Task:** GitHub deployment audit.
- **Input:** Env `production`.
- **Prompt:**

```text
GitHub MCP list deployments; map to sha; no promote.
```

- **Expected result:**

```text
deployment id dpl_123 sha abc1234 status success
```