# Cloud: Azure

- **Domain:** `devops-cloud`
- **Category:** `cloud-azure`
- **As of:** 2026-11-23

## Summary

Azure/KS operations through all-emplodie of the official MCP servers and Azure CLI.

## Recommended tool stack

- AKS-MCP + Azure CLI over call_az, readonly default

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| AKS / Azure Kubernetes MCP | MCP | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | Official Microsoft docs: unified tools call_kubectl and call_az; access levels readonly (default), readwrite, admin. Inherits Azure/K8s RBAC. | Via VS Code/AKS extension or mcp.json with --access-level. | Azure/mcp-kubernetes 62 Stars (smaller repo; docs are primary source). | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | no (as documented) |

## Typical workflows

- Docs listen Troubleshooting, Health, CRUD je nach Access-Level.

## Pitfalls

- Access--allows-levels. Auth- by enlarges.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
