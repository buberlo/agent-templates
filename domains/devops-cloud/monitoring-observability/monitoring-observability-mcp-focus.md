---
id: monitoring-observability-mcp-focus
title: "Monitoring und Observability: MCP/Skill-Fokus"
domain: devops-cloud
category: monitoring-observability
tags:
  - monitoring
  - devops-cloud
  - mcp
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "973 GitHub Stars"
  - name: grafana MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/grafana"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Monitoring und Observability"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Metrics, Traces, Dashboards in Grafana, Datadog, Sentry, Prometheus.

## Wann nutzen

- Anfragen passen zur Kategorie **Monitoring und Observability**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Sentry MCP | MCP | Aus Recherche 2026-11-23 |
| grafana MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| datadog MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| betterstack MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Monitoring und Observability (devops-cloud/monitoring-observability).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Community-Posts koppeln Coding-Agenten mit Sentry plus Browser-MCP, um Prod-Fehler zu sehen.
```

## Arbeitsablauf

- Community-Posts koppeln Coding-Agenten mit Sentry plus Browser-MCP, um Prod-Fehler zu sehen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Monitoring und Observability-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `monitoring-observability` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Monitoring und Observability. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Monitoring und Observability
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
