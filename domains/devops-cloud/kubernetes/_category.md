# Kubernetes

- **Domain:** `devops-cloud`
- **Category:** `kubernetes`
- **As of:** 2026-11-23

## Summary

Inspect and (with authorization) control clusters via kubectl, specialized MCPs, or skills.

## Recommended tool stack

- Read-only MCP or kubectl zuerst
- Azure: AKS-MCP with access-level readonly
- kubectl-ai als CLI-Agent

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| kubernetes-mcp-server (containers) | MCP | https://github.com/containers/kubernetes-mcp-server | MCP server for Kubernetes and OpenShift. | See the repo (typically binary/stdio, kubeconfig). | 2,274 stars | https://github.com/containers/kubernetes-mcp-server | no (as cited) |
| AKS / Azure Kubernetes MCP | MCP | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | Official Microsoft documentation: unified tools call_kubectl and call_az, access levels readonly (default), readwrite, admin. Inherits Azure/K8s RBAC. | Via VS Code/AKS extension or mcp.json with --access-level. | Azure/mcp-kubernetes 62 stars (smaller repo; docs are the primary source). | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | no (as cited) |
| kubectl-ai | CLI agent | https://github.com/GoogleCloudPlatform/kubectl-ai | Google's AI-assisted Kubernetes assistant CLI. | See the repo README. | 7,606 stars | https://github.com/GoogleCloudPlatform/kubectl-ai | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Always first: context, namespace, read-only diagnosis. AKS docs example: Why are pods pending in this cluster?
- Only elevate access level when necessary and approved.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Wrong kubeconfig context. MCP inherits RBAC. Admin level is a production risk.

## Sources

- https://github.com/containers/kubernetes-mcp-server
- https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server
- https://github.com/GoogleCloudPlatform/kubectl-ai
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
