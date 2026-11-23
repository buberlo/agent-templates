---
id: cicd-mcp-focus
title: "CI/CD: MCP/Skill focus"
domain: devops-cloud
category: cicd
tags:
  - cicd
  - mcp
  - github-actions
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Actions, PRs, Workflow-Runs"
  - name: gh
    install: "https://cli.github.com"
    version_notes: "Supplement when MCP read-only is enough"
inputs:
  - "Repo and failed workflow run ID"
  - "Skill steps for lint/test/deploy"
outputs:
  - "Skill↔MCP matrix for CI"
  - "Root-cause note with log excerpt"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Orchestrate CI/CD via **GitHub MCP** and **gh**: read failed runs, analyze logs, fixes as PR—writes only after approval.

## When to use

- Agent should read Actions logs and PR context without manual UI.
- Team documents which skill step uses which MCP tool.

**When not to use:** When only local `act` test without remote—use `coding-github-actions-ci-pipeline`.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| GitHub Official MCP | Runs, PRs | Structured API |
| gh CLI | Logs/fallback | `gh run view --log-failed` |
| Skill-CI | Flow | Repro, fix, verify |

## System prompt

```text
MCP/Skill focus for CI/CD (devops-cloud/cicd).

Map each skill step: discover workflows | fetch failed run | reproduce locally | propose yaml fix | open PR.
Use GitHub MCP for read: workflows, runs, check suites, PR files.
Use gh for large logs when MCP truncates: gh run view <id> --log-failed.

Never merge or approve PRs without user approval.
Never paste secrets from workflow logs; redact tokens and URLs with credentials.
Prefer read-only MCP tools; restrict write tools in Hermes/Cursor policy.

Skill verify: after yaml change, reference act or pending Actions run as DoD.
CircleCI/Buildkite MCP only if listed in required_tools for that session.
Document which tool answered each question (MCP vs gh).
One MCP for GitHub; do not duplicate with third-party GitHub mirrors.
```

## Workflow

1. Skill matrix: step → MCP tool / gh command.
2. MCP: workflow list and latest runs on `main` and PR branch.
3. Note failed run ID; in parallel `gh run view <id> --json conclusion,jobs`.
4. Log excerpt (error block) into ticket; redact secrets.
5. Extract local repro command from workflow.
6. Fix draft as diff; MCP/skill write only after approval.
7. After push: watch run; update matrix.

## Definition of done

- [ ] Failed run with job+step identified
- [ ] Skill↔MCP matrix complete for task
- [ ] No secrets in chat or PR description

## Security

- Never mirror pipeline secrets into chat.
- Write tools (PR merge, workflow_dispatch) only with approval.
- Limit fine-grained PAT to needed repos.

## Pitfalls

- MCP log size truncated—gh CLI as fallback.
- Two GitHub MCPs in parallel—duplicate tool schemas, slower agent.
- `workflow_dispatch` from agent without policy—accidental prod deploy.
- Fork PR context: MCP sees different permissions than maintainer branch.

## Basic examples

### Example 1 (Example data)

- **Task:** Letzten roten CI-Run auf PR #88 analysieren.
- **Input:** Repo `acme/api`, Run `20112233`.
- **Prompt:**

```text
Use GitHub MCP read tools for run 20112233; supplement with gh log-failed; no writes.
```

- **Expected result:**

```text
Matrix: step2=search_workflow_runs, step3=gh run view --log-failed
Root cause: pytest collection error in tests/integration/
```

### Example 2 (Example data)

- **Task:** Define skill for “green before merge”.
- **Input:** Branch protection verlangt `ci / test`.
- **Prompt:**

```text
Write 5-step skill mapping MCP reads and local verify; approval before gh pr merge.
```

- **Expected result:**

```text
Skill steps 1-4 read-only; step5 merge blocked until user types APPROVE
Check name documented: ci / test
```