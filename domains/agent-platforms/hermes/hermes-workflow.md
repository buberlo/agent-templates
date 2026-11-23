---
id: hermes-workflow
title: "Hermes Agent (Nous Research)"
domain: agent-platforms
category: hermes
tags:
  - hermes
  - agent-platforms
  - agentplattform
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "265550 GitHub Stars"
  - name: Nous-approved MCP-Katalog
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "linear\"
inputs:
  - "Kontext/Briefing für Hermes Agent (Nous Research)"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Skills, MCP-Katalog, Tool Gateway, Delegation an Claude Code/Codex, lokale Config.

## Wann nutzen

- Anfragen passen zur Kategorie **Hermes Agent (Nous Research)**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes Agent | Agent-Plattform | Aus Recherche 2026-11-23 |
| Nous-approved MCP-Katalog | Katalog | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Hermes Agent (Nous Research) (agent-platforms/hermes).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Blank Slate wenn man Least Privilege will. Sonst empfohlene Defaults, dann gezielt MCPs dazu.
```

## Arbeitsablauf

- Blank Slate wenn man Least Privilege will. Sonst empfohlene Defaults, dann gezielt MCPs dazu.
- Slash-Commands laut Docs: /github, /youtube-content, /excalidraw.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Sync respektiert lokale Loeschungen; Restore mit hermes skills reset --restore.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Hermes Agent (Nous Research)-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `hermes` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Hermes Agent (Nous Research). Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Hermes Agent (Nous Research)
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
