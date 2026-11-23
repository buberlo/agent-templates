---
id: plattform-deploy-workflow
title: "Platform Deploy"
domain: devops-cloud
category: plattform-deploy
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
    version_notes: "Freigabe Pflicht"
inputs:
  - "Zielumgebung (preview/prod)"
  - "Artifact oder Git SHA"
outputs:
  - "Deployment-URL oder Revision"
  - "Rollback-Befehl"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Plattform-Deployments (Vercel, Actions, K8s Prod) mit **Preview-first**, Prod nur nach expliziter Freigabe und Rollback-Plan.

## Wann nutzen

- Release Promotion preview → production.
- Hotfix-Pfad mit dokumentiertem Rollback.

**Wann nicht:** Erstes Setup ohne CI — zuerst `coding-github-actions-ci-pipeline`.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| vercel | Edge/Serverless | `vercel deploy` |
| gh | Actions deploy | audit trail |
| kubectl | K8s | `kubectl set image` gated |

## System-Prompt / Instruktionen

```text
Platform deploy workflow (devops-cloud/plattform-deploy).

Default preview/staging only until user message contains PROD_APPROVE with ticket id.
Vercel: vercel deploy --prebuilt for CI artifacts; vercel promote only after approval.
GitHub Actions: gh workflow run deploy.yml -f environment=production only after approval.
Kubectl prod: never kubectl apply -f live prod without change window; prefer rollout with pinned image digest.

Pre-deploy checklist: tests green, migrations reviewed, feature flags noted.
Post-deploy: smoke URL list user provides; 5xx check via curl -sf.
Rollback command prepared before prod deploy executes: vercel rollback or kubectl rollout undo.
Record deployment id, git sha, actor, UTC time in summary.
No database schema apply in same step unless DBA approval cited.
Secrets via platform env, never CLI args.
```

## Arbeitsablauf

1. Zielumgebung und SHA: `git rev-parse HEAD`.
2. Preview: `vercel deploy` oder PR-Preview via CI.
3. Smoke: `curl -sf https://preview-xxx.vercel.app/api/health`.
4. Prod-Freigabe abwarten (PROD_APPROVE).
5. `vercel deploy --prod` oder `gh workflow run deploy.yml -f env=production`.
6. Post-deploy smoke und 5 min Metrics-Fenster.
7. Rollback-Befehl im Ticket belassen.

## Qualitätskriterien / Definition of Done

- [ ] Preview erfolgreich vor Prod
- [ ] SHA und Deployment-ID dokumentiert
- [ ] Rollback getestet oder beschrieben

## Sicherheit & Freigaben

- **high** für Prod/remote deploy.
- Kein `--force` ohne IC.

## Fallstricke

- Prod ohne Preview — klassischer Ausfall.
- Promote falsches Preview — Version mismatch.
- DB migration irreversibel — Rollback app reicht nicht.
- kubectl latest Tag — digest pinnen.
- vercel --prod aus Feature-Branch — Branch-Policy prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Preview dann Prod Vercel.
- **Input:** SHA `abc1234`, Ticket INC-99.
- **Prompt:**

```text
Deploy preview, smoke health, wait for PROD_APPROVE INC-99, then prod with rollback noted.
```

- **Erwartetes Ergebnis:**

```bash
vercel deploy
curl -sf https://project-abc1234.vercel.app/api/health
# after PROD_APPROVE:
vercel deploy --prod
vercel rollback  # documented
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Prod via GitHub Actions.
- **Input:** workflow `deploy.yml`.
- **Prompt:**

```text
gh workflow run only after approval; watch run; no kubectl.
```

- **Erwartetes Ergebnis:**

```bash
gh workflow run deploy.yml -f environment=production
gh run watch
gh run view --log
```