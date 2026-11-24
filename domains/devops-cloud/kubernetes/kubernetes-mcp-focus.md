---
id: kubernetes-mcp-focus
title: "Kubernetes: MCP/Skill focus"
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
  - "Cluster context and namespace"
  - "Skill with diagnosis/mitigate steps"
outputs:
  - "Skill↔MCP-Matrix"
  - "Diagnosebericht"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Combine Kubernetes via **MCP** and **kubectl**: Skill defines access-level, approvaln and when CLI instead of MCP.

## When to use

Cursor/Hermes with kubernetes-mcp-server or AKS MCP.
- Team-Doku: welcher Skill-Schritt ruft `call_kubectl` vs. natives `kubectl logs`.

**When not to use:** If only Helm/kubectl releases — see `k8s-*` templates.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| kubernetes-mcp-server | MCP | Pod/Deploy describe |
| kubectl | supplement | logs, port-forward |
| kubectl-ai | optional | natural language→kubectl |

## System prompt

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

## Workflow

Check kubecontext: `kubectl config current-context`.
2. Skill-Matrix anlegen (Diagnose/Mitigate/Verify).
3. MCP: Namespaces, Deployments, Events lesen.
4. Logs per kubectl if MCP truncated.
5. Mitigation-Vorschlag; Gate bis APPROVE.
6. Nach approval: rollout undo or apply patch — kanal dokumentieren.
7. Verify: rollout status + MCP pod ready.

## Definition of done

- [ ] access-level in Skill and MCP-Config
- [ ] MCP vs. CLI je Schritt markiert
- [ ] Kein Admin-MCP in Prod without Ausnahmeprotokoll

## Security

- high risk auf Prod-Clustern.
- Kubeconfig not in chat; MCP about safe transport.

## Pitfalls

- Falscher Context trotz MCP — menschliche Verifikation Pflicht.
- Admin access-level Default — Produktionsrisiko.
- MCP without --previous logs — Crash-Loops unsichtbar.
- Zwei K8s-MCPs doppelte Tools.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Readonly Skill for Pending Pods.
- **Input:** Cluster staging, ns `app`.
- **Prompt:**

```text
Matrix MCP describe + kubectl events; no writes.
```

- **Expected result:**

```text
MCP: list pods; describe pod/payment-xxx
CLI: kubectl get events -n app --sort-by=.lastTimestamp
Cause: Insufficient cpu
```

### Example 2 (Example data (self-written))
and**Excalation to APPROVE for rollout undo.
- **Input:** Deploy `payment` broken.
- **Prompt:**

```text
Skill step 5 after APPROVE: kubectl rollout undo; MCP verify pods ready.
```

- **Expected result:**

```bash
kubectl -n app rollout undo deploy/payment
kubectl -n app rollout status deploy/payment
```