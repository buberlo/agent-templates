# Cloud: Azure

- **Domain:** `devops-cloud`
- **Kategorie:** `cloud-azure`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Azure/AKS-Operationen über offizielle MCP-Server und Azure CLI.

## Empfohlener Tool-Stack

- AKS-MCP + Azure CLI ueber call_az, readonly default

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| AKS / Azure Kubernetes MCP | MCP | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | Offizielle Microsoft-Dokumentation: unified tools call_kubectl und call_az, Access-Level readonly (Default), readwrite, admin. Erbt Azure/K8s-RBAC. | Ueber VS-Code/AKS-Extension oder mcp.json mit --access-level. | Azure/mcp-kubernetes 62 Stars (kleineres Repo; Docs sind die Primaerquelle). | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | nein (so belegt) |

## Typische Workflows

- Docs listen Troubleshooting, Health, CRUD je nach Access-Level.

## Fallstricke

- --access-level admin nur bewusst. Auth-Env-Vars nicht loggen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
