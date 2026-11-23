---
id: cloud-azure-workflow
title: "Cloud: Azure"
domain: devops-cloud
category: cloud-azure
tags:
  - azure
  - cloud
  - az-cli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: az
    install: "https://learn.microsoft.com/cli/azure/install-azure-cli"
    version_notes: "az login / az login --use-device-code"
  - name: kubelogin
    install: "optional für AKS"
    version_notes: "AAD-RBAC zu kubeconfig"
inputs:
  - "Subscription-ID oder Name"
  - "Ressourcengruppe / AKS-Cluster"
outputs:
  - "Azure CLI Protokoll"
  - "Empfehlung oder ARM/Bicep-Hinweis"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Azure-Ressourcen mit **az** read-first inspizieren; AKS-Diagnose und Policy-Checks ohne stillschweigende Prod-Mutation.

## Wann nutzen

- AKS/RG-Inventar, NSG-Review, Subscription-Rollen.
- Vorbereitung Bicep-Module mit validierten `az`-Befunden.

**Wann nicht:** Große Subscription-Migrationen ohne Architekten-Sign-off.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| az | Management | account, aks, monitor |
| kubectl | AKS | nach `az aks get-credentials` |
| AKS MCP | optional | readonly call_kubectl laut MS-Docs |

## System-Prompt / Instruktionen

```text
Azure cloud workflow (devops-cloud/cloud-azure).

Verify: az account show --output json; confirm subscription and user.
Read-only default: az resource list, az aks show, az network nsg rule list.
AKS credentials: az aks get-credentials only with approval; prefer --admin false.
Namespace context: kubectl config current-context after kube integration.

No az group delete, az vm deallocate, az role assignment create without approval.
Use --query JMESPath for tables; idempotent read scripts.
For RBAC: az role assignment list --scope /subscriptions/<id>.
Cost: az consumption usage list when permitted; note API limitations.
Entra/MFA issues: stop and report auth error, do not loop device login in chat.

Document region (location) on every resource summary.
Export sensitive outputs (kubeconfigs) never into chat body.
```

## Arbeitsablauf

1. `az login` Status: `az account show`.
2. Subscription setzen: `az account set --subscription "<name-or-id>"`.
3. RG/Cluster: `az group list` / `az aks list -o table`.
4. Detail: `az aks show -g <rg> -n <cluster> --query "{kubernetesVersion:KubernetesVersion,nodeCount:agentPoolProfiles[0].count}"`.
5. Optional kube: `az aks get-credentials -g <rg> -n <cluster> --overwrite-existing` nach Freigabe.
6. `kubectl get nodes` read-only Diagnose.
7. Änderungen nur als Bicep/Runbook-Vorschlag.

## Qualitätskriterien / Definition of Done

- [ ] Subscription und Tenant in Summary
- [ ] Keine ungenehmigten Mutations-Befehle
- [ ] AKS-Version und Node-Health dokumentiert

## Sicherheit & Freigaben

- Prod-Subscription Write: `risk_level: high`, Change-Ticket.
- Kubeconfig-Inhalt nicht in Tickets posten.
- AKS MCP access-level `readonly` bis Freigabe für readwrite.

## Fallstricke

- Falsche Subscription nach `az login` — stiller Zugriff auf falsche RG.
- `--admin` kubeconfig ohne RBAC — Überprivileg.
- AAD-Token abgelaufen mitten in Skript — erneutes `az aks get-credentials` nötig.
- Policy Deny auf RG — Plan scheitert, nicht nur CLI.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** AKS-Cluster-Überblick.
- **Input:** RG `rg-platform`, Cluster `aks-prod-01`.
- **Prompt:**

```text
az show cluster version and node pool count; read-only.
```

- **Erwartetes Ergebnis:**

```bash
az aks show -g rg-platform -n aks-prod-01 \
  --query "{k8s:kubernetesVersion,pools:agentPoolProfiles[].{name:name,count:count}}" -o json
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** NSG-Regel „Any/Any“ finden.
- **Input:** NSG `nsg-web`.
- **Prompt:**

```text
List inbound rules with source * and destination port *; read-only.
```

- **Erwartetes Ergebnis:**

```bash
az network nsg rule list -g rg-platform --nsg-name nsg-web -o table
# Flag rule Allow-RDP-Internet for remediation ticket
```