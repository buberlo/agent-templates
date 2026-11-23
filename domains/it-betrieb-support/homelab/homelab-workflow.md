---
id: homelab-workflow
title: "Homelab"
domain: it-betrieb-support
category: homelab
tags:
  - homelab
  - it-betrieb-support
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
    version_notes: "Nicht-k8s Stacks"
  - name: homeassistant-mcp (tevonsb)
    install: "https://github.com/tevonsb/homeassistant-mcp"
    version_notes: "Optional Dokumentation"
inputs:
  - "Inventar (Hosts, VMs, k8s ja/nein)"
  - "Änderungswunsch und Rollback"
outputs:
  - "Runbook-Abschnitt"
  - "kubectl/docker smoke nach Änderung"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Homelab dokumentieren und sicher ändern**: Proxmox/Docker/k3s — Inventar zuerst, kleine Schritte, `kubectl`/`docker` Smoke nach jedem Eingriff.

## Wann nutzen

- k3s-Dienst updaten, neuer Namespace, Backup-Strategie.
- Doku in Obsidian/HA für eigene Infrastruktur.

**Wann nicht**

- Produktions-IT ohne Change-Prozess (andere Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubectl | k3s/k8s | Workloads prüfen |
| docker compose | Stacks | Nicht jeder Dienst in k8s |
| Obsidian-Skills | Doku | Runbooks |

## System-Prompt / Instruktionen

```text
Role: homelab operator (it-betrieb-support/homelab).
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
FREIGABE HOMELAB PROD if homelab feeds family critical service else medium risk default.
Obsidian mcp only documents entities not production writes without user.
Destroy: never kubectl delete namespace all without typed confirm phrase user provides.
```

## Arbeitsablauf

1. Inventar und Backups prüfen.
2. `kubectl config current-context` und `get nodes`.
3. Änderung als kleines Manifest/Compose-Diff.
4. Backup/Commit vor Apply.
5. `kubectl apply` oder `compose up`; `rollout status`.
6. Smoke (HTTP, HA Entity, Pod Ready).
7. Runbook-Abschnitt aktualisieren.

## Qualitätskriterien / Definition of Done

- [ ] Richtiger kube-context dokumentiert
- [ ] Rollback-Schritt notiert
- [ ] Pods/Services healthy
- [ ] Keine Secrets im Git

## Sicherheit & Freigaben

- Homelab-Exposure ins Internet vermeiden oder absichern.
- Remote nur mit bewusster VPN-Lösung.

## Fallstricke

- Falscher kube-context → Work-Cluster getroffen.
- Kein Backup vor `helm upgrade`.
- Ein Node down → ganzer k3s-Stack unklar.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Deploy nginx in homelab ns
- **Input:** manifest deployment.yaml
- **Prompt:**

```text
verify context homelab apply rollout status curl smoke.
```

- **Erwartetes Ergebnis:**

```text
deploy/nginx ready | curl 200 | runbook updated
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Context prod
- **Input:** kubeconfig misclick
- **Prompt:**

```text
Apply homelab manifest now.
```

- **Erwartetes Ergebnis:**

```text
abort wrong context | show current-context
```