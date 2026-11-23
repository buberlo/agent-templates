# Kubernetes

- **Domain:** `devops-cloud`
- **Kategorie:** `kubernetes`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Cluster inspizieren und (berechtigt) steuern über kubectl, spezialisierte MCPs oder Skills.

## Empfohlener Tool-Stack

- Read-only MCP oder kubectl zuerst
- Azure: AKS-MCP mit access-level readonly
- kubectl-ai als CLI-Agent

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| kubernetes-mcp-server (containers) | MCP | https://github.com/containers/kubernetes-mcp-server | MCP-Server fuer Kubernetes und OpenShift. | Siehe Repo (typisch Binary/stdio, kubeconfig). | 2.274 Stars | https://github.com/containers/kubernetes-mcp-server | nein (so belegt) |
| AKS / Azure Kubernetes MCP | MCP | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | Offizielle Microsoft-Dokumentation: unified tools call_kubectl und call_az, Access-Level readonly (Default), readwrite, admin. Erbt Azure/K8s-RBAC. | Ueber VS-Code/AKS-Extension oder mcp.json mit --access-level. | Azure/mcp-kubernetes 62 Stars (kleineres Repo; Docs sind die Primaerquelle). | https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server | nein (so belegt) |
| kubectl-ai | CLI-Agent | https://github.com/GoogleCloudPlatform/kubectl-ai | KI-gestuetzte Kubernetes-Assistenten-CLI von Google. | Siehe Repo-README. | 7.606 Stars | https://github.com/GoogleCloudPlatform/kubectl-ai | nein (so belegt) |

## Typische Workflows

- Immer zuerst: Kontext, Namespace, Read-only Diagnose. AKS-Docs-Beispiel: Why are pods pending in this cluster?
- Access-Level nur erhoehen, wenn noetig und freigegeben.

## Fallstricke

- Falscher kubeconfig-Kontext. MCP erbt RBAC. Admin-Level ist Produktionsrisiko.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/containers/kubernetes-mcp-server
- https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server
- https://github.com/GoogleCloudPlatform/kubectl-ai
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
