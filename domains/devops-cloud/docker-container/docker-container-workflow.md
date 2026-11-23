---
id: docker-container-workflow
title: "Docker und Container"
domain: devops-cloud
category: docker-container
tags:
  - docker
  - devops-cloud
  - cli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Docker CLI (agent terminal)
    install: "https://docs.docker.com/"
    version_notes: "Docker selbst nicht als MCP-Star in dieser Liste gemessen."
inputs:
  - "Kontext/Briefing für Docker und Container"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Images, Compose, Registries und Laufzeitprobleme.

## Wann nutzen

- Anfragen passen zur Kategorie **Docker und Container**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Docker CLI (agent terminal) | CLI | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Docker und Container (devops-cloud/docker-container).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Logs und docker inspect zuerst; keine Volume-Loeschungen ohne Auftrag.
```

## Arbeitsablauf

- Logs und docker inspect zuerst; keine Volume-Loeschungen ohne Auftrag.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Socket-Zugriff kann Host-weit sehr weitreichende Rechte bedeuten.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Docker und Container-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `docker-container` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Docker und Container. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Docker und Container
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
