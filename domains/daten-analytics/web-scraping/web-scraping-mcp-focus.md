---
id: web-scraping-mcp-focus
title: "Web-Scraping: MCP/Skill-Fokus"
domain: daten-analytics
category: web-scraping
tags:
  - web
  - daten-analytics
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 GitHub Stars"
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
inputs:
  - "Kontext/Briefing für Web-Scraping"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Strukturierte Extraktion von Webdaten; Firecrawl, Browser-MCPs, respektiert robots/ToS.

## Wann nutzen

- Anfragen passen zur Kategorie **Web-Scraping**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Firecrawl MCP | MCP | Aus Recherche 2026-11-23 |
| Exa MCP | MCP | Aus Recherche 2026-11-23 |
| Tavily MCP | MCP | Aus Recherche 2026-11-23 |
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Web-Scraping (daten-analytics/web-scraping).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - ToS pruefen, rate-limit, strukturiertes Schema vorgeben.
```

## Arbeitsablauf

- ToS pruefen, rate-limit, strukturiertes Schema vorgeben.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Playwright als Scraper ist token-teuer.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Web-Scraping-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `web-scraping` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Web-Scraping. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Web-Scraping
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

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Fuer Extraktionsaufgaben den Kontextverbrauch von Playwright MCP mit einem Cloud-Browser vergleichen, der Markdown zurueckgibt.
- **Input:** Typische URL-holen-und-X-extrahieren-Aufgaben laut Beitrag.
- **Prompt:**
```text
Microsoft Playwright MCP (Accessibility-Tree/Snapshots) vs. ScrapingAnt-Cloud-Browser-MCP.
```
- **Erwartetes Ergebnis:**
  Der Beitrag (Selbstpromotion von ScrapingAnt, r/mcp) behauptet typisch ca. 114.000 Tokens bei Playwright-MCP-Aufgaben gegenueber ca. 5.000-15.000 Tokens fuer Markdown/HTML/Text ohne gestreamten Accessibility-Tree. Playwright MCP wird dort selbst als besser fuer lokale UI-Tests der eigenen App beschrieben.
- **Quelle:** https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
