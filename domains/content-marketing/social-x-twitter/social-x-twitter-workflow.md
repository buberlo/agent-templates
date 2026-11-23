---
id: social-x-twitter-workflow
title: "Social: X / Twitter"
domain: content-marketing
category: social-x-twitter
tags:
  - social
  - content-marketing
  - skillcli
target_agents:
  - grokbot
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes-Skill xurl
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-Katalog."
  - name: ClawHub „Humanizer“ (biostartechnology)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "105.439 Downloads, 601 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für Social: X / Twitter"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Recherche, Entwürfe, Threads und Veröffentlichung über xurl, X-MCP oder ähnliche CLIs.

## Wann nutzen

- Anfragen passen zur Kategorie **Social: X / Twitter**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill xurl | Skill + CLI | Aus Recherche 2026-11-23 |
| ClawHub „Humanizer“ (biostartechnology) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Social: X / Twitter (content-marketing/social-x-twitter).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Recherche, Entwurf zeigen, erst nach Freigabe posten.
```

## Arbeitsablauf

- Recherche, Entwurf zeigen, erst nach Freigabe posten.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Automatisches Posten ohne Gate verletzt oft den gewuenschten Prozess und Plattformregeln.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Social: X / Twitter-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `social-x-twitter` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Social: X / Twitter. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Social: X / Twitter
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
