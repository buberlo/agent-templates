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
    install: "https://github.com/Azure/kubelogin"
    version_notes: "AKS AAD-enabled clusters"
inputs:
  - "Subscription-ID or Name"
  - "Ressourcengruppe / AKS-Cluster"
outputs:
  - "Azure CLI Protokoll"
  - "Empfehlung or ARM/Bicep-Hinweis"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Inspect Azure resources with **az** read-first; AKS diagnosis and policy checks without tacit Prod mutation.

## When to use

- AKS/RG-Inventory, NSG-Review, Subscription-Rollen.
- Preparation of Bicep modules with validated `az` findings.

**When not:** Large subscription migrations without architect sign-off.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| az | Management | account, aks, monitor |
| kubectl | AKS | nach `az aks get-credentials` |
| AKS MCP | optional | readonly call_kubectl laut MS-Docs |

## System prompt

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

## Workflow

1. `az login` Status: `az account show`.
2. Subscription setzen: `az account set --subscription "<name-or-id>"`.
3. RG/Cluster: `az group list` / `az aks list -o table`.
4. Detail: `az aks show -g <rg> -n <cluster> --query "{kubernetesVersion:KubernetesVersion,nodeCount:agentPoolProfiles[0].count}"`.
5. Optional kube: `az aks get-credentials -g <rg> -n <cluster> --overwrite-existing` after release.
6. `kubectl get nodes` read-only Diagnose.
7. Changes only as a Bicep/Runbook proposal.

## Definition of done / Definition of Done

Subscription and Tenant in Summary
- [ ] No ungenehmigten Mutations-Befehle
- [ ] AKS version and Node-Health documented

## Security

- Prod-Subscription Write: `risk_level: high`, Change-Ticket.
- Do not post Kubeconfig content in tickets.
- AKS MCP access-level `readonly` until release for readwrite.

## Pitfalls

- Falsche Subscription nach `az login` — stiller Zugriff auf falsche RG.
- `--admin` kubeconfig without RBAC — Overprivilege.
- AAD token expired in the middle of script — renewed `az aks get-credentials` required.
- Policy Deny on RG — Plan fails, not just CLI.

## Basic examples

### Example 1 (Example data)

- **Task:** AKS cluster overview.
- **Input:** RG `rg-platform`, Cluster `aks-prod-01`.
- **Prompt:**

```text
az show cluster version and node pool count; read-only.
```

- **Expected result:**

```bash
az aks show -g rg-platform -n aks-prod-01 \
  --query "{k8s:kubernetesVersion,pools:agentPoolProfiles[].{name:name,count:count}}" -o json
```

### Example 2 (Example data)

- **Task:** NSG-Regel „Any/Any“ finden.
- **Input:** NSG `nsg-web`.
- **Prompt:**

```text
List inbound rules with source * and destination port *; read-only.
```

- **Expected result:**

```bash
az network nsg rule list -g rg-platform --nsg-name nsg-web -o table
# Flag rule Allow-RDP-Internet for remediation ticket
```