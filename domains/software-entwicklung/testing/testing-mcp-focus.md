---
id: testing-mcp-focus
title: "Testing: MCP/Skill-Fokus"
domain: software-entwicklung
category: testing
tags:
  - testing
  - software-entwicklung
  - mcp
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "40040 GitHub Stars"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "58941 GitHub Stars"
inputs:
  - "Kontext/Briefing für Testing"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Unit-, Integrations- und E2E-Tests (inkl. Playwright) schreiben und ausführen.

## Wann nutzen

- Anfragen passen zur Kategorie **Testing**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright MCP | MCP | Aus Recherche 2026-11-23 |
| Chrome DevTools MCP | MCP | Aus Recherche 2026-11-23 |
| Hermes-Skill test-driven-development | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Testing (software-entwicklung/testing).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Tests schreiben lassen, lokal ausfuehren, erst dann Implementation verbreitern.
```

## Arbeitsablauf

- Tests schreiben lassen, lokal ausfuehren, erst dann Implementation verbreitern.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Playwright MCP streamt grosse Snapshots – fuer reine Extraktion unnoetig teuer.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Testing-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `testing` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Testing. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Testing
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
