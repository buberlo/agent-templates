---
id: telefon-voice-agents-workflow
title: "Telefon und Voice-Agents"
domain: kommunikation
category: telefon-voice-agents
tags:
  - telefon
  - kommunikation
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: twilio-docs MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: ClawHub „Agent Phone Call“ (mrsz)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "72.476 Downloads, 8 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für Telefon und Voice-Agents"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Outbound/Inbound-Calls über Voice-Agent-Plattformen, Transkripte und Nachbearbeitung.

## Wann nutzen

- Anfragen passen zur Kategorie **Telefon und Voice-Agents**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| twilio-docs MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |
| ClawHub „Agent Phone Call“ (mrsz) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Telefon und Voice-Agents (kommunikation/telefon-voice-agents).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Anrufinhalte und Einwilligung klaeren; Aufzeichnungsregeln beachten.
```

## Arbeitsablauf

- Anrufinhalte und Einwilligung klaeren; Aufzeichnungsregeln beachten.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Warnmarkierte ClawHub-Skills nicht ungeprueft laden.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach 

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Telefon und Voice-Agents-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `telefon-voice-agents` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Telefon und Voice-Agents. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Telefon und Voice-Agents
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
