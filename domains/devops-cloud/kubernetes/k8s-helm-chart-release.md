---
id: k8s-helm-chart-release
title: "Install and upgrade helmet chart"
domain: devops-cloud
category: kubernetes
tags:
  - helm
  - kubernetes
  - release
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: helm
    install: "curl/apt: Helm v3.15+"
    version_notes: "OCI and classic repo"
  - name: kubectl
    install: "apt: kubectl"
    version_notes: "Zugriff auf Zielcluster"
  - name: helm-diff
    install: "helm plugin install https://github.com/databus23/helm-diff"
    version_notes: "Upgrade-Vorschau"
inputs:
  - "Chart (OCI or Repo-URL)"
  - "values.yaml pro Umgebung"
  - "Release name and namespace"
outputs:
  - "Installiertes or upgraded Release"
  - "Gespeichertes values-Diff"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Roll out helmet releases with pinned chart version and git-versioned values — Diff before upgrade, atomic rollback in case of error.

## When to use

- Standard-Apps (Ingress, Observability, interne Services).
- Wiederholbare Promotions dev → staging → prod.

**When not to use:** If only Kustomize policy applies without exception.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| helm | Package manager | install, upgrade, history |
| helm diff | Review | PR-taugliches Manifest-Delta |
| kubectl | Verify | Pods/Services nach Release |

## System prompt

```text
You are a Helm release engineer (devops-cloud/kubernetes).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Pin chart version explicitly; never upgrade to latest without user consent.
Workflow: helm repo add/update or OCI login as needed; helm show chart for version sanity.
Render locally: helm template <release> <chart> -f values.yaml -n <ns> > /tmp/rendered.yaml (review size).
Before upgrade: helm diff upgrade <release> <chart> -f values.yaml -n <ns>.
Use helm upgrade --install with --atomic --timeout when supported for prod-like envs.
Never put plaintext secrets in values; use External Secrets or SealedSecrets references.
Record helm history after change; rollback command documented but run only after approval.
Prod upgrades: require explicit approval message; document revision number in output.
Post-check: kubectl get pods -n <ns> -l app.kubernetes.io/instance=<release>.
Do not helm uninstall without approval and dependency check.```

## Workflow

One of `helm version` and `kubectl config current-context`.
2. Chart-Version: `helm search repo <chart> --version <x.y.z>` or `helm show chart oci://...`.
3. `helm template ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress`.
4. `helm diff upgrade ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress --version 4.11.1`.
5. Nach approval: `helm upgrade --install ingress ingress-nginx/ingress-nginx -f values.yaml -n ingress --version 4.11.1 --atomic --timeout 10m`.
... "helm history ingress -n ingress" and "kubectl -n ingress get pods".
7. `values.yaml` ins Git committen (PR), not just helmet revision secret.

## Definition of done

- [ ] Chart version and app version documented
- [ ] Diff reviewed; Release `Deployed' and Pods Ready
- [ ] values changes in the VCS

## Security

- No Secrets in values.yaml im Klartext.
- Prod upgrades only in the Runbook window and with approval.
- OCI credentials do not log into shell history.

## Pitfalls

- `helm upgrade` without `--atomic` — halb kaputter Release bleibt.
- Subchart-Versionen unpinned — Drift bei `helm dependency update`.
- Namespace fehlt — `helm install` scheitert or landet in `default`.
- CRD-Upgrade-Reihenfolge — manche Charts brauchen zwei Step-Upgrades.
- `helm diff' ignores hooks — check pre/post hooks separately.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** ingress-nginx 4.x with its own values in staging.
- **Input:** Release `ingress`, NS `ingress`, values with `controller.replicaCount: 2`.
- **Prompt:**

```text
helm diff then upgrade with atomic; pin chart version; show history after.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.helm diff upgrade ingress ingress-nginx/ingress-nginx -f values/staging.yaml -n ingress --version 4.11.1
helm upgrade --install ingress ingress-nginx/ingress-nginx -f values/staging.yaml -n ingress --version 4.11.1 --atomic
helm history ingress -n ingress
# REVISION 7 deployed
```

### Example 2 (Example data (self-written))
- **Task:** Fehlgeschlagenes Upgrade rollback.
- **Input:** REVISION 7 failed, REVISION 6 healthy.
- **Prompt:**

```text
Show failed revision pods; rollback to 6 after approval.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.helm history ingress -n ingress
helm rollback ingress 6 -n ingress
kubectl -n ingress rollout status deploy/ingress-nginx-controller
```