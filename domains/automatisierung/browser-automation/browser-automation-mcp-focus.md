---
id: browser-automation-mcp-focus
title: "Browser-Automation: MCP/Skill-Fokus"
domain: automatisierung
category: browser-automation
tags:
  - browser
  - automatisierung
  - mcp
  - playwright
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "npx @playwright/mcp@latest"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Nur bei Debug nach Fehlschlag"
inputs:
  - "Welche MCPs sind im Client aktiv (include/exclude)"
  - "Aufgabenklasse: interact | debug | read-only"
outputs:
  - "MCP-Auswahl und Begründung"
  - "Minimales Tool-Set für die Session"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**MCP- und Skill-Routing** für Browser-Aufgaben: Playwright vs. DevTools vs. Lesemcp — Tokenbudget und Tool-Policy vor der ersten Navigation festlegen.

## Wann nutzen

- Agent startet mit vielen MCPs → Browser-Tools gezielt reduzieren.
- Nutzer fragt „welchen Browser-MCP?“ vor einer größeren Session.

**Wann nicht**

- Wenn Aufgabe bereits als Playwright-CLI-Testspec beschrieben ist (direkt `browser-automation-workflow`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Playwright MCP | Interaktion | UI der eigenen App |
| Chrome DevTools MCP | Diagnose | Netzwerk/Console |
| ClawHub Playwright Skill | Wrapper | Progressive disclosure |

## System-Prompt / Instruktionen

```text
Role: browser MCP router (automatisierung/browser-automation-mcp-focus).
Mission: Pick minimal MCP/skill set before any navigation; document token risk.

Decision tree:
read public page text only → Firecrawl/Brave/Exa OFF Playwright unless DOM interaction required.
own app E2E click/fill → Playwright MCP OR Playwright CLI in terminal—not both unless user asks.
failed step debug → add Chrome DevTools MCP temporarily; remove after root cause.

Hermes: set mcp include list to playwright + optional devtools; exclude unused catalog entries.
OpenClaw: tool policy deny browser skills until user confirms task class interact.
Grok: plugin OAuth handles auth—no tokens in prompts.

Playwright MCP install check: npx @playwright/mcp@latest --help in user env if unsure.
Skills vs MCP: skill gives workflow text; MCP gives tools—enable skill only if team uses OpenClaw bundle.

Measure overhead: warn if >3 browser-related MCPs enabled citing 67k token anecdote—user may trim.
Snapshot strategy: ask user to limit snapshot depth or switch to CLI for batch asserts.
Handoff: scraping tables → id web-playwright-research-scrape in daten-analytics.
Handoff: CI pipeline → software-entwicklung/testing-workflow.

Never recommend Browserbase for purely local localhost unless user lacks local chrome.
Session end: suggest disable browser MCPs in client config to restore prompt budget.
Log recommendation table: task, chosen tool, rejected tools, reason one line each.
```

## Arbeitsablauf

1. Aufgabenklasse klassifizieren (interact / debug / read).
2. Aktive MCP-Liste vom Nutzer oder Client-Config erfassen.
3. Entscheidungsbaum anwenden; Überkill-Tools abwählen.
4. Install-Zeile und include/exclude für Hermes/OpenClaw notieren.
5. Bei interact → Verweis auf `browser-automation-workflow` mit konkretem ersten Schritt.
6. Nach Session: Empfehlung zum Deaktivieren schwerer MCPs.

## Qualitätskriterien / Definition of Done

- [ ] Begründete Tool-Auswahl (max. 2 Browser-MCPs gleichzeitig)
- [ ] Read-only nicht über Playwright-Snapshots gelöst ohne Warnung
- [ ] Handoff-IDs bei Scraping/CI genannt

## Sicherheit & Freigaben

- OAuth und Session-States nicht in Skill-Dateien duplizieren.
- Nur freigegebene MCPs aktivieren.

## Fallstricke

- Alle Browser-MCPs parallel → Prompt voll vor Aufgabe.
- DevTools dauerhaft an → noch mehr Kontextlast.
- Skill ohne verifizierten Owner (ClawHub Warnung).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Staging-Checkout klicken
- **Input:** interact, Hermes
- **Prompt:**

```text
Enable Playwright MCP only; exclude Firecrawl. First step navigate staging URL.
```

- **Erwartetes Ergebnis:**

```text
routing: playwright on | firecrawl off | next: open browser-automation-workflow
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Blog-Artikel nur zusammenfassen
- **Input:** read-only
- **Prompt:**

```text
Reject Playwright MCP; suggest search or scrape template.
```

- **Erwartetes Ergebnis:**

```text
no browser MCP | handoff daten-analytics/web-scraping or brave search
```