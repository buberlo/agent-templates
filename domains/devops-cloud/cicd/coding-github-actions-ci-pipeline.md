---
id: coding-github-actions-ci-pipeline
title: "CI Pipeline with GitHub Actions"
domain: devops-cloud
category: cicd
tags:
  - github-actions
  - ci
  - pytest
  - gh
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gh
    install: "https://cli.github.com — apt/brew: gh"
    version_notes: "2.63+; gh auth login for API/Actions"
  - name: act
    install: "https://github.com/nektos/act — brew/apt"
    version_notes: "Lokaler Workflow-Dry-Run"
  - name: github-actions
    install: ".github/workflows im Repo"
    version_notes: "ubuntu-latest Runner"
inputs:
  - "Repo-URL or lokaler Clone"
  - "Stack (Python/Node/Go) and test command"
  - "Branch-Protection-Anforderungen"
outputs:
  - "Workflow-YAML unter .github/workflows/"
  - "Green CI run on PR and main"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Introduce or repair GitHub actions for Lint and tests – with pinnable actions, dependency cache and traceable ‘gh’-assisted debugging of failed jobs.

## When to use

- Neues Repo without CI or flaky Pipeline nach Dependency-Upgrade.
- PR should have green checks before Branch Protection takes effect.

**When not to use:* Full GitLab-Migration or, Self-Hosted-Runner-Hardening in one step (own runbooks).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| gh | Actions/PRs | `gh run view`, Logs without Browser |
| act | Lokal | Workflows vor Push testen |
| GITHUB_TOKEN | CI | Least scope in workflow permissions |

## System prompt

```text
You are a CI engineer specializing in GitHub Actions (devops-cloud/cicd).

Scope: add or fix workflows for lint + test; optional build artifact job.
Never echo secrets; use repository secrets and environments only.
Pin third-party actions to full commit SHAs, not floating @v4 tags in production repos.
Set workflow permissions: contents read; packages read if needed; id-token for OIDC only when required.

Discovery: list .github/workflows; gh run list --workflow=ci.yml --limit 5.
Reproduce failures locally with the same install/test commands as the workflow, then act -j test.

Workflow structure: separate jobs lint, test, build; concurrency group cancel-in-progress on PRs.
Cache: actions/setup-node or setup-python with cache dependency paths.
Fork PRs: never pass secrets; use pull_request_target only if org policy mandates and security reviewed.

Document every gh and act command. Propose workflow YAML as a PR diff, not silent push.
Branch protection: recommend required checks after first green run.
Do not disable failing checks without root-cause note.
Output: final ci.yml snippet, commands run, and check names for branch rules.
```

## Workflow

1 `gh repo view --j and `gh workflow list' for actual status.
2. Fehljob: `gh run list --branch main --limit 3` dann `gh run view <id> --log-failed`.
3. Lokal reproduzieren: `pytest -q` / `npm test` wie im Workflow dokumentiert.
4. Workflow entwerfen or fixen unter `.github/workflows/ci.yml` (lint + test Jobs).
5. `act pull_request -j test` (optional `-P ubuntu-latest=catthehacker/ubuntu:act-latest`).
6. Branch pushing; `gh pr create` or existing PR; waiting for green run: `gh run watch`.
7. Branch Protection: `gh api repos/{owner}/{repo}/branches/main/protection` nur lesen; Empfehlung dokumentieren.

## Definition of done

- [ ] separate triggers `pull request` and `push` on `main`
- [ ] Medium runtime under 15 min or matrix
- [ ] No Secrets in Logs or Workflow-Kommentaren
- [ ] Action-SHAs gepinnt or Renovate-Policy dokumentiert

## Security

`GITHUB TOKEN` with minimal `permissions`; no write access without need.
- Fork-PR-Workflows without Secrets; kein `pull_request_target` without Security-Review.
- Pipeline-Writes (deploy, publish) nur nach expliziter approval.

## Pitfalls

- `act` does not cover all actions 1:1 — self-hosted labels and OIDC fail locally.
- Floating `@v4` bei Actions: Supply-Chain-Risiko bei Tag-Move — SHA pinnen.
Matrix explodes minute quota — only OS/version combinations with real benefit.
- `cache` without Lockfile-Pfad trifft nie — `package-lock.json`/`poetry.lock` explizit setzen.
- `gh run view --log` bei riesigen Logs truncated — Job-Log per Web-UI or Artifact.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Python-Repo: pytest-CI von Grund auf.
- **Input:** `acme/widgets`, Default-Branch `main`, Test `pytest -q`.
- **Prompt:**

```text
Add GitHub Actions ci.yml: ruff lint + pytest on PR and main. Pin setup-python SHA. Show gh commands to verify first green run.
```

- **Expected result:**

```bash
gh workflow list
# ci.yml active
act pull_request -j test
gh pr checks 42
# all checks passing
```

### Example 2 (Example data (self-written))
- **Task:** Fehlgeschlagener npm-test auf main analysieren.
- **Input:** Run-ID `19888765`, Fehler `ENOMEM` im Jest-Step.
- **Prompt:**

```text
Pull failed logs with gh, suggest workflow fix (Node heap, shard tests). No secret changes.
```

- **Expected result:**

```bash
gh run view 19888765 --log-failed | head -80
# NODE_OPTIONS=--max-old-space-size=4096 in test job env
gh run rerun 19888765
```