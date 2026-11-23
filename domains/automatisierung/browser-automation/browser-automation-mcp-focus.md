---
id: browser-automation-mcp-focus
title: "Browser-Automation: MCP/Skill-Fokus"
domain: automatisierung
category: browser-automation
tags:
  - browser
  - automatisierung
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "40040 GitHub Stars"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "58941 GitHub Stars"
inputs:
  - "Kontext/Briefing für Browser-Automation"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Playwright MCP, Chrome DevTools MCP, Cloud-Browser; Tokenkosten beachten.

## Wann nutzen

- Anfragen passen zur Kategorie **Browser-Automation**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |
| Chrome DevTools MCP | MCP | Aus Recherche 2026-11-23 |
| Firecrawl MCP | MCP | Aus Recherche 2026-11-23 |
| Browserbase MCP | MCP | Aus Recherche 2026-11-23 |
| ClawHub „Playwright MCP“ (spiceman161) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Browser-Automation (automatisierung/browser-automation).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - UI der eigenen App: Playwright oder DevTools. Offene Webseite nur lesen: Search/Firecrawl. Login-Sessions klar trennen
```

## Arbeitsablauf

- UI der eigenen App: Playwright oder DevTools. Offene Webseite nur lesen: Search/Firecrawl. Login-Sessions klar trennen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Snapshot-Schwemme. Community-Alternativen werben mit kleineren Payloads – unabhaengig benchmerken.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur n

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Browser-Automation-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `browser-automation` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Browser-Automation. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Browser-Automation
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
