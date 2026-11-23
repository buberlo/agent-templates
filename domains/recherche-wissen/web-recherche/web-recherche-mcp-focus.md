---
id: web-recherche-mcp-focus
title: "Web-Recherche: MCP/Skill-Fokus"
domain: recherche-wissen
category: web-recherche
tags:
  - web
  - recherche-wissen
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
inputs:
  - "Kontext/Briefing für Web-Recherche"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Aktuelle Websuche, Scraping und Quellenprüfung (Brave, Exa, Tavily, Firecrawl).

## Wann nutzen

- Anfragen passen zur Kategorie **Web-Recherche**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave Search MCP | MCP | Aus Recherche 2026-11-23 |
| Exa MCP | MCP | Aus Recherche 2026-11-23 |
| Tavily MCP | MCP | Aus Recherche 2026-11-23 |
| Firecrawl MCP | MCP | Aus Recherche 2026-11-23 |
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Web-Recherche (recherche-wissen/web-recherche).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Zuerst Suche, dann gezielt fetchen, dann zitieren. Playwright nicht als Default-Scraper (Tokenkosten).
```

## Arbeitsablauf

- Zuerst Suche, dann gezielt fetchen, dann zitieren. Playwright nicht als Default-Scraper (Tokenkosten).

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Web-Recherche-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `web-recherche` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Web-Recherche. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Web-Recherche
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
