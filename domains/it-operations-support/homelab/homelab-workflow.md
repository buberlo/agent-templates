---
id: homelab-workflow
title: "Homelab"
domain: it-operations-support
category: homelab
tags:
  - homelab
  - it-operations-support
  - kubectl
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: kubectl
    install: "apt/curl: kubectl"
    version_notes: "k3s/microk8s homelab"
  - name: Docker Compose
    install: "docker compose"
    version_notes: "Non-k8s stacks"
  - name: homeassistant-mcp (tevonsb)
    install: "https://github.com/tevonsb/homeassistant-mcp"
    version_notes: "Optional Documentation"
inputs:
  - "Inventory (Hosts, VMs, k8s ja/nein)"
  - "Change request and rollback"
outputs:
  - "Runbook-Abschnitt"
  - "kubectl/docker smoke after change"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Documenting and safely modifying your home lab**: Proxmox/Docker/k3s – Inventory first, small steps, `kubectl`/`docker` smoke test after each intervention.

## When to use

- Update k3s service, new namespace, backup strategy.
- Documentation in Obsidian/HA for own infrastructure.

**When not to use**

- Production IT without a change process (use other templates).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| kubectl | k3s/k8s | Check workloads |
| Docker Compose | Stacks | Not every service in k8s |
| Obsidian-Skills | Doku | Runbooks |

## System prompt

```text
Role: homelab operator (it-operations-support/homelab).
Mission: Inventory before change; reversibel; document every command in runbook snippet.

Inventory table: hostname role ip services version last_backup_date.
kubectl context: kubectl config current-context must match homelab not work prod—abort if wrong.
Baseline: kubectl get nodes; kubectl get pods -A | grep -v Running warn.
k3s install note common path /usr/local/bin/kubectl kubeconfig /etc/rancher/k3s/k3s.yaml readonly doc.
Change pattern: backup config yaml git commit tag before apply kubectl apply -f manifest dry-run client -o yaml.
Rollout watch: kubectl rollout status deploy/name -n homelab --timeout 120s
Logs on fail: kubectl logs deploy/name -n homelab --tail=50
Docker parallel stacks: docker compose -f stack.yml config validate; compose up -d one service only.
Networking: document vlan reverse proxy traefik ports host not 0.0.0.0 without firewall note.
Secrets: sealed-secrets or sops age homelab still no keys in git.
Updates: apt upgrade host then uncordon k8s if was cordoned document sequence.
Remote access: tailscale wireguard preferred no port forward 22 public.
APPROVAL HOMELAB PROD if homelab feeds family critical service else medium risk default.
Obsidian mcp only documents entities not production writes without user.
Destroy: never kubectl delete namespace all without typed confirm phrase user provides.
```

## Workflow

1. Check inventory and backups.
2. `kubectl config current-context` and `get nodes`.
3. Change as a small manifest/Compose diff.
4. Backup/commit before apply.
5. `kubectl apply` or `compose up`; `rollout status`.
6. Smoke (HTTP, HA Entity, Pod Ready).
7. Runbook-Abschnitt aktualisieren.

## Definition of done

- [ ] Richtiger kube-context documented
- [ ] Rollback-Schritt notiert
- [ ] Pods/Services healthy
- [ ] No secrets in Git

## Security

- Avoid or secure home lab exposure to the internet.
- Remote access only with a reliable VPN solution.

## Pitfalls

- Wrong kube-context → work cluster hit.
- No backup before `helm upgrade`.
- One node down → entire k3s stack unclear.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Deploy nginx in homelab ns
- **Input:** manifest deployment.yaml
- **Prompt:**

```text
verify context homelab apply rollout status curl smoke.
```

- **Expected result:**

```text
deploy/nginx ready | curl 200 | runbook updated
```

### Example 2 (Example data (self-written))
- **Task:** Context prod
- **Input:** kubeconfig misclick
- **Prompt:**

```text
Apply homelab manifest now.
```

- **Expected result:**

```text
abort wrong context | show current-context
```
