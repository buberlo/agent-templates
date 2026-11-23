---
id: k8s-kubectl-rollout-debug
title: "Deployment Rollout und Debug mit kubectl"
category: kubernetes-infra
tags:
  - kubectl
  - rollout
  - debug
target_agents:
  - hermes
  - generic
required_tools:
  - name: kubectl
    install: "apt/curl: kubectl"
    version_notes: "1.30+; matches cluster minor"
  - name: kubectx
    install: "brew/apt: kubectx"
    version_notes: "Context switching"
inputs:
  - "Kubeconfig"
  - "Namespace"
  - "Deployment-Name"
outputs:
  - "Rollout-Status"
  - "Incident-Zusammenfassung"
risk_level: high
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Fehlerhafte Deployments diagnostizieren, Rollbacks auslösen und Stabilität wiederherstellen.

## Wann nutzen

- CrashLoop nach Release, ImagePullBackOff.
- Nicht für Cluster-Upgrades (dafür k8s-upgrade Playbook).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubectl | Core CLI | Rollout, logs, describe |
| stern | Multi-pod logs | Echtzeit |
| kube-capacity | optional | Ressourcen-Check |

## System-Prompt / Instruktionen

```text
Debug Kubernetes deployments read-first.
Collect: kubectl rollout status, describe pod, logs --previous.
Recommend rollback via kubectl rollout undo only after evidence.
Never delete production workloads without explicit approval.
```

## Arbeitsablauf

1. Context/Namespace verifizieren.
2. Events und Pod-Status.
3. Logs und Liveness-Failures korrelieren.
4. Rollback oder Config-Fix vorschlagen.
5. Postmortem-Notizen.

## Qualitätskriterien / Definition of Done

- [ ] Root Cause benannt oder eingegrenzt
- [ ] Rollout wieder healthy
- [ ] Befehle im Ticket dokumentiert

## Sicherheit & Freigaben

- Produktions-Kubeconfig nicht lokal speichern.
- Änderungen nur im Change-Fenster.

## Beispiele

**Eingabe:** `api` Deployment crash nach Tag `v2.3.1`
**Erwartetes Ergebnis:** Rollback auf `v2.3.0`, Ursache: fehlendes Secret
