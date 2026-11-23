---
id: kubernetes-mcp-focus
title: "Kubernetes: MCP/Skill-Fokus"
domain: devops-cloud
category: kubernetes
tags:
  - kubernetes
  - devops-cloud
  - mcp
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: kubernetes-mcp-server (containers)
    install: "https://github.com/containers/kubernetes-mcp-server"
    version_notes: "2274 GitHub Stars"
  - name: AKS / Azure Kubernetes MCP
    install: "https://learn.microsoft.com/en-us/azure/aks/aks-model-context-protocol-server"
    version_notes: "62 GitHub Stars"
inputs:
  - "Kontext/Briefing für Kubernetes"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Cluster inspizieren und (berechtigt) steuern über kubectl, spezialisierte MCPs oder Skills.

## Wann nutzen

- Anfragen passen zur Kategorie **Kubernetes**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| kubernetes-mcp-server (containers) | MCP | Aus Recherche 2026-11-23 |
| AKS / Azure Kubernetes MCP | MCP | Aus Recherche 2026-11-23 |
| kubectl-ai | CLI-Agent | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Kubernetes (devops-cloud/kubernetes).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Immer zuerst: Kontext, Namespace, Read-only Diagnose. AKS-Docs-Beispiel: Why are pods pending in this cluster?
```

## Arbeitsablauf

- Immer zuerst: Kontext, Namespace, Read-only Diagnose. AKS-Docs-Beispiel: Why are pods pending in this cluster?
- Access-Level nur erhoehen, wenn noetig und freigegeben.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Falscher kubeconfig-Kontext. MCP erbt RBAC. Admin-Level ist Produktionsrisiko.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Kubernetes-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `kubernetes` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Kubernetes. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Kubernetes
- **Input:** Unvollständige oder ungültige Eingabe
- **Prompt:**
```text
Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.
```
- **Erwartetes Ergebnis:**
| Feld | Status |
|------|--------|
| input | fehlt |
| Aktion | keine Ausführung |
