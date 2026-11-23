---
id: grokbot-workflow
title: "Grok Bot"
domain: agent-platforms
category: grokbot
tags:
  - grokbot
  - agent-platforms
  - produktconnector
target_agents:
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Grok Bot Plugins / Custom MCP
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Connect Apps, Custom MCP HTTPS/Command; Wiki 0.75.x–0.77.x"
  - name: Grok Bot 101
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Gleiches Plugin-MCP-Modell wie Cursor"
inputs:
  - "Task-Beschreibung und gewünschte Tools"
  - "Bei Custom MCP: öffentliche HTTPS-URL oder Command auf der Bot-Box"
outputs:
  - "Ergebnis im Bot-Thread mit dokumentierten Tool-Policies"
  - "Liste blockierter/erlaubter Tools"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Grok Bot mit **Connect Apps** (kuratierte Plugins) oder **Custom MCP** betreiben: OAuth bleibt auf dem Connector-Backend, der Bot sieht keine Roh-Tokens. Custom-Server nur als öffentliches HTTPS oder als Command-Prozess auf dem Bot-Computer — nicht als localhost auf dem Laptop des Nutzers.

## Wann nutzen

- Aufgaben brauchen verbundene SaaS-Dienste über Connect Apps mit festen Tool-Policies (Always allow / Needs approval / Blocked).
- Du betreibst MCP-Logik auf der **Bot-Box** (npx/uvx) und akzeptierst, dass Shared-Bot-Teams Command und Args lesen können.
- **Wann nicht:** Wenn du einen MCP nur auf `127.0.0.1` am Entwicklerrechner hast (ohne öffentliches HTTPS oder Box-Command). Wenn du mehr als ~200 Skills aktivieren willst (Skill-Ceiling seit Wiki 0.71.2). Wenn Secrets sicher in Headern stecken müssen — Wiki nennt keinen verlässlichen Secret-Header-Weg für Custom MCP.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Connect Apps | Katalog-Plugins | OAuth auf Backend, Bot ohne Token |
| Custom MCP (HTTPS) | Remote-Server | Streamable HTTP/SSE, öffentlich erreichbar |
| Custom MCP (Command) | Box-Runtime | npx/uvx auf Bot-Maschine; argv ohne Secrets |
| @-Attach | Kontext | Skills/Plugins an Task hängen |
| Tool Policies | Risikosteuerung | Granular pro Tool (ab 0.70.2/1.2.3) |

## System-Prompt / Instruktionen

```text
Du arbeitest als Grok Bot mit Plugins und MCP. Nutze Connect Apps für Standard-Integrationen.
Custom MCP nur: öffentliches HTTPS oder Command auf der Bot-Box — nie Laptop-localhost, nie VPN-only ohne Reachability.
Keine Tokens, API-Keys oder Passwörter in Chat, Skill-Texten oder Command-Argumenten.
OAuth liegt auf dem Connector-Backend; fordere niemals Roh-Credentials vom Nutzer an.
Vor destruktiven Tools (write, send, delete, pay): Policy „Needs approval“ oder explizite Freigabe.
Einzelne Tools blocken, wenn die Aufgabe sie nicht braucht — weniger Schema-Noise.
Skill-Ceiling 200 beachten: nur relevante Skills @-attachieren.
Bei fehlendem Connector: Arbeit auf der Box (CLI/Dateien), nicht fingieren, ein privates MCP sei verbunden.
Shared Bot: alle Command-Zeilen als für Team-Leser sichtbar behandeln.
Nach Dokument-Erzeugung: Verify (Lesen/Render) wie in Document-Skills üblich.
```

## Arbeitsablauf

1. Connect Apps öffnen; Plugin wählen und Auth-Frist einhalten.
2. Task formulieren; passende Skills mit @ anhängen (unter 200-Skill-Decke bleiben).
3. Fehlende Integration: Custom MCP planen — HTTPS-Endpoint oder Box-Command, niemals lokaler Laptop-Host.
4. Tool-Policies setzen: kritische Tools auf Needs approval oder Blocked.
5. Bot-Task starten; Ausgaben protokollieren.
6. Vor Send/Write: Freigabe abwarten oder Policy-Dialog nutzen.
7. Bei Command-MCP: argv auf Secrets prüfen (Umgebungsvariablen auf Box, nicht in Args).
8. Ergebnis und Policy-Liste für Audit kurz dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Kein Custom MCP auf unerreichbarem localhost/VPN-only ohne dokumentierte Box-Alternative
- [ ] Tool-Policies passen zum Risiko (Writes nicht „Always allow“ ohne Grund)
- [ ] Keine Credentials in argv, Chat oder Skill-Dateien
- [ ] Nur angehängte Skills/Tools, die die Aufgabe braucht
- [ ] Dokument-Artefakte verifiziert (Lesen/Render)

## Sicherheit & Freigaben

- Connect Apps: Tokens nur auf Connector-Backend; Bot fordert keine Secrets in Klartext.
- Command-Server auf Shared Bots: Team kann Befehlszeile lesen — keine Keys in Args.
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach Freigabe oder Policy.

## Fallstricke

- **localhost-MCP:** User-Laptop-MCP ist für den Bot unsichtbar — stattdessen HTTPS oder Box-Command.
- **argv-Secrets:** Wiki verbietet Credentials in Command-Argumenten; Env auf der Box nutzen.
- **Skill-Ceiling 200:** Zu viele aktive Skills führen zu Verwirrung oder Abbruch — gezielt @-attachieren.
- **Shared-Bot-Sichtbarkeit:** Interne URLs oder Tokens in Command-Zeilen sind für Mitglieder lesbar.
- **Marketing-Threads:** Virale „N GitHub MCP“-Listen auf X ungeprüft übernehmen — nur Wiki/Connect Apps vertrauen.
- **Kein Secret-Header:** Custom MCP hat laut Wiki keinen sicheren Header-Geheimnis-Weg — Design entsprechend anpassen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Linear-Tickets lesen über Connect App
- **Input:** Connect App „Linear“ verbunden; Task „Offene Bugs der Woche listen“
- **Prompt:**
```text
@linear Nutze nur Lese-Tools. Keine Statusänderungen. Ausgabe als Markdown-Tabelle (ID, Titel, Status).
```
- **Erwartetes Ergebnis:**
```text
| ID | Titel | Status |
| LIN-101 | Login timeout | In Progress |
| LIN-104 | Footer link 404 | Todo |
(5 Zeilen, keine PATCH/POST ausgeführt)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Falscher Custom MCP (localhost auf Entwicklerrechner)
- **Input:** Nutzer schlägt `http://127.0.0.1:3847/mcp` auf dem MacBook vor
- **Prompt:**
```text
Verbinde meinen lokalen MCP unter localhost:3847.
```
- **Erwartetes Ergebnis:**
```text
Abbruch mit Begründung: Bot erreicht Laptop-localhost nicht.
Vorschlag: MCP auf Bot-Box als npx-Command starten ODER öffentliches HTTPS mit Auth am Server.
Kein Versuch, Token in argv zu setzen.
```