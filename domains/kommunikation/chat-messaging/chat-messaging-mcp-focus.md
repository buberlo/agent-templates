---
id: chat-messaging-mcp-focus
title: "Chat und Messaging: MCP/Skill-Fokus"
domain: kommunikation
category: chat-messaging
tags:
  - chat
  - kommunikation
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub „Slack“ (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "42.838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für Chat und Messaging"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Slack, Discord, Telegram, WhatsApp, iMessage – Nachrichten lesen und (freigegeben) senden.

## Wann nutzen

- Anfragen passen zur Kategorie **Chat und Messaging**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill imessage | Skill | Aus Recherche 2026-11-23 |
| ClawHub „Slack“ (steipete) | Skill | Aus Recherche 2026-11-23 |
| Grok Bot Slack-Plugin | Plugin | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Chat und Messaging (kommunikation/chat-messaging).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Lesen und Entwurf, Senden nach Freigabe.
```

## Arbeitsablauf

- Lesen und Entwurf, Senden nach Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- imessage-Skill ist macOS-spezifisch.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Chat und Messaging-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `chat-messaging` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Chat und Messaging. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Chat und Messaging
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
