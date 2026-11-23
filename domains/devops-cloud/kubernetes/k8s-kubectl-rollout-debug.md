---
id: k8s-kubectl-rollout-debug
domain: devops-cloud
title: "Deployment Rollout und Debug mit kubectl"
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
  - "Namespace und Deployment-Name"
  - "Symptom (CrashLoop, ImagePull, Pending)"
outputs:
  - "Root-Cause-Zusammenfassung"
  - "Empfohlene Remediation oder Rollback"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Fehlerhafte Kubernetes-Deployments mit read-first-Diagnose stabilisieren; Rollback nur auf Basis von Events, Logs und ReplicaSet-Historie.

## Wann nutzen

- CrashLoopBackOff, ImagePullBackOff oder fehlgeschlagener Rollout nach Release.
- Prod- oder Staging-Cluster mit gültigem RBAC.

**Wann nicht:** Cluster-Upgrades oder Node-Drain (eigenes Playbook).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubectl | Diagnose/Rollout | status, describe, logs, undo |
| stern | Logs | `stern deploy/api -n prod` |
| kube-capacity | optional | Pending wegen Ressourcen |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `kubectx` / `kubectl config use-context <cluster>` und Namespace bestätigen.
2. `kubectl -n <ns> rollout status deploy/<name> --timeout=120s`.
3. `kubectl -n <ns> get pods -l app=<label> -o wide` und failing Pod wählen.
4. `kubectl -n <ns> describe pod <pod>` und `kubectl -n <ns> logs <pod> --previous`.
5. `stern -n <ns> -l app=<label> --since 15m` bei Flapping.
6. Fix (Config/Secret/Image) oder nach Freigabe `kubectl rollout undo deploy/<name> -n <ns>`.
7. `kubectl -n <ns> rollout history deploy/<name>` für Ticket-Dokumentation.

## Qualitätskriterien / Definition of Done

- [ ] Root Cause benannt oder auf 1–2 Hypothesen eingegrenzt
- [ ] Rollout wieder `Successfully rolled out` oder Rollback dokumentiert
- [ ] Alle kubectl-Befehle im Thread/Ticket

## Sicherheit & Freigaben

- Prod-Kubeconfig nicht dauerhaft auf Laptop ohne Policy.
- Schreibende kubectl-Aktionen nur im Change-Fenster und mit Freigabe.
- Keine Secrets aus `kubectl get secret -o yaml` in Logs kopieren.

## Fallstricke

- Falscher Kontext — Classic „prod gedacht, staging getroffen“.
- `logs` ohne `--previous` bei Restart-Loop — letzter Crash fehlt.
- Rollback undo ohne ReplicaSet-Grund — gleiche kaputte Config bleibt.
- Readiness schlägt fehl wegen externer Dependency — undo hilft nicht.
- `kubectl delete pod` als Default — verschleiert StatefulSet-/PDB-Probleme.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** API-Deployment crash nach Tag `v2.3.1`.
- **Input:** Namespace `prod`, Deploy `api`.
- **Prompt:**

```text
Debug CrashLoop on api in prod. Read-only until root cause; propose rollback only if secret missing.
```

- **Erwartetes Ergebnis:**

```bash
kubectl -n prod describe deploy/api
kubectl -n prod logs deploy/api-7d9f8b-xxxxx --previous
# Error: secret "api-db" not found
kubectl -n prod rollout undo deploy/api
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** ImagePullBackOff nach Registry-Wechsel.
- **Input:** Pod Events `401 Unauthorized`.
- **Prompt:**

```text
List image pull events, suggest imagePullSecret fix path; no live patch without approval.
```

- **Erwartetes Ergebnis:**

```bash
kubectl -n staging get events --field-selector involvedObject.name=api-xxx
# Failed to pull image ... 401
kubectl -n staging get deploy api -o jsonpath='{.spec.template.spec.imagePullSecrets}'
```