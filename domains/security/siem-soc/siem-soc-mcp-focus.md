---
id: siem-soc-mcp-focus
title: "SIEM und SOC: MCP/Skill-Fokus"
domain: security
category: siem-soc
tags:
  - siem
  - security
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: datadog MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Sentry MCP
    install: "https://github.com/getsentry/sentry-mcp"
    version_notes: "973 GitHub Stars"
inputs:
  - "Kontext/Briefing für SIEM und SOC"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Alerts triagieren, Korrelation und Playbooks in SIEM/SOAR-Umgebungen (defensiv).

## Wann nutzen

- Anfragen passen zur Kategorie **SIEM und SOC**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: medium`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| datadog MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| Sentry MCP | MCP | Aus Recherche 2026-11-23 |
| grafana MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for SIEM und SOC (security/siem-soc).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Alert → Kontext sammeln → dokumentierte Mitigationsvorschlaege. Keine Offensivmassnahmen.
```

## Arbeitsablauf

- Alert → Kontext sammeln → dokumentierte Mitigationsvorschlaege. Keine Offensivmassnahmen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Write-Zugriff auf Detection-Rules ist hochsensibel.
- Nur defensive, autorisierte Nutzung.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-SIEM und SOC-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `siem-soc` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für SIEM und SOC. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in SIEM und SOC
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
