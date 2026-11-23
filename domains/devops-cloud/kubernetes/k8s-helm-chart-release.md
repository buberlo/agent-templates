---
id: k8s-helm-chart-release
domain: devops-cloud
title: "Helm Chart installieren und upgraden"
category: kubernetes
tags:
  - helm
  - kubernetes
  - release
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: helm
    install: "curl/apt: helm"
    version_notes: "v3.15+"
  - name: kubectl
    install: "apt: kubectl"
    version_notes: "Zugriff auf Zielcluster"
inputs:
  - "Chart (OCI/repo)"
  - "values.yaml"
  - "Release-Name"
outputs:
  - "Installiertes Release"
  - "values diff"
risk_level: high
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Anwendungen paketiert über Helm mit versionierten Values ausrollen.

## Wann nutzen

- Standard-Apps (Ingress, Prometheus, App).
- Nicht wenn reine Kustomize-Politik gilt ohne Ausnahme.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Helm | Package manager | Templating + Release |
| helm diff | Upgrade preview | PR-tauglich |
| chartmuseum/OCI | Registry | Version pinning |

## System-Prompt / Instruktionen

```text
Helm install/upgrade with helm diff before apply.
Pin chart version; values in git per environment.
Use --atomic on upgrades when supported.
Record revision: helm history after change.
```

## Arbeitsablauf

1. Chart-Version und App-Version prüfen.
2. `helm template` lokal rendern.
3. `helm diff upgrade`.
4. Upgrade mit Freigabe.
5. Smoke-Test und History archivieren.

## Qualitätskriterien / Definition of Done

- [ ] Diff reviewed
- [ ] Release HEALTHY
- [ ] values.yaml committed

## Sicherheit & Freigaben

- Keine Secrets in values; External Secrets Operator.
- Prod-Upgrades im Runbook.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Chart `ingress-nginx` 4.x, eigene values
**Erwartetes Ergebnis:** Release `ingress` Rev. 7 deployed
