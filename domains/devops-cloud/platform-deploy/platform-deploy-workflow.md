---
id: platform-deploy-workflow
title: "Platform deploy"
domain: devops-cloud
category: platform-deploy
tags:
  - deploy
  - vercel
  - production
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Vercel CLI
    install: "https://vercel.com/docs/cli"
    version_notes: "vercel deploy; see deployment docs"
  - name: GitHub CLI
    install: "https://cli.github.com/manual/gh"
    version_notes: "workflow_dispatch gated"
  - name: kubectl
    install: "optional Kubernetes production"
    version_notes: "approval required"
inputs:
  - "Target environment (preview or production)"
  - "Artifact or Git SHA"
outputs:
  - "Deployment URL or revision"
  - "Rollback command documented"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Run platform deployments (Vercel, GitHub Actions, optional Kubernetes production) with **preview-first** flow, explicit production approval, and rollback prepared before promote.

## When to use

- Promoting preview to production after smoke checks.
- Documented hotfix path with rollback commands.

### When not to use

- Greenfield CI setup without pipelines — use software CI templates first.
- Database migrations without DBA review in the same change window.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Vercel CLI | Edge and serverless | https://vercel.com/docs/deployments |
| gh | Actions deploy | Audit trail via workflow runs |
| kubectl | Kubernetes | `kubectl set image` or rollout undo when gated |

## System prompt

```text
You are a platform deploy assistant for devops-cloud/platform-deploy.
You default to preview or staging until the user message contains PROD_APPROVE with a ticket id.
You use vercel deploy for previews and vercel promote or production deploy only after approval.
You run gh workflow run with production environment only after PROD_APPROVE is recorded.
You never kubectl apply live production manifests without a change window; prefer rollout with pinned image digest.
You complete pre-deploy checklist: tests green, migrations reviewed, feature flags noted.
You run post-deploy smoke URLs the user lists with curl -sf and note 5xx responses.
You prepare rollback commands before production executes: vercel rollback or kubectl rollout undo.
You record deployment id, git sha, actor, and UTC time in the summary.
You do not apply database schema changes in the same step unless DBA approval is cited.
You keep secrets in platform environment settings, never CLI arguments.
```

## Workflow

1. Confirm target environment and `git rev-parse HEAD`.
2. Preview: `vercel deploy` or CI PR preview.
3. Smoke: `curl -sf` health endpoints on preview URL.
4. Wait for PROD_APPROVE with ticket id.
5. Production deploy via Vercel or `gh workflow run`.
6. Post-deploy smoke and five-minute metrics observation window.
7. Leave rollback command in the ticket comment.

## Definition of done

- [ ] Successful preview before production
- [ ] SHA and deployment id documented
- [ ] Rollback command tested or explicitly described

## Security

- **High risk** for production and remote deploy.
- No `--force` deploy without incident commander approval.
- Production tokens never pasted in chat.

## Pitfalls

- Production without preview — classic outage pattern.
- Promoting wrong preview URL — version mismatch.
- Irreversible DB migrations — app rollback insufficient.
- kubectl `latest` tag — pin digest.
- `vercel deploy --prod` from feature branch — verify branch policy.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Vercel preview then production.
- **Input:** SHA `abc1234`, ticket INC-99.
- **Prompt:**

```text
Deploy preview, smoke health, wait for PROD_APPROVE INC-99, then prod with rollback noted.
```

- **Expected result:**

```text
vercel deploy yields preview URL; curl -sf /api/health succeeds
Production blocked until PROD_APPROVE INC-99 appears in thread
After approval: vercel deploy --prod records deployment id dpl_123
Rollback documented: vercel rollback dpl_prev listed before prod step
Summary includes sha abc1234 and UTC deploy time
```

### Example 2 (Example data (self-written))

- **Task:** Production via GitHub Actions only.
- **Input:** workflow `deploy.yml`.
- **Prompt:**

```text
gh workflow run only after approval; watch run; no kubectl.
```

- **Expected result:**

```text
gh workflow run deploy.yml -f environment=production deferred without PROD_APPROVE
After approval: gh run watch captures success log tail
gh run view shows actor and sha; no kubectl commands issued
Rollback noted as re-run previous workflow dispatch input or revert commit
```