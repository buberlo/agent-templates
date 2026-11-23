---
id: desktop-automation-workflow
title: "Desktop-Automation"
domain: automatisierung
category: desktop-automation
tags:
  - desktop
  - automatisierung
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill computer-use
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub „Desktop Control“ (matagul)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "53.032 Downloads, 335 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für Desktop-Automation"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Computer-Use, OS-Automation, kontrollierte GUI-Steuerung.

## Wann nutzen

- Anfragen passen zur Kategorie **Desktop-Automation**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill computer-use | Skill | Aus Recherche 2026-11-23 |
| ClawHub „Desktop Control“ (matagul) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Desktop-Automation (automatisierung/desktop-automation).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Kleine, beobachtbare GUI-Schritte; bei Unklarheit stoppen.
```

## Arbeitsablauf

- Kleine, beobachtbare GUI-Schritte; bei Unklarheit stoppen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Desktop-Control hat weitreichende Rechte.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter 

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Desktop-Automation-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `desktop-automation` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Desktop-Automation. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Desktop-Automation
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
