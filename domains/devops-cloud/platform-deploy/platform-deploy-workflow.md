---
id: platform-deploy-workflow
title: "Platform Deploy"
domain: devops-cloud
category: platform-deploy
tags:
  - deploy
  - vercel
  - production
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: vercel
    install: "npm i -g vercel"
    version_notes: "vercel deploy --prebuilt"
  - name: gh
    install: "Deployment via Actions"
    version_notes: "workflow_dispatch gated"
  - name: kubectl
    install: "optional K8s prod"
    version_notes: "approval Pflicht"
inputs:
  - "Zielumgebung (preview/prod)"
  - "Artifact or Git SHA"
outputs:
  - "Deployment-URL or Revision"
  - "Rollback-Befehl"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Platform deployments (Vercel️,ms, K8s Prod) with **Preview-first**, Prod only after explicit approval and rollback plan.

## When to use

- Release Promotion preview → production.
- Hotfix path with documented rollback.

**When not to use:** Erstes Setup without CI — zuerst `coding-github-actions-ci-pipeline`.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| vercel | Edge/Serverless | `vercel deploy` |
| gh | Actions deploy | audit trail |
| kubectl | K8s | `kubectl set image` gated |

## System prompt

```text
Platform deploy workflow (devops-cloud/plattform-deploy).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Default preview/staging only until user message contains PROD_APPROVE with ticket id.
Vercel: vercel deploy --prebuilt for CI artifacts; vercel promote only after approval.
GitHub Actions: gh workflow run deploy.yml -f environment=production only after approval.
Kubectl prod: never kubectl apply -f live prod without change window; prefer rollout with pinned image digest.
Pre-deploy checklist: tests green, migrations reviewed, feature flags noted.
Post-deploy: smoke URL list user provides; 5xx check via curl -sf.
Rollback command prepared before prod deploy executes: vercel rollback or kubectl rollout undo.
Record deployment id, git sha, actor, UTC time in summary.
No database schema apply in same step unless DBA approval cited.
Secrets via platform env, never CLI args.```

## Workflow

1. Target environment and SHA: `git rev-parse HEAD`.
2. Preview: `vercel deploy` or PR-Preview via CI.
3. Smoke: `curl -sf https://preview-xxx.vercel.app/api/health`.
4. Prod-approval abwarten (PROD_APPROVE).
5. `vercel deploy --prod` or `gh workflow run deploy.yml -f env=production`.
6 6 Post-deploy smoke and 5 min metrics windows.
7. Rollback-Befehl im Ticket belassen.

## Definition of done

- [ ] Preview erfolgreich vor Prod
- [ ] SHA and deployment ID documented
- [ ] Rollback getestet or beschrieben

## Security

- **high** for Prod/remote deploy.
- Kein `--force` without IC.

## Pitfalls

- Prod without Preview — klassischer Ausfall.
- Promote falsches Preview — Version mismatch.
- DB migration irreversible — Rollback app is not enough.
- kubectl latest Tag — digest pinnen.
- vercel --prod from Feature Branch — Check Branch Policy.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Preview dann Prod Vercel.
- **Input:** SHA `abc1234`, Ticket INC-99.
- **Prompt:**

```text
Deploy preview, smoke health, wait for PROD_APPROVE INC-99, then prod with rollback noted.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.vercel deploy
curl -sf https://project-abc1234.vercel.app/api/health
# after PROD_APPROVE:
vercel deploy --prod
vercel rollback  # documented
```

### Example 2 (Example data (self-written))
- **Task:** Prod via GitHub Actions.
- **Input:** workflow `deploy.yml`.
- **Prompt:**

```text
gh workflow run only after approval; watch run; no kubectl.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.gh workflow run deploy.yml -f environment=production
gh run watch
gh run view --log
```