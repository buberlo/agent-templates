---
id: docker-container-workflow
title: "Docker und Container"
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
  - "Dockerfile und Build-Kontext"
  - "Registry (GHCR/ECR) und Tag-Policy"
outputs:
  - "Gebautes Image mit Digest"
  - "Hardening-Notizen (non-root, SBOM optional)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Container-Images reproduzierbar bauen, scannen und für Registry-Push vorbereiten — ohne privileged Defaults.

## Wann nutzen

- Neues Dockerfile, Image zu groß, CVE-Triage nach Build.
- Lokaler Parity-Test vor K8s-Deploy.

**Wann nicht:** Vollständiges Registry-Management (siehe plattform-deploy).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| docker buildx | Multi-arch Build | reproduzierbar |
| trivy | Scan | CVE vor Push |
| dive | Layer | Bloat finden |

## System-Prompt / Instruktionen

```text
Container workflow (devops-cloud/docker-container).

Use DOCKER_BUILDKIT=1 and docker buildx build when multi-platform requested.
Never docker push without user approval and registry auth confirmed.
Prefer non-root USER in Dockerfile; no secrets in ARG/ENV literals.
Build: docker build -t <name>:<tag> -f Dockerfile . with --progress=plain for CI logs.
Scan: trivy image <name>:<tag> --severity HIGH,CRITICAL before push recommendation.
Inspect: docker inspect for User, Env, Cmd validation.
Compose: docker compose config to validate merge; docker compose up only locally unless approved.
No --privileged in run examples unless user mandates with risk callout.
Document image digest after build: docker images --digests.
Registry login via credential helper, never password in command line.
```

## Arbeitsablauf

1. `docker version` und BuildKit-Status.
2. `docker build -t app:dev -f Dockerfile .` mit plain progress.
3. `docker run --rm app:dev <smoke-cmd>` lokal.
4. `trivy image app:dev` oder `docker scout cves app:dev`.
5. `dive app:dev` bei Größenproblemen.
6. Tag für Registry: `docker tag app:dev ghcr.io/org/app:1.2.3`.
7. `docker push` nur nach Freigabe und grünem Scan-Report.

## Qualitätskriterien / Definition of Done

- [ ] Image läuft non-root wenn Policy verlangt
- [ ] Keine CRITICAL offen oder Ausnahme dokumentiert
- [ ] Digest notiert

## Sicherheit & Freigaben

- Registry-Credentials nicht in Dockerfile oder Chat.
- Push zu Prod-Registry nur mit Freigabe.

## Fallstricke

- `latest`-Tag in Prod — immer versionieren.
- Cache bust durch COPY . . zu früh — Layer größer als nötig.
- amd64-only auf Apple Silicon ohne `--platform` — falsches Arch in CI.
- Secrets in Build-Args — in History sichtbar.
- compose override mit Prod-Endpoints — lokaler Leak.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** API-Image bauen und scannen.
- **Input:** `services/api/Dockerfile`.
- **Prompt:**

```text
Build app:1.0.0, trivy HIGH/CRITICAL, document USER directive.
```

- **Erwartetes Ergebnis:**

```bash
docker build -t app:1.0.0 -f services/api/Dockerfile services/api
trivy image app:1.0.0 --severity HIGH,CRITICAL
docker inspect app:1.0.0 --format '{{.Config.User}}'
# appuser
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Multi-arch für linux/arm64 und amd64.
- **Input:** Release `2.0.0`.
- **Prompt:**

```text
buildx for both platforms, output type=image, no push yet.
```

- **Erwartetes Ergebnis:**

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t app:2.0.0 --load .
```