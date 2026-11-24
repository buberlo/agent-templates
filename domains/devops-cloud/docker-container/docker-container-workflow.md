---
id: docker-container-workflow
title: "Docker Container Workflow"
domain: devops-cloud
category: docker-container
tags:
  - docker
  - container
  - buildkit
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: docker
    install: "Docker Engine / Docker Desktop"
    version_notes: "BuildKit default"
  - name: dive
    install: "https://github.com/wagoodman/dive"
    version_notes: "Image-Layer-Analyse"
inputs:
  - "Dockerfile and build context"
  - "Registry (GHCR/ECR) and Tag Policy"
outputs:
  - "Builded Image with Digest"
  - "Hardening-Notizen (non-root, SBOM optional)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Reproducible build, scan and prepare container images for registry push – without privileged defaults.

## When to use

- New Dockerfile, image too big, CVE triage after build.
- Lokaler Parity-Test vor K8s-Deploy.

**When not:** Full registry management (see plattform-deploy).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| docker buildx | Multi-arch Build | reproduzierbar |
| trivy | Scan | CVE vor Push |
| dive | Layer | Bloat finden |

## System prompt

```text
Container workflow (devops-cloud/docker-container).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Use DOCKER_BUILDKIT=1 and docker buildx build when multi-platform requested.
Never docker push without user approval and registry auth confirmed.
Prefer non-root USER in Dockerfile; no secrets in ARG/ENV literals.
Build: docker build -t <name>:<tag> -f Dockerfile . with --progress=plain for CI logs.
Scan: trivy image <name>:<tag> --severity HIGH,CRITICAL before push recommendation.
Inspect: docker inspect for User, Env, Cmd validation.
Compose: docker compose config to validate merge; docker compose up only locally unless approved.
No --privileged in run examples unless user mandates with risk callout.
Document image digest after build: docker images --digests.
Registry login via credential helper, never password in command line.```

## Workflow

1. `docker version` and BuildKit status.
2. `docker build -t app:dev -f Dockerfile .` with plain progress.
3. `docker run --rm app:dev <smoke-cmd>` lokal.
4. `trivy image app:dev` or `docker scout cves app:dev`.
5. `dive app:dev` for size problems.
6. Tag for Registry: `docker tag app:dev ghcr.io/org/app:1.2.3`.
7. `docker push` only after release and green scan report.

## Definition of done / Definition of Done

- [ ] Image runs non-root when policy is required
- [ ] No CRITICAL offen or Ausnahme dokumentiert
- [ ] Digest notiert

## Security

- Registry credentials not in Dockerfile or Chat.
- Push to Prod-Registry only with release.

## Pitfalls

- `latest`-Tag in Prod — immer versionieren.
- Cache busts through COPY . . too early — layer larger than necessary.
- amd64-only auf Apple Silicon without `--platform` — falsches Arch in CI.
- Secrets in Build-Args — in History sichtbar.
- compose override with Prod endpoints — local leak.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Build and scan API image.
- **Input:** `services/api/Dockerfile`.
- **Prompt:**

```text
Build app:1.0.0, trivy HIGH/CRITICAL, document USER directive.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.docker build -t app:1.0.0 -f services/api/Dockerfile services/api
trivy image app:1.0.0 --severity HIGH,CRITICAL
docker inspect app:1.0.0 --format '{{.Config.User}}'
# appuser
```

### Example 2 (Example data (self-written))
- **Task:** Multi-arch for linux/arm64 and amd64.
- **Input:** Release `2.0.0`.
- **Prompt:**

```text
buildx for both platforms, output type=image, no push yet.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.docker buildx build --platform linux/amd64,linux/arm64 -t app:2.0.0 --load .
```