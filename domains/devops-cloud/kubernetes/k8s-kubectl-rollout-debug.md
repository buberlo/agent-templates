---
id: k8s-kubectl-rollout-debug
title: "Deployment Rollout and Debug with kubectl"
domain: devops-cloud
category: kubernetes
tags:
  - kubectl
  - rollout
  - debug
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: kubectl
    install: "apt/curl: kubectl"
    version_notes: "Minor-Version passend zum Cluster"
  - name: kubectx
    install: "brew/apt: kubectx"
    version_notes: "Kontextwechsel"
  - name: stern
    install: "brew/apt: stern"
    version_notes: "Multi-Pod-Logs"
inputs:
  - "Kubeconfig (Scope begrenzt)"
  - "Namespace and Deployment Name"
  - "Symptom (CrashLoop, ImagePull, Pending)"
outputs:
  - "Root-Cause-Zusammenfassung"
  - "Empfohlene Remediation or Rollback"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Stabilise faulty Kubernetes deployments with read-first diagnosis; Rollback only based on events, logs and ReplicaSet history.

## When to use

- CrashLoopBackOff, ImagePullBackOff or fehlgeschlagener Rollout nach Release.
Prod or staging clusters with valid RBAC.

**When not to use:** Cluster-Upgrades or Node-Drain (eigenes Playbook).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| kubectl | Diagnose/Rollout | status, describe, logs, undo |
| stern | Logs | `stern deploy/api -n prod` |
| kube-capacity | optional | Pending wegen Ressourcen |

## System prompt

```text
You are a Kubernetes SRE debugging deployments (devops-cloud/kubernetes).

Always verify context first: kubectl config current-context and kubectl get ns.
Read-only phase: rollout status, describe deployment, describe failing pods, logs --previous.
Correlate events: kubectl get events --sort-by=.lastTimestamp -n <ns>.

Collect: image tag, envFrom secret refs, probe failures, OOMKilled, exit codes.
Never delete production deployments or namespaces without explicit approval.
Rollback suggestion: kubectl rollout undo deployment/<name> only after evidence and approval gate.

Document every kubectl command in order. No kubeconfig contents in chat.
If HPA or PDB blocks rollout, state constraint before recommending scale or patch.
Do not patch live prod without change ticket reference when user supplies one.
After remediation: kubectl rollout status until success; snapshot revision numbers.
```

## Workflow

1. `kubectx` / `kubectl config use-context <cluster>` and namespace confirm.
2. `kubectl -n <ns> rollout status deploy/<name> --timeout=120s`.
3. `kubectl -n <ns> get pods -l app=<label> -o wide` and failing pod.
4. `kubectl -n <ns> describe pod <pod>` and `kubectl -n <ns> logs <pod> --previous`.
5. `stern -n <ns> -l app=<label> --since 15m` bei Flapping.
6. Fix (Config/Secret/Image) or nach approval `kubectl rollout undo deploy/<name> -n <ns>`.
7. of an untouched and untouched gourmand, and of an untouched and untouched goar

## Definition of done

- [ ] Root Cause benannt or auf 1–2 Hypothesen eingegrenzt
- [ ] Rollout wieder `Successfully rolled out` or Rollback dokumentiert
- [ ] Alle kubectl-Befehle im Thread/Ticket

## Security

- Prod-Kubeconfig not permanently on laptop without policy.
- Writing kubectl actions only in the change window and with approval.
- No Secrets aus `kubectl get secret -o yaml` in Logs kopieren.

## Pitfalls

- Falscher Kontext — Classic „prod gedacht, staging getroffen“.
- `logs` without `--previous` bei Restart-Loop — letzter Crash fehlt.
- Rollback undo without ReplicaSet-Grund — gleiche kaputte Config bleibt.
- Readiness fails due to external dependency - undo does not help.
- `kubectl delete pod` als Default — verschleiert StatefulSet-/PDB-Probleme.

## Basic examples

### Example 1 (Example data)

- **Task:** API-Deployment crash nach Tag `v2.3.1`.
- **Input:** Namespace `prod`, Deploy `api`.
- **Prompt:**

```text
Debug CrashLoop on api in prod. Read-only until root cause; propose rollback only if secret missing.
```

- **Expected result:**

```bash
kubectl -n prod describe deploy/api
kubectl -n prod logs deploy/api-7d9f8b-xxxxx --previous
# Error: secret "api-db" not found
kubectl -n prod rollout undo deploy/api
```

### Example 2 (Example data)

- **Task:** ImagePullBackOff nach Registry-Wechsel.
- **Input:** Pod Events `401 Unauthorized`.
- **Prompt:**

```text
List image pull events, suggest imagePullSecret fix path; no live patch without approval.
```

- **Expected result:**

```bash
kubectl -n staging get events --field-selector involvedObject.name=api-xxx
# Failed to pull image ... 401
kubectl -n staging get deploy api -o jsonpath='{.spec.template.spec.imagePullSecrets}'
```