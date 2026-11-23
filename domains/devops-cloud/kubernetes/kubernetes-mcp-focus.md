---
id: kubernetes-mcp-focus
title: "Kubernetes: MCP/Skill-Fokus"
domain: devops-cloud
category: kubernetes
tags:
  - kubernetes
  - mcp
  - kubectl
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: kubernetes-mcp-server
    install: "https://github.com/containers/kubernetes-mcp-server"
    version_notes: "kubeconfig readonly default"
  - name: kubectl
    install: "Fallback bei MCP-Limits"
    version_notes: "Gleiche RBAC"
  - name: AKS Kubernetes MCP
    install: "Microsoft AKS MCP docs"
    version_notes: "--access-level readonly"
inputs:
  - "Cluster-Kontext und Namespace"
  - "Skill mit diagnose/mitigate Schritten"
outputs:
  - "Skill↔MCP-Matrix"
  - "Diagnosebericht"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Kubernetes über **MCP** und **kubectl** kombinieren: Skill definiert access-level, Freigaben und wann CLI statt MCP.

## Wann nutzen

- Cursor/Hermes mit kubernetes-mcp-server oder AKS MCP.
- Team-Doku: welcher Skill-Schritt ruft `call_kubectl` vs. natives `kubectl logs`.

**Wann nicht:** Wenn nur Helm/kubectl-Releases — siehe `k8s-*` Templates.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubernetes-mcp-server | MCP | Pod/Deploy describe |
| kubectl | Ergänzung | logs, port-forward |
| kubectl-ai | optional | Natürliche Sprache→kubectl |

## System-Prompt / Instruktionen

```text
Kubernetes MCP/Skill focus (devops-cloud/kubernetes).

Skill must state: default access readonly; escalate to readwrite only with approval keyword.
Map steps: verify context | list workloads | describe failing pod | fetch logs | propose patch/rollback.
MCP inherits RBAC; if Forbidden, report exact API error, do not switch contexts silently.
One cluster per session unless user lists multiple; kubectx switch documented.
Prefer MCP for get/describe; use kubectl for logs --previous and stern-like multi-pod if MCP lacks it.
AKS MCP: pass --access-level readonly in mcp.json; document in matrix.

No delete collection, no cluster-admin MCP in prod skill templates.
Helm changes not through MCP unless helm-mcp explicitly required_tools.
After mitigation skill step: kubectl rollout status as verify (CLI).
Document whether each command ran via MCP or shell.
```

## Arbeitsablauf

1. kubecontext prüfen: `kubectl config current-context`.
2. Skill-Matrix anlegen (Diagnose/Mitigate/Verify).
3. MCP: Namespaces, Deployments, Events lesen.
4. Logs per kubectl wenn MCP truncated.
5. Mitigation-Vorschlag; Gate bis APPROVE.
6. Nach Freigabe: rollout undo oder apply patch — kanal dokumentieren.
7. Verify: rollout status + MCP pod ready.

## Qualitätskriterien / Definition of Done

- [ ] access-level in Skill und MCP-Config übereinstimmend
- [ ] MCP vs. CLI je Schritt markiert
- [ ] Kein Admin-MCP in Prod ohne Ausnahmeprotokoll

## Sicherheit & Freigaben

- high risk auf Prod-Clustern.
- Kubeconfig nicht in Chat; MCP über sicheren Transport.

## Fallstricke

- Falscher Context trotz MCP — menschliche Verifikation Pflicht.
- Admin access-level Default — Produktionsrisiko.
- MCP ohne --previous logs — Crash-Loops unsichtbar.
- Zwei K8s-MCPs doppelte Tools.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Readonly Skill für Pending Pods.
- **Input:** Cluster staging, ns `app`.
- **Prompt:**

```text
Matrix MCP describe + kubectl events; no writes.
```

- **Erwartetes Ergebnis:**

```text
MCP: list pods; describe pod/payment-xxx
CLI: kubectl get events -n app --sort-by=.lastTimestamp
Cause: Insufficient cpu
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Escalation nach APPROVE für rollout undo.
- **Input:** Deploy `payment` broken.
- **Prompt:**

```text
Skill step 5 after APPROVE: kubectl rollout undo; MCP verify pods ready.
```

- **Erwartetes Ergebnis:**

```bash
kubectl -n app rollout undo deploy/payment
kubectl -n app rollout status deploy/payment
```