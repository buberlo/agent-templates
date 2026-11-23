# Kubernetes

- **Domain:** `devops-cloud`
- **Category:** `kubernetes`
- **As of:** 2026-11-23

## Summary

Cluster inspection and (authorized) control via kubectl, specialized MCPs or skills.

## Recommended tool stack

- Read-only MCP or kubectl zuerst
Azure: AKS-MCP with access-level readonly
- kubectl-ai als CLI-Agent

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| kubernetes-mcp-server (containers) | MCP | https://github.com/containers/kubernetes-mcp-server | MCP server for Kubernetes and OpenShift. | See repo (typically binary/stdio, kubeconfig). | 2.274 Stars | https://github.com/containers/kubernetes-mcp-server | no (as documented) |
| AKS / Azure Kubernetes MCP | MCP | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | Official Microsoft docs: unified tools call_kubectl and call_az; access levels readonly (default), readwrite, admin. Inherits Azure/K8s RBAC. | Via VS Code/AKS extension or mcp.json with --access-level. | Azure/mcp-kubernetes 62 Stars (smaller repo; docs are primary source). | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | no (as documented) |
| kubectl-ai | CLI agent | https://github.com/GoogleCloudPlatform/kubectl-ai | Google AI-assisted Kubernetes assistant CLI. | See repo README. | 7.606 Stars | https://github.com/GoogleCloudPlatform/kubectl-ai | no (as documented) |

## Typical workflows

- Always first: context, namespace, read-only diagnosis. AKS-Docs example: Why are pods pending in this cluster?
- only increase-level access if necessary and released.

## Pitfalls

- Falscher kubeconfig-Kontext. MCP erbt RBAC. Admin-Level ist Produktionsrisiko.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/containers/kubernetes-mcp-server
- https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server
- https://github.com/GoogleCloudPlatform/kubectl-ai
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
